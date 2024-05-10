
dir='us_macro'

# Quarterly
ids_Q = [
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

    'CURRCIR', # Currency in Circulation

    # Employment & Labor - U.S. Bureau of Labor Statistics
    'PAYEMS', # All Employees, Total Nonfarm
    'UNRATE', # Unemployment Rate
    'JTSJOL', # Job Openings: Total Nonfarm
    'AWHAETP', # Average Weekly Hours of All Employees, Total Private
    'CES0500000003', # Average Hourly Earnings of All Employees, Total Private

    # Consumption
    'TOTALSA', # Total Vehicle Sales

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

# Weekly
ids_W_wed = ['TOTCI', # Commercial and Industrial Loans, All Commercial Banks
                  ]
ids_W_sat = [
    # Employment
    'ICNSA', # Initial Claims
    'ADPWNUSNERSA', # Total Nonfarm Private Payroll Employment
]

# Daily
ids_D = [
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
