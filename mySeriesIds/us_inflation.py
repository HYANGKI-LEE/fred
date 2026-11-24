
dir='us_macro'

# Quarterly
ids_Q = [
    # Monetary
    'M2V', # Velocity of M2 Money Stock

    # GDP
    'GDP', # Gross Domestic Product
    'GDPDEF', # Gross Domestic Product: Implicit Price Deflator
    'DPCERL1Q225SBEA', # Real Personal Consumption Expenditures
    'CP', # Corporate Profits After Tax (without IVA and CCAdj)

    # Real GDP (https://fred.stlouisfed.org/release/tables?eid=14961&rid=53)
    'GDPC1', # Real Gross Domestic Product
    'PCECC96', # Real Personal Consumption Expenditures
        'DGDSRX1Q020SBEA', # Real personal consumption expenditures: Goods
        'PCESVC96', # Real Personal Consumption Expenditures: Services
            'DRCARX1Q020SBEA', # Real personal consumption expenditures: Recreation services
    'GPDIC1', # Real Gross Private Domestic Investment
        'FPIC1', # Real Private Fixed Investment
            'PNFIC1', # Real Private Nonresidential Fixed Investment
            'Y033RX1Q020SBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment
            'Y034RX1Q020SBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment: Information Processing Equipment
            'PRFIC1', # Real Private Residential Fixed Investment
            'B985RX1Q020SBEA', # Real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Intellectual property products: Software
            'Y006RX1Q020SBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products: Research and Development
        'CBIC1', # Change in Real Private Inventories
    'NETEXC', # Real Net Exports of Goods and Services
        'EXPGSC1', # Real Exports of Goods and Services
        'IMPGSC1', # Real imports of goods and services
    'GCEC1', # Real Government Consumption Expenditures and Gross Investment
        'FGCEC1', # Real Federal Consumption Expenditures and Gross Investment
        'SLCEC1', # Real State and Local Consumption Expenditures & Gross Investment, 1 Decimal
        'AR05RX1Q020SBEA', # Real gross domestic product: Residual


    # GDP : Contributions
    'A191RL1Q225SBEA',  # Real Gross Domestic Product

    'DPCERY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures
    'DGDSRY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Goods
    'DSERRY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Services
    'DHCERY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Services: Household consumption expenditures (for services)
    'DHLCRY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Services: Health care
    'A006RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment
    'A019RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Net exports of goods and services
    'A822RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Government consumption expenditures and gross investment
    'DHCERY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Services: Household consumption expenditures (for services)
    'DHLCRY2Q224SBEA', # Contributions to percent change in real gross domestic product: Personal consumption expenditures: Services: Health care

    # PCE : Decompositions
    'PCEC', # Personal Consumption Expenditures
    'PCESV', # Personal Consumption Expenditures: Services
    'DHLCRC1Q027SBEA', # Personal consumption expenditures: Services: Health care

    # Real PCE - Table 2.3.1. Percent Change From Preceding Period in Real Personal Consumption Expenditures by Major Type of Product:
    # https://fred.stlouisfed.org/release/tables?eid=4946&rid=53
    'DPCERL1Q225SBEA', # Real Personal Consumption Expenditures
    'DGDSRL1Q225SBEA', # Real Personal Consumption Expenditures: Goods
    'DSERRL1Q225SBEA', # Real Personal Consumption Expenditures: Services
    'DHCERL1Q225SBEA', # Real Personal Consumption Expenditures: Services: Household Consumption Expenditures
    'DNPIRL1Q225SBEA', # Real Personal Consumption Expenditures: Services: Final Consumption Expenditures of Nonprofit Institutions Serving Households (NPISHs)

    # GDP - Detailed (https://fred.stlouisfed.org/release/tables?rid=53&eid=14897#snid=14898)
    'GDP', # Gross Domestic Product
    'PCEC', # Personal Consumption Expenditures
    'DGDSRC1Q027SBEA', # Personal consumption expenditures: Goods
    'PCDG', # Personal Consumption Expenditures: Durable Goods
    'DMOTRC1Q027SBEA', # Personal consumption expenditures: Durable goods: Motor vehicles and parts
    'DFDHRC1Q027SBEA', # Personal consumption expenditures: Durable goods: Furnishings and durable household equipment
    'DREQRC1Q027SBEA', # Personal consumption expenditures: Durable goods: Recreational goods and vehicles
    'DODGRC1Q027SBEA', # Personal consumption expenditures: Durable goods: Other durable goods
    'PCND', # Personal Consumption Expenditures: Nondurable Goods
    'DFXARC1Q027SBEA', # Personal consumption expenditures: Nondurable goods: Food and beverages purchased for off-premises consumption
    'DCLORC1Q027SBEA', # Personal consumption expenditures: Nondurable goods: Clothing and footwear
    'DGOERC1Q027SBEA', # Personal consumption expenditures: Nondurable goods: Gasoline and other energy goods
    'DONGRC1Q027SBEA', # Personal consumption expenditures: Nondurable goods: Other nondurable goods
    'PCESV', # Personal Consumption Expenditures: Services
    'DHCERC1Q027SBEA', # Personal consumption expenditures: Services: Household consumption expenditures
    'DHUTRC1Q027SBEA', # Personal consumption expenditures: Services: Housing and utilities
    'DHLCRC1Q027SBEA', # Personal consumption expenditures: Services: Health care
    'DTRSRC1Q027SBEA', # Personal consumption expenditures: Transportation services
    'DRCARC1Q027SBEA', # Personal consumption expenditures: Recreation services
    'DFSARC1Q027SBEA', # Personal consumption expenditures: Services: Food services and accommodations
    'DIFSRC1Q027SBEA', # Personal consumption expenditures: Financial services and insurance
    'DOTSRC1Q027SBEA', # Personal consumption expenditures: Other services
    'DNPIRC1Q027SBEA', # Personal consumption expenditures: Services: Final consumption expenditures of nonprofit institutions serving households (NPISHs)
    'DNPERC1Q027SBEA', # Personal consumption expenditures: Services: Gross output of nonprofit institutions
    'DNPSRC1Q027SBEA', # Personal consumption expenditures: Services: Receipts from sales of goods and services by nonprofit institutions
    'GPDI', # Gross Private Domestic Investment
    'FPI', # Fixed Private Investment
    'PNFI', # Private Nonresidential Fixed Investment
    'B009RC1Q027SBEA', # Private fixed investment: Nonresidential: Structures
    'Y033RC1Q027SBEA', # Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment
    'Y034RC1Q027SBEA', # Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment: Information Processing Equipment
    'B935RC1Q027SBEA', # Private fixed investment: Nonresidential: Information processing equipment and software: Computers and peripheral equipment
    'A937RC1Q027SBEA', # Private fixed investment: Nonresidential: Equipment: Information processing equipment: Other
    'A680RC1Q027SBEA', # Private fixed investment: Nonresidential: Equipment: Industrial equipment
    'A681RC1Q027SBEA', # Private fixed investment: Nonresidential: Equipment: Transportation equipment
    'A862RC1Q027SBEA', # Private fixed investment: Nonresidential: Equipment: Other equipment
    'Y001RC1Q027SBEA', # Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products
    'B985RC1Q027SBEA', # Private fixed investment: Nonresidential: Intellectual property products: Software
    'Y006RC1Q027SBEA', # Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products: Research and Development
    'Y020RC1Q027SBEA', # Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products: Entertainment, Literary, and Artistic Originals
    'PRFI', # Private Residential Fixed Investment
    'CBI', # Change in Private Inventories
    'B018RC1Q027SBEA', # Change in private inventories: Farm
    'A015RC1Q027SBEA',  # Change in private inventories: Nonfarm
    'NETEXP', # Net Exports of Goods and Services
    'EXPGS', # Exports of Goods and Services
    'A253RC1Q027SBEA', # Current receipts from the rest of the world: Exports of goods
    'A646RC1Q027SBEA', # Current receipts from the rest of the world: Exports of services
    'IMPGS', # Imports of Goods and Services
    'A255RC1Q027SBEA', # Current payments to the rest of the world: Imports of goods
    'B656RC1Q027SBEA', # Current payments to the rest of the world: Imports of services

    'B009RX1Q020SBEA', # Real gross private domestic investment: Fixed investment: Nonresidential: Structures
    'Y033RX1Q020SBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment
    'PRFIC1', # Real Private Residential Fixed Investment

    'GCE', # Government Consumption Expenditures and Gross Investment
    'FGCE', # Federal Consumption Expenditures and Gross Investment
    'FDEFX', # Federal Government: National Defense Consumption Expenditures and Gross Investment
    'A997RC1Q027SBEA', # Government consumption expenditures: Federal: National defense
    'DGI', # Federal Government: National Defense Gross Investment
    'FNDEFX', # Federal Government: Nondefense Consumption Expenditures and Gross Investment
    'A542RC1Q027SBEA', # Government consumption expenditures: Federal: Nondefense
    'NDGI', # Federal Nondefense Gross Investment
    'SLCE', # State and Local Consumption Expenditures & Gross Investment
    'A991RC1Q027SBEA', # Government consumption expenditures: State and local
    'SLINV', # State and Local Government Gross Investment

    # Inflation - ECI
    'ECIWAG', # Employment Cost Index: Wages and Salaries: Private Industry Workers
    'ECIALLCIV', # Employment Cost Index: Total compensation: All Civilian


    # Balnace Sheet of Households - https://fred.stlouisfed.org/release/tables?rid=52&eid=810420#snid=810428
    'BOGZ1FL192000005Q', # Households; Total Assets, Level  (NSA)
    'BOGZ1LM192010005Q', # Households; Nonfinancial Assets, Market Value Levels (NSA)
    'HOOREVLMHMV', # Households; Owner-Occupied Real Estate Including Vacant Land and Mobile Homes at Market Value, Market Value Levels
    'BOGZ1FL194090005Q', # Households; Total Financial Assets, Level (NSA)
    'BOGZ1FL193020005Q', # Households; Checkable Deposits and Currency; Asset, Level (NSA)
    'BOGZ1FL193030205Q', # Households; Other Deposits Including Time and Savings Deposits; Asset (IMA), Level
    'BOGZ1FL193034005Q', # Households; Money Market Fund Shares; Asset, Level
    'BOGZ1LM194022005Q', # Households; Debt Securities; Asset, Market Value Levels (NSA)
    'BOGZ1LM193064005Q', # Households; Corporate Equities and Mutual Fund Shares; Asset, Market Value Levels (NSA)
    'BOGZ1LM152090205Q', # Households and Nonprofit Organizations; Proprietors' Equity in Noncorporate Business, Market Value Levels (NSA)
    'BOGZ1FL192090005Q', # Households; Net Worth, Level

    # 'TNWBSHNO', # Households and Nonprofit Organizations; Net Worth, Level
    'TFAABSHNO', # Households and Nonprofit Organizations; Total Financial Assets, Level
    'CDCABSHNO', # Households and Nonprofit Organizations; Checkable Deposits and Currency; Asset, Level
    'BOGZ1FL153064486Q', # Households and Nonprofit Organizations; Directly and Indirectly Held Corporate Equities as a Percentage of Financial Assets; Assets, Level

    'BOGZ1FL192000005Q', # Households; Total Assets, Level
    'BOGZ1FL194090005Q', # Households; Total Financial Assets, Level
    'BOGZ1FL193020005Q', # Households; Checkable Deposits and Currency; Asset, Level
    'BOGZ1FL193034005Q', # Households; Money Market Fund Shares; Asset, Level
    'BOGZ1LM193064005Q', # Households; Corporate Equities and Mutual Fund Shares; Asset, Market Value Levels

    #
    'DPI', # Disposable Personal Income
    'PCECTPI', # Personal Consumption Expenditures: Chain-type Price Index
    'CDSP', # Consumer Debt Service Payments as a Percent of Disposable Personal Income

    # Shares of Wealth by Wealth Percentile Groups - https://fred.stlouisfed.org/release/tables?rid=453&eid=813804#snid=813829
    'WFRBST01108', # Share of Total Assets Held by the Top 1% (99th to 100th Wealth Percentiles)
    'WFRBSN09135', # Share of Total Assets Held by the 90th to 99th Wealth Percentiles
    'WFRBSN40162', # Share of Total Assets Held by the 50th to 90th Wealth Percentiles
    'WFRBSB50189', # Share of Total Assets Held by the Bottom 50% (1st to 50th Wealth Percentiles)

    # Levels of Wealth by Wealth Percentile Groups - https://fred.stlouisfed.org/release/tables?rid=453&eid=813668
    'WFRBLT01004', # Financial Assets Held by the Top 1% (99th to 100th Wealth Percentiles)
    'WFRBLN09031', # Financial Assets Held by the 90th to 99th Wealth Percentiles
    'WFRBLN40058', # Financial Assets Held by the 50th to 90th Wealth Percentiles
    'WFRBLB50085', # Financial Assets Held by the Bottom 50% (1st to 50th Wealth Percentiles)

    # Wage Growth
    'LEU0252916100Q', # Employed full time: Usual weekly nominal earnings (first quartile): Wage and salary workers: 25 years and over
    'LEU0252887700Q', # Employed full time: Median usual weekly nominal earnings (second quartile): Wage and salary workers: 25 years and over
    'LEU0252916200Q', # Employed full time: Usual weekly nominal earnings (third quartile): Wage and salary workers: 25 years and over
    'LEU0252916300Q', # Employed full time: Usual weekly nominal earnings (ninth decile): Wage and salary workers: 25 years and over

    # Business
    'BOGZ1FA106030005Q', # Nonfinancial Corporate Business; Revenue from Sales of Goods and Services, Excluding Indirect Sales Taxes (FSIs), Transactions
    'NFCPATAX', # Nonfinancial Corporate Business: Profits After Tax
    'BCNSDODNS', # Nonfinancial Corporate Business; Debt Securities and Loans; Liability, Level
    'NCBCMDPMVCE', # Nonfinancial Corporate Business; Debt as a Percentage of the Market Value of Corporate Equities, Level
    'BOGZ1FA105050005Q', # Nonfinancial Corporate Business; Total Capital Expenditures, Transactions (SA)
    'BOGZ1FU105050005Q', # Nonfinancial Corporate Business; Total Capital Expenditures, Transactions (NSA)

    'BOGZ1FA315050005Q', # Federal Government; Total Capital Expenditures, Transactions (SA)
    'BOGZ1FU315050005Q', # Federal Government; Total Capital Expenditures, Transactions (NSA)

    # SLOOS
    'DRTSCILM', # Net Percentage of Domestic Banks Tightening Standards for Commercial and Industrial Loans to Large and Middle-Market Firms
    'DRTSCIS', # Net Percentage of Domestic Banks Tightening Standards for Commercial and Industrial Loans to Small Firms
    'DRISCFLM', # Net Percentage of Domestic Banks Increasing Spreads of Loan Rates over Banks' Cost of Funds to Large and Middle-Market Firms
    'DRISCFS', # Net Percentage of Domestic Banks Increasing Spreads of Loan Rates over Banks' Cost of Funds to Small Firms
    'DRSDCILM', # Net Percentage of Domestic Banks Reporting Stronger Demand for Commercial and Industrial Loans from Large and Middle-Market Firms
    'DRSDCIS', # Net Percentage of Domestic Banks Reporting Stronger Demand for Commercial and Industrial Loans from Small Firms
    'SUBLPDRCSC', # Net Percentage of Domestic Banks Tightening Standards for Commercial Real Estate Loans with Construction and Land Development Purposes
    'SUBLPDRCSM', # Net Percentage of Domestic Banks Tightening Standards for Commercial Real Estate Loans Secured by Multifamily Residential Structures
    'SUBLPDRCSN', # Net Percentage of Domestic Banks Tightening Standards for Commercial Real Estate Loans Secured by Nonfarm Nonresidential Structures
    'SUBLPDRCDC', # Net Percentage of Domestic Banks Reporting Stronger Demand for Commercial Real Estate Loans with Construction and Land Development Purposes
    'SUBLPDRCDM', # Net Percentage of Domestic Banks Reporting Stronger Demand for Commercial Real Estate Loans Secured by Multifamily Residential Structures
    'SUBLPDRCDN', # Net Percentage of Domestic Banks Reporting Stronger Demand for Commercial Real Estate Loans Secured by Nonfarm Nonresidential Structures

    'DRTSCLCC', # Net Percentage of Domestic Banks Tightening Standards for Credit Card Loans
    'STDSAUTO', # Net Percentage of Domestic Banks Tightening Standards for Auto Loans
    'STDSOTHCONS', # Net Percentage of Domestic Banks Tightening Standards for Consumer Loans Excluding Credit Card and Auto Loans
    'DRIWCIL', # Net Percentage of Domestic Banks Reporting Increased Willingness to Make Consumer Installment Loans
    'DEMCC', # Net Percentage of Domestic Banks Reporting Stronger Demand for Credit Card Loans
    'DEMAUTO', # Net Percentage of Domestic Banks Reporting Stronger Demand for Auto Loans
    'DEMOTHCONS', # Net Percentage of Domestic Banks Reporting Stronger Demand for Consumer Loans Excluding Credit Card and Auto Loans


    # Delinquency Rate - All banks
    'DRSREACBS', # Delinquency Rate on Loans Secured by Real Estate, All Commercial Banks
    'DRSFRMACBS', # Delinquency Rate on Single-Family Residential Mortgages, Booked in Domestic Offices, All Commercial Banks
    'DRCRELEXFACBS', # Delinquency Rate on Commercial Real Estate Loans (Excluding Farmland), Booked in Domestic Offices, All Commercial Banks
    'DRFLACBS', # Delinquency Rate on Farmland Loans, Booked in Domestic Offices, All Commercial Banks

    'DRCLACBS', # Delinquency Rate on Consumer Loans, All Commercial Banks
    'DRCCLACBS', # Delinquency Rate on Credit Card Loans, All Commercial Banks
    'DROCLACBS', # Delinquency Rate on Other Consumer Loans, All Commercial Banks

    'DRLFRACBS', # Delinquency Rate on Lease Financing Receivables, All Commercial Banks
    'DRBLACBS', # Delinquency Rate on Business Loans, All Commercial Banks
    'DRFAPGACBS', # Delinquency Rate on Loans to Finance Agricultural Production, All Commercial Banks
    'DRALACBS', # Delinquency Rate on All Loans, All Commercial Banks

    # Delinquency Rate - Large banks
    'DRSRET100S', # Delinquency Rate on Loans Secured by Real Estate, Banks Ranked 1st to 100th Largest in Size by Assets
    'DRSFRMT100S', # Delinquency Rate on Single-Family Residential Mortgages, Booked in Domestic Offices, Banks Ranked 1st to 100th Largest in Size by Assets
    'DRCRELEXFT100S', # Delinquency Rate on Commercial Real Estate Loans (Excluding Farmland), Booked in Domestic Offices, Banks Ranked 1st to 100th Largest in Size by Assets
    'DRFLT100S', # Delinquency Rate on Farmland Loans, Booked in Domestic Offices, Banks Ranked 1st to 100th Largest in Size by Assets

    'DRCLT100S', # Delinquency Rate on Consumer Loans, Banks Ranked 1st to 100th Largest in Size by Assets
    'DRCCLT100S', # Delinquency Rate on Credit Card Loans, Banks Ranked 1st to 100th Largest in Size by Assets
    'DROCLT100S', # Delinquency Rate on Other Consumer Loans, Banks Ranked 1st to 100th Largest in Size by Assets

    'DRLFRT100S', # Delinquency Rate on Lease Financing Receivables, Banks Ranked 1st to 100th Largest in Size by Assets
    'DRBLT100S', # Delinquency Rate on Business Loans, Banks Ranked 1st to 100th Largest in Size by Assets
    'DRFAPGT100S', # Delinquency Rate on Loans to Finance Agricultural Production, Banks Ranked 1st to 100th Largest in Size by Assets
    'DRALT100S', # Delinquency Rate on All Loans, Banks Ranked 1st to 100th Largest in Size by Assets

    # Delinquency Rate - Small banks
    'DRSREOBS', # Delinquency Rate on Loans Secured by Real Estate, Banks Not Among the 100 Largest in Size by Assets
    'DRSFRMOBS', # Delinquency Rate on Single-Family Residential Mortgages, Booked in Domestic Offices, Banks Not Among the 100 Largest in Size by Assets
    'DRCRELEXFOBS', # Delinquency Rate on Commercial Real Estate Loans (Excluding Farmland), Booked in Domestic Offices, Banks Not Among the 100 Largest in Size by Assets
    'DRFLOBS', # Delinquency Rate on Farmland Loans, Booked in Domestic Offices, Banks Not Among the 100 Largest in Size by Assets

    'DRCLOBS', # Delinquency Rate on Consumer Loans, Banks Not Among the 100 Largest in Size by Assets
    'DRCCLOBS', # Delinquency Rate on Credit Card Loans, Banks Not Among the 100 Largest in Size by Assets
    'DROCLOBS', # Delinquency Rate on Other Consumer Loans, Banks Not Among the 100 Largest in Size by Assets

    'DRLFROBS', # Delinquency Rate on Lease Financing Receivables, Banks Not Among the 100 Largest in Size by Assets
    'DRBLOBS', # Delinquency Rate on Business Loans, Banks Not Among the 100 Largest in Size by Assets
    'DRFAPGOBS', # Delinquency Rate on Loans to Finance Agricultural Production, Banks Not Among the 100 Largest in Size by Assets
    'DRALOBS', # Delinquency Rate on All Loans, Banks Not Among the 100 Largest in Size by Assets

    'QBPLNTLNNCUR', # Loan Performance: Total Loans and Leases: Noncurrent Rate
    'BOGZ1FL072052006Q', # Interest Rates and Price Indexes; Effective Federal Funds Rate (Percent), Level

    # Banks Charge-off rates
    'CORSREACBS', # Charge-Off Rate on Loans Secured by Real Estate, All Commercial Banks
    'CORSFRMACBS', # Charge-Off Rate on Single Family Residential Mortgages, Booked in Domestic Offices, All Commercial Banks
    'CORCREXFACBS', # Charge-Off Rate on Commercial Real Estate Loans (Excluding Farmland), Booked in Domestic Offices, All Commercial Banks
    'CORFLACBS', # Charge-Off Rate on Farmland Loans, Booked in Domestic Offices, All Commercial Banks
    'CORCACBS', # Charge-Off Rate on Consumer Loans, All Commercial Banks
    'CORCCACBS', # Charge-Off Rate on Credit Card Loans, All Commercial Banks
    'COROCLACBS', # Charge-Off Rate on Other Consumer Loans, All Commercial Banks
    'CORLFRACBS', # Charge-Off Rate on Lease Financing Receivables, All Commercial Banks
    'CORBLACBS', # Charge-Off Rate on Business Loans, All Commercial Banks
    'CORLAGACBS', # Charge-Off Rate on Loans to Finance Agricultural Production, All Commercial Banks
    'CORALACBS', # Charge-Off Rate on All Loans, All Commercial Banks



    # Bank Balance Sheet (FDIC-Insured Commercial Banks and Savings Institutions)
    'QBPBSTAS', # Balance Sheet: Total Assets
    'QBPBSTASSCUSTRSC', # Balance Sheet: Total Assets: Securities: U.S. Treasury Securities
    'QBPBSLEVK', # Balance Sheet: Tier 1 Leverage Capital (PCA Definition)
    'QBPBSRSKK', # Balance Sheet: Tier 1 Risk Based Capital (PCA Definition)

    # Bank Regulation (
    # 'FL704194005', #
    'BOGZ1FL010000026Q', # Financial Soundness Indicator; Regulatory Tier 1 Capital as a Percent of Assets, Level
    'DDSI05USA156NWDB', # Bank Regulatory Capital to Risk-Weighted Assets for United States


    # CSBS
    'CBSICO', # CSBS Community Bank Sentiment Index
    'CBSIBC', # CSBS Community Bank Sentiment, Business Conditions Index

    # Financial Institutions
    'BOGZ1FL622000623A', # Hedge Funds; Total Financial and Nonfinancial Assets, Level
    'BOGZ1FL622000003Q', # Hedge Funds; Total Net Assets; Asset, Level
    'BOGZ1FL704194005Q', # Private Depository Institutions; Total Liabilities and Equity, Level
    'BOGZ1FL704190005A', # Private Depository Institutions; Total Liabilities, Level
    ''



    # Housing
    'MSPUS', # Median Sales Price of Houses Sold for the United States
    'ASPUS', # Average Sales Price of Houses Sold for the United States
    'USSTHPI', # All-Transactions House Price Index for the United States
    'RRVRUSQ156N', # Rental Vacancy Rate in the United States
    'MDSP', # Mortgage Debt Service Payments as a Percent of Disposable Personal Income

    # Debt
    'TDSP', # Household Debt Service Payments as a Percent of Disposable Personal Income
    'HDTGPDUSQ163N', # Household Debt to GDP for United States

    'USRECQ', # NBER based Recession Indicators for the United States from the Peak through the Trough

                  ]

# Monthly

ids_M = [
    # Liquidity
    'CURRCIR', # Currency in Circulation

    # C&I Loans
    'BUSLOANS', # Commercial and Industrial Loans, All Commercial Banks

    # Employment & Labor - U.S. Bureau of Labor Statistics(BLS)
    ## Current Population Survey (Household Survey)
    'CE16OV', # Employment Level
    'UNRATE', # Unemployment Rate
    'UNEMPLOY', # Unemployment Level
    'LNS13025703', # Of Total Unemployed, Percent Unemployed 27 Weeks & over

    'CIVPART', # Labor Force Participation Rate

    ## Current Employment Statisticsq (Establishment Survey)
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

    # Wage Tracker (Atlanta Fed)
    'FRBATLWGT12MMAWMHWGO', # 12-Month Moving Average of Weighted Median Hourly Wage Growth: Overall
    'FRBATLWGT12MMUMHWGWD1WP', # 12-Month Moving Average of Unweighted Median Hourly Wage Growth: Wage Distribution: 1st to 25th Wage Percentile
    'FRBATLWGT12MMUMHWGWD26WP', # 12-Month Moving Average of Unweighted Median Hourly Wage Growth: Wage Distribution: 26th to 50th Wage Percentile
    'FRBATLWGT12MMUMHWGWD51WP', # 12-Month Moving Average of Unweighted Median Hourly Wage Growth: Wage Distribution: 51st to 75th Wage Percentile
    'FRBATLWGT12MMUMHWGWD76WP', # 12-Month Moving Average of Unweighted Median Hourly Wage Growth: Wage Distribution: 76th to 100th Wage Percentile

    # Employemnt - ADP
    'ADPMNUSNERSA', #  Total Nonfarm Private Payroll Employment

    # Inflation & Consumption
    ## Retail sales (Census Bureau) - https://www.census.gov/retail/sales.html
    'RSXFS',  # Advance Retail Sales: Retail Trade
    'RSAFS',  # Advance Retail Sales: Retail Trade and Food Services
    'RSFSXMV', # Advance Retail Sales: Retail Trade and Food Services, Excluding Motor Vehicle and Parts Dealers
    'MARTSSM44W72USS', # Advance Retail Sales: Retail Trade and Food Services, Excluding Motor Vehicle and Parts Dealers and Gasoline Stations

    #--Dollar value (SA)
    'RSMVPD',  # Advance Retail Sales: Motor Vehicle and Parts Dealers
    'RSFHFS', # Advance Retail Sales: Furniture and Home Furnishings Stores
    'RSEAS', # Advance Retail Sales: Electronics and Appliance Stores
    'RSBMGESD', # Advance Retail Sales: Building Materials, Garden Equipment and Supplies Dealers
    'RSDBS', # Advance Retail Sales: Food and Beverage Stores
    'RSHPCS', # Advance Retail Sales: Health and Personal Care Stores
    'RSGASS', # Advance Retail Sales: Gasoline Stations
    'RSCCAS', # Advance Retail Sales: Clothing and Clothing Accessory Stores
    'RSSGHBMS', # Advance Retail Sales: Sporting Goods, Hobby, Musical Instrument, and Book Stores
    'RSGMS', # Advance Retail Sales: General Merchandise Stores
    'RSMSR', # Advance Retail Sales: Miscellaneous Store Retailers
    'RSNSR', # Advance Retail Sales: Nonstore Retailers
    'RSFSDP', # Advance Retail Sales: Food Services and Drinking Places

    #--MoM(SA)
    'MARTSMPCSM441USS', # Advance Retail Sales: Motor Vehicle and Parts Dealers
    'MARTSMPCSM442USS', # Advance Retail Sales: Furniture and Home Furnishings Stores
    'MARTSMPCSM443USS', # Advance Retail Sales: Electronics and Appliance Stores
    'MARTSMPCSM444USS', # Advance Retail Sales: Building Materials, Garden Equipment and Supplies Dealers
    'MARTSMPCSM445USS', # Advance Retail Sales: Food and Beverage Stores
    'MARTSMPCSM446USS', # Advance Retail Sales: Health and Personal Care Stores
    'MARTSMPCSM447USS', # Advance Retail Sales: Gasoline Stations
    'MARTSMPCSM448USS', # Advance Retail Sales: Clothing and Clothing Accessory Stores
    'MARTSMPCSM451USS', # Advance Retail Sales: Sporting Goods, Hobby, Musical Instrument, and Book Stores
    'MARTSMPCSM452USS', # Advance Retail Sales: General Merchandise Stores
    'MARTSMPCSM453USS', # Advance Retail Sales: Miscellaneous Store Retailers
    'MARTSMPCSM454USS', # Advance Retail Sales: Nonstore Retailers
    'MARTSMPCSM722USS', # Advance Retail Sales: Food Services and Drinking Places

    # 'MRTSSM44X72USS',  # Retail Sales: Retail Trade and Food Services
    # 'MRTSSM44000USS', # Retail Sales: Retail Trade
    # 'MRTSSM44X72USS', # Retail Sales: Retail Trade and Food Services
    # 'MRTSMPCSM44000USS', # Retail Sales: Retail Trade
    'TOTALSA', # Total Vehicle Sales

    ## Consumer loans
    'CCLACBM027NBOG', # Consumer Loans: Credit Cards and Other Revolving Plans, All Commercial Banks (NSA)
    'CCLACBM027SBOG', # Consumer Loans: Credit Cards and Other Revolving Plans, All Commercial Banks (SA)

    ## Consumer sentiment
    'UMCSENT', # University of Michigan: Consumer Sentiment
    'MICH', # University of Michigan: Inflation Expectation
    'CSCICP03USM665S', # Composite Leading Indicators: Composite Consumer Confidence Amplitude Adjusted for United States

    ## Inflation Expectation
    'MICH', # University of Michigan: Inflation Expectation



    ## PCE & CPI
    'PCEPI', # Personal Consumption Expenditures: Chain-type Price Index
    'PCEPILFE', # Personal Consumption Expenditures Excluding Food and Energy
    'DPCCRC1M027SBEA',  # Personal consumption expenditures excluding food and energy
    'IA001176M', # Personal Consumption Expenditures Excluding Food, Energy, and Housing (Chain-Type Price Index)
    'PCE',  # Personal Consumption Expenditures
    'PCEC96', # Real Personal Consumption Expenditures
    'PCETRIM12M159SFRBDAL',# Trimmed Mean PCE Inflation Rate
    'MEDCPIM159SFRBCLE', # Median Consumer Price Index

    'CPIAUCSL', # Consumer Price Index for All Urban Consumers: All Items in U.S. City Average (SA)
    'CPIAUCNS', # Consumer Price Index for All Urban Consumers: All Items in U.S. City Average (NSA)
    'CPILFENS', # Consumer Price Index for All Urban Consumers: All Items Less Food and Energy in U.S. City Average (NSA)
    'STICKCPIM157SFRBATL', # Sticky Price Consumer Price Index
    'CORESTICKM159SFRBATL', # Sticky Price Consumer Price Index less Food and Energy
    'CRESTKCPIXSLTRM159SFRBATL', # Sticky Price Consumer Price Index less Food, Energy, and Shelter
    'STICKCPIXSHLTRM159SFRBATL', # Sticky Price Consumer Price Index less Shelter
    'CPIUFDNS', # Consumer Price Index for All Urban Consumers: Food in U.S. City Average (NSA)
    'CPIENGNS', # Consumer Price Index for All Urban Consumers: Energy in U.S. City Average (NSA)
    'CUUR0000SACL1E', # Consumer Price Index for All Urban Consumers: Commodities Less Food and Energy Commodities in U.S. City Average (NSA)
    'CUUR0000SAH1', # Consumer Price Index for All Urban Consumers: Shelter in U.S. City Average (NSA)
    'CUUR0000SAM2', # Consumer Price Index for All Urban Consumers: Medical Care Services in U.S. City Average (NSA)
    'CUUR0000SAS4', # Consumer Price Index for All Urban Consumers: Transportation Services in U.S. City Average (NSA)

    'CUUR0000SA0R', # Consumer Price Index for All Urban Consumers: Purchasing Power of the Consumer Dollar in U.S. City Average

    'DSPI', # Disposable Personal Income
    'DSPIC96', # Real Disposable Personal Income

    ## Wage & Earnings
    'CES0500000003', # Average Hourly Earnings of All Employees, Total Private
    'DSPIC96', # Real Disposable Personal Income
    'FRBATLWGT3MMAUMHWGWD51WP', # 3-Month Moving Average of Unweighted Median Hourly Wage Growth: Wage Distribution: 51st to 100th Wage Percentile
    'FRBATLWGT3MMAUMHGWD1WP', # 3-Month Moving Average of Unweighted Median Hourly Wage Growth: Wage Distribution: 1st to 50th Wage Percentile

    'FRBATLWGT12MMUMHWGWDLHWP', # 12-Month Moving Average of Unweighted Median Hourly Wage Growth: Wage Distribution: 1st to 50th Wage Percentile
    'FRBATLWGT12MMUMHWGWDUPWP', # 12-Month Moving Average of Unweighted Median Hourly Wage Growth: Wage Distribution: 51st to 100th Wage Percentile

    'FRBATLWGT3MMAWMHWGO', # 3-Month Moving Average of Weighted Median Hourly Wage Growth: Overall
    'FRBATLWGT3MMAUMHWGO', # 3-Month Moving Average of Unweighted Median Hourly Wage Growth: Overall
    'FRBATLWGT3MMAU75PHWGO', # 3-Month Moving Average of Unweighted 75th Percentile Hourly Wage Growth: Overall
    'FRBATLWGT3MMAU25PHWGO', # 3-Month Moving Average of Unweighted 25th Percentile Hourly Wage Growth: Overall

    'FRBATLWGT12MMUMHWGWD1WP', # 12-Month Moving Average of Unweighted Median Hourly Wage Growth: Wage Distribution: 1st to 25th Wage Percentile
    'FRBATLWGT12MMUMHWGWD26WP', # 12-Month Moving Average of Unweighted Median Hourly Wage Growth: Wage Distribution: 26th to 50th Wage Percentile
    'FRBATLWGT12MMUMHWGWD51WP', # 12-Month Moving Average of Unweighted Median Hourly Wage Growth: Wage Distribution: 51st to 75th Wage Percentile
    'FRBATLWGT12MMUMHWGWD76WP', # 12-Month Moving Average of Unweighted Median Hourly Wage Growth: Wage Distribution: 76th to 100th Wage Percentile

    ## PPI
    'PPIACO', # Producer Price Index by Commodity: All Commodities (NSA)
    'PPIFID', # Producer Price Index by Commodity: Final Demand (NSA)
    'PPIFDG', # Producer Price Index by Commodity: Final Demand: Final Demand Goods (NSA)
    'PPIFDS', # Producer Price Index by Commodity: Final Demand: Final Demand Services (NSA)

    'PCUOMFGOMFG',  # Producer Price Index by Industry: Total Manufacturing Industries



    # Industrial production - https://www.federalreserve.gov/releases/g17/
    'INDPRO', # Industrial Production: Total Index

    'IPFPNSS', # Industrial Production: Final Products and Nonindustrial Supplies
        'IPCONGD', # Industrial Production: Consumer Goods
            'IPDCONGD', # Industrial Production: Durable Consumer Goods: Durable Consumer Goods
                'IPB51110S', # Industrial Production: Durable Consumer Goods: Automotive Products
                'IPB51121S', # Industrial Production: Durable Consumer Goods: Computers, Video and Audio Equipment
                'IPB51122S', # Industrial Production: Durable Consumer Goods: Appliances, Furniture, and Carpeting
                'IPB51123S', # Industrial Production: Durable Consumer Goods: Miscellaneous Durable Goods
            'IPNCONGD', # Industrial Production: Nondurable Consumer Goods
                'IPB51210S', # Industrial Production: Nondurable Nonenergy Consumer Goods
                'IPB51220S', # Industrial Production: Nondurable Energy Consumer Goods: Consumer Energy Products
        'IPBUSEQ', # Industrial Production: Equipment: Business Equipment
            'IPB52110S', # Industrial Production: Equipment: Transit Equipment
            'IPB52120S', # Industrial Production: Equipment: Information Processing and Related Equipment
            'IPB52130S', # Industrial Production: Equipment: Industrial and Other Equipment
        'IPB52300S', # Industrial Production: Equipment: Defense and Space Equipment
        'IPB54100S', # Industrial Production: Construction Supplies
        'IPB54200S', # Industrial Production: Business Supplies

    'IPMAT', # Industrial Production: Materials
        'IPZ53010S', # Industrial Production: Materials Excluding Energy Materials
        'IPB53300S', # Industrial Production: Energy Materials: Energy Materials


    # Industry Group
    'IPMANSICS', # Industrial Production: Manufacturing (SIC)
        'IPMAN', # Industrial Production: Manufacturing (NAICS)
            'IPDMAN', # Industrial Production: Durable Manufacturing (NAICS)
                'IPG321S', #  Industrial Production: Manufacturing: Durable Goods: Wood Product
                'IPG327S', # Industrial Production: Manufacturing: Durable Goods: Nonmetallic Mineral Product
                'IPG331S', # Industrial Production: Manufacturing: Durable Goods: Primary Metal
                'IPG332S', # Industrial Production: Manufacturing: Durable Goods: Fabricated Metal Product (NAICS = 332)
                'IPG333S', # Industrial Production: Manufacturing: Durable Goods: Machinery (NAICS = 333)
                'IPG334S', # Industrial Production: Manufacturing: Durable Goods: Computer and Electronic Product (NAICS = 334)
                'IPG335S', # Industrial Production: Manufacturing: Durable Goods: Electrical Equipment, Appliance, and Component (NAICS = 335)
                'IPG3361T3S', # Industrial Production: Manufacturing: Durable Goods: Motor Vehicles and Parts (NAICS = 3361-3)
                'IPG3364T9S', # Industrial Production: Manufacturing: Durable Goods: Aerospace and Miscellaneous Transportation Equipment (NAICS = 3364-9)
                'IPG337S', # Industrial Production: Manufacturing: Durable Goods: Furniture and Related Product (NAICS = 337)
                'IPG339S', # Industrial Production: Manufacturing: Durable Goods: Miscellaneous (NAICS = 339)
            'IPNMAN', # Industrial Production: Nondurable Manufacturing (NAICS)
                'IPG311A2S', # Industrial Production: Manufacturing: Nondurable Goods: Food, Beverage, and Tobacco (NAICS = 311,2)
                'IPG313A4S', # Industrial Production: Manufacturing: Nondurable Goods: Textiles and Products (NAICS = 313,4)
                'IPG315A6S', # Industrial Production: Manufacturing: Nondurable Goods: Apparel and Leather Goods (NAICS = 315,6)
                'IPG322S', # Industrial Production: Manufacturing: Nondurable Goods: Paper (NAICS = 322)
                'IPG323S', # Industrial Production: Manufacturing: Nondurable Goods: Printing and Related Support Activities (NAICS = 323)
                'IPG324S', # Industrial Production: Manufacturing: Nondurable Goods: Petroleum and Coal Products (NAICS = 324)
                'IPG325S', # Industrial Production: Manufacturing: Nondurable Goods: Chemical (NAICS = 325)
                'IPG326S', # Industrial Production: Manufacturing: Nondurable Goods: Plastics and Rubber Products (NAICS = 326)
            'IPGMFOS', # Industrial Production: Other Manufacturing
    'IPMINE', # Industrial Production: Mining: Mining (NAICS = 21)
    'IPUTIL', # Industrial Production: Utilities: Electric and Gas Utilities (NAICS = 2211,2)
        'IPG2211S', # Industrial Production: Utilities: Electric Power Generation, Transmission, and Distribution (NAICS = 2211)
        'IPG2212S', # Industrial Production: Utilities: Natural Gas Distribution (NAICS = 2212)


    # Capacity Utiliation
    'TCU', # Capacity Utilization: Total Index
    'CUMFNS', # Capacity Utilization: Manufacturing (SIC)
    'CAPUTLX4HTK2S', # Capacity Utilization: Manufacturing Excluding Computers, Communications Equipment, and Semiconductors
    'CAPUTLG334S', # Capacity Utilization: Manufacturing: Durable Goods: Computer and Electronic Product (NAICS = 334)
    'CAPUTLG21S', # Capacity Utilization: Mining: Mining (NAICS = 21)
    'CAPUTLG2211A2S', # Capacity Utilization: Utilities: Electric and Gas Utilities (NAICS = 2211,2)
    'CAPUTLB5610CS', # Capacity Utilization: Stage-of-Process: Crude Processing
    'CAPUTLB562A3CS', # Capacity Utilization: Stage-of-Process: Primary & Semifinished Processing
    'CAPUTLB5640CS', # Capacity Utilization: Stage-of-Process: Finished Processing


    # Value of Construction Put In Place (https://fred.stlouisfed.org/release/tables?rid=229&eid=22348)
    'TTLCONS', # Total Construction Spending: Total Construction in the United States
        'TLRESCONS', # Total Construction Spending: Residential in the United States
        'TLNRESCONS', # Total Construction Spending: Nonresidential in the United States
            'TLLODGCONS', # Total Construction Spending: Lodging in the United States
            'TLOFCONS', # Total Construction Spending: Office in the United States
            'TLCOMCONS', # Total Construction Spending: Commercial in the United States
            'TLHLTHCONS', # Total Construction Spending: Health Care in the United States
            'TLEDUCONS', # Total Construction Spending: Educational in the United States
            'TLRELCONS', # Total Construction Spending: Religious in the United States
            'TLPSCONS', # Total Construction Spending: Public Safety in the United States
            'TLAMUSCONS', # Total Construction Spending: Amusement and Recreation in the United States
            'TLTRANSCONS', # Total Construction Spending: Transportation in the United States
            'TLCMUCONS', # Total Construction Spending: Communication in the United States
            'TLPWRCONS', # Total Construction Spending: Power in the United States
            'TLHWYCONS', # Total Construction Spending: Highway and Street in the United States
            'TLSWDCONS', # Total Construction Spending: Sewage and Waste Disposal in the United States
            'TLWSCONS', # Total Construction Spending: Water Supply in the United States
            'TLCADCONS', # Total Construction Spending: Conservation and Development in the United States
            'TLMFGCONS', # Total Construction Spending: Manufacturing in the United States
    'TLPRVCONS', # Total Private Construction Spending: Total Construction in the United States

    'TLPBLCONS', # Total Public Construction Spending: Total Construction in the United States


    # Manufacturing - Census Bureau
    'MNFCTRIMSA', # Manufacturers Inventories
    'MNFCTRSMSA', # Manufacturers Sales
    'MNFCTRIRSA',  # Manufacturers: Inventories to Sales Ratio

    'AMTMNO', # Manufacturers' New Orders: Total Manufacturing
    'DGORDER', # Manufacturers' New Orders: Durable Goods
    'NEWORDER', # Manufacturers' New Orders: Nondefense Capital Goods Excluding Aircraft
    'ADXTNO', # Manufacturers' New Orders: Durable Goods Excluding Transportation
    'A36SNO', # Manufacturers' New Orders: Transportation Equipment
    'A33SNO', # Manufacturers' New Orders: Machinery
    'A31SNO', # Manufacturers' New Orders: Primary Metals
    'A34SNO', # Manufacturers' New Orders: Computers and Electronic Products
    'AMTMTI', # Manufacturers' Total Inventories: Total Manufacturing
    'AMTMVS', # Manufacturers' Value of Shipments: Total Manufacturing
    'AMTMIS', # Manufacturers' Inventories to Shipments Ratios: Total Manufacturing

    # Empire State Manufacturing Survey
    'GACDISA066MSFRBNY', # Current General Business Conditions; Diffusion Index for New York
    'CEFDISA066MSFRBNY', # Future Capital Expenditures; Diffusion Index for New York
    'TSFDISA066MSFRBNY', # Future Technology Spending; Diffusion Index for New York
    'NOCDISA066MSFRBNY', # Current New Orders; Diffusion Index for New York
    'PPCDISA066MSFRBNY', # Current Prices Paid; Diffusion Index for New York
    'GAFDISA066MSFRBNY', # Future General Business Conditions; Diffusion Index for New York

    #
    'DAUPSA', # Domestic Auto Production
    # Business Sentiment
    'BSCICP02USM460S', # Business Tendency Surveys (Manufacturing): Confidence Indicators: Composite Indicators: National Indicator for United States


    # Housing price
    'CSUSHPISA', # S&P CoreLogic Case-Shiller U.S. National Home Price Index
    'CSUSHPINSA',  # S&P CoreLogic Case-Shiller U.S. National Home Price Index
    'SPCS10RSA', # S&P CoreLogic Case-Shiller 10-City Composite Home Price Index
    'SPCS20RSA', # S&P CoreLogic Case-Shiller 20-City Composite Home Price Index
    'ATXRSA', #  S&P CoreLogic Case-Shiller GA-Atlanta Home Price Index
    'BOXRSA', # S&P CoreLogic Case-Shiller MA-Boston Home Price Index
    'CRXRSA', # S&P CoreLogic Case-Shiller NC-Charlotte Home Price Index
    'CHXRSA', # S&P CoreLogic Case-Shiller IL-Chicago Home Price Index
    'CEXRSA', # S&P CoreLogic Case-Shiller OH-Cleveland Home Price Index
    'DAXRSA', # S&P CoreLogic Case-Shiller TX-Dallas Home Price Index
    'DNXRSA', # S&P CoreLogic Case-Shiller CO-Denver Home Price Index
    'DEXRSA', # S&P CoreLogic Case-Shiller MI-Detroit Home Price Index
    'LVXRSA', # S&P CoreLogic Case-Shiller NV-Las Vegas Home Price Index
    'LXXRSA', # S&P CoreLogic Case-Shiller CA-Los Angeles Home Price Index
    'MIXRSA', # S&P CoreLogic Case-Shiller FL-Miami Home Price Index
    'MNXRSA', # S&P CoreLogic Case-Shiller MN-Minneapolis Home Price Index
    'NYXRSA', # S&P CoreLogic Case-Shiller NY-New York Home Price Index
    'PHXRSA', # S&P CoreLogic Case-Shiller AZ-Phoenix Home Price Index
    'POXRSA', # S&P CoreLogic Case-Shiller OR-Portland Home Price Index
    'SDXRSA', # S&P CoreLogic Case-Shiller CA-San Diego Home Price Index
    'SFXRSA', # S&P CoreLogic Case-Shiller CA-San Francisco Home Price Index
    'SEXRSA', # S&P CoreLogic Case-Shiller WA-Seattle Home Price Index
    'TPXRSA', # S&P CoreLogic Case-Shiller FL-Tampa Home Price Index
    'WDXRSA', # S&P CoreLogic Case-Shiller DC-Washington Home Price Index

    'USAUCSFRCONDOSMSAMID', # Zillow Home Value Index (ZHVI) for All Homes Including Single-Family Residences, Condos, and CO-OPs in the United States of America

    'MSPNHSUS', # Median Sales Price for New Houses Sold in the United States
    'ASPNHSUS', # Average Sales Price for New Houses Sold in the United States

    'USSTHPI', # All-Transactions House Price Index for the United States
    'EXHOSLUSM495S', # Existing Home Sales
    'EXSFHSUSM495S', # Existing Single-Family Home Sales
    'ACTLISCOUUS', # Housing Inventory: Active Listing Count in the United States
    'HOSINVUSM495N', # Existing Home Sales: Housing Inventory
    'HOSSUPUSM673N', # Existing Home Sales: Months Supply

    'HOUST', # New Privately-Owned Housing Units Started: Total Units
    'HOUST1F', # New Privately-Owned Housing Units Started: Single-Family Units

    'RSAHORUSQ156S', # Homeownership Rate in the United States

    'MSACSR',  # Monthly Supply of New Houses in the United States
    'HSN1F',  # New One Family Houses Sold: United States

    # MONTHLY NEW RESIDENTIAL CONSTRUCTION - https://www.census.gov/construction/nrc/current/index.html
    'PERMIT', # New Privately-Owned Housing Units Authorized in Permit-Issuing Places: Total Units
    'HOUST',  # New Privately-Owned Housing Units Started: Total Units
    'COMPUTSA', # New Privately-Owned Housing Units Completed: Total Units

    # Banking
    #-- all commercial banks
    'TLAACBM027SBOG', # Total Assets, All Commercial Banks
    'LOANS', # Loans and Leases in Bank Credit, All Commercial Banks
    'LNFACBM027SBOG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, All Commercial Banks

    #-- large banks : https://fred.stlouisfed.org/release/tables?rid=22&eid=823378
    'TLALCBM027SBOG', # Total Assets, Large Domestically Chartered Commercial Banks
    'BC0LCBM027SBOG', # Bank Credit, Large Domestically Chartered Commercial Banks
    'LLBLCBM027SBOG', # Loans and Leases in Bank Credit, Large Domestically Chartered Commercial Banks
    'LNFLCBM027SBOG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Large Domestically Chartered Commercial Banks
    'RELLCBM027SBOG', # Real Estate Loans, Large Domestically Chartered Commercial Banks
    'RRELCBM027SBOG', # Real Estate Loans: Residential Real Estate Loans, Large Domestically Chartered Commercial Banks
    'CRELCBM027SBOG', # Real Estate Loans: Commercial Real Estate Loans, Large Domestically Chartered Commercial Banks

    #-- small banks : https://fred.stlouisfed.org/release/tables?rid=22&eid=823674
    'TLASCBM027SBOG', # Total Assets, Small Domestically Chartered Commercial Banks
    'BC0SCBM027SBOG', # Bank Credit, Small Domestically Chartered Commercial Banks
    'LLBSCBM027SBOG', # Loans and Leases in Bank Credit, Small Domestically Chartered Commercial Banks
    'LNFSCBM027SBOG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Small Domestically Chartered Commercial Banks
    'RELSCBM027SBOG', # Real Estate Loans, Small Domestically Chartered Commercial Banks
    'RRESCBM027SBOG', # Real Estate Loans: Residential Real Estate Loans, Small Domestically Chartered Commercial Banks
    'CRESCBM027SBOG', # Real Estate Loans: Commercial Real Estate Loans, Small Domestically Chartered Commercial Banks

    #
    'EPUTRADE', # Economic Policy Uncertainty Index: Categorical Index: Trade policy
    'EPUFISCAL', # Economic Policy Uncertainty Index: Categorical Index: Fiscal Policy
    'EPUMONETARY', # Economic Policy Uncertainty Index: Categorical Index: Monetary policy


    # Leading Index
    'BSCICP03USM665S', # Composite Leading Indicators: Composite Business Confidence Amplitude Adjusted for United States

    # OECD
    'OECDLOLITOAASTSAM', # Leading Indicators OECD: Leading indicators: CLI: Amplitude adjusted for OECD - Total

    # Recession
    'USRECM', # NBER based Recession Indicators for the United States from the Peak through the Trough
    'RECPROUSM156N', # Smoothed U.S. Recession Probabilities
    'SAHMCURRENT', # Sahm Rule Recession Indicator

    # Rates & Yields
    'FEDFUNDS', # Federal Funds Effective Rate
    'AAA', # Moody's Seasoned Aaa Corporate Bond Yield
    'BAA', # Moody's Seasoned Baa Corporate Bond Yield
    'SNDR', # National Deposit Rates: Savings
]

# Weekly
ids_W_mon = [
    'CD12NRNJ', # National Rate on Non-Jumbo Deposits (less than $100,000): 12 Month CD
    'MMNRJD', # National Rate on Jumbo Deposits (greater or equal to $100,000): Money Market (DISCONTINUED)
]

ids_W_wed = [
    'TLAACBW027SBOG', # Total Assets, All Commercial Banks
    # 'BUSLOANS', # Commercial and Industrial Loans, All Commercial Banks
    'TOTCI', # Commercial and Industrial Loans, All Commercial Banks
    'TOTLL', # Loans and Leases in Bank Credit, All Commercial Banks
    'CASACBW027SBOG', # Cash Assets, All Commercial Banks
    'SBCACBW027SBOG', # Securities in Bank Credit, All Commercial Banks
    'CREACBW027SBOG', # Real Estate Loans: Commercial Real Estate Loans, All Commercial Banks
    'CCLACBW027SBOG', # Consumer Loans: Credit Cards and Other Revolving Plans, All Commercial Banks

    'DPSACBW027SBOG', # Deposits, All Commercial Banks
    'DPSSCBW027NBOG', # Deposits, Small Domestically Chartered Commercial Banks
    'DPSLCBW027SBOG', # Deposits, Large Domestically Chartered Commercial Banks
    'TOTBKCR', # Bank Credit, All Commercial Banks

    'FF', # Federal Funds Effective Rate
                  ]
ids_W_thu = [
    'MORTGAGE30US', # 30-Year Fixed Rate Mortgage Average in the United States
]

ids_W_fri = [
    'NFCI', # Chicago Fed National Financial Conditions Index
    'ANFCI', # Chicago Fed Adjusted National Financial Conditions Index
    'NFCIRISK', # Chicago Fed National Financial Conditions Risk Subindex
    'NFCICREDIT', # Chicago Fed National Financial Conditions Credit Subindex
    'NFCILEVERAGE', # Chicago Fed National Financial Conditions Leverage Subindex
    'NFCINONFINLEVERAGE', # Chicago Fed National Financial Conditions Index Nonfinancial Leveral Subindex
]

ids_W_sat = [
    # Employment
    'ICNSA', # Initial Claims

    # Employment - ADP
    'ADPWNUSNERSA', # Total Nonfarm Private Payroll Employment
]


# Daily

ids_D_every = [
    # Rate
    'DFEDTAR', # Federal Funds Target Rate (DISCONTINUED)
    'DFEDTARL', # Federal Funds Target Range - Lower Limit
    'DFEDTARU', # Federal Funds Target Range - Upper Limit
    'DFF', # Federal Funds Effective Rate

    'T5YIE', # 5-Year Breakeven Inflation Rate
    'DGS1MO', # Market Yield on U.S. Treasury Securities at 1-Month Constant Maturity, Quoted on an Investment Basis
    'RRPONTSYAWARD', # Overnight Reverse Repurchase Agreements Award Rate: Treasury Securities Sold by the Federal Reserve in the Temporary Open Market Operations

    # OAS
    'BAMLC0A0CM', # ICE BofA US Corporate Index Option-Adjusted Spread
    'BAMLH0A0HYM2', # ICE BofA US High Yield Index Option-Adjusted Spread

    'BAMLC0A4CBBB', # ICE BofA BBB US Corporate Index Option-Adjusted Spread
    'BAMLH0A3HYC', # ICE BofA CCC & Lower US High Yield Index Option-Adjusted Spread

    # Yield
    'BAMLC0A0CMEY', # ICE BofA US Corporate Index Effective Yield
    'BAMLH0A0HYM2EY', # ICE BofA US High Yield Index Effective Yield
    'BAMLH0A3HYCEY', # ICE BofA CCC & Lower US High Yield Index Effective Yield
    'DAAA', # Moody's Seasoned Aaa Corporate Bond Yield
    'DBAA', # Moody's Seasoned Baa Corporate Bond Yield

    # Recession
    'USRECDP', # NBER based Recession Indicators for the United States from the Peak through the Period preceding the Trough

    #
    'USEPUINDXD', # Economic Policy Uncertainty Index for United States
]

ids_D = [
    # Rate
    'T5YIE',  # 5-Year Breakeven Inflation Rate
    'DGS1MO',  # Market Yield on U.S. Treasury Securities at 1-Month Constant Maturity, Quoted on an Investment Basis
    'RRPONTSYAWARD', # Overnight Reverse Repurchase Agreements Award Rate: Treasury Securities Sold by the Federal Reserve in the Temporary Open Market Operations
    'DTWEXBGS', # Nominal Broad U.S. Dollar Index
    'DTWEXAFEGS', # Nominal Advanced Foreign Economies U.S. Dollar Index
    'DTWEXEMEGS', # Nominal Emerging Market Economies U.S. Dollar Index

    # OAS
    'BAMLC0A0CM',  # ICE BofA US Corporate Index Option-Adjusted Spread
    'BAMLH0A0HYM2',  # ICE BofA US High Yield Index Option-Adjusted Spread

    'BAMLC0A4CBBB',  # ICE BofA BBB US Corporate Index Option-Adjusted Spread
    'BAMLH0A3HYC',  # ICE BofA CCC & Lower US High Yield Index Option-Adjusted Spread

    # Yield
    'BAMLC0A0CMEY',  # ICE BofA US Corporate Index Effective Yield
    'BAMLH0A0HYM2EY',  # ICE BofA US High Yield Index Effective Yield
    'BAMLH0A3HYCEY',  # ICE BofA CCC & Lower US High Yield Index Effective Yield
    'DAAA',  # Moody's Seasoned Aaa Corporate Bond Yield
    'DBAA',  # Moody's Seasoned Baa Corporate Bond Yield

    # Recession
    # 'USRECDP', # NBER based Recession Indicators for the United States from the Peak through the Period preceding the Trough

]
