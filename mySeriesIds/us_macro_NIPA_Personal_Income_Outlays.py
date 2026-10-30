# FRED > National Accounts > National Income & Product Accounts > Personal Income & Outlays (category_id 110)
# https://fred.stlouisfed.org/categories/110  하위 카테고리 + 직속 시리즈 전체. 주기는 FRED 메타데이터 기준
# 위계: # 카테고리 > ## 단위 (계절조정)
dir='us_macro_NIPA_Personal_Income_Outlays'
category_ids = [110]  # build_db.py가 이 카테고리(하위 포함) 메타데이터를 일괄 조회

# Monthly (107)
ids_M = [
    # Personal Income & Outlays (47)
    ## $ (SAAR)
    'A229RC0', # Disposable Personal Income: Per capita: Current dollars
    ## Bil. of $ (SAAR)
    'A038RC1', # Compensation of Employees, Received: Supplements to Wages and Salaries
    'A576RC1', # Compensation of Employees, Received: Wage and Salary Disbursements
    'A132RC1', # Compensation of Employees, Received: Wage and Salary Disbursements: Private Industries
    'W209RC1', # Compensation of employees, received
    'B202RC1', # Compensation of employees, received: Wage and salary disbursements: Government
    'A061RC1', # Contributions for government social insurance, domestic
    'DSPI', # Disposable Personal Income
    'B223RC1', # Government unemployment insurance benefits (DISCONTINUED)
    'B222RC1', # Old-age, survivors, disability, and health insurance benefits (DISCONTINUED)
    'W236RC1', # Other (DISCONTINUED)
    'PCE', # Personal Consumption Expenditures
    'PCEDG', # Personal Consumption Expenditures: Durable Goods
    'DGDSRC1', # Personal Consumption Expenditures: Goods
    'PCEND', # Personal Consumption Expenditures: Nondurable Goods
    'PCES', # Personal Consumption Expenditures: Services
    'PCTR', # Personal Current Transfer Receipts
    'PI', # Personal Income
    'PIROA', # Personal Income Receipts on Assets
    'PDI', # Personal Income Receipts on Assets: Personal Dividend Income
    'PII', # Personal Income Receipts on Assets: Personal Interest Income
    'W055RC1', # Personal current taxes
    'W211RC1', # Personal current transfer payments
    'W062RC1M027SBEA', # Personal current transfer payments: to government
    'A063RC1', # Personal current transfer receipts: Government social benefits to persons
    'W729RC1', # Personal current transfer receipts: Government social benefits to persons: Medicaid
    'W824RC1', # Personal current transfer receipts: Government social benefits to persons: Medicare
    'W827RC1', # Personal current transfer receipts: Government social benefits to persons: Other
    'W823RC1', # Personal current transfer receipts: Government social benefits to persons: Social security
    'W825RC1', # Personal current transfer receipts: Government social benefits to persons: Unemployment insurance
    'W826RC1', # Personal current transfer receipts: Government social benefits to persons: Veterans' benefits
    'B931RC1', # Personal current transfer receipts: Other current transfer receipts, from business (net)
    'B069RC1', # Personal interest payments
    'A068RC1', # Personal outlays
    'A041RC1', # Proprietors' income with inventory valuation and capital consumption adjustments
    'B042RC1', # Proprietors' income with inventory valuation and capital consumption adjustments: Farm
    'A045RC1', # Proprietors' income with inventory valuation and capital consumption adjustments: Nonfarm
    'A048RC1', # Rental income of persons with capital consumption adjustment
    ## Bil. of Chn. 2017 $ (SAAR)
    'DSPIC96', # Real Disposable Personal Income
    'PCEC96', # Real Personal Consumption Expenditures
    'PCEDGC96', # Real Personal Consumption Expenditures: Durable Goods
    'DGDSRX1', # Real Personal Consumption Expenditures: Goods
    'PCENDC96', # Real Personal Consumption Expenditures: Nondurable Goods
    'PCESC96', # Real Personal Consumption Expenditures: Services
    'RPI', # Real Personal Income
    'W875RX1', # Real personal income excluding current transfer receipts
    ## Chn. 2017 $ (SAAR)
    'A229RX0', # Real Disposable Personal Income: Per Capita

    # Personal Income & Outlays > Employer Contributions (2)
    ## Bil. of $ (SAAR)
    'B040RC1M027SBEA', # Compensation of employees: Supplements to wages and salaries: Employer contributions for employee pension and insurance funds
    'B039RC1M027SBEA', # Compensation of employees: Supplements to wages and salaries: Employer contributions for government social insurance

    # Personal Income & Outlays > Personal Consumption Expenditures (58)
    ## % Chg. from Preceding Period (SA)
    'DPCERV1M225SBEA', # Personal consumption expenditures (chain-type price index) (DISCONTINUED)
    'DPCCRV1M225SBEA', # Personal consumption expenditures excluding food and energy (chain-type price index) (DISCONTINUED)
    'DNRGRV1M225SBEA', # Personal consumption expenditures: Energy goods and services (chain-type price index) (DISCONTINUED)
    'DFXARV1M225SBEA', # Personal consumption expenditures: Food (chain-type price index) (DISCONTINUED)
    'DGDSRV1M225SBEA', # Personal consumption expenditures: Goods (chain-type price index) (DISCONTINUED)
    'DDURRV1M225SBEA', # Personal consumption expenditures: Goods: Durable goods (chain-type price index) (DISCONTINUED)
    'DNDGRV1M225SBEA', # Personal consumption expenditures: Goods: Nondurable goods (chain-type price index) (DISCONTINUED)
    'DSERRV1M225SBEA', # Personal consumption expenditures: Services (chain-type price index) (DISCONTINUED)
    'DPCMRV1M225SBEA', # Personal market-based PCE (chain-type price index) (DISCONTINUED)
    'DPCXRV1M225SBEA', # Personal market-based PCE excluding food and energy (chain-type price index) (DISCONTINUED)
    'DPCERGM1M225SBEA', # Prices for Personal Consumption Expenditures: Chained Price Index
    'DNRGRGM1M225SBEA', # Prices for Personal Consumption Expenditures: Chained Price Index: Energy goods and services
    'DFXARGM1M225SBEA', # Prices for Personal Consumption Expenditures: Chained Price Index: Food
    'DGDSRGM1M225SBEA', # Prices for Personal Consumption Expenditures: Chained Price Index: Goods
    'DDURRGM1M225SBEA', # Prices for Personal Consumption Expenditures: Chained Price Index: Goods: Durable goods
    'DNDGRGM1M225SBEA', # Prices for Personal Consumption Expenditures: Chained Price Index: Goods: Nondurable goods
    'DPCMRGM1M225SBEA', # Prices for Personal Consumption Expenditures: Chained Price Index: Market-based PCE
    'DPCXRGM1M225SBEA', # Prices for Personal Consumption Expenditures: Chained Price Index: Market-based PCE excluding food and energy
    'PP001176M', # Prices for Personal Consumption Expenditures: Chained Price Index: PCE Excluding Food, Energy, and Housing
    'DPCCRGM1M225SBEA', # Prices for Personal Consumption Expenditures: Chained Price Index: PCE excluding food and energy
    'PP001260M', # Prices for Personal Consumption Expenditures: Chained Price Index: PCE: Services Excluding Energy and Housing
    'DSERRGM1M225SBEA', # Prices for Personal Consumption Expenditures: Chained Price Index: Services
    'DPCERAM1M225NBEA', # Real Personal Consumption Expenditures
    'DNRGRAM1M225NBEA', # Real Personal Consumption Expenditures: Energy goods and services
    'DFXARAM1M225NBEA', # Real Personal Consumption Expenditures: Food
    'DGDSRAM1M225NBEA', # Real Personal Consumption Expenditures: Goods
    'DDURRAM1M225NBEA', # Real Personal Consumption Expenditures: Goods: Durable goods
    'DNDGRAM1M225NBEA', # Real Personal Consumption Expenditures: Goods: Nondurable goods
    'DPCMRAM1M225NBEA', # Real Personal Consumption Expenditures: Market-based PCE
    'DPCXRAM1M225NBEA', # Real Personal Consumption Expenditures: Market-based PCE excluding food and energy
    'PQ001176M', # Real Personal Consumption Expenditures: PCE Excluding Food, Energy, and Housing
    'DPCCRAM1M225NBEA', # Real Personal Consumption Expenditures: PCE excluding food and energy
    'PQ001260M', # Real Personal Consumption Expenditures: PCE: Services Excluding Energy and Housing
    'DSERRAM1M225NBEA', # Real Personal Consumption Expenditures: Services
    'DPCMRL1M225NBEA', # Real market-based PCE (DISCONTINUED)
    'DPCXRL1M225NBEA', # Real market-based PCE excluding food and energy (DISCONTINUED)
    'DPCERL1M225NBEA', # Real personal consumption expenditures (DISCONTINUED)
    'DPCCRL1M225NBEA', # Real personal consumption expenditures excluding food and energy (DISCONTINUED)
    'DNRGRL1M225NBEA', # Real personal consumption expenditures: Energy goods and services (DISCONTINUED)
    'DFXARL1M225NBEA', # Real personal consumption expenditures: Food (DISCONTINUED)
    'DGDSRL1M225NBEA', # Real personal consumption expenditures: Goods (DISCONTINUED)
    'DDURRL1M225NBEA', # Real personal consumption expenditures: Goods: Durable goods (DISCONTINUED)
    'DNDGRL1M225NBEA', # Real personal consumption expenditures: Goods: Nondurable goods (DISCONTINUED)
    'DSERRL1M225NBEA', # Real personal consumption expenditures: Services (DISCONTINUED)
    ## Bil. of $ (SAAR)
    'DPCCRC1M027SBEA', # Personal consumption expenditures excluding food and energy
    'DNRGRC1M027SBEA', # Personal consumption expenditures: Energy goods and services
    'DFXARC1M027SBEA', # Personal consumption expenditures: Food
    'DPCMRC1M027SBEA', # Personal consumption expenditures: Market-based
    'DPCXRC1M027SBEA', # Personal consumption expenditures: Market-based PCE excluding food and energy
    ## Bil. of Chn. 2017 $ (SAAR)
    'DPCCRX1M020SBEA', # Real personal consumption expenditures excluding food and energy
    'DNRGRX1M020SBEA', # Real personal consumption expenditures: Energy goods and services
    'DFXARX1M020SBEA', # Real personal consumption expenditures: Food
    'DPCMRX1M020SBEA', # Real personal consumption expenditures: Market-based
    'DPCXRX1M020SBEA', # Real personal consumption expenditures: Market-based PCE excluding food and energy
    ## Mil. of $ (SAAR)
    'LA001176M', # Personal Consumption Expenditures Excluding Food, Energy, and Housing
    'LA001260M', # Personal Consumption Expenditures: Services Excluding Energy and Housing
    ## Mil. of Chn. 2017 $ (SAAR)
    'LB001176M', # Real Personal Consumption Expenditures Excluding Food, Energy, and Housing
    'LB001260M', # Real Personal Consumption Expenditures: Services Excluding Energy and Housing

]

# Quarterly (343)
ids_Q = [
    # Personal Income & Outlays (47)
    ## $ (SAAR)
    'A229RC0Q052SBEA', # Disposable personal income: Per capita
    'A792RC0Q052SBEA', # Personal income per capita
    ## % (SAAR)
    'A072RC1Q156SBEA', # Personal saving as a percentage of disposable personal income
    ## % Chg. from Preceding Period (SAAR)
    'A067RP1Q027SBEA', # Disposable Personal Income
    'A067RL1Q156SBEA', # Real Disposable Personal Income
    ## % Chg. from Qtr.  1 Yr. Ago (SA)
    'A067RO1Q156NBEA', # Real Disposable Personal Income
    ## Bil. of $ (NSA)
    'L318151Q027NBEA', # Federal government cash receipts from the public: Timing differences: Withheld personal income tax and social security contributions (DISCONTINUED)
    'M318151Q027NBEA', # Federal government receipts: Timing differences: Withheld personal income tax and social security contributions (NIPA vs. Budget)
    ## Bil. of $ (SAAR)
    'A132RC1Q027SBEA', # Compensation of employees: Wages and salaries: Private industries
    'DPI', # Disposable Personal Income
    'PCEC', # Personal Consumption Expenditures
    'PCDG', # Personal Consumption Expenditures: Durable Goods
    'PCND', # Personal Consumption Expenditures: Nondurable Goods
    'PCESV', # Personal Consumption Expenditures: Services
    'PINCOME', # Personal Income
    'W211RC1Q027SBEA', # Personal current transfer payments
    'W062RC1Q027SBEA', # Personal current transfer payments: to government
    'A577RC1Q027SBEA', # Personal current transfer receipts
    'B931RC1Q027SBEA', # Personal current transfer receipts: Other current transfer receipts, from business (net)
    'W210RC1Q027SBEA', # Personal income receipts on assets
    'B703RC1Q027SBEA', # Personal income receipts on assets: Personal dividend income
    'A064RC1Q027SBEA', # Personal income receipts on assets: Personal interest income
    'B069RC1Q027SBEA', # Personal interest payments
    'A068RC1Q027SBEA', # Personal outlays
    ## Bil. of Chn. 2017 $ (SAAR)
    'DPIC96', # Real Disposable Personal Income
    'PCECC96', # Real Personal Consumption Expenditures
    'PCDGCC96', # Real Personal Consumption Expenditures: Durable Goods
    'PCNDGC96', # Real Personal Consumption Expenditures: Nondurable Goods
    'PCESVC96', # Real Personal Consumption Expenditures: Services
    'PIECTR', # Real personal income excluding current transfer receipts
    ## Chn. 2017 $ (SAAR)
    'A229RX0Q048SBEA', # Real Disposable Personal Income: Per Capita
    ## Index 2017=100 (NSA)
    'NC000349Q', # Personal Consumption Expenditures
    'NC000346Q', # Personal Consumption Expenditures: Durable Goods
    'NC000348Q', # Personal Consumption Expenditures: Nondurable Goods
    'NC000350Q', # Personal Consumption Expenditures: Services
    'NC000337Q', # Private Fixed Investment
    'NB000349Q', # Real Personal Consumption Expenditures
    'NB000346Q', # Real Personal Consumption Expenditures: Durable Goods
    'NB000348Q', # Real Personal Consumption Expenditures: Nondurable Goods
    'NB000350Q', # Real Personal Consumption Expenditures: Services
    'NB000337Q', # Real Private Fixed Investment
    ## Mil. of $ (NSA)
    'NA000349Q', # Personal Consumption Expenditures
    'NA000346Q', # Personal Consumption Expenditures: Durable Goods
    'NA000348Q', # Personal Consumption Expenditures: Nondurable Goods
    'NA000350Q', # Personal Consumption Expenditures: Services
    'NA000337Q', # Private Fixed Investment
    ## Mil. of $ (SAAR)
    'DHSGRC0', # Personal Consumption Expenditures by Type of Product: Services: Household Consumption Expenditures: Housing

    # Personal Income & Outlays > Compensation of Employees (5)
    ## Bil. of $ (SAAR)
    'W209RC1Q027SBEA', # Compensation of employees (DISCONTINUED)
    'A038RC1Q027SBEA', # Compensation of employees: Supplements to wages and salaries
    'A442RC1Q027SBEA', # Net value added of corporate business: Compensation of employees
    'A444RC1Q027SBEA', # Net value added of corporate business: Compensation of employees: Supplements to wages and salaries
    ## Mil. of $ (NSA)
    'NA000271Q', # Compensation of employees: Supplements to wages and salaries

    # Personal Income & Outlays > Employer Contributions (59)
    ## % (NSA)
    'QPRPCTCSHPCTHOLDINGSUSNO', # State and Local Government: Percent Distribution of Holdings: Percent Cash and Short-Term Investments (DISCONTINUED)
    'QPRPCTBNDPCTHOLDINGSUSNO', # State and Local Government: Percent Distribution of Holdings: Percent Corporate Bonds (DISCONTINUED)
    'QPRPCTSTKPCTHOLDINGSUSNO', # State and Local Government: Percent Distribution of Holdings: Percent Corporate Stocks (DISCONTINUED)
    'QPRPCTFASPCTHOLDINGSUSNO', # State and Local Government: Percent Distribution of Holdings: Percent Federal Agency Securities (DISCONTINUED)
    'QPRPCTFGSPCTHOLDINGSUSNO', # State and Local Government: Percent Distribution of Holdings: Percent Federal Government Securities (DISCONTINUED)
    'QPRPCTINTPCTHOLDINGSUSNO', # State and Local Government: Percent Distribution of Holdings: Percent International Securities (DISCONTINUED)
    'QPRPCTMTGPCTHOLDINGSUSNO', # State and Local Government: Percent Distribution of Holdings: Percent Mortgages (DISCONTINUED)
    'QPRPCTOTHPCTHOLDINGSUSNO', # State and Local Government: Percent Distribution of Holdings: Percent Other Securities (DISCONTINUED)
    'QPRPCTSLSPCTHOLDINGSUSNO', # State and Local Government: Percent Distribution of Holdings: Percent State and Local Government Securities (DISCONTINUED)
    'QPRPCTUSTPCTHOLDINGSUSNO', # State and Local Government: Percent Distribution of Holdings: Percent United States Treasuries (DISCONTINUED)
    ## Bil. of $ (SAAR)
    'B040RC1Q027SBEA', # Compensation of employees: Supplements to wages and salaries: Employer contributions for employee pension and insurance funds
    'B039RC1Q027SBEA', # Compensation of employees: Supplements to wages and salaries: Employer contributions for government social insurance
    ## Mil. of $ (NSA)
    'QPRHLDCSHAMTHOLDINGSUSNO', # State and Local Government: Cash and Security Holdings: Cash and Short-Term Investments (DISCONTINUED)
    'QPRHLDBNDAMTHOLDINGSUSNO', # State and Local Government: Cash and Security Holdings: Corporate Bonds (DISCONTINUED)
    'QPRHLDSTKAMTHOLDINGSUSNO', # State and Local Government: Cash and Security Holdings: Corporate Stocks (DISCONTINUED)
    'QPRHLDFASAMTHOLDINGSUSNO', # State and Local Government: Cash and Security Holdings: Federal Agency Securities (DISCONTINUED)
    'QPRHLDFGSAMTHOLDINGSUSNO', # State and Local Government: Cash and Security Holdings: Federal Government Securities (DISCONTINUED)
    'QPRHLDINTAMTHOLDINGSUSNO', # State and Local Government: Cash and Security Holdings: International Securities (DISCONTINUED)
    'QPRHLDMTGAMTHOLDINGSUSNO', # State and Local Government: Cash and Security Holdings: Mortgages (DISCONTINUED)
    'QPRHLDOTHAMTHOLDINGSUSNO', # State and Local Government: Cash and Security Holdings: Other Securities (DISCONTINUED)
    'QPRHLDSLSAMTHOLDINGSUSNO', # State and Local Government: Cash and Security Holdings: State and Local Government Securities (DISCONTINUED)
    'QPRHLDTOTAMTHOLDINGSUSNO', # State and Local Government: Cash and Security Holdings: Total Cash and Security Holdings (DISCONTINUED)
    'QPRHLDUSTAMTHOLDINGSUSNO', # State and Local Government: Cash and Security Holdings: United States Treasuries (DISCONTINUED)
    'QPRHLDCCDCSHHOLDINGSUSNO', # State and Local Government: Cash and Short-Term Investments: Cash and Checkable Deposits
    'QPRHLDCPCSHHOLDINGSUSNO', # State and Local Government: Cash and Short-Term Investments: Commercial Paper
    'QPRHLDMMFCSHHOLDINGSUSNO', # State and Local Government: Cash and Short-Term Investments: Money Market Funds
    'QPRHLDOSTCSHHOLDINGSUSNO', # State and Local Government: Cash and Short-Term Investments: Other Short-Term Investments
    'QPRHLDRRACSHHOLDINGSUSNO', # State and Local Government: Cash and Short-Term Investments: Reverse Repurchase Agreements
    'QPRHLDTSDCSHHOLDINGSUSNO', # State and Local Government: Cash and Short-Term Investments: Time and Savings Deposits
    'QPRHLDCBDBNDHOLDINGSUSNO', # State and Local Government: Corporate Bonds: Domestic
    'QPRHLDCBFBNDHOLDINGSUSNO', # State and Local Government: Corporate Bonds: Foreign
    'QPRHLDCEDCEQHOLDINGSUSNO', # State and Local Government: Corporate Equity: Domestic
    'QPRHLDCEFCEQHOLDINGSUSNO', # State and Local Government: Corporate Equity: Foreign
    'QPRHLDFTSFEDHOLDINGSUSNO', # State and Local Government: Federal Government Securities: Federal Treasury Securities
    'QPRHLDIFAFEDHOLDINGSUSNO', # State and Local Government: Federal Government Securities: Securities Issued by Federal Agencies
    'QPRHLDETFINDHOLDINGSUSNO', # State and Local Government: Other Indirectly Held Assets: Exchange Traded Funds
    'QPRHLDTHFINDHOLDINGSUSNO', # State and Local Government: Other Indirectly Held Assets: Hedge Funds
    'QPRHLDTMFINDHOLDINGSUSNO', # State and Local Government: Other Indirectly Held Assets: Mutual Funds
    'QPRHLDOPFINDHOLDINGSUSNO', # State and Local Government: Other Indirectly Held Assets: Other Private Funds
    'QPRHLDREIINDHOLDINGSUSNO', # State and Local Government: Other Indirectly Held Assets: Real Estate Investment Trusts (REITs)
    'QPRHLDDHMMIVHOLDINGSUSNO', # State and Local Government: Other Investments: Directly Held Mortgages
    'QPRHLDDRPMIVHOLDINGSUSNO', # State and Local Government: Other Investments: Directly Held Real Property
    'QPRHLDOMIMIVHOLDINGSUSNO', # State and Local Government: Other Investments: Other Miscellaneous Investments
    'QPRRVBNFTAMTREVENUESUSNO', # State and Local Government: Revenues: Benefits (DISCONTINUED)
    'QPRRVEARNAMTREVENUESUSNO', # State and Local Government: Revenues: Earnings on Investments (DISCONTINUED)
    'QPRRVCNTEAMTREVENUESUSNO', # State and Local Government: Revenues: Employee Contributions (DISCONTINUED)
    'QPRRVCNTGAMTREVENUESUSNO', # State and Local Government: Revenues: Government Contributions (DISCONTINUED)
    'QPRRVCNTTAMTREVENUESUSNO', # State and Local Government: Revenues: Total Contributions (DISCONTINUED)
    'QPRRVPMTSAMTREVENUESUSNO', # State and Local Government: Revenues: Total Payments (DISCONTINUED)
    'QPRRVTOTAMTREVENUESUSNO', # State and Local Government: Revenues: Total Receipts (DISCONTINUED)
    'QPRRVWDLSAMTREVENUESUSNO', # State and Local Government: Revenues: Withdrawals (DISCONTINUED)
    'QPRHLDTOTTOTHOLDINGSUSNO', # State and Local Government: Total Cash and Security Holdings
    'QPRHLDTCSCSHHOLDINGSUSNO', # State and Local Government: Total Cash and Short-Term Investments
    'QPRHLDTCBBNDHOLDINGSUSNO', # State and Local Government: Total Corporate Bonds
    'QPRHLDTCECEQHOLDINGSUSNO', # State and Local Government: Total Corporate Equity
    'QPRHLDTFGFEDHOLDINGSUSNO', # State and Local Government: Total Federal Government Securities
    'QPRHLDOIAINDHOLDINGSUSNO', # State and Local Government: Total Other Indirectly Held Assets
    'QPRHLDTOIMIVHOLDINGSUSNO', # State and Local Government: Total Other Investments
    'QPRHLDTPEPEQHOLDINGSUSNO', # State and Local Government: Total Private Equity

    # Personal Income & Outlays > Personal Consumption Expenditures (214)
    ## $ (SAAR)
    'A794RC0Q052SBEA', # Personal consumption expenditures per capita
    'AGDSRC0Q052SBEA', # Personal consumption expenditures per capita: Goods
    'A795RC0Q052SBEA', # Personal consumption expenditures per capita: Goods: Durable goods
    'A796RC0Q052SBEA', # Personal consumption expenditures per capita: Goods: Nondurable goods
    'A797RC0Q052SBEA', # Personal consumption expenditures per capita: Services
    ## % Chg. at Annual Rate (SAAR)
    'PCENOW', # Nowcast for Real Personal Consumption Expenditures
    'PCEGOODSNOW', # Nowcast for Real Personal Consumption Expenditures: Goods
    'PCESERVICESNOW', # Nowcast for Real Personal Consumption Expenditures: Services
    ## % Chg. from Preceding Period (SAAR)
    'DPCMRL1Q225SBEA', # Real Market-based PCE
    'DPCXRL1Q225SBEA', # Real Market-based PCE Excluding Food and Energy
    'AB61RL1Q225SBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Personal Consumption Expenditures
    'W240RL1Q225SBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Personal Consumption Expenditures: Net Purchases of Used Autos and Used Light Trucks
    'B137RL1Q225SBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Personal Consumption Expenditures: Net Purchases of Used Autos and Used Light Trucks: Used Autos
    'W241RL1Q225SBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Personal Consumption Expenditures: Net Purchases of Used Autos and Used Light Trucks: Used Light Trucks (including Utility Vehicles)
    'AB67RL1Q225SBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Personal Consumption Expenditures: New Motor Vehicles
    'A136RL1Q225SBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Personal Consumption Expenditures: New Motor Vehicles: Autos
    'B704RL1Q225SBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Personal Consumption Expenditures: New Motor Vehicles: Light Trucks (including Utility Vehicles)
    'DPCERL1Q225SBEA', # Real Personal Consumption Expenditures
    'DPCCRL1Q225SBEA', # Real Personal Consumption Expenditures (PCE) Excluding Food and Energy
    'PB001176Q', # Real Personal Consumption Expenditures (PCE) Excluding Food, Energy, and Housing
    'DNRGRL1Q225SBEA', # Real Personal Consumption Expenditures (PCE): Energy Goods and Services
    'DGDSRL1Q225SBEA', # Real Personal Consumption Expenditures: Goods
    'DDURRL1Q225SBEA', # Real Personal Consumption Expenditures: Goods: Durable Goods
    'DFDHRL1Q225SBEA', # Real Personal Consumption Expenditures: Goods: Durable Goods: Furnishings and Durable Household Equipment
    'DMOTRL1Q225SBEA', # Real Personal Consumption Expenditures: Goods: Durable Goods: Motor Vehicles and Parts
    'DODGRL1Q225SBEA', # Real Personal Consumption Expenditures: Goods: Durable Goods: Other Durable Goods
    'DREQRL1Q225SBEA', # Real Personal Consumption Expenditures: Goods: Durable Goods: Recreational Goods and Vehicles
    'DNDGRL1Q225SBEA', # Real Personal Consumption Expenditures: Goods: Nondurable Goods
    'DCLORL1Q225SBEA', # Real Personal Consumption Expenditures: Goods: Nondurable Goods: Clothing and Footwear
    'DFXARL1Q225SBEA', # Real Personal Consumption Expenditures: Goods: Nondurable Goods: Food and Beverages Purchased for Off-premises Consumption
    'DGOERL1Q225SBEA', # Real Personal Consumption Expenditures: Goods: Nondurable Goods: Gasoline and Other Energy Goods
    'DONGRL1Q225SBEA', # Real Personal Consumption Expenditures: Goods: Nondurable Goods: Other Nondurable Goods
    'DSERRL1Q225SBEA', # Real Personal Consumption Expenditures: Services
    'PB001260Q', # Real Personal Consumption Expenditures: Services Excluding Energy and Housing
    'DNPIRL1Q225SBEA', # Real Personal Consumption Expenditures: Services: Final Consumption Expenditures of Nonprofit Institutions Serving Households (NPISHs)
    'DNPERL1Q225SBEA', # Real Personal Consumption Expenditures: Services: Final Consumption Expenditures of Nonprofit Institutions Serving Households (NPISHs): Gross Output of Nonprofit Institutions
    'DHCERL1Q225SBEA', # Real Personal Consumption Expenditures: Services: Household Consumption Expenditures (for Services)
    'DIFSRL1Q225SBEA', # Real Personal Consumption Expenditures: Services: Household Consumption Expenditures (for Services): Financial Services and Insurance
    'DFSARL1Q225SBEA', # Real Personal Consumption Expenditures: Services: Household Consumption Expenditures (for Services): Food Services and Accommodations
    'DHLCRL1Q225SBEA', # Real Personal Consumption Expenditures: Services: Household Consumption Expenditures (for Services): Health Care
    'DHUTRL1Q225SBEA', # Real Personal Consumption Expenditures: Services: Household Consumption Expenditures (for Services): Housing and Utilities
    'DOTSRL1Q225SBEA', # Real Personal Consumption Expenditures: Services: Household Consumption Expenditures (for Services): Other Services
    'DRCARL1Q225SBEA', # Real Personal Consumption Expenditures: Services: Household Consumption Expenditures (for Services): Recreation Services
    'DTRSRL1Q225SBEA', # Real Personal Consumption Expenditures: Services: Household Consumption Expenditures (for Services): Transportation Services
    'DNPSRL1Q225SBEA', # Real Personal Consumption Expenditures: Services: Receipts from Sales of Goods and Services by Nonprofit Institutions
    ## % Chg. from Qtr.  1 Yr. Ago (NSA)
    'OB000349Q', # Real Personal Consumption Expenditures
    'OB000346Q', # Real Personal Consumption Expenditures: Durable Goods
    'OB000347Q', # Real Personal Consumption Expenditures: Goods
    'OB000348Q', # Real Personal Consumption Expenditures: Nondurable Goods
    'OB000350Q', # Real Personal Consumption Expenditures: Services
    ## % Chg. from Qtr.  1 Yr. Ago (SA)
    'DPCERO1Q156NBEA', # Real Personal Consumption Expenditures
    'DGDSRO1Q156NBEA', # Real Personal Consumption Expenditures: Goods
    'DDURRO1Q156NBEA', # Real Personal Consumption Expenditures: Goods: Durable Goods
    'DNDGRO1Q156NBEA', # Real Personal Consumption Expenditures: Goods: Nondurable Goods
    'DSERRO1Q156NBEA', # Real Personal Consumption Expenditures: Services
    ## Bil. of $ (SAAR)
    'A135RC1Q027SBEA', # Automobile output: Personal consumption expenditures
    'AB61RC1Q027SBEA', # Motor vehicle output: Personal consumption expenditures
    'DPCCRC1Q027SBEA', # Personal consumption expenditures excluding food and energy
    'DFDHRC1Q027SBEA', # Personal consumption expenditures: Durable goods: Furnishings and durable household equipment
    'DMOTRC1Q027SBEA', # Personal consumption expenditures: Durable goods: Motor vehicles and parts
    'DODGRC1Q027SBEA', # Personal consumption expenditures: Durable goods: Other durable goods
    'DREQRC1Q027SBEA', # Personal consumption expenditures: Durable goods: Recreational goods and vehicles
    'DNRGRC1Q027SBEA', # Personal consumption expenditures: Energy goods and services
    'DIFSRC1Q027SBEA', # Personal consumption expenditures: Financial services and insurance
    'DGDSRC1Q027SBEA', # Personal consumption expenditures: Goods
    'DPCMRC1Q027SBEA', # Personal consumption expenditures: Market-based
    'DPCXRC1Q027SBEA', # Personal consumption expenditures: Market-based, excluding food and energy
    'A137RC1Q027SBEA', # Personal consumption expenditures: Net purchases of used autos
    'W240RC1Q027SBEA', # Personal consumption expenditures: Net purchases of used autos and used light trucks
    'W241RC1Q027SBEA', # Personal consumption expenditures: Net purchases of used light trucks (including utility vehicles)
    'A136RC1Q027SBEA', # Personal consumption expenditures: New autos
    'AB67RC1Q027SBEA', # Personal consumption expenditures: New motor vehicles
    'B704RC1Q027SBEA', # Personal consumption expenditures: New motor vehicles: Light trucks (including utility vehicles)
    'DCLORC1Q027SBEA', # Personal consumption expenditures: Nondurable goods: Clothing and footwear
    'DFXARC1Q027SBEA', # Personal consumption expenditures: Nondurable goods: Food and beverages purchased for off-premises consumption
    'DGOERC1Q027SBEA', # Personal consumption expenditures: Nondurable goods: Gasoline and other energy goods
    'DONGRC1Q027SBEA', # Personal consumption expenditures: Nondurable goods: Other nondurable goods
    'DOTSRC1Q027SBEA', # Personal consumption expenditures: Other services
    'DRCARC1Q027SBEA', # Personal consumption expenditures: Recreation services
    'DNPIRC1Q027SBEA', # Personal consumption expenditures: Services: Final consumption expenditures of nonprofit institutions serving households (NPISHs)
    'DFSARC1Q027SBEA', # Personal consumption expenditures: Services: Food services and accommodations
    'DNPERC1Q027SBEA', # Personal consumption expenditures: Services: Gross output of nonprofit institutions
    'DHLCRC1Q027SBEA', # Personal consumption expenditures: Services: Health care
    'DHCERC1Q027SBEA', # Personal consumption expenditures: Services: Household consumption expenditures
    'DHUTRC1Q027SBEA', # Personal consumption expenditures: Services: Housing and utilities
    'DNPSRC1Q027SBEA', # Personal consumption expenditures: Services: Receipts from sales of goods and services by nonprofit institutions
    'DTRSRC1Q027SBEA', # Personal consumption expenditures: Transportation services
    ## Bil. of Chn. 2017 $ (NSA)
    'ND000349Q', # Real Personal Consumption Expenditures
    'ND000346Q', # Real Personal Consumption Expenditures: Durable Goods
    'ND000347Q', # Real Personal Consumption Expenditures: Goods
    'ND000348Q', # Real Personal Consumption Expenditures: Nondurable Goods
    'ND000350Q', # Real Personal Consumption Expenditures: Services
    ## Bil. of Chn. 2017 $ (SAAR)
    'AB61RX1Q020SBEA', # Real motor vehicle output: Personal consumption expenditures
    'DPCCRX1Q020SBEA', # Real personal consumption expenditures excluding food and energy
    'DFDHRX1Q020SBEA', # Real personal consumption expenditures: Durable goods: Furnishings and durable household equipment
    'DMOTRX1Q020SBEA', # Real personal consumption expenditures: Durable goods: Motor vehicles and parts
    'DODGRX1Q020SBEA', # Real personal consumption expenditures: Durable goods: Other durable goods
    'DREQRX1Q020SBEA', # Real personal consumption expenditures: Durable goods: Recreational goods and vehicles
    'DNRGRX1Q020SBEA', # Real personal consumption expenditures: Energy goods and services
    'DIFSRX1Q020SBEA', # Real personal consumption expenditures: Financial services and insurance
    'DGDSRX1Q020SBEA', # Real personal consumption expenditures: Goods
    'DPCMRX1Q020SBEA', # Real personal consumption expenditures: Market-based
    'DPCXRX1Q020SBEA', # Real personal consumption expenditures: Market-based, excluding food and energy
    'A137RX1Q020SBEA', # Real personal consumption expenditures: Net purchases of used autos
    'W240RX1Q020SBEA', # Real personal consumption expenditures: Net purchases of used autos and used light trucks
    'W241RX1Q020SBEA', # Real personal consumption expenditures: Net purchases of used light trucks (including utility vehicles)
    'AB67RX1Q020SBEA', # Real personal consumption expenditures: New motor vehicles
    'A136RX1Q020SBEA', # Real personal consumption expenditures: New motor vehicles: Autos
    'B704RX1Q020SBEA', # Real personal consumption expenditures: New motor vehicles: Light trucks (including utility vehicles)
    'DCLORX1Q020SBEA', # Real personal consumption expenditures: Nondurable goods: Clothing and footwear
    'DFXARX1Q020SBEA', # Real personal consumption expenditures: Nondurable goods: Food and beverages purchased for off-premises consumption
    'DGOERX1Q020SBEA', # Real personal consumption expenditures: Nondurable goods: Gasoline and other energy goods
    'DONGRX1Q020SBEA', # Real personal consumption expenditures: Nondurable goods: Other nondurable goods
    'DOTSRX1Q020SBEA', # Real personal consumption expenditures: Other services
    'DRCARX1Q020SBEA', # Real personal consumption expenditures: Recreation services
    'D236RX1Q020SBEA', # Real personal consumption expenditures: Residual
    'DNPIRX1Q020SBEA', # Real personal consumption expenditures: Services: Final consumption expenditures of nonprofit institutions serving households (NPISHs)
    'DFSARX1Q020SBEA', # Real personal consumption expenditures: Services: Food services and accommodations
    'DNPERX1Q020SBEA', # Real personal consumption expenditures: Services: Gross output of nonprofit institutions
    'DHLCRX1Q020SBEA', # Real personal consumption expenditures: Services: Health care
    'DHCERX1Q020SBEA', # Real personal consumption expenditures: Services: Household consumption expenditures
    'DHUTRX1Q020SBEA', # Real personal consumption expenditures: Services: Housing and utilities
    'DNPSRX1Q020SBEA', # Real personal consumption expenditures: Services: Receipts from sales of goods and services by nonprofit institutions
    'DTRSRX1Q020SBEA', # Real personal consumption expenditures: Transportation services
    ## Chn. 2017 $ (SAAR)
    'A794RX0Q048SBEA', # Real personal consumption expenditures per capita
    'AGDSRX0Q048SBEA', # Real personal consumption expenditures per capita: Goods
    'A795RX0Q048SBEA', # Real personal consumption expenditures per capita: Goods: Durable goods
    'A796RX0Q048SBEA', # Real personal consumption expenditures per capita: Goods: Nondurable goods
    'A797RX0Q048SBEA', # Real personal consumption expenditures per capita: Services
    ## Index 2017=100 (NSA)
    'NC000347Q', # Personal Consumption Expenditures: Goods
    'NB000347Q', # Real Personal Consumption Expenditures: Goods
    ## Mil. of $ (NSA)
    'NA000347Q', # Personal Consumption Expenditures: Goods
    ## Mil. of $ (SAAR)
    'LA001176Q', # Personal Consumption Expenditures Excluding Food, Energy, and Housing
    'LA001260Q', # Personal Consumption Expenditures: Services Excluding Energy and Housing
    ## Mil. of Chn. 2017 $ (SAAR)
    'LB001176Q', # Real Personal Consumption Expenditures Excluding Food, Energy, and Housing
    'LB001260Q', # Real Personal Consumption Expenditures: Services Excluding Energy and Housing
    ## Percentage Points (SA)
    'PCECONTRIBNOW', # Contributions to percent change in GDPNow: Real Personal Consumption Expenditures
    'PCEGOODSCONTRIBNOW', # Contributions to percent change in GDPNow: Real Personal Consumption Expenditures: Goods
    'PCESERVICESCONTRIBNOW', # Contributions to percent change in GDPNow: Real Personal Consumption Expenditures: Services
    ## Percentage Points at Annual Rate (SAAR)
    'CB001176Q', # Contributions to Percent Change in Real Personal Consumption Expenditures: Real Personal Consumption Expenditures Excluding Food, Energy, and Housing
    'CB001260Q', # Contributions to Percent Change in Real Personal Consumption Expenditures: Real Personal Consumption Expenditures: Services Excluding Energy and Housing
    'DPCERS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures
    'DDURRS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Durable goods
    'DFDHRS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Durable goods: Furnishings and durable household equipment
    'DMOTRS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Durable goods: Motor vehicles and parts
    'DREQRS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Durable goods: Recreational goods and vehicles
    'DNPIRS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Final consumption expenditures of nonprofit institutions serving households (NPISHs)
    'DGDSRS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Goods
    'DIFSRS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Household consumption expenditures: Financial services and insurance
    'DOTSRS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Household consumption expenditures: Other services
    'DRCARS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Household consumption expenditures: Recreation services
    'DTRSRS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Household consumption expenditures: Transportation services
    'DNDGRS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Nondurable goods
    'DCLORS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Nondurable goods: Clothing and footwear
    'DFXARS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Nondurable goods: Food and beverages purchased for off-premises consumption
    'DGOERS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Nondurable goods: Gasoline and other energy goods
    'DODGRS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Other durable goods
    'DONGRS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Other nondurable goods
    'DSERRS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Services
    'DHCERS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Services: Household consumption expenditures
    'DFSARS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Services: Household consumption expenditures: Food services and accommodations
    'DHLCRS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Services: Household consumption expenditures: Health care
    'DHUTRS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Services: Household consumption expenditures: Housing and utilities
    'DNPSRY2Q224SBEA', # Contributions to percent change in real GDP: PCE: Final consumption expenditures of nonprofit institutions serving households (NPISHs): Less: Receipts from sales of goods and services by nonprofit institutions
    'DPCERY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures
    'DDURRY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Durable goods
    'DFDHRY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Durable goods: Furnishings and durable household equipment
    'DMOTRY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Durable goods: Motor vehicles and parts
    'DREQRY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Durable goods: Recreational goods and vehicles
    'DNPIRY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Final consumption expenditures of nonprofit institutions serving households (NPISHs)
    'DGDSRY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Goods
    'DNDGRY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Nondurable goods
    'DCLORY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Nondurable goods: Clothing and footwear
    'DFXARY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Nondurable goods: Food and beverages purchased for off-premises consumption
    'DGOERY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Nondurable goods: Gasoline and other energy goods
    'DODGRY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Other durable goods
    'DONGRY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Other nondurable goods
    'DOTSRY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Other services
    'DRCARY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Recreation services
    'DSERRY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Services
    'DNPERY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Services: Final consumption expenditures of nonprofit institutions serving households (NPISHs): Gross output of nonprofit institutions
    'DIFSRY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Services: Financial services and insurance
    'DFSARY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Services: Food services and accommodations
    'DHLCRY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Services: Health care
    'DHCERY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Services: Household consumption expenditures (for services)
    'DHUTRY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Services: Housing and utilities
    'DTRSRY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Transportation services
    'DDURRZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Durable goods
    'DFDHRZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Durable goods: Furnishings and durable household equipment
    'DMOTRZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Durable goods: Motor vehicles and parts
    'DODGRZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Durable goods: Other durable goods
    'DREQRZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Durable goods: Recreational goods and vehicles
    'DNRGRZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Energy goods and services
    'DIFSRZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Financial services and insurance
    'DGDSRZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Goods
    'DPCMRZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Market-based
    'DPCXRZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Market-based, excluding food and energy
    'DNDGRZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Nondurable goods
    'DCLORZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Nondurable goods: Clothing and footwear
    'DFXARZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Nondurable goods: Food and beverages purchased for off-premises consumption
    'DGOERZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Nondurable goods: Gasoline and other energy goods
    'DONGRZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Nondurable goods: Other nondurable goods
    'DOTSRZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Other services
    'DPCCRZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Real personal consumption expenditures excluding food and energy
    'DRCARZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Recreation services
    'DSERRZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Services
    'DNPIRZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Services: Final consumption expenditures of nonprofit institutions serving households (NPISHs)
    'DFSARZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Services: Food services and accommodations
    'DNPERZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Services: Gross output of nonprofit institutions
    'DHLCRZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Services: Health care
    'DHCERZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Services: Household consumption expenditures
    'DHUTRZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Services: Housing and utilities
    'DNPSRZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Services: Receipts from sales of goods and services by nonprofit institutions
    'DTRSRZ2Q224SBEA', # Contributions to percent change in real personal consumption expenditures: Transportation services

    # Personal Income & Outlays > Personal Current Taxes (10)
    ## Bil. of $ (NSA)
    'A074RU1Q027NBEA', # Federal government current tax receipts: Personal current taxes (DISCONTINUED)
    'W071RU1Q027NBEA', # State and local government current tax receipts: Personal current taxes (DISCONTINUED)
    ## Bil. of $ (SAAR)
    'A074RC1Q027SBEA', # Federal government current tax receipts: Personal current taxes
    'W055RC1Q027SBEA', # Personal current taxes
    'W071RC1Q027SBEA', # State and local government current tax receipts: Personal current taxes
    'B245RC1Q027SBEA', # State and local government current tax receipts: Personal current taxes: Income taxes
    'B247RC1Q027SBEA', # State and local government current tax receipts: Personal current taxes: Other
    ## Mil. of $ (NSA)
    'NA000320Q', # Federal government current tax receipts: Personal current taxes
    'NA000321Q', # State and local government current tax receipts: Personal current taxes
    ## Mil. of $ (SAAR)
    'S210400', # Personal Current Tax Receipts: State and Local Government: Property Taxes

    # Personal Income & Outlays > Wage and Salary Accruals (8)
    ## Bil. of $ (SAAR)
    'W269RC1Q027SBEA', # Gross domestic income: Compensation of employees, paid: Wage and salary accruals: Disbursements (DISCONTINUED)
    'A4102C1Q027SBEA', # Gross domestic income: Compensation of employees, paid: Wages and salaries
    'W270RC1Q027SBEA', # Gross domestic income: Compensation of employees, paid: Wages and salaries: to persons
    'A553RC1Q027SBEA', # National income: Compensation of employees: Wages and salaries: Government (DISCONTINUED)
    'B203RC1Q027SBEA', # National income: Compensation of employees: Wages and salaries: Other (DISCONTINUED)
    'A443RC1Q027SBEA', # Net value added of corporate business: Compensation of employees: Wages and salaries
    ## Mil. of $ (NSA)
    'NA000275Q', # Gross domestic income: Compensation of employees, paid: Wages and salaries
    'NA000259Q', # Gross domestic income: Compensation of employees, paid: Wages and salaries: to persons

]

# Annually (1715)
ids_Y = [
    # Personal Income & Outlays (92)
    ## $ (NSA)
    'A229RC0A052NBEA', # Disposable personal income: Per capita
    'A792RC0A052NBEA', # Personal income per capita
    ## % (NSA)
    'A072RC1A156NBEA', # Personal saving as a percentage of disposable personal income
    ## % Chg. from Preceding Period (NSA)
    'A067RP1A027NBEA', # Disposable Personal Income
    'A067RL1A156NBEA', # Real Disposable Personal Income
    ## Bil. of $ (NSA)
    'A132RC1A027NBEA', # Compensation of employees: Wages and salaries: Private industries
    'W388RC1A027NBEA', # Disposable household income
    'A067RC1A027NBEA', # Disposable personal income
    'L318151A027NBEA', # Federal government cash receipts from the public: Timing differences: Withheld personal income tax and social security contributions (DISCONTINUED)
    'M318151A027NBEA', # Federal government receipts: Timing differences: Withheld personal income tax and social security contributions (NIPA vs. Budget)
    'B1138C1A027NBEA', # Monetary interest received: Persons
    'B1170C1A027NBEA', # Monetary interest received: Persons: Other (DISCONTINUED)
    'B1169C1A027NBEA', # Monetary interest received: Persons: Publicly administered government employee retirement plans (DISCONTINUED)
    'W424RC1A027NBEA', # Nonprofit institution income included in personal income
    'PCECA', # Personal Consumption Expenditures
    'PCDGA', # Personal Consumption Expenditures: Durable Goods
    'PCNDA', # Personal Consumption Expenditures: Nondurable Goods
    'PCESVA', # Personal Consumption Expenditures: Services
    'W211RC1A027NBEA', # Personal current transfer payments
    'W062RC1A027NBEA', # Personal current transfer payments: to government
    'A577RC1A027NBEA', # Personal current transfer receipts
    'B931RC1A027NBEA', # Personal current transfer receipts: Other current transfer receipts, from business (net)
    'A065RC1A027NBEA', # Personal income
    'W210RC1A027NBEA', # Personal income receipts on assets
    'B703RC1A027NBEA', # Personal income receipts on assets: Personal dividend income
    'A064RC1A027NBEA', # Personal income receipts on assets: Personal interest income
    'Y685RC1A027NBEA', # Personal income: Imputations: Defined benefit and defined contribution pension plans
    'Q397RC1A027NBEA', # Personal income: Nonprofit institution income: Nonprofit institution transfer receipts: From households
    'Y508RC1A027NBEA', # Personal income: Personal income receipts on assets: Excluding imputations
    'Y507RC1A027NBEA', # Personal income: Personal income receipts on assets: Imputations
    'B069RC1A027NBEA', # Personal interest payments
    'A068RC1A027NBEA', # Personal outlays
    'A071RC1A027NBEA', # Personal saving
    'A048RC1A027NBEA', # Rental income of persons with capital consumption adjustment
    'W157RC1A027NBEA', # Rental income of persons with capital consumption adjustment: Households and nonprofit institutions
    'W158RC1A027NBEA', # Rental income of persons with capital consumption adjustment: Households and nonprofit institutions: Farm owner-occupied housing owned by farm operators
    'A2217C1A027NBEA', # Rental income of persons with capital consumption adjustment: Households and nonprofit institutions: Nonfarm owner-occupied housing
    'B1435C1A027NBEA', # Rental income of persons with capital consumption adjustment: Households and nonprofit institutions: Nonfarm owner-occupied housing: Manufactured homes
    'B1434C1A027NBEA', # Rental income of persons with capital consumption adjustment: Households and nonprofit institutions: Nonfarm owner-occupied housing: Permanent site
    'B1437C1A027NBEA', # Rental income of persons with capital consumption adjustment: Private business: Farms owned by nonoperator landlords
    'B1438C1A027NBEA', # Rental income of persons with capital consumption adjustment: Private business: Nonfarm nonresidential properties
    'B1439C1A027NBEA', # Rental income of persons with capital consumption adjustment: Private business: Royalties
    'W285RC1A027NBEA', # Rental income of persons with capital consumption adjustment: Private business: Tenant-occupied housing
    'W155RC1A027NBEA', # Rental income of persons with capital consumption adjustment: Private business: Tenant-occupied housing, farms owned by nonoperator landlords, nonfarm nonresidential properties, and royalties
    'W156RC1A027NBEA', # Rental income of persons with capital consumption adjustment: Private business: Tenant-occupied housing: Farm tenant-occupied housing owned by farm operator landlords
    'B1436C1A027NBEA', # Rental income of persons with capital consumption adjustment: Private business: Tenant-occupied housing: Nonfarm tenant-occupied permanent site housing
    'A2215C1A027NBEA', # Rental income with capital consumption adjustment
    'CONBFE1A027NBEA', # Supplements to wages and salaries: Federal employees unemployment insurance
    'CON1501A027NBEA', # Supplements to wages and salaries: Federal unemployment tax
    'A2210C1A027NBEA', # Supplements to wages and salaries: Health insurance
    'L306061A027NBEA', # Supplements to wages and salaries: Health insurance: Federal hospital insurance
    'B1606C1A027NBEA', # Supplements to wages and salaries: Health insurance: Military medical insurance
    'B4923C1A027NBEA', # Supplements to wages and salaries: Health insurance: Private group health insurance
    'S252101A027NBEA', # Supplements to wages and salaries: Health insurance: Temporary disability insurance
    'A2211C1A027NBEA', # Supplements to wages and salaries: Life insurance
    'B4924C1A027NBEA', # Supplements to wages and salaries: Life insurance: Private group life insurance
    'CON2101A027NBEA', # Supplements to wages and salaries: Life insurance: Veterans life insurance
    'A2209C1A027NBEA', # Supplements to wages and salaries: Pension, profit-sharing, and other retirement benefit plans
    'B4945C1A027NBEA', # Supplements to wages and salaries: Pension, profit-sharing, and other retirement benefit plans: Federal civilian employee retirement
    'B1583C1A027NBEA', # Supplements to wages and salaries: Pension, profit-sharing, and other retirement benefit plans: Federal military employee retirement
    'L306051A027NBEA', # Supplements to wages and salaries: Pension, profit-sharing, and other retirement benefit plans: Old-age, survivors, and disability insurance
    'B1043C1A027NBEA', # Supplements to wages and salaries: Pension, profit-sharing, and other retirement benefit plans: Pension benefit guaranty
    'B4921C1A027NBEA', # Supplements to wages and salaries: Pension, profit-sharing, and other retirement benefit plans: Private pension and profit-sharing
    'CON1701A027NBEA', # Supplements to wages and salaries: Pension, profit-sharing, and other retirement benefit plans: Railroad retirement
    'S251101A027NBEA', # Supplements to wages and salaries: Pension, profit-sharing, and other retirement benefit plans: State and local employee retirement
    'B4926C1A027NBEA', # Supplements to wages and salaries: Private supplemental unemployment insurance
    'CON1601A027NBEA', # Supplements to wages and salaries: Railroad employees unemployment insurance
    'CON1201A027NBEA', # Supplements to wages and salaries: State unemployment insurance
    'A2213C1A027NBEA', # Supplements to wages and salaries: Unemployment insurance
    'A2212C1A027NBEA', # Supplements to wages and salaries: Workers' compensation
    'CON2201A027NBEA', # Supplements to wages and salaries: Workers' compensation: Federal
    'B4925C1A027NBEA', # Supplements to wages and salaries: Workers' compensation: Private insurance
    'S253001A027NBEA', # Supplements to wages and salaries: Workers' compensation: State and local
    'BA06RC1A027NBEA', # Total wages and salaries, BLS
    'BA07RC1A027NBEA', # Total wages and salaries, BLS: Adjustment for misreporting on employment tax returns
    'W873RC1A027NBEA', # Total wages and salaries, BLS: Adjustment for wages and salaries not covered or not fully covered by unemployment insurance
    'W787RC1A027NBEA', # Total wages and salaries, BLS: Adjustment for wages and salaries not covered or not fully covered by unemployment insurance: Government
    'W786RC1A027NBEA', # Total wages and salaries, BLS: Adjustment for wages and salaries not covered or not fully covered by unemployment insurance: Other
    ## Bil. of Chn. 2017 $ (NSA)
    'PCECCA', # Real Personal Consumption Expenditures
    'PCDGCCA', # Real Personal Consumption Expenditures: Durable Goods
    'PCNDGCA', # Real Personal Consumption Expenditures: Nondurable Goods
    'PCESVCA', # Real Personal Consumption Expenditures: Services
    'A067RX1A020NBEA', # Real disposable personal income
    'W875RX1A020NBEA', # Real personal income excluding current transfer receipts
    ## Chn. 2017 $ (NSA)
    'A229RX0A048NBEA', # Real Disposable Personal Income: Per Capita
    'RPIPCUS', # Real Per Capita Personal Income for United States
    'RPIPCUSNMP', # Real Per Capita Personal Income: Nonmetropolitan Portion for United States (DISCONTINUED)
    ## Mil. of $ (NSA)
    'B4941C0A144NBEA', # Employee contributions for publicly administered government employee retirement plans (DISCONTINUED)
    'B4947C0A144NBEA', # Employee contributions for publicly administered government employee retirement plans: Federal civilian (DISCONTINUED)
    'S251200A144NBEA', # State and Local Government Defined Benefit Pension Plans: Effect of participation in defined benefit plans on personal income, saving, and wealth: Household actual contributions (DISCONTINUED)
    ## Mil. of Chn. 2012 $ (NSA)
    'RPIUS', # Real Personal Income for United States
    ## Thous. of Chn. 2012 $ (NSA)
    'RPIUSNMP', # Real Personal Income: Nonmetropolitan Portion for United States (DISCONTINUED)

    # Personal Income & Outlays > Compensation of Employees (301)
    ## Bil. of $ (NSA)
    'W209RC1A027NBEA', # Compensation of employees (DISCONTINUED)
    'A038RC1A027NBEA', # Compensation of employees: Supplements to wages and salaries
    'A033RC1A027NBEA', # National income: Compensation of employees
    'A442RC1A027NBEA', # National income: Domestic business: Corporate business: Compensation of employees
    'A444RC1A027NBEA', # National income: Domestic business: Corporate business: Compensation of employees: Supplements to wages and salaries
    'W462RC1A027NBEA', # National income: Domestic business: Noncorporate business: Compensation of employees
    'W464RC1A027NBEA', # National income: Domestic business: Noncorporate business: Compensation of employees: Supplements to wages and salaries
    'A1658C1A027NBEA', # National income: Domestic business: Noncorporate business: Government enterprises: Compensation of employees
    'B1660C1A027NBEA', # National income: Domestic business: Noncorporate business: Government enterprises: Compensation of employees: Supplements to wages and salaries
    'A1651C1A027NBEA', # National income: Domestic business: Noncorporate business: Other private business: Compensation of employees
    'B1653C1A027NBEA', # National income: Domestic business: Noncorporate business: Other private business: Compensation of employees: Supplements to wages and salaries
    'A1642C1A027NBEA', # National income: Domestic business: Noncorporate business: Sole proprietorships and partnerships: Compensation of employees
    'B1644C1A027NBEA', # National income: Domestic business: Noncorporate business: Sole proprietorships and partnerships: Compensation of employees: Supplements to wages and salaries
    'B1664C1A027NBEA', # National income: General government: Compensation of employees: Supplements to wages and salaries
    'W152RC1A027NBEA', # National income: Households and institutions: Nonprofit institutions serving households: Compensation of employees
    'W482RC1A027NBEA', # National income: Households and institutions: Nonprofit institutions serving households: Compensation of employees: Supplements to wages and salaries
    'W151RC1A027NBEA', # National income: Households: Compensation of employees
    'B1662C1A027NBEA', # National income: Households: Compensation of employees: Supplements to wages and salaries
    'A4187C1A027NBEA', # National income: Rest of the world: Compensation of employees
    'Y390RC1A027NBEA', # Supplements to Wages and Salaries: Health insurance: Publicly administered government employee insurance funds
    'Y239RC1A027NBEA', # Supplements to Wages and Salaries: Pension and other employee benefit plans: State and local employee retirement
    ## Mil. of $ (NSA)
    'A4003C0A144NBEA', # Compensation of employees: Domestic private industries
    'N4085C0A144NBEA', # Compensation of employees: Domestic private industries: Accommodation
    'N4084C0A144NBEA', # Compensation of employees: Domestic private industries: Accommodation and food services
    'N4073C0A144NBEA', # Compensation of employees: Domestic private industries: Administrative and support services
    'N4072C0A144NBEA', # Compensation of employees: Domestic private industries: Administrative and waste management services
    'H4006C0A144NBEA', # Compensation of employees: Domestic private industries: Agricultural services, forestry, and fisheries
    'B4006C0A144NBEA', # Compensation of employees: Domestic private industries: Agricultural services, forestry, and fishing
    'J4006C0A144NBEA', # Compensation of employees: Domestic private industries: Agricultural services, forestry, and fishing
    'H4004C0A144NBEA', # Compensation of employees: Domestic private industries: Agriculture, forestry, and fisheries
    'A4004C0A144NBEA', # Compensation of employees: Domestic private industries: Agriculture, forestry, and fishing
    'J4004C0A144NBEA', # Compensation of employees: Domestic private industries: Agriculture, forestry, and fishing (DISCONTINUED)
    'N4004C0A144NBEA', # Compensation of employees: Domestic private industries: Agriculture, forestry, fishing, and hunting
    'N4046C0A144NBEA', # Compensation of employees: Domestic private industries: Air transportation
    'N4077C0A144NBEA', # Compensation of employees: Domestic private industries: Ambulatory health care services
    'B4067C0A144NBEA', # Compensation of employees: Domestic private industries: Amusement and recreation services
    'J4067C0A144NBEA', # Compensation of employees: Domestic private industries: Amusement and recreation services
    'N4083C0A144NBEA', # Compensation of employees: Domestic private industries: Amusements, gambling, and recreation industries
    'B4092C0A144NBEA', # Compensation of employees: Domestic private industries: Anthracite mining
    'N4081C0A144NBEA', # Compensation of employees: Domestic private industries: Arts, entertainment, and recreation
    'B4064C0A144NBEA', # Compensation of employees: Domestic private industries: Auto repair, services, and parking
    'J4053C0A144NBEA', # Compensation of employees: Domestic private industries: Banking
    'H4009C0A144NBEA', # Compensation of employees: Domestic private industries: Bituminous and other soft coal mining
    'B4063C0A144NBEA', # Compensation of employees: Domestic private industries: Business services
    'H4063C0A144NBEA', # Compensation of employees: Domestic private industries: Business services
    'J4063C0A144NBEA', # Compensation of employees: Domestic private industries: Business services
    'B4009C0A144NBEA', # Compensation of employees: Domestic private industries: Coal mining
    'J4009C0A144NBEA', # Compensation of employees: Domestic private industries: Coal mining
    'A4046C0A144NBEA', # Compensation of employees: Domestic private industries: Communication
    'J4046C0A144NBEA', # Compensation of employees: Domestic private industries: Communication
    'B4048C0A144NBEA', # Compensation of employees: Domestic private industries: Communication: Radio and television
    'J4048C0A144NBEA', # Compensation of employees: Domestic private industries: Communication: Radio and television
    'B4047C0A144NBEA', # Compensation of employees: Domestic private industries: Communication: Telephone and telegraph
    'J4047C0A144NBEA', # Compensation of employees: Domestic private industries: Communication: Telephone and telegraph
    'N4069C0A144NBEA', # Compensation of employees: Domestic private industries: Computer systems design and related services
    'B4012C0A144NBEA', # Compensation of employees: Domestic private industries: Construction
    'N4012C0A144NBEA', # Compensation of employees: Domestic private industries: Construction
    'J4012C0A144NBEA', # Compensation of employees: Domestic private industries: Construction (DISCONTINUED)
    'H4012C0A144NBEA', # Compensation of employees: Domestic private industries: Contract construction
    'H4054C0A144NBEA', # Compensation of employees: Domestic private industries: Credit agencies (other than banks) and holding and other investment companies
    'J4054C0A144NBEA', # Compensation of employees: Domestic private industries: Credit agencies other than banks
    'B4053C0A144NBEA', # Compensation of employees: Domestic private industries: Depository institutions
    'B4070C0A144NBEA', # Compensation of employees: Domestic private industries: Educational services
    'J4070C0A144NBEA', # Compensation of employees: Domestic private industries: Educational services
    'N4075C0A144NBEA', # Compensation of employees: Domestic private industries: Educational services
    'H4070C0A144NBEA', # Compensation of employees: Domestic private industries: Educational services, n.e.c.
    'B4005C0A144NBEA', # Compensation of employees: Domestic private industries: Farms
    'H4005C0A144NBEA', # Compensation of employees: Domestic private industries: Farms
    'N4005C0A144NBEA', # Compensation of employees: Domestic private industries: Farms
    'N4060C0A144NBEA', # Compensation of employees: Domestic private industries: Federal Reserve banks, credit intermediation, and related activities
    'N4059C0A144NBEA', # Compensation of employees: Domestic private industries: Finance and insurance
    'A4052C0A144NBEA', # Compensation of employees: Domestic private industries: Finance, insurance, and real estate
    'H4052C0A144NBEA', # Compensation of employees: Domestic private industries: Finance, insurance, and real estate
    'J4052C0A144NBEA', # Compensation of employees: Domestic private industries: Finance, insurance, and real estate (DISCONTINUED)
    'H4055C0A144NBEA', # Compensation of employees: Domestic private industries: Finance, insurance, and real estate: Security and commodity brokers, and services
    'N4086C0A144NBEA', # Compensation of employees: Domestic private industries: Food services and drinking places
    'N4006C0A144NBEA', # Compensation of employees: Domestic private industries: Forestry, fishing, and related activities
    'N4063C0A144NBEA', # Compensation of employees: Domestic private industries: Funds, trusts, and other financial vehicles
    'N4076C0A144NBEA', # Compensation of employees: Domestic private industries: Health care and social assistance
    'B4068C0A144NBEA', # Compensation of employees: Domestic private industries: Health services
    'H4068C0A144NBEA', # Compensation of employees: Domestic private industries: Health services
    'J4068C0A144NBEA', # Compensation of employees: Domestic private industries: Health services
    'B4059C0A144NBEA', # Compensation of employees: Domestic private industries: Holding and other investment offices
    'N4078C0A144NBEA', # Compensation of employees: Domestic private industries: Hospitals
    'N4054C0A144NBEA', # Compensation of employees: Domestic private industries: Information
    'N4057C0A144NBEA', # Compensation of employees: Domestic private industries: Information: Broadcasting and telecommunications
    'N4058C0A144NBEA', # Compensation of employees: Domestic private industries: Information: Information and data processing services
    'N4056C0A144NBEA', # Compensation of employees: Domestic private industries: Information: Motion picture and sound recording industries
    'N4055C0A144NBEA', # Compensation of employees: Domestic private industries: Information: Publishing industries (includes software)
    'B4057C0A144NBEA', # Compensation of employees: Domestic private industries: Insurance agents, brokers, and service
    'H4057C0A144NBEA', # Compensation of employees: Domestic private industries: Insurance agents, brokers, and service
    'J4057C0A144NBEA', # Compensation of employees: Domestic private industries: Insurance agents, brokers, and service
    'B4056C0A144NBEA', # Compensation of employees: Domestic private industries: Insurance carriers
    'N4062C0A144NBEA', # Compensation of employees: Domestic private industries: Insurance carriers and related activities
    'B4069C0A144NBEA', # Compensation of employees: Domestic private industries: Legal services
    'J4069C0A144NBEA', # Compensation of employees: Domestic private industries: Legal services
    'N4068C0A144NBEA', # Compensation of employees: Domestic private industries: Legal services
    'B4094C0A144NBEA', # Compensation of employees: Domestic private industries: Local utilities and public services, n.e.c.
    'N4071C0A144NBEA', # Compensation of employees: Domestic private industries: Management of companies and enterprises
    'A4013C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing
    'H4013C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing
    'N4013C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing
    'J4013C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing (DISCONTINUED)
    'A4014C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods
    'H4014C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods
    'N4014C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods
    'J4014C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods (DISCONTINUED)
    'N4020C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Computer and electronic products
    'B4021C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Electric and electronic equipment
    'H4021C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Electric and electronic equipment
    'J4021C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Electric and electronic equipment
    'N4021C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Electrical equipment, appliances, and components
    'B4019C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Fabricated metal products
    'J4019C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Fabricated metal products
    'N4018C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Fabricated metal products
    'H4016C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Furniture and finished lumber products
    'B4016C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Furniture and fixtures
    'J4016C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Furniture and fixtures
    'N4024C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Furniture and related products
    'B4024C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Instruments and related products
    'J4024C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Instruments and related products
    'H4018C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Iron and steel and their products, including ordnance
    'H4015C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Lumber and basic timber products
    'B4015C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Lumber and wood products
    'J4015C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Lumber and wood products
    'N4019C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Machinery
    'B4020C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Machinery, except electrical
    'H4020C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Machinery, except electrical
    'J4020C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Machinery, except electrical
    'N4025C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Miscellaneous manufacturing
    'B4025C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Miscellaneous manufacturing industries
    'J4025C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Miscellaneous manufacturing industries
    'H4025C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Miscellaneous manufacturing, including instruments and miscellaneous plastic products
    'B4022C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Motor vehicles and equipment
    'H4022C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Motor vehicles and equipment
    'J4022C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Motor vehicles and equipment
    'N4022C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Motor vehicles, bodies and trailers, and parts
    'H4019C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Nonferrous metals and their products
    'N4016C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Nonmetallic mineral products
    'B4023C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Other transportation equipment
    'H4023C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Other transportation equipment
    'J4023C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Other transportation equipment
    'N4023C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Other transportation equipment
    'B4018C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Primary metal industries
    'J4018C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Primary metal industries
    'N4017C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Primary metals
    'B4017C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Stone, clay, and glass products
    'H4017C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Stone, clay, and glass products
    'J4017C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Stone, clay, and glass products
    'N4015C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Durable goods: Wood products
    'A4026C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods
    'H4026C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods
    'N4026C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods
    'J4026C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods (DISCONTINUED)
    'N4030C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Apparel and leather and allied products
    'B4030C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Apparel and other textile products
    'H4030C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Apparel and other textile products
    'J4030C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Apparel and other textile products
    'N4035C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Chemical products
    'B4033C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Chemicals and allied products
    'H4033C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Chemicals and allied products
    'J4033C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Chemicals and allied products
    'N4027C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Food and beverage and tobacco products
    'B4027C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Food and kindred products
    'H4027C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Food and kindred products
    'J4027C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Food and kindred products
    'B4036C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Leather and leather products
    'H4036C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Leather and leather products
    'J4036C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Leather and leather products
    'B4031C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Paper and allied products
    'J4031C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Paper and allied products
    'N4032C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Paper products
    'B4034C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Petroleum and coal products
    'H4034C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Petroleum and coal products
    'J4034C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Petroleum and coal products
    'N4034C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Petroleum and coal products
    'N4036C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Plastics and rubber products
    'B4032C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Printing and publishing
    'H4032C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Printing and publishing
    'J4032C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Printing and publishing
    'N4033C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Printing and related support activities
    'B4035C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Rubber and miscellaneous plastics products
    'J4035C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Rubber and miscellaneous plastics products
    'H4035C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Rubber products
    'B4029C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Textile mill products
    'H4029C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Textile mill products
    'J4029C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Textile mill products
    'N4029C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Textile mills and textile product mills
    'B4028C0A144NBEA', # Compensation of employees: Domestic private industries: Manufacturing: Nondurable goods: Tobacco manufactures
    'B4073C0A144NBEA', # Compensation of employees: Domestic private industries: Membership organizations
    'B4008C0A144NBEA', # Compensation of employees: Domestic private industries: Metal mining
    'A4007C0A144NBEA', # Compensation of employees: Domestic private industries: Mining
    'H4007C0A144NBEA', # Compensation of employees: Domestic private industries: Mining
    'N4007C0A144NBEA', # Compensation of employees: Domestic private industries: Mining
    'J4007C0A144NBEA', # Compensation of employees: Domestic private industries: Mining (DISCONTINUED)
    'N4009C0A144NBEA', # Compensation of employees: Domestic private industries: Mining, except oil and gas
    'H4010C0A144NBEA', # Compensation of employees: Domestic private industries: Mining: Crude petroleum and natural gas
    'B4011C0A144NBEA', # Compensation of employees: Domestic private industries: Mining: Nonmetallic minerals, except fuels
    'N4008C0A144NBEA', # Compensation of employees: Domestic private industries: Mining: Oil and gas extraction
    'B4074C0A144NBEA', # Compensation of employees: Domestic private industries: Miscellaneous professional services
    'H4074C0A144NBEA', # Compensation of employees: Domestic private industries: Miscellaneous professional services
    'J4074C0A144NBEA', # Compensation of employees: Domestic private industries: Miscellaneous professional services
    'N4070C0A144NBEA', # Compensation of employees: Domestic private industries: Miscellaneous professional, scientific, and technical services
    'B4065C0A144NBEA', # Compensation of employees: Domestic private industries: Miscellaneous repair services
    'B4054C0A144NBEA', # Compensation of employees: Domestic private industries: Nondepository institutions
    'N4079C0A144NBEA', # Compensation of employees: Domestic private industries: Nursing and residential care facilities
    'B4010C0A144NBEA', # Compensation of employees: Domestic private industries: Oil and gas extraction
    'J4010C0A144NBEA', # Compensation of employees: Domestic private industries: Oil and gas extraction
    'N4087C0A144NBEA', # Compensation of employees: Domestic private industries: Other services, except government
    'N4052C0A144NBEA', # Compensation of employees: Domestic private industries: Other transportation and support activities
    'N4082C0A144NBEA', # Compensation of employees: Domestic private industries: Performing arts, spectator sports, museums, and related activities
    'B4062C0A144NBEA', # Compensation of employees: Domestic private industries: Personal services
    'J4062C0A144NBEA', # Compensation of employees: Domestic private industries: Personal services
    'N4051C0A144NBEA', # Compensation of employees: Domestic private industries: Pipeline transportation
    'N4067C0A144NBEA', # Compensation of employees: Domestic private industries: Professional, scientific, and technical services
    'N4047C0A144NBEA', # Compensation of employees: Domestic private industries: Rail transportation
    'B4039C0A144NBEA', # Compensation of employees: Domestic private industries: Railroad transportation
    'B4058C0A144NBEA', # Compensation of employees: Domestic private industries: Real estate
    'H4058C0A144NBEA', # Compensation of employees: Domestic private industries: Real estate
    'J4058C0A144NBEA', # Compensation of employees: Domestic private industries: Real estate
    'N4065C0A144NBEA', # Compensation of employees: Domestic private industries: Real estate
    'N4064C0A144NBEA', # Compensation of employees: Domestic private industries: Real estate and rental and leasing
    'N4066C0A144NBEA', # Compensation of employees: Domestic private industries: Rental and leasing services and lessors of intangible assets
    'B4051C0A144NBEA', # Compensation of employees: Domestic private industries: Retail trade
    'N4040C0A144NBEA', # Compensation of employees: Domestic private industries: Retail trade
    'J4051C0A144NBEA', # Compensation of employees: Domestic private industries: Retail trade (DISCONTINUED)
    'H4051C0A144NBEA', # Compensation of employees: Domestic private industries: Retail trade and automobile services
    'N4042C0A144NBEA', # Compensation of employees: Domestic private industries: Retail trade: Food and beverage stores
    'N4043C0A144NBEA', # Compensation of employees: Domestic private industries: Retail trade: General merchandise stores
    'N4041C0A144NBEA', # Compensation of employees: Domestic private industries: Retail trade: Motor vehicle and parts dealers
    'N4044C0A144NBEA', # Compensation of employees: Domestic private industries: Retail trade: Other retail
    'N4061C0A144NBEA', # Compensation of employees: Domestic private industries: Securities, commodity contracts, and investments
    'B4055C0A144NBEA', # Compensation of employees: Domestic private industries: Security and commodity brokers
    'J4055C0A144NBEA', # Compensation of employees: Domestic private industries: Security and commodity brokers
    'A4060C0A144NBEA', # Compensation of employees: Domestic private industries: Services
    'H4060C0A144NBEA', # Compensation of employees: Domestic private industries: Services
    'J4060C0A144NBEA', # Compensation of employees: Domestic private industries: Services (DISCONTINUED)
    'B4095C0A144NBEA', # Compensation of employees: Domestic private industries: Services: Commercial and trade schools and employment agencies
    'B4061C0A144NBEA', # Compensation of employees: Domestic private industries: Services: Hotels and other lodging places
    'H4071C0A144NBEA', # Compensation of employees: Domestic private industries: Services: Membership organizations
    'B4066C0A144NBEA', # Compensation of employees: Domestic private industries: Services: Motion pictures
    'J4066C0A144NBEA', # Compensation of employees: Domestic private industries: Services: Motion pictures
    'N4080C0A144NBEA', # Compensation of employees: Domestic private industries: Social assistance
    'B4072C0A144NBEA', # Compensation of employees: Domestic private industries: Social services
    'A4071C0A144NBEA', # Compensation of employees: Domestic private industries: Social services and membership organizations
    'J4071C0A144NBEA', # Compensation of employees: Domestic private industries: Social services and membership organizations
    'N4010C0A144NBEA', # Compensation of employees: Domestic private industries: Support activities for mining
    'N4050C0A144NBEA', # Compensation of employees: Domestic private industries: Transit and ground passenger transportation
    'A4038C0A144NBEA', # Compensation of employees: Domestic private industries: Transportation
    'J4038C0A144NBEA', # Compensation of employees: Domestic private industries: Transportation
    'A4037C0A144NBEA', # Compensation of employees: Domestic private industries: Transportation and public utilities
    'B4049C0A144NBEA', # Compensation of employees: Domestic private industries: Transportation and public utilities: Electric, gas, and sanitary services
    'J4049C0A144NBEA', # Compensation of employees: Domestic private industries: Transportation and public utilities: Electric, gas, and sanitary services
    'N4045C0A144NBEA', # Compensation of employees: Domestic private industries: Transportation and warehousing
    'B4043C0A144NBEA', # Compensation of employees: Domestic private industries: Transportation by air
    'H4043C0A144NBEA', # Compensation of employees: Domestic private industries: Transportation by air
    'J4043C0A144NBEA', # Compensation of employees: Domestic private industries: Transportation by air
    'B4045C0A144NBEA', # Compensation of employees: Domestic private industries: Transportation services
    'H4045C0A144NBEA', # Compensation of employees: Domestic private industries: Transportation services
    'J4045C0A144NBEA', # Compensation of employees: Domestic private industries: Transportation services
    'B4040C0A144NBEA', # Compensation of employees: Domestic private industries: Transportation: Local and interurban passenger transit
    'H4040C0A144NBEA', # Compensation of employees: Domestic private industries: Transportation: Local and interurban passenger transit
    'J4040C0A144NBEA', # Compensation of employees: Domestic private industries: Transportation: Local and interurban passenger transit
    'B4044C0A144NBEA', # Compensation of employees: Domestic private industries: Transportation: Pipelines, except natural gas
    'B4041C0A144NBEA', # Compensation of employees: Domestic private industries: Transportation: Trucking and warehousing
    'N4049C0A144NBEA', # Compensation of employees: Domestic private industries: Truck transportation
    'N4011C0A144NBEA', # Compensation of employees: Domestic private industries: Utilities
    'B4093C0A144NBEA', # Compensation of employees: Domestic private industries: Utilities: electric and gas
    'N4053C0A144NBEA', # Compensation of employees: Domestic private industries: Warehousing and storage
    'N4074C0A144NBEA', # Compensation of employees: Domestic private industries: Waste management and remediation services
    'B4042C0A144NBEA', # Compensation of employees: Domestic private industries: Water transportation
    'H4042C0A144NBEA', # Compensation of employees: Domestic private industries: Water transportation
    'J4042C0A144NBEA', # Compensation of employees: Domestic private industries: Water transportation
    'N4048C0A144NBEA', # Compensation of employees: Domestic private industries: Water transportation
    'B4050C0A144NBEA', # Compensation of employees: Domestic private industries: Wholesale trade
    'H4050C0A144NBEA', # Compensation of employees: Domestic private industries: Wholesale trade
    'N4037C0A144NBEA', # Compensation of employees: Domestic private industries: Wholesale trade
    'J4050C0A144NBEA', # Compensation of employees: Domestic private industries: Wholesale trade (DISCONTINUED)
    'N4038C0A144NBEA', # Compensation of employees: Domestic private industries: Wholesale trade: Durable goods
    'N4039C0A144NBEA', # Compensation of employees: Domestic private industries: Wholesale trade: Nondurable goods
    'B4079C0A144NBEA', # Compensation of employees: Federal general government: Civilian
    'W4080C0A144NBEA', # Compensation of employees: Federal general government: Military
    'B4077C0A144NBEA', # Compensation of employees: Federal government
    'A4081C0A144NBEA', # Compensation of employees: Federal government enterprises
    'A4076C0A144NBEA', # Compensation of employees: Government
    'W506RC0A144NBEA', # Compensation of employees: Households and institutions
    'A4091C0A144NBEA', # Compensation of employees: Nonfarm business
    'C4091C0A144NBEA', # Compensation of employees: Nonfarm business (DISCONTINUED)
    'A4087C0A144NBEA', # Compensation of employees: Rest of the world (DISCONTINUED)
    'B4084C0A144NBEA', # Compensation of employees: State and local general government: Education
    'B4085C0A144NBEA', # Compensation of employees: State and local general government: Other
    'B4082C0A144NBEA', # Compensation of employees: State and local government
    'B4086C0A144NBEA', # Compensation of employees: State and local government enterprises
    'B4189C0A144NBEA', # Current payments to the rest of the world: Income payments: Wage and salary payments (DISCONTINUED)
    'B4188C0A144NBEA', # Current receipts from the rest of the world: Income receipts: Wage and salary receipts (DISCONTINUED)
    'A4002C0A144NBEA', # Gross Domestic Income: Compensation of Employees, Paid (DISCONTINUED)
    'A033RC0A144NBEA', # National income: Compensation of employees (DISCONTINUED)
    'W151RC0A144NBEA', # National income: Households: Compensation of employees (DISCONTINUED)
    'A4187C0A144NBEA', # National income: Rest of the world: Compensation of employees (DISCONTINUED)
    'B568RC0A144NBEA', # Net value added: Net domestic product: General government: Federal (DISCONTINUED)
    'B251RC0A144NBEA', # Net value added: Net domestic product: General government: State and local (DISCONTINUED)

    # Personal Income & Outlays > Employer Contributions (209)
    ## Bil. of $ (NSA)
    'B040RC1A027NBEA', # Compensation of employees: Supplements to wages and salaries: Employer contributions for employee pension and insurance funds
    'B039RC1A027NBEA', # Compensation of employees: Supplements to wages and salaries: Employer contributions for government social insurance
    'A1580C1A027NBEA', # Contributions for government social insurance: Employer contributions: Federal social insurance funds
    'CON1101A027NBEA', # Contributions for government social insurance: Employer contributions: Federal social insurance funds: Old-age, survivors, disability, and hospital insurance
    'A1581C1A027NBEA', # Contributions for government social insurance: Employer contributions: Federal social insurance funds: Unemployment insurance
    'A744RC1A027NBEA', # Contributions for government social insurance: Employer contributions: State and local social insurance funds
    'Y617RC1A027NBEA', # Defined Benefit Pension Plans: Cash flow
    'Y618RC1A027NBEA', # Defined Benefit Pension Plans: Cash flow: Actual employer and household contributions
    'Y620RC1A027NBEA', # Defined Benefit Pension Plans: Cash flow: Benefit payments and withdrawals
    'Y619RC1A027NBEA', # Defined Benefit Pension Plans: Cash flow: Monetary income receipts on assets
    'Q601RC1A027NBEA', # Defined Benefit Pension Plans: Current expenditures, accrual basis
    'Y601RC1A027NBEA', # Defined Benefit Pension Plans: Current receipts, accrual basis
    'Y602RC1A027NBEA', # Defined Benefit Pension Plans: Current receipts, accrual basis: Contributions
    'Y612RC1A027NBEA', # Defined Benefit Pension Plans: Current receipts, accrual basis: Contributions: Claims to benefits accrued through service to employers
    'Y603RC1A027NBEA', # Defined Benefit Pension Plans: Current receipts, accrual basis: Contributions: Claims to benefits accrued through service to employers: Actual employer contributions
    'Y605RC1A027NBEA', # Defined Benefit Pension Plans: Current receipts, accrual basis: Contributions: Claims to benefits accrued through service to employers: Actual household contributions
    'Y610RC1A027NBEA', # Defined Benefit Pension Plans: Current receipts, accrual basis: Income receipts on assets: Dividends
    'Y607RC1A027NBEA', # Defined Benefit Pension Plans: Current receipts, accrual basis: Income receipts on assets: Interest
    'Y608RC1A027NBEA', # Defined Benefit Pension Plans: Current receipts, accrual basis: Income receipts on assets: Interest: Monetary interest
    'Y631RC1A027NBEA', # Defined Benefit Pension Plans: Effect of participation in defined benefit plans on personal income, saving, and wealth: Change in benefit entitlements including implied funding of benefits from holding gains on assets
    'Y628RC1A027NBEA', # Defined Benefit Pension Plans: Effect of participation in defined benefit plans on personal income, saving, and wealth: Change in personal wealth
    'Y622RC1A027NBEA', # Defined Benefit Pension Plans: Effect of participation in defined benefit plans on personal income, saving, and wealth: Effect on personal income
    'Y624RC1A027NBEA', # Defined Benefit Pension Plans: Effect of participation in defined benefit plans on personal income, saving, and wealth: Effect on personal saving
    'Y625RC1A027NBEA', # Defined Benefit Pension Plans: Effect of participation in defined benefit plans on personal income, saving, and wealth: Implied funding of benefits from holding gains on assets
    'Y626RC1A027NBEA', # Defined Benefit Pension Plans: Effect of participation in defined benefit plans on personal income, saving, and wealth: Implied funding of benefits from holding gains on assets: Interest accrued on benefit entitlements
    'Y606RC1A027NBEA', # Defined Benefit Pension Plans: Effect of participation in defined benefit plans on personal income, saving, and wealth: Implied funding of benefits from holding gains on assets: Interest and dividend income received by plans
    'Y218RC1A027NBEA', # Defined Benefit and Defined Contribution Pension Plans: Cash flow
    'Y219RC1A027NBEA', # Defined Benefit and Defined Contribution Pension Plans: Cash flow: Actual employer and household contributions
    'Y204RC1A027NBEA', # Defined Benefit and Defined Contribution Pension Plans: Cash flow: Administrative expenses
    'Y235RC1A027NBEA', # Defined Benefit and Defined Contribution Pension Plans: Cash flow: Benefit payments and withdrawals
    'Y220RC1A027NBEA', # Defined Benefit and Defined Contribution Pension Plans: Cash flow: Monetary income receipts on assets
    'Y212RC1A027NBEA', # Defined Benefit and Defined Contribution Pension Plans: Current expenditures
    'Y632RC1A027NBEA', # Defined Benefit and Defined Contribution Pension Plans: Current expenditures, accrual basis: Net change in benefit entitlements
    'Y233RC1A027NBEA', # Defined Benefit and Defined Contribution Pension Plans: Current expenditures: Imputed income payments on assets to persons: Interest
    'Y201RC1A027NBEA', # Defined Benefit and Defined Contribution Pension Plans: Current receipts
    'Y616RC1A027NBEA', # Defined Benefit and Defined Contribution Pension Plans: Current receipts, accrual basis: Contributions: Claims to benefits accrued through service to employers: Actual household contributions: Pension service charges
    'Y604RC1A027NBEA', # Defined Benefit and Defined Contribution Pension Plans: Current receipts, accrual basis: Contributions: Claims to benefits: Imputed employer contributions
    'Y609RC1A027NBEA', # Defined Benefit and Defined Contribution Pension Plans: Current receipts, accrual basis: Income receipts on assets: Interest: Imputed interest on plans' claims on employers
    'Y202RC1A027NBEA', # Defined Benefit and Defined Contribution Pension Plans: Current receipts: Contributions
    'Y206RC1A027NBEA', # Defined Benefit and Defined Contribution Pension Plans: Current receipts: Contributions: Claims to benefits
    'Y203RC1A027NBEA', # Defined Benefit and Defined Contribution Pension Plans: Current receipts: Contributions: Claims to benefits: Actual employer contributions
    'Y208RC1A027NBEA', # Defined Benefit and Defined Contribution Pension Plans: Current receipts: Contributions: Claims to benefits: Actual household contributions
    'Y209RC1A027NBEA', # Defined Benefit and Defined Contribution Pension Plans: Current receipts: Contributions: Household pension contribution supplements
    'Y234RC1A027NBEA', # Defined Benefit and Defined Contribution Pension Plans: Current receipts: Income receipts on assets: Interest: Dividends
    'Y210RC1A027NBEA', # Defined Benefit and Defined Contribution Pension Plans: Current receipts: Income receipts on assets: Interest: Monetary interest
    'Y232RC1A027NBEA', # Defined Benefit and Defined Contribution Pension Plans: Effect of participation in defined benefit and defined contribution pension plans on personal income, saving, and wealth: Change in personal wealth
    'Y226RC1A027NBEA', # Defined Benefit and Defined Contribution Pension Plans: Effect of participation in defined benefit and defined contribution pension plans on personal income, saving, and wealth: Effect on personal income
    'Y228RC1A027NBEA', # Defined Benefit and Defined Contribution Pension Plans: Effect of participation in defined benefit and defined contribution pension plans on personal income, saving, and wealth: Effect on personal saving
    'Y229RC1A027NBEA', # Defined Benefit and Defined Contribution Pension Plans: Effect of participation in defined benefit and defined contribution pension plans on personal income, saving, and wealth: Implied funding of benefits from holding gains and other changes in assets
    'Y350RC1A027NBEA', # Defined Contribution Pension Plans: Cash flow
    'Y351RC1A027NBEA', # Defined Contribution Pension Plans: Cash flow: Actual employer and household contributions
    'Y353RC1A027NBEA', # Defined Contribution Pension Plans: Cash flow: Benefit payments and withdrawals
    'Y346RC1A027NBEA', # Defined Contribution Pension Plans: Current expenditures
    'Y901RC1A027NBEA', # Defined Contribution Pension Plans: Current expenditures: Imputed income payments on assets to persons: Dividends
    'Y900RC1A027NBEA', # Defined Contribution Pension Plans: Current expenditures: Imputed income payments on assets to persons: Interest
    'Y905RC1A027NBEA', # Defined Contribution Pension Plans: Current expenditures: Net change in assets from current transactions
    'Y338RC1A027NBEA', # Defined Contribution Pension Plans: Current receipts
    'Y339RC1A027NBEA', # Defined Contribution Pension Plans: Current receipts: Contributions
    'Y347RC1A027NBEA', # Defined Contribution Pension Plans: Current receipts: Contributions: Claims to benefits
    'Y340RC1A027NBEA', # Defined Contribution Pension Plans: Current receipts: Contributions: Claims to benefits: Actual employer contributions
    'Y912RC1A027NBEA', # Defined Contribution Pension Plans: Current receipts: Contributions: Claims to benefits: Actual employer contributions: Federal government plans
    'Y934RC1A027NBEA', # Defined Contribution Pension Plans: Current receipts: Contributions: Claims to benefits: Actual employer contributions: Private plans
    'Y955RC1A027NBEA', # Defined Contribution Pension Plans: Current receipts: Contributions: Claims to benefits: Actual employer contributions: State and local government plans
    'Y344RC1A027NBEA', # Defined Contribution Pension Plans: Current receipts: Contributions: Claims to benefits: Actual household contributions
    'Y345RC1A027NBEA', # Defined Contribution Pension Plans: Current receipts: Contributions: Household pension contribution supplements
    'Y349RC1A027NBEA', # Defined Contribution Pension Plans: Current receipts: Output
    'Y355RC1A027NBEA', # Defined Contribution Pension Plans: Effect of participation in defined contribution plans on personal income
    'Y907RC1A027NBEA', # Defined Contribution Pension Plans: Effect of participation in defined contribution plans on personal income, saving, and wealth: Change in personal wealth
    'Y906RC1A027NBEA', # Defined Contribution Pension Plans: Effect of participation in defined contribution plans on personal income, saving, and wealth: Holding gains and other changes in assets
    'Y357RC1A027NBEA', # Defined Contribution Pension Plans: Effect of participation in defined contribution plans on personal saving
    'Y670RC1A027NBEA', # Defined benefit and defined contribution pension plans: Imputed employer contributions: General government
    'Y671RC1A027NBEA', # Defined benefit and defined contribution pension plans: Imputed employer contributions: Government enterprises
    'Y673RC1A027NBEA', # Defined benefit and defined contribution pension plans: Imputed household contributions and contribution supplements
    'Y672RC1A027NBEA', # Defined benefit and defined contribution pension plans: Imputed interest on plans' claims on employers: Government
    'L313051A027NBEA', # Government social insurance funds: Current federal receipts: Contributions for government social insurance: Employer contributions: Government
    'L313061A027NBEA', # Government social insurance funds: Current federal receipts: Contributions for government social insurance: Employer contributions: Other
    'B739RC1A027NBEA', # Government social insurance funds: Current state and local receipts: Contributions for government social insurance: Employer contributions: Government
    'B740RC1A027NBEA', # Government social insurance funds: Current state and local receipts: Contributions for government social insurance: Employer contributions: Other
    'Y253RC1A027NBEA', # Private Defined Benefit Pension Plan: Cash flow
    'Y254RC1A027NBEA', # Private Defined Benefit Pension Plan: Cash flow: Actual employer and household contributions
    'Y256RC1A027NBEA', # Private Defined Benefit Pension Plan: Cash flow: Benefit payments and withdrawals
    'Y255RC1A027NBEA', # Private Defined Benefit Pension Plan: Cash flow: Monetary income receipts on assets
    'Q237RC1A027NBEA', # Private Defined Benefit Pension Plan: Current expenditures, accrual basis
    'Y246RC1A027NBEA', # Private Defined Benefit Pension Plan: Current expenditures, accrual basis: Imputed income payments on assets to persons: Dividends
    'Y243RC1A027NBEA', # Private Defined Benefit Pension Plan: Current expenditures, accrual basis: Imputed income payments on assets to persons: Interest
    'Y252RC1A027NBEA', # Private Defined Benefit Pension Plan: Current expenditures, accrual basis: Net change in benefit entitlements
    'Y237RC1A027NBEA', # Private Defined Benefit Pension Plan: Current receipts, accrual basis
    'Y238RC1A027NBEA', # Private Defined Benefit Pension Plan: Current receipts, accrual basis: Contributions
    'Y248RC1A027NBEA', # Private Defined Benefit Pension Plan: Current receipts, accrual basis: Contributions: Claims to benefits accrued through service to employers
    'W350RC1A027NBEA', # Private Defined Benefit Pension Plan: Current receipts, accrual basis: Contributions: Claims to benefits accrued through service to employers: Actual employer contributions
    'Y240RC1A027NBEA', # Private Defined Benefit Pension Plan: Current receipts, accrual basis: Contributions: Claims to benefits accrued through service to employers: Imputed employer contributions
    'Y245RC1A027NBEA', # Private Defined Benefit Pension Plan: Current receipts, accrual basis: Income receipts on assets: Interest: Imputed interest on plans' claims on employers
    'Y244RC1A027NBEA', # Private Defined Benefit Pension Plan: Current receipts, accrual basis: Income receipts on assets: Interest: Monetary interest
    'Y257RC1A027NBEA', # Private Defined Benefit Pension Plan: Current receipts, accrual basis: Output
    'Y267RC1A027NBEA', # Private Defined Benefit Pension Plan: Effect of participation in defined benefit plans on personal income, saving, and wealth: Change in benefit entitlements including implied funding of benefits from holding gains on assets
    'Y264RC1A027NBEA', # Private Defined Benefit Pension Plan: Effect of participation in defined benefit plans on personal income, saving, and wealth: Change in personal wealth
    'Y258RC1A027NBEA', # Private Defined Benefit Pension Plan: Effect of participation in defined benefit plans on personal income, saving, and wealth: Effect on personal income
    'Y260RC1A027NBEA', # Private Defined Benefit Pension Plan: Effect of participation in defined benefit plans on personal income, saving, and wealth: Effect on personal saving
    'Y241RC1A027NBEA', # Private Defined Benefit Pension Plan: Effect of participation in defined benefit plans on personal income, saving, and wealth: Household actual contributions
    'Y261RC1A027NBEA', # Private Defined Benefit Pension Plan: Effect of participation in defined benefit plans on personal income, saving, and wealth: Implied funding of benefits from holding gains on assets
    'Y262RC1A027NBEA', # Private Defined Benefit Pension Plan: Effect of participation in defined benefit plans on personal income, saving, and wealth: Implied funding of benefits from holding gains on assets: Interest accrued on benefit entitlements
    'Y242RC1A027NBEA', # Private Defined Benefit Pension Plan: Effect of participation in defined benefit plans on personal income, saving, and wealth: Implied funding of benefits from holding gains on assets: Interest and dividend income received by plans
    'L319261A027NBEA', # State and Local government current expenditures: Coverage differences: State and local employee retirement plan transactions: Employer contributions to own retirement plans (NIPA vs. Census)
    'L319381A027NBEA', # State and Local government current expenditures: Netting and grossing differences: Employer contributions to own social insurance funds
    'L319181A027NBEA', # State and Local government current receipts: Netting and grossing differences: Employer contributions to own social insurance funds (DISCONTINUED)
    ## Mil. of $ (NSA)
    'B040RC0A144NBEA', # Compensation of employees: Supplements to wages and salaries: Employer contributions for employee pension and insurance funds (DISCONTINUED)
    'B039RC0A144NBEA', # Compensation of employees: Supplements to wages and salaries: Employer contributions for government social insurance (DISCONTINUED)
    'Y235RC0A144NBEA', # Defined Benefit and Defined Contribution Pension Plans: Cash flow: Benefit payments and withdrawals (DISCONTINUED)
    'Y392RC0A144NBEA', # Employer Contributions for Employee Pension and Insurance Funds: Pension plans: Government employee pension plans: Federal
    'Y696RC0A144NBEA', # Employer Contributions for Employee Pension and Insurance Funds: Pension plans: Private pension plans: Defined benefit
    'B4928C0A144NBEA', # Employer contributions for employee pension and insurance funds: Benefits paid by pension and insurance funds
    'B4903C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries
    'B4904C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Agriculture, forestry, and fishing
    'N4904C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Agriculture, forestry, fishing, and hunting
    'N4919C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Arts, entertainment, recreation, accommodation, and food services
    'B4912C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Communication
    'B4906C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Construction
    'N4907C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Construction
    'N4918C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Educational services, health care, and social assistance
    'B4916C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Finance, insurance, and real estate
    'J4916C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Finance, insurance, and real estate
    'N4915C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Finance, insurance, real estate, rental, and leasing
    'N4914C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Information
    'B4907C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Manufacturing
    'N4908C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Manufacturing
    'B4908C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Manufacturing: Durable goods
    'J4908C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Manufacturing: Durable goods
    'N4909C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Manufacturing: Durable goods
    'B4909C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Manufacturing: Nondurable goods
    'J4909C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Manufacturing: Nondurable goods
    'N4910C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Manufacturing: Nondurable goods
    'B4905C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Mining
    'N4905C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Mining
    'N4929C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Other services, except government
    'N4916C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Professional and business services
    'B4915C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Retail trade
    'J4915C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Retail trade
    'N4912C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Retail trade
    'B4917C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Services
    'J4917C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Services
    'B4911C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Transportation
    'J4911C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Transportation
    'B4910C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Transportation and public utilities
    'B4913C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Transportation and public utilities: Electric, gas, and sanitary services
    'J4913C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Transportation and public utilities: Electric, gas, and sanitary services
    'N4913C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Transportation and warehousing
    'N4906C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Utilities
    'B4914C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Wholesale trade
    'J4914C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Wholesale trade
    'N4911C0A144NBEA', # Employer contributions for employee pension and insurance funds: Domestic private industries: Wholesale trade
    'B4918C0A144NBEA', # Employer contributions for employee pension and insurance funds: Government
    'B4934C0A144NBEA', # Employer contributions for employee pension and insurance funds: Pension and profit-sharing
    'B4936C0A144NBEA', # Employer contributions for employee pension and insurance funds: Private insurance funds
    'W351RC0A144NBEA', # Employer contributions for employee pension and insurance funds: Private pension and profit-sharing: Defined contribution pension and profit-sharing
    'B4935C0A144NBEA', # Employer contributions for employee pension and insurance funds: Publicly administered government employee retirement plans
    'B4802C0A144NBEA', # Employer contributions for government social insurance: Domestic industries
    'B4803C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries
    'B4804C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Agriculture, forestry, and fishing
    'N4804C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Agriculture, forestry, fishing, and hunting
    'N4829C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Arts, entertainment, recreation, accommodation, and food services
    'J4812C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Communication
    'B4812C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Communications
    'B4806C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Construction
    'N4807C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Construction
    'N4828C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Educational services, health care, and social assistance
    'N4815C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Finance and insurance, real estate, rental, and leasing
    'B4816C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Finance, insurance, and real estate
    'J4816C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Finance, insurance, and real estate
    'N4814C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Information
    'B4807C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Manufacturing
    'N4808C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Manufacturing
    'B4808C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Manufacturing: Durable goods
    'J4808C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Manufacturing: Durable goods
    'N4809C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Manufacturing: Durable goods
    'B4809C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Manufacturing: Nondurable goods
    'J4809C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Manufacturing: Nondurable goods
    'N4810C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Manufacturing: Nondurable goods
    'B4805C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Mining
    'N4805C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Mining
    'N4830C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Other services, except government
    'N4816C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Professional, and business services
    'B4815C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Retail trade
    'J4815C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Retail trade
    'N4812C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Retail trade
    'B4817C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Services
    'J4817C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Services
    'B4811C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Transportation
    'J4811C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Transportation
    'B4810C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Transportation and public utilities
    'B4813C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Transportation and public utilities: Electric, gas, and sanitary services
    'J4813C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Transportation and public utilities: Electric, gas, and sanitary services
    'N4813C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Transportation and warehousing
    'N4806C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Utilities
    'B4814C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Wholesale trade
    'J4814C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Wholesale trade
    'N4811C0A144NBEA', # Employer contributions for government social insurance: Domestic private industries: Wholesale trade
    'B4818C0A144NBEA', # Employer contributions for government social insurance: Government
    'B4922C0A144NBEA', # Employment-related imputations: Employer contributions for health and life insurance (DISCONTINUED)
    'W350RC0A144NBEA', # Private Defined Benefit Pension Plan: Current receipts, accrual basis: Contributions: Claims to benefits accrued through service to employers: Actual employer contributions (DISCONTINUED)
    'Y390RC0A144NBEA', # Supplements to Wages and Salaries: Health insurance: Publicly administered government employee insurance funds (DISCONTINUED)
    'Y239RC0A144NBEA', # Supplements to Wages and Salaries: Pension and other employee benefit plans: State and local employee retirement (DISCONTINUED)
    'B4923C0A144NBEA', # Supplements to wages and salaries: Health insurance: Private group health insurance (DISCONTINUED)
    'B4924C0A144NBEA', # Supplements to wages and salaries: Life insurance: Private group life insurance (DISCONTINUED)
    'B4945C0A144NBEA', # Supplements to wages and salaries: Pension, profit-sharing, and other retirement benefit plans: Federal civilian employee retirement (DISCONTINUED)
    'B1583C0A144NBEA', # Supplements to wages and salaries: Pension, profit-sharing, and other retirement benefit plans: Federal military employee retirement (DISCONTINUED)
    'B4921C0A144NBEA', # Supplements to wages and salaries: Pension, profit-sharing, and other retirement benefit plans: Private pension and profit-sharing (DISCONTINUED)
    'S251100A144NBEA', # Supplements to wages and salaries: Pension, profit-sharing, and other retirement benefit plans: State and local employee retirement (DISCONTINUED)
    'B4926C0A144NBEA', # Supplements to wages and salaries: Private supplemental unemployment insurance (DISCONTINUED)
    'B4925C0A144NBEA', # Supplements to wages and salaries: Workers' compensation: Private insurance (DISCONTINUED)

    # Personal Income & Outlays > Personal Consumption Expenditures (536)
    ## $ (NSA)
    'USPCEPCG', # Per Capita Personal Consumption Expenditures: Goods for United States
    'USPCEPCDURG', # Per Capita Personal Consumption Expenditures: Goods: Durable Goods for United States
    'USPCEPCFUR', # Per Capita Personal Consumption Expenditures: Goods: Durable Goods: Furnishings and Durable Household Equipment for United States
    'USPCEPCVEH', # Per Capita Personal Consumption Expenditures: Goods: Durable Goods: Motor Vehicles and Parts for United States
    'USPCEPCODURG', # Per Capita Personal Consumption Expenditures: Goods: Durable Goods: Other Durable Goods for United States
    'USPCEPCRECGD', # Per Capita Personal Consumption Expenditures: Goods: Durable Goods: Recreational Goods and Vehicles for United States
    'USPCEPCNDURG', # Per Capita Personal Consumption Expenditures: Nondurable Goods for United States
    'USPCEPCCLTH', # Per Capita Personal Consumption Expenditures: Nondurable Goods: Clothing and Footwear for United States
    'USPCEPCFOOD', # Per Capita Personal Consumption Expenditures: Nondurable Goods: Food and Beverages Purchased for Off-Premises Consumption for United States
    'USPCEPCGAS', # Per Capita Personal Consumption Expenditures: Nondurable Goods: Gasoline and Other Energy Goods for United States
    'USPCEPCONDURG', # Per Capita Personal Consumption Expenditures: Nondurable Goods: Other Nondurable Goods for United States
    'USPCEPCSRV', # Per Capita Personal Consumption Expenditures: Services for United States
    'USPCEPCFCENPISH', # Per Capita Personal Consumption Expenditures: Services: Final Consumption Expenditures of Nonprofit Institutions Serving Households for United States
    'USPCEPCGONPI', # Per Capita Personal Consumption Expenditures: Services: Final Consumption Expenditures of Nonprofit Institutions Serving Households: Gross Output of Nonprofit Institutions for United States
    'USPCEPCLRPTSLSGSNPIS', # Per Capita Personal Consumption Expenditures: Services: Final Consumption Expenditures of Nonprofit Institutions Serving Households: Less: Receipts from Sales of Goods and Services by Nonprofit Institutions for United States
    'USPCEPCFININS', # Per Capita Personal Consumption Expenditures: Services: Financial Services and Insurance for United States
    'USPCEPCFDSRVACCMD', # Per Capita Personal Consumption Expenditures: Services: Food Services and Accommodations for United States
    'USPCEPCHLTHCARE', # Per Capita Personal Consumption Expenditures: Services: Health Care for United States
    'USPCEPCHCE', # Per Capita Personal Consumption Expenditures: Services: Household Consumption Expenditures for Services for United States
    'USPCEPCHOUSUTL', # Per Capita Personal Consumption Expenditures: Services: Housing and Utilities for United States
    'USPCEPCOSRV', # Per Capita Personal Consumption Expenditures: Services: Other Services for United States
    'USPCEPCSRECSRV', # Per Capita Personal Consumption Expenditures: Services: Recreation Services for United States
    'USPCEPCTRANS', # Per Capita Personal Consumption Expenditures: Services: Transportation Services for United States
    'USPCEPC', # Per Capita Personal Consumption Expenditures: Total for United States
    'A794RC0A052NBEA', # Personal consumption expenditures per capita
    'AGDSRC0A052NBEA', # Personal consumption expenditures per capita: Goods
    'A795RC0A052NBEA', # Personal consumption expenditures per capita: Goods: Durable goods
    'A796RC0A052NBEA', # Personal consumption expenditures per capita: Goods: Nondurable goods
    'A797RC0A052NBEA', # Personal consumption expenditures per capita: Services
    ## % Chg. from Preceding Period (NSA)
    'DPCMRL1A225NBEA', # Real Market-based PCE
    'DPCXRL1A225NBEA', # Real Market-based PCE Excluding Food and Energy
    'AB61RL1A225NBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Personal Consumption Expenditures
    'W240RL1A225NBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Personal Consumption Expenditures: Net Purchases of Used Autos and Used Light Trucks
    'B137RL1A225NBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Personal Consumption Expenditures: Net Purchases of Used Autos and Used Light Trucks: Used Autos
    'W241RL1A225NBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Personal Consumption Expenditures: Net Purchases of Used Autos and Used Light Trucks: Used Light Trucks (including Utility Vehicles)
    'AB67RL1A225NBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Personal Consumption Expenditures: New Motor Vehicles
    'A136RL1A225NBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Personal Consumption Expenditures: New Motor Vehicles: Autos
    'B704RL1A225NBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Personal Consumption Expenditures: New Motor Vehicles: Light Trucks (including Utility Vehicles)
    'DPCERL1A225NBEA', # Real Personal Consumption Expenditures
    'DPCCRL1A225NBEA', # Real Personal Consumption Expenditures (PCE) Excluding Food and Energy
    'PB001176A', # Real Personal Consumption Expenditures (PCE) Excluding Food, Energy, and Housing
    'DNRGRL1A225NBEA', # Real Personal Consumption Expenditures (PCE): Energy Goods and Services
    'DGDSRL1A225NBEA', # Real Personal Consumption Expenditures: Goods
    'DDURRL1A225NBEA', # Real Personal Consumption Expenditures: Goods: Durable Goods
    'DFDHRL1A225NBEA', # Real Personal Consumption Expenditures: Goods: Durable Goods: Furnishings and Durable Household Equipment
    'DMOTRL1A225NBEA', # Real Personal Consumption Expenditures: Goods: Durable Goods: Motor Vehicles and Parts
    'DODGRL1A225NBEA', # Real Personal Consumption Expenditures: Goods: Durable Goods: Other Durable Goods
    'DREQRL1A225NBEA', # Real Personal Consumption Expenditures: Goods: Durable Goods: Recreational Goods and Vehicles
    'DNDGRL1A225NBEA', # Real Personal Consumption Expenditures: Goods: Nondurable Goods
    'DCLORL1A225NBEA', # Real Personal Consumption Expenditures: Goods: Nondurable Goods: Clothing and Footwear
    'DFXARL1A225NBEA', # Real Personal Consumption Expenditures: Goods: Nondurable Goods: Food and Beverages Purchased for Off-premises Consumption
    'DGOERL1A225NBEA', # Real Personal Consumption Expenditures: Goods: Nondurable Goods: Gasoline and Other Energy Goods
    'DONGRL1A225NBEA', # Real Personal Consumption Expenditures: Goods: Nondurable Goods: Other Nondurable Goods
    'DSERRL1A225NBEA', # Real Personal Consumption Expenditures: Services
    'PB001260A', # Real Personal Consumption Expenditures: Services Excluding Energy and Housing
    'DNPIRL1A225NBEA', # Real Personal Consumption Expenditures: Services: Final Consumption Expenditures of Nonprofit Institutions Serving Households (NPISHs)
    'DNPERL1A225NBEA', # Real Personal Consumption Expenditures: Services: Final Consumption Expenditures of Nonprofit Institutions Serving Households (NPISHs): Gross Output of Nonprofit Institutions
    'DHCERL1A225NBEA', # Real Personal Consumption Expenditures: Services: Household Consumption Expenditures (for Services)
    'DIFSRL1A225NBEA', # Real Personal Consumption Expenditures: Services: Household Consumption Expenditures (for Services): Financial Services and Insurance
    'DFSARL1A225NBEA', # Real Personal Consumption Expenditures: Services: Household Consumption Expenditures (for Services): Food Services and Accommodations
    'DHLCRL1A225NBEA', # Real Personal Consumption Expenditures: Services: Household Consumption Expenditures (for Services): Health Care
    'DHUTRL1A225NBEA', # Real Personal Consumption Expenditures: Services: Household Consumption Expenditures (for Services): Housing and Utilities
    'DOTSRL1A225NBEA', # Real Personal Consumption Expenditures: Services: Household Consumption Expenditures (for Services): Other Services
    'DRCARL1A225NBEA', # Real Personal Consumption Expenditures: Services: Household Consumption Expenditures (for Services): Recreation Services
    'DTRSRL1A225NBEA', # Real Personal Consumption Expenditures: Services: Household Consumption Expenditures (for Services): Transportation Services
    'DNPSRL1A225NBEA', # Real Personal Consumption Expenditures: Services: Receipts from Sales of Goods and Services by Nonprofit Institutions
    ## Bil. of $ (NSA)
    'A135RC1A027NBEA', # Automobile output: Personal consumption expenditures
    'AB61RC1A027NBEA', # Motor vehicle output: Personal consumption expenditures
    'DPCCRC1A027NBEA', # Personal consumption expenditures excluding food and energy
    'DEXFRC1A027NBEA', # Personal consumption expenditures in the United States by nonresidents
    'DPRORC1A027NBEA', # Personal consumption expenditures: Accounting and other business services
    'DADMRC1A027NBEA', # Personal consumption expenditures: Admissions to specified spectator amusements
    'DLIGRC1A027NBEA', # Personal consumption expenditures: Admissions to specified spectator amusements: Live entertainment, excluding sports
    'DMOVRC1A027NBEA', # Personal consumption expenditures: Admissions to specified spectator amusements: Motion picture theaters
    'DSPERC1A027NBEA', # Personal consumption expenditures: Admissions to specified spectator amusements: Spectator sports
    'DORSRC1A027NBEA', # Personal consumption expenditures: Amusements parks, campgrounds, and related recreational services
    'DCRCRC1A027NBEA', # Personal consumption expenditures: Cleaning, repair, and rental of clothing
    'DCLTRC1A027NBEA', # Personal consumption expenditures: Clothing
    'DLGRRC1A027NBEA', # Personal consumption expenditures: Clothing repair, rental, and alterations
    'DCAFRC1A027NBEA', # Personal consumption expenditures: Clothing, footwear, and related services
    'DOCMRC1A027NBEA', # Personal consumption expenditures: Clothing: Other clothing materials
    'DCMCRC1A027NBEA', # Personal consumption expenditures: Communication
    'DPSTRC1A027NBEA', # Personal consumption expenditures: Communication: First-class postal service by U.S. Postal Service (USPS)
    'DEBKRC1A027NBEA', # Personal consumption expenditures: Durable goods: Educational books
    'DFDHRC1A027NBEA', # Personal consumption expenditures: Durable goods: Furnishings and durable household equipment
    'DFFFRC1A027NBEA', # Personal consumption expenditures: Durable goods: Furniture and furnishings
    'DUTERC1A027NBEA', # Personal consumption expenditures: Durable goods: Glassware, tableware, and household utensils
    'DAPPRC1A027NBEA', # Personal consumption expenditures: Durable goods: Household appliances
    'DJRYRC1A027NBEA', # Personal consumption expenditures: Durable goods: Jewelry and watches
    'DLUGRC1A027NBEA', # Personal consumption expenditures: Durable goods: Luggage and similar personal items
    'DMVPRC1A027NBEA', # Personal consumption expenditures: Durable goods: Motor vehicle parts and accessories
    'DMOTRC1A027NBEA', # Personal consumption expenditures: Durable goods: Motor vehicles and parts
    'DMSCRC1A027NBEA', # Personal consumption expenditures: Durable goods: Musical instruments
    'DNPVRC1A027NBEA', # Personal consumption expenditures: Durable goods: Net purchases of used motor vehicles
    'DNMVRC1A027NBEA', # Personal consumption expenditures: Durable goods: New motor vehicles
    'DODGRC1A027NBEA', # Personal consumption expenditures: Durable goods: Other durable goods
    'DRBKRC1A027NBEA', # Personal consumption expenditures: Durable goods: Recreational books
    'DREQRC1A027NBEA', # Personal consumption expenditures: Durable goods: Recreational goods and vehicles
    'DSPGRC1A027NBEA', # Personal consumption expenditures: Durable goods: Sporting equipment, supplies, guns, and ammunition
    'DWHLRC1A027NBEA', # Personal consumption expenditures: Durable goods: Sports and recreational vehicles
    'DTCERC1A027NBEA', # Personal consumption expenditures: Durable goods: Telephone and related communication equipment
    'DTAERC1A027NBEA', # Personal consumption expenditures: Durable goods: Therapeutic appliances and equipment
    'DTOORC1A027NBEA', # Personal consumption expenditures: Durable goods: Tools and equipment for house and garden
    'DVAPRC1A027NBEA', # Personal consumption expenditures: Durable goods: Video, audio, photographic, and information processing equipment and media
    'DEDURC1A027NBEA', # Personal consumption expenditures: Education
    'DTEDRC1A027NBEA', # Personal consumption expenditures: Education services
    'DNRGRC1A027NBEA', # Personal consumption expenditures: Energy goods and services
    'DFNLRC1A027NBEA', # Personal consumption expenditures: Financial services
    'DIFSRC1A027NBEA', # Personal consumption expenditures: Financial services and insurance
    'DIMPRC1A027NBEA', # Personal consumption expenditures: Financial services furnished without payment
    'DFSERC1A027NBEA', # Personal consumption expenditures: Food services
    'DFTWRC1A027NBEA', # Personal consumption expenditures: Footwear
    'DFTRRC1A027NBEA', # Personal consumption expenditures: Foreign travel by U.S. residents
    'DFUNRC1A027NBEA', # Personal consumption expenditures: Funeral and burial services
    'DFHHRC1A027NBEA', # Personal consumption expenditures: Furnishings, household equipment, and routine household maintenance
    'DGDSRC1A027NBEA', # Personal consumption expenditures: Goods
    'DHLTRC1A027NBEA', # Personal consumption expenditures: Health
    'DOUTRC1A027NBEA', # Personal consumption expenditures: Health care: Outpatient services
    'DDENRC1A027NBEA', # Personal consumption expenditures: Health care: Outpatient services: Dental services
    'DPMSRC1A027NBEA', # Personal consumption expenditures: Health care: Outpatient services: Paramedical services
    'DPHYRC1A027NBEA', # Personal consumption expenditures: Health care: Outpatient services: Physician services
    'DHHCRC1A027NBEA', # Personal consumption expenditures: Home health care
    'DHPNRC1A027NBEA', # Personal consumption expenditures: Hospital and nursing home services
    'DHAPRC1A027NBEA', # Personal consumption expenditures: Household appliances
    'DPHCRC1A027NBEA', # Personal consumption expenditures: Household consumption expenditures
    'DFURRC1A027NBEA', # Personal consumption expenditures: Household consumption expenditures: Furniture, furnishings, and floor coverings
    'DOGSRC1A027NBEA', # Personal consumption expenditures: Household consumption expenditures: Other household goods and services
    'DTEXRC1A027NBEA', # Personal consumption expenditures: Household textiles
    'DUTFRC1A027NBEA', # Personal consumption expenditures: Household utilities and fuels
    'DEGFRC1A027NBEA', # Personal consumption expenditures: Household utilities and fuels: Electricity, gas, and other fuels
    'DHUFRC1A027NBEA', # Personal consumption expenditures: Housing, utilities, and fuels
    'DUNSRC1A027NBEA', # Personal consumption expenditures: Labor organization dues
    'DDRYRC1A027NBEA', # Personal consumption expenditures: Laundry and dry cleaning services
    'DGALRC1A027NBEA', # Personal consumption expenditures: Legal services
    'DNBSRC1A027NBEA', # Personal consumption expenditures: Magazines, newspapers, books, and stationery
    'DRRERC1A027NBEA', # Personal consumption expenditures: Maintenance and repair of recreational vehicles and sports equipment
    'DPCMRC1A027NBEA', # Personal consumption expenditures: Market-based
    'DPCXRC1A027NBEA', # Personal consumption expenditures: Market-based, excluding food and energy
    'DMPARC1A027NBEA', # Personal consumption expenditures: Medical products, appliances, and equipment
    'DMDFRC1A027NBEA', # Personal consumption expenditures: Membership clubs and participant sports centers
    'DMVORC1A027NBEA', # Personal consumption expenditures: Motor vehicle operation
    'DMVSRC1A027NBEA', # Personal consumption expenditures: Motor vehicle services
    'DMUSRC1A027NBEA', # Personal consumption expenditures: Museums and libraries
    'DFORRC1A027NBEA', # Personal consumption expenditures: Net foreign travel (Foreign travel by U.S. residents less expenditures in the U. S. by nonresidents)
    'DNFTRC1A027NBEA', # Personal consumption expenditures: Net foreign travel and expenditures abroad by U.S. residents
    'DIINRC1A027NBEA', # Personal consumption expenditures: Net health insurance: Income loss
    'DMINRC1A027NBEA', # Personal consumption expenditures: Net health insurance: Medical care and hospitalization
    'DPWCRC1A027NBEA', # Personal consumption expenditures: Net health insurance: Workers' compensation
    'A137RC1A027NBEA', # Personal consumption expenditures: Net purchases of used autos
    'W240RC1A027NBEA', # Personal consumption expenditures: Net purchases of used autos and used light trucks
    'W241RC1A027NBEA', # Personal consumption expenditures: Net purchases of used light trucks (including utility vehicles)
    'A136RC1A027NBEA', # Personal consumption expenditures: New autos
    'AB67RC1A027NBEA', # Personal consumption expenditures: New motor vehicles
    'B704RC1A027NBEA', # Personal consumption expenditures: New motor vehicles: Light trucks (including utility vehicles)
    'DAOPRC1A027NBEA', # Personal consumption expenditures: Nondurable goods: Alcoholic beverages purchased for off-premises consumption
    'DCICRC1A027NBEA', # Personal consumption expenditures: Nondurable goods: Children's and infants' clothing
    'DCLORC1A027NBEA', # Personal consumption expenditures: Nondurable goods: Clothing and footwear
    'DFXARC1A027NBEA', # Personal consumption expenditures: Nondurable goods: Food and beverages purchased for off-premises consumption
    'DTFDRC1A027NBEA', # Personal consumption expenditures: Nondurable goods: Food and nonalcoholic beverages purchased for off-premises consumption
    'DFFDRC1A027NBEA', # Personal consumption expenditures: Nondurable goods: Food produced and consumed on farms
    'DFULRC1A027NBEA', # Personal consumption expenditures: Nondurable goods: Fuel oil and other fuels
    'DGARRC1A027NBEA', # Personal consumption expenditures: Nondurable goods: Garments
    'DGOERC1A027NBEA', # Personal consumption expenditures: Nondurable goods: Gasoline and other energy goods
    'DHOURC1A027NBEA', # Personal consumption expenditures: Nondurable goods: Household supplies
    'DNEWRC1A027NBEA', # Personal consumption expenditures: Nondurable goods: Magazines, newspapers, and stationery
    'DMBCRC1A027NBEA', # Personal consumption expenditures: Nondurable goods: Men's and boys' clothing
    'DMFLRC1A027NBEA', # Personal consumption expenditures: Nondurable goods: Motor vehicle fuels, lubricants, and fluids
    'DOCCRC1A027NBEA', # Personal consumption expenditures: Nondurable goods: Other clothing materials and footwear
    'DONGRC1A027NBEA', # Personal consumption expenditures: Nondurable goods: Other nondurable goods
    'DOPCRC1A027NBEA', # Personal consumption expenditures: Nondurable goods: Personal care products
    'DPHMRC1A027NBEA', # Personal consumption expenditures: Nondurable goods: Pharmaceutical and other medical products
    'DREIRC1A027NBEA', # Personal consumption expenditures: Nondurable goods: Recreational items
    'DTOBRC1A027NBEA', # Personal consumption expenditures: Nondurable goods: Tobacco
    'DWGCRC1A027NBEA', # Personal consumption expenditures: Nondurable goods: Women's and girls' clothing
    'DOISRC1A027NBEA', # Personal consumption expenditures: Other goods and services - personal care, social and religious, professional, funeral and burial, and tobacco
    'DOMPRC1A027NBEA', # Personal consumption expenditures: Other medical products
    'DOVSRC1A027NBEA', # Personal consumption expenditures: Other motor vehicle services
    'DNFRRC1A027NBEA', # Personal consumption expenditures: Other nondurable goods: Net expenditures abroad by U.S. residents
    'DOTRRC1A027NBEA', # Personal consumption expenditures: Other recreational services - food, transportation insurance, and household insurance
    'DOTSRC1A027NBEA', # Personal consumption expenditures: Other services
    'DMLBRC1A027NBEA', # Personal consumption expenditures: Outpatient services: Paramedical services: Medical laboratories
    'DOMDRC1A027NBEA', # Personal consumption expenditures: Outpatient services: Paramedical services: Other professional medical services
    'DXHLRC1A027NBEA', # Personal consumption expenditures: Package tours
    'DPCRRC1A027NBEA', # Personal consumption expenditures: Personal care
    'DPERRC1A027NBEA', # Personal consumption expenditures: Personal care and clothing services
    'DPEORC1A027NBEA', # Personal consumption expenditures: Personal items
    'DPETRC1A027NBEA', # Personal consumption expenditures: Pets, pet products, and related services
    'DPNPRC1A027NBEA', # Personal consumption expenditures: Pharmaceutical products
    'DPHORC1A027NBEA', # Personal consumption expenditures: Photographic goods and services
    'DPSSRC1A027NBEA', # Personal consumption expenditures: Postal and delivery services
    'DODSRC1A027NBEA', # Personal consumption expenditures: Postal and delivery services: Other delivery services (by non-USPS facilities)
    'DPRSRC1A027NBEA', # Personal consumption expenditures: Professional and other services
    'DAXSRC1A027NBEA', # Personal consumption expenditures: Professional association dues
    'DRRLRC1A027NBEA', # Personal consumption expenditures: Recreation
    'DRCARC1A027NBEA', # Personal consumption expenditures: Recreation services
    'DAVPRC1A027NBEA', # Personal consumption expenditures: Recreation services: Audio-video, photographic, and information processing equipment services
    'DSVCRC1A027NBEA', # Personal consumption expenditures: Services related to video and audio goods and computers
    'DACCRC1A027NBEA', # Personal consumption expenditures: Services: Accommodations
    'DVEDRC1A027NBEA', # Personal consumption expenditures: Services: Commercial and vocational schools
    'DCOMRC1A027NBEA', # Personal consumption expenditures: Services: Communication
    'DNPIRC1A027NBEA', # Personal consumption expenditures: Services: Final consumption expenditures of nonprofit institutions serving households (NPISHs)
    'DOFIRC1A027NBEA', # Personal consumption expenditures: Services: Financial service charges, fees, and commissions
    'DFOORC1A027NBEA', # Personal consumption expenditures: Services: Food furnished to employees (including military)
    'DFSARC1A027NBEA', # Personal consumption expenditures: Services: Food services and accommodations
    'DGAMRC1A027NBEA', # Personal consumption expenditures: Services: Gambling
    'DNPERC1A027NBEA', # Personal consumption expenditures: Services: Gross output of nonprofit institutions
    'DHLCRC1A027NBEA', # Personal consumption expenditures: Services: Health care
    'DHEDRC1A027NBEA', # Personal consumption expenditures: Services: Higher education
    'DHSPRC1A027NBEA', # Personal consumption expenditures: Services: Hospitals
    'DHCERC1A027NBEA', # Personal consumption expenditures: Services: Household consumption expenditures
    'DAITRC1A027NBEA', # Personal consumption expenditures: Services: Household consumption expenditures: Transportation services: Public transportation: Air transportation
    'DHHMRC1A027NBEA', # Personal consumption expenditures: Services: Household maintenance
    'DUTLRC1A027NBEA', # Personal consumption expenditures: Services: Household utilities
    'DELCRC1A027NBEA', # Personal consumption expenditures: Services: Household utilities: Electricity
    'DELGRC1A027NBEA', # Personal consumption expenditures: Services: Household utilities: Electricity and gas
    'DGHERC1A027NBEA', # Personal consumption expenditures: Services: Household utilities: Natural gas
    'DWRSRC1A027NBEA', # Personal consumption expenditures: Services: Household utilities: Water supply and sanitation
    'DHUTRC1A027NBEA', # Personal consumption expenditures: Services: Housing and utilities
    'DHSGRC1A027NBEA', # Personal consumption expenditures: Services: Housing and utilities: Housing
    'DGRHRC1A027NBEA', # Personal consumption expenditures: Services: Housing: Group housing
    'DOWNRC1A027NBEA', # Personal consumption expenditures: Services: Housing: Imputed rental of owner-occupied nonfarm housing
    'DTENRC1A027NBEA', # Personal consumption expenditures: Services: Housing: Rental of tenant-occupied nonfarm housing
    'DFARRC1A027NBEA', # Personal consumption expenditures: Services: Housing: Rental value of farm dwellings
    'DINSRC1A027NBEA', # Personal consumption expenditures: Services: Insurance
    'DINTRC1A027NBEA', # Personal consumption expenditures: Services: Internet access
    'DLIFRC1A027NBEA', # Personal consumption expenditures: Services: Life insurance
    'DRLSRC1A027NBEA', # Personal consumption expenditures: Services: Membership clubs, sports centers, parks, theaters, and museums
    'DVMRRC1A027NBEA', # Personal consumption expenditures: Services: Motor vehicle maintenance and repair
    'DHINRC1A027NBEA', # Personal consumption expenditures: Services: Net health insurance
    'DFINRC1A027NBEA', # Personal consumption expenditures: Services: Net household insurance
    'DTINRC1A027NBEA', # Personal consumption expenditures: Services: Net motor vehicle and other transportation insurance
    'DNEHRC1A027NBEA', # Personal consumption expenditures: Services: Nursery, elementary, and secondary schools
    'DNRSRC1A027NBEA', # Personal consumption expenditures: Services: Nursing homes
    'DPUBRC1A027NBEA', # Personal consumption expenditures: Services: Public transportation
    'DGRDRC1A027NBEA', # Personal consumption expenditures: Services: Public transportation: Ground transportation
    'DWATRC1A027NBEA', # Personal consumption expenditures: Services: Public transportation: Water transportation
    'DPMBRC1A027NBEA', # Personal consumption expenditures: Services: Purchased meals and beverages
    'DNPSRC1A027NBEA', # Personal consumption expenditures: Services: Receipts from sales of goods and services by nonprofit institutions
    'DSOCRC1A027NBEA', # Personal consumption expenditures: Social services and religious activities
    'DODRRC1A027NBEA', # Personal consumption expenditures: Sports and recreational goods and related services
    'DORIRC1A027NBEA', # Personal consumption expenditures: Sports and recreational goods and related services: Other sporting and recreational goods
    'DTCSRC1A027NBEA', # Personal consumption expenditures: Telecommunication services
    'DTRNRC1A027NBEA', # Personal consumption expenditures: Transportation
    'DTRSRC1A027NBEA', # Personal consumption expenditures: Transportation services
    'DMTRRC1A027NBEA', # Personal consumption expenditures: Transportation: Motor vehicles
    'DVAARC1A027NBEA', # Personal consumption expenditures: Video and audio equipment
    'DVPIRC1A027NBEA', # Personal consumption expenditures: Video and audio equipment, computers, and related services
    'DIPERC1A027NBEA', # Personal consumption expenditures: Video and audio equipment, computers, and related services: Information processing equipment
    ## Bil. of Chn. 2009 $ (NSA)
    'DPCERX1A020NBEA', # Real Personal Consumption Expenditures (DISCONTINUED)
    ## Bil. of Chn. 2017 $ (NSA)
    'DIPERX1A020NBEA', # Real Personal Consumption Expenditures: Household consumption expenditures: Recreation: Video and audio equipment, computers, and related services: Information processing equipment
    'AB61RX1A020NBEA', # Real motor vehicle output: Personal consumption expenditures
    'DPCCRX1A020NBEA', # Real personal consumption expenditures excluding food and energy
    'DEXFRX1A020NBEA', # Real personal consumption expenditures in the United States by nonresidents
    'DPRORX1A020NBEA', # Real personal consumption expenditures: Accounting and other business services
    'DADMRX1A020NBEA', # Real personal consumption expenditures: Admissions to specified spectator amusements
    'DLIGRX1A020NBEA', # Real personal consumption expenditures: Admissions to specified spectator amusements: Live entertainment, excluding sports
    'DMOVRX1A020NBEA', # Real personal consumption expenditures: Admissions to specified spectator amusements: Motion picture theaters
    'DSPERX1A020NBEA', # Real personal consumption expenditures: Admissions to specified spectator amusements: Spectator sports
    'DORSRX1A020NBEA', # Real personal consumption expenditures: Amusements parks, campgrounds, and related recreational services
    'DCRCRX1A020NBEA', # Real personal consumption expenditures: Cleaning, repair, and rental of clothing
    'DCLTRX1A020NBEA', # Real personal consumption expenditures: Clothing
    'DLGRRX1A020NBEA', # Real personal consumption expenditures: Clothing repair, rental, and alterations
    'DCAFRX1A020NBEA', # Real personal consumption expenditures: Clothing, footwear, and related services
    'DOCMRX1A020NBEA', # Real personal consumption expenditures: Clothing: Other clothing materials
    'DCMCRX1A020NBEA', # Real personal consumption expenditures: Communication
    'DPSTRX1A020NBEA', # Real personal consumption expenditures: Communication: First-class postal service by U.S. Postal Service (USPS)
    'DEBKRX1A020NBEA', # Real personal consumption expenditures: Durable goods: Educational books
    'DFDHRX1A020NBEA', # Real personal consumption expenditures: Durable goods: Furnishings and durable household equipment
    'DFFFRX1A020NBEA', # Real personal consumption expenditures: Durable goods: Furniture and furnishings
    'DUTERX1A020NBEA', # Real personal consumption expenditures: Durable goods: Glassware, tableware, and household utensils
    'DAPPRX1A020NBEA', # Real personal consumption expenditures: Durable goods: Household appliances
    'DJRYRX1A020NBEA', # Real personal consumption expenditures: Durable goods: Jewelry and watches
    'DLUGRX1A020NBEA', # Real personal consumption expenditures: Durable goods: Luggage and similar personal items
    'DMVPRX1A020NBEA', # Real personal consumption expenditures: Durable goods: Motor vehicle parts and accessories
    'DMOTRX1A020NBEA', # Real personal consumption expenditures: Durable goods: Motor vehicles and parts
    'DMSCRX1A020NBEA', # Real personal consumption expenditures: Durable goods: Musical instruments
    'DNPVRX1A020NBEA', # Real personal consumption expenditures: Durable goods: Net purchases of used motor vehicles
    'DNMVRX1A020NBEA', # Real personal consumption expenditures: Durable goods: New motor vehicles
    'DODGRX1A020NBEA', # Real personal consumption expenditures: Durable goods: Other durable goods
    'DRBKRX1A020NBEA', # Real personal consumption expenditures: Durable goods: Recreational books
    'DREQRX1A020NBEA', # Real personal consumption expenditures: Durable goods: Recreational goods and vehicles
    'DSPGRX1A020NBEA', # Real personal consumption expenditures: Durable goods: Sporting equipment, supplies, guns, and ammunition
    'DWHLRX1A020NBEA', # Real personal consumption expenditures: Durable goods: Sports and recreational vehicles
    'DTCERX1A020NBEA', # Real personal consumption expenditures: Durable goods: Telephone and related communication equipment
    'DTAERX1A020NBEA', # Real personal consumption expenditures: Durable goods: Therapeutic appliances and equipment
    'DTOORX1A020NBEA', # Real personal consumption expenditures: Durable goods: Tools and equipment for house and garden
    'DVAPRX1A020NBEA', # Real personal consumption expenditures: Durable goods: Video, audio, photographic, and information processing equipment and media
    'DEDURX1A020NBEA', # Real personal consumption expenditures: Education
    'DTEDRX1A020NBEA', # Real personal consumption expenditures: Education services
    'DNRGRX1A020NBEA', # Real personal consumption expenditures: Energy goods and services
    'DFNLRX1A020NBEA', # Real personal consumption expenditures: Financial services
    'DIFSRX1A020NBEA', # Real personal consumption expenditures: Financial services and insurance
    'DIMPRX1A020NBEA', # Real personal consumption expenditures: Financial services furnished without payment
    'DFSERX1A020NBEA', # Real personal consumption expenditures: Food services
    'DFTWRX1A020NBEA', # Real personal consumption expenditures: Footwear
    'DFTRRX1A020NBEA', # Real personal consumption expenditures: Foreign travel by U.S. residents
    'DFUNRX1A020NBEA', # Real personal consumption expenditures: Funeral and burial services
    'DFHHRX1A020NBEA', # Real personal consumption expenditures: Furnishings, household equipment, and routine household maintenance
    'DGDSRX1A020NBEA', # Real personal consumption expenditures: Goods
    'DHLTRX1A020NBEA', # Real personal consumption expenditures: Health
    'DOUTRX1A020NBEA', # Real personal consumption expenditures: Health care: Outpatient services
    'DDENRX1A020NBEA', # Real personal consumption expenditures: Health care: Outpatient services: Dental services
    'DPMSRX1A020NBEA', # Real personal consumption expenditures: Health care: Outpatient services: Paramedical services
    'DPHYRX1A020NBEA', # Real personal consumption expenditures: Health care: Outpatient services: Physician services
    'DHHCRX1A020NBEA', # Real personal consumption expenditures: Home health care
    'DHPNRX1A020NBEA', # Real personal consumption expenditures: Hospital and nursing home services
    'DHAPRX1A020NBEA', # Real personal consumption expenditures: Household appliances
    'DPHCRX1A020NBEA', # Real personal consumption expenditures: Household consumption expenditures
    'DFURRX1A020NBEA', # Real personal consumption expenditures: Household consumption expenditures: Furniture, furnishings, and floor coverings
    'DOGSRX1A020NBEA', # Real personal consumption expenditures: Household consumption expenditures: Other household goods and services
    'DTEXRX1A020NBEA', # Real personal consumption expenditures: Household textiles
    'DUTFRX1A020NBEA', # Real personal consumption expenditures: Household utilities and fuels
    'DEGFRX1A020NBEA', # Real personal consumption expenditures: Household utilities and fuels: Electricity, gas, and other fuels
    'DHUFRX1A020NBEA', # Real personal consumption expenditures: Housing, utilities, and fuels
    'DUNSRX1A020NBEA', # Real personal consumption expenditures: Labor organization dues
    'DDRYRX1A020NBEA', # Real personal consumption expenditures: Laundry and dry cleaning services
    'DGALRX1A020NBEA', # Real personal consumption expenditures: Legal services
    'DNBSRX1A020NBEA', # Real personal consumption expenditures: Magazines, newspapers, books, and stationery
    'DRRERX1A020NBEA', # Real personal consumption expenditures: Maintenance and repair of recreational vehicles and sports equipment
    'DPCMRX1A020NBEA', # Real personal consumption expenditures: Market-based
    'DPCXRX1A020NBEA', # Real personal consumption expenditures: Market-based, excluding food and energy
    'DMPARX1A020NBEA', # Real personal consumption expenditures: Medical products, appliances, and equipment
    'DMDFRX1A020NBEA', # Real personal consumption expenditures: Membership clubs and participant sports centers
    'DMVORX1A020NBEA', # Real personal consumption expenditures: Motor vehicle operation
    'DMVSRX1A020NBEA', # Real personal consumption expenditures: Motor vehicle services
    'DMUSRX1A020NBEA', # Real personal consumption expenditures: Museums and libraries
    'DNFTRX1A020NBEA', # Real personal consumption expenditures: Net foreign travel and expenditures abroad by U.S. residents
    'DIINRX1A020NBEA', # Real personal consumption expenditures: Net health insurance: Income loss
    'DMINRX1A020NBEA', # Real personal consumption expenditures: Net health insurance: Medical care and hospitalization
    'DPWCRX1A020NBEA', # Real personal consumption expenditures: Net health insurance: Workers' compensation
    'A137RX1A020NBEA', # Real personal consumption expenditures: Net purchases of used autos
    'W240RX1A020NBEA', # Real personal consumption expenditures: Net purchases of used autos and used light trucks
    'W241RX1A020NBEA', # Real personal consumption expenditures: Net purchases of used light trucks (including utility vehicles)
    'AB67RX1A020NBEA', # Real personal consumption expenditures: New motor vehicles
    'A136RX1A020NBEA', # Real personal consumption expenditures: New motor vehicles: Autos
    'B704RX1A020NBEA', # Real personal consumption expenditures: New motor vehicles: Light trucks (including utility vehicles)
    'DNFRRX1A020NBEA', # Real personal consumption expenditures: Nondurable Goods: Net expenditures abroad by U.S. residents
    'DAOPRX1A020NBEA', # Real personal consumption expenditures: Nondurable goods: Alcoholic beverages purchased for off-premises consumption
    'DCICRX1A020NBEA', # Real personal consumption expenditures: Nondurable goods: Children's and infants' clothing
    'DCLORX1A020NBEA', # Real personal consumption expenditures: Nondurable goods: Clothing and footwear
    'DFXARX1A020NBEA', # Real personal consumption expenditures: Nondurable goods: Food and beverages purchased for off-premises consumption
    'DTFDRX1A020NBEA', # Real personal consumption expenditures: Nondurable goods: Food and nonalcoholic beverages purchased for off-premises consumption
    'DFFDRX1A020NBEA', # Real personal consumption expenditures: Nondurable goods: Food produced and consumed on farms
    'DFULRX1A020NBEA', # Real personal consumption expenditures: Nondurable goods: Fuel oil and other fuels
    'DGARRX1A020NBEA', # Real personal consumption expenditures: Nondurable goods: Garments
    'DGOERX1A020NBEA', # Real personal consumption expenditures: Nondurable goods: Gasoline and other energy goods
    'DHOURX1A020NBEA', # Real personal consumption expenditures: Nondurable goods: Household supplies
    'DNEWRX1A020NBEA', # Real personal consumption expenditures: Nondurable goods: Magazines, newspapers, and stationery
    'DMBCRX1A020NBEA', # Real personal consumption expenditures: Nondurable goods: Men's and boys' clothing
    'DMFLRX1A020NBEA', # Real personal consumption expenditures: Nondurable goods: Motor vehicle fuels, lubricants, and fluids
    'DOCCRX1A020NBEA', # Real personal consumption expenditures: Nondurable goods: Other clothing materials and footwear
    'DONGRX1A020NBEA', # Real personal consumption expenditures: Nondurable goods: Other nondurable goods
    'DOPCRX1A020NBEA', # Real personal consumption expenditures: Nondurable goods: Personal care products
    'DPHMRX1A020NBEA', # Real personal consumption expenditures: Nondurable goods: Pharmaceutical and other medical products
    'DREIRX1A020NBEA', # Real personal consumption expenditures: Nondurable goods: Recreational items
    'DTOBRX1A020NBEA', # Real personal consumption expenditures: Nondurable goods: Tobacco
    'DWGCRX1A020NBEA', # Real personal consumption expenditures: Nondurable goods: Women's and girls' clothing
    'DOISRX1A020NBEA', # Real personal consumption expenditures: Other goods and services - personal care, social and religious, professional, funeral and burial, and tobacco
    'DOMPRX1A020NBEA', # Real personal consumption expenditures: Other medical products
    'DOVSRX1A020NBEA', # Real personal consumption expenditures: Other motor vehicle services
    'DOTRRX1A020NBEA', # Real personal consumption expenditures: Other recreational services - food, transportation insurance, and household insurance
    'DOTSRX1A020NBEA', # Real personal consumption expenditures: Other services
    'DMLBRX1A020NBEA', # Real personal consumption expenditures: Outpatient services: Paramedical services: Medical laboratories
    'DOMDRX1A020NBEA', # Real personal consumption expenditures: Outpatient services: Paramedical services: Other professional medical services
    'DXHLRX1A020NBEA', # Real personal consumption expenditures: Package tours
    'DPCRRX1A020NBEA', # Real personal consumption expenditures: Personal care
    'DPERRX1A020NBEA', # Real personal consumption expenditures: Personal care and clothing services
    'DPEORX1A020NBEA', # Real personal consumption expenditures: Personal items
    'DPETRX1A020NBEA', # Real personal consumption expenditures: Pets, pet products, and related services
    'DPNPRX1A020NBEA', # Real personal consumption expenditures: Pharmaceutical products
    'DPHORX1A020NBEA', # Real personal consumption expenditures: Photographic goods and services
    'DPSSRX1A020NBEA', # Real personal consumption expenditures: Postal and delivery services
    'DODSRX1A020NBEA', # Real personal consumption expenditures: Postal and delivery services: Other delivery services (by non-USPS facilities)
    'DPRSRX1A020NBEA', # Real personal consumption expenditures: Professional and other services
    'DAXSRX1A020NBEA', # Real personal consumption expenditures: Professional association dues
    'DRRLRX1A020NBEA', # Real personal consumption expenditures: Recreation
    'DRCARX1A020NBEA', # Real personal consumption expenditures: Recreation services
    'DAVPRX1A020NBEA', # Real personal consumption expenditures: Recreation services: Audio-video, photographic, and information processing equipment services
    'A964RX1A020NBEA', # Real personal consumption expenditures: Residual
    'A965RX1A020NBEA', # Real personal consumption expenditures: Residual
    'D236RX1A020NBEA', # Real personal consumption expenditures: Residual
    'DSVCRX1A020NBEA', # Real personal consumption expenditures: Services related to video and audio goods and computers
    'DACCRX1A020NBEA', # Real personal consumption expenditures: Services: Accommodations
    'DVEDRX1A020NBEA', # Real personal consumption expenditures: Services: Commercial and vocational schools
    'DCOMRX1A020NBEA', # Real personal consumption expenditures: Services: Communication
    'DNPIRX1A020NBEA', # Real personal consumption expenditures: Services: Final consumption expenditures of nonprofit institutions serving households (NPISHs)
    'DOFIRX1A020NBEA', # Real personal consumption expenditures: Services: Financial service charges, fees, and commissions
    'DFOORX1A020NBEA', # Real personal consumption expenditures: Services: Food furnished to employees (including military)
    'DFSARX1A020NBEA', # Real personal consumption expenditures: Services: Food services and accommodations
    'DGAMRX1A020NBEA', # Real personal consumption expenditures: Services: Gambling
    'DNPERX1A020NBEA', # Real personal consumption expenditures: Services: Gross output of nonprofit institutions
    'DHLCRX1A020NBEA', # Real personal consumption expenditures: Services: Health care
    'DHEDRX1A020NBEA', # Real personal consumption expenditures: Services: Higher education
    'DHSPRX1A020NBEA', # Real personal consumption expenditures: Services: Hospitals
    'DHCERX1A020NBEA', # Real personal consumption expenditures: Services: Household consumption expenditures
    'DAITRX1A020NBEA', # Real personal consumption expenditures: Services: Household consumption expenditures: Transportation services: Public transportation: Air transportation
    'DHHMRX1A020NBEA', # Real personal consumption expenditures: Services: Household maintenance
    'DUTLRX1A020NBEA', # Real personal consumption expenditures: Services: Household utilities
    'DELCRX1A020NBEA', # Real personal consumption expenditures: Services: Household utilities: Electricity
    'DELGRX1A020NBEA', # Real personal consumption expenditures: Services: Household utilities: Electricity and gas
    'DGHERX1A020NBEA', # Real personal consumption expenditures: Services: Household utilities: Natural gas
    'DWRSRX1A020NBEA', # Real personal consumption expenditures: Services: Household utilities: Water supply and sanitation
    'DHUTRX1A020NBEA', # Real personal consumption expenditures: Services: Housing and utilities
    'DHSGRX1A020NBEA', # Real personal consumption expenditures: Services: Housing and utilities: Housing
    'DGRHRX1A020NBEA', # Real personal consumption expenditures: Services: Housing: Group housing
    'DOWNRX1A020NBEA', # Real personal consumption expenditures: Services: Housing: Imputed rental of owner-occupied nonfarm housing
    'DTENRX1A020NBEA', # Real personal consumption expenditures: Services: Housing: Rental of tenant-occupied nonfarm housing
    'DFARRX1A020NBEA', # Real personal consumption expenditures: Services: Housing: Rental value of farm dwellings
    'DINSRX1A020NBEA', # Real personal consumption expenditures: Services: Insurance
    'DINTRX1A020NBEA', # Real personal consumption expenditures: Services: Internet access
    'DLIFRX1A020NBEA', # Real personal consumption expenditures: Services: Life insurance
    'DRLSRX1A020NBEA', # Real personal consumption expenditures: Services: Membership clubs, sports centers, parks, theaters, and museums
    'DVMRRX1A020NBEA', # Real personal consumption expenditures: Services: Motor vehicle maintenance and repair
    'DFORRX1A020NBEA', # Real personal consumption expenditures: Services: Net foreign travel
    'DHINRX1A020NBEA', # Real personal consumption expenditures: Services: Net health insurance
    'DFINRX1A020NBEA', # Real personal consumption expenditures: Services: Net household insurance
    'DTINRX1A020NBEA', # Real personal consumption expenditures: Services: Net motor vehicle and other transportation insurance
    'DNEHRX1A020NBEA', # Real personal consumption expenditures: Services: Nursery, elementary, and secondary schools
    'DNRSRX1A020NBEA', # Real personal consumption expenditures: Services: Nursing homes
    'DPUBRX1A020NBEA', # Real personal consumption expenditures: Services: Public transportation
    'DGRDRX1A020NBEA', # Real personal consumption expenditures: Services: Public transportation: Ground transportation
    'DWATRX1A020NBEA', # Real personal consumption expenditures: Services: Public transportation: Water transportation
    'DPMBRX1A020NBEA', # Real personal consumption expenditures: Services: Purchased meals and beverages
    'DNPSRX1A020NBEA', # Real personal consumption expenditures: Services: Receipts from sales of goods and services by nonprofit institutions
    'DSOCRX1A020NBEA', # Real personal consumption expenditures: Social services and religious activities
    'DODRRX1A020NBEA', # Real personal consumption expenditures: Sports and recreational goods and related services
    'DORIRX1A020NBEA', # Real personal consumption expenditures: Sports and recreational goods and related services: Other sporting and recreational goods
    'DTCSRX1A020NBEA', # Real personal consumption expenditures: Telecommunication services
    'DTRNRX1A020NBEA', # Real personal consumption expenditures: Transportation
    'DTRSRX1A020NBEA', # Real personal consumption expenditures: Transportation services
    'DMTRRX1A020NBEA', # Real personal consumption expenditures: Transportation: Motor vehicles
    'DVAARX1A020NBEA', # Real personal consumption expenditures: Video and audio equipment
    'DVPIRX1A020NBEA', # Real personal consumption expenditures: Video and audio equipment, computers, and related services
    ## Mil. of $ (NSA)
    'LA001176A', # Personal Consumption Expenditures Excluding Food, Energy, and Housing
    'USPCEG', # Personal Consumption Expenditures: Goods for United States
    'USPCEDURG', # Personal Consumption Expenditures: Goods: Durable Goods for United States
    'USPCEFUR', # Personal Consumption Expenditures: Goods: Durable Goods: Furnishings and Durable Household Equipment for United States
    'USPCEVEH', # Personal Consumption Expenditures: Goods: Durable Goods: Motor Vehicles and Parts for United States
    'USPCEODURG', # Personal Consumption Expenditures: Goods: Durable Goods: Other Durable Goods for United States
    'USPCERECGD', # Personal Consumption Expenditures: Goods: Durable Goods: Recreational Goods and Vehicles for United States
    'USPCENDURG', # Personal Consumption Expenditures: Nondurable Goods for United States
    'USPCECLTH', # Personal Consumption Expenditures: Nondurable Goods: Clothing and Footwear for United States
    'USPCEFOOD', # Personal Consumption Expenditures: Nondurable Goods: Food and Beverages Purchased for Off-Premises Consumption for United States
    'USPCEGAS', # Personal Consumption Expenditures: Nondurable Goods: Gasoline and Other Energy Goods for United States
    'USPCEONDURG', # Personal Consumption Expenditures: Nondurable Goods: Other Nondurable Goods for United States
    'LA001260A', # Personal Consumption Expenditures: Services Excluding Energy and Housing
    'USPCESRV', # Personal Consumption Expenditures: Services for United States
    'USPCEFCENPISH', # Personal Consumption Expenditures: Services: Final Consumption Expenditures of Nonprofit Institutions Serving Households for United States
    'USPCEGONPI', # Personal Consumption Expenditures: Services: Final Consumption Expenditures of Nonprofit Institutions Serving Households: Gross Output of Nonprofit Institutions for United States
    'USPCELRPTSLSGSNPIS', # Personal Consumption Expenditures: Services: Final Consumption Expenditures of Nonprofit Institutions Serving Households: Less: Receipts from Sales of Goods and Services by Nonprofit Institutions for United States
    'USPCEFININS', # Personal Consumption Expenditures: Services: Financial Services and Insurance for United States
    'USPCEFDSRVACCMD', # Personal Consumption Expenditures: Services: Food Services and Accommodations for United States
    'USPCEHLTHCARE', # Personal Consumption Expenditures: Services: Health Care for United States
    'USPCEHCE', # Personal Consumption Expenditures: Services: Household Consumption Expenditures for Services for United States
    'USPCEHOUSUTL', # Personal Consumption Expenditures: Services: Housing and Utilities for United States
    'USPCEOSRV', # Personal Consumption Expenditures: Services: Other Services for United States
    'USPCESRECSRV', # Personal Consumption Expenditures: Services: Recreation Services for United States
    'USPCETRANS', # Personal Consumption Expenditures: Services: Transportation Services for United States
    'USPCE', # Personal Consumption Expenditures: Total for United States
    ## Mil. of Chn. 2017 $ (NSA)
    'LB001176A', # Real Personal Consumption Expenditures Excluding Food, Energy, and Housing
    'LB001260A', # Real Personal Consumption Expenditures: Services Excluding Energy and Housing
    ## Percentage Points at Annual Rate (NSA)
    'CB001176A', # Contributions to Percent Change In Real Personal Consumption Expenditures: Real Personal Consumption Expenditures Excluding Food, Energy, and Housing
    'CB001260A', # Contributions to Percent Change in Real Personal Consumption Expenditures: Real Personal Consumption Expenditures: Services Excluding Energy and Housing
    'DPCERS2A224NBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures
    'DDURRS2A224NBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Durable goods
    'DFDHRS2A224NBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Durable goods: Furnishings and durable household equipment
    'DMOTRS2A224NBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Durable goods: Motor vehicles and parts
    'DREQRS2A224NBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Durable goods: Recreational goods and vehicles
    'DNPIRS2A224NBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Final consumption expenditures of nonprofit institutions serving households (NPISHs)
    'DGDSRS2A224NBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Goods
    'DIFSRS2A224NBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Household consumption expenditures: Financial services and insurance
    'DOTSRS2A224NBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Household consumption expenditures: Other services
    'DRCARS2A224NBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Household consumption expenditures: Recreation services
    'DTRSRS2A224NBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Household consumption expenditures: Transportation services
    'DNDGRS2A224NBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Nondurable goods
    'DCLORS2A224NBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Nondurable goods: Clothing and footwear
    'DFXARS2A224NBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Nondurable goods: Food and beverages purchased for off-premises consumption
    'DGOERS2A224NBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Nondurable goods: Gasoline and other energy goods
    'DODGRS2A224NBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Other durable goods
    'DONGRS2A224NBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Other nondurable goods
    'DSERRS2A224NBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Services
    'DHCERS2A224NBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Services: Household consumption expenditures
    'DFSARS2A224NBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Services: Household consumption expenditures: Food services and accommodations
    'DHLCRS2A224NBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Services: Household consumption expenditures: Health care
    'DHUTRS2A224NBEA', # Contributions to percent change in gross domestic purchases: Personal consumption expenditures: Services: Household consumption expenditures: Housing and utilities
    'DNPSRY2A224NBEA', # Contributions to percent change in real GDP: PCE: Final consumption expenditures of nonprofit institutions serving households (NPISHs): Less: Receipts from sales of goods and services by nonprofit institutions
    'DPCERY2A224NBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures
    'DDURRY2A224NBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Durable goods
    'DFDHRY2A224NBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Durable goods: Furnishings and durable household equipment
    'DMOTRY2A224NBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Durable goods: Motor vehicles and parts
    'DREQRY2A224NBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Durable goods: Recreational goods and vehicles
    'DNPIRY2A224NBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Final consumption expenditures of nonprofit institutions serving households (NPISHs)
    'DGDSRY2A224NBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Goods
    'DNDGRY2A224NBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Nondurable goods
    'DCLORY2A224NBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Nondurable goods: Clothing and footwear
    'DFXARY2A224NBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Nondurable goods: Food and beverages purchased for off-premises consumption
    'DGOERY2A224NBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Nondurable goods: Gasoline and other energy goods
    'DODGRY2A224NBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Other durable goods
    'DONGRY2A224NBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Other nondurable goods
    'DOTSRY2A224NBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Other services
    'DRCARY2A224NBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Recreation services
    'DSERRY2A224NBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Services
    'DNPERY2A224NBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Services: Final consumption expenditures of nonprofit institutions serving households (NPISHs): Gross output of nonprofit institutions
    'DIFSRY2A224NBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Services: Financial services and insurance
    'DFSARY2A224NBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Services: Food services and accommodations
    'DHLCRY2A224NBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Services: Health care
    'DHCERY2A224NBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Services: Household consumption expenditures (for services)
    'DHUTRY2A224NBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Services: Housing and utilities
    'DTRSRY2A224NBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Transportation services
    'DDURRZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Durable goods
    'DFDHRZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Durable goods: Furnishings and durable household equipment
    'DMOTRZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Durable goods: Motor vehicles and parts
    'DODGRZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Durable goods: Other durable goods
    'DREQRZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Durable goods: Recreational goods and vehicles
    'DNRGRZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Energy goods and services
    'DIFSRZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Financial services and insurance
    'DGDSRZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Goods
    'DPCMRZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Market-based
    'DPCXRZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Market-based, excluding food and energy
    'DNDGRZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Nondurable goods
    'DCLORZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Nondurable goods: Clothing and footwear
    'DFXARZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Nondurable goods: Food and beverages purchased for off-premises consumption
    'DGOERZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Nondurable goods: Gasoline and other energy goods
    'DONGRZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Nondurable goods: Other nondurable goods
    'DOTSRZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Other services
    'DPCCRZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Real personal consumption expenditures excluding food and energy
    'DRCARZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Recreation services
    'DSERRZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Services
    'DNPIRZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Services: Final consumption expenditures of nonprofit institutions serving households (NPISHs)
    'DFSARZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Services: Food services and accommodations
    'DNPERZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Services: Gross output of nonprofit institutions
    'DHLCRZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Services: Health care
    'DHCERZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Services: Household consumption expenditures
    'DHUTRZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Services: Housing and utilities
    'DNPSRZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Services: Receipts from sales of goods and services by nonprofit institutions
    'DTRSRZ2A224NBEA', # Contributions to percent change in real personal consumption expenditures: Transportation services

    # Personal Income & Outlays > Personal Current Taxes (18)
    ## Bil. of $ (NSA)
    'A074RC1A027NBEA', # Federal government current tax receipts: Personal current taxes
    'W832RC1A027NBEA', # Local government current tax receipts: Personal current taxes
    'W833RC1A027NBEA', # Local government current tax receipts: Personal current taxes: Income taxes
    'W834RC1A027NBEA', # Local government current tax receipts: Personal current taxes: Other
    'W055RC1A027NBEA', # Personal current taxes
    'B231RC1A027NBEA', # Personal current taxes: Federal: Income taxes
    'PTN1001A027NBEA', # Personal current taxes: Federal: Income taxes: Declarations and settlements
    'PTN2001A027NBEA', # Personal current taxes: Federal: Income taxes: Refunds
    'PTN0181A027NBEA', # Personal current taxes: Federal: Income taxes: Withheld
    'B035RC1A027NBEA', # Personal current taxes: Federal: Other taxes
    'S210301A027NBEA', # Personal current taxes: State and local: Motor vehicle licenses
    'S210501A027NBEA', # Personal current taxes: State and local: Other taxes
    'S210401A027NBEA', # Personal current taxes: State and local: Property taxes
    'W071RC1A027NBEA', # State and local government current tax receipts: Personal current taxes
    'B247RC1A027NBEA', # State and local government current tax receipts: Personal current taxes: Other
    'W732RC1A027NBEA', # State government current tax receipts: Personal current taxes
    'W733RC1A027NBEA', # State government current tax receipts: Personal current taxes: Income taxes
    'W734RC1A027NBEA', # State government current tax receipts: Personal current taxes: Other

    # Personal Income & Outlays > Wage and Salary Accruals (559)
    ## $ (NSA)
    'A4401C0A052NBEA', # Wage and salary accruals per full-time equivalent employee
    'A4402C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic industries
    'B4496C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic industries: Federal general government: Work relief
    'B4497C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic industries: State and local general government: Work relief
    'A4403C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries
    'N4497C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Accommodation
    'N4496C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Accommodation and food services
    'N4471C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Administrative and support services
    'N4470C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Administrative and waste management services
    'H4406C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Agricultural services, forestry, and fisheries
    'B4406C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Agricultural services, forestry, and fishing
    'J4406C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Agricultural services, forestry, and fishing
    'H4404C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Agriculture, forestry, and fisheries
    'A4404C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Agriculture, forestry, and fishing
    'J4404C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Agriculture, forestry, and fishing
    'N4404C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Agriculture, forestry, fishing, and hunting
    'N4444C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Air transportation
    'N4475C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Ambulatory health care services
    'B4467C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Amusement and recreation services
    'J4467C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Amusement and recreation services
    'N4495C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Amusements, gambling, and recreation industries
    'B4492C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Anthracite mining
    'N4493C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Arts, entertainment, and recreation
    'B4464C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Auto repair, services, and parking
    'J4453C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Banking
    'H4409C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Bituminous and other soft coal mining
    'B4463C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Business services
    'H4463C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Business services
    'J4463C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Business services
    'B4409C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Coal mining
    'J4409C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Coal mining
    'A4446C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Communication
    'J4448C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Communication: Radio and television
    'J4447C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Communication: Telephone and telegraph
    'B4448C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Communications: Radio and television
    'B4447C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Communications: Telephone and telegraph
    'N4467C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Computer systems design and related services
    'B4412C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Construction
    'J4412C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Construction
    'N4412C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Construction
    'H4412C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Contract construction
    'H4454C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Credit agencies (other than banks) and holding and other investment companies
    'J4454C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Credit agencies other than banks
    'B4453C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Depository institutions
    'B4470C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Educational services
    'J4470C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Educational services
    'N4473C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Educational services
    'H4470C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Educational services, n.e.c.
    'B4405C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Farms
    'N4405C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Farms
    'N4458C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Federal Reserve banks, credit intermediation, and related activities
    'N4457C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Finance and insurance
    'A4452C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Finance, insurance, and real estate
    'J4452C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Finance, insurance, and real estate
    'N4498C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Food services and drinking places
    'N4406C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Forestry, fishing, and related activities
    'N4461C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Funds, trusts, and other financial vehicles
    'N4474C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Health care and social assistance
    'N4490C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Health care and social assistance: Hospitals
    'N4491C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Health care and social assistance: Nursing and residential care facilities
    'B4468C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Health services
    'H4468C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Health services
    'J4468C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Health services
    'B4459C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Holding and other investment offices
    'N4452C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Information
    'N4455C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Information: Broadcasting and telecommunications
    'N4456C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Information: Information and data processing services
    'N4454C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Information: Motion picture and sound recording industries
    'N4453C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Information: Publishing industries (includes software)
    'B4457C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Insurance agents, brokers, and service
    'H4457C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Insurance agents, brokers, and service
    'J4457C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Insurance agents, brokers, and service
    'B4456C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Insurance carriers
    'N4460C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Insurance carriers and related activities
    'B4469C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Legal services
    'J4469C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Legal services
    'N4466C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Legal services
    'N4469C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Management of companies and enterprises
    'A4413C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing
    'H4413C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing
    'J4413C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing
    'N4413C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing
    'A4414C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods
    'H4414C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods
    'J4414C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods
    'N4414C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods
    'N4420C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Computer and electronic products
    'H4421C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Electric and electronic equipment
    'J4421C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Electric and electronic equipment
    'N4421C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Electrical equipment, appliances, and components
    'B4421C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Electronic and other electric equipment
    'B4419C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Fabricated metal products
    'J4419C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Fabricated metal products
    'N4418C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Fabricated metal products
    'H4416C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Furniture and finished lumber products
    'B4416C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Furniture and fixtures
    'J4416C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Furniture and fixtures
    'N4424C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Furniture and related products
    'B4420C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Industrial machinery and equipment
    'B4424C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Instruments and related products
    'J4424C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Instruments and related products
    'H4418C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Iron and steel and their products, including ordnance
    'H4415C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Lumber and basic timber products
    'B4415C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Lumber and wood products
    'J4415C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Lumber and wood products
    'N4419C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Machinery
    'H4420C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Machinery, except electrical
    'J4420C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Machinery, except electrical
    'N4425C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Miscellaneous manufacturing
    'B4425C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Miscellaneous manufacturing industries
    'J4425C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Miscellaneous manufacturing industries
    'H4425C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Miscellaneous manufacturing, including instruments and miscellaneous plastic products
    'B4422C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Motor vehicles and equipment
    'H4422C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Motor vehicles and equipment
    'J4422C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Motor vehicles and equipment
    'N4422C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Motor vehicles, bodies and trailers, and parts
    'H4419C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Nonferrous metals and their products
    'N4416C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Nonmetallic mineral products
    'B4423C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Other transportation equipment
    'H4423C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Other transportation equipment
    'J4423C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Other transportation equipment
    'N4423C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Other transportation equipment
    'B4418C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Primary metal industries
    'J4418C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Primary metal industries
    'N4417C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Primary metals
    'B4417C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Stone, clay, and glass products
    'H4417C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Stone, clay, and glass products
    'J4417C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Stone, clay, and glass products
    'N4415C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Durable goods: Wood products
    'A4426C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods
    'H4426C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods
    'J4426C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods
    'N4426C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods
    'N4429C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Apparel and leather and allied products
    'B4430C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Apparel and other textile products
    'H4430C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Apparel and other textile products
    'J4430C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Apparel and other textile products
    'N4433C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Chemical products
    'B4433C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Chemicals and allied products
    'H4433C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Chemicals and allied products
    'J4433C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Chemicals and allied products
    'N4427C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Food and beverage and tobacco products
    'B4427C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Food and kindred products
    'H4427C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Food and kindred products
    'J4427C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Food and kindred products
    'B4436C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Leather and leather products
    'H4436C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Leather and leather products
    'J4436C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Leather and leather products
    'B4431C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Paper and allied products
    'J4431C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Paper and allied products
    'N4430C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Paper products
    'B4434C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Petroleum and coal products
    'H4434C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Petroleum and coal products
    'J4434C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Petroleum and coal products
    'N4432C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Petroleum and coal products
    'N4434C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Plastics and rubber products
    'B4432C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Printing and publishing
    'N4431C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Printing and related support activities
    'B4435C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Rubber and miscellaneous plastics products
    'J4435C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Rubber and miscellaneous plastics products
    'H4435C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Rubber products
    'B4429C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Textile mill products
    'H4429C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Textile mill products
    'J4429C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Textile mill products
    'N4428C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Textile mills and textile product mills
    'B4428C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Manufacturing: Nondurable goods: Tobacco manufactures
    'B4408C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Metal mining
    'A4407C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Mining
    'H4407C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Mining
    'J4407C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Mining
    'N4407C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Mining
    'N4409C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Mining, except oil and gas
    'H4410C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Mining: Crude petroleum and natural gas
    'B4411C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Mining: Nonmetallic minerals, except fuels
    'B4410C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Mining: Oil and gas extraction
    'J4410C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Mining: Oil and gas extraction
    'N4408C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Mining: Oil and gas extraction
    'H4474C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Miscellaneous professional services
    'N4468C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Miscellaneous professional, scientific, and technical services
    'B4465C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Miscellaneous repair services
    'B4454C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Nondepository institutions
    'N4499C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Other services, except government
    'N4450C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Other transportation and support activities
    'N4494C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Performing arts, spectator sports, museums, and related activities
    'B4462C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Personal services
    'H4462C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Personal services
    'J4462C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Personal services
    'N4449C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Pipeline transportation
    'N4465C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Professional, scientific, and technical services
    'N4445C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Rail transportation
    'B4439C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Railroad transportation
    'B4458C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Real estate
    'H4458C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Real estate
    'J4458C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Real estate
    'N4463C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Real estate
    'N4462C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Real estate and rental and leasing
    'N4464C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Rental and leasing services and lessors of intangible assets
    'B4451C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Retail trade
    'J4451C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Retail trade
    'N4438C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Retail trade
    'H4451C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Retail trade and automobile services
    'N4440C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Retail trade: Food and beverage stores
    'N4441C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Retail trade: General merchandise stores
    'N4439C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Retail trade: Motor vehicle and parts dealers
    'N4442C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Retail trade: Other retail
    'N4459C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Securities, commodity contracts, and investments
    'B4455C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Security and commodity brokers
    'J4455C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Security and commodity brokers
    'H4455C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Security and commodity brokers, and services
    'A4460C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Services
    'H4460C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Services
    'J4460C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Services
    'B4495C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Services: Commercial and trade schools and employment agencies
    'B4461C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Services: Hotels and other lodging places
    'H4461C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Services: Hotels and other lodging places
    'J4461C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Services: Hotels and other lodging places
    'B4473C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Services: Membership organizations
    'H4473C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Services: Membership organizations
    'J4473C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Services: Membership organizations
    'J4474C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Services: Miscellaneous professional services
    'B4466C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Services: Motion pictures
    'J4466C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Services: Motion pictures
    'B4474C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Services: Other services
    'B4475C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Services: Private households
    'N4492C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Social assistance
    'B4472C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Social services
    'A4471C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Social services and membership organizations
    'N4410C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Support activities for mining
    'N4448C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Transit and ground passenger transportation
    'A4438C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Transportation
    'J4438C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Transportation
    'A4437C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Transportation and public utilities
    'B4449C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Transportation and public utilities: Electric, gas, and sanitary services
    'J4449C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Transportation and public utilities: Electric, gas, and sanitary services
    'B4494C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Transportation and public utilities: Local utilities and public services, n.e.c.
    'B4493C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Transportation and public utilities: Utilities: electric and gas
    'N4443C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Transportation and warehousing
    'N4451C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Transportation and warehousing: Warehousing and storage
    'B4443C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Transportation by air
    'H4443C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Transportation by air
    'J4443C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Transportation by air
    'B4445C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Transportation services
    'H4445C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Transportation services
    'J4445C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Transportation services
    'B4440C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Transportation: Local and interurban passenger transit
    'H4440C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Transportation: Local and interurban passenger transit
    'J4440C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Transportation: Local and interurban passenger transit
    'B4444C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Transportation: Pipelines, except natural gas
    'B4441C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Transportation: Trucking and warehousing
    'N4447C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Truck transportation
    'N4411C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Utilities
    'N4472C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Waste management and remediation services
    'B4442C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Water transportation
    'H4442C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Water transportation
    'J4442C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Water transportation
    'N4446C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Water transportation
    'B4450C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Wholesale trade
    'H4450C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Wholesale trade
    'J4450C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Wholesale trade
    'N4435C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Wholesale trade
    'N4436C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Wholesale trade: Durable goods
    'N4437C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Domestic private industries: Wholesale trade: Nondurable goods
    'A4478C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Federal general government
    'B4479C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Federal general government: Civilian
    'B4480C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Federal general government: Military
    'A4477C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Federal government
    'B4481C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Federal government enterprises
    'A4476C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: Government
    'A4483C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: State and local general government
    'B4484C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: State and local general government: Education
    'B4485C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: State and local general government: Other
    'A4482C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: State and local government
    'B4486C0A052NBEA', # Wage and salary accruals per full-time equivalent employee: State and local government enterprises
    ## Bil. of $ (NSA)
    'W269RC1A027NBEA', # Gross domestic income: Compensation of employees, paid: Wage and salary accruals: Disbursements (DISCONTINUED)
    'A4102C1A027NBEA', # Gross domestic income: Compensation of employees, paid: Wages and salaries
    'W270RC1A027NBEA', # Gross domestic income: Compensation of employees, paid: Wages and salaries: to persons
    'A034RC1A027NBEA', # National income: Compensation of employees: Wages and salaries
    'A553RC1A027NBEA', # National income: Compensation of employees: Wages and salaries: Government (DISCONTINUED)
    'B203RC1A027NBEA', # National income: Compensation of employees: Wages and salaries: Other (DISCONTINUED)
    'A443RC1A027NBEA', # National income: Domestic business: Corporate business: Compensation of employees: Wages and salaries
    'W463RC1A027NBEA', # National income: Domestic business: Noncorporate business: Compensation of employees: Wage and salary accruals
    'B1659C1A027NBEA', # National income: Domestic business: Noncorporate business: Government enterprises: Compensation of employees: Wage and salary accruals
    'B1652C1A027NBEA', # National income: Domestic business: Noncorporate business: Other private business: Compensation of employees: Wage and salary accruals
    'B1643C1A027NBEA', # National income: Domestic business: Noncorporate business: Sole proprietorships and partnerships: Compensation of employees: Wage and salary accruals
    'B1663C1A027NBEA', # National income: General government: Compensation of employees: Wage and salary accruals
    'W481RC1A027NBEA', # National income: Households and institutions: Nonprofit institutions serving households: Compensation of employees: Wage and salary accruals
    'B1661C1A027NBEA', # National income: Households: Compensation of employees: Wage and salary accruals
    'Y663RC1A027NBEA', # Total wages and salaries, BLS: Timing adjustment for accrual basis
    ## Mil. of $ (NSA)
    'A4102C0A144NBEA', # Gross domestic income: Compensation of employees, paid: Wages and salaries (DISCONTINUED)
    'A034RC0A144NBEA', # National income: Compensation of employees: Wages and salaries (DISCONTINUED)
    'B4196C0A144NBEA', # Wage and salary accruals: Domestic industries: Federal general government: Work relief
    'B4197C0A144NBEA', # Wage and salary accruals: Domestic industries: State and local general government: Work relief
    'A4103C0A144NBEA', # Wage and salary accruals: Domestic private industries
    'N4185C0A144NBEA', # Wage and salary accruals: Domestic private industries: Accommodation
    'N4184C0A144NBEA', # Wage and salary accruals: Domestic private industries: Accommodation and food services
    'N4173C0A144NBEA', # Wage and salary accruals: Domestic private industries: Administrative and support services
    'N4172C0A144NBEA', # Wage and salary accruals: Domestic private industries: Administrative and waste management services
    'H4106C0A144NBEA', # Wage and salary accruals: Domestic private industries: Agricultural services, forestry, and fisheries
    'B4106C0A144NBEA', # Wage and salary accruals: Domestic private industries: Agricultural services, forestry, and fishing
    'J4106C0A144NBEA', # Wage and salary accruals: Domestic private industries: Agricultural services, forestry, and fishing
    'H4104C0A144NBEA', # Wage and salary accruals: Domestic private industries: Agriculture, forestry, and fisheries
    'A4104C0A144NBEA', # Wage and salary accruals: Domestic private industries: Agriculture, forestry, and fishing
    'J4104C0A144NBEA', # Wage and salary accruals: Domestic private industries: Agriculture, forestry, and fishing
    'N4104C0A144NBEA', # Wage and salary accruals: Domestic private industries: Agriculture, forestry, fishing, and hunting
    'N4146C0A144NBEA', # Wage and salary accruals: Domestic private industries: Air transportation
    'N4177C0A144NBEA', # Wage and salary accruals: Domestic private industries: Ambulatory health care services
    'B4167C0A144NBEA', # Wage and salary accruals: Domestic private industries: Amusement and recreation services
    'J4167C0A144NBEA', # Wage and salary accruals: Domestic private industries: Amusement and recreation services
    'N4183C0A144NBEA', # Wage and salary accruals: Domestic private industries: Amusements, gambling, and recreation industries
    'B4192C0A144NBEA', # Wage and salary accruals: Domestic private industries: Anthracite mining
    'N4181C0A144NBEA', # Wage and salary accruals: Domestic private industries: Arts, entertainment, and recreation
    'B4164C0A144NBEA', # Wage and salary accruals: Domestic private industries: Auto repair, services, and parking
    'J4153C0A144NBEA', # Wage and salary accruals: Domestic private industries: Banking
    'H4109C0A144NBEA', # Wage and salary accruals: Domestic private industries: Bituminous and other soft coal mining
    'B4163C0A144NBEA', # Wage and salary accruals: Domestic private industries: Business services
    'H4163C0A144NBEA', # Wage and salary accruals: Domestic private industries: Business services
    'J4163C0A144NBEA', # Wage and salary accruals: Domestic private industries: Business services
    'B4109C0A144NBEA', # Wage and salary accruals: Domestic private industries: Coal mining
    'J4109C0A144NBEA', # Wage and salary accruals: Domestic private industries: Coal mining
    'A4146C0A144NBEA', # Wage and salary accruals: Domestic private industries: Communication
    'B4148C0A144NBEA', # Wage and salary accruals: Domestic private industries: Communication: Radio and television
    'J4148C0A144NBEA', # Wage and salary accruals: Domestic private industries: Communication: Radio and television
    'B4147C0A144NBEA', # Wage and salary accruals: Domestic private industries: Communication: Telephone and telegraph
    'J4147C0A144NBEA', # Wage and salary accruals: Domestic private industries: Communication: Telephone and telegraph
    'N4169C0A144NBEA', # Wage and salary accruals: Domestic private industries: Computer systems design and related services
    'B4112C0A144NBEA', # Wage and salary accruals: Domestic private industries: Construction
    'J4112C0A144NBEA', # Wage and salary accruals: Domestic private industries: Construction
    'N4112C0A144NBEA', # Wage and salary accruals: Domestic private industries: Construction
    'H4112C0A144NBEA', # Wage and salary accruals: Domestic private industries: Contract construction
    'H4154C0A144NBEA', # Wage and salary accruals: Domestic private industries: Credit agencies (other than banks) and holding and other investment companies
    'J4154C0A144NBEA', # Wage and salary accruals: Domestic private industries: Credit agencies other than banks
    'B4153C0A144NBEA', # Wage and salary accruals: Domestic private industries: Depository institutions
    'B4170C0A144NBEA', # Wage and salary accruals: Domestic private industries: Educational services
    'J4170C0A144NBEA', # Wage and salary accruals: Domestic private industries: Educational services
    'N4175C0A144NBEA', # Wage and salary accruals: Domestic private industries: Educational services
    'H4170C0A144NBEA', # Wage and salary accruals: Domestic private industries: Educational services, n.e.c.
    'B4105C0A144NBEA', # Wage and salary accruals: Domestic private industries: Farms
    'N4105C0A144NBEA', # Wage and salary accruals: Domestic private industries: Farms
    'N4160C0A144NBEA', # Wage and salary accruals: Domestic private industries: Federal Reserve banks, credit intermediation, and related activities
    'N4159C0A144NBEA', # Wage and salary accruals: Domestic private industries: Finance and insurance
    'A4152C0A144NBEA', # Wage and salary accruals: Domestic private industries: Finance, insurance, and real estate
    'H4152C0A144NBEA', # Wage and salary accruals: Domestic private industries: Finance, insurance, and real estate
    'J4152C0A144NBEA', # Wage and salary accruals: Domestic private industries: Finance, insurance, and real estate
    'N4186C0A144NBEA', # Wage and salary accruals: Domestic private industries: Food services and drinking places
    'N4106C0A144NBEA', # Wage and salary accruals: Domestic private industries: Forestry, fishing, and related activities
    'N4163C0A144NBEA', # Wage and salary accruals: Domestic private industries: Funds, trusts, and other financial vehicles
    'N4176C0A144NBEA', # Wage and salary accruals: Domestic private industries: Health care and social assistance
    'B4168C0A144NBEA', # Wage and salary accruals: Domestic private industries: Health services
    'H4168C0A144NBEA', # Wage and salary accruals: Domestic private industries: Health services
    'J4168C0A144NBEA', # Wage and salary accruals: Domestic private industries: Health services
    'B4159C0A144NBEA', # Wage and salary accruals: Domestic private industries: Holding and other investment offices
    'N4178C0A144NBEA', # Wage and salary accruals: Domestic private industries: Hospitals
    'N4154C0A144NBEA', # Wage and salary accruals: Domestic private industries: Information
    'N4157C0A144NBEA', # Wage and salary accruals: Domestic private industries: Information: Broadcasting and telecommunications
    'N4158C0A144NBEA', # Wage and salary accruals: Domestic private industries: Information: Information and data processing services
    'N4156C0A144NBEA', # Wage and salary accruals: Domestic private industries: Information: Motion picture and sound recording industries
    'N4155C0A144NBEA', # Wage and salary accruals: Domestic private industries: Information: Publishing industries (includes software)
    'B4157C0A144NBEA', # Wage and salary accruals: Domestic private industries: Insurance agents, brokers, and service
    'H4157C0A144NBEA', # Wage and salary accruals: Domestic private industries: Insurance agents, brokers, and service
    'J4157C0A144NBEA', # Wage and salary accruals: Domestic private industries: Insurance agents, brokers, and service
    'B4156C0A144NBEA', # Wage and salary accruals: Domestic private industries: Insurance carriers
    'N4162C0A144NBEA', # Wage and salary accruals: Domestic private industries: Insurance carriers and related activities
    'B4169C0A144NBEA', # Wage and salary accruals: Domestic private industries: Legal services
    'J4169C0A144NBEA', # Wage and salary accruals: Domestic private industries: Legal services
    'N4168C0A144NBEA', # Wage and salary accruals: Domestic private industries: Legal services
    'J4140C0A144NBEA', # Wage and salary accruals: Domestic private industries: Local and interurban passenger transit
    'N4171C0A144NBEA', # Wage and salary accruals: Domestic private industries: Management of companies and enterprises
    'A4113C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing
    'H4113C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing
    'J4113C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing
    'N4113C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing (DISCONTINUED)
    'A4114C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods
    'H4114C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods
    'J4114C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods
    'N4114C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods
    'N4120C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Computer and electronic products
    'B4121C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Electric and electronic equipment
    'H4121C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Electric and electronic equipment
    'J4121C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Electric and electronic equipment
    'N4121C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Electrical equipment, appliances, and components
    'B4119C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Fabricated metal products
    'J4119C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Fabricated metal products
    'N4118C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Fabricated metal products
    'H4116C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Furniture and finished lumber products
    'B4116C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Furniture and fixtures
    'J4116C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Furniture and fixtures
    'N4124C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Furniture and related products
    'B4124C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Instruments and related products
    'J4124C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Instruments and related products
    'H4118C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Iron and steel and their products, including ordnance
    'H4115C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Lumber and basic timber products
    'B4115C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Lumber and wood products
    'J4115C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Lumber and wood products
    'N4119C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Machinery
    'B4120C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Machinery, except electrical
    'H4120C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Machinery, except electrical
    'J4120C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Machinery, except electrical
    'N4125C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Miscellaneous manufacturing
    'B4125C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Miscellaneous manufacturing industries
    'J4125C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Miscellaneous manufacturing industries
    'H4125C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Miscellaneous manufacturing, including instruments and miscellaneous plastic products
    'B4122C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Motor vehicles and equipment
    'H4122C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Motor vehicles and equipment
    'J4122C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Motor vehicles and equipment
    'N4122C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Motor vehicles, bodies and trailers, and parts
    'H4119C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Nonferrous metals and their products
    'N4116C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Nonmetallic mineral products
    'B4123C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Other transportation equipment
    'H4123C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Other transportation equipment
    'J4123C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Other transportation equipment
    'N4123C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Other transportation equipment
    'B4118C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Primary metal industries
    'J4118C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Primary metal industries
    'N4117C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Primary metals
    'B4117C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Stone, clay, and glass products
    'H4117C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Stone, clay, and glass products
    'J4117C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Stone, clay, and glass products
    'N4115C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Durable goods: Wood products
    'A4126C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods
    'H4126C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods
    'J4126C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods
    'N4126C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods
    'N4130C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Apparel and leather and allied products
    'B4130C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Apparel and other textile products
    'H4130C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Apparel and other textile products
    'J4130C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Apparel and other textile products
    'N4135C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Chemical products
    'B4133C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Chemicals and allied products
    'H4133C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Chemicals and allied products
    'J4133C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Chemicals and allied products
    'N4127C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Food and beverage and tobacco products
    'B4127C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Food and kindred products
    'H4127C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Food and kindred products
    'J4127C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Food and kindred products
    'B4136C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Leather and leather products
    'H4136C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Leather and leather products
    'J4136C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Leather and leather products
    'B4131C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Paper and allied products
    'J4131C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Paper and allied products
    'N4132C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Paper products
    'B4134C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Petroleum and coal products
    'H4134C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Petroleum and coal products
    'J4134C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Petroleum and coal products
    'N4134C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Petroleum and coal products
    'N4136C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Plastics and rubber products
    'B4132C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Printing and publishing
    'N4133C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Printing and related support activities
    'B4135C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Rubber and miscellaneous plastics products
    'J4135C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Rubber and miscellaneous plastics products
    'H4135C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Rubber products
    'B4129C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Textile mill products
    'H4129C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Textile mill products
    'J4129C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Textile mill products
    'N4129C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Textile mills and textile product mills
    'B4128C0A144NBEA', # Wage and salary accruals: Domestic private industries: Manufacturing: Nondurable goods: Tobacco manufactures
    'B4108C0A144NBEA', # Wage and salary accruals: Domestic private industries: Metal mining
    'A4107C0A144NBEA', # Wage and salary accruals: Domestic private industries: Mining
    'H4107C0A144NBEA', # Wage and salary accruals: Domestic private industries: Mining
    'J4107C0A144NBEA', # Wage and salary accruals: Domestic private industries: Mining
    'N4107C0A144NBEA', # Wage and salary accruals: Domestic private industries: Mining
    'N4109C0A144NBEA', # Wage and salary accruals: Domestic private industries: Mining, except oil and gas
    'H4110C0A144NBEA', # Wage and salary accruals: Domestic private industries: Mining: Crude petroleum and natural gas
    'B4111C0A144NBEA', # Wage and salary accruals: Domestic private industries: Mining: Nonmetallic minerals, except fuels
    'J4110C0A144NBEA', # Wage and salary accruals: Domestic private industries: Mining: Oil and gas extraction
    'N4108C0A144NBEA', # Wage and salary accruals: Domestic private industries: Mining: Oil and gas extraction
    'H4174C0A144NBEA', # Wage and salary accruals: Domestic private industries: Miscellaneous professional services
    'J4174C0A144NBEA', # Wage and salary accruals: Domestic private industries: Miscellaneous professional services
    'N4170C0A144NBEA', # Wage and salary accruals: Domestic private industries: Miscellaneous professional, scientific, and technical services
    'B4165C0A144NBEA', # Wage and salary accruals: Domestic private industries: Miscellaneous repair services
    'B4154C0A144NBEA', # Wage and salary accruals: Domestic private industries: Nondepository institutions
    'N4179C0A144NBEA', # Wage and salary accruals: Domestic private industries: Nursing and residential care facilities
    'B4110C0A144NBEA', # Wage and salary accruals: Domestic private industries: Oil and gas extraction
    'B4174C0A144NBEA', # Wage and salary accruals: Domestic private industries: Other services
    'N4187C0A144NBEA', # Wage and salary accruals: Domestic private industries: Other services, except government
    'N4152C0A144NBEA', # Wage and salary accruals: Domestic private industries: Other transportation and support activities
    'N4182C0A144NBEA', # Wage and salary accruals: Domestic private industries: Performing arts, spectator sports, museums, and related activities
    'B4162C0A144NBEA', # Wage and salary accruals: Domestic private industries: Personal services
    'J4162C0A144NBEA', # Wage and salary accruals: Domestic private industries: Personal services
    'N4151C0A144NBEA', # Wage and salary accruals: Domestic private industries: Pipeline transportation
    'N4167C0A144NBEA', # Wage and salary accruals: Domestic private industries: Professional, scientific, and technical services
    'N4147C0A144NBEA', # Wage and salary accruals: Domestic private industries: Rail transportation
    'B4139C0A144NBEA', # Wage and salary accruals: Domestic private industries: Railroad transportation
    'B4158C0A144NBEA', # Wage and salary accruals: Domestic private industries: Real estate
    'H4158C0A144NBEA', # Wage and salary accruals: Domestic private industries: Real estate
    'J4158C0A144NBEA', # Wage and salary accruals: Domestic private industries: Real estate
    'N4165C0A144NBEA', # Wage and salary accruals: Domestic private industries: Real estate
    'N4164C0A144NBEA', # Wage and salary accruals: Domestic private industries: Real estate and rental and leasing
    'N4166C0A144NBEA', # Wage and salary accruals: Domestic private industries: Rental and leasing services and lessors of intangible assets
    'B4151C0A144NBEA', # Wage and salary accruals: Domestic private industries: Retail trade
    'J4151C0A144NBEA', # Wage and salary accruals: Domestic private industries: Retail trade
    'N4140C0A144NBEA', # Wage and salary accruals: Domestic private industries: Retail trade
    'H4151C0A144NBEA', # Wage and salary accruals: Domestic private industries: Retail trade and automobile services
    'N4142C0A144NBEA', # Wage and salary accruals: Domestic private industries: Retail trade: Food and beverage stores
    'N4143C0A144NBEA', # Wage and salary accruals: Domestic private industries: Retail trade: General merchandise stores
    'N4141C0A144NBEA', # Wage and salary accruals: Domestic private industries: Retail trade: Motor vehicle and parts dealers
    'N4144C0A144NBEA', # Wage and salary accruals: Domestic private industries: Retail trade: Other retail
    'N4161C0A144NBEA', # Wage and salary accruals: Domestic private industries: Securities, commodity contracts, and investments
    'B4155C0A144NBEA', # Wage and salary accruals: Domestic private industries: Security and commodity brokers
    'J4155C0A144NBEA', # Wage and salary accruals: Domestic private industries: Security and commodity brokers
    'H4155C0A144NBEA', # Wage and salary accruals: Domestic private industries: Security and commodity brokers, and services
    'A4160C0A144NBEA', # Wage and salary accruals: Domestic private industries: Services
    'H4160C0A144NBEA', # Wage and salary accruals: Domestic private industries: Services
    'J4160C0A144NBEA', # Wage and salary accruals: Domestic private industries: Services
    'B4195C0A144NBEA', # Wage and salary accruals: Domestic private industries: Services: Commercial and trade schools and employment agencies
    'B4161C0A144NBEA', # Wage and salary accruals: Domestic private industries: Services: Hotels and other lodging places
    'B4173C0A144NBEA', # Wage and salary accruals: Domestic private industries: Services: Membership organizations
    'H4171C0A144NBEA', # Wage and salary accruals: Domestic private industries: Services: Membership organizations
    'B4166C0A144NBEA', # Wage and salary accruals: Domestic private industries: Services: Motion pictures
    'J4166C0A144NBEA', # Wage and salary accruals: Domestic private industries: Services: Motion pictures
    'B411RC0A144NBEA', # Wage and salary accruals: Domestic private industries: Services: Private households
    'N4180C0A144NBEA', # Wage and salary accruals: Domestic private industries: Social assistance
    'B4172C0A144NBEA', # Wage and salary accruals: Domestic private industries: Social services
    'A4171C0A144NBEA', # Wage and salary accruals: Domestic private industries: Social services and membership organizations
    'J4171C0A144NBEA', # Wage and salary accruals: Domestic private industries: Social services and membership organizations
    'N4110C0A144NBEA', # Wage and salary accruals: Domestic private industries: Support activities for mining
    'N4150C0A144NBEA', # Wage and salary accruals: Domestic private industries: Transit and ground passenger transportation
    'A4138C0A144NBEA', # Wage and salary accruals: Domestic private industries: Transportation
    'J4138C0A144NBEA', # Wage and salary accruals: Domestic private industries: Transportation
    'A4137C0A144NBEA', # Wage and salary accruals: Domestic private industries: Transportation and public utilities
    'B4149C0A144NBEA', # Wage and salary accruals: Domestic private industries: Transportation and public utilities: Electric, gas, and sanitary services
    'J4149C0A144NBEA', # Wage and salary accruals: Domestic private industries: Transportation and public utilities: Electric, gas, and sanitary services
    'B4194C0A144NBEA', # Wage and salary accruals: Domestic private industries: Transportation and public utilities: Local utilities and public services, n.e.c.
    'B4193C0A144NBEA', # Wage and salary accruals: Domestic private industries: Transportation and public utilities: Utilities: electric and gas
    'N4145C0A144NBEA', # Wage and salary accruals: Domestic private industries: Transportation and warehousing
    'B4143C0A144NBEA', # Wage and salary accruals: Domestic private industries: Transportation by air
    'H4143C0A144NBEA', # Wage and salary accruals: Domestic private industries: Transportation by air
    'J4143C0A144NBEA', # Wage and salary accruals: Domestic private industries: Transportation by air
    'B4145C0A144NBEA', # Wage and salary accruals: Domestic private industries: Transportation services
    'H4145C0A144NBEA', # Wage and salary accruals: Domestic private industries: Transportation services
    'J4145C0A144NBEA', # Wage and salary accruals: Domestic private industries: Transportation services
    'B4140C0A144NBEA', # Wage and salary accruals: Domestic private industries: Transportation: Local and interurban passenger transit
    'H4140C0A144NBEA', # Wage and salary accruals: Domestic private industries: Transportation: Local and interurban passenger transit
    'B4144C0A144NBEA', # Wage and salary accruals: Domestic private industries: Transportation: Pipelines, except natural gas
    'B4141C0A144NBEA', # Wage and salary accruals: Domestic private industries: Transportation: Trucking and warehousing
    'N4149C0A144NBEA', # Wage and salary accruals: Domestic private industries: Truck transportation
    'N4111C0A144NBEA', # Wage and salary accruals: Domestic private industries: Utilities
    'N4153C0A144NBEA', # Wage and salary accruals: Domestic private industries: Warehousing and storage
    'N4174C0A144NBEA', # Wage and salary accruals: Domestic private industries: Waste management and remediation services
    'B4142C0A144NBEA', # Wage and salary accruals: Domestic private industries: Water transportation
    'H4142C0A144NBEA', # Wage and salary accruals: Domestic private industries: Water transportation
    'J4142C0A144NBEA', # Wage and salary accruals: Domestic private industries: Water transportation
    'N4148C0A144NBEA', # Wage and salary accruals: Domestic private industries: Water transportation
    'B4150C0A144NBEA', # Wage and salary accruals: Domestic private industries: Wholesale trade
    'H4150C0A144NBEA', # Wage and salary accruals: Domestic private industries: Wholesale trade
    'J4150C0A144NBEA', # Wage and salary accruals: Domestic private industries: Wholesale trade
    'N4137C0A144NBEA', # Wage and salary accruals: Domestic private industries: Wholesale trade
    'N4138C0A144NBEA', # Wage and salary accruals: Domestic private industries: Wholesale trade: Durable goods
    'N4139C0A144NBEA', # Wage and salary accruals: Domestic private industries: Wholesale trade: Nondurable goods
    'A4177C0A144NBEA', # Wage and salary accruals: Federal Government
    'B4181C0A144NBEA', # Wage and salary accruals: Federal Government enterprises
    'A4178C0A144NBEA', # Wage and salary accruals: Federal general government
    'B4179C0A144NBEA', # Wage and salary accruals: Federal general government: Civilian
    'B4180C0A144NBEA', # Wage and salary accruals: Federal general government: Military
    'A553RC0A144NBEA', # Wage and salary accruals: Government (DISCONTINUED)
    'A4183C0A144NBEA', # Wage and salary accruals: State and local general government
    'B4184C0A144NBEA', # Wage and salary accruals: State and local general government: Education
    'B4185C0A144NBEA', # Wage and salary accruals: State and local general government: Other
    'A4182C0A144NBEA', # Wage and salary accruals: State and local government
    'B4186C0A144NBEA', # Wage and salary accruals: State and local government enterprises

]
