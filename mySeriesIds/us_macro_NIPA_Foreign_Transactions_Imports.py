# FRED > National Accounts > National Income & Product Accounts > Foreign Transactions > Imports (category_id 33019)
# https://fred.stlouisfed.org/categories/33019  하위 카테고리 + 직속 시리즈 전체. 주기는 FRED 메타데이터 기준
# 위계: # 카테고리 > ## 단위 (계절조정)
dir='us_macro_NIPA_Foreign_Transactions_Imports'
category_ids = [33019]  # build_db.py가 이 카테고리(하위 포함) 메타데이터를 일괄 조회

# Monthly (2)
ids_M = [
    # Imports (2)
    ## Mil. of $ (SA)
    'BOMVMPM133S', # U.S. Imports of Services - Passenger Fares
    'BOMTVLM133S', # U.S. Imports of Services - Travel

]

# Quarterly (167)
ids_Q = [
    # Imports (167)
    ## % Chg. at Annual Rate (SAAR)
    'IMPORTSGOODSNOW', # Nowcast for Real Imports of Goods
    'IMPORTSNOW', # Nowcast for Real Imports of Goods and Services
    'IMPORTSERVICESNOW', # Nowcast for Real Imports of Services
    ## % Chg. from Preceding Period (SAAR)
    'PB0000071Q225SBEA', # Imports of goods: Industrial supplies and materials: Nondurable goods
    'A333RL1Q225SBEA', # Real Imports of Durable Goods
    'A255RL1Q225SBEA', # Real Imports of Goods
    'A021RL1Q158SBEA', # Real Imports of Goods and Services
    'B021RL1Q225SBEA', # Real Imports of Goods and Services (DISCONTINUED)
    'B651RL1Q225SBEA', # Real Imports of Goods: Automotive Vehicles, Engines, and Parts
    'A650RL1Q225SBEA', # Real Imports of Goods: Capital Goods, Except Automotive
    'B932RL1Q225SBEA', # Real Imports of Goods: Capital Goods, Except Automotive: Civilian Aircraft, Engines, and Parts
    'B852RL1Q225SBEA', # Real Imports of Goods: Capital Goods, Except Automotive: Computers, Peripherals, and Parts
    'B853RL1Q225SBEA', # Real Imports of Goods: Capital Goods, Except Automotive: Other
    'A652RL1Q225SBEA', # Real Imports of Goods: Consumer Goods, Except Food and Automotive
    'B697RL1Q225SBEA', # Real Imports of Goods: Consumer Goods, Except Food and Automotive: Durable Goods
    'B698RL1Q225SBEA', # Real Imports of Goods: Consumer Goods, Except Food and Automotive: Nondurable Goods
    'B647RL1Q225SBEA', # Real Imports of Goods: Foods, Feeds, and Beverages
    'A649RL1Q225SBEA', # Real Imports of Goods: Industrial Supplies and Materials, Except Petroleum and Products (DISCONTINUED)
    'B696RL1Q225SBEA', # Real Imports of Goods: Industrial Supplies and Materials, Except Petroleum and Products: Nondurable Goods
    'A820RL1Q225SBEA', # Real Imports of Goods: Industrial Supplies and Materials: Durable Goods
    'A653RL1Q225SBEA', # Real Imports of Goods: Other
    'B648RL1Q225SBEA', # Real Imports of Goods: Petroleum and Products
    'A340RL1Q225SBEA', # Real Imports of Nondurable Goods
    'A187RL1Q225SBEA', # Real Imports of Nonpetroleum Goods
    'A656RL1Q225SBEA', # Real Imports of Services
    'B656RL1Q225SBEA', # Real Imports of Services (DISCONTINUED)
    'B908RL1Q225SBEA', # Real Imports of Services: Charges for the use of intellectual property n.e.c.
    'B910RL1Q225SBEA', # Real Imports of Services: Other
    'PB0000041Q225SBEA', # Real Imports of goods: Industrial supplies and materials
    'AB70RL1Q225SBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Imports
    'B143RL1Q225SBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Imports: Autos
    'B707RL1Q225SBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Imports: Trucks
    'B149RL1Q225SBEA', # Real Motor Vehicle Output: Sales of Imported New Autos
    'Y807RL1Q225SBEA', # Real imports of services: Government goods and services n.e.c.
    'Y806RL1Q225SBEA', # Real imports of services: Other business services
    'Y804RL1Q225SBEA', # Real imports of services: Transport
    'Y805RL1Q225SBEA', # Real imports of services: Travel (for all purposes including education)
    ## % Chg. from Qtr.  1 Yr. Ago (NSA)
    'OB000343Q', # Real Imports of Goods
    'OB000342Q', # Real Imports of Goods and Services
    'OB000344Q', # Real Imports of Services
    ## % Chg. from Qtr.  1 Yr. Ago (SA)
    'A255RO1Q156NBEA', # Real Imports of Goods
    'A021RO1Q156NBEA', # Real Imports of Goods and Services
    'A656RO1Q156NBEA', # Real Imports of Services
    ## Bil. of $ (SAAR)
    'A333RC1Q027SBEA', # Current payments to the rest of the world: Imports of durable goods
    'A255RC1Q027SBEA', # Current payments to the rest of the world: Imports of goods
    'A340RC1Q027SBEA', # Current payments to the rest of the world: Imports of nondurable goods
    'B656RC1Q027SBEA', # Current payments to the rest of the world: Imports of services
    'IMPGS', # Imports of Goods and Services
    'IMPGSN', # Imports of Goods and Services, GNP-Basis (DISCONTINUED)
    'B651RC1Q027SBEA', # Imports of goods: Automotive vehicles, engines, and parts
    'A650RC1Q027SBEA', # Imports of goods: Capital goods, except automotive
    'B932RC1Q027SBEA', # Imports of goods: Capital goods, except automotive: Civilian aircraft, engines, and parts
    'B852RC1Q027SBEA', # Imports of goods: Capital goods, except automotive: Computers, peripherals, and parts
    'B853RC1Q027SBEA', # Imports of goods: Capital goods, except automotive: Other
    'A652RC1Q027SBEA', # Imports of goods: Consumer goods, except food and automotive
    'B697RC1Q027SBEA', # Imports of goods: Consumer goods, except food and automotive: Durable goods
    'B698RC1Q027SBEA', # Imports of goods: Consumer goods, except food and automotive: Nondurable goods
    'B647RC1Q027SBEA', # Imports of goods: Foods, feeds, and beverages
    'LA0000041Q027SBEA', # Imports of goods: Industrial supplies and materials
    'A649RC1Q027SBEA', # Imports of goods: Industrial supplies and materials, except petroleum and products (DISCONTINUED)
    'B696RC1Q027SBEA', # Imports of goods: Industrial supplies and materials, except petroleum and products: Nondurable goods
    'A820RC1Q027SBEA', # Imports of goods: Industrial supplies and materials: Durable goods
    'LA0000071Q027SBEA', # Imports of goods: Industrial supplies and materials: Nondurable goods
    'A653RC1Q027SBEA', # Imports of goods: Other
    'B648RC1Q027SBEA', # Imports of goods: Petroleum and products
    'A187RC1Q027SBEA', # Imports of nonpetroleum goods
    'B752RC1Q027SBEA', # Imports of services: Direct defense expenditures (DISCONTINUED)
    'Y807RC1Q027SBEA', # Imports of services: Government goods and services n.e.c. (chain-type price index)
    'B910RC1Q027SBEA', # Imports of services: Other
    'Y806RC1Q027SBEA', # Imports of services: Other business services (chain-type price index)
    'B909RC1Q027SBEA', # Imports of services: Other private services (DISCONTINUED)
    'B770RC1Q027SBEA', # Imports of services: Other transportation (DISCONTINUED)
    'B769RC1Q027SBEA', # Imports of services: Passenger fares (DISCONTINUED)
    'B908RC1Q027SBEA', # Imports of services: Royalties and license fees
    'Y804RC1Q027SBEA', # Imports of services: Transport (chain-type price index)
    'B768RC1Q027SBEA', # Imports of services: Travel (DISCONTINUED)
    'Y805RC1Q027SBEA', # Imports of services: Travel (for all purposes including education) (chain-type price index)
    ## Bil. of Chn. 1992 $ (SAAR)
    'IMPGSC1N', # Real Imports of Goods and Services, GNP-Basis (DISCONTINUED)
    ## Bil. of Chn. 2009 $ (SAAR)
    'B021RX1Q020SBEA', # Real imports of goods and services (DISCONTINUED)
    'IMPGSC96', # Real imports of goods and services (DISCONTINUED)
    'A649RX1Q020SBEA', # Real imports of goods: Industrial supplies and materials, except petroleum and products (DISCONTINUED)
    'B752RX1Q020SBEA', # Real imports of services: Direct defense expenditures (DISCONTINUED)
    'B909RX1Q020SBEA', # Real imports of services: Other private services (DISCONTINUED)
    'B770RX1Q020SBEA', # Real imports of services: Other transportation (DISCONTINUED)
    'B769RX1Q020SBEA', # Real imports of services: Passenger fares (DISCONTINUED)
    'B768RX1Q020SBEA', # Real imports of services: Travel (DISCONTINUED)
    ## Bil. of Chn. 2017 $ (NSA)
    'ND000343Q', # Real Imports of Goods
    'ND000342Q', # Real Imports of Goods and Services
    'ND000344Q', # Real Imports of Services
    ## Bil. of Chn. 2017 $ (SAAR)
    'B852RX1Q020SBEA', # Real Imports of goods: Capital goods, except automotive: Computers, peripherals, and parts
    'LB0000041Q020SBEA', # Real Imports of goods: Industrial supplies and materials
    'LB0000071Q020SBEA', # Real Imports of goods: Industrial supplies and materials: Nondurable goods
    'A333RX1Q020SBEA', # Real imports of durable goods
    'A255RX1Q020SBEA', # Real imports of goods
    'IMPGSC1', # Real imports of goods and services
    'C021RX1Q020SBEA', # Real imports of goods and services, command basis
    'A978RX1Q020SBEA', # Real imports of goods and services: Residual
    'B651RX1Q020SBEA', # Real imports of goods: Automotive vehicles, engines, and parts
    'A650RX1Q020SBEA', # Real imports of goods: Capital goods, except automotive
    'B932RX1Q020SBEA', # Real imports of goods: Capital goods, except automotive: Civilian aircraft, engines, and parts
    'B853RX1Q020SBEA', # Real imports of goods: Capital goods, except automotive: Other
    'A652RX1Q020SBEA', # Real imports of goods: Consumer goods, except food and automotive
    'B697RX1Q020SBEA', # Real imports of goods: Consumer goods, except food and automotive: Durable goods
    'B698RX1Q020SBEA', # Real imports of goods: Consumer goods, except food and automotive: Nondurable goods
    'B647RX1Q020SBEA', # Real imports of goods: Foods, feeds, and beverages
    'B696RX1Q020SBEA', # Real imports of goods: Industrial supplies and materials, except petroleum and products: Nondurable goods
    'A820RX1Q020SBEA', # Real imports of goods: Industrial supplies and materials: Durable goods
    'A653RX1Q020SBEA', # Real imports of goods: Other
    'B648RX1Q020SBEA', # Real imports of goods: Petroleum and products
    'A340RX1Q020SBEA', # Real imports of nondurable goods
    'A187RX1Q020SBEA', # Real imports of nonpetroleum goods
    'B656RX1Q020SBEA', # Real imports of services
    'Y807RX1Q020SBEA', # Real imports of services: Government goods and services n.e.c.
    'B910RX1Q020SBEA', # Real imports of services: Other
    'Y806RX1Q020SBEA', # Real imports of services: Other business services
    'B908RX1Q020SBEA', # Real imports of services: Royalties and license fees
    'Y804RX1Q020SBEA', # Real imports of services: Transport
    'Y805RX1Q020SBEA', # Real imports of services: Travel (for all purposes including education)
    ## Index 2017=100 (NSA)
    'NC000342Q', # Imports of Goods and Services
    'NC000344Q', # Imports of Services
    'NB000342Q', # Real Imports of Goods and Services
    'NB000344Q', # Real Imports of Services
    ## Index 2017=100 (SAAR)
    'Y807RG3Q086SBEA', # Imports of services: Government goods and services n.e.c. (chain-type price index)
    'Y806RG3Q086SBEA', # Imports of services: Other business services (chain-type price index)
    'Y804RG3Q086SBEA', # Imports of services: Transport (chain-type price index)
    'Y805RG3Q086SBEA', # Imports of services: Travel (for all purposes including education) (chain-type price index)
    'Y807RA3Q086SBEA', # Real imports of services: Government goods and services n.e.c. (chain-type quantity index)
    'Y806RA3Q086SBEA', # Real imports of services: Other business services (chain-type quantity index)
    'Y804RA3Q086SBEA', # Real imports of services: Transport (chain-type quantity index)
    'Y805RA3Q086SBEA', # Real imports of services: Travel (for all purposes including education) (chain-type quantity index)
    ## Mil. of $ (NSA)
    'NA000342Q', # Imports of Goods and Services
    'NA000344Q', # Imports of Services
    ## Percentage Points (SA)
    'IMPORTSGOODSCONTRIBNOW', # Contributions to percent change in GDPNow: Real Imports of Goods
    'IMPORTSCONTRIBNOW', # Contributions to percent change in GDPNow: Real Imports of Goods and Services
    'IMPORTSERVICESCONTRIBNOW', # Contributions to percent change in GDPNow: Real Imports of Services
    ## Percentage Points at Annual Rate (SAAR)
    'CB0000042Q224SBEA', # Contributions to Percent Change in Real Imports of Goods and Services by Type of Product: Imports of goods: Industrial supplies and materials
    'CB0000072Q224SBEA', # Contributions to Percent Change in Real Imports of Goods and Services by Type of Product: Imports of goods: Industrial supplies and materials: Nondurable goods
    'Y807RZ2Q224SBEA', # Contributions to Percent Change in Real Imports of Goods and Services by Type of Product: Imports of services: Government goods and services n.e.c.
    'Y806RZ2Q224SBEA', # Contributions to Percent Change in Real Imports of Goods and Services by Type of Product: Imports of services: Other business services
    'Y804RZ2Q224SBEA', # Contributions to Percent Change in Real Imports of Goods and Services by Type of Product: Imports of services: Transport
    'Y805RZ2Q224SBEA', # Contributions to Percent Change in Real Imports of Goods and Services by Type of Product: Imports of services: Travel (for all purposes including education)
    'A255RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Imports of goods
    'A021RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Imports of goods and services
    'A656RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Imports of services
    'A255RZ2Q224SBEA', # Contributions to percent change in real imports of goods
    'B651RZ2Q224SBEA', # Contributions to percent change in real imports of goods: Automotive vehicles, engines, and parts
    'A650RZ2Q224SBEA', # Contributions to percent change in real imports of goods: Capital goods, except automotive
    'B932RZ2Q224SBEA', # Contributions to percent change in real imports of goods: Capital goods, except automotive: Civilian aircraft, engines, and parts
    'B852RZ2Q224SBEA', # Contributions to percent change in real imports of goods: Capital goods, except automotive: Computers, peripherals, and parts
    'B853RZ2Q224SBEA', # Contributions to percent change in real imports of goods: Capital goods, except automotive: Other
    'A652RZ2Q224SBEA', # Contributions to percent change in real imports of goods: Consumer goods, except food and automotive
    'B697RZ2Q224SBEA', # Contributions to percent change in real imports of goods: Consumer goods, except food and automotive: Durable goods
    'B698RZ2Q224SBEA', # Contributions to percent change in real imports of goods: Consumer goods, except food and automotive: Nondurable goods
    'B647RZ2Q224SBEA', # Contributions to percent change in real imports of goods: Foods, feeds, and beverages
    'A820RZ2Q224SBEA', # Contributions to percent change in real imports of goods: Industrial Supplies and Materials: Durable Goods
    'A649RZ2Q224SBEA', # Contributions to percent change in real imports of goods: Industrial supplies and materials, except petroleum and products (DISCONTINUED)
    'B696RZ2Q224SBEA', # Contributions to percent change in real imports of goods: Industrial supplies and materials, except petroleum and products: Nondurable goods
    'A653RZ2Q224SBEA', # Contributions to percent change in real imports of goods: Other
    'B648RZ2Q224SBEA', # Contributions to percent change in real imports of goods: Petroleum and products
    'B656RZ2Q224SBEA', # Contributions to percent change in real imports of services
    'B752RZ2Q224SBEA', # Contributions to percent change in real imports of services: Direct defense expenditures (DISCONTINUED)
    'B910RZ2Q224SBEA', # Contributions to percent change in real imports of services: Other
    'B909RZ2Q224SBEA', # Contributions to percent change in real imports of services: Other private services (DISCONTINUED)
    'B770RZ2Q224SBEA', # Contributions to percent change in real imports of services: Other transportation (DISCONTINUED)
    'B769RZ2Q224SBEA', # Contributions to percent change in real imports of services: Passenger fares (DISCONTINUED)
    'B908RZ2Q224SBEA', # Contributions to percent change in real imports of services: Royalties and license fees
    'B768RZ2Q224SBEA', # Contributions to percent change in real imports of services: Travel (DISCONTINUED)

]

# Annually (154)
ids_Y = [
    # Imports (154)
    ## % Chg. from Preceding Period (NSA)
    'PB0000041A225NBEA', # Imports of goods: Industrial supplies and materials
    'PB0000071A225NBEA', # Imports of goods: Industrial supplies and materials: Nondurable goods
    'Y807RL1A225NBEA', # Imports of services: Government goods and services n.e.c.
    'Y806RL1A225NBEA', # Imports of services: Other business services
    'Y804RL1A225NBEA', # Imports of services: Transport
    'Y805RL1A225NBEA', # Imports of services: Travel (for all purposes including education)
    'A333RL1A225NBEA', # Real Imports of Durable Goods
    'A255RL1A225NBEA', # Real Imports of Goods
    'A021RL1A158NBEA', # Real Imports of Goods and Services
    'B021RL1A225NBEA', # Real Imports of Goods and Services (DISCONTINUED)
    'B651RL1A225NBEA', # Real Imports of Goods: Automotive Vehicles, Engines, and Parts
    'A650RL1A225NBEA', # Real Imports of Goods: Capital Goods, Except Automotive
    'B932RL1A225NBEA', # Real Imports of Goods: Capital Goods, Except Automotive: Civilian Aircraft, Engines, and Parts
    'B852RL1A225NBEA', # Real Imports of Goods: Capital Goods, Except Automotive: Computers, Peripherals, and Parts
    'B853RL1A225NBEA', # Real Imports of Goods: Capital Goods, Except Automotive: Other
    'A652RL1A225NBEA', # Real Imports of Goods: Consumer Goods, Except Automotive
    'B697RL1A225NBEA', # Real Imports of Goods: Consumer Goods, Except Automotive: Durable Goods
    'B698RL1A225NBEA', # Real Imports of Goods: Consumer Goods, Except Automotive: Nondurable Goods
    'B647RL1A225NBEA', # Real Imports of Goods: Foods, Feeds, and Beverages
    'A649RL1A225NBEA', # Real Imports of Goods: Industrial Supplies and Materials, Except Petroleum and Products (DISCONTINUED)
    'A820RL1A225NBEA', # Real Imports of Goods: Industrial Supplies and Materials, Except Petroleum and Products: Durable Goods
    'B696RL1A225NBEA', # Real Imports of Goods: Industrial Supplies and Materials, Except Petroleum and Products: Nondurable Goods
    'A653RL1A225NBEA', # Real Imports of Goods: Other
    'B648RL1A225NBEA', # Real Imports of Goods: Petroleum and Products
    'A340RL1A225NBEA', # Real Imports of Nondurable Goods
    'A187RL1A225NBEA', # Real Imports of Nonpetroleum Goods
    'A656RL1A225NBEA', # Real Imports of Services
    'B656RL1A225NBEA', # Real Imports of Services (DISCONTINUED)
    'B908RL1A225NBEA', # Real Imports of Services: Charges for the use of intellectual property n.e.c.
    'B910RL1A225NBEA', # Real Imports of Services: Other
    'AB70RL1A225NBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Imports
    'B143RL1A225NBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Imports: Autos
    'B707RL1A225NBEA', # Real Motor Vehicle Output: Final Sales of Domestic Product: Imports: Trucks
    'B149RL1A225NBEA', # Real Motor Vehicle Output: Sales of Imported New Autos
    ## Bil. of $ (NSA)
    'A333RC1A027NBEA', # Current payments to the rest of the world: Imports of durable goods
    'A255RC1A027NBEA', # Current payments to the rest of the world: Imports of goods
    'A340RC1A027NBEA', # Current payments to the rest of the world: Imports of nondurable goods
    'B656RC1A027NBEA', # Current payments to the rest of the world: Imports of services
    'IMPGSA', # Imports of Goods and Services
    'IMPGSNA', # Imports of Goods and Services, GNP-Basis (DISCONTINUED)
    'B1095C1A027NBEA', # Imports of gold, International Transactions Accounts
    'B1091C1A027NBEA', # Imports of gold, NIPAs
    'B1243C1A027NBEA', # Imports of gold: Statistical differences, International Transactions Accounts vs. NIPAs
    'B1231C1A027NBEA', # Imports of goods and services and income payments, International Transactions Accounts
    'A1074C1A027NBEA', # Imports of goods and services and income payments, NIPAs
    'B921RC1A027NBEA', # Imports of goods and services and income payments: Adjustment for U.S. territories and Puerto Rico
    'W370RC1A027NBEA', # Imports of goods and services and income payments: Imputed interest paid to the rest of the world
    'B1092C1A027NBEA', # Imports of goods and services and income payments: Other items
    'B1093C1A027NBEA', # Imports of goods and services and income payments: Statistical differences , International Transactions Accounts vs. NIPAs
    'B1242C1A027NBEA', # Imports of goods, ITAs
    'B1244C1A027NBEA', # Imports of goods: Adjustment for U.S. territories and Puerto Rico
    'B651RC1A027NBEA', # Imports of goods: Automotive vehicles, engines, and parts
    'A650RC1A027NBEA', # Imports of goods: Capital goods, except automotive
    'B932RC1A027NBEA', # Imports of goods: Capital goods, except automotive: Civilian aircraft, engines, and parts
    'B852RC1A027NBEA', # Imports of goods: Capital goods, except automotive: Computers, peripherals, and parts
    'B853RC1A027NBEA', # Imports of goods: Capital goods, except automotive: Other
    'A652RC1A027NBEA', # Imports of goods: Consumer goods, except automotive
    'B697RC1A027NBEA', # Imports of goods: Consumer goods, except automotive: Durable goods
    'B698RC1A027NBEA', # Imports of goods: Consumer goods, except automotive: Nondurable goods
    'B647RC1A027NBEA', # Imports of goods: Foods, feeds, and beverages
    'LA0000041A027NBEA', # Imports of goods: Industrial supplies and materials
    'A649RC1A027NBEA', # Imports of goods: Industrial supplies and materials, except petroleum and products (DISCONTINUED)
    'A820RC1A027NBEA', # Imports of goods: Industrial supplies and materials, except petroleum and products: Durable goods
    'B696RC1A027NBEA', # Imports of goods: Industrial supplies and materials, except petroleum and products: Nondurable goods
    'LA0000071A027NBEA', # Imports of goods: Industrial supplies and materials: Nondurable goods
    'A653RC1A027NBEA', # Imports of goods: Other
    'B648RC1A027NBEA', # Imports of goods: Petroleum and products
    'A187RC1A027NBEA', # Imports of nonpetroleum goods
    'B1245C1A027NBEA', # Imports of services, ITAs
    'B1247C1A027NBEA', # Imports of services: Adjustment for U.S. territories and Puerto Rico
    'B752RC1A027NBEA', # Imports of services: Direct defense expenditures (DISCONTINUED)
    'Y807RC1A027NBEA', # Imports of services: Government goods and services n.e.c.
    'B910RC1A027NBEA', # Imports of services: Other
    'Y806RC1A027NBEA', # Imports of services: Other business services
    'B909RC1A027NBEA', # Imports of services: Other private services (DISCONTINUED)
    'B770RC1A027NBEA', # Imports of services: Other transportation (DISCONTINUED)
    'B769RC1A027NBEA', # Imports of services: Passenger fares (DISCONTINUED)
    'B908RC1A027NBEA', # Imports of services: Royalties and license fees
    'B1246C1A027NBEA', # Imports of services: Statistical differences, International Transactions Accounts vs. NIPAs
    'Y804RC1A027NBEA', # Imports of services: Transport
    'B768RC1A027NBEA', # Imports of services: Travel (DISCONTINUED)
    'Y805RC1A027NBEA', # Imports of services: Travel (for all purposes including education)
    'Y700RC1A027NBEA', # Taxes on Production and Imports: Federal: Excise taxes: Health insurance
    'Y701RC1A027NBEA', # Taxes on Production and Imports: Federal: Excise taxes: Medical devices
    'Y702RC1A027NBEA', # Taxes on Production and Imports: Federal: Excise taxes: Pharmaceutical
    ## Bil. of 1982 $ (NSA)
    'IMPGSCNA', # Real Imports of Goods and Services, GNP-Basis (DISCONTINUED)
    ## Bil. of Chn. 2009 $ (NSA)
    'B021RX1A020NBEA', # Real imports of goods and services (DISCONTINUED)
    'A649RX1A020NBEA', # Real imports of goods: Industrial supplies and materials, except petroleum and products (DISCONTINUED)
    'B752RX1A020NBEA', # Real imports of services: Direct defense expenditures (DISCONTINUED)
    'B909RX1A020NBEA', # Real imports of services: Other private services (DISCONTINUED)
    'B770RX1A020NBEA', # Real imports of services: Other transportation (DISCONTINUED)
    'B769RX1A020NBEA', # Real imports of services: Passenger fares (DISCONTINUED)
    'B768RX1A020NBEA', # Real imports of services: Travel (DISCONTINUED)
    ## Bil. of Chn. 2017 $ (NSA)
    'IMPGSCA', # Real Imports of Goods and Services
    'B852RX1A020NBEA', # Real Imports of goods: Capital goods, except automotive: Computers, peripherals, and parts
    'LB0000041A020NBEA', # Real Imports of goods: Industrial supplies and materials
    'LB0000071A020NBEA', # Real Imports of goods: Industrial supplies and materials: Nondurable goods
    'Y807RX1A020NBEA', # Real Imports of services: Government goods and services n.e.c.
    'Y806RX1A020NBEA', # Real Imports of services: Other business services
    'Y804RX1A020NBEA', # Real Imports of services: Transport
    'Y805RX1A020NBEA', # Real Imports of services: Travel (for all purposes including education)
    'A333RX1A020NBEA', # Real imports of durable goods
    'A255RX1A020NBEA', # Real imports of goods
    'C021RX1A020NBEA', # Real imports of goods and services, command basis
    'A978RX1A020NBEA', # Real imports of goods and services: Residual
    'B651RX1A020NBEA', # Real imports of goods: Automotive vehicles, engines, and parts
    'A650RX1A020NBEA', # Real imports of goods: Capital goods, except automotive
    'B932RX1A020NBEA', # Real imports of goods: Capital goods, except automotive: Civilian aircraft, engines, and parts
    'B853RX1A020NBEA', # Real imports of goods: Capital goods, except automotive: Other
    'A652RX1A020NBEA', # Real imports of goods: Consumer goods, except automotive
    'B697RX1A020NBEA', # Real imports of goods: Consumer goods, except automotive: Durable goods
    'B698RX1A020NBEA', # Real imports of goods: Consumer goods, except automotive: Nondurable goods
    'B647RX1A020NBEA', # Real imports of goods: Foods, feeds, and beverages
    'A820RX1A020NBEA', # Real imports of goods: Industrial supplies and materials, except petroleum and products: Durable goods
    'B696RX1A020NBEA', # Real imports of goods: Industrial supplies and materials, except petroleum and products: Nondurable goods
    'A653RX1A020NBEA', # Real imports of goods: Other
    'B648RX1A020NBEA', # Real imports of goods: Petroleum and products
    'A340RX1A020NBEA', # Real imports of nondurable goods
    'A187RX1A020NBEA', # Real imports of nonpetroleum goods
    'B656RX1A020NBEA', # Real imports of services
    'B910RX1A020NBEA', # Real imports of services: Other
    'B908RX1A020NBEA', # Real imports of services: Royalties and license fees
    ## Percentage Points at Annual Rate (NSA)
    'CB0000042A224NBEA', # Contributions to percent change in Imports of goods and services: Imports of Goods: Industrial supplies and materials
    'CB0000072A224NBEA', # Contributions to percent change in Imports of goods and services: Imports of Goods: Industrial supplies and materials: Nondurable goods
    'Y807RZ2A224NBEA', # Contributions to percent change in Imports of goods and services: Imports of services: Government goods and services n.e.c.
    'Y806RZ2A224NBEA', # Contributions to percent change in Imports of goods and services: Imports of services: Other business services
    'Y804RZ2A224NBEA', # Contributions to percent change in Imports of goods and services: Imports of services: Transport
    'Y805RZ2A224NBEA', # Contributions to percent change in Imports of goods and services: Imports of services: Travel (for all purposes including education)
    'A255RY2A224NBEA', # Contributions to percent change in real gross domestic product: Imports of goods
    'A021RY2A224NBEA', # Contributions to percent change in real gross domestic product: Imports of goods and services
    'A656RY2A224NBEA', # Contributions to percent change in real gross domestic product: Imports of services
    'A255RZ2A224NBEA', # Contributions to percent change in real imports of goods
    'B651RZ2A224NBEA', # Contributions to percent change in real imports of goods: Automotive vehicles, engines, and parts
    'A650RZ2A224NBEA', # Contributions to percent change in real imports of goods: Capital goods, except automotive
    'B932RZ2A224NBEA', # Contributions to percent change in real imports of goods: Capital goods, except automotive: Civilian aircraft, engines, and parts
    'B852RZ2A224NBEA', # Contributions to percent change in real imports of goods: Capital goods, except automotive: Computers, peripherals, and parts
    'B853RZ2A224NBEA', # Contributions to percent change in real imports of goods: Capital goods, except automotive: Other
    'A652RZ2A224NBEA', # Contributions to percent change in real imports of goods: Consumer goods, except automotive
    'B697RZ2A224NBEA', # Contributions to percent change in real imports of goods: Consumer goods, except automotive: Durable goods
    'B698RZ2A224NBEA', # Contributions to percent change in real imports of goods: Consumer goods, except automotive: Nondurable goods
    'B647RZ2A224NBEA', # Contributions to percent change in real imports of goods: Foods, feeds, and beverages
    'A649RZ2A224NBEA', # Contributions to percent change in real imports of goods: Industrial supplies and materials, except petroleum and products (DISCONTINUED)
    'A820RZ2A224NBEA', # Contributions to percent change in real imports of goods: Industrial supplies and materials, except petroleum and products: Durable goods
    'B696RZ2A224NBEA', # Contributions to percent change in real imports of goods: Industrial supplies and materials, except petroleum and products: Nondurable goods
    'A653RZ2A224NBEA', # Contributions to percent change in real imports of goods: Other
    'B648RZ2A224NBEA', # Contributions to percent change in real imports of goods: Petroleum and products
    'B656RZ2A224NBEA', # Contributions to percent change in real imports of services
    'B752RZ2A224NBEA', # Contributions to percent change in real imports of services: Direct defense expenditures (DISCONTINUED)
    'B910RZ2A224NBEA', # Contributions to percent change in real imports of services: Other
    'B909RZ2A224NBEA', # Contributions to percent change in real imports of services: Other private services (DISCONTINUED)
    'B770RZ2A224NBEA', # Contributions to percent change in real imports of services: Other transportation (DISCONTINUED)
    'B769RZ2A224NBEA', # Contributions to percent change in real imports of services: Passenger fares (DISCONTINUED)
    'B908RZ2A224NBEA', # Contributions to percent change in real imports of services: Royalties and license fees
    'B768RZ2A224NBEA', # Contributions to percent change in real imports of services: Travel (DISCONTINUED)

]
