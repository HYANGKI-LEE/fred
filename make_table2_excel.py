"""
Census M3 Table 2 (Value of Manufacturers' New Orders for Industry Groups) -> 엑셀
DB(output/db/us_macro_PBA_manufacturing.db)의 SA 시계열로 MoM / YoY 변동률 표 생성

    python make_table2_excel.py
    -> output/excel/M3_Table2_NewOrders_SA.xlsx

시트
    Tickers : Table 2 industry 행 순서대로 FRED 티커(SA/NSA), 제목, 최근값
    변동률   : C2 드롭다운으로 MoM / YoY 선택 (수식으로 Level_SA 참조)
    Level_SA : SA 원계열 (백만 달러)
"""
import sqlite3

from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

from util import make_dir

DB_PATH = './output/db/us_macro_PBA_manufacturing.db'
OUT_DIR = './output/excel'
OUT_PATH = f'{OUT_DIR}/M3_Table2_NewOrders_SA.xlsx'

# (Table 2 industry, 들여쓰기 수준, SA 티커, NSA 티커) - PDF 표 순서
ROWS = [
    ('All manufacturing industries', 0, 'AMTMNO', 'UMTMNO'),
    ('Excluding transportation', 1, 'AMXTNO', 'UMXTNO'),
    ('Excluding defense', 1, 'AMXDNO', 'UMXDNO'),
    ('With unfilled orders', 1, 'AMTUNO', 'UMTUNO'),
    ('Durable goods industries', 0, 'DGORDER', 'UMDMNO'),
    ('Primary metals', 1, 'A31SNO', 'U31SNO'),
    ('Iron and steel mills', 2, 'A31ANO', 'U31ANO'),
    ('Aluminum and nonferrous metals', 2, 'AANMNO', 'UANMNO'),
    ('Ferrous metal foundries', 2, 'A31CNO', 'U31CNO'),
    ('Fabricated metal products', 1, 'A32SNO', 'U32SNO'),
    ('Machinery', 1, 'A33SNO', 'U33SNO'),
    ('Construction machinery', 2, 'A33CNO', 'U33CNO'),
    ('Mining, oil field, and gas field machinery', 2, 'A33DNO', 'U33DNO'),
    ('Industrial machinery', 2, 'A33ENO', 'U33ENO'),
    ('Photographic equipment', 2, 'A33GNO', 'U33GNO'),
    ('Ventilation, heating, air-conditioning, and refrigeration equipment', 2, 'A33HNO', 'U33HNO'),
    ('Metalworking machinery', 2, 'A33INO', 'U33INO'),
    ('Turbines, generators, and other power transmission equipment', 2, 'ATGPNO', 'UTGPNO'),
    ('Material handling equipment', 2, 'A33MNO', 'U33MNO'),
    ('Computers and electronic products', 1, 'A34SNO', 'U34SNO'),
    ('Computers', 2, 'A34ANO', 'U34ANO'),
    ('Nondefense communications equipment', 2, 'A34DNO', 'U34DNO'),
    ('Defense communications equipment', 2, 'A34ENO', 'U34ENO'),
    ('Electronic components', 2, 'A34HNO', 'U34HNO'),
    ('Nondefense search and navigation equipment', 2, 'A34INO', 'U34INO'),
    ('Defense search and navigation equipment', 2, 'A34JNO', 'U34JNO'),
    ('Electromedical, measuring, and control instruments', 2, 'A34KNO', 'U34KNO'),
    ('Electrical equipment, appliances, and components', 1, 'A35SNO', 'U35SNO'),
    ('Electric lighting equipment', 2, 'A35ANO', 'U35ANO'),
    ('Household appliances', 2, 'A35BNO', 'U35BNO'),
    ('Electrical equipment', 2, 'A35CNO', 'U35CNO'),
    ('Transportation equipment', 1, 'A36SNO', 'U36SNO'),
    ('Motor vehicle bodies, parts, and trailers', 2, 'ABTPNO', 'UBTPNO'),
    ('Nondefense aircraft and parts', 2, 'ANAPNO', 'UNAPNO'),
    ('Defense aircraft and parts', 2, 'ADAPNO', 'UDAPNO'),
    ('Ships and boats', 2, 'A36ZNO', 'U36ZNO'),
    ('Furniture and related products', 1, 'A37SNO', 'U37SNO'),
    ('Nondurable goods industries', 0, 'AMNMNO', 'UMNMNO'),
]

FONT = 'Arial'
HEAD_FILL = PatternFill('solid', fgColor='DCE6F1')
INPUT_FILL = PatternFill('solid', fgColor='FFFF00')
THIN = Side(style='thin', color='A6A6A6')
FIRST_ROW = 5  # 표 데이터 시작 행 (1~4행: 제목, 선택, 안내, 헤더)


def f(bold=False, color='000000', size=10, italic=False):
    return Font(name=FONT, bold=bold, color=color, size=size, italic=italic)


def industry_cell(ws, row, name, level):
    c = ws.cell(row, 1, name)
    c.font = f(bold=level == 0)
    c.alignment = Alignment(indent=level * 2)


def main():
    con = sqlite3.connect(f'file:{DB_PATH}?mode=ro', uri=True)
    tickers = [r[2] for r in ROWS]
    q = ','.join('?' * len(tickers))
    info = {r[0]: r[1:] for r in con.execute(
        f'SELECT series_id, title, units, seasonal_adjustment, last_updated FROM series_info WHERE series_id IN ({q})',
        tickers)}
    obs = {}
    for sid, date, value in con.execute(f'SELECT series_id, date, value FROM obs_monthly WHERE series_id IN ({q})', tickers):
        obs[(sid, date)] = value
    con.close()
    missing = [t for t in tickers if t not in info]
    if missing:
        raise SystemExit(f'DB에 없는 티커: {missing}')
    dates = sorted({d for _, d in obs}, reverse=True)  # PDF 표처럼 최신 월이 왼쪽

    wb = Workbook()

    # ---------------- 변동률 ----------------
    ws = wb.active
    ws.title = '변동률'
    ws['A1'] = "Value of Manufacturers' New Orders for Industry Groups - Seasonally Adjusted, Monthly Percent Change"
    ws['A1'].font = f(bold=True, size=12)
    ws['A2'] = '기준 선택 (MoM / YoY) ▶'
    ws['A2'].font = f(bold=True)
    ws['A2'].alignment = Alignment(horizontal='right')
    ws['B2'] = 'MoM'
    ws['B2'].font = f(bold=True, color='0000FF', size=11)
    ws['B2'].fill = INPUT_FILL
    ws['B2'].alignment = Alignment(horizontal='center')
    ws['B2'].border = Border(THIN, THIN, THIN, THIN)
    dv = DataValidation(type='list', formula1='"MoM,YoY"', allow_blank=False,
                        showErrorMessage=True, errorTitle='선택', error='MoM 또는 YoY만 선택할 수 있습니다.')
    ws.add_data_validation(dv)
    dv.add('B2')
    ws['B2'].comment = Comment('노란 셀 드롭다운에서 MoM(전월 대비) / YoY(전년 동월 대비)를 고르면 표 전체가 바뀝니다.', 'fred')
    ws['C2'] = '=IF($B$2="YoY","전년 동월 대비 변동률 (%)","전월 대비 변동률 (%)")'
    ws['C2'].font = f(italic=True)
    ws['A3'] = ('Source: FRED (U.S. Census Bureau M3 Survey) via fred DB. 원계열은 Level_SA 시트. '
                'Computers and electronic products 등은 Census 기준대로 반도체 제외.')
    ws['A3'].font = f(italic=True, color='595959', size=9)

    hdr = FIRST_ROW - 1
    ws.cell(hdr, 1, 'Industry')
    ws.cell(hdr, 2, 'Ticker (SA)')
    for j, d in enumerate(dates):
        ws.cell(hdr, 3 + j, d[:7])
    for c in ws[hdr]:
        c.font = f(bold=True)
        c.fill = HEAD_FILL
        c.alignment = Alignment(horizontal='center')
        c.border = Border(bottom=THIN)

    last_col = 2 + len(dates)
    for i, (name, level, sa, _) in enumerate(ROWS):
        r = FIRST_ROW + i
        industry_cell(ws, r, name, level)
        ws.cell(r, 2, sa).font = f(color='595959')
        for j in range(len(dates)):
            col = 3 + j
            cur = f'Level_SA!{get_column_letter(col)}{r}'
            prev = f'Level_SA!{get_column_letter(col + 1)}{r}' if col + 1 <= last_col else None
            yago = f'Level_SA!{get_column_letter(col + 12)}{r}' if col + 12 <= last_col else None
            mom = f'IF(OR({cur}="",{prev}="",{prev}=0),"",{cur}/{prev}-1)' if prev else '""'
            yoy = f'IF(OR({cur}="",{yago}="",{yago}=0),"",{cur}/{yago}-1)' if yago else '""'
            c = ws.cell(r, col, f'=IF($B$2="YoY",{yoy},{mom})')
            c.number_format = '0.0%;[Red]-0.0%;0.0%'
            c.font = f(bold=level == 0)

    # ---------------- Level_SA ----------------
    wl = wb.create_sheet('Level_SA')
    wl['A1'] = "Value of Manufacturers' New Orders - Seasonally Adjusted (Millions of Dollars)"
    wl['A1'].font = f(bold=True, size=12)
    wl['A3'] = 'Source: FRED series/observations (U.S. Census Bureau M3), fred DB에서 생성. 값은 원자료(하드코딩).'
    wl['A3'].font = f(italic=True, color='595959', size=9)
    wl.cell(hdr, 1, 'Industry')
    wl.cell(hdr, 2, 'Ticker (SA)')
    for j, d in enumerate(dates):
        wl.cell(hdr, 3 + j, d[:7])
    for c in wl[hdr]:
        c.font = f(bold=True)
        c.fill = HEAD_FILL
        c.alignment = Alignment(horizontal='center')
        c.border = Border(bottom=THIN)
    for i, (name, level, sa, _) in enumerate(ROWS):
        r = FIRST_ROW + i
        industry_cell(wl, r, name, level)
        wl.cell(r, 2, sa).font = f(color='595959')
        for j, d in enumerate(dates):
            v = obs.get((sa, d))
            if v is not None:
                c = wl.cell(r, 3 + j, v)
                c.number_format = '#,##0'
                c.font = f(color='0000FF', bold=level == 0)

    # ---------------- Tickers ----------------
    wt = wb.create_sheet('Tickers', 0)
    wt['A1'] = "Census M3 Table 2 - Industry별 FRED 티커"
    wt['A1'].font = f(bold=True, size=12)
    wt['A2'] = ('Table 2: Value of Manufacturers\' New Orders for Industry Groups (M3 Full Report). '
                'SA = Seasonally Adjusted, NSA = Not Seasonally Adjusted.')
    wt['A2'].font = f(italic=True, color='595959', size=9)
    heads = ['Industry', 'Level', 'FRED Ticker (SA)', 'FRED Ticker (NSA)', 'FRED Title', 'Units',
             'Latest Month', 'Latest Value (SA)', 'FRED Last Updated', 'FRED URL (SA)']
    for k, h in enumerate(heads, 1):
        c = wt.cell(hdr, k, h)
        c.font = f(bold=True)
        c.fill = HEAD_FILL
        c.border = Border(bottom=THIN)
    for i, (name, level, sa, nsa) in enumerate(ROWS):
        r = FIRST_ROW + i
        title, units, _, updated = info[sa]
        latest = next(d for d in dates if (sa, d) in obs)
        industry_cell(wt, r, name, level)
        vals = [level, sa, nsa, title, units, latest[:7], obs[(sa, latest)], updated,
                f'https://fred.stlouisfed.org/series/{sa}']
        for k, v in enumerate(vals, 2):
            c = wt.cell(r, k, v)
            c.font = f()
        wt.cell(r, 8).number_format = '#,##0'
        wt.cell(r, 10).hyperlink = f'https://fred.stlouisfed.org/series/{sa}'
        wt.cell(r, 10).font = f(color='0563C1')

    for sheet, widths in [(ws, {'A': 58, 'B': 13}), (wl, {'A': 58, 'B': 13}),
                          (wt, {'A': 58, 'B': 7, 'C': 16, 'D': 17, 'E': 70, 'F': 20, 'G': 12, 'H': 16, 'I': 22, 'J': 42})]:
        for col, w in widths.items():
            sheet.column_dimensions[col].width = w
        if sheet is not wt:
            for j in range(len(dates)):
                sheet.column_dimensions[get_column_letter(3 + j)].width = 9.5
        sheet.freeze_panes = sheet.cell(FIRST_ROW, 3)
        sheet.sheet_view.showGridLines = sheet is not ws

    wb.active = 1
    make_dir(OUT_DIR)
    wb.save(OUT_PATH)
    print(f'>>> {OUT_PATH} : {len(ROWS)} industries x {len(dates)} months ({dates[-1][:7]} ~ {dates[0][:7]})')


if __name__ == '__main__':
    main()
