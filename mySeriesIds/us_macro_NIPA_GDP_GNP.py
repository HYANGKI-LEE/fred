# FRED > National Accounts > National Income & Product Accounts > GDP/GNP (category_id 106)
# https://fred.stlouisfed.org/categories/106  하위 카테고리 + 직속 시리즈 전체. 주기는 FRED 메타데이터 기준
# 위계: # 카테고리 > ## 단위 (계절조정)
# 주기 미상 제외: GDPC1CTHLR, GDPC1CTLLR, GDPC1CTMLR, GDPC1MDLR, GDPC1RHLR, GDPC1RLLR, GDPC1RMLR
dir='us_macro_NIPA_GDP_GNP'
category_ids = [106]  # build_db.py가 이 카테고리(하위 포함) 메타데이터를 일괄 조회

# Weekly (1)
ids_W = [
    # GDP/GNP (1)
    ## Index (NSA)
    'WEI', # Weekly Economic Index (Lewis-Mertens-Stock)

]

# Monthly (8)
ids_M = [
    # GDP/GNP (8)
    ## Annualized % Chg. from Preceding Period (SA)
    'BBKMCY', # Brave-Butters-Kelley Cycle Component of GDP
    'BBKMCLA', # Brave-Butters-Kelley Cycle: Lagging Subcomponent of GDP
    'BBKMCLE', # Brave-Butters-Kelley Cycle: Leading Subcomponent of GDP
    'BBKMIR', # Brave-Butters-Kelley Irregular Component of GDP
    'BBKMGDP', # Brave-Butters-Kelley Real Gross Domestic Product
    'BBKMTRD', # Brave-Butters-Kelley Trend Component of GDP
    ## Standard Deviations (SA)
    'BBKMCOIX', # Brave-Butters-Kelley Coincident Index
    'BBKMLEIX', # Brave-Butters-Kelley Leading Index

]

# Quarterly (220)
ids_Q = [
    # GDP/GNP (195)
    ## $ (SAAR)
    'A939RC0Q052SBEA', # Gross domestic product per capita
    'A791RC0Q052SBEA', # Gross national product per capita
    ## % (SA)
    'Y033RE1Q156NBEA', # Shares of Gross Domestic Product: Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment
    'Y001RE1Q156NBEA', # Shares of Gross Domestic Product: Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products
    ## % (SAAR)
    'PB0000091Q156SBEA', # Real Average of GDP and GDI (DISCONTINUED)
    'PB0000031Q156SBEA', # Real final sales to private domestic purchasers (DISCONTINUED)
    ## % Chg. at Annual Rate (SAAR)
    'GDPNOW', # GDPNow
    'FINSALESNOW', # Nowcast for Real Final Sales of Domestic Product
    'FINSALESDOMPURNOW', # Nowcast for Real Final Sales of Domestic Purchasers
    'FINSALESDOMPRIVPUR', # Nowcast for Real Final Sales of Private Domestic Purchasers
    'STLENI', # St. Louis Fed Economic News Index: Real GDP Nowcast
    ## % Chg. from Preceding Period (SAAR)
    'PA0000091Q225SBEA', # Average of GDP and GDI
    'C191RL1Q086SBEA', # Command-Basis Gross Domestic Product
    'CB22RL1Q086SBEA', # Command-Basis Gross National Product
    'A190RP1Q027SBEA', # Final Sales of Domestic Product
    'A713RP1Q027SBEA', # Final Sales to Domestic Purchasers, Current Dollars
    'PA0000031Q225SBEA', # Final sales to private domestic purchasers, current dollars
    'A191RP1Q027SBEA', # Gross Domestic Product
    'A712RP1Q027SBEA', # Gross Domestic Purchases
    'A001RP1Q027SBEA', # Gross National Product
    'PB0000091Q225SBEA', # Real Average of GDP and GDI
    'C362RL1Q156SBEA', # Real Command-basis Net Domestic Product
    'C027RL1Q156SBEA', # Real Command-basis Net National Product
    'A190RL1Q225SBEA', # Real Final Sales of Domestic Product
    'A713RL1Q225SBEA', # Real Final Sales to Domestic Purchasers
    'A191RL1Q225SBEA', # Real Gross Domestic Product
    'BB00RL1Q225SBEA', # Real Gross Domestic Product Excluding Final Sales of Computers
    'A962RL1Q225SBEA', # Real Gross Domestic Product Excluding Motor Vehicle Output
    'Y695RL1Q225SBEA', # Real Gross Domestic Product Excluding Research and Development
    'BB01RL1Q225SBEA', # Real Gross Domestic Product: Final Sales of Computers
    'A353RL1Q225SBEA', # Real Gross Domestic Product: Goods
    'A354RL1Q225SBEA', # Real Gross Domestic Product: Goods: Durable Goods
    'A326RL1Q225SBEA', # Real Gross Domestic Product: Goods: Durable Goods: Final Sales
    'A325RL1Q225SBEA', # Real Gross Domestic Product: Goods: Final Sales
    'A356RL1Q225SBEA', # Real Gross Domestic Product: Goods: Nondurable Goods
    'A334RL1Q225SBEA', # Real Gross Domestic Product: Goods: Nondurable Goods: Final Sales
    'A953RL1Q225SBEA', # Real Gross Domestic Product: Motor Vehicle Output
    'Y694RL1Q225SBEA', # Real Gross Domestic Product: Research and Development
    'A341RL1Q225SBEA', # Real Gross Domestic Product: Services
    'A755RL1Q225SBEA', # Real Gross Domestic Product: Structures
    'A712RL1Q225SBEA', # Real Gross Domestic Purchases
    'BB05RL1Q225SBEA', # Real Gross Domestic Purchases Excluding Final Sales of Computers to Domestic Purchasers
    'A023RL1Q225SBEA', # Real Gross National Income
    'A001RL1Q225SBEA', # Real Gross National Product
    'A195RL1Q225SBEA', # Real Gross Value Added: Gross Domestic Product: Business
    'B359RL1Q225SBEA', # Real Gross Value Added: Gross Domestic Product: Business: Farm
    'A358RL1Q225SBEA', # Real Gross Value Added: Gross Domestic Product: Business: Nonfarm
    'A765RL1Q225SBEA', # Real Gross Value Added: Gross Domestic Product: General Government
    'A766RL1Q225SBEA', # Real Gross Value Added: Gross Domestic Product: General Government: Federal
    'A767RL1Q225SBEA', # Real Gross Value Added: Gross Domestic Product: General Government: State and Local
    'A193RL1Q225SBEA', # Real Gross Value Added: Gross Domestic Product: Households and Institutions
    'B701RL1Q225SBEA', # Real Gross Value Added: Gross Domestic Product: Households and Institutions: Households
    'B702RL1Q225SBEA', # Real Gross Value Added: Gross Domestic Product: Households and Institutions: Nonprofit Institutions Serving Households
    'A655RL1Q225SBEA', # Real Income Payments to the Rest of the World
    'B645RL1Q225SBEA', # Real Income Receipts from the Rest of the World
    'W256RL1Q225SBEA', # Real Net Domestic Income
    'A362RL1Q225SBEA', # Real Net Domestic Product
    'W367RL1Q225SBEA', # Real Net Domestic Purchases
    'A027RL1Q225SBEA', # Real Net National Product
    'PB0000031Q225SBEA', # Real final sales to private domestic purchasers
    'PA0000111Q225SBEA', # Real gross domestic income, current dollars
    ## % Chg. from Qtr.  1 Yr. Ago (NSA)
    'OB000334Q', # Real Gross Domestic Product
    ## % Chg. from Qtr.  1 Yr. Ago (SA)
    'A190RO1Q156NBEA', # Real Final Sales of Domestic Product
    'A713RO1Q156NBEA', # Real Final Sales to Domestic Purchasers
    'A191RO1Q156NBEA', # Real Gross Domestic Product
    'A712RO1Q156NBEA', # Real Gross Domestic Purchases
    'A001RO1Q156NBEA', # Real Gross National Product
    ## % Chg. from Qtr.  1 Yr. Ago (SAAR)
    'PE0000091Q156NBEA', # Real Average of GDP and GDI
    'PE0000031Q156NBEA', # Real Final sales to private domestic purchasers
    ## Annualized % Chg. from Preceding Period (SA)
    'BBKQCY', # Brave-Butters-Kelley Cycle Component of GDP
    'BBKQCLA', # Brave-Butters-Kelley Cycle: Lagging Subcomponent of GDP
    'BBKQCLE', # Brave-Butters-Kelley Cycle: Leading Subcomponent of GDP
    'BBKQIR', # Brave-Butters-Kelley Irregular Component of GDP
    'BBKQGDP', # Brave-Butters-Kelley Real Gross Domestic Product
    'BBKQTRD', # Brave-Butters-Kelley Trend Component of GDP
    ## Bil. of $ (NSA)
    'NGDPPOT', # Nominal Potential Gross Domestic Product
    ## Bil. of $ (SAAR)
    'LA0000091Q027SBEA', # Average of GDP and GDI
    'CBI', # Change in Private Inventories
    'FINSAL', # Final Sales of Domestic Product
    'FSDP', # Final Sales to Domestic Purchasers
    'LA0000031Q027SBEA', # Final Sales to Private Domestic Purchasers
    'GDP', # Gross Domestic Product
    'Y695RC1Q027SBEA', # Gross Domestic Product Excluding Research and Development
    'Y694RC1Q027SBEA', # Gross Domestic Product: Research and Development
    'GDB', # Gross Domestic Purchases
    'GNP', # Gross National Product
    'W260RC1Q027SBEA', # Gross domestic income: Net operating surplus: Private enterprises
    'W272RC1Q027SBEA', # Gross domestic income: Net operating surplus: Private enterprises: Net interest and miscellaneous payments, domestic industries
    'BB00RC1Q027SBEA', # Gross domestic product excluding final sales of computers
    'A962RC1Q027SBEA', # Gross domestic product excluding motor vehicle output
    'A354RC1Q027SBEA', # Gross domestic product: Durable goods
    'A326RC1Q027SBEA', # Gross domestic product: Durable goods: Final sales
    'BB01RC1Q027SBEA', # Gross domestic product: Final sales of computers
    'A353RC1Q027SBEA', # Gross domestic product: Goods
    'A325RC1Q027SBEA', # Gross domestic product: Goods: Final sales
    'A356RC1Q027SBEA', # Gross domestic product: Nondurable goods
    'A334RC1Q027SBEA', # Gross domestic product: Nondurable goods: Final sales
    'A341RC1Q027SBEA', # Gross domestic product: Services
    'A755RC1Q027SBEA', # Gross domestic product: Structures
    'X023RC1Q027SBEA', # Gross national factor income
    'A023RC1Q027SBEA', # Gross national income
    'A195RC1Q027SBEA', # Gross value added: GDP: Business
    'A422RC1Q027SBEA', # National income without capital consumption adjustment
    'J422RC1Q027SBEA', # National income without capital consumption adjustment (DISCONTINUED)
    'W256RC1Q027SBEA', # Net domestic income
    'A362RC1Q027SBEA', # Net domestic product
    'W367RC1Q027SBEA', # Net domestic purchases
    'X032RC1Q027SBEA', # Net national factor income
    'A027RC1Q027SBEA', # Net national product
    'B470RC1Q027SBEA', # Nonfinancial corporate business: Capital consumption adjustment
    'A464RC1Q027SBEA', # Nonfinancial corporate business: Profits before tax (without IVA and CCAdj)
    ## Bil. of 2017 US $ (SAAR)
    'LB0000031Q020SBEA', # Real Final Sales to Private Domestic Purchasers
    ## Bil. of Chn. 2009 $ (SAAR)
    'CBIC96', # Change in Real Private Inventories (DISCONTINUED)
    'FINSLC96', # Real Final Sales of Domestic Product (DISCONTINUED)
    'GDPC96', # Real Gross Domestic Product (DISCONTINUED)
    ## Bil. of Chn. 2017 $ (NSA)
    'ND000334Q', # Real Gross Domestic Product
    'ND000364Q', # Real Gross Domestic Product: Residual
    'GDPPOT', # Real Potential Gross Domestic Product
    ## Bil. of Chn. 2017 $ (SAAR)
    'CBIC1', # Change in Real Private Inventories
    'C191RX1Q020SBEA', # Command-basis real gross domestic product
    'CB22RX1Q020SBEA', # Command-basis real gross national product
    'C362RX1Q020SBEA', # Command-basis real net domestic product
    'C027RX1Q020SBEA', # Command-basis real net national product
    'LB0000091Q020SBEA', # Real Average of GDP and GDI
    'FINSLC1', # Real Final Sales of Domestic Product
    'GDPC1', # Real Gross Domestic Product
    'Y695RX1Q020SBEA', # Real Gross Domestic Product Excluding Research and Development
    'Y694RX1Q020SBEA', # Real Gross Domestic Product: Research and Development
    'GNPC96', # Real Gross National Product
    'A713RX1Q020SBEA', # Real final sales to domestic purchasers
    'A261RX1Q020SBEA', # Real gross domestic income
    'BB00RX1Q020SBEA', # Real gross domestic product excluding final sales of computers
    'A962RX1Q020SBEA', # Real gross domestic product excluding motor vehicle output
    'A354RX1Q020SBEA', # Real gross domestic product: Durable goods
    'A326RX1Q020SBEA', # Real gross domestic product: Durable goods: Final sales
    'BB01RX1Q020SBEA', # Real gross domestic product: Final sales of computers
    'A353RX1Q020SBEA', # Real gross domestic product: Goods
    'A325RX1Q020SBEA', # Real gross domestic product: Goods: Final sales
    'A655RX1Q020SBEA', # Real gross domestic product: Income payments to the rest of the world
    'A645RX1Q020SBEA', # Real gross domestic product: Income receipts from the rest of the world
    'A356RX1Q020SBEA', # Real gross domestic product: Nondurable goods
    'A334RX1Q020SBEA', # Real gross domestic product: Nondurable goods: Final sales
    'A958RX1Q020SBEA', # Real gross domestic product: Residual
    'A959RX1Q020SBEA', # Real gross domestic product: Residual
    'A960RX1Q020SBEA', # Real gross domestic product: Residual
    'AR05RX1Q020SBEA', # Real gross domestic product: Residual
    'A341RX1Q020SBEA', # Real gross domestic product: Services
    'A755RX1Q020SBEA', # Real gross domestic product: Structures
    'A712RX1Q020SBEA', # Real gross domestic purchases
    'A023RX1Q020SBEA', # Real gross national income
    'A961RX1Q020SBEA', # Real gross value added: GDP: Residual
    'A027RX1Q020SBEA', # Real net national product
    ## Chn. 2017 $ (SAAR)
    'A939RX0Q048SBEA', # Real gross domestic product per capita
    'A791RX0Q048SBEA', # Real gross national product per capita
    ## Index (SA)
    'W369RG3Q066SBEA', # Gross domestic product: Terms of trade index
    'W370RG3Q020SBEA', # Gross domestic product: Terms of trade index: Terms of trade, goods
    'W371RG3Q020SBEA', # Gross domestic product: Terms of trade index: Terms of trade, nonpetroleum goods
    'W368RG3Q066SBEA', # Gross domestic product: Trading gains index
    ## Index 2017=100 (NSA)
    'NC000334Q', # Gross Domestic Product
    'NB000334Q', # Real Gross Domestic Product
    ## Index 2017=100 (SA)
    'W367RG3Q086SBEA', # Net domestic purchases
    ## Mil. of $ (NSA)
    'NA000373Q', # Change in private inventories
    'NA000334Q', # Gross Domestic Product
    'NA000262Q', # Gross domestic income: Net operating surplus: Private enterprises
    'NA000256Q', # Gross domestic income: Net operating surplus: Private enterprises: Net interest and miscellaneous payments, domestic industries
    ## Mil. of Chn. 2009 $ (SAAR)
    'GDPMC1', # Real Gross Domestic Product (DISCONTINUED)
    ## Percentage Points (SA)
    'FINSALESCONTRIBNOW', # Contributions to percent change in GDPNow: Real Final Sales of Domestic Product
    ## Percentage Points at Annual Rate (SAAR)
    'Y695RY2Q224SBEA', # Contributions to Percent Change in Real Gross Domestic Product: Gross Domestic Product Excluding Research and Development
    'Y033RY2Q224SBEA', # Contributions to Percent Change in Real Gross Domestic Product: Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment
    'Y034RY2Q224SBEA', # Contributions to Percent Change in Real Gross Domestic Product: Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment: Information Processing Equipment
    'Y001RY2Q224SBEA', # Contributions to Percent Change in Real Gross Domestic Product: Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products
    'Y020RY2Q224SBEA', # Contributions to Percent Change in Real Gross Domestic Product: Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products: Entertainment, Literary, and Artistic Originals
    'Y006RY2Q224SBEA', # Contributions to Percent Change in Real Gross Domestic Product: Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products: Research and Development
    'Y694RY2Q224SBEA', # Contributions to Percent Change in Real Gross Domestic Product: Research and Development
    'B982RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Energy goods and services
    'W489RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Final sales of computers to domestic purchasers
    'B981RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Food
    'BB05RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Gross domestic purchases excluding final sales of computers to domestic purchasers
    'B983RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Gross domestic purchases excluding food and energy
    'A354RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Durable goods
    'A326RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Durable goods: Final sales
    'BB01RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Final sales of computers
    'A190RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Final sales of domestic product
    'A353RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Goods
    'A325RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Goods: Final sales
    'BB00RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Gross domestic product excluding final sales of computers
    'A962RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Gross domestic product excluding motor vehicle output
    'A953RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Motor vehicle output
    'A356RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Nondurable goods
    'A334RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Nondurable goods: Final sales
    'A341RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Services
    'A755RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Structures
    ## Percentage of GDP (SAAR)
    'SB0000081Q027SBEA', # Gross domestic product : Statistical discrepancy as a percentage of GDP
    ## Standard Deviations (SA)
    'BBKQCOIX', # Brave-Butters-Kelley Coincident Index
    'BBKQLEIX', # Brave-Butters-Kelley Leading Index

    # GDP/GNP > Shares of GDP (25)
    ## % (NSA)
    'A191RE1Q156NBEA', # Shares of gross domestic product
    'A253RE1Q156NBEA', # Shares of gross domestic product: Exports of goods
    'B020RE1Q156NBEA', # Shares of gross domestic product: Exports of goods and services
    'A646RE1Q156NBEA', # Shares of gross domestic product: Exports of services
    'A822RE1Q156NBEA', # Shares of gross domestic product: Government consumption expenditures and gross investment
    'A823RE1Q156NBEA', # Shares of gross domestic product: Government consumption expenditures and gross investment: Federal
    'A824RE1Q156NBEA', # Shares of gross domestic product: Government consumption expenditures and gross investment: Federal: National defense
    'A825RE1Q156NBEA', # Shares of gross domestic product: Government consumption expenditures and gross investment: Federal: Nondefense
    'A829RE1Q156NBEA', # Shares of gross domestic product: Government consumption expenditures and gross investment: State and local
    'A006RE1Q156NBEA', # Shares of gross domestic product: Gross private domestic investment
    'A014RE1Q156NBEA', # Shares of gross domestic product: Gross private domestic investment: Change in private inventories
    'A007RE1Q156NBEA', # Shares of gross domestic product: Gross private domestic investment: Fixed investment
    'A008RE1Q156NBEA', # Shares of gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential
    'B010RE1Q156NBEA', # Shares of gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Equipment and software (DISCONTINUED)
    'B009RE1Q156NBEA', # Shares of gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Structures
    'A011RE1Q156NBEA', # Shares of gross domestic product: Gross private domestic investment: Fixed investment: Residential
    'A255RE1Q156NBEA', # Shares of gross domestic product: Imports of goods
    'B021RE1Q156NBEA', # Shares of gross domestic product: Imports of goods and services
    'B656RE1Q156NBEA', # Shares of gross domestic product: Imports of services
    'A019RE1Q156NBEA', # Shares of gross domestic product: Net exports of goods and services
    'DPCERE1Q156NBEA', # Shares of gross domestic product: Personal consumption expenditures
    'DDURRE1Q156NBEA', # Shares of gross domestic product: Personal consumption expenditures: Durable goods
    'DGDSRE1Q156NBEA', # Shares of gross domestic product: Personal consumption expenditures: Goods
    'DNDGRE1Q156NBEA', # Shares of gross domestic product: Personal consumption expenditures: Nondurable goods
    'DSERRE1Q156NBEA', # Shares of gross domestic product: Personal consumption expenditures: Services

]

# Annually (216)
ids_Y = [
    # GDP/GNP (166)
    ## $ (NSA)
    'A939RC0A052NBEA', # Gross domestic product per capita
    'A791RC0A052NBEA', # Gross national product per capita
    ## % (NSA)
    'Y033RE1A156NBEA', # Shares of Gross Domestic Product: Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment
    'Y001RE1A156NBEA', # Shares of Gross Domestic Product: Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products
    ## % Chg. From Preceding Period (NSA)
    'PB0000091A156NBEA', # Real average of GDP and GDI (DISCONTINUED)
    'PB0000031A156NBEA', # Real final sales to private domestic purchasers (DISCONTINUED)
    ## % Chg. from Preceding Period (NSA)
    'PA0000091A225NBEA', # Average of GDP and GDI, current dollars
    'C191RL1A086NBEA', # Command-Basis Gross Domestic Product
    'CB22RL1A086NBEA', # Command-Basis Gross National Product
    'A190RP1A027NBEA', # Final Sales of Domestic Product
    'A713RP1A027NBEA', # Final Sales to Domestic Purchasers, Current Dollars
    'PA0000031A225NBEA', # Final sales to private domestic purchasers, current dollars
    'A191RP1A027NBEA', # Gross Domestic Product
    'A712RP1A027NBEA', # Gross Domestic Purchases
    'A001RP1A027NBEA', # Gross National Product
    'PA0000111A225NBEA', # Gross domestic income, current dollars
    'C362RL1A156NBEA', # Real Command-basis Net Domestic Product
    'C027RL1A156NBEA', # Real Command-basis Net National Product
    'A190RL1A225NBEA', # Real Final Sales of Domestic Product
    'A713RL1A225NBEA', # Real Final Sales to Domestic Purchasers
    'A191RL1A225NBEA', # Real Gross Domestic Product
    'BB00RL1A225NBEA', # Real Gross Domestic Product Excluding Final Sales of Computers
    'A962RL1A225NBEA', # Real Gross Domestic Product Excluding Motor Vehicle Output
    'Y695RL1A225NBEA', # Real Gross Domestic Product Excluding Research and Development
    'BB01RL1A225NBEA', # Real Gross Domestic Product: Final Sales of Computers
    'A353RL1A225NBEA', # Real Gross Domestic Product: Goods
    'A354RL1A225NBEA', # Real Gross Domestic Product: Goods: Durable Goods
    'A326RL1A225NBEA', # Real Gross Domestic Product: Goods: Durable Goods: Final Sales
    'A325RL1A225NBEA', # Real Gross Domestic Product: Goods: Final Sales
    'A356RL1A225NBEA', # Real Gross Domestic Product: Goods: Nondurable Goods
    'A334RL1A225NBEA', # Real Gross Domestic Product: Goods: Nondurable Goods: Final Sales
    'A953RL1A225NBEA', # Real Gross Domestic Product: Motor Vehicle Output
    'Y694RL1A225NBEA', # Real Gross Domestic Product: Research and Development
    'A341RL1A225NBEA', # Real Gross Domestic Product: Services
    'A755RL1A225NBEA', # Real Gross Domestic Product: Structures
    'A712RL1A225NBEA', # Real Gross Domestic Purchases
    'BB05RL1A225NBEA', # Real Gross Domestic Purchases Excluding Final Sales of Computers to Domestic Purchasers
    'A023RL1A225NBEA', # Real Gross National Income
    'A001RL1A225NBEA', # Real Gross National Product
    'A195RL1A225NBEA', # Real Gross Value Added: Gross Domestic Product: Business
    'B359RL1A225NBEA', # Real Gross Value Added: Gross Domestic Product: Business: Farm
    'A358RL1A225NBEA', # Real Gross Value Added: Gross Domestic Product: Business: Nonfarm
    'A765RL1A225NBEA', # Real Gross Value Added: Gross Domestic Product: General Government
    'A766RL1A225NBEA', # Real Gross Value Added: Gross Domestic Product: General Government: Federal
    'A767RL1A225NBEA', # Real Gross Value Added: Gross Domestic Product: General Government: State and Local
    'A193RL1A225NBEA', # Real Gross Value Added: Gross Domestic Product: Households and Institutions
    'B701RL1A225NBEA', # Real Gross Value Added: Gross Domestic Product: Households and Institutions: Households
    'B702RL1A225NBEA', # Real Gross Value Added: Gross Domestic Product: Households and Institutions: Nonprofit Institutions Serving Households
    'A655RL1A225NBEA', # Real Income Payments to the Rest of the World
    'B645RL1A225NBEA', # Real Income Receipts from the Rest of the World
    'W256RL1A225NBEA', # Real Net Domestic Income
    'A362RL1A225NBEA', # Real Net Domestic Product
    'W367RL1A225NBEA', # Real Net Domestic Purchases
    'A027RL1A225NBEA', # Real Net National Product
    'PB0000091A225NBEA', # Real average of GDP and GDI
    'PB0000031A225NBEA', # Real final sales to private domestic purchasers
    ## Bil. of $ (NSA)
    'LA0000091A027NBEA', # Average of GDP and GDI
    'CBIA', # Change in Private Inventories
    'A713RC1A027NBEA', # Final sales to domestic purchasers
    'LA0000031A027NBEA', # Final sales to private domestic purchasers
    'GDPA', # Gross Domestic Product
    'Y695RC1A027NBEA', # Gross Domestic Product Excluding Research and Development
    'Y694RC1A027NBEA', # Gross Domestic Product: Research and Development
    'GNPA', # Gross National Product
    'W272RC1A027NBEA', # Gross domestic income: Net interest and miscellaneous payments
    'W260RC1A027NBEA', # Gross domestic income: Net operating surplus: Private enterprises
    'BB00RC1A027NBEA', # Gross domestic product excluding final sales of computers
    'A962RC1A027NBEA', # Gross domestic product excluding motor vehicle output
    'A354RC1A027NBEA', # Gross domestic product: Durable goods
    'A326RC1A027NBEA', # Gross domestic product: Durable goods: Final sales
    'BB01RC1A027NBEA', # Gross domestic product: Final sales of computers
    'A190RC1A027NBEA', # Gross domestic product: Final sales of domestic product
    'A353RC1A027NBEA', # Gross domestic product: Goods
    'A325RC1A027NBEA', # Gross domestic product: Goods: Final sales
    'A356RC1A027NBEA', # Gross domestic product: Nondurable goods
    'A334RC1A027NBEA', # Gross domestic product: Nondurable goods: Final sales
    'A341RC1A027NBEA', # Gross domestic product: Services
    'A755RC1A027NBEA', # Gross domestic product: Structures
    'A712RC1A027NBEA', # Gross domestic purchases
    'X023RC1A027NBEA', # Gross national factor income
    'A023RC1A027NBEA', # Gross national income
    'A195RC1A027NBEA', # Gross value added: GDP: Business
    'A032RC1A027NBEA', # National income
    'A422RC1A027NBEA', # National income without capital consumption adjustment
    'J422RC1A027NBEA', # National income without capital consumption adjustment (DISCONTINUED)
    'A368RC1A027NBEA', # National income: Domestic business
    'W256RC1A027NBEA', # Net domestic income
    'A362RC1A027NBEA', # Net domestic product
    'W367RC1A027NBEA', # Net domestic purchases
    'X032RC1A027NBEA', # Net national factor income
    'A027RC1A027NBEA', # Net national product
    'B470RC1A027NBEA', # Nonfinancial corporate business: Capital consumption adjustment
    'A466RC1A027NBEA', # Nonfinancial corporate business: Profits after tax (without IVA and CCAdj)
    'A464RC1A027NBEA', # Nonfinancial corporate business: Profits before tax (without IVA and CCAdj)
    ## Bil. of Chn. 2017 $ (NSA)
    'C191RX1A020NBEA', # Command-basis real gross domestic product
    'CB22RX1A020NBEA', # Command-basis real gross national product
    'C362RX1A020NBEA', # Command-basis real net domestic product
    'C027RX1A020NBEA', # Command-basis real net national product
    'CBICA', # Real Change in Private Inventories
    'FINSLCA', # Real Final Sales of Domestic Product
    'GDPCA', # Real Gross Domestic Product
    'Y695RX1A020NBEA', # Real Gross Domestic Product Excluding Research and Development
    'Y694RX1A020NBEA', # Real Gross Domestic Product: Research and Development
    'GNPCA', # Real Gross National Product
    'LB0000091A020NBEA', # Real average of GDP and GDI
    'LB0000031A020NBEA', # Real final expenditures by U.S. residents: Final sales to private domestic purchasers
    'A713RX1A020NBEA', # Real final sales to domestic purchasers
    'A261RX1A020NBEA', # Real gross domestic income
    'BB00RX1A020NBEA', # Real gross domestic product excluding final sales of computers
    'A962RX1A020NBEA', # Real gross domestic product excluding motor vehicle output
    'A354RX1A020NBEA', # Real gross domestic product: Durable goods
    'A326RX1A020NBEA', # Real gross domestic product: Durable goods: Final sales
    'BB01RX1A020NBEA', # Real gross domestic product: Final sales of computers
    'A353RX1A020NBEA', # Real gross domestic product: Goods
    'A325RX1A020NBEA', # Real gross domestic product: Goods: Final sales
    'A655RX1A020NBEA', # Real gross domestic product: Income payments to the rest of the world
    'A645RX1A020NBEA', # Real gross domestic product: Income receipts from the rest of the world
    'A356RX1A020NBEA', # Real gross domestic product: Nondurable goods
    'A334RX1A020NBEA', # Real gross domestic product: Nondurable goods: Final sales
    'A958RX1A020NBEA', # Real gross domestic product: Residual
    'A959RX1A020NBEA', # Real gross domestic product: Residual
    'A960RX1A020NBEA', # Real gross domestic product: Residual
    'AR05RX1A020NBEA', # Real gross domestic product: Residual
    'A341RX1A020NBEA', # Real gross domestic product: Services
    'A755RX1A020NBEA', # Real gross domestic product: Structures
    'A712RX1A020NBEA', # Real gross domestic purchases
    'A023RX1A020NBEA', # Real gross national income
    'A961RX1A020NBEA', # Real gross value added: GDP: Residual
    'A027RX1A020NBEA', # Real net national product
    ## Fourth Qtr. to Fourth Qtr. % Chg. (NSA)
    'GDPC1CTH', # FOMC Summary of Economic Projections for the Growth Rate of Real Gross Domestic Product, Central Tendency, High
    'GDPC1CTL', # FOMC Summary of Economic Projections for the Growth Rate of Real Gross Domestic Product, Central Tendency, Low
    'GDPC1CTM', # FOMC Summary of Economic Projections for the Growth Rate of Real Gross Domestic Product, Central Tendency, Midpoint
    'GDPC1MD', # FOMC Summary of Economic Projections for the Growth Rate of Real Gross Domestic Product, Median
    'GDPC1RH', # FOMC Summary of Economic Projections for the Growth Rate of Real Gross Domestic Product, Range, High
    'GDPC1RL', # FOMC Summary of Economic Projections for the Growth Rate of Real Gross Domestic Product, Range, Low
    'GDPC1RM', # FOMC Summary of Economic Projections for the Growth Rate of Real Gross Domestic Product, Range, Midpoint
    ## Index 2017=100 (NSA)
    'W367RG3A086NBEA', # Net domestic purchases
    ## Mil. of $ (NSA)
    'USNGSP', # Gross Domestic Product: All Industry Total in the United States
    ## Mil. of Chn. 2009 $ (NSA)
    'GDPMCA1', # Real Gross Domestic Product (DISCONTINUED)
    ## Mil. of Chn. 2017 $ (NSA)
    'USRGSP', # Real Gross Domestic Product: All Industry Total in the United States
    ## Percentage Points at Annual Rate (NSA)
    'Y695RY2A224NBEA', # Contributions to Percent Change in Real Gross Domestic Product: Gross Domestic Product Excluding Research and Development
    'Y033RY2A224NBEA', # Contributions to Percent Change in Real Gross Domestic Product: Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment
    'Y034RY2A224NBEA', # Contributions to Percent Change in Real Gross Domestic Product: Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment: Information Processing Equipment
    'Y001RY2A224NBEA', # Contributions to Percent Change in Real Gross Domestic Product: Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products
    'Y020RY2A224NBEA', # Contributions to Percent Change in Real Gross Domestic Product: Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products: Entertainment, Literary, and Artistic Originals
    'Y006RY2A224NBEA', # Contributions to Percent Change in Real Gross Domestic Product: Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products: Research and Development
    'Y694RY2A224NBEA', # Contributions to Percent Change in Real Gross Domestic Product: Research and Development
    'B982RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Energy goods and services
    'W489RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Final sales of computers to domestic purchasers
    'B981RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Food
    'BB05RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Gross domestic purchases excluding final sales of computers to domestic purchasers
    'B983RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Gross domestic purchases excluding food and energy
    'A354RY2A224NBEA', # Contributions to percent change in real gross domestic product: Durable goods
    'A326RY2A224NBEA', # Contributions to percent change in real gross domestic product: Durable goods: Final sales
    'BB01RY2A224NBEA', # Contributions to percent change in real gross domestic product: Final sales of computers
    'A190RY2A224NBEA', # Contributions to percent change in real gross domestic product: Final sales of domestic product
    'A353RY2A224NBEA', # Contributions to percent change in real gross domestic product: Goods
    'A325RY2A224NBEA', # Contributions to percent change in real gross domestic product: Goods: Final sales
    'BB00RY2A224NBEA', # Contributions to percent change in real gross domestic product: Gross domestic product excluding final sales of computers
    'A962RY2A224NBEA', # Contributions to percent change in real gross domestic product: Gross domestic product excluding motor vehicle output
    'A953RY2A224NBEA', # Contributions to percent change in real gross domestic product: Motor vehicle output
    'A356RY2A224NBEA', # Contributions to percent change in real gross domestic product: Nondurable goods
    'A334RY2A224NBEA', # Contributions to percent change in real gross domestic product: Nondurable goods: Final sales
    'A341RY2A224NBEA', # Contributions to percent change in real gross domestic product: Services
    'A755RY2A224NBEA', # Contributions to percent change in real gross domestic product: Structures
    ## Percentage of GDP (NSA)
    'SB0000081A027NBEA', # Statistical discrepancy as a percentage of GDP

    # GDP/GNP > Shares of GDP (50)
    ## % (NSA)
    'A261RE1A156NBEA', # Shares of gross domestic income
    'A4002E1A156NBEA', # Shares of gross domestic income: Compensation of employees, paid
    'A038RE1A156NBEA', # Shares of gross domestic income: Compensation of employees, paid: Supplements to wages and salaries
    'A4102E1A156NBEA', # Shares of gross domestic income: Compensation of employees, paid: Wage and salary accruals
    'W269RE1A156NBEA', # Shares of gross domestic income: Compensation of employees, paid: Wage and salary accruals: Disbursements (DISCONTINUED)
    'W270RE1A156NBEA', # Shares of gross domestic income: Compensation of employees, paid: Wage and salary accruals: Disbursements: to persons
    'B4189E1A156NBEA', # Shares of gross domestic income: Compensation of employees, paid: Wage and salary accruals: Disbursements: to the rest of the world
    'A062RE1A156NBEA', # Shares of gross domestic income: Compensation of employees, paid: Wage and salary accruals: Wage accruals less disbursements (DISCONTINUED)
    'A262RE1A156NBEA', # Shares of gross domestic income: Consumption of fixed capital
    'A264RE1A156NBEA', # Shares of gross domestic income: Consumption of fixed capital: Government
    'A024RE1A156NBEA', # Shares of gross domestic income: Consumption of fixed capital: Private
    'A445RE1A156NBEA', # Shares of gross domestic income: Corporate profits with inventory valuation and capital consumption adjustments, domestic industries
    'W273RE1A156NBEA', # Shares of gross domestic income: Corporate profits with inventory valuation and capital consumption adjustments, domestic industries: Profits after tax with inventory valuation and capital consumption adjustments
    'A449RE1A156NBEA', # Shares of gross domestic income: Corporate profits with inventory valuation and capital consumption adjustments, domestic industries: Profits after tax with inventory valuation and capital consumption adjustments: Net dividends
    'A054RE1A156NBEA', # Shares of gross domestic income: Corporate profits with inventory valuation and capital consumption adjustments, domestic industries: Taxes on corporate income
    'A108RE1A156NBEA', # Shares of gross domestic income: Current surplus of government enterprises
    'W271RE1A156NBEA', # Shares of gross domestic income: Net operating surplus
    'W260RE1A156NBEA', # Shares of gross domestic income: Net operating surplus: Private enterprises
    'B029RE1A156NBEA', # Shares of gross domestic income: Net operating surplus: Private enterprises: Business current transfer payments (net)
    'W272RE1A156NBEA', # Shares of gross domestic income: Net operating surplus: Private enterprises: Net interest and miscellaneous payments, domestic industries
    'A041RE1A156NBEA', # Shares of gross domestic income: Net operating surplus: Private enterprises: Proprietors' income with inventory valuation and capital consumption adjustments
    'A048RE1A156NBEA', # Shares of gross domestic income: Net operating surplus: Private enterprises: Rental income of persons with capital consumption adjustment
    'W274RE1A156NBEA', # Shares of gross domestic income: Profits after tax with inventory valuation and capital consumption adjustments: Undistributed corporate profits with inventory valuation and capital consumption adjustments
    'A107RE1A156NBEA', # Shares of gross domestic income: Subsidies
    'W056RE1A156NBEA', # Shares of gross domestic income: Taxes on production and imports
    'A191RE1A156NBEA', # Shares of gross domestic product
    'A253RE1A156NBEA', # Shares of gross domestic product: Exports of goods
    'B020RE1A156NBEA', # Shares of gross domestic product: Exports of goods and services
    'A646RE1A156NBEA', # Shares of gross domestic product: Exports of services
    'A822RE1A156NBEA', # Shares of gross domestic product: Government consumption expenditures and gross investment
    'A823RE1A156NBEA', # Shares of gross domestic product: Government consumption expenditures and gross investment: Federal
    'A824RE1A156NBEA', # Shares of gross domestic product: Government consumption expenditures and gross investment: Federal: National defense
    'A825RE1A156NBEA', # Shares of gross domestic product: Government consumption expenditures and gross investment: Federal: Nondefense
    'A829RE1A156NBEA', # Shares of gross domestic product: Government consumption expenditures and gross investment: State and local
    'A006RE1A156NBEA', # Shares of gross domestic product: Gross private domestic investment
    'A014RE1A156NBEA', # Shares of gross domestic product: Gross private domestic investment: Change in private inventories
    'A007RE1A156NBEA', # Shares of gross domestic product: Gross private domestic investment: Fixed investment
    'A008RE1A156NBEA', # Shares of gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential
    'B010RE1A156NBEA', # Shares of gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Equipment and software (DISCONTINUED)
    'B009RE1A156NBEA', # Shares of gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Structures
    'A011RE1A156NBEA', # Shares of gross domestic product: Gross private domestic investment: Fixed investment: Residential
    'A255RE1A156NBEA', # Shares of gross domestic product: Imports of goods
    'B021RE1A156NBEA', # Shares of gross domestic product: Imports of goods and services
    'B656RE1A156NBEA', # Shares of gross domestic product: Imports of services
    'A019RE1A156NBEA', # Shares of gross domestic product: Net exports of goods and services
    'DPCERE1A156NBEA', # Shares of gross domestic product: Personal consumption expenditures
    'DDURRE1A156NBEA', # Shares of gross domestic product: Personal consumption expenditures: Durable goods
    'DGDSRE1A156NBEA', # Shares of gross domestic product: Personal consumption expenditures: Goods
    'DNDGRE1A156NBEA', # Shares of gross domestic product: Personal consumption expenditures: Nondurable goods
    'DSERRE1A156NBEA', # Shares of gross domestic product: Personal consumption expenditures: Services

]
