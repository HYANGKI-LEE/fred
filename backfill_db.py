"""
FRED가 최근 구간만 주는 시리즈의 과거값을 다른 DB(와이드 market 테이블)에서 채운다.
FRED 첫 날짜 이전 구간만 넣고, 겹치는 구간은 FRED 값을 그대로 둔다.
build_db.py는 다시 받을 때 FRED 첫 날짜 이전 값을 지우지 않으므로 한 번 채우면 유지된다.

    python backfill_db.py --ids us_macro_MBF_financial_indicator --series SP500 \
        --source-db ../TradingCheckboard/data/market.db --source-col "주가__S&P 500-현재가"

일별 원천이 주말·휴일을 전일값으로 채워 둔 경우(인포맥스 market.db)를 위해
주말과 '전일과 값이 같은 평일'(휴일)은 기본으로 뺀다 (--keep-repeats 로 끌 수 있음).

기록: backfill 테이블 (series_id, source, date_from, date_to, n_rows, filled_at)
"""
import importlib
import os
import sqlite3
from argparse import ArgumentParser
from datetime import date, datetime


def main():
    parser = ArgumentParser(description='과거값 채우기')
    parser.add_argument('--ids', required=True, help='mySeriesIds 안의 모듈 이름 (DB 경로 결정)')
    parser.add_argument('--series', required=True, help='채울 FRED series_id')
    parser.add_argument('--source-db', required=True, help='원천 SQLite (market 테이블, date + 칼럼)')
    parser.add_argument('--source-col', required=True, help='원천 칼럼 이름')
    parser.add_argument('--keep-repeats', action='store_true', help='주말·휴일(전일 반복값)도 넣기')
    args = parser.parse_args()

    module = importlib.import_module(f'mySeriesIds.{args.ids}')
    db_path = f'./output/db/{module.dir}.db'
    con = sqlite3.connect(db_path)
    row = con.execute('SELECT list_name FROM series_info WHERE series_id=? AND status=?', (args.series, 'ok')).fetchone()
    if not row:
        raise SystemExit(f'{args.series}: {db_path} 에 아직 받은 값이 없어요. build_db.py 를 먼저 돌려주세요.')
    freq = row[0][4:]
    table = {'D': 'obs_daily', 'W': 'obs_weekly', 'M': 'obs_monthly', 'Q': 'obs_quarterly', 'Y': 'obs_annual'}[freq]
    first = con.execute(f'SELECT MIN(date) FROM {table} WHERE series_id=? AND date >= ('
                        'SELECT observation_start FROM series_info WHERE series_id=?)', (args.series, args.series)).fetchone()[0]

    src = sqlite3.connect(f'file:{args.source_db}?mode=ro', uri=True)
    col = args.source_col.replace('"', '""')
    rows = src.execute(f'SELECT date, "{col}" FROM market WHERE "{col}" IS NOT NULL ORDER BY date').fetchall()
    src.close()

    picked, prev = [], None
    for d, v in rows:
        repeat = v == prev
        prev = v
        if d >= first:
            break
        if not args.keep_repeats and (date.fromisoformat(d).weekday() >= 5 or repeat):
            continue
        picked.append((args.series, d, v))

    con.execute(f'DELETE FROM {table} WHERE series_id=? AND date<?', (args.series, first))
    con.executemany(f'INSERT INTO {table} VALUES (?,?,?)', picked)
    con.execute('''CREATE TABLE IF NOT EXISTS backfill (
        series_id TEXT PRIMARY KEY, source TEXT, date_from TEXT, date_to TEXT, n_rows INTEGER, filled_at TEXT)''')
    if picked:
        con.execute('INSERT OR REPLACE INTO backfill VALUES (?,?,?,?,?,?)', (
            args.series, f'{os.path.basename(args.source_db)}:{args.source_col}', picked[0][1], picked[-1][1],
            len(picked), datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    con.commit()
    con.close()
    print(f'>>> {args.series} ({table}) : FRED 시작 {first} 이전 {len(picked)}행 채움'
          + (f' ({picked[0][1]} ~ {picked[-1][1]})' if picked else ''))


if __name__ == '__main__':
    main()
