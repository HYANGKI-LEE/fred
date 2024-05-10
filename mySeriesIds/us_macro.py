
dir='us_macro'

# Quarterly
ids_Q = [
    # Monetary
    'M2V', # Velocity of M2 Money Stock

    # Inflation
    'ECIWAG', # Employment Cost Index: Wages and Salaries: Private Industry Workers

    # Business
    'BOGZ1FA106030005Q', # Nonfinancial Corporate Business; Revenue from Sales of Goods and Services, Excluding Indirect Sales Taxes (FSIs), Transactions
    'NFCPATAX', # Nonfinancial Corporate Business: Profits After Tax
    'NCBCMDPMVCE', # Nonfinancial Corporate Business; Debt as a Percentage of the Market Value of Corporate Equities, Level


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

# Monthly
ids_M = [
    # Liquidity
    'CURRCIR', # Currency in Circulation

    # Employment & Labor - U.S. Bureau of Labor Statistics
    'PAYEMS', # All Employees, Total Nonfarm
    'CIVPART', # Labor Force Participation Rate
    'UNEMPLOY', # Unemployment Level
    'UNRATE', # Unemployment Rate
    'JTSJOL', # Job Openings: Total Nonfarm,

    'AWHAETP', # Average Weekly Hours of All Employees, Total Private
    'CES0500000003', # Average Hourly Earnings of All Employees, Total Private

    # Inflation & Consumption
    'CPIAUCSL', # Consumer Price Index for All Urban Consumers: All Items in U.S. City Average
    'CORESTICKM159SFRBATL', # Sticky Price Consumer Price Index less Food and Energy
    'PCE',  # Personal Consumption Expenditures
    'PCEC96', # Real Personal Consumption Expenditures

    'DSPI', # Disposable Personal Income
    'DSPIC96', # Real Disposable Personal Income
    'TOTALSA', # Total Vehicle Sales

    # Manufacturing - Census Bureau
    'MNFCTRIMSA', # Manufacturers Inventories
    'MNFCTRSMSA', # Manufacturers Sales
    'MNFCTRIRSA',  # Manufacturers: Inventories to Sales Ratio

    'AMTMNO', # Manufacturers' New Orders: Total Manufacturing
    'AMTMTI', # Manufacturers' Total Inventories: Total Manufacturing
    'AMTMVS', # Manufacturers' Value of Shipments: Total Manufacturing
    'AMTMIS', # Manufacturers' Inventories to Shipments Ratios: Total Manufacturing

    # OECD
    'OECDLOLITOAASTSAM', # Leading Indicators OECD: Leading indicators: CLI: Amplitude adjusted for OECD - Total

    # Yield - Moody's
    'AAA', # Moody's Seasoned Aaa Corporate Bond Yield
]

# Weekly
ids_W_wed = [
    'TOTCI', # Commercial and Industrial Loans, All Commercial Banks
    'TOTLL', # Loans and Leases in Bank Credit, All Commercial Banks
    'CREACBW027SBOG', # Real Estate Loans: Commercial Real Estate Loans, All Commercial Banks
    'CCLACBW027SBOG', # Consumer Loans: Credit Cards and Other Revolving Plans, All Commercial Banks

    'DPSACBW027SBOG', # Deposits, All Commercial Banks
    'TOTBKCR', # Bank Credit, All Commercial Banks
                  ]
ids_W_thu = [
    'MORTGAGE30US', # 30-Year Fixed Rate Mortgage Average in the United States

]
ids_W_sat = [
    # Employment
    'ICNSA', # Initial Claims
    'ADPWNUSNERSA', # Total Nonfarm Private Payroll Employment
]

# Daily
ids_D = [
    # Rate
    'DFEDTAR', # Federal Funds Target Rate (DISCONTINUED)
    'DFEDTARL', # Federal Funds Target Range - Lower Limit
    'DFEDTARU', # Federal Funds Target Range - Upper Limit
    'DFF', # Federal Funds Effective Rate
    'T5YIE', # 5-Year Breakeven Inflation Rate

    # OAS
    'BAMLC0A0CM', # ICE BofA US Corporate Index Option-Adjusted Spread
    'BAMLH0A0HYM2', # ICE BofA US High Yield Index Option-Adjusted Spread

    # Yield
    'BAMLH0A0HYM2EY', # ICE BofA US High Yield Index Effective Yield
    'BAMLC0A4CBBB', # ICE BofA BBB US Corporate Index Option-Adjusted Spread

    # Recession
    'USRECDP', # NBER based Recession Indicators for the United States from the Peak through the Period preceding the Trough

    #
    'USEPUINDXD', # Economic Policy Uncertainty Index for United States
]
