# FRED > National Accounts > National Income & Product Accounts > Domestic Capital Account (Saving & Investment) (category_id 112)
# https://fred.stlouisfed.org/categories/112  하위 카테고리 + 직속 시리즈 전체. 주기는 FRED 메타데이터 기준
# 위계: # 카테고리 > ## 단위 (계절조정)
dir='us_macro_NIPA_Domestic_Capital_Account'
category_ids = [112]  # build_db.py가 이 카테고리(하위 포함) 메타데이터를 일괄 조회

# Monthly (2)
ids_M = [
    # Domestic Capital Account (Saving & Investment) (2)
    ## % (SAAR)
    'PSAVERT', # Personal Saving Rate
    ## Bil. of $ (SAAR)
    'PMSAVE', # Personal Saving

]

# Quarterly (560)
ids_Q = [
    # Domestic Capital Account (Saving & Investment) (64)
    ## % (SAAR)
    'W206RC1Q156SBEA', # Gross saving as a percentage of gross national income
    'W207RC1Q156SBEA', # Net saving as a percentage of gross national income
    ## Bil. of $ (SAAR)
    'B029RC1Q027SBEA', # Business current transfer payments (net)
    'W991RC1Q027SBEA', # Capital account transactions (net): Government
    'W992RC1Q027SBEA', # Capital account transactions (net): Government: Federal
    'W993RC1Q027SBEA', # Capital account transactions (net): Government: State and local
    'W999RC1Q027SBEA', # Capital account transactions (net): Private
    'W989RC1Q027SBEA', # Capital account transactions (net): Private: Domestic business
    'W990RC1Q027SBEA', # Capital account transactions (net): Private: Households and institutions
    'Y0004C1Q027SBEA', # Consumption of fixed capital: Private: Domestic business: Capital consumption adjustment
    'FPI', # Fixed Private Investment
    'GGSAVE', # Gross Government Saving
    'GPDI', # Gross Private Domestic Investment
    'GPSAVE', # Gross Private Saving
    'GSAVE', # Gross Saving
    'W997RC1Q027SBEA', # Gross private saving: Domestic business
    'W998RC1Q027SBEA', # Gross private saving: Households and institutions
    'A358RC1Q027SBEA', # Gross value added: GDP: Business: Nonfarm
    'W061RC1Q027SBEA', # National income: Business current transfer payments (net): to government (net)
    'W237RC1Q027SBEA', # National income: Business current transfer payments (net): to the rest of the world (net)
    'B050RC1Q027SBEA', # National income: Rental income of persons with CCAdj
    'A030RC1Q027SBEA', # Net lending or net borrowing (-), NIPAs: Government: Statistical discrepancy
    'W994RC1Q027SBEA', # Net lending or net borrowing (-), NIPAs: Private
    'W995RC1Q027SBEA', # Net lending or net borrowing (-), NIPAs: Private: Domestic business
    'W996RC1Q027SBEA', # Net lending or net borrowing (-), NIPAs: Private: Households and institutions
    'W202RC1Q027SBEA', # Net private saving
    'A127RC1Q027SBEA', # Net private saving: Domestic business
    'W986RC1Q027SBEA', # Net private saving: Households and institutions
    'W201RC1Q027SBEA', # Net saving
    'PSAVE', # Personal Saving
    'PNFI', # Private Nonresidential Fixed Investment
    'PRFI', # Private Residential Fixed Investment
    'B010RC1Q027SBEA', # Private fixed investment: Nonresidential: Equipment and software (DISCONTINUED)
    'B009RC1Q027SBEA', # Private fixed investment: Nonresidential: Structures
    'W771RC1Q027SBEA', # Saving and investment: Disaster losses
    'W772RC1Q027SBEA', # Saving and investment: Disaster losses: Private
    'W773RC1Q027SBEA', # Saving and investment: Disaster losses: Private: Domestic business
    'W774RC1Q027SBEA', # Saving and investment: Disaster losses: Private: Households and institutions
    ## Bil. of Chn. 2005 $ (SAAR)
    'NRIPDC1', # Real Nonresidential Investment: Equipment and Software, 1 Decimal (DISCONTINUED)
    'NRIPDC96', # Real Nonresidential Investment: Equipment and Software, 3 Decimal (DISCONTINUED)
    ## Bil. of Chn. 2009 $ (SAAR)
    'GPDIC96', # Real Gross Private Domestic Investment (DISCONTINUED)
    'FPIC96', # Real Private Fixed Investment (DISCONTINUED)
    'PNFIC96', # Real Private Nonresidential Fixed Investment (DISCONTINUED)
    'PRFIC96', # Real Private Residential Fixed Investment (DISCONTINUED)
    ## Bil. of Chn. 2017 $ (NSA)
    'ND000335Q', # Real Gross Private Domestic Investment
    ## Bil. of Chn. 2017 $ (SAAR)
    'GPDIC1', # Real Gross Private Domestic Investment
    'FPIC1', # Real Private Fixed Investment
    'PNFIC1', # Real Private Nonresidential Fixed Investment
    'PRFIC1', # Real Private Residential Fixed Investment
    'N456RX1Q027SBEA', # Real gross value added of nonfinancial corporate business: Consumption of fixed capital
    'A195RX1Q020SBEA', # Real gross value added: GDP: Business
    'B359RX1Q020SBEA', # Real gross value added: GDP: Business: Farm
    'A358RX1Q020SBEA', # Real gross value added: GDP: Business: Nonfarm
    ## Index 2017=100 (NSA)
    'NC000335Q', # Gross Private Domestic Investment
    'NC000336Q', # Private Nonresidential Fixed Investment
    'NC000338Q', # Private Residential Investment
    'NB000335Q', # Real Gross Private Domestic Investment
    'NB000336Q', # Real Private Nonresidential Fixed Investment
    'NB000338Q', # Real Private Residential Investment
    ## Mil. of $ (NSA)
    'NA000250Q', # Business current transfer payments (net)
    'NA000335Q', # Gross Private Domestic Investment
    'NA000258Q', # Net lending or net borrowing (-), NIPAs: Government: Statistical discrepancy
    'NA000336Q', # Private Nonresidential Fixed Investment
    'NA000338Q', # Private Residential Investment

    # Domestic Capital Account (Saving & Investment) > Capital Transfers Paid (4)
    ## Bil. of $ (NSA)
    'L318301Q027NBEA', # Federal government cash payments to the public: Coverage differences: Capital transfers paid (DISCONTINUED)
    'M318301Q027NBEA', # Federal government expenditures: Coverage differences: Capital transfers paid (NIPA vs. Budget)
    ## Bil. of $ (SAAR)
    'B232RC1Q027SBEA', # Federal government capital transfer receipts
    'W976RC1Q027SBEA', # National income: Corporate cash flow: Net cash flow with IVA: Capital transfers paid (net)

    # Domestic Capital Account (Saving & Investment) > Capital Transfers Received (10)
    ## Bil. of $ (NSA)
    'M318521Q027NBEA', # Federal government budget: Net capital transfers received
    'L318471Q027NBEA', # Federal government budget: Net capital transfers received (DISCONTINUED)
    'L318491Q027NBEA', # Federal government budget: Net capital transfers received : Other coverage differences (DISCONTINUED)
    'M318531Q027NBEA', # Federal government budget: Net capital transfers received: Federal employee retirement plans
    'L318481Q027NBEA', # Federal government budget: Net capital transfers received: Federal employee retirement plans (DISCONTINUED)
    'M318541Q027NBEA', # Federal government budget: Net capital transfers received: Other coverage differences (NIPA vs. Budget)
    'L318501Q027NBEA', # Federal government budget: Net capital transfers received: Timing differences (DISCONTINUED)
    'M318551Q027NBEA', # Federal government budget: Net capital transfers received: Timing differences (NIPA vs. Budget)
    'L318051Q027NBEA', # Federal government cash receipts from the public: Coverage differences: Capital transfers received (DISCONTINUED)
    'M318051Q027NBEA', # Federal government receipts: Coverage differences: Capital transfers received (NIPA vs. Budget)

    # Domestic Capital Account (Saving & Investment) > Consumptions of Fixed Capital (36)
    ## Bil. of $ (NSA)
    'A918RU1Q027NBEA', # Federal government consumption of fixed capital (DISCONTINUED)
    'A919RU1Q027NBEA', # State and local government consumption of fixed capital (DISCONTINUED)
    ## Bil. of $ (SAAR)
    'A265RC1Q027SBEA', # Consumption of fixed capital: General government
    'B995RC1Q027SBEA', # Consumption of fixed capital: General government: Federal
    'B986RC1Q027SBEA', # Consumption of fixed capital: General government: State and local
    'A264RC1Q027SBEA', # Consumption of fixed capital: Government
    'A266RC1Q027SBEA', # Consumption of fixed capital: Government enterprises
    'B833RC1Q027SBEA', # Consumption of fixed capital: Government enterprises: Federal
    'B846RC1Q027SBEA', # Consumption of fixed capital: Government enterprises: State and local
    'A918RC1Q027SBEA', # Consumption of fixed capital: Government: Federal
    'A919RC1Q027SBEA', # Consumption of fixed capital: Government: State and local
    'B1667C1Q027SBEA', # Consumption of fixed capital: Nonfarm business
    'A024RC1Q027SBEA', # Consumption of fixed capital: Private
    'W276RC1Q027SBEA', # Consumption of fixed capital: Private: Domestic business
    'Y0000C1Q027SBEA', # Consumption of fixed capital: Private: Domestic business: Capital consumption allowances
    'B580RC1Q027SBEA', # Consumption of fixed capital: Private: Domestic: Corporate business: Financial
    'B456RC1Q027SBEA', # Consumption of fixed capital: Private: Domestic: Corporate business: Nonfinancial
    'W277RC1Q027SBEA', # Consumption of fixed capital: Private: Domestic: Noncorporate business
    'B1619C1Q027SBEA', # Consumption of fixed capital: Private: Domestic: Noncorporate business: Proprietors' income
    'B1620C1Q027SBEA', # Consumption of fixed capital: Private: Domestic: Noncorporate business: Rental income of persons
    'A1618C1Q027SBEA', # Consumption of fixed capital: Private: Domestic: Noncorporate business: Rental income of persons and proprietors' income
    'A1615C1Q027SBEA', # Consumption of fixed capital: Private: Domestic: Noncorporate business: Sole proprietorships and partnerships
    'B1616C1Q027SBEA', # Consumption of fixed capital: Private: Domestic: Noncorporate business: Sole proprietorships and partnerships: Farm
    'B1617C1Q027SBEA', # Consumption of fixed capital: Private: Domestic: Noncorporate business: Sole proprietorships and partnerships: Nonfarm
    'W279RC1Q027SBEA', # Consumption of fixed capital: Private: Households and institutions
    'B1621C1Q027SBEA', # Consumption of fixed capital: Private: Households and institutions: Nonprofit institutions serving households
    'B2607C1Q027SBEA', # Consumption of fixed capital: Private: Households and institutions: Owner-occupied housing
    ## Bil. of Chn. 2017 $ (SAAR)
    'A262RX1Q020SBEA', # Real consumption of fixed capital
    'A265RX1Q020SBEA', # Real consumption of fixed capital: General government
    'A264RX1Q020SBEA', # Real consumption of fixed capital: Government
    'A266RX1Q020SBEA', # Real consumption of fixed capital: Government: Government enterprises
    'A024RX1Q020SBEA', # Real consumption of fixed capital: Private
    ## Mil. of $ (NSA)
    'NA000255Q', # Consumption of fixed capital: Government
    'NA000281Q', # Consumption of fixed capital: Government: Federal
    'NA000282Q', # Consumption of fixed capital: Government: State and local
    'NA000257Q', # Consumption of fixed capital: Private

    # Domestic Capital Account (Saving & Investment) > Domestic Investments (65)
    ## % Chg. at Annual Rate (SAAR)
    'GDPINOW', # Nowcast for Real Gross Private Domestic Investment
    'FIXINVESTNOW', # Nowcast for Real Gross Private Domestic Investment: Fixed Investment
    'BUSFIXINVESTNOW', # Nowcast for Real Gross Private Domestic Investment: Fixed Investment: Business
    'EQUIPNOW', # Nowcast for Real Gross Private Domestic Investment: Fixed Investment: Business: Equipment
    'IPPNOW', # Nowcast for Real Gross Private Domestic Investment: Fixed Investment: Business: Intellectual Property Products
    'STRUCTNOW', # Nowcast for Real Gross Private Domestic Investment: Fixed Investment: Business: Structures
    'RESNOW', # Nowcast for Real Gross Private Domestic Investment: Fixed Investment: Residential
    ## % Chg. from Preceding Period (SAAR)
    'A006RL1Q225SBEA', # Real Gross Private Domestic Investment
    ## % Chg. from Qtr.  1 Yr. Ago (NSA)
    'OB000335Q', # Real Gross Private Domestic Investment
    'OB000339Q', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Structures
    ## % Chg. from Qtr.  1 Yr. Ago (SA)
    'B006RO1Q156NBEA', # Real Gross Private Domestic Investment
    ## Bil. of $ (SAAR)
    'W170RC1Q027SBEA', # Gross domestic investment
    'A928RC1Q027SBEA', # Gross domestic investment, capital account transactions, and net lending, NIPAs
    'W987RC1Q027SBEA', # Gross private domestic investment: Domestic business
    'W988RC1Q027SBEA', # Gross private domestic investment: Households and institutions
    'W171RC1Q027SBEA', # Net domestic investment
    'A889RC1Q027SBEA', # Net domestic investment: Government
    'A890RC1Q027SBEA', # Net domestic investment: Government: Federal
    'A893RC1Q027SBEA', # Net domestic investment: Government: State and local
    'A557RC1Q027SBEA', # Net domestic investment: Private
    'W790RC1Q027SBEA', # Net domestic investment: Private: Domestic business
    'W791RC1Q027SBEA', # Net domestic investment: Private: Households and institutions
    ## Bil. of Chn. 2017 $ (SAAR)
    'A680RX1Q020SBEA', # Real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Industrial equipment
    'A937RX1Q020SBEA', # Real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Information processing equipment: Other
    'A862RX1Q020SBEA', # Real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Other equipment
    'A681RX1Q020SBEA', # Real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Transportation equipment
    'B985RX1Q020SBEA', # Real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Intellectual property products: Software
    'A679RX1Q020SBEA', # Real gross private domestic investment: Fixed investment: Nonresidential: Information processing equipment and software
    'B009RX1Q020SBEA', # Real gross private domestic investment: Fixed investment: Nonresidential: Structures
    'W256RX1Q020SBEA', # Real net domestic income
    'A362RX1Q020SBEA', # Real net domestic product
    'W367RX1Q020SBEA', # Real net domestic purchases
    ## Percentage Points (SA)
    'GDPICONTRIBNOW', # Contributions to percent change in GDPNow: Real Gross Private Domestic Investment
    'FIXINVESTCONTRIBNOW', # Contributions to percent change in GDPNow: Real Gross Private Domestic Investment: Fixed Investment
    'BUSFIXINVESTCONTRIBNOW', # Contributions to percent change in GDPNow: Real Gross Private Domestic Investment: Fixed Investment: Business
    'EQUIPCONTRIBNOW', # Contributions to percent change in GDPNow: Real Gross Private Domestic Investment: Fixed Investment: Business: Equipment
    'IPPCONTRIBNOW', # Contributions to percent change in GDPNow: Real Gross Private Domestic Investment: Fixed Investment: Business: Intellectual Property Products
    'STRUCTCONTRIBNOW', # Contributions to percent change in GDPNow: Real Gross Private Domestic Investment: Fixed Investment: Business: Structures
    'RESCONTRIBNOW', # Contributions to percent change in GDPNow: Real Gross Private Domestic Investment: Fixed Investment: Residential
    ## Percentage Points at Annual Rate (SAAR)
    'A006RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment
    'A007RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Fixed investment
    'A008RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Fixed investment: Nonresidential
    'A010RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Fixed investment: Nonresidential: Equipment and software (DISCONTINUED)
    'A680RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Industrial equipment
    'B935RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Information processing equipment: Computers and peripheral equipment
    'A937RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Information processing equipment: Other
    'A862RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Other equipment
    'A681RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Transportation equipment
    'A679RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Fixed investment: Nonresidential: Information processing equipment and software (DISCONTINUED)
    'B985RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Fixed investment: Nonresidential: Intellectual property products: Software
    'A009RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Fixed investment: Nonresidential: Structures
    'A011RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Fixed investment: Residential
    'A006RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment
    'A007RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Fixed investment
    'A008RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential
    'A010RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Equipment and software (DISCONTINUED)
    'A680RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Industrial equipment
    'B935RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Information processing equipment: Computers and peripheral equipment
    'A937RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Information processing equipment: Other
    'A862RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Other equipment
    'A681RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Transportation equipment
    'A679RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Information processing equipment and software (DISCONTINUED)
    'B985RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Intellectual property products: Software
    'A009RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Structures
    'A011RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Fixed investment: Residential

    # Domestic Capital Account (Saving & Investment) > Inventories (217)
    ## % (SA)
    'A812RC2Q027SBEA', # Ratios of nonfarm inventories to final sales of domestic business
    'A813RC2Q027SBEA', # Ratios of nonfarm inventories to final sales of goods and structures
    'A811RC2Q027SBEA', # Ratios of private inventories to final sales of domestic business
    ## Bil. of $ (SA)
    'A371RC1Q027SBEA', # Private inventories
    'N241RC1Q027SBEA', # Private inventories: Durable goods industries
    'B372RC1Q027SBEA', # Private inventories: Farm
    'N376RC1Q027SBEA', # Private inventories: Manufacturing
    'N377RC1Q027SBEA', # Private inventories: Manufacturing: Durable goods industries
    'N378RC1Q027SBEA', # Private inventories: Manufacturing: Nondurable goods industries
    'N802RC1Q027SBEA', # Private inventories: Merchant wholesale trade
    'N803RC1Q027SBEA', # Private inventories: Merchant wholesale trade: Durable goods industries
    'N804RC1Q027SBEA', # Private inventories: Merchant wholesale trade: Nondurable goods industries
    'N238RC1Q027SBEA', # Private inventories: Mining, utilities, and construction
    'N242RC1Q027SBEA', # Private inventories: Nondurable goods industries
    'A373RC1Q027SBEA', # Private inventories: Nonfarm
    'A374RC1Q027SBEA', # Private inventories: Nonfarm: Durable goods
    'A376RC1Q027SBEA', # Private inventories: Nonfarm: Manufacturing
    'B377RC1Q027SBEA', # Private inventories: Nonfarm: Manufacturing: Durable goods
    'B378RC1Q027SBEA', # Private inventories: Nonfarm: Manufacturing: Nondurable goods
    'A375RC1Q027SBEA', # Private inventories: Nonfarm: Nondurable goods
    'A385RC1Q027SBEA', # Private inventories: Nonfarm: Other durable and nondurable goods
    'B386RC1Q027SBEA', # Private inventories: Nonfarm: Other: Durable goods
    'B387RC1Q027SBEA', # Private inventories: Nonfarm: Other: Nondurable goods
    'A382RC1Q027SBEA', # Private inventories: Nonfarm: Retail trade
    'B383RC1Q027SBEA', # Private inventories: Nonfarm: Retail trade: Durable goods
    'B864RC1Q027SBEA', # Private inventories: Nonfarm: Retail trade: Durable goods: Motor vehicle dealers
    'A865RC1Q027SBEA', # Private inventories: Nonfarm: Retail trade: Durable goods: Other
    'B384RC1Q027SBEA', # Private inventories: Nonfarm: Retail trade: Nondurable goods
    'A379RC1Q027SBEA', # Private inventories: Nonfarm: Wholesale trade
    'A380RC1Q027SBEA', # Private inventories: Nonfarm: Wholesale trade: Durable goods
    'B803RC1Q027SBEA', # Private inventories: Nonfarm: Wholesale trade: Merchant wholesalers: Durable goods
    'B804RC1Q027SBEA', # Private inventories: Nonfarm: Wholesale trade: Merchant wholesalers: Nondurable goods
    'A381RC1Q027SBEA', # Private inventories: Nonfarm: Wholesale trade: Nondurable goods
    'A802RC1Q027SBEA', # Private inventories: Nonfarm: Wholesale trade: Nondurable goods: Merchant wholesalers
    'A805RC1Q027SBEA', # Private inventories: Nonfarm: Wholesale trade: Nondurable goods: Nonmerchant wholesalers
    'B806RC1Q027SBEA', # Private inventories: Nonfarm: Wholesale trade: Nonmerchant wholesalers: Durable goods
    'B807RC1Q027SBEA', # Private inventories: Nonfarm: Wholesale trade: Nonmerchant wholesalers: Nondurable goods
    'N805RC1Q027SBEA', # Private inventories: Nonmerchant wholesale trade
    'N385RC1Q027SBEA', # Private inventories: Other industries
    'N382RC1Q027SBEA', # Private inventories: Retail trade
    'N239RC1Q027SBEA', # Private inventories: Retail trade: Food and beverage stores
    'N240RC1Q027SBEA', # Private inventories: Retail trade: General merchandise stores
    'N864RC1Q027SBEA', # Private inventories: Retail trade: Motor vehicle and parts dealers
    'N865RC1Q027SBEA', # Private inventories: Retail trade: Other retail stores
    'N379RC1Q027SBEA', # Private inventories: Wholesale trade
    'N380RC1Q027SBEA', # Private inventories: Wholesale trade: Durable goods industries
    'N381RC1Q027SBEA', # Private inventories: Wholesale trade: Nondurable goods industries
    ## Bil. of $ (SAAR)
    'A145RC1Q027SBEA', # Automobile output: Change in private inventories of new and used autos
    'B146RC1Q027SBEA', # Automobile output: Change in private inventories of new autos
    'B147RC1Q027SBEA', # Automobile output: Change in private inventories of used autos
    'N355RC1Q027SBEA', # Change in private inventories: Durable goods industries
    'B018RC1Q027SBEA', # Change in private inventories: Farm
    'N150RC1Q027SBEA', # Change in private inventories: Manufacturing
    'N624RC1Q027SBEA', # Change in private inventories: Manufacturing: Durable goods industries
    'N625RC1Q027SBEA', # Change in private inventories: Manufacturing: Nondurable goods industries
    'N151RC1Q027SBEA', # Change in private inventories: Merchant wholesale trade
    'N626RC1Q027SBEA', # Change in private inventories: Merchant wholesale trade: Durable goods industries
    'N627RC1Q027SBEA', # Change in private inventories: Merchant wholesale trade: Nondurable goods industries
    'N541RC1Q027SBEA', # Change in private inventories: Mining, utilities, and construction
    'N357RC1Q027SBEA', # Change in private inventories: Nondurable goods industries
    'A015RC1Q027SBEA', # Change in private inventories: Nonfarm
    'B016RC1Q027SBEA', # Change in private inventories: Nonfarm: Change in book value
    'B017RC1Q027SBEA', # Change in private inventories: Nonfarm: Inventory valuation adjustment
    'A150RC1Q027SBEA', # Change in private inventories: Nonfarm: Manufacturing
    'A624RC1Q027SBEA', # Change in private inventories: Nonfarm: Manufacturing: Durable goods
    'A625RC1Q027SBEA', # Change in private inventories: Nonfarm: Manufacturing: Nondurable goods
    'A154RC1Q027SBEA', # Change in private inventories: Nonfarm: Other durable and nondurable goods
    'A636RC1Q027SBEA', # Change in private inventories: Nonfarm: Other: Durable goods
    'A637RC1Q027SBEA', # Change in private inventories: Nonfarm: Other: Nondurable goods
    'A153RC1Q027SBEA', # Change in private inventories: Nonfarm: Retail trade
    'A630RC1Q027SBEA', # Change in private inventories: Nonfarm: Retail trade: Durable goods
    'A631RC1Q027SBEA', # Change in private inventories: Nonfarm: Retail trade: Durable goods: Motor vehicle dealers
    'A632RC1Q027SBEA', # Change in private inventories: Nonfarm: Retail trade: Durable goods: Other
    'A633RC1Q027SBEA', # Change in private inventories: Nonfarm: Retail trade: Nondurable goods
    'A658RC1Q027SBEA', # Change in private inventories: Nonfarm: Wholesale trade
    'A661RC1Q027SBEA', # Change in private inventories: Nonfarm: Wholesale trade: Durable goods
    'A626RC1Q027SBEA', # Change in private inventories: Nonfarm: Wholesale trade: Merchant wholesalers: Durable goods
    'A627RC1Q027SBEA', # Change in private inventories: Nonfarm: Wholesale trade: Merchant wholesalers: Nondurable goods
    'A664RC1Q027SBEA', # Change in private inventories: Nonfarm: Wholesale trade: Nondurable goods
    'A151RC1Q027SBEA', # Change in private inventories: Nonfarm: Wholesale trade: Nondurable goods: Merchant wholesalers
    'A152RC1Q027SBEA', # Change in private inventories: Nonfarm: Wholesale trade: Nondurable goods: Nonmerchant wholesalers
    'A628RC1Q027SBEA', # Change in private inventories: Nonfarm: Wholesale trade: Nonmerchant wholesalers: Durable goods
    'A629RC1Q027SBEA', # Change in private inventories: Nonfarm: Wholesale trade: Nonmerchant wholesalers: Nondurable goods
    'N152RC1Q027SBEA', # Change in private inventories: Nonmerchant wholesale trade
    'N154RC1Q027SBEA', # Change in private inventories: Other industries
    'N153RC1Q027SBEA', # Change in private inventories: Retail trade
    'N542RC1Q027SBEA', # Change in private inventories: Retail trade: Food and beverage stores
    'N543RC1Q027SBEA', # Change in private inventories: Retail trade: General merchandise stores
    'N631RC1Q027SBEA', # Change in private inventories: Retail trade: Motor vehicle and parts dealers
    'N558RC1Q027SBEA', # Change in private inventories: Retail trade: Other retail stores
    'N658RC1Q027SBEA', # Change in private inventories: Wholesale trade
    'N661RC1Q027SBEA', # Change in private inventories: Wholesale trade: Durable goods industries
    'N664RC1Q027SBEA', # Change in private inventories: Wholesale trade: Nondurable goods industries
    'A355RC1Q027SBEA', # Gross domestic product: Durable goods: Change in private inventories
    'A357RC1Q027SBEA', # Gross domestic product: Nondurable goods: Change in private inventories
    'AB65RC1Q027SBEA', # Motor vehicle output: Change in private inventories
    'AB71RC1Q027SBEA', # Motor vehicle output: Change in private inventories: Autos: New: Domestic
    'AB72RC1Q027SBEA', # Motor vehicle output: Change in private inventories: Autos: New: Foreign
    'B709RC1Q027SBEA', # Motor vehicle output: Change in private inventories: Trucks
    'W244RC1Q027SBEA', # Motor vehicle output: Change in private inventories: Trucks: New
    'AB73RC1Q027SBEA', # Motor vehicle output: Change in private inventories: Trucks: New: Domestic
    'AB74RC1Q027SBEA', # Motor vehicle output: Change in private inventories: Trucks: New: Foreign
    'W245RC1Q027SBEA', # Motor vehicle output: Change in private inventories: Trucks: Used
    ## Bil. of Chn. 2009 $ (SAAR)
    'B015RX1Q020SBEA', # Change in real private inventories: Nonfarm (DISCONTINUED)
    ## Bil. of Chn. 2012 $ (SAAR)
    'CHNGNETINVENTNOW', # Nowcast for Real Change of Inventory Investment
    ## Bil. of Chn. 2017 $ (NSA)
    'ND000373Q', # Change in Real Private Inventories
    ## Bil. of Chn. 2017 $ (SA)
    'A371RX1Q020SBEA', # Real private inventories
    'N241RX1Q020SBEA', # Real private inventories: Durable goods industries
    'B372RX1Q020SBEA', # Real private inventories: Farm
    'N376RX1Q020SBEA', # Real private inventories: Manufacturing
    'N377RX1Q020SBEA', # Real private inventories: Manufacturing: Durable goods industries
    'N378RX1Q020SBEA', # Real private inventories: Manufacturing: Nondurable goods industries
    'N802RX1Q020SBEA', # Real private inventories: Merchant wholesale trade
    'N803RX1Q020SBEA', # Real private inventories: Merchant wholesale trade: Durable goods industries
    'N804RX1Q020SBEA', # Real private inventories: Merchant wholesale trade: Nondurable goods industries
    'N238RX1Q020SBEA', # Real private inventories: Mining, utilities, and construction
    'N242RX1Q020SBEA', # Real private inventories: Nondurable goods industries
    'A373RX1Q020SBEA', # Real private inventories: Nonfarm
    'A374RX1Q020SBEA', # Real private inventories: Nonfarm: Durable goods
    'A376RX1Q020SBEA', # Real private inventories: Nonfarm: Manufacturing
    'B377RX1Q020SBEA', # Real private inventories: Nonfarm: Manufacturing: Durable goods
    'B378RX1Q020SBEA', # Real private inventories: Nonfarm: Manufacturing: Nondurable goods
    'A375RX1Q020SBEA', # Real private inventories: Nonfarm: Nondurable goods
    'A385RX1Q020SBEA', # Real private inventories: Nonfarm: Other durable and nondurable goods
    'B386RX1Q020SBEA', # Real private inventories: Nonfarm: Other: Durable goods
    'B387RX1Q020SBEA', # Real private inventories: Nonfarm: Other: Nondurable goods
    'A382RX1Q020SBEA', # Real private inventories: Nonfarm: Retail trade
    'B383RX1Q020SBEA', # Real private inventories: Nonfarm: Retail trade: Durable goods
    'B864RX1Q020SBEA', # Real private inventories: Nonfarm: Retail trade: Durable goods: Motor vehicle dealers
    'A865RX1Q020SBEA', # Real private inventories: Nonfarm: Retail trade: Durable goods: Other
    'B384RX1Q020SBEA', # Real private inventories: Nonfarm: Retail trade: Nondurable goods
    'A379RX1Q020SBEA', # Real private inventories: Nonfarm: Wholesale trade
    'A380RX1Q020SBEA', # Real private inventories: Nonfarm: Wholesale trade: Durable goods
    'B803RX1Q020SBEA', # Real private inventories: Nonfarm: Wholesale trade: Merchant wholesalers: Durable goods
    'B804RX1Q020SBEA', # Real private inventories: Nonfarm: Wholesale trade: Merchant wholesalers: Nondurable goods
    'A381RX1Q020SBEA', # Real private inventories: Nonfarm: Wholesale trade: Nondurable goods
    'A802RX1Q020SBEA', # Real private inventories: Nonfarm: Wholesale trade: Nondurable goods: Merchant wholesalers
    'A805RX1Q020SBEA', # Real private inventories: Nonfarm: Wholesale trade: Nondurable goods: Nonmerchant wholesalers
    'B806RX1Q020SBEA', # Real private inventories: Nonfarm: Wholesale trade: Nonmerchant wholesalers: Durable goods
    'B807RX1Q020SBEA', # Real private inventories: Nonfarm: Wholesale trade: Nonmerchant wholesalers: Nondurable goods
    'N805RX1Q020SBEA', # Real private inventories: Nonmerchant wholesale trade
    'N385RX1Q020SBEA', # Real private inventories: Other industries
    'A968RX1Q020SBEA', # Real private inventories: Residual
    'N968RX1Q020SBEA', # Real private inventories: Residual
    'N382RX1Q020SBEA', # Real private inventories: Retail trade
    'N239RX1Q020SBEA', # Real private inventories: Retail trade: Food and beverage stores
    'N240RX1Q020SBEA', # Real private inventories: Retail trade: General merchandise stores
    'N864RX1Q020SBEA', # Real private inventories: Retail trade: Motor vehicle and parts dealers
    'N865RX1Q020SBEA', # Real private inventories: Retail trade: Other retail stores
    'N379RX1Q020SBEA', # Real private inventories: Wholesale trade
    'N380RX1Q020SBEA', # Real private inventories: Wholesale trade: Durable goods industries
    'N381RX1Q020SBEA', # Real private inventories: Wholesale trade: Nondurable goods industries
    ## Bil. of Chn. 2017 $ (SAAR)
    'N355RX1Q020SBEA', # Change in private inventories: Durable goods industries
    'B018RX1Q020SBEA', # Change in real private inventories: Farm
    'N150RX1Q020SBEA', # Change in real private inventories: Manufacturing
    'N624RX1Q020SBEA', # Change in real private inventories: Manufacturing: Durable goods industries
    'N625RX1Q020SBEA', # Change in real private inventories: Manufacturing: Nondurable goods industries
    'N151RX1Q020SBEA', # Change in real private inventories: Merchant wholesale trade
    'N626RX1Q020SBEA', # Change in real private inventories: Merchant wholesale trade: Durable goods industries
    'N627RX1Q020SBEA', # Change in real private inventories: Merchant wholesale trade: Nondurable goods industries
    'N541RX1Q020SBEA', # Change in real private inventories: Mining, utilities, and construction
    'N357RX1Q020SBEA', # Change in real private inventories: Nondurable goods industries
    'A150RX1Q020SBEA', # Change in real private inventories: Nonfarm: Manufacturing
    'C624RX1Q020SBEA', # Change in real private inventories: Nonfarm: Manufacturing: Durable goods
    'C625RX1Q020SBEA', # Change in real private inventories: Nonfarm: Manufacturing: Nondurable goods
    'A154RX1Q020SBEA', # Change in real private inventories: Nonfarm: Other durable and nondurable goods
    'C636RX1Q020SBEA', # Change in real private inventories: Nonfarm: Other: Durable goods
    'C637RX1Q020SBEA', # Change in real private inventories: Nonfarm: Other: Nondurable goods
    'A153RX1Q020SBEA', # Change in real private inventories: Nonfarm: Retail trade
    'C630RX1Q020SBEA', # Change in real private inventories: Nonfarm: Retail trade: Durable goods
    'C631RX1Q020SBEA', # Change in real private inventories: Nonfarm: Retail trade: Durable goods: Motor vehicle dealers
    'A632RX1Q020SBEA', # Change in real private inventories: Nonfarm: Retail trade: Durable goods: Other
    'C633RX1Q020SBEA', # Change in real private inventories: Nonfarm: Retail trade: Nondurable goods
    'A658RX1Q020SBEA', # Change in real private inventories: Nonfarm: Wholesale trade
    'A661RX1Q020SBEA', # Change in real private inventories: Nonfarm: Wholesale trade: Durable goods
    'C626RX1Q020SBEA', # Change in real private inventories: Nonfarm: Wholesale trade: Merchant wholesalers: Durable goods
    'C627RX1Q020SBEA', # Change in real private inventories: Nonfarm: Wholesale trade: Merchant wholesalers: Nondurable goods
    'A664RX1Q020SBEA', # Change in real private inventories: Nonfarm: Wholesale trade: Nondurable goods
    'A151RX1Q020SBEA', # Change in real private inventories: Nonfarm: Wholesale trade: Nondurable goods: Merchant wholesalers
    'A152RX1Q020SBEA', # Change in real private inventories: Nonfarm: Wholesale trade: Nonmerchant wholesalers
    'C628RX1Q020SBEA', # Change in real private inventories: Nonfarm: Wholesale trade: Nonmerchant wholesalers: Durable goods
    'C629RX1Q020SBEA', # Change in real private inventories: Nonfarm: Wholesale trade: Nonmerchant wholesalers: Nondurable goods
    'N152RX1Q020SBEA', # Change in real private inventories: Nonmerchant wholesale trade
    'N154RX1Q020SBEA', # Change in real private inventories: Other industries
    'A969RX1Q020SBEA', # Change in real private inventories: Residual
    'N969RX1Q020SBEA', # Change in real private inventories: Residual
    'N153RX1Q020SBEA', # Change in real private inventories: Retail trade
    'N542RX1Q020SBEA', # Change in real private inventories: Retail trade: Food and beverage stores
    'N543RX1Q020SBEA', # Change in real private inventories: Retail trade: General merchandise stores
    'N631RX1Q020SBEA', # Change in real private inventories: Retail trade: Motor vehicle and parts dealers
    'N558RX1Q020SBEA', # Change in real private inventories: Retail trade: Other retail stores
    'N658RX1Q020SBEA', # Change in real private inventories: Wholesale trade
    'N661RX1Q020SBEA', # Change in real private inventories: Wholesale trade: Durable goods industries
    'N664RX1Q020SBEA', # Change in real private inventories: Wholesale trade: Nondurable goods industries
    'A355RX1Q020SBEA', # Real gross domestic product: Durable goods: Change in private inventories
    'A357RX1Q020SBEA', # Real gross domestic product: Nondurable goods: Change in private inventories
    'A015RX1Q020SBEA', # Real gross private domestic investment: Change in private inventories: Nonfarm
    'AB65RX1Q020SBEA', # Real motor vehicle output: Change in private inventories
    'A145RX1Q020SBEA', # Real motor vehicle output: Change in private inventories: Autos
    'B146RX1Q020SBEA', # Real motor vehicle output: Change in private inventories: Autos: New
    'AB71RX1Q020SBEA', # Real motor vehicle output: Change in private inventories: Autos: New: Domestic
    'AB72RX1Q020SBEA', # Real motor vehicle output: Change in private inventories: Autos: New: Foreign
    'B147RX1Q020SBEA', # Real motor vehicle output: Change in private inventories: Autos: Used
    'B709RX1Q020SBEA', # Real motor vehicle output: Change in private inventories: Trucks
    'W244RX1Q020SBEA', # Real motor vehicle output: Change in private inventories: Trucks: New
    'AB73RX1Q020SBEA', # Real motor vehicle output: Change in private inventories: Trucks: New: Domestic
    'AB74RX1Q020SBEA', # Real motor vehicle output: Change in private inventories: Trucks: New: Foreign
    'W245RX1Q020SBEA', # Real motor vehicle output: Change in private inventories: Trucks: Used
    ## Percentage Points (SA)
    'CHNGNETINVENTCONTRIBNOW', # Contributions to percent change in GDPNow: Real Change of Inventory Investment
    ## Percentage Points at Annual Rate (SAAR)
    'A014RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Change in private inventories
    'B018RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Change in private inventories: Farm
    'A015RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Change in private inventories: Nonfarm
    'A355RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Durable goods: Change in private inventories
    'A014RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Change in private inventories
    'B018RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Change in private inventories: Farm
    'A015RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Change in private inventories: Nonfarm
    'A357RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Nondurable goods: Change in private inventories

    # Domestic Capital Account (Saving & Investment) > Private Fixed Investments (164)
    ## % Chg. from Preceding Period (SAAR)
    'A007RL1Q225SBEA', # Real Gross Private Domestic Investment: Fixed Investment
    'A008RL1Q225SBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential
    'Y033RL1Q225SBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment
    'A680RL1Q225SBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment: Industrial Equipment
    'Y034RL1Q225SBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment: Information Processing Equipment
    'B935RL1Q225SBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment: Information Processing Equipment: Computers and Peripheral Equipment
    'A937RL1Q225SBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment: Information Processing Equipment: Other
    'A862RL1Q225SBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment: Other Equipment
    'A681RL1Q225SBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment: Transportation Equipment
    'Y001RL1Q225SBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products
    'Y020RL1Q225SBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products: Entertainment, Literary, and Artistic Originals
    'Y006RL1Q225SBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products: Research and Development
    'B985RL1Q225SBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products: Software
    'A009RL1Q225SBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Structures
    'A011RL1Q225SBEA', # Real Gross Private Domestic Investment: Fixed Investment: Residential
    'AB76RL1Q225SBEA', # Real Private Fixed Investment in New Autos and New Light Trucks
    'B009RL1Q225SBEA', # Real Private Fixed Investment: Nonresidential: Structures (DISCONTINUED)
    'W001RL1Q225SBEA', # Real Private Fixed Investment: Nonresidential: Structures: Commercial and Health Care
    'C307RL1Q225SBEA', # Real Private Fixed Investment: Nonresidential: Structures: Manufacturing
    'E318RL1Q225SBEA', # Real Private Fixed Investment: Nonresidential: Structures: Mining Exploration, Shafts, and Wells
    'W004RL1Q225SBEA', # Real Private Fixed Investment: Nonresidential: Structures: Other Structures
    'W003RL1Q225SBEA', # Real Private Fixed Investment: Nonresidential: Structures: Power and Communication
    'A679RL1Q225SBEA', # Real Private Fixed Investment: Private Fixed Investment in Information Processing Equipment and Software
    'W040RL1Q225SBEA', # Real Private Fixed Investment: Private Fixed Investment in New Structures
    'A771RL1Q225SBEA', # Real Private Fixed Investment: Private Fixed Investment in New Structures: Nonresidential Structures
    'A756RL1Q225SBEA', # Real Private Fixed Investment: Private Fixed Investment in New Structures: Residential Structures
    'A349RL1Q225SBEA', # Real Private Fixed Investment: Private Fixed Investment in Structures
    'B013RL1Q225SBEA', # Real Private Fixed Investment: Residential: Equipment
    'A012RL1Q225SBEA', # Real Private Fixed Investment: Residential: Structures
    'A863RL1Q225SBEA', # Real Private Fixed Investment: Residential: Structures: Other Structures
    'A943RL1Q225SBEA', # Real Private Fixed Investment: Residential: Structures: Permanent Site
    'C292RL1Q225SBEA', # Real Private Fixed Investment: Residential: Structures: Permanent Site: Multifamily
    'A944RL1Q225SBEA', # Real Private Fixed Investment: Residential: Structures: Permanent Site: Single Family
    ## % Chg. from Qtr.  1 Yr. Ago (NSA)
    'OB000340Q', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment
    'OB000341Q', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products
    'OB000337Q', # Real Private Fixed Investment
    'OB000336Q', # Real Private Nonresidential Fixed Investment
    'OB000338Q', # Real Private Residential Investment
    ## % Chg. from Qtr.  1 Yr. Ago (SA)
    'A007RO1Q156NBEA', # Real Gross Private Domestic Investment: Fixed Investment
    'A008RO1Q156NBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential
    'Y033RO1Q156NBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment
    'Y001RO1Q156NBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products
    'A009RO1Q156NBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Structures
    'A011RO1Q156NBEA', # Real Gross Private Domestic Investment: Fixed Investment: Residential
    ## Bil. of $ (SAAR)
    'A138RC1Q027SBEA', # Automobile output: Private fixed investment (DISCONTINUED)
    'B139RC1Q027SBEA', # Automobile output: Private fixed investment: New autos
    'Y033RC1Q027SBEA', # Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment
    'Y034RC1Q027SBEA', # Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment: Information Processing Equipment
    'Y001RC1Q027SBEA', # Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products
    'Y020RC1Q027SBEA', # Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products: Entertainment, Literary, and Artistic Originals
    'Y006RC1Q027SBEA', # Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products: Research and Development
    'AB62RC1Q027SBEA', # Motor vehicle output: Private fixed investment
    'A327RC1Q027SBEA', # Private fixed investment in equipment and software (DISCONTINUED)
    'A679RC1Q027SBEA', # Private fixed investment in information processing equipment and software
    'AB76RC1Q027SBEA', # Private fixed investment in new autos and new light trucks
    'W040RC1Q027SBEA', # Private fixed investment in new structures
    'A771RC1Q027SBEA', # Private fixed investment in new structures: Nonresidential structures
    'A756RC1Q027SBEA', # Private fixed investment in new structures: Residential structures
    'A349RC1Q027SBEA', # Private fixed investment in structures
    'W242RC1Q027SBEA', # Private fixed investment: Net purchases of used autos and used light trucks
    'W243RC1Q027SBEA', # Private fixed investment: Net purchases of used light trucks (including utility vehicles)
    'AB68RC1Q027SBEA', # Private fixed investment: New motor vehicles
    'B196RC1Q027SBEA', # Private fixed investment: New motor vehicles: Light trucks (including utility vehicles)
    'B705RC1Q027SBEA', # Private fixed investment: New motor vehicles: Trucks
    'B197RC1Q027SBEA', # Private fixed investment: New motor vehicles: Trucks: Other
    'A680RC1Q027SBEA', # Private fixed investment: Nonresidential: Equipment: Industrial equipment
    'A937RC1Q027SBEA', # Private fixed investment: Nonresidential: Equipment: Information processing equipment: Other
    'A862RC1Q027SBEA', # Private fixed investment: Nonresidential: Equipment: Other equipment
    'A681RC1Q027SBEA', # Private fixed investment: Nonresidential: Equipment: Transportation equipment
    'B935RC1Q027SBEA', # Private fixed investment: Nonresidential: Information processing equipment and software: Computers and peripheral equipment
    'B985RC1Q027SBEA', # Private fixed investment: Nonresidential: Intellectual property products: Software
    'W004RC1Q027SBEA', # Private fixed investment: Nonresidential: Other structures
    'W001RC1Q027SBEA', # Private fixed investment: Nonresidential: Structures: Commercial and health care
    'C307RC1Q027SBEA', # Private fixed investment: Nonresidential: Structures: Manufacturing
    'E318RC1Q027SBEA', # Private fixed investment: Nonresidential: Structures: Mining exploration, shafts, and wells
    'W003RC1Q027SBEA', # Private fixed investment: Nonresidential: Structures: Power and communication
    'B013RC1Q027SBEA', # Private fixed investment: Residential: Equipment
    'A863RC1Q027SBEA', # Private fixed investment: Residential: Other structures
    'A012RC1Q027SBEA', # Private fixed investment: Residential: Structures
    'A943RC1Q027SBEA', # Private fixed investment: Residential: Structures: Permanent site
    'C292RC1Q027SBEA', # Private fixed investment: Residential: Structures: Permanent site: Multifamily
    'A944RC1Q027SBEA', # Private fixed investment: Residential: Structures: Permanent site: Single family
    ## Bil. of Chn. 2005 $ (SAAR)
    'A327RX1Q020SBEA', # Real private fixed investment in equipment and software (DISCONTINUED)
    ## Bil. of Chn. 2017 $ (NSA)
    'ND000340Q', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment
    'ND000341Q', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products
    'ND000339Q', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Structures
    'ND000337Q', # Real Private Fixed Investment
    'ND000336Q', # Real Private Nonresidential Fixed Investment
    'ND000338Q', # Real Private Residential Fixed Investment
    ## Bil. of Chn. 2017 $ (SAAR)
    'Y033RX1Q020SBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment
    'Y034RX1Q020SBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment: Information Processing Equipment
    'Y001RX1Q020SBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products
    'Y020RX1Q020SBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products: Entertainment, Literary, and Artistic Originals
    'Y006RX1Q020SBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products: Research and Development
    'AB62RX1Q020SBEA', # Real motor vehicle output: Private fixed investment
    'AB76RX1Q020SBEA', # Real private fixed investment in new autos and new light trucks
    'W040RX1Q020SBEA', # Real private fixed investment in new structures
    'A771RX1Q020SBEA', # Real private fixed investment in new structures: Nonresidential structures
    'A756RX1Q020SBEA', # Real private fixed investment in new structures: Residential structures
    'A349RX1Q020SBEA', # Real private fixed investment in structures
    'B140RX1Q020SBEA', # Real private fixed investment: Net purchases of used autos
    'W242RX1Q020SBEA', # Real private fixed investment: Net purchases of used autos and used light trucks
    'W243RX1Q020SBEA', # Real private fixed investment: Net purchases of used light trucks (including utility vehicles)
    'AB68RX1Q020SBEA', # Real private fixed investment: New motor vehicles
    'B139RX1Q020SBEA', # Real private fixed investment: New motor vehicles: Autos
    'B196RX1Q020SBEA', # Real private fixed investment: New motor vehicles: Light trucks (including utility vehicles)
    'B705RX1Q020SBEA', # Real private fixed investment: New motor vehicles: Trucks
    'B197RX1Q020SBEA', # Real private fixed investment: New motor vehicles: Trucks: Other
    'W001RX1Q020SBEA', # Real private fixed investment: Nonresidential: Structures: Commercial and health care
    'C307RX1Q020SBEA', # Real private fixed investment: Nonresidential: Structures: Manufacturing
    'E318RX1Q020SBEA', # Real private fixed investment: Nonresidential: Structures: Mining exploration, shafts, and wells
    'W004RX1Q020SBEA', # Real private fixed investment: Nonresidential: Structures: Other structures
    'W003RX1Q020SBEA', # Real private fixed investment: Nonresidential: Structures: Power and communication
    'B013RX1Q020SBEA', # Real private fixed investment: Residential: Equipment
    'A012RX1Q020SBEA', # Real private fixed investment: Residential: Structures
    'A863RX1Q020SBEA', # Real private fixed investment: Residential: Structures: Other structures
    'A943RX1Q020SBEA', # Real private fixed investment: Residential: Structures: Permanent site
    'C292RX1Q020SBEA', # Real private fixed investment: Residential: Structures: Permanent site: Multifamily
    'A944RX1Q020SBEA', # Real private fixed investment: Residential: Structures: Permanent site: Single family
    'A972RX1Q020SBEA', # Real private fixed investment: Residual
    ## Index 2017=100 (NSA)
    'NC000340Q', # Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment
    'NC000341Q', # Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products
    'NC000339Q', # Gross Private Domestic Investment: Fixed Investment: Nonresidential: Structures
    'NC000343Q', # Imports of Goods
    'NB000340Q', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment
    'NB000341Q', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products
    'NB000339Q', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Structures
    'NB000343Q', # Real Imports of Goods
    ## Mil. of $ (NSA)
    'NA000340Q', # Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment
    'NA000341Q', # Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products
    'NA000339Q', # Gross Private Domestic Investment: Fixed Investment: Nonresidential: Structures
    'NA000343Q', # Imports of Goods
    ## Percentage Points at Annual Rate (SAAR)
    'Y033RZ2Q224SBEA', # Contributions to Percent Change in Real Private Fixed Investment: Nonresidential: Equipment
    'Y034RZ2Q224SBEA', # Contributions to Percent Change in Real Private Fixed Investment: Nonresidential: Equipment: Information Processing Equipment
    'Y001RZ2Q224SBEA', # Contributions to Percent Change in Real Private Fixed Investment: Nonresidential: Intellectual Property Products
    'Y020RZ2Q224SBEA', # Contributions to Percent Change in Real Private Fixed Investment: Nonresidential: Intellectual Property Products: Entertainment, Literary, and Artistic Originals
    'Y006RZ2Q224SBEA', # Contributions to Percent Change in Real Private Fixed Investment: Nonresidential: Intellectual Property Products: Research and Development
    'A008RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Nonresidential
    'B010RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Equipment and software (DISCONTINUED)
    'A680RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Equipment: Industrial equipment
    'B935RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Equipment: Information processing equipment: Computers and peripheral equipment
    'A937RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Equipment: Information processing equipment: Other
    'A862RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Equipment: Other equipment
    'A681RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Equipment: Transportation equipment
    'B985RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Intellectual property products: Software
    'W004RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Other structures
    'B009RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Structures
    'W001RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Structures: Commercial and health care
    'C307RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Structures: Manufacturing
    'E318RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Structures: Mining exploration, shafts, and wells
    'W003RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Structures: Power and communication
    'A327RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Private fixed investment in equipment and software (DISCONTINUED)
    'A679RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Private fixed investment in information processing equipment and software
    'W040RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Private fixed investment in new structures
    'A771RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Private fixed investment in new structures: Nonresidential structures
    'A756RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Private fixed investment in new structures: Residential structures
    'A349RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Private fixed investment in structures
    'A011RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Residential
    'B013RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Residential: Equipment
    'A863RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Residential: Other structures
    'A012RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Residential: Structures
    'A943RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Residential: Structures: Permanent site
    'C292RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Residential: Structures: Permanent site: Multifamily
    'A944RZ2Q224SBEA', # Contributions to percent change in real private fixed investment: Residential: Structures: Permanent site: Single family

]

# Annually (1184)
ids_Y = [
    # Domestic Capital Account (Saving & Investment) (259)
    ## % (NSA)
    'W206RC1A156NBEA', # Gross saving as a percentage of gross national income
    'W207RC1A156NBEA', # Net saving as a percentage of gross national income
    ## Bil. of $ (NSA)
    'K160121A027NBEA', # Accumulation of produced assets: Gross fixed investment: Government (DISCONTINUED)
    'K160141A027NBEA', # Accumulation of produced assets: Gross fixed investment: Government: Equipment and software (DISCONTINUED)
    'K160131A027NBEA', # Accumulation of produced assets: Gross fixed investment: Government: Structures (DISCONTINUED)
    'K160071A027NBEA', # Accumulation of produced assets: Gross fixed investment: Private (DISCONTINUED)
    'K160081A027NBEA', # Accumulation of produced assets: Gross fixed investment: Private: Nonresidential (DISCONTINUED)
    'K160101A027NBEA', # Accumulation of produced assets: Gross fixed investment: Private: Nonresidential: Equipment and software (DISCONTINUED)
    'K160091A027NBEA', # Accumulation of produced assets: Gross fixed investment: Private: Nonresidential: Structures (DISCONTINUED)
    'K160111A027NBEA', # Accumulation of produced assets: Gross fixed investment: Private: Residential (DISCONTINUED)
    'K160151A027NBEA', # Accumulation of produced assets: Stock reconciliation adjustments (DISCONTINUED)
    'K160171A027NBEA', # Accumulation of produced assets: Stock reconciliation adjustments: Government (DISCONTINUED)
    'K160161A027NBEA', # Accumulation of produced assets: Stock reconciliation adjustments: Private (DISCONTINUED)
    'W456RC1A027NBEA', # BEA-derived gross output of nonprofit institutions and current transfer payments
    'B029RC1A027NBEA', # Business current transfer payments (net)
    'A1870C1A027NBEA', # Business current transfer payments (net): Insurance payments to persons by business
    'B1871C1A027NBEA', # Business current transfer payments (net): Insurance payments to persons by business: Automobile insurance
    'B1872C1A027NBEA', # Business current transfer payments (net): Insurance payments to persons by business: Medical malpractice insurance
    'W238RC1A027NBEA', # Business current transfer payments (net): Insurance payments to persons by business: Net insurance settlements
    'W061RC1A027NBEA', # Business current transfer payments (net): Payments to government (net)
    'B1873C1A027NBEA', # Business current transfer payments (net): Payments to persons (net): Donations by corporate business to nonprofit institutions serving households
    'B1874C1A027NBEA', # Business current transfer payments (net): Payments to persons (net): Other
    'W237RC1A027NBEA', # Business current transfer payments (net): Payments to the rest of the world (net)
    'W991RC1A027NBEA', # Capital account transactions (net): Government
    'W992RC1A027NBEA', # Capital account transactions (net): Government: Federal
    'W993RC1A027NBEA', # Capital account transactions (net): Government: State and local
    'W999RC1A027NBEA', # Capital account transactions (net): Private
    'W989RC1A027NBEA', # Capital account transactions (net): Private: Domestic business
    'W990RC1A027NBEA', # Capital account transactions (net): Private: Households and institutions
    'W371RC1A027NBEA', # Capital account transactions, ITAs
    'W373RC1A027NBEA', # Capital account transactions: Adjustments for U.S. territories and Puerto Rico
    'W372RC1A027NBEA', # Capital account transactions: Statistical differences, International Transactions Accounts vs. NIPAs
    'Y0004C1A027NBEA', # Capital consumption adjustment
    'A2201C1A027NBEA', # Capital consumption adjustment: Domestic corporate business
    'B393RC1A027NBEA', # Capital consumption adjustment: Domestic corporate business: Financial
    'B1404C1A027NBEA', # Capital consumption adjustment: Domestic corporate business: Financial: for consistent accounting at historical cost
    'B1405C1A027NBEA', # Capital consumption adjustment: Domestic corporate business: Financial: for current-cost valuation
    'A2203C1A027NBEA', # Capital consumption adjustment: Domestic corporate business: Nonfinancial
    'B1406C1A027NBEA', # Capital consumption adjustment: Domestic corporate business: Nonfinancial: for consistent accounting at historical cost
    'B1407C1A027NBEA', # Capital consumption adjustment: Domestic corporate business: Nonfinancial: for current-cost valuation
    'A1402C1A027NBEA', # Capital consumption adjustment: Domestic corporate business: for consistent accounting at historical cost
    'A1403C1A027NBEA', # Capital consumption adjustment: Domestic corporate business: for current-cost valuation
    'W282RC1A027NBEA', # Capital consumption adjustment: Domestic noncorporate business
    'B050RC1A027NBEA', # Capital consumption adjustment: Domestic noncorporate business: Rental income of persons
    'W283RC1A027NBEA', # Capital consumption adjustment: Domestic noncorporate business: Rental income of persons: Farm tenant-occupied housing
    'B2614C1A027NBEA', # Capital consumption adjustment: Domestic noncorporate business: Rental income of persons: Farms owned by nonoperator landlords
    'B2615C1A027NBEA', # Capital consumption adjustment: Domestic noncorporate business: Rental income of persons: Nonfarm nonresidential properties
    'B2611C1A027NBEA', # Capital consumption adjustment: Domestic noncorporate business: Rental income of persons: Nonfarm tenant-occupied housing
    'A1400C1A027NBEA', # Capital consumption adjustment: for consistent accounting at historical cost
    'A1401C1A027NBEA', # Capital consumption adjustment: for current-cost valuation
    'K100541A027NBEA', # Changes in Net Stock of Produced Assets: Nominal holding gains or losses (-)
    'K100551A027NBEA', # Changes in Net Stock of Produced Assets: Nominal holding gains or losses (-): Neutral holding gains or losses
    'K100561A027NBEA', # Changes in Net Stock of Produced Assets: Nominal holding gains or losses (-): Neutral holding gains or losses: Fixed assets
    'K100601A027NBEA', # Changes in Net Stock of Produced Assets: Nominal holding gains or losses (-): Neutral holding gains or losses: Fixed assets: Government
    'K100571A027NBEA', # Changes in Net Stock of Produced Assets: Nominal holding gains or losses (-): Neutral holding gains or losses: Fixed assets: Private
    'K100581A027NBEA', # Changes in Net Stock of Produced Assets: Nominal holding gains or losses (-): Neutral holding gains or losses: Fixed assets: Private: Nonresidential
    'K100591A027NBEA', # Changes in Net Stock of Produced Assets: Nominal holding gains or losses (-): Neutral holding gains or losses: Fixed assets: Private: Residential
    'K100611A027NBEA', # Changes in Net Stock of Produced Assets: Nominal holding gains or losses (-): Neutral holding gains or losses: Private inventories
    'K100621A027NBEA', # Changes in Net Stock of Produced Assets: Nominal holding gains or losses (-): Real holding gains or losses
    'K100631A027NBEA', # Changes in Net Stock of Produced Assets: Nominal holding gains or losses (-): Real holding gains or losses: Fixed assets
    'K100671A027NBEA', # Changes in Net Stock of Produced Assets: Nominal holding gains or losses (-): Real holding gains or losses: Fixed assets: Government
    'K100641A027NBEA', # Changes in Net Stock of Produced Assets: Nominal holding gains or losses (-): Real holding gains or losses: Fixed assets: Private
    'K100651A027NBEA', # Changes in Net Stock of Produced Assets: Nominal holding gains or losses (-): Real holding gains or losses: Fixed assets: Private: Nonresidential
    'K100661A027NBEA', # Changes in Net Stock of Produced Assets: Nominal holding gains or losses (-): Real holding gains or losses: Fixed assets: Private: Residential
    'K100681A027NBEA', # Changes in Net Stock of Produced Assets: Nominal holding gains or losses (-): Real holding gains or losses: Private inventories
    'K100441A027NBEA', # Changes in Net Stock of Produced Assets: Other changes in volume of assets
    'K100511A027NBEA', # Changes in Net Stock of Produced Assets: Other changes in volume of assets: Government fixed assets
    'K100521A027NBEA', # Changes in Net Stock of Produced Assets: Other changes in volume of assets: Government fixed assets: General government
    'K100531A027NBEA', # Changes in Net Stock of Produced Assets: Other changes in volume of assets: Government fixed assets: Government enterprises
    'K100451A027NBEA', # Changes in Net Stock of Produced Assets: Other changes in volume of assets: Private fixed assets
    'K100461A027NBEA', # Changes in Net Stock of Produced Assets: Other changes in volume of assets: Private fixed assets: Nonresidential fixed assets
    'K100481A027NBEA', # Changes in Net Stock of Produced Assets: Other changes in volume of assets: Private fixed assets: Nonresidential fixed assets: Equipment
    'K100491A027NBEA', # Changes in Net Stock of Produced Assets: Other changes in volume of assets: Private fixed assets: Nonresidential fixed assets: Intellectual property products
    'K100471A027NBEA', # Changes in Net Stock of Produced Assets: Other changes in volume of assets: Private fixed assets: Nonresidential fixed assets: Structures
    'K100501A027NBEA', # Changes in Net Stock of Produced Assets: Other changes in volume of assets: Private fixed assets: Residential fixed assets
    'K100011A027NBEA', # Changes in Net Stock of Produced Assets: Produced assets
    'K100691A027NBEA', # Changes in Net Stock of Produced Assets: Produced assets: Closing: Produced assets
    'K100701A027NBEA', # Changes in Net Stock of Produced Assets: Produced assets: Closing: Produced assets: Fixed assets
    'K100741A027NBEA', # Changes in Net Stock of Produced Assets: Produced assets: Closing: Produced assets: Fixed assets: Government
    'K100711A027NBEA', # Changes in Net Stock of Produced Assets: Produced assets: Closing: Produced assets: Fixed assets: Private
    'K100721A027NBEA', # Changes in Net Stock of Produced Assets: Produced assets: Closing: Produced assets: Fixed assets: Private: Nonresidential
    'K100731A027NBEA', # Changes in Net Stock of Produced Assets: Produced assets: Closing: Produced assets: Fixed assets: Private: Residential
    'A371RC1A027NBEA', # Changes in Net Stock of Produced Assets: Produced assets: Closing: Produced assets: Private inventories
    'K100021A027NBEA', # Changes in Net Stock of Produced Assets: Produced assets: Opening: Fixed assets
    'K100061A027NBEA', # Changes in Net Stock of Produced Assets: Produced assets: Opening: Fixed assets: Government
    'K100031A027NBEA', # Changes in Net Stock of Produced Assets: Produced assets: Opening: Fixed assets: Private
    'K100041A027NBEA', # Changes in Net Stock of Produced Assets: Produced assets: Opening: Fixed assets: Private: Nonresidential
    'K100051A027NBEA', # Changes in Net Stock of Produced Assets: Produced assets: Opening: Fixed assets: Private: Residential
    'K100191A027NBEA', # Changes in Net Stock of Produced Assets: Stock reconciliation adjustments
    'K100291A027NBEA', # Changes in Net Stock of Produced Assets: Stock reconciliation adjustments: Government
    'K100301A027NBEA', # Changes in Net Stock of Produced Assets: Stock reconciliation adjustments: Government: Electric plants put in place less electric plants put in use
    'K100311A027NBEA', # Changes in Net Stock of Produced Assets: Stock reconciliation adjustments: Government: Other
    'K100201A027NBEA', # Changes in Net Stock of Produced Assets: Stock reconciliation adjustments: Private
    'K100211A027NBEA', # Changes in Net Stock of Produced Assets: Stock reconciliation adjustments: Private: Nonresidential
    'K100251A027NBEA', # Changes in Net Stock of Produced Assets: Stock reconciliation adjustments: Private: Nonresidential: Abandoned electric plants
    'K100231A027NBEA', # Changes in Net Stock of Produced Assets: Stock reconciliation adjustments: Private: Nonresidential: Brokers' commissions on sale of nonresidential used structures and dealers' margins on used equipment
    'K100241A027NBEA', # Changes in Net Stock of Produced Assets: Stock reconciliation adjustments: Private: Nonresidential: Electric plants put in place less electric plants put in use
    'K100221A027NBEA', # Changes in Net Stock of Produced Assets: Stock reconciliation adjustments: Private: Nonresidential: Intersectoral auto valuation adjustment
    'K100271A027NBEA', # Changes in Net Stock of Produced Assets: Stock reconciliation adjustments: Private: Nonresidential: Other
    'K100281A027NBEA', # Changes in Net Stock of Produced Assets: Stock reconciliation adjustments: Private: Residential
    'B058RC1A027NBEA', # Corporate Inventory Valuation Adjustment
    'A2218C1A027NBEA', # Dividends paid
    'B1194C1A027NBEA', # Dividends paid in cash or assets, IRS
    'B1196C1A027NBEA', # Dividends paid in cash or assets, IRS: Dividends paid by Federal Reserve banks and certain federally sponsored credit agencies
    'B1198C1A027NBEA', # Dividends paid in cash or assets, IRS: Dividends received by U.S. corporations
    'B1635C1A027NBEA', # Dividends paid in cash or assets, IRS: Interest payments of regulated investment companies
    'B1195C1A027NBEA', # Dividends paid in cash or assets, IRS: Posttabulation amendments and revisions
    'A2220C1A027NBEA', # Dividends received (DISCONTINUED)
    'W444RC1A027NBEA', # Expenses of nonprofit institutions, IRS
    'W537RC1A027NBEA', # Financial services furnished without payment
    'W541RC1A027NBEA', # Financial services furnished without payment: Borrower services
    'W542RC1A027NBEA', # Financial services furnished without payment: Borrower services: Persons
    'Y521RC1A027NBEA', # Financial services furnished without payment: Depositor services
    'W457RC1A027NBEA', # Gap, IRS less BEA gross output of nonprofit institutions and current transfer payments
    'W443RC1A027NBEA', # Gap, IRS less BEA nonprofit institution income and receipts from sales
    'GPDIA', # Gross Private Domestic Investment
    'W172RC1A027NBEA', # Gross domestic fixed investment
    'W451RC1A027NBEA', # Gross output of nonprofit institutions and current transfer payments not recorded by the IRS
    'W452RC1A027NBEA', # Gross output of nonprofit institutions and current transfer payments not recorded by the IRS: Adjustment for other accounting differences
    'W454RC1A027NBEA', # Gross output of nonprofit institutions and current transfer payments not recorded by the IRS: Other organizations
    'W453RC1A027NBEA', # Gross output of nonprofit institutions and current transfer payments not recorded by the IRS: Religious organizations
    'DCIORC1A027NBEA', # Gross output of nonprofit institutions serving households: Civic and social organizations
    'DEDGRC1A027NBEA', # Gross output of nonprofit institutions serving households: Education
    'DFXORC1A027NBEA', # Gross output of nonprofit institutions serving households: Foundations and grantmaking and giving establishments
    'DHLGRC1A027NBEA', # Gross output of nonprofit institutions serving households: Health
    'DSNGRC1A027NBEA', # Gross output of nonprofit institutions serving households: Professional advocacy
    'DRCGRC1A027NBEA', # Gross output of nonprofit institutions serving households: Recreation
    'DREORC1A027NBEA', # Gross output of nonprofit institutions serving households: Religious organizations
    'DSAORC1A027NBEA', # Gross output of nonprofit institutions serving households: Social advocacy establishments
    'DSSGRC1A027NBEA', # Gross output of nonprofit institutions serving households: Social services
    'FPIA', # Gross private domestic investment: Fixed investment
    'A126RC1A027NBEA', # Gross private saving
    'W997RC1A027NBEA', # Gross private saving: Domestic business
    'W998RC1A027NBEA', # Gross private saving: Households and institutions
    'B2638C1A027NBEA', # Gross rental value of farm housing, USDA
    'A929RC1A027NBEA', # Gross saving
    'A358RC1A027NBEA', # Gross value added: GDP: Business: Nonfarm
    'W455RC1A027NBEA', # IRS-derived gross output of nonprofit institutions and current transfer payments
    'W441RC1A027NBEA', # IRS-derived nonprofit institution income and receipts from sales
    'Y712RC1A027NBEA', # Interest Paid and Received by Sector and Legal Form Organization: Monetary interest received: Rest of the world: From government
    'Y375RC1A027NBEA', # Monetary dividends received
    'Y376RC1A027NBEA', # Monetary dividends received: Domestic corporate business
    'Y377RC1A027NBEA', # Monetary dividends received: Domestic corporate business: Financial
    'A2061C1A027NBEA', # Monetary interest paid
    'A2062C1A027NBEA', # Monetary interest paid: Domestic business
    'B1130C1A027NBEA', # Monetary interest paid: Domestic: Private business: Rental income of persons
    'W319RC1A027NBEA', # Monetary interest paid: Nonprofit institutions
    'A2068C1A027NBEA', # Monetary interest received
    'A2069C1A027NBEA', # Monetary interest received: Domestic business
    'B1137C1A027NBEA', # Monetary interest received: Domestic business: Other private business
    'A593RC1A027NBEA', # Net fixed investment: Net nonresidential
    'B010RC1A027NBEA', # Net fixed investment: Net nonresidential: Equipment and software (DISCONTINUED)
    'A747RC1A027NBEA', # Net fixed investment: Net nonresidential: Net equipment and software (DISCONTINUED)
    'A594RC1A027NBEA', # Net fixed investment: Net nonresidential: Net structures
    'B009RC1A027NBEA', # Net fixed investment: Net nonresidential: Structures
    'A748RC1A027NBEA', # Net fixed investment: Net residential
    'A1626C1A027NBEA', # Net interest (paid and received): Domestic business
    'W499RC1A027NBEA', # Net interest (paid and received): Domestic business: Corporate
    'B1657C1A027NBEA', # Net interest (paid and received): Domestic business: Other private business
    'B1131C1A027NBEA', # Net interest (paid and received): Nonprofit institutions
    'W318RC1A027NBEA', # Net interest (paid and received): Owner-occupied housing
    'A1627C1A027NBEA', # Net interest (paid and received): Rest of the world
    'A030RC1A027NBEA', # Net lending or net borrowing (-), NIPAs: Government: Statistical discrepancy
    'W994RC1A027NBEA', # Net lending or net borrowing (-), NIPAs: Private
    'W995RC1A027NBEA', # Net lending or net borrowing (-), NIPAs: Private: Domestic business
    'W996RC1A027NBEA', # Net lending or net borrowing (-), NIPAs: Private: Households and institutions
    'W202RC1A027NBEA', # Net private saving
    'A127RC1A027NBEA', # Net private saving: Domestic business
    'W986RC1A027NBEA', # Net private saving: Households and institutions
    'W201RC1A027NBEA', # Net saving
    'K160581A027NBEA', # Net stock of produced assets: Abandoned electric plants (DISCONTINUED)
    'K160541A027NBEA', # Net stock of produced assets: Brokers' commissions on sale of nonresidential used structures and dealers' margins on used equipment (DISCONTINUED)
    'K160551A027NBEA', # Net stock of produced assets: Electric plants put in place less electric plants put in use (DISCONTINUED)
    'K160571A027NBEA', # Net stock of produced assets: Electric plants put in place less electric plants put in use: Government (DISCONTINUED)
    'K160561A027NBEA', # Net stock of produced assets: Electric plants put in place less electric plants put in use: Private (DISCONTINUED)
    'K160531A027NBEA', # Net stock of produced assets: Intersectoral auto valuation adjustment (DISCONTINUED)
    'K160601A027NBEA', # Net stock of produced assets: Other private investments (DISCONTINUED)
    'K160591A027NBEA', # Net stock of produced assets: Sale of equipment scrap, excluding autos (DISCONTINUED)
    'A363RC1A027NBEA', # Net value added: Net domestic product: Business
    'A364RC1A027NBEA', # Net value added: Net domestic product: Business: Nonfarm
    'W419RC1A027NBEA', # Nonprofit institution current transfer payments
    'Q386RC1A027NBEA', # Nonprofit institution current transfer payments: to households
    'W404RC1A027NBEA', # Nonprofit institution dividend income
    'W445RC1A027NBEA', # Nonprofit institution expenses recorded by the IRS not included in gross output of nonprofit institutions and current transfer payments
    'W446RC1A027NBEA', # Nonprofit institution expenses recorded by the IRS not included in gross output of nonprofit institutions and current transfer payments: Adjustment for different accounting periods
    'W429RC1A027NBEA', # Nonprofit institution expenses recorded by the IRS not included in gross output of nonprofit institutions and current transfer payments: Capital consumption adjustment
    'W448RC1A027NBEA', # Nonprofit institution expenses recorded by the IRS not included in gross output of nonprofit institutions and current transfer payments: Government hospitals and schools
    'W447RC1A027NBEA', # Nonprofit institution expenses recorded by the IRS not included in gross output of nonprofit institutions and current transfer payments: Nonresident institutions
    'W449RC1A027NBEA', # Nonprofit institution expenses recorded by the IRS not included in gross output of nonprofit institutions and current transfer payments: Other out-of-scope activity
    'W400RC1A027NBEA', # Nonprofit institution income
    'W442RC1A027NBEA', # Nonprofit institution income and receipts from sales
    'W438RC1A027NBEA', # Nonprofit institution income not recorded by the IRS
    'W428RC1A027NBEA', # Nonprofit institution income not recorded by the IRS: Other accounting differences
    'W440RC1A027NBEA', # Nonprofit institution income not recorded by the IRS: Other organizations
    'W439RC1A027NBEA', # Nonprofit institution income not recorded by the IRS: Religious organizations
    'W402RC1A027NBEA', # Nonprofit institution income receipts on assets
    'W403RC1A027NBEA', # Nonprofit institution interest income
    'W412RC1A027NBEA', # Nonprofit institution outlays
    'W422RC1A027NBEA', # Nonprofit institution saving
    'W405RC1A027NBEA', # Nonprofit institution transfer receipts
    'W407RC1A027NBEA', # Nonprofit institution transfer receipts: from business (net)
    'W406RC1A027NBEA', # Nonprofit institution transfer receipts: from government
    'W431RC1A027NBEA', # Nonprofit revenue recorded by the IRS not included in nonprofit institution income and receipts from sales
    'W433RC1A027NBEA', # Nonprofit revenue recorded by the IRS not included in nonprofit institution income and receipts from sales: Adjustment for different accounting periods
    'W432RC1A027NBEA', # Nonprofit revenue recorded by the IRS not included in nonprofit institution income and receipts from sales: Capital gains or losses
    'W435RC1A027NBEA', # Nonprofit revenue recorded by the IRS not included in nonprofit institution income and receipts from sales: Government hospitals and schools
    'W434RC1A027NBEA', # Nonprofit revenue recorded by the IRS not included in nonprofit institution income and receipts from sales: Nonresident institutions
    'W436RC1A027NBEA', # Nonprofit revenue recorded by the IRS not included in nonprofit institution income and receipts from sales: Other out-of-scope activity
    'K160281A027NBEA', # Other changes in volume of assets (DISCONTINUED)
    'K160341A027NBEA', # Other changes in volume of assets: Government fixed assets (DISCONTINUED)
    'K160351A027NBEA', # Other changes in volume of assets: Government fixed assets: General government (DISCONTINUED)
    'K160361A027NBEA', # Other changes in volume of assets: Government fixed assets: Government enterprises (DISCONTINUED)
    'K160291A027NBEA', # Other changes in volume of assets: Private fixed assets (DISCONTINUED)
    'K160301A027NBEA', # Other changes in volume of assets: Private fixed assets: Nonresidential fixed assets (DISCONTINUED)
    'K160321A027NBEA', # Other changes in volume of assets: Private fixed assets: Nonresidential fixed assets: Equipment and software (DISCONTINUED)
    'K160311A027NBEA', # Other changes in volume of assets: Private fixed assets: Nonresidential fixed assets: Structures (DISCONTINUED)
    'K160331A027NBEA', # Other changes in volume of assets: Private fixed assets: Residential fixed assets (DISCONTINUED)
    'PNFIA', # Private Nonresidential Fixed Investment
    'PRFIA', # Private Residential Fixed Investment
    'K100071A027NBEA', # Produced Assets Net Stock: Opening Balance: Private Inventories
    'K160481A027NBEA', # Produced assets, closing balance (DISCONTINUED)
    'K160491A027NBEA', # Produced assets, closing balance: Fixed assets (DISCONTINUED)
    'K160511A027NBEA', # Produced assets, closing balance: Fixed assets: Government (DISCONTINUED)
    'K160501A027NBEA', # Produced assets, closing balance: Fixed assets: Private (DISCONTINUED)
    'K160011A027NBEA', # Produced assets, opening balance (DISCONTINUED)
    'K160021A027NBEA', # Produced assets, opening balance: Fixed assets (DISCONTINUED)
    'K160041A027NBEA', # Produced assets, opening balance: Fixed assets: Government (DISCONTINUED)
    'K160031A027NBEA', # Produced assets, opening balance: Fixed assets: Private (DISCONTINUED)
    'W159RC1A027NBEA', # Rental income of nonprofit institutions with capital consumption adjustment
    'K160381A027NBEA', # Revaluation of produced assets: Neutral holding gains or losses (-) (DISCONTINUED)
    'K160391A027NBEA', # Revaluation of produced assets: Neutral holding gains or losses (-): Fixed assets (DISCONTINUED)
    'K160411A027NBEA', # Revaluation of produced assets: Neutral holding gains or losses (-): Fixed assets: Government (DISCONTINUED)
    'K160401A027NBEA', # Revaluation of produced assets: Neutral holding gains or losses (-): Fixed assets: Private (DISCONTINUED)
    'K160371A027NBEA', # Revaluation of produced assets: Nominal holding gains or losses (-) (DISCONTINUED)
    'K160431A027NBEA', # Revaluation of produced assets: Real holding gains or losses (-) (DISCONTINUED)
    'K160441A027NBEA', # Revaluation of produced assets: Real holding gains or losses (-): Fixed assets (DISCONTINUED)
    'K160461A027NBEA', # Revaluation of produced assets: Real holding gains or losses (-): Fixed assets: Government (DISCONTINUED)
    'K160451A027NBEA', # Revaluation of produced assets: Real holding gains or losses (-): Fixed assets: Private (DISCONTINUED)
    'W771RC1A027NBEA', # Saving and investment: Disaster losses
    'W772RC1A027NBEA', # Saving and investment: Disaster losses: Private
    'W773RC1A027NBEA', # Saving and investment: Disaster losses: Private: Domestic business
    'W774RC1A027NBEA', # Saving and investment: Disaster losses: Private: Households and institutions
    'B1186C1A027NBEA', # Tax-return measures: Costs of trading or issuing corporate securities
    'B1184C1A027NBEA', # Tax-return measures: Dividends received from domestic corporations
    'B1183C1A027NBEA', # Tax-return measures: Gains, net of losses, from sale of property
    'B1185C1A027NBEA', # Tax-return measures: Income on equities in foreign corporations and branches (to U.S. corporations)
    'W426RC1A027NBEA', # Transfer payments between nonprofit institutions
    ## Bil. of Chn. 2005 $ (NSA)
    'NRIPDCA', # Real Private Nonresidential Investment: Equipment and Software (DISCONTINUED)
    ## Bil. of Chn. 2017 $ (NSA)
    'GPDICA', # Real Gross Private Domestic Investment
    'FPICA', # Real Private Fixed Investment
    'PNFICA', # Real Private Nonresidential Fixed Investment
    'PRFICA', # Real Private Residential Fixed Investment
    'A195RX1A020NBEA', # Real gross value added: GDP: Business
    'B359RX1A020NBEA', # Real gross value added: GDP: Business: Farm
    'A358RX1A020NBEA', # Real gross value added: GDP: Business: Nonfarm
    'A363RX1A020NBEA', # Real net value added: Net domestic product: Business
    'A365RX1A020NBEA', # Real net value added: Net domestic product: Business: Farm
    'A364RX1A020NBEA', # Real net value added: Net domestic product: Business: Nonfarm
    'A966RX1A020NBEA', # Real net value added: Net domestic product: Residual

    # Domestic Capital Account (Saving & Investment) > Capital Transfers Paid (56)
    ## Bil. of $ (NSA)
    'Y660RC1A027NBEA', # Business Current Transfer Payments: Net Payments to Persons: Net Defined Benefit and Defined Contribution Pension Plans
    'LA0000301A027NBEA', # Business Current Transfer Payments: Net Payments to the Rest of the World: Current transfer payments to the rest of the world
    'W947RC1A027NBEA', # Capital transfers paid, by government
    'W948RC1A027NBEA', # Capital transfers paid, by government: Federal (DISCONTINUED)
    'AD11RC1A027NBEA', # Capital transfers paid, by government: Federal: Capital grants to state and local governments
    'AD10RC1A027NBEA', # Capital transfers paid, by government: Federal: Capital transfers paid to the rest of the world (net)
    'W949RC1A027NBEA', # Capital transfers paid, by government: Federal: Disaster-related insurance benefits
    'W950RC1A027NBEA', # Capital transfers paid, by government: Federal: Financial stabilization payments
    'W951RC1A027NBEA', # Capital transfers paid, by government: Federal: Other capital transfers paid to business
    'W027RC1A027NBEA', # Capital transfers paid, by government: Federal: Other capital transfers paid to persons
    'W952RC1A027NBEA', # Capital transfers paid, by government: State and local (DISCONTINUED)
    'W953RC1A027NBEA', # Capital transfers paid, by persons
    'B232RC1A027NBEA', # Capital transfers paid, by persons: Estate and gift taxes, federal
    'S210201A027NBEA', # Capital transfers paid, by persons: Estate and gift taxes, state and local
    'W941RC1A027NBEA', # Capital transfers paid, by private business sector
    'W942RC1A027NBEA', # Capital transfers paid, by private business sector: Financial corporations
    'W943RC1A027NBEA', # Capital transfers paid, by private business sector: Financial corporations: Disaster-related insurance benefits
    'W944RC1A027NBEA', # Capital transfers paid, by private business sector: Financial corporations: Other non disaster related insurance benefits
    'W946RC1A027NBEA', # Capital transfers paid, by private business sector: Noncorporate business
    'W945RC1A027NBEA', # Capital transfers paid, by private business sector: Nonfinancial corporations
    'W940RC1A027NBEA', # Capital transfers paid, by sector
    'W954RC1A027NBEA', # Capital transfers paid, by the rest of the world
    'W955RC1A027NBEA', # Capital transfers paid, by the rest of the world: Disaster-related insurance benefits
    'W956RC1A027NBEA', # Capital transfers paid, by the rest of the world: Other non disaster related insurance benefits
    'G171361A027NBEA', # Federal government capital transfers paid: Economic affairs
    'W699RC1A027NBEA', # Federal government capital transfers paid: Economic affairs: Other economic affairs
    'G171371A027NBEA', # Federal government capital transfers paid: Economic affairs: Transportation
    'G171391A027NBEA', # Federal government capital transfers paid: Economic affairs: Transportation: Air
    'G171381A027NBEA', # Federal government capital transfers paid: Economic affairs: Transportation: Highways
    'G171411A027NBEA', # Federal government capital transfers paid: Economic affairs: Transportation: Transit and railroad
    'W813RC1A027NBEA', # Federal government capital transfers paid: Economic affairs: Transportation: Water
    'W698RC1A027NBEA', # Federal government capital transfers paid: General public service
    'G171431A027NBEA', # Federal government capital transfers paid: Health
    'G171421A027NBEA', # Federal government capital transfers paid: Housing and community services
    'G171441A027NBEA', # Federal government capital transfers paid: Income security
    'L318301A027NBEA', # Federal government cash payments to the public: Coverage differences: Capital transfers paid (DISCONTINUED)
    'M318301A027NBEA', # Federal government expenditures: Coverage differences: Capital transfers paid (NIPA vs. Budget)
    'W801RC1A027NBEA', # Government capital transfers paid: Economic affairs
    'W807RC1A027NBEA', # Government capital transfers paid: Economic affairs: Other economic affairs
    'W802RC1A027NBEA', # Government capital transfers paid: Economic affairs: Transportation
    'W804RC1A027NBEA', # Government capital transfers paid: Economic affairs: Transportation: Air
    'W803RC1A027NBEA', # Government capital transfers paid: Economic affairs: Transportation: Highways
    'W806RC1A027NBEA', # Government capital transfers paid: Economic affairs: Transportation: Transit and railroad
    'W805RC1A027NBEA', # Government capital transfers paid: Economic affairs: Transportation: Water
    'W800RC1A027NBEA', # Government capital transfers paid: General public service
    'W809RC1A027NBEA', # Government capital transfers paid: Health
    'W808RC1A027NBEA', # Government capital transfers paid: Housing and community services
    'W810RC1A027NBEA', # Government capital transfers paid: Income security
    'W978RC1A027NBEA', # Net capital transfers paid by government
    'W979RC1A027NBEA', # Net capital transfers paid by government: Federal
    'W980RC1A027NBEA', # Net capital transfers paid by government: State and local
    'W981RC1A027NBEA', # Net capital transfers paid by persons
    'W975RC1A027NBEA', # Net capital transfers paid by private business sector
    'W976RC1A027NBEA', # Net capital transfers paid by private business sector: Corporate business
    'W977RC1A027NBEA', # Net capital transfers paid by private business sector: Noncorporate business
    'W982RC1A027NBEA', # Net capital transfers paid by the rest of the world

    # Domestic Capital Account (Saving & Investment) > Capital Transfers Received (35)
    ## Bil. of $ (NSA)
    'W968RC1A027NBEA', # Capital transfers received, by government
    'W969RC1A027NBEA', # Capital transfers received, by government: State and local
    'W970RC1A027NBEA', # Capital transfers received, by government: State and local: Disaster-related insurance benefits
    'W937RC1A027NBEA', # Capital transfers received, by government: State and local: Other
    'W971RC1A027NBEA', # Capital transfers received, by persons
    'W972RC1A027NBEA', # Capital transfers received, by persons: Disaster-related insurance benefits
    'W688RC1A027NBEA', # Capital transfers received, by persons: Other non disaster related insurance benefits
    'W958RC1A027NBEA', # Capital transfers received, by private business sector
    'W959RC1A027NBEA', # Capital transfers received, by private business sector: Financial corporations
    'W960RC1A027NBEA', # Capital transfers received, by private business sector: Financial corporations: Disaster-related insurance benefits
    'W961RC1A027NBEA', # Capital transfers received, by private business sector: Financial corporations: Other non disaster related insurance benefits
    'W965RC1A027NBEA', # Capital transfers received, by private business sector: Noncorporate business
    'W966RC1A027NBEA', # Capital transfers received, by private business sector: Noncorporate business: Disaster-related insurance benefits
    'W967RC1A027NBEA', # Capital transfers received, by private business sector: Noncorporate business: Other non disaster related insurance benefits
    'W962RC1A027NBEA', # Capital transfers received, by private business sector: Nonfinancial corporations
    'W963RC1A027NBEA', # Capital transfers received, by private business sector: Nonfinancial corporations: Disaster-related insurance benefits
    'W964RC1A027NBEA', # Capital transfers received, by private business sector: Nonfinancial corporations: Other non disaster related insurance benefits
    'W957RC1A027NBEA', # Capital transfers received, by sector
    'W973RC1A027NBEA', # Capital transfers received, by the rest of the world
    'W974RC1A027NBEA', # Capital transfers received, by the rest of the world: Other
    'L318481A027NBEA', # Federal government budget: Federal employee retirement plans (DISCONTINUED)
    'M318521A027NBEA', # Federal government budget: Net capital transfers received
    'L318471A027NBEA', # Federal government budget: Net capital transfers received (DISCONTINUED)
    'M318531A027NBEA', # Federal government budget: Net capital transfers received: Federal employee retirement plans
    'M318541A027NBEA', # Federal government budget: Net capital transfers received: Other coverage differences (NIPA vs. Budget)
    'M318551A027NBEA', # Federal government budget: Net capital transfers received: Timing differences (NIPA vs. Budget)
    'L318491A027NBEA', # Federal government budget: Other coverage differences (DISCONTINUED)
    'L318501A027NBEA', # Federal government budget: Timing differences (DISCONTINUED)
    'L318051A027NBEA', # Federal government cash receipts from the public: Coverage differences: Capital transfers received (DISCONTINUED)
    'M318051A027NBEA', # Federal government receipts: Coverage differences: Capital transfers received (NIPA vs. Budget)
    'L319101A027NBEA', # State and Local government current receipts: Coverage differences: Capital transfers received (NIPA vs. Census)
    'L319431A027NBEA', # State and Local government current receipts: Coverage differences: Net capital transfers received (NIPA vs. Census) (DISCONTINUED)
    'L319451A027NBEA', # State and Local government current receipts: Coverage differences: Net capital transfers received: Other coverage differences (NIPA vs. Census)
    'L319441A027NBEA', # State and Local government current receipts: Coverage differences: Net capital transfers received: State and local employee retirement plans (NIPA vs. Census)
    'L319461A027NBEA', # State and Local government current receipts: Coverage differences: Net capital transfers received: Timing and other differences (NIPA vs. Census)

    # Domestic Capital Account (Saving & Investment) > Consumptions of Fixed Capital (62)
    ## Bil. of $ (NSA)
    'K160181A027NBEA', # Accumulation of produced assets: Consumption of fixed capital (DISCONTINUED)
    'K160241A027NBEA', # Accumulation of produced assets: Consumption of fixed capital: Government (DISCONTINUED)
    'K160261A027NBEA', # Accumulation of produced assets: Consumption of fixed capital: Government: Equipment and software (DISCONTINUED)
    'K160251A027NBEA', # Accumulation of produced assets: Consumption of fixed capital: Government: Structures (DISCONTINUED)
    'K160191A027NBEA', # Accumulation of produced assets: Consumption of fixed capital: Private (DISCONTINUED)
    'K160201A027NBEA', # Accumulation of produced assets: Consumption of fixed capital: Private: Nonresidential (DISCONTINUED)
    'K160221A027NBEA', # Accumulation of produced assets: Consumption of fixed capital: Private: Nonresidential: Equipment and software (DISCONTINUED)
    'K160211A027NBEA', # Accumulation of produced assets: Consumption of fixed capital: Private: Nonresidential: Structures (DISCONTINUED)
    'K160231A027NBEA', # Accumulation of produced assets: Consumption of fixed capital: Private: Residential (DISCONTINUED)
    'A265RC1A027NBEA', # Consumption of fixed capital: General government
    'B995RC1A027NBEA', # Consumption of fixed capital: General government: Federal
    'B986RC1A027NBEA', # Consumption of fixed capital: General government: State and local
    'A264RC1A027NBEA', # Consumption of fixed capital: Government
    'A266RC1A027NBEA', # Consumption of fixed capital: Government enterprises
    'B833RC1A027NBEA', # Consumption of fixed capital: Government enterprises: Federal
    'B846RC1A027NBEA', # Consumption of fixed capital: Government enterprises: State and local
    'A918RC1A027NBEA', # Consumption of fixed capital: Government: Federal
    'A919RC1A027NBEA', # Consumption of fixed capital: Government: State and local
    'B1667C1A027NBEA', # Consumption of fixed capital: Nonfarm business
    'A024RC1A027NBEA', # Consumption of fixed capital: Private
    'W276RC1A027NBEA', # Consumption of fixed capital: Private: Domestic business
    'Y0000C1A027NBEA', # Consumption of fixed capital: Private: Domestic business: Capital consumption allowances
    'A438RC1A027NBEA', # Consumption of fixed capital: Private: Domestic: Corporate business
    'B580RC1A027NBEA', # Consumption of fixed capital: Private: Domestic: Corporate business: Financial
    'B456RC1A027NBEA', # Consumption of fixed capital: Private: Domestic: Corporate business: Nonfinancial
    'W277RC1A027NBEA', # Consumption of fixed capital: Private: Domestic: Noncorporate business
    'B1619C1A027NBEA', # Consumption of fixed capital: Private: Domestic: Noncorporate business: Proprietors' income
    'B1620C1A027NBEA', # Consumption of fixed capital: Private: Domestic: Noncorporate business: Rental income of persons
    'A1618C1A027NBEA', # Consumption of fixed capital: Private: Domestic: Noncorporate business: Rental income of persons and proprietors' income
    'W278RC1A027NBEA', # Consumption of fixed capital: Private: Domestic: Noncorporate business: Rental income of persons: Farm tenant-occupied housing
    'B2609C1A027NBEA', # Consumption of fixed capital: Private: Domestic: Noncorporate business: Rental income of persons: Farms owned by nonoperator landlords
    'B2610C1A027NBEA', # Consumption of fixed capital: Private: Domestic: Noncorporate business: Rental income of persons: Nonfarm nonresidential properties
    'B2608C1A027NBEA', # Consumption of fixed capital: Private: Domestic: Noncorporate business: Rental income of persons: Nonfarm tenant-occupied housing
    'A1615C1A027NBEA', # Consumption of fixed capital: Private: Domestic: Noncorporate business: Sole proprietorships and partnerships
    'B1616C1A027NBEA', # Consumption of fixed capital: Private: Domestic: Noncorporate business: Sole proprietorships and partnerships: Farm
    'B1617C1A027NBEA', # Consumption of fixed capital: Private: Domestic: Noncorporate business: Sole proprietorships and partnerships: Nonfarm
    'W279RC1A027NBEA', # Consumption of fixed capital: Private: Households and institutions
    'B1621C1A027NBEA', # Consumption of fixed capital: Private: Households and institutions: Nonprofit institutions serving households
    'B2607C1A027NBEA', # Consumption of fixed capital: Private: Households and institutions: Owner-occupied housing
    'B128RC1A027NBEA', # Corporations: Consumption of fixed capital, NIPAs (DISCONTINUED)
    'W869RC1A027NBEA', # Local government expenditures: Consumption of fixed capital
    'B188RC1A027NBEA', # Net fixed investment: Net nonresidential: Consumption of fixed capital
    'B189RC1A027NBEA', # Net fixed investment: Net nonresidential: Equipment and software: Consumption of fixed capital (DISCONTINUED)
    'A753RC1A027NBEA', # Net fixed investment: Nonresidential: Consumption of fixed capital
    'A754RC1A027NBEA', # Net fixed investment: Residential: Consumption of fixed capital
    'A900RC1A027NBEA', # Net government investment: Equipment and software: Consumption of fixed capital (DISCONTINUED)
    'A894RC1A027NBEA', # Net government investment: Structures: Consumption of fixed capital
    'B1157C1A027NBEA', # Rental value of nonresidential fixed assets owned and used by nonprofit institutions serving households: Consumption of fixed capital
    'W769RC1A027NBEA', # State government expenditures: Consumption of fixed capital
    ## Bil. of Chn. 2005 $ (NSA)
    'B189RX1A020NBEA', # Real net fixed investment: Net nonresidential: Equipment and Software: Consumption of fixed capital (DISCONTINUED)
    'B900RX1A020NBEA', # Real net government investment: Equipment and Software: Consumption of fixed capital (DISCONTINUED)
    ## Bil. of Chn. 2009 $ (NSA)
    'B024RX1A020NBEA', # Real gross private domestic investment: Consumption of fixed capital (DISCONTINUED)
    ## Bil. of Chn. 2017 $ (NSA)
    'A262RX1A020NBEA', # Real consumption of fixed capital
    'A265RX1A020NBEA', # Real consumption of fixed capital: General government
    'A266RX1A020NBEA', # Real consumption of fixed capital: Government: Government enterprises
    'A024RX1A020NBEA', # Real consumption of fixed capital: Private
    'A264RX1A020NBEA', # Real gross domestic investment: Consumption of fixed capital
    'B1028X1A020NBEA', # Real housing output: Consumption of fixed capital
    'B188RX1A020NBEA', # Real net fixed investment: Net nonresidential: Structures: Consumption of fixed capital
    'A753RX1A020NBEA', # Real net fixed investment: Nonresidential: Consumption of fixed capital
    'A754RX1A020NBEA', # Real net fixed investment: Residential: Consumption of fixed capital
    'B894RX1A020NBEA', # Real net government investment: Structures: Consumption of fixed capital

    # Domestic Capital Account (Saving & Investment) > Corporate Capital Consumption (156)
    ## Mil. of $ (NSA)
    'N7799C0A144NBEA', # Corporate capital consumption allowances: Accommodation
    'N7798C0A144NBEA', # Corporate capital consumption allowances: Accommodation and food services
    'N7788C0A144NBEA', # Corporate capital consumption allowances: Administrative and support services
    'N7787C0A144NBEA', # Corporate capital consumption allowances: Administrative and waste management services
    'B1724C0A144NBEA', # Corporate capital consumption allowances: Agricultural services, forestry, and fishing
    'A1722C0A144NBEA', # Corporate capital consumption allowances: Agriculture, forestry, and fishing
    'N7722C0A144NBEA', # Corporate capital consumption allowances: Agriculture, forestry, fishing, and hunting
    'N7758C0A144NBEA', # Corporate capital consumption allowances: Air transportation
    'N7792C0A144NBEA', # Corporate capital consumption allowances: Ambulatory health care services
    'B1787C0A144NBEA', # Corporate capital consumption allowances: Amusement and recreation services
    'N7797C0A144NBEA', # Corporate capital consumption allowances: Amusements, gambling, and recreation industries
    'B1793C0A144NBEA', # Corporate capital consumption allowances: Anthracite mining
    'N7795C0A144NBEA', # Corporate capital consumption allowances: Arts, entertainment, and recreation
    'B1784C0A144NBEA', # Corporate capital consumption allowances: Auto repair, services, and parking
    'A1771C0A144NBEA', # Corporate capital consumption allowances: Banking
    'B1783C0A144NBEA', # Corporate capital consumption allowances: Business services
    'B1727C0A144NBEA', # Corporate capital consumption allowances: Coal mining
    'B1773C0A144NBEA', # Corporate capital consumption allowances: Commercial and mutual banks
    'B1797C0A144NBEA', # Corporate capital consumption allowances: Commercial and mutual depository institutions
    'A1764C0A144NBEA', # Corporate capital consumption allowances: Communication
    'B1766C0A144NBEA', # Corporate capital consumption allowances: Communication: Radio and television
    'B1765C0A144NBEA', # Corporate capital consumption allowances: Communication: Telephone and telegraph
    'N7782C0A144NBEA', # Corporate capital consumption allowances: Computer systems design and related services
    'B1730C0A144NBEA', # Corporate capital consumption allowances: Construction
    'N7730C0A144NBEA', # Corporate capital consumption allowances: Construction
    'B1774C0A144NBEA', # Corporate capital consumption allowances: Credit agencies other than banks
    'B1796C0A144NBEA', # Corporate capital consumption allowances: Depository institutions
    'B1791C0A144NBEA', # Corporate capital consumption allowances: Educational services
    'N7790C0A144NBEA', # Corporate capital consumption allowances: Educational services
    'B1723C0A144NBEA', # Corporate capital consumption allowances: Farms
    'N7723C0A144NBEA', # Corporate capital consumption allowances: Farms
    'B1772C0A144NBEA', # Corporate capital consumption allowances: Federal Reserve banks
    'N7772C0A144NBEA', # Corporate capital consumption allowances: Federal Reserve banks
    'N7771C0A144NBEA', # Corporate capital consumption allowances: Finance and insurance
    'N7773C0A144NBEA', # Corporate capital consumption allowances: Finance and insurance: Credit intermediation and related activities
    'A1770C0A144NBEA', # Corporate capital consumption allowances: Finance, insurance, and real estate
    'N7700C0A144NBEA', # Corporate capital consumption allowances: Food services and drinking places
    'N7724C0A144NBEA', # Corporate capital consumption allowances: Forestry, fishing, and related activities
    'N7776C0A144NBEA', # Corporate capital consumption allowances: Funds, trusts, and other financial vehicles
    'N7791C0A144NBEA', # Corporate capital consumption allowances: Health care and social assistance
    'B1789C0A144NBEA', # Corporate capital consumption allowances: Health services
    'A1788C0A144NBEA', # Corporate capital consumption allowances: Health, legal, educational, and other services
    'B1779C0A144NBEA', # Corporate capital consumption allowances: Holding and other investment offices
    'N7793C0A144NBEA', # Corporate capital consumption allowances: Hospitals and nursing and residential care facilities
    'N7766C0A144NBEA', # Corporate capital consumption allowances: Information
    'N7769C0A144NBEA', # Corporate capital consumption allowances: Information: Broadcasting and telecommunications
    'N7770C0A144NBEA', # Corporate capital consumption allowances: Information: Information and data processing services
    'N7768C0A144NBEA', # Corporate capital consumption allowances: Information: Motion picture and sound recording industries
    'N7767C0A144NBEA', # Corporate capital consumption allowances: Information: Publishing industries (includes software)
    'B1777C0A144NBEA', # Corporate capital consumption allowances: Insurance agents, brokers, and service
    'B1776C0A144NBEA', # Corporate capital consumption allowances: Insurance carriers
    'N7775C0A144NBEA', # Corporate capital consumption allowances: Insurance carriers and related activities
    'B1790C0A144NBEA', # Corporate capital consumption allowances: Legal services
    'N7781C0A144NBEA', # Corporate capital consumption allowances: Legal services
    'N7784C0A144NBEA', # Corporate capital consumption allowances: Management of companies and enterprises
    'B1731C0A144NBEA', # Corporate capital consumption allowances: Manufacturing
    'N7731C0A144NBEA', # Corporate capital consumption allowances: Manufacturing
    'A1732C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Durable goods
    'N7732C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Durable goods
    'N7738C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Durable goods: Computer and electronic products
    'B1739C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Durable goods: Electric and electronic equipment
    'N7739C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Durable goods: Electrical equipment, appliances, and components
    'B1737C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Durable goods: Fabricated metal products
    'N7736C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Durable goods: Fabricated metal products
    'B1734C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Durable goods: Furniture and fixtures
    'N7742C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Durable goods: Furniture and related products
    'B1742C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Durable goods: Instruments and related products
    'B1733C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Durable goods: Lumber and wood products
    'N7737C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Durable goods: Machinery
    'B1738C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Durable goods: Machinery, except electrical
    'N7743C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Durable goods: Miscellaneous manufacturing
    'B1743C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Durable goods: Miscellaneous manufacturing industries
    'B1740C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Durable goods: Motor vehicles and equipment
    'N7740C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Durable goods: Motor vehicles, bodies and trailers, and parts
    'N7734C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Durable goods: Nonmetallic mineral products
    'B1741C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Durable goods: Other transportation equipment
    'N7741C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Durable goods: Other transportation equipment
    'B1736C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Durable goods: Primary metal industries
    'N7735C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Durable goods: Primary metals
    'B1735C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Durable goods: Stone, clay, and glass products
    'N7733C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Durable goods: Wood products
    'A1744C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Nondurable goods
    'N7744C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Nondurable goods
    'N7747C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Nondurable goods: Apparel and leather and allied products
    'B1748C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Nondurable goods: Apparel and other textile products
    'N7751C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Nondurable goods: Chemical products
    'B1751C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Nondurable goods: Chemicals and allied products
    'N7745C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Nondurable goods: Food and beverage and tobacco products
    'B1745C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Nondurable goods: Food and kindred products
    'B1754C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Nondurable goods: Leather and leather products
    'B1749C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Nondurable goods: Paper and allied products
    'N7748C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Nondurable goods: Paper products
    'B1752C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Nondurable goods: Petroleum and coal products
    'N7750C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Nondurable goods: Petroleum and coal products
    'N7752C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Nondurable goods: Plastics and rubber products
    'B1750C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Nondurable goods: Printing and publishing
    'N7749C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Nondurable goods: Printing and related support activities
    'B1753C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Nondurable goods: Rubber and miscellaneous plastics products
    'B1747C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Nondurable goods: Textile mill products
    'N7746C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Nondurable goods: Textile mills and textile product mills
    'B1746C0A144NBEA', # Corporate capital consumption allowances: Manufacturing: Nondurable goods: Tobacco manufactures
    'B1726C0A144NBEA', # Corporate capital consumption allowances: Metal mining
    'A1725C0A144NBEA', # Corporate capital consumption allowances: Mining
    'N7725C0A144NBEA', # Corporate capital consumption allowances: Mining
    'N7727C0A144NBEA', # Corporate capital consumption allowances: Mining, except oil and gas
    'B1729C0A144NBEA', # Corporate capital consumption allowances: Mining: Nonmetallic minerals, except fuels
    'B1728C0A144NBEA', # Corporate capital consumption allowances: Mining: Oil and gas extraction
    'N7726C0A144NBEA', # Corporate capital consumption allowances: Mining: Oil and gas extraction
    'N7783C0A144NBEA', # Corporate capital consumption allowances: Miscellaneous professional, scientific, and technical services
    'B1785C0A144NBEA', # Corporate capital consumption allowances: Miscellaneous repair services
    'B1798C0A144NBEA', # Corporate capital consumption allowances: Nondepository institutions
    'B1792C0A144NBEA', # Corporate capital consumption allowances: Other services
    'N7701C0A144NBEA', # Corporate capital consumption allowances: Other services, except government
    'N7764C0A144NBEA', # Corporate capital consumption allowances: Other transportation and support activities
    'N7796C0A144NBEA', # Corporate capital consumption allowances: Performing arts, spectator sports, museums, and related activities
    'B1782C0A144NBEA', # Corporate capital consumption allowances: Personal services
    'N7763C0A144NBEA', # Corporate capital consumption allowances: Pipeline transportation
    'N7780C0A144NBEA', # Corporate capital consumption allowances: Professional, scientific, and technical services
    'N7759C0A144NBEA', # Corporate capital consumption allowances: Rail transportation
    'B1757C0A144NBEA', # Corporate capital consumption allowances: Railroad transportation
    'B1778C0A144NBEA', # Corporate capital consumption allowances: Real estate
    'N7778C0A144NBEA', # Corporate capital consumption allowances: Real estate
    'N7777C0A144NBEA', # Corporate capital consumption allowances: Real estate and rental and leasing
    'N7779C0A144NBEA', # Corporate capital consumption allowances: Rental and leasing services and lessors of intangible assets
    'B1769C0A144NBEA', # Corporate capital consumption allowances: Retail trade
    'N7756C0A144NBEA', # Corporate capital consumption allowances: Retail trade
    'N7774C0A144NBEA', # Corporate capital consumption allowances: Securities, commodity contracts, and investments
    'B1775C0A144NBEA', # Corporate capital consumption allowances: Security and commodity brokers
    'A1780C0A144NBEA', # Corporate capital consumption allowances: Services
    'B1781C0A144NBEA', # Corporate capital consumption allowances: Services: Hotels and other lodging places
    'B1786C0A144NBEA', # Corporate capital consumption allowances: Services: Motion pictures
    'N7794C0A144NBEA', # Corporate capital consumption allowances: Social assistance
    'N7728C0A144NBEA', # Corporate capital consumption allowances: Support activities for mining
    'N7762C0A144NBEA', # Corporate capital consumption allowances: Transit and ground passenger transportation
    'A1756C0A144NBEA', # Corporate capital consumption allowances: Transportation
    'A1755C0A144NBEA', # Corporate capital consumption allowances: Transportation and public utilities
    'B1767C0A144NBEA', # Corporate capital consumption allowances: Transportation and public utilities: Electric, gas, and sanitary services
    'B1795C0A144NBEA', # Corporate capital consumption allowances: Transportation and public utilities: Local utilities and public services, n.e.c.
    'N7757C0A144NBEA', # Corporate capital consumption allowances: Transportation and warehousing
    'N7765C0A144NBEA', # Corporate capital consumption allowances: Transportation and warehousing: Warehousing and storage
    'B1761C0A144NBEA', # Corporate capital consumption allowances: Transportation by air
    'B1763C0A144NBEA', # Corporate capital consumption allowances: Transportation services
    'B1758C0A144NBEA', # Corporate capital consumption allowances: Transportation: Local and interurban passenger transit
    'B1762C0A144NBEA', # Corporate capital consumption allowances: Transportation: Pipelines, except natural gas
    'B1759C0A144NBEA', # Corporate capital consumption allowances: Transportation: Trucking and warehousing
    'N7761C0A144NBEA', # Corporate capital consumption allowances: Truck transportation
    'N7729C0A144NBEA', # Corporate capital consumption allowances: Utilities
    'B1794C0A144NBEA', # Corporate capital consumption allowances: Utilities: electric and gas
    'N7789C0A144NBEA', # Corporate capital consumption allowances: Waste management and remediation services
    'B1760C0A144NBEA', # Corporate capital consumption allowances: Water transportation
    'N7760C0A144NBEA', # Corporate capital consumption allowances: Water transportation
    'B1768C0A144NBEA', # Corporate capital consumption allowances: Wholesale trade
    'N7753C0A144NBEA', # Corporate capital consumption allowances: Wholesale trade
    'N7754C0A144NBEA', # Corporate capital consumption allowances: Wholesale trade: Durable goods
    'N7755C0A144NBEA', # Corporate capital consumption allowances: Wholesale trade: Nondurable goods
    'A677RC0A144NBEA', # Corporations: Capital consumption allowances, NIPAs (DISCONTINUED)

    # Domestic Capital Account (Saving & Investment) > Domestic Investments (69)
    ## % Chg. from Preceding Period (NSA)
    'A006RL1A225NBEA', # Real Gross Private Domestic Investment
    ## Bil. of $ (NSA)
    'K160061A027NBEA', # Accumulation of produced assets: Gross fixed investment (DISCONTINUED)
    'W170RC1A027NBEA', # Gross domestic investment
    'A928RC1A027NBEA', # Gross domestic investment, capital account transactions, and net lending, NIPAs
    'W987RC1A027NBEA', # Gross private domestic investment: Domestic business
    'W988RC1A027NBEA', # Gross private domestic investment: Households and institutions
    'W173RC1A027NBEA', # Net domestic fixed investment
    'W171RC1A027NBEA', # Net domestic investment
    'A889RC1A027NBEA', # Net domestic investment: Government
    'A890RC1A027NBEA', # Net domestic investment: Government: Federal
    'A893RC1A027NBEA', # Net domestic investment: Government: State and local
    'A557RC1A027NBEA', # Net domestic investment: Private
    'W790RC1A027NBEA', # Net domestic investment: Private: Domestic business
    'W791RC1A027NBEA', # Net domestic investment: Private: Households and institutions
    'A560RC1A027NBEA', # Net private domestic investment: Net fixed investment
    'Y080RC1A027NBEA', # Private domestic investment: Fixed investment: Nonresidential: Equipment: Consumption of fixed capital
    'Y083RC1A027NBEA', # Private domestic investment: Fixed investment: Nonresidential: Intellectual property products: Consumption of fixed capital
    'Y081RC1A027NBEA', # Private domestic investment: Fixed investment: Nonresidential: Net equipment
    'Y084RC1A027NBEA', # Private domestic investment: Fixed investment: Nonresidential: Net intellectual property products
    ## Bil. of Chn. 2005 $ (NSA)
    'A747RX1A020NBEA', # Real net fixed investment: Net nonresidential: Net equipment and software (DISCONTINUED)
    ## Bil. of Chn. 2017 $ (NSA)
    'W172RX1A020NBEA', # Real gross domestic fixed investment
    'W170RX1A020NBEA', # Real gross domestic investment
    'A680RX1A020NBEA', # Real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Industrial equipment
    'A937RX1A020NBEA', # Real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Information processing equipment: Other
    'A862RX1A020NBEA', # Real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Other equipment
    'A681RX1A020NBEA', # Real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Transportation equipment
    'B985RX1A020NBEA', # Real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Intellectual property products: Software
    'A679RX1A020NBEA', # Real gross private domestic investment: Fixed investment: Nonresidential: Information processing equipment and software
    'W173RX1A020NBEA', # Real net domestic fixed investment
    'W256RX1A020NBEA', # Real net domestic income
    'W171RX1A020NBEA', # Real net domestic investment
    'A362RX1A020NBEA', # Real net domestic product
    'W367RX1A020NBEA', # Real net domestic purchases
    'A560RX1A020NBEA', # Real net fixed investment
    'A593RX1A020NBEA', # Real net fixed investment: Net nonresidential
    'A594RX1A020NBEA', # Real net fixed investment: Net nonresidential: Net structures
    'B009RX1A020NBEA', # Real net fixed investment: Net nonresidential: Structures
    'A748RX1A020NBEA', # Real net fixed investment: Net residential
    'A557RX1A020NBEA', # Real net private domestic investment
    'Y080RX1A020NBEA', # Real private domestic investment: Fixed investment: Nonresidential: Consumption of fixed capital
    'Y083RX1A020NBEA', # Real private domestic investment: Fixed investment: Nonresidential: Intellectual property products: Consumption of fixed capital
    'Y081RX1A020NBEA', # Real private domestic investment: Fixed investment: Nonresidential: Net equipment
    'Y084RX1A020NBEA', # Real private domestic investment: Fixed investment: Nonresidential: Net intellectual property products
    ## Percentage Points at Annual Rate (NSA)
    'A006RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment
    'A007RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Fixed investment
    'A008RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Fixed investment: Nonresidential
    'A010RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Fixed investment: Nonresidential: Equipment and software (DISCONTINUED)
    'A680RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Industrial equipment
    'B935RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Information processing equipment: Computers and peripheral equipment
    'A937RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Information processing equipment: Other
    'A862RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Other equipment
    'A681RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Transportation equipment
    'A679RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Fixed investment: Nonresidential: Information processing equipment and software (DISCONTINUED)
    'B985RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Fixed investment: Nonresidential: Intellectual property products: Software
    'A009RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Fixed investment: Nonresidential: Structures
    'A011RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Fixed investment: Residential
    'A006RY2A224NBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment
    'A007RY2A224NBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Fixed investment
    'A008RY2A224NBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential
    'A010RY2A224NBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Equipment and software (DISCONTINUED)
    'A680RY2A224NBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Industrial equipment
    'B935RY2A224NBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Information processing equipment: Computers and peripheral equipment
    'A937RY2A224NBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Information processing equipment: Other
    'A862RY2A224NBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Other equipment
    'A681RY2A224NBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Equipment: Transportation equipment
    'A679RY2A224NBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Information processing equipment and software (DISCONTINUED)
    'B985RY2A224NBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Intellectual property products: Software
    'A009RY2A224NBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Fixed investment: Nonresidential: Structures
    'A011RY2A224NBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Fixed investment: Residential

    # Domestic Capital Account (Saving & Investment) > Inventories (126)
    ## Bil. of $ (NSA)
    'K160271A027NBEA', # Accumulation of produced assets: Change in private inventories (DISCONTINUED)
    'A145RC1A027NBEA', # Automobile output: Change in private inventories of new and used autos
    'B146RC1A027NBEA', # Automobile output: Change in private inventories of new autos
    'B147RC1A027NBEA', # Automobile output: Change in private inventories of used autos
    'N355RC1A027NBEA', # Change in private inventories: Durable goods industries
    'B018RC1A027NBEA', # Change in private inventories: Farm
    'N150RC1A027NBEA', # Change in private inventories: Manufacturing
    'N624RC1A027NBEA', # Change in private inventories: Manufacturing: Durable goods industries
    'N625RC1A027NBEA', # Change in private inventories: Manufacturing: Nondurable goods industries
    'N151RC1A027NBEA', # Change in private inventories: Merchant wholesale trade
    'N626RC1A027NBEA', # Change in private inventories: Merchant wholesale trade: Durable goods industries
    'N627RC1A027NBEA', # Change in private inventories: Merchant wholesale trade: Nondurable goods industries
    'N541RC1A027NBEA', # Change in private inventories: Mining, utilities, and construction
    'N357RC1A027NBEA', # Change in private inventories: Nondurable goods industries
    'A015RC1A027NBEA', # Change in private inventories: Nonfarm
    'B016RC1A027NBEA', # Change in private inventories: Nonfarm: Change in book value
    'B017RC1A027NBEA', # Change in private inventories: Nonfarm: Inventory valuation adjustment
    'A150RC1A027NBEA', # Change in private inventories: Nonfarm: Manufacturing
    'A624RC1A027NBEA', # Change in private inventories: Nonfarm: Manufacturing: Durable goods
    'A625RC1A027NBEA', # Change in private inventories: Nonfarm: Manufacturing: Nondurable goods
    'A154RC1A027NBEA', # Change in private inventories: Nonfarm: Other durable and nondurable goods
    'A636RC1A027NBEA', # Change in private inventories: Nonfarm: Other: Durable goods
    'A637RC1A027NBEA', # Change in private inventories: Nonfarm: Other: Nondurable goods
    'A153RC1A027NBEA', # Change in private inventories: Nonfarm: Retail trade
    'A630RC1A027NBEA', # Change in private inventories: Nonfarm: Retail trade: Durable goods
    'A631RC1A027NBEA', # Change in private inventories: Nonfarm: Retail trade: Durable goods: Motor vehicle dealers
    'A632RC1A027NBEA', # Change in private inventories: Nonfarm: Retail trade: Durable goods: Other
    'A633RC1A027NBEA', # Change in private inventories: Nonfarm: Retail trade: Nondurable goods
    'A658RC1A027NBEA', # Change in private inventories: Nonfarm: Wholesale trade
    'A661RC1A027NBEA', # Change in private inventories: Nonfarm: Wholesale trade: Durable goods
    'A626RC1A027NBEA', # Change in private inventories: Nonfarm: Wholesale trade: Merchant wholesalers: Durable goods
    'A627RC1A027NBEA', # Change in private inventories: Nonfarm: Wholesale trade: Merchant wholesalers: Nondurable goods
    'A664RC1A027NBEA', # Change in private inventories: Nonfarm: Wholesale trade: Nondurable goods
    'A151RC1A027NBEA', # Change in private inventories: Nonfarm: Wholesale trade: Nondurable goods: Merchant wholesalers
    'A152RC1A027NBEA', # Change in private inventories: Nonfarm: Wholesale trade: Nondurable goods: Nonmerchant wholesalers
    'A628RC1A027NBEA', # Change in private inventories: Nonfarm: Wholesale trade: Nonmerchant wholesalers: Durable goods
    'A629RC1A027NBEA', # Change in private inventories: Nonfarm: Wholesale trade: Nonmerchant wholesalers: Nondurable goods
    'N152RC1A027NBEA', # Change in private inventories: Nonmerchant wholesale trade
    'N154RC1A027NBEA', # Change in private inventories: Other industries
    'N153RC1A027NBEA', # Change in private inventories: Retail trade
    'N542RC1A027NBEA', # Change in private inventories: Retail trade: Food and beverage stores
    'N543RC1A027NBEA', # Change in private inventories: Retail trade: General merchandise stores
    'N631RC1A027NBEA', # Change in private inventories: Retail trade: Motor vehicle and parts dealers
    'N558RC1A027NBEA', # Change in private inventories: Retail trade: Other retail stores
    'N658RC1A027NBEA', # Change in private inventories: Wholesale trade
    'N661RC1A027NBEA', # Change in private inventories: Wholesale trade: Durable goods industries
    'N664RC1A027NBEA', # Change in private inventories: Wholesale trade: Nondurable goods industries
    'A355RC1A027NBEA', # Gross domestic product: Durable goods: Change in private inventories
    'A357RC1A027NBEA', # Gross domestic product: Nondurable goods: Change in private inventories
    'AB65RC1A027NBEA', # Motor vehicle output: Change in private inventories
    'AB71RC1A027NBEA', # Motor vehicle output: Change in private inventories: Autos: New: Domestic
    'AB72RC1A027NBEA', # Motor vehicle output: Change in private inventories: Autos: New: Foreign
    'B709RC1A027NBEA', # Motor vehicle output: Change in private inventories: Trucks
    'W244RC1A027NBEA', # Motor vehicle output: Change in private inventories: Trucks: New
    'AB73RC1A027NBEA', # Motor vehicle output: Change in private inventories: Trucks: New: Domestic
    'AB74RC1A027NBEA', # Motor vehicle output: Change in private inventories: Trucks: New: Foreign
    'W245RC1A027NBEA', # Motor vehicle output: Change in private inventories: Trucks: Used
    'K160521A027NBEA', # Produced assets, closing balance: Private inventories (DISCONTINUED)
    'K160051A027NBEA', # Produced assets, opening balance: Private inventories (DISCONTINUED)
    'K160421A027NBEA', # Revaluation of produced assets: Neutral holding gains or losses (-): Private inventories (DISCONTINUED)
    'K160471A027NBEA', # Revaluation of produced assets: Real holding gains or losses (-): Private inventories (DISCONTINUED)
    ## Bil. of Chn. 2009 $ (NSA)
    'B015RX1A020NBEA', # Change in real private inventories: Nonfarm (DISCONTINUED)
    ## Bil. of Chn. 2017 $ (NSA)
    'N355RX1A020NBEA', # Change in real private inventories: Durable goods industries
    'B018RX1A020NBEA', # Change in real private inventories: Farm
    'N150RX1A020NBEA', # Change in real private inventories: Manufacturing
    'N624RX1A020NBEA', # Change in real private inventories: Manufacturing: Durable goods industries
    'N625RX1A020NBEA', # Change in real private inventories: Manufacturing: Nondurable goods industries
    'N151RX1A020NBEA', # Change in real private inventories: Merchant wholesale trade
    'N626RX1A020NBEA', # Change in real private inventories: Merchant wholesale trade: Durable goods industries
    'N627RX1A020NBEA', # Change in real private inventories: Merchant wholesale trade: Nondurable goods industries
    'N541RX1A020NBEA', # Change in real private inventories: Mining, utilities, and construction
    'N357RX1A020NBEA', # Change in real private inventories: Nondurable goods industries
    'A150RX1A020NBEA', # Change in real private inventories: Nonfarm: Manufacturing
    'C624RX1A020NBEA', # Change in real private inventories: Nonfarm: Manufacturing: Durable goods
    'C625RX1A020NBEA', # Change in real private inventories: Nonfarm: Manufacturing: Nondurable goods
    'A154RX1A020NBEA', # Change in real private inventories: Nonfarm: Other durable and nondurable goods
    'C636RX1A020NBEA', # Change in real private inventories: Nonfarm: Other: Durable goods
    'C637RX1A020NBEA', # Change in real private inventories: Nonfarm: Other: Nondurable goods
    'A153RX1A020NBEA', # Change in real private inventories: Nonfarm: Retail trade
    'C630RX1A020NBEA', # Change in real private inventories: Nonfarm: Retail trade: Durable goods
    'C631RX1A020NBEA', # Change in real private inventories: Nonfarm: Retail trade: Durable goods: Motor vehicle dealers
    'A632RX1A020NBEA', # Change in real private inventories: Nonfarm: Retail trade: Durable goods: Other
    'C633RX1A020NBEA', # Change in real private inventories: Nonfarm: Retail trade: Nondurable goods
    'A658RX1A020NBEA', # Change in real private inventories: Nonfarm: Wholesale trade
    'A661RX1A020NBEA', # Change in real private inventories: Nonfarm: Wholesale trade: Durable goods
    'C626RX1A020NBEA', # Change in real private inventories: Nonfarm: Wholesale trade: Merchant wholesalers: Durable goods
    'C627RX1A020NBEA', # Change in real private inventories: Nonfarm: Wholesale trade: Merchant wholesalers: Nondurable goods
    'A664RX1A020NBEA', # Change in real private inventories: Nonfarm: Wholesale trade: Nondurable goods
    'A151RX1A020NBEA', # Change in real private inventories: Nonfarm: Wholesale trade: Nondurable goods: Merchant wholesalers
    'A152RX1A020NBEA', # Change in real private inventories: Nonfarm: Wholesale trade: Nonmerchant wholesalers
    'C628RX1A020NBEA', # Change in real private inventories: Nonfarm: Wholesale trade: Nonmerchant wholesalers: Durable goods
    'C629RX1A020NBEA', # Change in real private inventories: Nonfarm: Wholesale trade: Nonmerchant wholesalers: Nondurable goods
    'N152RX1A020NBEA', # Change in real private inventories: Nonmerchant wholesale trade
    'N154RX1A020NBEA', # Change in real private inventories: Other industries
    'A969RX1A020NBEA', # Change in real private inventories: Residual
    'N969RX1A020NBEA', # Change in real private inventories: Residual
    'N153RX1A020NBEA', # Change in real private inventories: Retail trade
    'N542RX1A020NBEA', # Change in real private inventories: Retail trade: Food and beverage stores
    'N543RX1A020NBEA', # Change in real private inventories: Retail trade: General merchandise stores
    'N631RX1A020NBEA', # Change in real private inventories: Retail trade: Motor vehicle and parts dealers
    'N558RX1A020NBEA', # Change in real private inventories: Retail trade: Other retail stores
    'N658RX1A020NBEA', # Change in real private inventories: Wholesale trade
    'N661RX1A020NBEA', # Change in real private inventories: Wholesale trade: Durable goods industries
    'N664RX1A020NBEA', # Change in real private inventories: Wholesale trade: Nondurable goods industries
    'A355RX1A020NBEA', # Real gross domestic product: Durable goods: Change in private inventories
    'A357RX1A020NBEA', # Real gross domestic product: Nondurable goods: Change in private inventories
    'A015RX1A020NBEA', # Real gross private domestic investment: Change in private inventories: Nonfarm
    'AB65RX1A020NBEA', # Real motor vehicle output: Change in private inventories
    'A145RX1A020NBEA', # Real motor vehicle output: Change in private inventories: Autos
    'B146RX1A020NBEA', # Real motor vehicle output: Change in private inventories: Autos: New
    'AB71RX1A020NBEA', # Real motor vehicle output: Change in private inventories: Autos: New: Domestic
    'AB72RX1A020NBEA', # Real motor vehicle output: Change in private inventories: Autos: New: Foreign
    'B147RX1A020NBEA', # Real motor vehicle output: Change in private inventories: Autos: Used
    'B709RX1A020NBEA', # Real motor vehicle output: Change in private inventories: Trucks
    'W244RX1A020NBEA', # Real motor vehicle output: Change in private inventories: Trucks: New
    'AB73RX1A020NBEA', # Real motor vehicle output: Change in private inventories: Trucks: New: Domestic
    'AB74RX1A020NBEA', # Real motor vehicle output: Change in private inventories: Trucks: New: Foreign
    'W245RX1A020NBEA', # Real motor vehicle output: Change in private inventories: Trucks: Used
    ## Percentage Points at Annual Rate (NSA)
    'A014RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Change in private inventories
    'B018RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Change in private inventories: Farm
    'A015RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Gross private domestic investment: Change in private inventories: Nonfarm
    'A355RY2A224NBEA', # Contributions to percent change in real gross domestic product: Durable goods: Change in private inventories
    'A014RY2A224NBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Change in private inventories
    'B018RY2A224NBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Change in private inventories: Farm
    'A015RY2A224NBEA', # Contributions to percent change in real gross domestic product: Gross private domestic investment: Change in private inventories: Nonfarm
    'A357RY2A224NBEA', # Contributions to percent change in real gross domestic product: Nondurable goods: Change in private inventories

    # Domestic Capital Account (Saving & Investment) > Noncorporate Business (78)
    ## Bil. of $ (NSA)
    'W461RC1A027NBEA', # National income: Domestic business: Noncorporate business
    'W474RC1A027NBEA', # National income: Domestic business: Noncorporate business: Government enterprises
    'W468RC1A027NBEA', # National income: Domestic business: Noncorporate business: Net interest
    'A1650C1A027NBEA', # National income: Domestic business: Noncorporate business: Other private business
    'W473RC1A027NBEA', # National income: Domestic business: Noncorporate business: Other private business: Taxes on production and imports less subsidies plus business current transfer payments
    'W469RC1A027NBEA', # National income: Domestic business: Noncorporate business: Taxes on production and imports less subsidies plus business current transfer payments
    ## Mil. of $ (NSA)
    'B1835C0A144NBEA', # Inventory valuation adjustment to nonfarm incomes: Noncorporate business: Construction
    'N1835C0A144NBEA', # Inventory valuation adjustment to nonfarm incomes: Noncorporate business: Construction
    'A1836C0A144NBEA', # Inventory valuation adjustment to nonfarm incomes: Noncorporate business: Manufacturing
    'N1836C0A144NBEA', # Inventory valuation adjustment to nonfarm incomes: Noncorporate business: Manufacturing
    'B1837C0A144NBEA', # Inventory valuation adjustment to nonfarm incomes: Noncorporate business: Manufacturing: Durable goods
    'N1837C0A144NBEA', # Inventory valuation adjustment to nonfarm incomes: Noncorporate business: Manufacturing: Durable goods
    'B1838C0A144NBEA', # Inventory valuation adjustment to nonfarm incomes: Noncorporate business: Manufacturing: Nondurable goods
    'N1838C0A144NBEA', # Inventory valuation adjustment to nonfarm incomes: Noncorporate business: Manufacturing: Nondurable goods
    'B1834C0A144NBEA', # Inventory valuation adjustment to nonfarm incomes: Noncorporate business: Mining
    'N1834C0A144NBEA', # Inventory valuation adjustment to nonfarm incomes: Noncorporate business: Mining
    'B1841C0A144NBEA', # Inventory valuation adjustment to nonfarm incomes: Noncorporate business: Other
    'N1841C0A144NBEA', # Inventory valuation adjustment to nonfarm incomes: Noncorporate business: Other
    'B1840C0A144NBEA', # Inventory valuation adjustment to nonfarm incomes: Noncorporate business: Retail trade
    'N1840C0A144NBEA', # Inventory valuation adjustment to nonfarm incomes: Noncorporate business: Retail trade
    'B1839C0A144NBEA', # Inventory valuation adjustment to nonfarm incomes: Noncorporate business: Wholesale trade
    'N1839C0A144NBEA', # Inventory valuation adjustment to nonfarm incomes: Noncorporate business: Wholesale trade
    'B179RC0A144NBEA', # National income: Proprietors' income with IVA: Nonfarm (DISCONTINUED)
    'A1700C0A144NBEA', # Noncorporate capital consumption allowances
    'N1725C0A144NBEA', # Noncorporate capital consumption allowances: Accommodation and food services
    'B1703C0A144NBEA', # Noncorporate capital consumption allowances: Agricultural services, forestry, and fishing
    'A1701C0A144NBEA', # Noncorporate capital consumption allowances: Agriculture, forestry, and fishing
    'N1701C0A144NBEA', # Noncorporate capital consumption allowances: Agriculture, forestry, fishing, and hunting
    'B2622C0A144NBEA', # Noncorporate capital consumption allowances: Amusement and recreation services
    'N1724C0A144NBEA', # Noncorporate capital consumption allowances: Arts, entertainment, and recreation
    'N1723C0A144NBEA', # Noncorporate capital consumption allowances: Arts, entertainment, recreation, accommodation, and food services
    'B2619C0A144NBEA', # Noncorporate capital consumption allowances: Auto repair, services, and parking
    'B2618C0A144NBEA', # Noncorporate capital consumption allowances: Business services
    'B1711C0A144NBEA', # Noncorporate capital consumption allowances: Communication
    'B1705C0A144NBEA', # Noncorporate capital consumption allowances: Construction
    'N1706C0A144NBEA', # Noncorporate capital consumption allowances: Construction
    'N1721C0A144NBEA', # Noncorporate capital consumption allowances: Educational services
    'N1720C0A144NBEA', # Noncorporate capital consumption allowances: Educational services, health care, and social assistance
    'B1702C0A144NBEA', # Noncorporate capital consumption allowances: Farms
    'N1702C0A144NBEA', # Noncorporate capital consumption allowances: Farms
    'B1716C0A144NBEA', # Noncorporate capital consumption allowances: Finance and insurance
    'N1715C0A144NBEA', # Noncorporate capital consumption allowances: Finance and insurance
    'A1715C0A144NBEA', # Noncorporate capital consumption allowances: Finance, insurance, and real estate
    'N1714C0A144NBEA', # Noncorporate capital consumption allowances: Finance, insurance, real estate, rental, and leasing
    'N1703C0A144NBEA', # Noncorporate capital consumption allowances: Forestry, fishing, and related activities
    'N1722C0A144NBEA', # Noncorporate capital consumption allowances: Health care and social assistance
    'B2623C0A144NBEA', # Noncorporate capital consumption allowances: Health services
    'N1713C0A144NBEA', # Noncorporate capital consumption allowances: Information
    'B2624C0A144NBEA', # Noncorporate capital consumption allowances: Legal services
    'N1719C0A144NBEA', # Noncorporate capital consumption allowances: Management of companies and enterprises; administrative and waste management services
    'A1706C0A144NBEA', # Noncorporate capital consumption allowances: Manufacturing
    'N1707C0A144NBEA', # Noncorporate capital consumption allowances: Manufacturing
    'B1707C0A144NBEA', # Noncorporate capital consumption allowances: Manufacturing: Durable goods
    'N1708C0A144NBEA', # Noncorporate capital consumption allowances: Manufacturing: Durable goods
    'B1708C0A144NBEA', # Noncorporate capital consumption allowances: Manufacturing: Nondurable goods
    'N1709C0A144NBEA', # Noncorporate capital consumption allowances: Manufacturing: Nondurable goods
    'B1704C0A144NBEA', # Noncorporate capital consumption allowances: Mining
    'N1704C0A144NBEA', # Noncorporate capital consumption allowances: Mining
    'B2620C0A144NBEA', # Noncorporate capital consumption allowances: Miscellaneous repair services
    'N1726C0A144NBEA', # Noncorporate capital consumption allowances: Other services, except government
    'B2617C0A144NBEA', # Noncorporate capital consumption allowances: Personal services
    'N1717C0A144NBEA', # Noncorporate capital consumption allowances: Professional and business services
    'N1718C0A144NBEA', # Noncorporate capital consumption allowances: Professional, scientific, and technical services
    'A1717C0A144NBEA', # Noncorporate capital consumption allowances: Real estate
    'N1716C0A144NBEA', # Noncorporate capital consumption allowances: Real estate and rental and leasing
    'B1714C0A144NBEA', # Noncorporate capital consumption allowances: Retail trade
    'N1711C0A144NBEA', # Noncorporate capital consumption allowances: Retail trade
    'B1720C0A144NBEA', # Noncorporate capital consumption allowances: Services
    'B2616C0A144NBEA', # Noncorporate capital consumption allowances: Services: Hotels and other lodging places
    'B2621C0A144NBEA', # Noncorporate capital consumption allowances: Services: Motion pictures
    'B2625C0A144NBEA', # Noncorporate capital consumption allowances: Services: Other
    'B1710C0A144NBEA', # Noncorporate capital consumption allowances: Transportation
    'A1709C0A144NBEA', # Noncorporate capital consumption allowances: Transportation and public utilities
    'B1712C0A144NBEA', # Noncorporate capital consumption allowances: Transportation and public utilities: Electric, gas, and sanitary services
    'N1712C0A144NBEA', # Noncorporate capital consumption allowances: Transportation and warehousing
    'N1705C0A144NBEA', # Noncorporate capital consumption allowances: Utilities
    'B1713C0A144NBEA', # Noncorporate capital consumption allowances: Wholesale trade
    'N1710C0A144NBEA', # Noncorporate capital consumption allowances: Wholesale trade

    # Domestic Capital Account (Saving & Investment) > Private Fixed Investments (343)
    ## % Chg. from Preceding Period (NSA)
    'A007RL1A225NBEA', # Real Gross Private Domestic Investment: Fixed Investment
    'A008RL1A225NBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential
    'Y033RL1A225NBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment
    'A680RL1A225NBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment: Industrial Equipment
    'Y034RL1A225NBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment: Information Processing Equipment
    'B935RL1A225NBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment: Information Processing Equipment: Computers and Peripheral Equipment
    'A937RL1A225NBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment: Information Processing Equipment: Other
    'A862RL1A225NBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment: Other Equipment
    'A681RL1A225NBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment: Transportation Equipment
    'Y001RL1A225NBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products
    'Y020RL1A225NBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products: Entertainment, Literary, and Artistic Originals
    'Y006RL1A225NBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products: Research and Development
    'B985RL1A225NBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products: Software
    'A009RL1A225NBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Structures
    'A011RL1A225NBEA', # Real Gross Private Domestic Investment: Fixed Investment: Residential
    'AB76RL1A225NBEA', # Real Private Fixed Investment in New Autos and New Light Trucks
    'B009RL1A225NBEA', # Real Private Fixed Investment: Nonresidential: Structures (DISCONTINUED)
    'W001RL1A225NBEA', # Real Private Fixed Investment: Nonresidential: Structures: Commercial and Health Care
    'C307RL1A225NBEA', # Real Private Fixed Investment: Nonresidential: Structures: Manufacturing
    'E318RL1A225NBEA', # Real Private Fixed Investment: Nonresidential: Structures: Mining Exploration, Shafts, and Wells
    'W004RL1A225NBEA', # Real Private Fixed Investment: Nonresidential: Structures: Other Structures
    'W003RL1A225NBEA', # Real Private Fixed Investment: Nonresidential: Structures: Power and Communication
    'A679RL1A225NBEA', # Real Private Fixed Investment: Private Fixed Investment in Information Processing Equipment and Software
    'W040RL1A225NBEA', # Real Private Fixed Investment: Private Fixed Investment in New Structures
    'A771RL1A225NBEA', # Real Private Fixed Investment: Private Fixed Investment in New Structures: Nonresidential Structures
    'A756RL1A225NBEA', # Real Private Fixed Investment: Private Fixed Investment in New Structures: Residential Structures
    'A349RL1A225NBEA', # Real Private Fixed Investment: Private Fixed Investment in Structures
    'B013RL1A225NBEA', # Real Private Fixed Investment: Residential: Equipment
    'A012RL1A225NBEA', # Real Private Fixed Investment: Residential: Structures
    'A863RL1A225NBEA', # Real Private Fixed Investment: Residential: Structures: Other Structures
    'A943RL1A225NBEA', # Real Private Fixed Investment: Residential: Structures: Permanent Site
    'C292RL1A225NBEA', # Real Private Fixed Investment: Residential: Structures: Permanent Site: Multifamily
    'A944RL1A225NBEA', # Real Private Fixed Investment: Residential: Structures: Permanent Site: Single Family
    ## Bil. of $ (NSA)
    'A138RC1A027NBEA', # Automobile output: Private fixed investment (DISCONTINUED)
    'B139RC1A027NBEA', # Automobile output: Private fixed investment: New autos
    'Y033RC1A027NBEA', # Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment
    'Y034RC1A027NBEA', # Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment: Information Processing Equipment
    'Y001RC1A027NBEA', # Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products
    'Y020RC1A027NBEA', # Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products: Entertainment, Literary, and Artistic Originals
    'Y006RC1A027NBEA', # Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products: Research and Development
    'AB62RC1A027NBEA', # Motor vehicle output: Private fixed investment
    'A327RC1A027NBEA', # Private fixed investment in equipment and software (DISCONTINUED)
    'B549RC1A027NBEA', # Private fixed investment in equipment and software: Dealers' margin on used equipment
    'B550RC1A027NBEA', # Private fixed investment in equipment and software: Net purchases of used equipment from government
    'B554RC1A027NBEA', # Private fixed investment in equipment and software: Net sales of used equipment
    'C268RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Agricultural machinery
    'C269RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Construction machinery
    'A670RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Electrical equipment, n.e.c.
    'A667RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Furniture and fixtures
    'C276RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Industrial equipment: Electrical transmission, distribution, and industrial apparatus
    'A668RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Industrial equipment: Engines and turbines
    'C263RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Industrial equipment: Fabricated metal products
    'C273RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Industrial equipment: General industrial, including materials handling, equipment
    'C271RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Industrial equipment: Metalworking machinery
    'C272RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Industrial equipment: Special industry machinery, n.e.c.
    'C275RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Information processing equipment and software: Communication equipment
    'W175RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Information processing equipment and software: Computers, software, and communication (DISCONTINUED)
    'W176RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Information processing equipment and software: Medical equipment and instruments
    'W177RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Information processing equipment and software: Nonmedical instruments
    'B936RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Information processing equipment and software: Office and accounting equipment
    'C285RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Information processing equipment and software: Photocopy and related equipment
    'C270RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Mining and oilfield machinery
    'A682RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Other equipment - furniture and fixtures, agricultural, construction, mining and oilfield, service industry machinery, electrical equipment n.e.c.
    'C286RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Other equipment n.e.c.
    'C287RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Sale of equipment scrap, excluding autos
    'C570RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Service industry machinery
    'C281RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Transportation equipment: Aircraft
    'C280RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Transportation equipment: Autos
    'W178RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Transportation equipment: Light trucks (including utility vehicles)
    'W179RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Transportation equipment: Other trucks, buses, and truck trailers
    'C283RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Transportation equipment: Railroad equipment
    'C282RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Transportation equipment: Ships and boats
    'C279RC1A027NBEA', # Private fixed investment in equipment and software: Nonresidential: Transportation equipment: Trucks, buses, and truck trailers
    'B556RC1A027NBEA', # Private fixed investment in equipment and software: Sale of equipment scrap
    'AB76RC1A027NBEA', # Private fixed investment in new autos and new light trucks
    'A763RC1A027NBEA', # Private fixed investment in new equipment and software (DISCONTINUED)
    'W040RC1A027NBEA', # Private fixed investment in new structures
    'A771RC1A027NBEA', # Private fixed investment in new structures: Nonresidential structures
    'A756RC1A027NBEA', # Private fixed investment in new structures: Residential structures
    'A349RC1A027NBEA', # Private fixed investment in structures
    'W046RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Amusement and recreation
    'C321RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Brokers' commissions on sale of structures
    'W037RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Commercial and health care: Food and beverage establishments
    'W036RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Commercial and health care: Multimerchandise shopping
    'W031RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Commercial and health care: Office
    'W039RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Commercial and health care: Other commercial
    'W038RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Commercial and health care: Warehouses
    'C314RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Communication
    'W044RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Educational and vocational
    'C316RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Farm
    'W032RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Health care
    'W035RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Health care: Medical buildings
    'W033RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Hospitals
    'C311RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Hospitals and special care
    'W034RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Hospitals and special care: Special care
    'W045RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Lodging
    'C320RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Mining
    'C319RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Mining exploration, shafts, and wells: Petroleum and natural gas
    'E322RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Net purchases of used structures
    'W050RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Other miscellaneous structures
    'W029RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Other power
    'W028RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Power
    'C571RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Power: Electric
    'C309RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Religious
    'W047RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Transportation
    'W048RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Transportation: Air
    'W049RC1A027NBEA', # Private fixed investment in structures: Nonresidential: Transportation: Land
    'A758RC1A027NBEA', # Private fixed investment in structures: Residential: Brokers' commissions on sale of structures
    'C295RC1A027NBEA', # Private fixed investment in structures: Residential: Dormitories
    'A946RC1A027NBEA', # Private fixed investment in structures: Residential: Improvements
    'A945RC1A027NBEA', # Private fixed investment in structures: Residential: Manufactured homes
    'A759RC1A027NBEA', # Private fixed investment in structures: Residential: Net purchases of used structures
    'W242RC1A027NBEA', # Private fixed investment: Net purchases of used autos and used light trucks
    'W243RC1A027NBEA', # Private fixed investment: Net purchases of used light trucks (including utility vehicles)
    'AB68RC1A027NBEA', # Private fixed investment: New motor vehicles
    'B196RC1A027NBEA', # Private fixed investment: New motor vehicles: Light trucks (including utility vehicles)
    'B705RC1A027NBEA', # Private fixed investment: New motor vehicles: Trucks
    'B197RC1A027NBEA', # Private fixed investment: New motor vehicles: Trucks: Other
    'A680RC1A027NBEA', # Private fixed investment: Nonresidential: Equipment: Industrial equipment
    'B935RC1A027NBEA', # Private fixed investment: Nonresidential: Equipment: Information processing equipment: Computers and peripheral equipment
    'A937RC1A027NBEA', # Private fixed investment: Nonresidential: Equipment: Information processing equipment: Other
    'A862RC1A027NBEA', # Private fixed investment: Nonresidential: Equipment: Other equipment
    'A681RC1A027NBEA', # Private fixed investment: Nonresidential: Equipment: Transportation equipment
    'B985RC1A027NBEA', # Private fixed investment: Nonresidential: Intellectual property products: Software
    'W004RC1A027NBEA', # Private fixed investment: Nonresidential: Other structures
    'W001RC1A027NBEA', # Private fixed investment: Nonresidential: Structures: Commercial and health care
    'C307RC1A027NBEA', # Private fixed investment: Nonresidential: Structures: Manufacturing
    'E318RC1A027NBEA', # Private fixed investment: Nonresidential: Structures: Mining exploration, shafts, and wells
    'W003RC1A027NBEA', # Private fixed investment: Nonresidential: Structures: Power and communication
    'A679RC1A027NBEA', # Private fixed investment: Private fixed investment in information processing equipment and software
    'B013RC1A027NBEA', # Private fixed investment: Residential: Equipment
    'A863RC1A027NBEA', # Private fixed investment: Residential: Other structures
    'A012RC1A027NBEA', # Private fixed investment: Residential: Structures
    'A943RC1A027NBEA', # Private fixed investment: Residential: Structures: Permanent site
    'C292RC1A027NBEA', # Private fixed investment: Residential: Structures: Permanent site: Multifamily
    'A944RC1A027NBEA', # Private fixed investment: Residential: Structures: Permanent site: Single family
    ## Bil. of Chn. 2005 $ (NSA)
    'A327RX1A020NBEA', # Real private fixed investment in equipment and software (DISCONTINUED)
    'W175RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential: Information processing equipment and software: Computers, software, and communication (DISCONTINUED)
    'A970RX1A020NBEA', # Real private fixed investment in equipment and software: Residual (DISCONTINUED)
    ## Bil. of Chn. 2017 $ (NSA)
    'Y033RX1A020NBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment
    'Y034RX1A020NBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Equipment: Information Processing Equipment
    'Y001RX1A020NBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products
    'Y020RX1A020NBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products: Entertainment, Literary, and Artistic Originals
    'Y006RX1A020NBEA', # Real Gross Private Domestic Investment: Fixed Investment: Nonresidential: Intellectual Property Products: Research and Development
    'AB62RX1A020NBEA', # Real motor vehicle output: Private fixed investment
    'C268RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential equipment: Agricultural machinery
    'C269RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential equipment: Construction machinery
    'A670RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential equipment: Electrical equipment, n.e.c.
    'A667RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential equipment: Furniture and fixtures
    'C270RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential equipment: Mining and oilfield machinery
    'C286RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential equipment: Other
    'A682RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential equipment: Other equipment-furniture and fixtures, agricultural, construction, mining and oilfield, service industry machinery, electrical equipment n.e.c.
    'C570RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential equipment: Service industry machinery
    'C276RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential: Industrial equipment: Electrical transmission, distribution, and industrial apparatus
    'A668RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential: Industrial equipment: Engines and turbines
    'C263RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential: Industrial equipment: Fabricated metal products
    'C273RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential: Industrial equipment: General industrial, including materials handling, equipment
    'C271RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential: Industrial equipment: Metalworking machinery
    'C272RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential: Industrial equipment: Special industry machinery, n.e.c.
    'C275RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential: Information processing equipment and software: Computers, software, and communication: Communication equipment
    'W176RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential: Information processing equipment and software: Medical equipment and instruments
    'W177RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential: Information processing equipment and software: Nonmedical instruments
    'B936RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential: Information processing equipment and software: Office and accounting equipment
    'C285RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential: Information processing equipment and software: Photocopy and related equipment
    'C287RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential: Sale of equipment scrap, excluding autos
    'C281RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential: Transportation equipment: Aircraft
    'C280RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential: Transportation equipment: Autos
    'C283RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential: Transportation equipment: Railroad equipment
    'C282RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential: Transportation equipment: Ships and boats
    'C279RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential: Transportation equipment: Trucks, buses, and truck trailers
    'W178RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential: Transportation equipment: Trucks, buses, and truck trailers: Light trucks (including utility vehicles)
    'W179RX1A020NBEA', # Real private fixed investment in equipment and software: Nonresidential: Transportation equipment: Trucks, buses, and truck trailers: Other trucks, buses, and truck trailers
    'AB76RX1A020NBEA', # Real private fixed investment in new autos and new light trucks
    'W040RX1A020NBEA', # Real private fixed investment in new structures
    'A771RX1A020NBEA', # Real private fixed investment in new structures: Nonresidential structures
    'A756RX1A020NBEA', # Real private fixed investment in new structures: Residential structures
    'A349RX1A020NBEA', # Real private fixed investment in structures
    'W046RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Amusement and recreation
    'C321RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Brokers' commissions on sale of structures
    'W037RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Commercial and health care: Food and beverage establishments
    'W036RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Commercial and health care: Multimerchandise shopping
    'W031RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Commercial and health care: Office
    'W039RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Commercial and health care: Other commercial
    'W038RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Commercial and health care: Warehouses
    'C314RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Communication
    'W044RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Educational and vocational
    'C316RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Farm
    'W032RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Health care
    'W035RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Health care: Medical buildings
    'W033RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Hospitals
    'C311RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Hospitals and special care
    'W034RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Hospitals and special care: Special care
    'W045RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Lodging
    'C320RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Mining
    'C319RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Mining exploration, shafts, and wells: Petroleum and natural gas
    'E322RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Net purchases of used structures
    'W050RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Other
    'W028RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Power
    'C571RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Power: Electric
    'W029RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Power: Other power
    'C309RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Religious
    'W047RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Transportation
    'W048RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Transportation: Air
    'W049RX1A020NBEA', # Real private fixed investment in structures: Nonresidential: Transportation: Land
    'A758RX1A020NBEA', # Real private fixed investment in structures: Residential: Brokers' commissions on sale of structures
    'C295RX1A020NBEA', # Real private fixed investment in structures: Residential: Dormitories
    'A946RX1A020NBEA', # Real private fixed investment in structures: Residential: Improvements
    'A945RX1A020NBEA', # Real private fixed investment in structures: Residential: Manufactured homes
    'A759RX1A020NBEA', # Real private fixed investment in structures: Residential: Net purchases of used structures
    'A971RX1A020NBEA', # Real private fixed investment in structures: Residual
    'B140RX1A020NBEA', # Real private fixed investment: Net purchases of used autos
    'W242RX1A020NBEA', # Real private fixed investment: Net purchases of used autos and used light trucks
    'W243RX1A020NBEA', # Real private fixed investment: Net purchases of used light trucks (including utility vehicles)
    'AB68RX1A020NBEA', # Real private fixed investment: New motor vehicles
    'B139RX1A020NBEA', # Real private fixed investment: New motor vehicles: Autos
    'B196RX1A020NBEA', # Real private fixed investment: New motor vehicles: Light trucks (including utility vehicles)
    'B705RX1A020NBEA', # Real private fixed investment: New motor vehicles: Trucks
    'B197RX1A020NBEA', # Real private fixed investment: New motor vehicles: Trucks: Other
    'W001RX1A020NBEA', # Real private fixed investment: Nonresidential: Structures: Commercial and health care
    'C307RX1A020NBEA', # Real private fixed investment: Nonresidential: Structures: Manufacturing
    'E318RX1A020NBEA', # Real private fixed investment: Nonresidential: Structures: Mining exploration, shafts, and wells
    'W004RX1A020NBEA', # Real private fixed investment: Nonresidential: Structures: Other structures
    'W003RX1A020NBEA', # Real private fixed investment: Nonresidential: Structures: Power and communication
    'B013RX1A020NBEA', # Real private fixed investment: Residential: Equipment
    'A012RX1A020NBEA', # Real private fixed investment: Residential: Structures
    'A863RX1A020NBEA', # Real private fixed investment: Residential: Structures: Other structures
    'A943RX1A020NBEA', # Real private fixed investment: Residential: Structures: Permanent site
    'C292RX1A020NBEA', # Real private fixed investment: Residential: Structures: Permanent site: Multifamily
    'A944RX1A020NBEA', # Real private fixed investment: Residential: Structures: Permanent site: Single family
    'A972RX1A020NBEA', # Real private fixed investment: Residual
    ## Percentage Points at Annual Rate (NSA)
    'Y033RZ2A224NBEA', # Contributions to Percent Change in Real Private Fixed Investment: Nonresidential: Equipment
    'Y034RZ2A224NBEA', # Contributions to Percent Change in Real Private Fixed Investment: Nonresidential: Equipment: Information Processing Equipment
    'Y001RZ2A224NBEA', # Contributions to Percent Change in Real Private Fixed Investment: Nonresidential: Intellectual Property Products
    'Y020RZ2A224NBEA', # Contributions to Percent Change in Real Private Fixed Investment: Nonresidential: Intellectual Property Products: Entertainment, Literary, and Artistic Originals
    'Y006RZ2A224NBEA', # Contributions to Percent Change in Real Private Fixed Investment: Nonresidential: Intellectual Property Products: Research and Development
    'B010RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential equipment and software (DISCONTINUED)
    'C268RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Agricultural machinery
    'C269RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Construction machinery
    'A670RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Electrical equipment, n.e.c.
    'A667RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Furniture and fixtures
    'A680RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Industrial equipment
    'C276RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Industrial equipment: Electrical transmission, distribution, and industrial apparatus
    'A668RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Industrial equipment: Engines and turbines
    'C263RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Industrial equipment: Fabricated metal products
    'C273RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Industrial equipment: General industrial, including materials handling, equipment
    'C271RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Industrial equipment: Metalworking machinery
    'C272RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Industrial equipment: Special industry machinery, n.e.c.
    'A679RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Information processing equipment and software (DISCONTINUED)
    'C275RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Information processing equipment and software: Communication equipment
    'B935RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Information processing equipment and software: Computers and peripheral equipment
    'W175RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Information processing equipment and software: Computers, software, and communication (DISCONTINUED)
    'W176RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Information processing equipment and software: Medical equipment and instruments
    'W177RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Information processing equipment and software: Nonmedical instruments
    'B936RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Information processing equipment and software: Office and accounting equipment
    'C285RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Information processing equipment and software: Photocopy and related equipment
    'B985RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Information processing equipment and software: Software
    'C270RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Mining and oilfield machinery
    'A682RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Other equipment - furniture and fixtures, agricultural, construction, mining and oilfield, service industry machinery, electrical equipment n.e.c.
    'C286RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Other equipment n.e.c.
    'C287RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Sale of equipment scrap, excluding autos
    'C570RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Service industry machinery
    'A681RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Transportation equipment
    'C281RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Transportation equipment: Aircraft
    'C280RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Transportation equipment: Autos
    'W178RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Transportation equipment: Light trucks (including utility vehicles)
    'W179RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Transportation equipment: Other trucks, buses, and truck trailers
    'C283RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Transportation equipment: Railroad equipment
    'C282RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Transportation equipment: Ships and boats
    'C279RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Nonresidential: Transportation equipment: Trucks, buses, and truck trailers
    'B013RW2A224NBEA', # Contributions to percent change in real private fixed investment in equipment and software: Residential equipment
    'W040RW2A224NBEA', # Contributions to percent change in real private fixed investment in new structures
    'A771RW2A224NBEA', # Contributions to percent change in real private fixed investment in new structures: Nonresidential structures
    'A756RW2A224NBEA', # Contributions to percent change in real private fixed investment in new structures: Residential structures
    'B009RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential
    'W046RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Amusement and recreation
    'C321RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Brokers' commissions on sale of structures
    'W001RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Commercial and health care
    'W037RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Commercial and health care: Food and beverage establishments
    'W036RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Commercial and health care: Multimerchandise shopping
    'W031RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Commercial and health care: Office
    'W039RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Commercial and health care: Other commercial
    'W038RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Commercial and health care: Warehouses
    'C314RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Communication
    'W044RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Educational and vocational
    'C316RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Farm
    'W032RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Health care
    'W035RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Health care: Medical buildings
    'W033RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Hospitals
    'C311RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Hospitals and special care
    'W034RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Hospitals and special care: Special care
    'W045RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Lodging
    'C307RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Manufacturing
    'C320RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Mining
    'E318RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Mining exploration, shafts, and wells
    'C319RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Mining exploration, shafts, and wells: Petroleum and natural gas
    'E322RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Net purchases of used structures
    'W050RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Other miscellaneous structures
    'W029RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Other power
    'W004RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Other structures - religious, educational and vocational, lodging, amusement and recreation, transportation, and farm
    'W028RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Power
    'W003RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Power and communication
    'C571RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Power: Electric
    'C309RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Religious
    'W047RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Transportation
    'W048RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Transportation: Air
    'W049RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Nonresidential: Transportation: Land
    'A012RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Residential
    'A758RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Residential: Brokers' commissions on sale of structures
    'C295RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Residential: Dormitories
    'A946RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Residential: Improvements
    'A945RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Residential: Manufactured homes
    'A759RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Residential: Net purchases of used structures
    'A863RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Residential: Other structures - manufactured homes, dormitories, improvements, brokers' commissions on sales of structures
    'A943RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Residential: Permanent site
    'C292RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Residential: Permanent site: Multifamily structures
    'A944RW2A224NBEA', # Contributions to percent change in real private fixed investment in structures: Residential: Permanent site: Single-family structures
    'A008RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Nonresidential
    'B010RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Equipment and software (DISCONTINUED)
    'A680RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Equipment: Industrial equipment
    'B935RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Equipment: Information processing equipment: Computers and peripheral equipment
    'A937RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Equipment: Information processing equipment: Other
    'A862RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Equipment: Other equipment
    'A681RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Equipment: Transportation equipment
    'B985RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Intellectual property products: Software
    'W004RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Other structures
    'B009RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Structures
    'W001RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Structures: Commercial and health care
    'C307RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Structures: Manufacturing
    'E318RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Structures: Mining exploration, shafts, and wells
    'W003RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Nonresidential: Structures: Power and communication
    'A327RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Private fixed investment in equipment and software (DISCONTINUED)
    'A679RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Private fixed investment in information processing equipment and software
    'W040RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Private fixed investment in new structures
    'A771RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Private fixed investment in new structures: Nonresidential structures
    'A756RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Private fixed investment in new structures: Residential structures
    'A349RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Private fixed investment in structures
    'A011RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Residential
    'B013RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Residential: Equipment
    'A863RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Residential: Other structures
    'A012RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Residential: Structures
    'A943RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Residential: Structures: Permanent site
    'C292RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Residential: Structures: Permanent site: Multifamily
    'A944RZ2A224NBEA', # Contributions to percent change in real private fixed investment: Residential: Structures: Permanent site: Single family

]
