######################
###### US MACRO ######
######################

# Quarterly
us_macro_ids_Q = ['DRTSCILM', 'DRTSCIS', 'DRTSCLCC', 'STDSAUTO', 'DRBLACBS']
us_macro_dir_Q = 'us_macro(Q)'

# Monthly
us_macro_ids_M = ['CURRCIR']
us_macro_dir_M = 'us_macro(M)'

# Weekly
us_macro_ids_W = ['TOTCI']
us_macro_dir_W = 'us_macro(W)'

# Daily
us_macro_ids_D = ['USRECDP']
us_macro_dir_D = 'us_macro(D)'

################################
###### FED BALANCE SHEETS ######
################################
fed_bs_ids_Q = ['MMMFFAQ027S',
                'M1V',
                'M2V',
                'BOGZ1FL193020005Q']
fed_bs_dir_Q='fed_bs(Q)'

fed_bs_ids_M = ['CURRCIR',
                'BOGMBASE', # Monetary Base (Total)

                'M1SL', 'M1NS', # M1
                'M1REAL', # M1 deflated with CPI

                'M2SL', 'M2NS',  # M2
                'FEDFUNDS',
                'DPSACBM027NBOG',
                'SAVINGSL'
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
                'DPCREDIT']
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

