
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

    # Employment & Labor - U.S. Bureau of Labor Statistics(BLS)
    ## Current Population Survey (Household Survey)
    'CE16OV', # Employment Level
    'UNRATE', # Unemployment Rate
    'UNEMPLOY', # Unemployment Level
    'CIVPART', # Labor Force Participation Rate

    ## Current Employment Statistics (Establishment Survey)
    'PAYEMS',  # All Employees, Total Nonfarm
    # 'USPRIV',  # All Employees, Total Private

    # Employment - JOLTs
    ## Job Openings - level
    'JTSJOL', # Job Openings: Total Nonfarm
    'JTS1000JOL', # Job Openings: Total Private
    'JTU110099JOL', # Job Openings: Mining and Logging
    'JTS2300JOL', # Job Openings: Construction
    'JTS3000JOL', # Job Openings: Manufacturing
    'JTS4000JOL', # Job Openings: Trade, Transportation, and Utilities
    'JTU5100JOL', # Job Openings: Information
    'JTU510099JOL', # Job Openings: Financial Activities
    'JTS540099JOL', # Job Openings: Professional and Business Services
    'JTS6000JOL', # Job Openings: Private Education and Health Services
    'JTS7000JOL', # Job Openings: Leisure and Hospitality
    'JTU8100JOL', # Job Openings: Other Services
    'JTU9100JOL', # Job Openings: Federal
    'JTS9200JOL', # Job Openings: State and Local

    ## Job Openings - rate
    'JTSJOR', # Job Openings: Total Nonfarm
    'JTS1000JOR', # Job Openings: Total Private
    'JTU110099JOR', # Job Openings: Mining and Logging
    'JTS2300JOR', # Job Openings: Construction
    'JTS3000JOR', # Job Openings: Manufacturing
    'JTU4000JOR', # Job Openings: Trade, Transportation, and Utilities
    'JTU5100JOR', # Job Openings: Information
    'JTU510099JOR', #  Job Openings: Financial Activities
    'JTS540099JOR', # Job Openings: Professional and Business Services
    'JTS6000JOR', # Job Openings: Private Education and Health Services
    'JTS7000JOR', # Job Openings: Leisure and Hospitality
    'JTU8100JOR', # Job Openings: Other Services
    'JTU9100JOR', # Job Openings: Federal
    'JTS9200JOR', # Job Openings: State and Local

    ## Hires - level
    'JTSHIL', # Hires: Total Nonfarm
    'JTS1000HIL', # Hires: Total Private
    'JTS2300HIL', # Hires: Construction
    'JTS3000HIL', # Hires: Manufacturing
    'JTS4000HIL', # Hires: Trade, Transportation, and Utilities
    'JTU5100HIL', # Hires: Information
    'JTU510099HIL', # Hires: Financial Activities
    'JTS540099HIL', # Hires: Professional and Business Services
    'JTS6000HIL', # Hires: Private Education and Health Services
    'JTS7000HIL', # Hires: Leisure and Hospitality
    'JTU8100HIL', # Hires: Other Services
    'JTU9100HIL', # Hires: Federal
    'JTS9200HIL', # Hires: State and Local

    ## Hires - rate
    'JTSHIR', # Hires: Total Nonfarm
    'JTS1000HIR', # Hires: Total Private
    'JTS2300HIR', # Hires: Construction
    'JTS3000HIR', # Hires: Manufacturing
    'JTS4000HIR', # Hires: Trade, Transportation, and Utilities
    'JTU5100HIR', # Hires: Information
    'JTU510099HIR', # Hires: Financial Activities
    'JTS540099HIR', # Hires: Professional and Business Services
    'JTS6000HIR', # Hires: Private Education and Health Services
    'JTS7000HIR', # Hires: Leisure and Hospitality
    'JTU8100HIR', # Hires: Other Services
    'JTU9100HIR', # Hires: Federal
    'JTS9200HIR', # Hires: State and Local

    ## Separations - level
    'JTSTSL', # Total Separations: Total Nonfarm
    'JTS1000TSL', # Total Separations: Total Private
    'JTS2300TSL', # Total Separations: Construction
    'JTS3000TSL', # Total Separations: Manufacturing
    'JTS4000TSL', # Total Separations: Trade, Transportation, and Utilities
    'JTU5100TSL', # Total Separations: Information
    'JTU510099TSL', # Total Separations: Financial Activities
    'JTS540099TSL', # Total Separations: Professional and Business Services
    'JTS6000TSL', # Total Separations: Private Education and Health Services
    'JTS7000TSL', # Total Separations: Leisure and Hospitality
    'JTU8100TSL', # Total Separations: Other Services
    'JTU9100TSL', # Total Separations: Federal
    'JTS9200TSL', # Total Separations: State and Local

    ## Separations - rate
    'JTSTSR', # Total Separations: Total Nonfarm
    'JTS1000TSR', # Total Separations: Total Private
    'JTS2300TSR', # Total Separations: Construction
    'JTS3000TSR', # Total Separations: Manufacturing
    'JTS4000TSR', # Total Separations: Trade, Transportation, and Utilities
    'JTU5100TSR', # Total Separations: Information
    'JTU510099TSR', # Total Separations: Financial Activities
    'JTS540099TSR', # Total Separations: Professional and Business Services
    'JTS6000TSR', # Total Separations: Private Education and Health Services
    'JTS7000TSR', # Total Separations: Leisure and Hospitality
    'JTU8100TSR', # Total Separations: Other Services
    'JTU9100TSR', # Total Separations: Federal
    'JTS9200TSR', # Total Separations: State and Local

    'AWHAETP', # Average Weekly Hours of All Employees, Total Private
    'CES0500000003', # Average Hourly Earnings of All Employees, Total Private

    # Employemnt - ADP
    'ADPMNUSNERSA', #  Total Nonfarm Private Payroll Employment


    # Inflation & Consumption
    'CPIAUCSL', # Consumer Price Index for All Urban Consumers: All Items in U.S. City Average
    'CORESTICKM159SFRBATL', # Sticky Price Consumer Price Index less Food and Energy
    'PCE',  # Personal Consumption Expenditures
    'PCEC96', # Real Personal Consumption Expenditures

    'DSPI', # Disposable Personal Income
    'DSPIC96', # Real Disposable Personal Income
    'TOTALSA', # Total Vehicle Sales

    # Inflation & Consumption - Housing price
    'CSUSHPINSA', # S&P CoreLogic Case-Shiller U.S. National Home Price Index
    'SPCS20RSA', # S&P CoreLogic Case-Shiller 20-City Composite Home Price Index
    'SPCS10RSA', # S&P CoreLogic Case-Shiller 10-City Composite Home Price Index
    'USSTHPI', # All-Transactions House Price Index for the United States

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
    # 'AAA', # Moody's Seasoned Aaa Corporate Bond Yield
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

    # Employment - ADP
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
