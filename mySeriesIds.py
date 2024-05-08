######################
###### US MACRO ######
######################

# Quarterly
us_macro_ids_Q = [
    # SLOOS
    'DRTSCILM', # Net Percentage of Domestic Banks Tightening Standards for Commercial and Industrial Loans to Large and Middle-Market Firms
    'DRTSCIS', # Net Percentage of Domestic Banks Tightening Standards for Commercial and Industrial Loans to Small Firms
    'DRTSCLCC', # Net Percentage of Domestic Banks Tightening Standards for Credit Card Loans
    'STDSAUTO', # Net Percentage of Domestic Banks Tightening Standards for Auto Loans

    # Delinquency Rate
    'DRBLACBS', # Delinquency Rate on Business Loans, All Commercial Banks
    'DRCCLACBS', # Delinquency Rate on Credit Card Loans, All Commercial Banks
    'DRCLACBS', # Delinquency Rate on Consumer Loans, All Commercial Banks
    'DRALACBN', # Delinquency Rate on All Loans, All Commercial Banks
                  ]
us_macro_dir_Q = 'us_macro(Q)'

# Monthly
us_macro_ids_M = [

    'CURRCIR', # Currency in Circulation

    # Employment & Labor - U.S. Bureau of Labor Statistics
    'PAYEMS', # All Employees, Total Nonfarm
    'UNRATE', # Unemployment Rate
    'JTSJOL', # Job Openings: Total Nonfarm

    # Manufacturing - Census Bureau
    'MNFCTRIMSA', # Manufacturers Inventories
    'MNFCTRSMSA', # Manufacturers Sales
    'MNFCTRIRSA',  # Manufacturers: Inventories to Sales Ratio

    'AMTMNO', # Manufacturers' New Orders: Total Manufacturing
    'AMTMTI', # Manufacturers' Total Inventories: Total Manufacturing
    'AMTMVS', # Manufacturers' Value of Shipments: Total Manufacturing
    'AMTMIS', # Manufacturers' Inventories to Shipments Ratios: Total Manufacturing

    # Yield - Moody's
    'AAA', # Moody's Seasoned Aaa Corporate Bond Yield
]
us_macro_dir_M = 'us_macro(M)'

# Weekly
us_macro_ids_W_wed = ['TOTCI', # Commercial and Industrial Loans, All Commercial Banks
                  ]
us_macro_dir_W_wed = 'us_macro(W)_wed'

us_macro_ids_W_sat = [
    # Employment
    'ICNSA', # Initial Claims
    'ADPWNUSNERSA', # Total Nonfarm Private Payroll Employment
]
us_macro_dir_W_sat = 'us_macro(W)_sat'

# Daily
us_macro_ids_D = [
    # OAS
    'BAMLC0A0CM', # ICE BofA US Corporate Index Option-Adjusted Spread
    'BAMLH0A0HYM2', # ICE BofA US High Yield Index Option-Adjusted Spread

    # Yield
    'BAMLH0A0HYM2EY', # ICE BofA US High Yield Index Effective Yield

    'BAMLC0A4CBBB', # ICE BofA BBB US Corporate Index Option-Adjusted Spread


    'USRECDP',
                  ]
us_macro_dir_D = 'us_macro(D)'










################################
###### FED BALANCE SHEETS ######
################################
fed_bs_ids_Q = ['MMMFFAQ027S',
                'M1V',
                'M2V',
                'BOGZ1FL193020005Q',
                'GDP',

                'GFDEBTN',
                'GFDEGDQ188S',
                'USSTHPI' # All-Transactions House Price Index for the United States
                ]
fed_bs_dir_Q='fed_bs(Q)'

fed_bs_ids_M = ['CURRCIR',
                'BOGMBASE', # Monetary Base (Total)

                'M1SL', 'M1NS', # M1
                'M1REAL', # M1 deflated with CPI

                'M2SL', 'M2NS',  # M2
                'FEDFUNDS',
                'DPSACBM027NBOG',
                'SAVINGSL',

                'USSLIND',
                'CONSUMER', # Consumer Loans, All Commercial Banks
                # 'REALLN', # Real Estate Loans, All Commercial Banks
                'REALLNNSA', # Real Estate Loans, All Commercial Banks
                'BUSLOANS',  # Commercial and Industrial Loans, All Commercial Banks
                'CSUSHPINSA', # S&P CoreLogic Case-Shiller U.S. National Home Price Index


                ]
fed_bs_dir_M='fed_bs(M)'

fed_bs_ids_W_wed = ['WALCL', # assets : total assets (less elimination from consolidation) (wednesday level)
                    'WSHOMCB', # assets : securities held outright : MBS (wednesday level)
                    'WSHOTSL', # assets : securities held outright : UST (wednesday level)
                    'WLCFLL',  # assets : liquidity and credit facilities : Loans (wednesday level)
                    'H41RESPPALDKNWW', # assets : liquidity and credit facilities : Bank Term Funding Program

                    'RESPPLNWW', # liabilities and capital : total liabilities and capital (wednesday level)
                    'WLTLECL', # liabilities and capital : total liabilities (less elimination from consolidation) (wednesday level)
                    'WCTCL', # liabilities and capital : total capital (wednesday level)
                    'WRBWFRBL', # liabilities and capital : other factors draining reserve balances : reserve balance with FRB (wednesday level)
                    'WLRRAL', # liabilities and capital : RRP (wednesday level)
                    'WDTGAL', # liabilities and capital : deposits with FRB, toher than reserve balances : US TGA (wednesday level)
                    'WCICL', # liabilities and capital : other factors draining reserve balances : currency in circulation (wednesday level)

                    'DPSACBW027SBOG', # Deposits, All Commercial Banks
                    'DPSLCBW027SBOG', # Deposits, Large Domestically Chartered Commercial Banks
                    'DPSSCBW027SBOG', # Deposits, Small Domestically Chartered Commercial Banks
                    'CCLACBW027SBOG', # Consumer loans: Credit cards and Other revolving plans, All Commercial Banks
                    'TOTBKCR', # Bank Credit, All Commercial Banks
                    'RHEACBW027SBOG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, All Commercial Banks
                    'CREACBW027SBOG', # Real Estate Loans: Commercial Real Estate Loans, All Commercial Banks
                    'TLAACBW027SBOG', # Total Assets, All Commercial Banks
                    'CASACBW027SBOG', # Cash Assets, All Commercial Banks

                ]
fed_bs_dir_W_wed = 'fed_bs(W)_wed'

fed_bs_ids_W_mon = ['WRMFNS', # Ratail Money Market Funds
                    'WM1NS', # M1 (weekly)
                    'WM2NS', # M2 (weekly)
                    ]
fed_bs_dir_W_mon = 'fed_bs(W)_mon'


fed_bs_ids_D = ['RPONTSYD',
                'RRPONTSYD',
                'RRPONTSYAWARD',
                'SOFR30DAYAVG', 'SOFR90DAYAVG', 'SOFR180DAYAVG',
                'EFFR',
                'IORB',
                'DFEDTARU',
                'DPCREDIT',

                'SP500',
                'BAMLH0A0HYM2',
                'DTWEXBGS',

                'DGS3MO', # Market Yield on U.S. Treasury Securities at 3-Month Constant Maturity, Quoted on an Investment Basis
                'DGS1', # Market Yield on U.S. Treasury Securities at 1-Year Constant Maturity, Quoted on an Investment Basis
                'DGS5', # Market Yield on U.S. Treasury Securities at 5-Year Constant Maturity, Quoted on an Investment Basis
                'DGS7', # Market Yield on U.S. Treasury Securities at 7-Year Constant Maturity, Quoted on an Investment Basis
                'DGS10', # Market Yield on U.S. Treasury Securities at 10-Year Constant Maturity, Quoted on an Investment Basis
                'DGS20', # Market Yield on U.S. Treasury Securities at 20-Year Constant Maturity, Quoted on an Investment Basis
                'DGS30', # Market Yield on U.S. Treasury Securities at 30-Year Constant Maturity, Quoted on an Investment Basis
                ]
fed_bs_dir_D = 'fed_bs(D)'

########################
###### US HISTORY ######
########################

# Annually
us_history_ids_Q = ['GDPA', # Gross Domestic Product
                    ]
us_history_dir_Q = 'us_history(A)'

# Quarterly
us_history_ids_Q = ['GDP', # Gross Domestic Product
                    ]
us_history_dir_Q = 'us_history(Q)'

# Monthly
us_history_ids_M = ['CPIAUCSL', # Consumer Price Index for All Urban Consumers: All Items in U.S. City Average
                    'CORESTICKM159SFRBATL', # Sticky Price Consumer Price Index less Food and Energy (YoY)
                    'PCEPI', # Personal Consumption Expenditures: Chain-type Price Index
                    'PCEPILFE', # Personal Consumption Expenditures Excluding Food and Energy (Chain-Type Price Index)
                    'FEDFUNDS', # Federal Funds Effective Rate
                    ]
us_history_dir_M = 'us_history(M)'

# Weekly
us_history_ids_W = ['']
us_history_dir_W = 'us_history(W)'

# Daily
us_history_ids_D = ['SP500', # S&P 500
                    'DJIA', # Dow Jones Industrial Average
                    'NASDAQCOM', # NASDAQ Composite Index
                    ]
us_history_dir_D = 'us_history(D)'

