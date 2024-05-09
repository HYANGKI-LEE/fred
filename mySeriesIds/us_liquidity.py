
dir='us_liquidity'

ids_Q = ['MMMFFAQ027S',
                'M1V',
                'M2V',
                'BOGZ1FL193020005Q',
                'GDP',

                'GFDEBTN',
                'GFDEGDQ188S',
                'USSTHPI' # All-Transactions House Price Index for the United States
                ]

ids_M = ['CURRCIR',
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

ids_W_wed = ['WALCL', # assets : total assets (less elimination from consolidation) (wednesday level)
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

ids_W_mon = ['WRMFNS', # Ratail Money Market Funds
                    'WM1NS', # M1 (weekly)
                    'WM2NS', # M2 (weekly)
                    ]


ids_D = ['RPONTSYD',
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
