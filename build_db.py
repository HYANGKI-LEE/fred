"""
mySeriesIds 리스트 -> SQLite DB (output/db/<dir>.db)

    python build_db.py --ids us_macro_PBA_manufacturing
    python build_db.py --ids us_macro_PBA_manufacturing --limit 20   # 앞 20개만 테스트
    python build_db.py --ids us_macro_PBA_manufacturing --force      # 전부 다시 받기

테이블
    series_info     : 시리즈 메타데이터 + 주석 위계(group_path) + 수집 상태(status, error)
    obs_monthly 등  : (series_id, date, value) 세로형. ids_D -> obs_daily, ids_W -> obs_weekly,
                      ids_M -> obs_monthly, ids_Q -> obs_quarterly, ids_Y -> obs_annual

에러 대비
    - FRED 호출 제한(분당 120회)보다 느리게 호출
    - 429 / 5xx / 타임아웃은 대기 후 재시도, 잘못된 ID(400)는 기록하고 건너뜀
    - 시리즈 하나 끝날 때마다 커밋 -> 중간에 끊겨도 다시 실행하면 이어서 진행
    - 이미 받은 시리즈는 FRED last_updated가 바뀌었을 때만 관측값을 다시 받음
    - 다시 받을 때 FRED 첫 날짜 이전 값은 지우지 않음 (backfill_db.py로 채운 과거값 보존)

빠른 업데이트
    리스트 모듈에 category_ids = [32429] 처럼 적어두면 그 카테고리(하위 포함)의 메타데이터를
    1,000개씩 한 번에 받아 바뀐 시리즈만 골라냄. 카테고리 밖 시리즈는 하나씩 조회.
"""
import importlib
import inspect
import os
import re
import sqlite3
import time
import warnings
from argparse import ArgumentParser
from datetime import datetime

import requests
from urllib3.exceptions import InsecureRequestWarning

from config import user_agent, myAPIkey
from util import make_dir

warnings.filterwarnings("ignore", category=InsecureRequestWarning)

BASE_URL = 'https://api.stlouisfed.org/fred/'
MIN_INTERVAL = 0.6          # 초. 분당 최대 100회
RETRY_WAITS = [20, 40, 60, 120, 180]
TABLES = {'D': 'obs_daily', 'W': 'obs_weekly', 'M': 'obs_monthly', 'Q': 'obs_quarterly', 'Y': 'obs_annual', 'A': 'obs_annual'}


class BadSeries(Exception):
    pass


class Fred:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers['User-Agent'] = user_agent
        self.last_call = 0.0

    def get(self, path, **params):
        params.update(api_key=myAPIkey, file_type='json')
        for wait in RETRY_WAITS + [None]:
            time.sleep(max(0.0, MIN_INTERVAL - (time.time() - self.last_call)))
            self.last_call = time.time()
            try:
                r = self.session.get(BASE_URL + path, params=params, timeout=60, verify=False)
            except requests.RequestException as e:
                reason = type(e).__name__
            else:
                if r.status_code == 200:
                    return r.json()
                if r.status_code in (400, 404):
                    try:
                        msg = r.json().get('error_message', r.text)
                    except ValueError:
                        msg = r.text
                    raise BadSeries(f'{r.status_code}: {msg[:200]}')
                reason = f'HTTP {r.status_code}'
            if wait is None:
                raise RuntimeError(f'재시도 초과 ({reason})')
            print(f'    ! {reason} -> {wait}초 후 재시도')
            time.sleep(wait)


def bulk_meta(fred, category_ids):
    """카테고리(하위 카테고리 포함) 시리즈 메타데이터를 한 번에 수집 -> {series_id: info}"""
    meta, todo, done = {}, list(category_ids), set()
    while todo:
        cid = todo.pop()
        if cid in done:
            continue
        done.add(cid)
        todo += [c['id'] for c in fred.get('category/children', category_id=cid)['categories']]
        offset = 0
        while True:
            r = fred.get('category/series', category_id=cid, limit=1000, offset=offset)
            meta.update({s['id']: s for s in r['seriess']})
            offset += 1000
            if offset >= r['count']:
                break
    print(f'>>> 카테고리 {len(done)}개에서 메타데이터 {len(meta)}개 일괄 수집')
    return meta


def group_paths(module):
    """리스트 안의 #, ##, ### 주석을 시리즈별 위계 문자열로 변환"""
    paths, heads = {}, {}
    for line in inspect.getsource(module).splitlines():
        s = line.strip()
        m = re.match(r'^(#{1,3}) (.+)$', s)
        if m:
            level = len(m.group(1))
            heads = {k: v for k, v in heads.items() if k < level}
            heads[level] = m.group(2).strip()
            continue
        m = re.match(r"^'([^']+)'", s)
        if m:
            paths.setdefault(m.group(1), ' > '.join(heads[k] for k in sorted(heads)))
        elif re.match(r'^\w+ = \[', s):
            heads = {}
    return paths


def setup_db(con, tables):
    con.execute('''CREATE TABLE IF NOT EXISTS series_info (
        series_id TEXT PRIMARY KEY, list_name TEXT, group_path TEXT, title TEXT,
        frequency TEXT, units TEXT, seasonal_adjustment TEXT,
        observation_start TEXT, observation_end TEXT, last_updated TEXT,
        n_obs INTEGER, fetched_at TEXT, status TEXT, error TEXT)''')
    for t in tables:
        con.execute(f'''CREATE TABLE IF NOT EXISTS {t} (
            series_id TEXT, date TEXT, value REAL, PRIMARY KEY (series_id, date)) WITHOUT ROWID''')
    con.commit()


def to_float(v):
    try:
        return float(v)
    except ValueError:
        return None  # FRED 결측값 '.'


def main():
    parser = ArgumentParser(description='fred -> sqlite')
    parser.add_argument('--ids', required=True, help='mySeriesIds 안의 모듈 이름')
    parser.add_argument('--limit', type=int, help='리스트별 앞 N개만 (테스트용)')
    parser.add_argument('--force', action='store_true', help='last_updated와 관계없이 전부 다시 받기')
    args = parser.parse_args()

    module = importlib.import_module(f'mySeriesIds.{args.ids}')
    jobs = []
    for name, ids in vars(module).items():
        if name.startswith('ids_') and isinstance(ids, list):
            freq = name[4:]
            table = TABLES.get(freq, f'obs_{freq.lower()}')
            jobs += [(sid, name, table) for sid in (ids[:args.limit] if args.limit else ids) if sid]
    paths = group_paths(module)

    db_dir = './output/db'
    make_dir(db_dir)
    db_path = f'{db_dir}/{module.dir}.db'
    con = sqlite3.connect(db_path)
    setup_db(con, sorted({t for _, _, t in jobs}))
    stored = {r[0]: r[1:] for r in con.execute('SELECT series_id, last_updated, status, fetched_at FROM series_info')}

    fred = Fred()
    started = time.time()
    bulk = bulk_meta(fred, getattr(module, 'category_ids', []))
    today = datetime.now().strftime('%Y-%m-%d')
    stats = {'new/updated': 0, 'unchanged': 0, 'skipped(today)': 0, 'error': 0}
    print(f'>>> {db_path} : {len(jobs)} series')

    for i, (sid, list_name, table) in enumerate(jobs, 1):
        prev = stored.get(sid)
        if prev and prev[1] == 'ok' and (prev[2] or '').startswith(today) and not args.force:
            stats['skipped(today)'] += 1
            continue
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            info = bulk.get(sid) or fred.get('series', series_id=sid)['seriess'][0]
            meta = (sid, list_name, paths.get(sid, ''), info['title'], info['frequency_short'],
                    info['units'], info['seasonal_adjustment_short'], info['observation_start'],
                    info['observation_end'], info['last_updated'])
            if prev and prev[1] == 'ok' and prev[0] == info['last_updated'] and not args.force:
                con.execute('UPDATE series_info SET fetched_at=? WHERE series_id=?', (now, sid))
                stats['unchanged'] += 1
            else:
                obs = fred.get('series/observations', series_id=sid)['observations']
                rows = [(sid, o['date'], to_float(o['value'])) for o in obs]
                rows = [r for r in rows if r[2] is not None]
                if rows:
                    # FRED 첫 날짜 이전 값(backfill_db.py로 다른 소스에서 채운 과거값)은 남김
                    con.execute(f'DELETE FROM {table} WHERE series_id=? AND date>=?', (sid, rows[0][1]))
                con.executemany(f'INSERT INTO {table} VALUES (?,?,?)', rows)
                con.execute('INSERT OR REPLACE INTO series_info VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                            meta + (len(rows), now, 'ok', None))
                stats['new/updated'] += 1
        except (BadSeries, RuntimeError, KeyError, IndexError, ValueError) as e:
            con.execute('''INSERT INTO series_info (series_id, list_name, group_path, fetched_at, status, error)
                           VALUES (?,?,?,?,?,?) ON CONFLICT(series_id) DO UPDATE SET
                           fetched_at=excluded.fetched_at, status=excluded.status, error=excluded.error''',
                        (sid, list_name, paths.get(sid, ''), now, 'error', str(e)))
            stats['error'] += 1
            print(f'    x {sid}: {e}')
        con.commit()
        if i % 50 == 0 or i == len(jobs):
            mins = (time.time() - started) / 60
            print(f'  {i}/{len(jobs)} ({mins:.1f}분) {stats}')

    con.close()
    print(f'>>> 완료 ({(time.time() - started) / 60:.1f}분) {stats}')
    if stats['error']:
        print("    에러 목록: SELECT series_id, error FROM series_info WHERE status='error'")


if __name__ == '__main__':
    main()
