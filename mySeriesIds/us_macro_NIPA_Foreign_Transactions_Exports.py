# FRED > National Accounts > National Income & Product Accounts > Foreign Transactions > Exports (category_id 33018)
# https://fred.stlouisfed.org/categories/33018  하위 카테고리 + 직속 시리즈 전체. 주기는 FRED 메타데이터 기준
# 위계: # 카테고리 > ## 단위 (계절조정)
dir='us_macro_NIPA_Foreign_Transactions_Exports'
category_ids = [33018]  # build_db.py가 이 카테고리(하위 포함) 메타데이터를 일괄 조회

# Quarterly (172)
ids_Q = [
    # Exports (172)
    ## % Chg. at Annual Rate (SAAR)
    'EXPORTSGOODSNOW', # Nowcast for Real Exports of Goods
    'EXPORTSNOW', # Nowcast for Real Exports of Goods and Services
    'EXPORTSSERVICESNOW', # Nowcast for Real Exports of Services
    ## % Chg. from Preceding Period (SAAR)
    'PB0000051Q225SBEA', # Exports of goods: Industrial supplies and materials: Nondurable goods: Nondurable goods, excluding petroleum and products
    'PB0000061Q225SBEA', # Exports of goods: Industrial supplies and materials: Nondurable goods: Petroleum and products
    'B181RL1Q225SBEA', # Real Exports of Agricultural Goods
    'A332RL1Q225SBEA', # Real Exports of Durable Goods
    'A253RL1Q225SBEA', # Real Exports of Goods
    'A020RL1Q158SBEA', # Real Exports of Goods and Services
    'B020RL1Q225SBEA', # Real Exports of Goods and Services (DISCONTINUED)
    'B641RL1Q225SBEA', # Real Exports of Goods: Automotive Vehicles, Engines, and Parts
    'A640RL1Q225SBEA', # Real Exports of Goods: Capital Goods, Except Automotive
    'B688RL1Q225SBEA', # Real Exports of Goods: Capital Goods, Except Automotive: Civilian Aircraft, Engines, and Parts
    'B850RL1Q225SBEA', # Real Exports of Goods: Capital Goods, Except Automotive: Computers, Peripherals, and Parts
    'B689RL1Q225SBEA', # Real Exports of Goods: Capital Goods, Except Automotive: Other
    'A642RL1Q225SBEA', # Real Exports of Goods: Consumer Goods, Except food and Automotive
    'B690RL1Q225SBEA', # Real Exports of Goods: Consumer Goods, Except food and Automotive: Durable Goods
    'B691RL1Q225SBEA', # Real Exports of Goods: Consumer Goods, Except food and Automotive: Nondurable Goods
    'B638RL1Q225SBEA', # Real Exports of Goods: Foods, Feeds, and Beverages
    'A639RL1Q225SBEA', # Real Exports of Goods: Industrial Supplies and Materials
    'B686RL1Q225SBEA', # Real Exports of Goods: Industrial Supplies and Materials: Durable Goods
    'B687RL1Q225SBEA', # Real Exports of Goods: Industrial Supplies and Materials: Nondurable Goods
    'A643RL1Q225SBEA', # Real Exports of Goods: Other
    'A182RL1Q225SBEA', # Real Exports of Nonagricultural Goods
    'A339RL1Q225SBEA', # Real Exports of Nondurable Goods
    'A646RL1Q225SBEA', # Real Exports of Services
    'B684RL1Q225SBEA', # Real Exports of Services: Charges for the use of intellectual property n.e.c.
    'B980RL1Q225SBEA', # Real Exports of Services: Other
    'AB69RL1Q225SBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Exports
    'B142RL1Q225SBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Exports: Autos
    'B706RL1Q225SBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Exports: Trucks
    'Y803RL1Q225SBEA', # Real exports of services: Government goods and services n.e.c.
    'Y802RL1Q225SBEA', # Real exports of services: Other business services
    'Y800RL1Q225SBEA', # Real exports of services: Transport
    'Y801RL1Q225SBEA', # Real exports of services: Travel (for all purposes including education)
    ## % Chg. from Qtr.  1 Yr. Ago (NSA)
    'OB000353Q', # Real Exports of Goods
    'OB000352Q', # Real Exports of Goods and Services
    'OB000354Q', # Real Exports of Services
    ## % Chg. from Qtr.  1 Yr. Ago (SA)
    'A253RO1Q156NBEA', # Real Exports of Goods
    'A020RO1Q156NBEA', # Real Exports of Goods and Services
    'A646RO1Q156NBEA', # Real Exports of Services
    ## Bil. of $ (SAAR)
    'A332RC1Q027SBEA', # Current receipts from the rest of the world: Exports of durable goods
    'A253RC1Q027SBEA', # Current receipts from the rest of the world: Exports of goods
    'A339RC1Q027SBEA', # Current receipts from the rest of the world: Exports of nondurable goods
    'A646RC1Q027SBEA', # Current receipts from the rest of the world: Exports of services
    'EXPGS', # Exports of Goods and Services
    'EXPGSN', # Exports of Goods and Services, GNP-Basis (DISCONTINUED)
    'B181RC1Q027SBEA', # Exports of agricultural goods
    'B641RC1Q027SBEA', # Exports of goods: Automotive vehicles, engines, and parts
    'A640RC1Q027SBEA', # Exports of goods: Capital goods, except automotive
    'B688RC1Q027SBEA', # Exports of goods: Capital goods, except automotive: Civilian aircraft, engines, and parts
    'B850RC1Q027SBEA', # Exports of goods: Capital goods, except automotive: Computers, peripherals, and parts
    'B689RC1Q027SBEA', # Exports of goods: Capital goods, except automotive: Other
    'A642RC1Q027SBEA', # Exports of goods: Consumer goods, except food and automotive
    'B690RC1Q027SBEA', # Exports of goods: Consumer goods, except food and automotive: Durable goods
    'B691RC1Q027SBEA', # Exports of goods: Consumer goods, except food and automotive: Nondurable goods
    'B638RC1Q027SBEA', # Exports of goods: Foods, feeds, and beverages
    'A639RC1Q027SBEA', # Exports of goods: Industrial supplies and materials
    'B686RC1Q027SBEA', # Exports of goods: Industrial supplies and materials: Durable goods
    'B687RC1Q027SBEA', # Exports of goods: Industrial supplies and materials: Nondurable goods
    'LA0000051Q027SBEA', # Exports of goods: Industrial supplies and materials: Nondurable goods: Nondurable goods, excluding petroleum and products
    'LA0000061Q027SBEA', # Exports of goods: Industrial supplies and materials: Nondurable goods: Petroleum and products
    'A643RC1Q027SBEA', # Exports of goods: Other
    'A182RC1Q027SBEA', # Exports of nonagricultural goods
    'Y803RC1Q027SBEA', # Exports of services: Government goods and services n.e.c. (chain-type price index)
    'B980RC1Q027SBEA', # Exports of services: Other
    'Y802RC1Q027SBEA', # Exports of services: Other business services (chain-type price index)
    'B720RC1Q027SBEA', # Exports of services: Other private services (DISCONTINUED)
    'B683RC1Q027SBEA', # Exports of services: Other transportation (DISCONTINUED)
    'B533RC1Q027SBEA', # Exports of services: Passenger fares (DISCONTINUED)
    'B684RC1Q027SBEA', # Exports of services: Royalties and license fees
    'B267RC1Q027SBEA', # Exports of services: Transfers under U.S. military agency sales contracts (DISCONTINUED)
    'Y800RC1Q027SBEA', # Exports of services: Transport (chain-type price index)
    'B493RC1Q027SBEA', # Exports of services: Travel (DISCONTINUED)
    'Y801RC1Q027SBEA', # Exports of services: Travel (for all purposes including education) (chain-type price index)
    'NETEXP', # Net Exports of Goods and Services
    ## Bil. of Chn. 1992 $ (SAAR)
    'EXPGSC1N', # Real Exports of Goods and Services, GNP-Basis (DISCONTINUED)
    ## Bil. of Chn. 2009 $ (SAAR)
    'EXPGSC96', # Real Exports of Goods and Services (DISCONTINUED)
    'NETEXC96', # Real Net Exports of Goods and Services (DISCONTINUED)
    'B020RX1Q020SBEA', # Real exports of goods and services (DISCONTINUED)
    'B720RX1Q020SBEA', # Real exports of services: Other private services (DISCONTINUED)
    'B683RX1Q020SBEA', # Real exports of services: Other transportation (DISCONTINUED)
    'B533RX1Q020SBEA', # Real exports of services: Passenger fares (DISCONTINUED)
    'B267RX1Q020SBEA', # Real exports of services: Transfers under U.S. military agency sales contracts (DISCONTINUED)
    'B493RX1Q020SBEA', # Real exports of services: Travel (DISCONTINUED)
    ## Bil. of Chn. 2012 $ (SAAR)
    'CHNGNETEXPORTSNOW', # Nowcast for Real Change of Net Exports of Goods and Services
    ## Bil. of Chn. 2017 $ (NSA)
    'ND000353Q', # Real Exports of Goods
    'ND000352Q', # Real Exports of Goods and Services
    'ND000354Q', # Real Exports of Services
    'ND000374Q', # Real Net Exports of Goods and Services
    ## Bil. of Chn. 2017 $ (SAAR)
    'EXPGSC1', # Real Exports of Goods and Services
    'B850RX1Q020SBEA', # Real Exports of goods: Capital goods, except automotive: Computers, peripherals, and parts
    'LB0000051Q020SBEA', # Real Exports of goods: Industrial supplies and materials: Nondurable goods: Nondurable goods, excluding petroleum and products
    'LB0000061Q020SBEA', # Real Exports of goods: Industrial supplies and materials: Nondurable goods: Petroleum and products
    'NETEXC', # Real Net Exports of Goods and Services
    'B181RX1Q020SBEA', # Real exports of agricultural goods
    'A332RX1Q020SBEA', # Real exports of durable goods
    'A253RX1Q020SBEA', # Real exports of goods
    'C020RX1Q020SBEA', # Real exports of goods and services, command basis
    'A977RX1Q020SBEA', # Real exports of goods and services: Residual
    'B641RX1Q020SBEA', # Real exports of goods: Automotive vehicles, engines, and parts
    'A640RX1Q020SBEA', # Real exports of goods: Capital goods, except automotive
    'B688RX1Q020SBEA', # Real exports of goods: Capital goods, except automotive: Civilian aircraft, engines, and parts
    'B689RX1Q020SBEA', # Real exports of goods: Capital goods, except automotive: Other
    'A642RX1Q020SBEA', # Real exports of goods: Consumer goods, except food and automotive
    'B690RX1Q020SBEA', # Real exports of goods: Consumer goods, except food and automotive: Durable goods
    'B691RX1Q020SBEA', # Real exports of goods: Consumer goods, except food and automotive: Nondurable goods
    'B638RX1Q020SBEA', # Real exports of goods: Foods, feeds, and beverages
    'A639RX1Q020SBEA', # Real exports of goods: Industrial supplies and materials
    'B686RX1Q020SBEA', # Real exports of goods: Industrial supplies and materials: Durable goods
    'B687RX1Q020SBEA', # Real exports of goods: Industrial supplies and materials: Nondurable goods
    'A643RX1Q020SBEA', # Real exports of goods: Other
    'A182RX1Q020SBEA', # Real exports of nonagricultural goods
    'A339RX1Q020SBEA', # Real exports of nondurable goods
    'A646RX1Q020SBEA', # Real exports of services
    'Y803RX1Q020SBEA', # Real exports of services: Government goods and services n.e.c.
    'B980RX1Q020SBEA', # Real exports of services: Other
    'Y802RX1Q020SBEA', # Real exports of services: Other business services
    'B684RX1Q020SBEA', # Real exports of services: Royalties and license fees
    'Y800RX1Q020SBEA', # Real exports of services: Transport
    'Y801RX1Q020SBEA', # Real exports of services: Travel (for all purposes including education)
    ## Index 2017=100 (NSA)
    'NC000352Q', # Exports of Goods and Services
    'NC000354Q', # Exports of Services
    'NB000352Q', # Real Exports of Goods and Services
    'NB000354Q', # Real Exports of Services
    ## Index 2017=100 (SAAR)
    'Y803RG3Q086SBEA', # Exports of services: Government goods and services n.e.c. (chain-type price index)
    'Y802RG3Q086SBEA', # Exports of services: Other business services (chain-type price index)
    'Y800RG3Q086SBEA', # Exports of services: Transport (chain-type price index)
    'Y801RG3Q086SBEA', # Exports of services: Travel (for all purposes including education) (chain-type price index)
    'Y803RA3Q086SBEA', # Real exports of services: Government goods and services n.e.c. (chain-type quantity index)
    'Y802RA3Q086SBEA', # Real exports of services: Other business services (chain-type quantity index)
    'Y800RA3Q086SBEA', # Real exports of services: Transport (chain-type quantity index)
    'Y801RA3Q086SBEA', # Real exports of services: Travel (for all purposes including education) (chain-type quantity index)
    ## Mil. of $ (NSA)
    'NA000352Q', # Exports of Goods and Services
    'NA000354Q', # Exports of Services
    'NA000374Q', # Net exports of goods and services
    ## Percentage Points (SA)
    'CHNGNETEXPORTSCONTRIBNOW', # Contributions to percent change in GDPNow: Real Change of Net Exports of Goods and Services
    'EXPORTSGOODSCONTRIBNOW', # Contributions to percent change in GDPNow: Real Exports of Goods
    'EXPORTSCONTRIBNOW', # Contributions to percent change in GDPNow: Real Exports of Goods and Services
    'EXPORTSSERVICESCONTRIBNOW', # Contributions to percent change in GDPNow: Real Exports of Services
    ## Percentage Points at Annual Rate (SAAR)
    'CB0000052Q224SBEA', # Contributions to Percent Change in Real Exports of Goods and Services by Type of Product: Exports of goods: Industrial supplies and materials: Nondurable goods: Nondurable goods, excluding petroleum and products
    'CB0000062Q224SBEA', # Contributions to Percent Change in Real Exports of Goods and Services by Type of Product: Exports of goods: Industrial supplies and materials: Nondurable goods: Petroleum and products
    'Y803RZ2Q224SBEA', # Contributions to Percent Change in Real Exports of Goods and Services by Type of Product: Exports of services: Government goods and services n.e.c.
    'Y802RZ2Q224SBEA', # Contributions to Percent Change in Real Exports of Goods and Services by Type of Product: Exports of services: Other business services
    'Y800RZ2Q224SBEA', # Contributions to Percent Change in Real Exports of Goods and Services by Type of Product: Exports of services: Transport
    'Y801RZ2Q224SBEA', # Contributions to Percent Change in Real Exports of Goods and Services by Type of Product: Exports of services: Travel (for all purposes including education)
    'A253RZ2Q224SBEA', # Contributions to percent change in real exports of goods
    'B641RZ2Q224SBEA', # Contributions to percent change in real exports of goods: Automotive vehicles, engines, and parts
    'A640RZ2Q224SBEA', # Contributions to percent change in real exports of goods: Capital goods, except automotive
    'B688RZ2Q224SBEA', # Contributions to percent change in real exports of goods: Capital goods, except automotive: Civilian aircraft, engines, and parts
    'B850RZ2Q224SBEA', # Contributions to percent change in real exports of goods: Capital goods, except automotive: Computers, peripherals, and parts
    'B689RZ2Q224SBEA', # Contributions to percent change in real exports of goods: Capital goods, except automotive: Other
    'A642RZ2Q224SBEA', # Contributions to percent change in real exports of goods: Consumer goods, except food and automotive
    'B690RZ2Q224SBEA', # Contributions to percent change in real exports of goods: Consumer goods, except food and automotive: Durable goods
    'B691RZ2Q224SBEA', # Contributions to percent change in real exports of goods: Consumer goods, except food and automotive: Nondurable goods
    'B638RZ2Q224SBEA', # Contributions to percent change in real exports of goods: Foods, feeds, and beverages
    'A639RZ2Q224SBEA', # Contributions to percent change in real exports of goods: Industrial supplies and materials
    'B686RZ2Q224SBEA', # Contributions to percent change in real exports of goods: Industrial supplies and materials: Durable goods
    'B687RZ2Q224SBEA', # Contributions to percent change in real exports of goods: Industrial supplies and materials: Nondurable goods
    'A643RZ2Q224SBEA', # Contributions to percent change in real exports of goods: Other
    'A646RZ2Q224SBEA', # Contributions to percent change in real exports of services
    'B980RZ2Q224SBEA', # Contributions to percent change in real exports of services: Other
    'B720RZ2Q224SBEA', # Contributions to percent change in real exports of services: Other private services (DISCONTINUED)
    'B683RZ2Q224SBEA', # Contributions to percent change in real exports of services: Other transportation (DISCONTINUED)
    'B533RZ2Q224SBEA', # Contributions to percent change in real exports of services: Passenger fares (DISCONTINUED)
    'B684RZ2Q224SBEA', # Contributions to percent change in real exports of services: Royalties and license fees
    'B267RZ2Q224SBEA', # Contributions to percent change in real exports of services: Transfers under U.S. military agency sales contracts (DISCONTINUED)
    'B493RZ2Q224SBEA', # Contributions to percent change in real exports of services: Travel (DISCONTINUED)
    'A253RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Exports of goods
    'A020RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Exports of goods and services
    'A646RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Exports of services
    'A019RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Net exports of goods and services

]

# Annually (155)
ids_Y = [
    # Exports (155)
    ## % Chg. from Preceding Period (NSA)
    'PB0000051A225NBEA', # Exports of goods: Industrial supplies and materials: Nondurable goods: Nondurable goods, excluding petroleum and products
    'PB0000061A225NBEA', # Exports of goods: Industrial supplies and materials: Nondurable goods: Petroleum and products
    'Y803RL1A225NBEA', # Exports of services: Government goods and services n.e.c.
    'Y802RL1A225NBEA', # Exports of services: Other business services
    'Y800RL1A225NBEA', # Exports of services: Transport
    'Y801RL1A225NBEA', # Exports of services: Travel (for all purposes including education)
    'B181RL1A225NBEA', # Real Exports of Agricultural Goods
    'A332RL1A225NBEA', # Real Exports of Durable Goods
    'A253RL1A225NBEA', # Real Exports of Goods
    'A020RL1A158NBEA', # Real Exports of Goods and Services
    'B020RL1A225NBEA', # Real Exports of Goods and Services (DISCONTINUED)
    'B641RL1A225NBEA', # Real Exports of Goods: Automotive Vehicles, Engines, and Parts
    'A640RL1A225NBEA', # Real Exports of Goods: Capital Goods, Except Automotive
    'B688RL1A225NBEA', # Real Exports of Goods: Capital Goods, Except Automotive: Civilian Aircraft, Engines, and Parts
    'B850RL1A225NBEA', # Real Exports of Goods: Capital Goods, Except Automotive: Computers, Peripherals, and Parts
    'B689RL1A225NBEA', # Real Exports of Goods: Capital Goods, Except Automotive: Other
    'A642RL1A225NBEA', # Real Exports of Goods: Consumer Goods, Except Automotive
    'B690RL1A225NBEA', # Real Exports of Goods: Consumer Goods, Except Automotive: Durable Goods
    'B691RL1A225NBEA', # Real Exports of Goods: Consumer Goods, Except Automotive: Nondurable Goods
    'B638RL1A225NBEA', # Real Exports of Goods: Foods, Feeds, and Beverages
    'A639RL1A225NBEA', # Real Exports of Goods: Industrial Supplies and Materials
    'B686RL1A225NBEA', # Real Exports of Goods: Industrial Supplies and Materials: Durable Goods
    'B687RL1A225NBEA', # Real Exports of Goods: Industrial Supplies and Materials: Nondurable Goods
    'A643RL1A225NBEA', # Real Exports of Goods: Other
    'A182RL1A225NBEA', # Real Exports of Nonagricultural Goods
    'A339RL1A225NBEA', # Real Exports of Nondurable Goods
    'A646RL1A225NBEA', # Real Exports of Services
    'B684RL1A225NBEA', # Real Exports of Services: Charges for the use of intellectual property n.e.c.
    'B980RL1A225NBEA', # Real Exports of Services: Other
    'AB69RL1A225NBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Exports
    'B142RL1A225NBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Exports: Autos
    'B706RL1A225NBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Exports: Trucks
    ## Bil. of $ (NSA)
    'A332RC1A027NBEA', # Current receipts from the rest of the world: Exports of durable goods
    'A253RC1A027NBEA', # Current receipts from the rest of the world: Exports of goods
    'A339RC1A027NBEA', # Current receipts from the rest of the world: Exports of nondurable goods
    'A646RC1A027NBEA', # Current receipts from the rest of the world: Exports of services
    'EXPGSA', # Exports of Goods and Services
    'EXPGSNA', # Exports of Goods and Services, GNP-Basis (DISCONTINUED)
    'B181RC1A027NBEA', # Exports of agricultural goods
    'B1087C1A027NBEA', # Exports of gold, International Transactions Accounts
    'B1233C1A027NBEA', # Exports of gold: Statistical differences, International Transactions Accounts vs. NIPAs
    'B1229C1A027NBEA', # Exports of goods and services and income receipts, International Transactions Accounts
    'A1073C1A027NBEA', # Exports of goods and services and income receipts, NIPAs
    'B920RC1A027NBEA', # Exports of goods and services and income receipts: Adjustment for U.S. territories and Puerto Rico
    'B2628C1A027NBEA', # Exports of goods and services and income receipts: Adjustment for grossing of parent/affiliate transactions
    'B1607C1A027NBEA', # Exports of goods and services and income receipts: Financial services furnished without payment
    'W320RC1A027NBEA', # Exports of goods and services and income receipts: Imputed interest received from the rest of the world
    'B2629C1A027NBEA', # Exports of goods and services and income receipts: Other items (DISCONTINUED)
    'B1085C1A027NBEA', # Exports of goods and services and income receipts: Statistical differences, International Transactions Accounts vs. NIPAs
    'B1232C1A027NBEA', # Exports of goods, ITAs
    'B1234C1A027NBEA', # Exports of goods: Adjustment for U.S. territories and Puerto Rico
    'B641RC1A027NBEA', # Exports of goods: Automotive vehicles, engines, and parts
    'A640RC1A027NBEA', # Exports of goods: Capital goods, except automotive
    'B688RC1A027NBEA', # Exports of goods: Capital goods, except automotive: Civilian aircraft, engines, and parts
    'B850RC1A027NBEA', # Exports of goods: Capital goods, except automotive: Computers, peripherals, and parts
    'B689RC1A027NBEA', # Exports of goods: Capital goods, except automotive: Other
    'A642RC1A027NBEA', # Exports of goods: Consumer goods, except automotive
    'B690RC1A027NBEA', # Exports of goods: Consumer goods, except automotive: Durable goods
    'B691RC1A027NBEA', # Exports of goods: Consumer goods, except automotive: Nondurable goods
    'B638RC1A027NBEA', # Exports of goods: Foods, feeds, and beverages
    'A639RC1A027NBEA', # Exports of goods: Industrial supplies and materials
    'B686RC1A027NBEA', # Exports of goods: Industrial supplies and materials: Durable goods
    'B687RC1A027NBEA', # Exports of goods: Industrial supplies and materials: Nondurable goods
    'LA0000051A027NBEA', # Exports of goods: Industrial supplies and materials: Nondurable goods: Nondurable goods, excluding petroleum and products
    'LA0000061A027NBEA', # Exports of goods: Industrial supplies and materials: Nondurable goods: Petroleum and products
    'A643RC1A027NBEA', # Exports of goods: Other
    'A182RC1A027NBEA', # Exports of nonagricultural goods
    'B1235C1A027NBEA', # Exports of services, ITAs
    'B1238C1A027NBEA', # Exports of services: Adjustment for U.S. territories and Puerto Rico
    'Y803RC1A027NBEA', # Exports of services: Government goods and services n.e.c.
    'B980RC1A027NBEA', # Exports of services: Other
    'B1237C1A027NBEA', # Exports of services: Other adjustment items, International Transactions Accounts vs. NIPAs
    'Y802RC1A027NBEA', # Exports of services: Other business services
    'B720RC1A027NBEA', # Exports of services: Other private services (DISCONTINUED)
    'B683RC1A027NBEA', # Exports of services: Other transportation (DISCONTINUED)
    'B533RC1A027NBEA', # Exports of services: Passenger fares (DISCONTINUED)
    'B684RC1A027NBEA', # Exports of services: Royalties and license fees
    'B1236C1A027NBEA', # Exports of services: Statistical differences, International Transactions Accounts vs. NIPAs
    'B267RC1A027NBEA', # Exports of services: Transfers under U.S. military agency sales contracts (DISCONTINUED)
    'Y800RC1A027NBEA', # Exports of services: Transport
    'B493RC1A027NBEA', # Exports of services: Travel (DISCONTINUED)
    'Y801RC1A027NBEA', # Exports of services: Travel (for all purposes including education)
    'A019RC1A027NBEA', # Net exports of goods and services
    'A1072C1A027NBEA', # Net exports of goods and services and net receipts of income, NIPAs
    'B555RC1A027NBEA', # Private fixed investment in equipment and software: Net exports of used equipment
    ## Bil. of 1982 $ (NSA)
    'EXPGSCNA', # Real Exports of Goods and Services, GNP-Basis (DISCONTINUED)
    ## Bil. of Chn. 2009 $ (NSA)
    'B020RX1A020NBEA', # Real exports of goods and services (DISCONTINUED)
    'B720RX1A020NBEA', # Real exports of services: Other private services (DISCONTINUED)
    'B683RX1A020NBEA', # Real exports of services: Other transportation (DISCONTINUED)
    'B533RX1A020NBEA', # Real exports of services: Passenger fares (DISCONTINUED)
    'B267RX1A020NBEA', # Real exports of services: Transfers under U.S. military agency sales contracts (DISCONTINUED)
    'B493RX1A020NBEA', # Real exports of services: Travel (DISCONTINUED)
    ## Bil. of Chn. 2017 $ (NSA)
    'EXPGSCA', # Real Exports of Goods and Services
    'B850RX1A020NBEA', # Real Exports of goods: Capital goods, except automotive: Computers, peripherals, and parts
    'LB0000051A020NBEA', # Real Exports of goods: Industrial supplies and materials: Nondurable goods: Nondurable goods, excluding petroleum and products
    'LB0000061A020NBEA', # Real Exports of goods: Industrial supplies and materials: Nondurable goods: Petroleum and products
    'Y803RX1A020NBEA', # Real Exports of services: Government goods and services n.e.c.
    'Y802RX1A020NBEA', # Real Exports of services: Other business services
    'Y800RX1A020NBEA', # Real Exports of services: Transport
    'Y801RX1A020NBEA', # Real Exports of services: Travel (for all purposes including education)
    'B181RX1A020NBEA', # Real exports of agricultural goods
    'A332RX1A020NBEA', # Real exports of durable goods
    'A253RX1A020NBEA', # Real exports of goods
    'C020RX1A020NBEA', # Real exports of goods and services, command basis
    'A977RX1A020NBEA', # Real exports of goods and services: Residual
    'B641RX1A020NBEA', # Real exports of goods: Automotive vehicles, engines, and parts
    'A640RX1A020NBEA', # Real exports of goods: Capital goods, except automotive
    'B688RX1A020NBEA', # Real exports of goods: Capital goods, except automotive: Civilian aircraft, engines, and parts
    'B689RX1A020NBEA', # Real exports of goods: Capital goods, except automotive: Other
    'A642RX1A020NBEA', # Real exports of goods: Consumer goods, except automotive
    'B690RX1A020NBEA', # Real exports of goods: Consumer goods, except automotive: Durable goods
    'B691RX1A020NBEA', # Real exports of goods: Consumer goods, except automotive: Nondurable goods
    'B638RX1A020NBEA', # Real exports of goods: Foods, feeds, and beverages
    'A639RX1A020NBEA', # Real exports of goods: Industrial supplies and materials
    'B686RX1A020NBEA', # Real exports of goods: Industrial supplies and materials: Durable goods
    'B687RX1A020NBEA', # Real exports of goods: Industrial supplies and materials: Nondurable goods
    'A643RX1A020NBEA', # Real exports of goods: Other
    'A182RX1A020NBEA', # Real exports of nonagricultural goods
    'A339RX1A020NBEA', # Real exports of nondurable goods
    'A646RX1A020NBEA', # Real exports of services
    'B980RX1A020NBEA', # Real exports of services: Other
    'B684RX1A020NBEA', # Real exports of services: Royalties and license fees
    'A019RX1A020NBEA', # Real net exports of goods and services
    ## Percentage Points at Annual Rate (NSA)
    'CB0000052A224NBEA', # Contributions to percent change in Exports of goods and services: Export of goods: Industrial supplies and materials: Nondurable goods: Nondurable goods, excluding petroleum and products
    'CB0000062A224NBEA', # Contributions to percent change in Exports of goods and services: Export of goods: Industrial supplies and materials: Nondurable goods: Petroleum and products
    'Y803RZ2A224NBEA', # Contributions to percent change in Exports of goods and services: Export of services: Government goods and services n.e.c.
    'Y802RZ2A224NBEA', # Contributions to percent change in Exports of goods and services: Export of services: Other business services
    'Y800RZ2A224NBEA', # Contributions to percent change in Exports of goods and services: Export of services: Transport
    'Y801RZ2A224NBEA', # Contributions to percent change in Exports of goods and services: Export of services: Travel (for all purposes including education)
    'A253RZ2A224NBEA', # Contributions to percent change in real exports of goods
    'B641RZ2A224NBEA', # Contributions to percent change in real exports of goods: Automotive vehicles, engines, and parts
    'A640RZ2A224NBEA', # Contributions to percent change in real exports of goods: Capital goods, except automotive
    'B688RZ2A224NBEA', # Contributions to percent change in real exports of goods: Capital goods, except automotive: Civilian aircraft, engines, and parts
    'B850RZ2A224NBEA', # Contributions to percent change in real exports of goods: Capital goods, except automotive: Computers, peripherals, and parts
    'B689RZ2A224NBEA', # Contributions to percent change in real exports of goods: Capital goods, except automotive: Other
    'A642RZ2A224NBEA', # Contributions to percent change in real exports of goods: Consumer goods, except automotive
    'B690RZ2A224NBEA', # Contributions to percent change in real exports of goods: Consumer goods, except automotive: Durable goods
    'B691RZ2A224NBEA', # Contributions to percent change in real exports of goods: Consumer goods, except automotive: Nondurable goods
    'B638RZ2A224NBEA', # Contributions to percent change in real exports of goods: Foods, feeds, and beverages
    'A639RZ2A224NBEA', # Contributions to percent change in real exports of goods: Industrial supplies and materials
    'B686RZ2A224NBEA', # Contributions to percent change in real exports of goods: Industrial supplies and materials: Durable goods
    'B687RZ2A224NBEA', # Contributions to percent change in real exports of goods: Industrial supplies and materials: Nondurable goods
    'A643RZ2A224NBEA', # Contributions to percent change in real exports of goods: Other
    'A646RZ2A224NBEA', # Contributions to percent change in real exports of services
    'B980RZ2A224NBEA', # Contributions to percent change in real exports of services: Other
    'B720RZ2A224NBEA', # Contributions to percent change in real exports of services: Other private services (DISCONTINUED)
    'B683RZ2A224NBEA', # Contributions to percent change in real exports of services: Other transportation (DISCONTINUED)
    'B533RZ2A224NBEA', # Contributions to percent change in real exports of services: Passenger fares (DISCONTINUED)
    'B684RZ2A224NBEA', # Contributions to percent change in real exports of services: Royalties and license fees
    'B267RZ2A224NBEA', # Contributions to percent change in real exports of services: Transfers under U.S. military agency sales contracts (DISCONTINUED)
    'B493RZ2A224NBEA', # Contributions to percent change in real exports of services: Travel (DISCONTINUED)
    'A253RY2A224NBEA', # Contributions to percent change in real gross domestic product: Exports of goods
    'A020RY2A224NBEA', # Contributions to percent change in real gross domestic product: Exports of goods and services
    'A646RY2A224NBEA', # Contributions to percent change in real gross domestic product: Exports of services
    'A019RY2A224NBEA', # Contributions to percent change in real gross domestic product: Net exports of goods and services

]
