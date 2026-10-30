# FRED > NIPA Table 1.10. Gross Domestic Income by Type of Income (release 53, element 17636)
# https://fred.stlouisfed.org/release/tables?rid=53&eid=17636  표의 분기 시리즈 전체 (macro-dashboard GDP > GDI 탭)
# 다른 NIPA 리스트에 이미 있는 줄(임금·급여 등)도 표 하나를 이 DB에서 다 읽도록 같이 넣음
# 위계: # 표 > ## 단위 (계절조정)
dir='us_macro_NIPA_GDI'

# Quarterly (24)
ids_Q = [
    # Table 1.10 (24)
    ## Bil. of $ (SAAR)
    'GDI', # Gross domestic income
    'GDICOMP', # Compensation of employees, paid
    'A4102C1Q027SBEA', # Wages and salaries
    'W270RC1Q027SBEA', # To persons
    'B4189C1Q027SBEA', # To the rest of the world
    'A038RC1Q027SBEA', # Supplements to wages and salaries
    'GDITAXES', # Taxes on production and imports
    'GDISUBS', # Less: Subsidies
    'GDINOS', # Net operating surplus
    'W260RC1Q027SBEA', # Private enterprises
    'W272RC1Q027SBEA', # Net interest and miscellaneous payments, domestic industries
    'B029RC1Q027SBEA', # Business current transfer payments (net)
    'PROPINC', # Proprietors' income with inventory valuation and capital consumption adjustments
    'RENTIN', # Rental income of persons with capital consumption adjustment
    'A445RC1Q027SBEA', # Corporate profits with IVA and CCAdj, domestic industries
    'A054RC1Q027SBEA', # Taxes on corporate income
    'W273RC1Q027SBEA', # Profits after tax with IVA and CCAdj
    'A449RC1Q027SBEA', # Net dividends
    'W274RC1Q027SBEA', # Undistributed corporate profits with IVA and CCAdj
    'A108RC1Q027SBEA', # Current surplus of government enterprises
    'COFC', # Consumption of fixed capital
    'A024RC1Q027SBEA', # Private
    'A264RC1Q027SBEA', # Government
    'A030RC1Q027SBEA', # Statistical discrepancy

]
