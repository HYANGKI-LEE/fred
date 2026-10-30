# FRED > National Accounts > National Income & Product Accounts > Gov't Receipts, Expenditures & Investment (category_id 107)
# https://fred.stlouisfed.org/categories/107  하위 카테고리 + 직속 시리즈 전체. 주기는 FRED 메타데이터 기준
# 위계: # 카테고리 > ## 단위 (계절조정)
dir='us_macro_NIPA_Govt_Receipts_Expenditures'
category_ids = [107]  # build_db.py가 이 카테고리(하위 포함) 메타데이터를 일괄 조회

# Quarterly (871)
ids_Q = [
    # Gov't Receipts, Expenditures & Investment (483)
    ## % (NSA)
    'VAPGDPG', # Value Added by Industry: Government as a Percentage of GDP
    'VAPGDPF', # Value Added by Industry: Government: Federal as a Percentage of GDP
    'VAPGDPSL', # Value Added by Industry: Government: State and Local as a Percentage of GDP
    ## % Chg. (SAAR)
    'GOPIPG', # Gross Output by Industry: Government (Chain-Type Price Index)
    'GOQIPG', # Gross Output by Industry: Government (Chain-Type Quantity Index)
    'GOPIPF', # Gross Output by Industry: Government: Federal (Chain-Type Price Index)
    'GOQIPF', # Gross Output by Industry: Government: Federal (Chain-Type Quantity Index)
    'GOPIPSL', # Gross Output by Industry: Government: State and Local (Chain-Type Price Index)
    'GOQIPSL', # Gross Output by Industry: Government: State and Local (Chain-Type Quantity Index)
    'IIPIPG', # Intermediate Inputs by Industry: Government (Chain-Type Price Index)
    'IIQIPG', # Intermediate Inputs by Industry: Government (Chain-Type Quantity Index)
    'IIPIPF', # Intermediate Inputs by Industry: Government: Federal (Chain-Type Price Index)
    'IIQIPF', # Intermediate Inputs by Industry: Government: Federal (Chain-Type Quantity Index)
    'IIPIPSL', # Intermediate Inputs by Industry: Government: State and Local (Chain-Type Price Index)
    'IIQIPSL', # Intermediate Inputs by Industry: Government: State and Local (Chain-Type Quantity Index)
    'VAPIPG', # Value Added by Industry: Government (Chain-Type Price Index)
    'VAQIPG', # Value Added by Industry: Government (Chain-Type Quantity Index)
    'VAPIPF', # Value Added by Industry: Government: Federal (Chain-Type Price Index)
    'VAQIPF', # Value Added by Industry: Government: Federal (Chain-Type Quantity Index)
    'VAPIPSL', # Value Added by Industry: Government: State and Local (Chain-Type Price Index)
    'VAQIPSL', # Value Added by Industry: Government: State and Local (Chain-Type Quantity Index)
    ## % Chg. from Preceding Period (SAAR)
    'A822RL1Q225SBEA', # Real Government Consumption Expenditures and Gross Investment
    'A823RL1Q225SBEA', # Real Government Consumption Expenditures and Gross Investment: Federal
    'A824RL1Q225SBEA', # Real Government Consumption Expenditures and Gross Investment: Federal: National Defense
    'A825RL1Q225SBEA', # Real Government Consumption Expenditures and Gross Investment: Federal: Nondefense
    'A542RL1Q225SBEA', # Real Government Consumption Expenditures and Gross Investment: Federal: Nondefense: Consumption Expenditures
    'A829RL1Q225SBEA', # Real Government Consumption Expenditures and Gross Investment: State and Local
    'W101RL1Q225SBEA', # Real Gross Output of General Government
    'W104RL1Q225SBEA', # Real Gross Output of General Government: Intermediate Goods and Services Purchased
    'W105RL1Q225SBEA', # Real Gross Output of General Government: Intermediate Goods and Services Purchased: Durable Goods
    'W106RL1Q225SBEA', # Real Gross Output of General Government: Intermediate Goods and Services Purchased: Nondurable Goods
    'W107RL1Q225SBEA', # Real Gross Output of General Government: Intermediate Goods and Services Purchased: Services
    'W102RL1Q225SBEA', # Real Gross Output of General Government: Value Added
    'A194RL1Q225SBEA', # Real Gross Output of General Government: Value Added: Compensation of General Government Employees
    'B999RL1Q225SBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Durable Goods: Aircraft
    'B388RL1Q225SBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Durable Goods: Electronics
    'B277RL1Q225SBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Durable Goods: Missiles
    'B389RL1Q225SBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Durable Goods: Other Durable Goods
    'B278RL1Q225SBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Durable Goods: Ships
    'B288RL1Q225SBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Durable Goods: Vehicles
    'B781RL1Q225SBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Nondurable Goods: Ammunition
    'B783RL1Q225SBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Nondurable Goods: Other Nondurable Goods
    'B780RL1Q225SBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Nondurable Goods: Petroleum Products
    'B911RL1Q225SBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Services: Installation Support
    'B913RL1Q225SBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Services: Personnel Support
    'B786RL1Q225SBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Services: Transportation of Material
    'B785RL1Q225SBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Services: Travel of Persons
    'B912RL1Q225SBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Services: Weapons Support
    'W090RL1Q225SBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Value Added: Compensation of General Government Employees: Civilian
    'B4080L1Q225SBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Value Added: Compensation of General Government Employees: Military
    'B874RL1Q225SBEA', # Real National Defense Gross Investment: Equipment: Aircraft
    'Y051RL1Q225SBEA', # Real National Defense Gross Investment: Equipment: Electronics
    'B875RL1Q225SBEA', # Real National Defense Gross Investment: Equipment: Missiles
    'B879RL1Q225SBEA', # Real National Defense Gross Investment: Equipment: Other Equipment
    'B876RL1Q225SBEA', # Real National Defense Gross Investment: Equipment: Ships
    'B877RL1Q225SBEA', # Real National Defense Gross Investment: Equipment: Vehicles
    ## % Chg. from Qtr.  1 Yr. Ago (NSA)
    'OB000330Q', # Real Federal Consumption Expenditures and Gross Investment
    'OB000333Q', # Real Government Consumption Expenditures and Gross Investment
    'OB000351Q', # Real State and Local Consumption Expenditures and Gross Investment
    ## % Chg. from Qtr.  1 Yr. Ago (SA)
    'A822RO1Q156NBEA', # Real Government Consumption Expenditures and Gross Investment
    'A823RO1Q156NBEA', # Real Government Consumption Expenditures and Gross Investment: Federal
    'A824RO1Q156NBEA', # Real Government Consumption Expenditures and Gross Investment: Federal: National Defense
    'A825RO1Q156NBEA', # Real Government Consumption Expenditures and Gross Investment: Federal: Nondefense
    'A829RO1Q156NBEA', # Real Government Consumption Expenditures and Gross Investment: State and Local
    ## Bil. of $ (NSA)
    'L318461Q027NBEA', # Cash payments to the public: Coverage differences: Net investment (DISCONTINUED)
    'M318501Q027NBEA', # Federal government budget surplus or deficit (-)
    'L318191Q027NBEA', # Federal government cash payments to the public (DISCONTINUED)
    'L318201Q027NBEA', # Federal government cash payments to the public: Coverage differences (DISCONTINUED)
    'L318271Q027NBEA', # Federal government cash payments to the public: Coverage differences: District of Columbia (DISCONTINUED)
    'L318281Q027NBEA', # Federal government cash payments to the public: Coverage differences: Federal Home Loan Banks and Federal Land Banks (DISCONTINUED)
    'L318221Q027NBEA', # Federal government cash payments to the public: Coverage differences: Federal employee retirement plan transactions (DISCONTINUED)
    'L318261Q027NBEA', # Federal government cash payments to the public: Coverage differences: Federal employee retirement plan transactions: Administrative expenses (DISCONTINUED)
    'L318251Q027NBEA', # Federal government cash payments to the public: Coverage differences: Federal employee retirement plan transactions: Benefits paid (DISCONTINUED)
    'L318241Q027NBEA', # Federal government cash payments to the public: Coverage differences: Federal employee retirement plan transactions: Contributions received (employer) (DISCONTINUED)
    'L318231Q027NBEA', # Federal government cash payments to the public: Coverage differences: Federal employee retirement plan transactions: Interest received (DISCONTINUED)
    'L318311Q027NBEA', # Federal government cash payments to the public: Coverage differences: Financial transactions (DISCONTINUED)
    'L318321Q027NBEA', # Federal government cash payments to the public: Coverage differences: Financial transactions: Loan disbursements less loan repayments and sales (DISCONTINUED)
    'L318331Q027NBEA', # Federal government cash payments to the public: Coverage differences: Financial transactions: Net purchases of foreign currency (DISCONTINUED)
    'L318291Q027NBEA', # Federal government cash payments to the public: Coverage differences: Net investment (DISCONTINUED)
    'L318341Q027NBEA', # Federal government cash payments to the public: Coverage differences: Other (DISCONTINUED)
    'L318351Q027NBEA', # Federal government cash payments to the public: Netting and grossing differences (DISCONTINUED)
    'W702LC1Q027NBEA', # Federal government cash payments to the public: Netting and grossing differences: Current surplus of government enterprises (DISCONTINUED)
    'W703LC1Q027NBEA', # Federal government cash payments to the public: Netting and grossing differences: Interest receipts (DISCONTINUED)
    'L318371Q027NBEA', # Federal government cash payments to the public: Netting and grossing differences: Other (DISCONTINUED)
    'L318381Q027NBEA', # Federal government cash payments to the public: Timing differences (DISCONTINUED)
    'L318431Q027NBEA', # Federal government cash payments to the public: Timing differences: Checks outstanding and certain other accounts (DISCONTINUED)
    'L318411Q027NBEA', # Federal government cash payments to the public: Timing differences: Current transfer payments (DISCONTINUED)
    'L318401Q027NBEA', # Federal government cash payments to the public: Timing differences: Interest payments (DISCONTINUED)
    'L318391Q027NBEA', # Federal government cash payments to the public: Timing differences: Purchases (increase in payables net of advances) (DISCONTINUED)
    'L318421Q027NBEA', # Federal government cash payments to the public: Timing differences: Subsidies (DISCONTINUED)
    'L318011Q027NBEA', # Federal government cash receipts from the public (DISCONTINUED)
    'L318021Q027NBEA', # Federal government cash receipts from the public: Coverage differences (DISCONTINUED)
    'L318041Q027NBEA', # Federal government cash receipts from the public: Coverage differences: Contributions received by federal employee retirement plans (DISCONTINUED)
    'L318071Q027NBEA', # Federal government cash receipts from the public: Coverage differences: District of Columbia (DISCONTINUED)
    'L318061Q027NBEA', # Federal government cash receipts from the public: Coverage differences: Financial transactions (DISCONTINUED)
    'L318081Q027NBEA', # Federal government cash receipts from the public: Coverage differences: Other (DISCONTINUED)
    'L318091Q027NBEA', # Federal government cash receipts from the public: Netting and grossing differences (DISCONTINUED)
    'W700LC1Q027NBEA', # Federal government cash receipts from the public: Netting and grossing differences: Current surplus of government enterprises (DISCONTINUED)
    'W701LC1Q027NBEA', # Federal government cash receipts from the public: Netting and grossing differences: Interest receipts (DISCONTINUED)
    'L318111Q027NBEA', # Federal government cash receipts from the public: Netting and grossing differences: Other (DISCONTINUED)
    'L318121Q027NBEA', # Federal government cash receipts from the public: Timing differences (DISCONTINUED)
    'L318161Q027NBEA', # Federal government cash receipts from the public: Timing differences: Excise taxes (DISCONTINUED)
    'L318141Q027NBEA', # Federal government cash receipts from the public: Timing differences: Federal and state unemployment insurance taxes (DISCONTINUED)
    'L318171Q027NBEA', # Federal government cash receipts from the public: Timing differences: Other (DISCONTINUED)
    'L318451Q027NBEA', # Federal government consolidated cash budget surplus or deficit (-) (DISCONTINUED)
    'B098RU1Q027NBEA', # Federal government current expenditures: Wage accruals less disbursements (DISCONTINUED)
    'W005RU1Q027NBEA', # Federal government current receipts (DISCONTINUED)
    'M318181Q027NBEA', # Federal government current receipts, NIPAs
    'L318181Q027NBEA', # Federal government current receipts, NIPAs (DISCONTINUED)
    'W780RU1Q027NBEA', # Federal government current receipts: Contributions for government social insurance (DISCONTINUED)
    'B097RU1Q027NBEA', # Federal government current receipts: Current surplus of government enterprises (DISCONTINUED)
    'W009RU1Q027NBEA', # Federal government current receipts: Income receipts on assets (DISCONTINUED)
    'W006RU1Q027NBEA', # Federal government current tax receipts (DISCONTINUED)
    'W008RU1Q027NBEA', # Federal government current tax receipts: Taxes from the rest of the world (DISCONTINUED)
    'W007RU1Q027NBEA', # Federal government current tax receipts: Taxes on production and imports (DISCONTINUED)
    'M318191Q027NBEA', # Federal government expenditures: Budget outlays
    'M318201Q027NBEA', # Federal government expenditures: Coverage differences (NIPA vs. Budget)
    'M318221Q027NBEA', # Federal government expenditures: Coverage differences: Federal employee retirement plan transactions (NIPA vs. Budget)
    'M318261Q027NBEA', # Federal government expenditures: Coverage differences: Federal employee retirement plan transactions: Administrative expenses (NIPA vs. Budget)
    'M318251Q027NBEA', # Federal government expenditures: Coverage differences: Federal employee retirement plan transactions: Benefits paid (NIPA vs. Budget)
    'M318241Q027NBEA', # Federal government expenditures: Coverage differences: Federal employee retirement plan transactions: Contributions received (employer) (NIPA vs. Budget)
    'M318231Q027NBEA', # Federal government expenditures: Coverage differences: Federal employee retirement plan transactions: Interest received (NIPA vs. Budget)
    'M318311Q027NBEA', # Federal government expenditures: Coverage differences: Financial transactions (NIPA vs. Budget)
    'B1069C1Q027NBEA', # Federal government expenditures: Coverage differences: Financial transactions: Deposit insurance (NIPA vs. Budget)
    'M318321Q027NBEA', # Federal government expenditures: Coverage differences: Financial transactions: Loan disbursements less loan repayments and sales (NIPA vs. Budget)
    'M318341Q027NBEA', # Federal government expenditures: Coverage differences: Financial transactions: Net purchases of foreign currency (NIPA vs. Budget)
    'M318351Q027NBEA', # Federal government expenditures: Coverage differences: Financial transactions: Other (NIPA vs. Budget)
    'M318271Q027NBEA', # Federal government expenditures: Coverage differences: Financing disbursements from credit programs (NIPA vs. Budget)
    'M318291Q027NBEA', # Federal government expenditures: Coverage differences: Net investment (NIPA vs. Budget)
    'M318511Q027NBEA', # Federal government expenditures: Coverage differences: Net investment (NIPA vs. Budget) (DISCONTINUED)
    'M318361Q027NBEA', # Federal government expenditures: Coverage differences: Net purchases of nonproduced assets (NIPA vs. Budget)
    'M318381Q027NBEA', # Federal government expenditures: Coverage differences: Net purchases of nonproduced assets: Land and other (NIPA vs. Budget) (DISCONTINUED)
    'M318371Q027NBEA', # Federal government expenditures: Coverage differences: Net purchases of nonproduced assets: Outer Continental Shelf (NIPA vs. Budget) (DISCONTINUED)
    'M318391Q027NBEA', # Federal government expenditures: Coverage differences: Other (NIPA vs. Budget)
    'M318281Q027NBEA', # Federal government expenditures: Coverage differences: Other differences in funds covered (NIPA vs. Budget)
    'M318401Q027NBEA', # Federal government expenditures: Netting and grossing differences
    'W707MC1Q027NBEA', # Federal government expenditures: Netting and grossing differences: Current surplus of government enterprises
    'W706MC1Q027NBEA', # Federal government expenditures: Netting and grossing differences: Interest receipts
    'M318431Q027NBEA', # Federal government expenditures: Netting and grossing differences: Other
    'M318411Q027NBEA', # Federal government expenditures: Netting and grossing differences: Supplementary medical insurance premiums
    'M318441Q027NBEA', # Federal government expenditures: Timing differences (NIPA vs. Budget)
    'M318471Q027NBEA', # Federal government expenditures: Timing differences: Current transfer payments (NIPA vs. Budget)
    'M318461Q027NBEA', # Federal government expenditures: Timing differences: Interest payments (NIPA vs. Budget)
    'W708MC1Q027NBEA', # Federal government expenditures: Timing differences: Other (NIPA vs. Budget)
    'M318451Q027NBEA', # Federal government expenditures: Timing differences: Purchases (increase in payables net of advances) (NIPA vs. Budget)
    'M318011Q027NBEA', # Federal government receipts: Budget receipts
    'M318021Q027NBEA', # Federal government receipts: Coverage differences (NIPA vs. Budget)
    'M318041Q027NBEA', # Federal government receipts: Coverage differences: Contributions received by federal employee retirement plans (NIPA vs. Budget)
    'M318061Q027NBEA', # Federal government receipts: Coverage differences: Financial transactions (NIPA vs. Budget)
    'M318071Q027NBEA', # Federal government receipts: Coverage differences: Other (NIPA vs. Budget)
    'M318081Q027NBEA', # Federal government receipts: Netting and grossing differences
    'W705MC1Q027NBEA', # Federal government receipts: Netting and grossing differences: Current surplus of government enterprises
    'W704MC1Q027NBEA', # Federal government receipts: Netting and grossing differences: Interest receipts
    'M318111Q027NBEA', # Federal government receipts: Netting and grossing differences: Other
    'M318091Q027NBEA', # Federal government receipts: Netting and grossing differences: Supplementary medical insurance premiums
    'M318121Q027NBEA', # Federal government receipts: Timing differences (NIPA vs. Budget)
    'M318161Q027NBEA', # Federal government receipts: Timing differences: Excise taxes (NIPA vs. Budget)
    'M318141Q027NBEA', # Federal government receipts: Timing differences: Federal and state unemployment insurance taxes (NIPA vs. Budget)
    'M318171Q027NBEA', # Federal government receipts: Timing differences: Other (NIPA vs. Budget)
    'M318561Q027NBEA', # Federal government saving, national income and product accounts
    'A923RU1Q027NBEA', # Net federal government saving (DISCONTINUED)
    'L318511Q027NBEA', # Net federal government saving, national income and product accounts (DISCONTINUED)
    'A924RU1Q027NBEA', # Net state and local government saving (DISCONTINUED)
    'B116RU1Q027NBEA', # State and local government current expenditures: Wage accruals less disbursements (DISCONTINUED)
    'W023RU1Q027NBEA', # State and local government current receipts (DISCONTINUED)
    'B104RU1Q027NBEA', # State and local government current receipts: Contributions for government social insurance (DISCONTINUED)
    'B115RU1Q027NBEA', # State and local government current receipts: Current surplus of government enterprises (DISCONTINUED)
    'W075RU1Q027NBEA', # State and local government current receipts: Current transfer receipts (DISCONTINUED)
    'W076RU1Q027NBEA', # State and local government current receipts: Current transfer receipts: from business (net) (DISCONTINUED)
    'B246RU1Q027NBEA', # State and local government current receipts: Current transfer receipts: from persons (DISCONTINUED)
    'W074RU1Q027NBEA', # State and local government current receipts: Income receipts on assets (DISCONTINUED)
    'W070RU1Q027NBEA', # State and local government current tax receipts (DISCONTINUED)
    'W072RU1Q027NBEA', # State and local government current tax receipts: Taxes on production and imports (DISCONTINUED)
    ## Bil. of $ (SAAR)
    'B202RC1Q027SBEA', # Compensation of employees: Wages and salaries: Government
    'A061RC1Q027SBEA', # Contributions for government social insurance, domestic
    'FGCE', # Federal Consumption Expenditures and Gross Investment
    'FGRECPT', # Federal Government Current Receipts
    'FGEXPND', # Federal Government: Current Expenditures
    'FDEFX', # Federal Government: National Defense Consumption Expenditures and Gross Investment
    'DGI', # Federal Government: National Defense Gross Investment
    'FNDEFX', # Federal Government: Nondefense Consumption Expenditures and Gross Investment
    'NDGI', # Federal Nondefense Gross Investment
    'W020RC1Q027SBEA', # Federal government capital transfer payments
    'W086RC1Q027SBEA', # Federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Value added
    'B237RC1Q027SBEA', # Federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Value added: Compensation of general government employees
    'B432RC1Q027SBEA', # Federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Value added: Consumption of general government fixed capital
    'W111RC1Q027SBEA', # Federal government consumption expenditures: Gross output of general government: Value added
    'B568RC1Q027SBEA', # Federal government consumption expenditures: Gross output of general government: Value added: Compensation of general government employees
    'W129RC1Q027SBEA', # Federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Value added
    'W130RC1Q027SBEA', # Federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Value added: Compensation of general government employees
    'B546RC1Q027SBEA', # Federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Value added: Consumption of general government fixed capital
    'A091RC1Q027SBEA', # Federal government current expenditures: Interest payments
    'B098RC1Q027SBEA', # Federal government current expenditures: Wage accruals less disbursements (DISCONTINUED)
    'W780RC1Q027SBEA', # Federal government current receipts: Contributions for government social insurance
    'B097RC1Q027SBEA', # Federal government current receipts: Current surplus of government enterprises
    'W009RC1Q027SBEA', # Federal government current receipts: Income receipts on assets
    'W053RC1Q027SBEA', # Federal government current receipts: Income receipts on assets: Dividends
    'B094RC1Q027SBEA', # Federal government current receipts: Income receipts on assets: Interest receipts
    'B1040C1Q027SBEA', # Federal government current receipts: Income receipts on assets: Rents and royalties
    'W006RC1Q027SBEA', # Federal government current tax receipts
    'W008RC1Q027SBEA', # Federal government current tax receipts: Taxes from the rest of the world
    'W007RC1Q027SBEA', # Federal government current tax receipts: Taxes on production and imports
    'B235RC1Q027SBEA', # Federal government current tax receipts: Taxes on production and imports: Customs duties
    'B234RC1Q027SBEA', # Federal government current tax receipts: Taxes on production and imports: Excise taxes
    'W014RC1Q027SBEA', # Federal government current transfer payments
    'W010RC1Q027SBEA', # Federal government current transfer payments: Other current transfer payments
    'W017RC1Q027SBEA', # Federal government current transfer payments: Other current transfer payments to the rest of the world
    'FGSL', # Federal government current transfer payments: Other current transfer payments: Grants-in-aid to state and local governments
    'W019RCQ027SBEA', # Federal government total expenditures
    'AD08RC1Q027SBEA', # Federal government total expenditures: Net purchases of nonproduced assets
    'W018RC1Q027SBEA', # Federal government total receipts
    'GCE', # Government Consumption Expenditures and Gross Investment
    'GEXPND', # Government Current Expenditures
    'GRECPT', # Government Current Receipts
    'W069RC1Q027SBEA', # Government capital transfer payments
    'W067RC1Q027SBEA', # Government capital transfer receipts
    'W102RC1Q027SBEA', # Government consumption expenditures: Gross output of general government: Value added
    'A194RC1Q027SBEA', # Government consumption expenditures: Gross output of general government: Value added: Compensation of general government employees
    'A184RC1Q027SBEA', # Government current expenditures: Wage accruals less disbursements (DISCONTINUED)
    'W782RC1Q027SBEA', # Government current receipts: Contributions for government social insurance
    'W054RC1Q027SBEA', # Government current tax receipts
    'A084RC1Q027SBEA', # Government current transfer payments
    'W058RC1Q027SBEA', # Government income receipts on assets
    'W065RC1Q027SBEA', # Government income receipts on assets: Dividends
    'W059RC1Q027SBEA', # Government income receipts on assets: Interest and miscellaneous receipts
    'A391RC1Q027SBEA', # Government saving: Other (excluding social insurance funds)
    'A221RC1Q027SBEA', # Government saving: Social insurance funds
    'W068RCQ027SBEA', # Government total expenditures
    'AD07RC1Q027SBEA', # Government total expenditures: Net purchases of nonproduced assets
    'W066RC1Q027SBEA', # Government total receipts
    'GOG', # Gross Output by Industry: Government
    'GOF', # Gross Output by Industry: Government: Federal
    'GOSL', # Gross Output by Industry: Government: State and Local
    'A926RC1Q027SBEA', # Gross government saving: Federal
    'A925RC1Q027SBEA', # Gross government saving: State and local
    'A765RC1Q027SBEA', # Gross value added: GDP: General government
    'A766RC1Q027SBEA', # Gross value added: GDP: General government: Federal
    'A767RC1Q027SBEA', # Gross value added: GDP: General government: State and local
    'IIG', # Intermediate Inputs by Industry: Government
    'IIF', # Intermediate Inputs by Industry: Government: Federal
    'IISL', # Intermediate Inputs by Industry: Government: State and Local
    'Y051RC1Q027SBEA', # National Defense Gross Investment: Equipment: Electronics
    'B999RC1Q027SBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Aircraft
    'B388RC1Q027SBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Electronics
    'B277RC1Q027SBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Missiles
    'B389RC1Q027SBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Other durable goods
    'B278RC1Q027SBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Ships
    'B288RC1Q027SBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Vehicles
    'B781RC1Q027SBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Ammunition
    'B783RC1Q027SBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Other nondurable goods
    'B780RC1Q027SBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Petroleum products
    'B911RC1Q027SBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Installation support
    'B913RC1Q027SBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Personnel support
    'B784RC1Q027SBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Research and development (DISCONTINUED)
    'B786RC1Q027SBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Transportation of material
    'B785RC1Q027SBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Travel of persons
    'B912RC1Q027SBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Weapons support
    'W090RC1Q027SBEA', # National defense consumption expenditures: Gross output of general government: Value added: Compensation of general government employees: Civilian
    'B4080C1Q027SBEA', # National defense consumption expenditures: Gross output of general government: Value added: Compensation of general government employees: Military
    'B436RC1Q027SBEA', # National income without capital consumption adjustment: Government
    'FGDEF', # Net Federal Government Saving
    'TGDEF', # Net Government Saving
    'SLDEF', # Net State and Local Government Saving
    'B244RC1Q027SBEA', # Net federal government saving: Other (excluding social insurance funds)
    'B243RC1Q027SBEA', # Net federal government saving: Social insurance funds
    'AD01RC1Q027SBEA', # Net lending or net borrowing (-), NIPAs: Government
    'AD02RC1Q027SBEA', # Net lending or net borrowing (-), NIPAs: Government: Federal
    'AD03RC1Q027SBEA', # Net lending or net borrowing (-), NIPAs: Government: State and local
    'B119RC1Q027SBEA', # Net state and local government saving: Other (exluding social insurance funds)
    'B118RC1Q027SBEA', # Net state and local government saving: Social insurance funds
    'W775RC1Q027SBEA', # Saving and investment: Disaster losses: Government
    'W776RC1Q027SBEA', # Saving and investment: Disaster losses: Government: Federal
    'W777RC1Q027SBEA', # Saving and investment: Disaster losses: Government: State and local
    'SLCE', # State and Local Consumption Expenditures & Gross Investment
    'SLEXPND', # State and Local Government Current Expenditures
    'SLINV', # State and Local Government Gross Investment
    'W139RC1Q027SBEA', # State and Local government consumption expenditures: Gross output of general government: Value added
    'B251RC1Q027SBEA', # State and Local government consumption expenditures: Gross output of general government: Value added: Compensation of general government employees
    'W080RC1Q027SBEA', # State and local government capital transfer payments
    'AD06RC1Q027SBEA', # State and local government capital transfer receipts (DISCONTINUED)
    'W023RC1Q027SBEA', # State and local government current receipts
    'B104RC1Q027SBEA', # State and local government current receipts: Contributions for government social insurance
    'B115RC1Q027SBEA', # State and local government current receipts: Current surplus of government enterprises
    'B109RC1Q027SBEA', # State and local government current receipts: Government social benefit payments to persons
    'W074RC1Q027SBEA', # State and local government current receipts: Income receipts on assets
    'B081RC1Q027SBEA', # State and local government current receipts: Income receipts on assets: Dividends
    'B112RC1Q027SBEA', # State and local government current receipts: Income receipts on assets: Interest receipts
    'S230541Q027SBEA', # State and local government current receipts: Income receipts on assets: Rents and royalties
    'B111RC1Q027SBEA', # State and local government current receipts: Interest payments
    'B114RC1Q027SBEA', # State and local government current receipts: Subsidies
    'B116RC1Q027SBEA', # State and local government current receipts: Wage accruals less disbursements (DISCONTINUED)
    'W070RC1Q027SBEA', # State and local government current tax receipts
    'W072RC1Q027SBEA', # State and local government current tax receipts: Taxes on production and imports
    'W073RC1Q027SBEA', # State and local government current tax receipts: Taxes on production and imports: Other
    'B249RC1Q027SBEA', # State and local government current tax receipts: Taxes on production and imports: Property taxes
    'B248RC1Q027SBEA', # State and local government current tax receipts: Taxes on production and imports: Sales taxes
    'AD09RC1Q027SBEA', # State and local government expenditures: Net purchases of nonproduced assets
    'W079RCQ027SBEA', # State and local government total expenditures
    'W077RC1Q027SBEA', # State and local government total receipts
    'VAG', # Value Added by Industry: Government
    'VAF', # Value Added by Industry: Government: Federal
    'VASL', # Value Added by Industry: Government: State and Local
    ## Bil. of Chn. 2005 $ (SAAR)
    'B784RX1Q020SBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Research and development (DISCONTINUED)
    'B878RX1Q020SBEA', # Real national defense gross investment: Equipment and software: Electronics and software (DISCONTINUED)
    ## Bil. of Chn. 2009 $ (SAAR)
    'FGCEC96', # Real Federal Consumption Expenditures and Gross Investment (DISCONTINUED)
    'GCEC96', # Real Government Consumption Expenditures and Gross Investment (DISCONTINUED)
    'SLCEC96', # Real State and Local Consumption Expenditures & Gross Investment, 1 Decimal (DISCONTINUED)
    ## Bil. of Chn. 2017 $ (NSA)
    'ND000330Q', # Real Federal Consumption Expenditures and Gross Investment
    'ND000333Q', # Real Government Consumption Expenditures and Gross Investment
    'ND000331Q', # Real Government Consumption Expenditures and Gross Investment: Federal: National defense
    'ND000332Q', # Real Government Consumption Expenditures and Gross Investment: Federal: Nondefense
    'ND000351Q', # Real State and Local Consumption Expenditures and Gross Investment
    ## Bil. of Chn. 2017 $ (SAAR)
    'DGIC96', # Federal Government: Real National Defense Gross Investment
    'FGCEC1', # Real Federal Consumption Expenditures and Gross Investment
    'NDGIC96', # Real Federal Nondefense Gross Investment
    'GCEC1', # Real Government Consumption Expenditures and Gross Investment
    'Y051RX1Q020SBEA', # Real National Defense Gross Investment: Equipment: Electronics
    'SLCEC1', # Real State and Local Consumption Expenditures & Gross Investment, 1 Decimal
    'SLINVC96', # Real State and Local Government: Gross Investment
    'RVAG', # Real Value Added by Industry: Government
    'RVAF', # Real Value Added by Industry: Government: Federal
    'RVASL', # Real Value Added by Industry: Government: State and Local
    'W086RX1Q020SBEA', # Real federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Value added
    'B237RX1Q020SBEA', # Real federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Value added: Compensation of general government employees
    'B432RX1Q020SBEA', # Real federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Value added: Consumption of general government fixed capital
    'W111RX1Q020SBEA', # Real federal government consumption expenditures: Gross output of general government: Value added
    'B568RX1Q020SBEA', # Real federal government consumption expenditures: Gross output of general government: Value added: Compensation of general government employees
    'B995RX1Q020SBEA', # Real federal government consumption expenditures: Gross output of general government: Value added: Consumption of general government fixed capital
    'W129RX1Q020SBEA', # Real federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Value added
    'W130RX1Q020SBEA', # Real federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Value added: Compensation of general government employees
    'B546RX1Q020SBEA', # Real federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Value added: Consumption of general government fixed capital
    'W102RX1Q020SBEA', # Real government consumption expenditures: Gross output of general government: Value added
    'A194RX1Q020SBEA', # Real government consumption expenditures: Gross output of general government: Value added: Compensation of general government employees
    'A765RX1Q020SBEA', # Real gross value added: GDP: General government
    'A766RX1Q020SBEA', # Real gross value added: GDP: General government: Federal
    'A767RX1Q020SBEA', # Real gross value added: GDP: General government: State and local
    'B874RX1Q020SBEA', # Real national defense consumption expenditures and gross investment: Gross investment: Equipment: Aircraft
    'B875RX1Q020SBEA', # Real national defense consumption expenditures and gross investment: Gross investment: Equipment: Missiles
    'B879RX1Q020SBEA', # Real national defense consumption expenditures and gross investment: Gross investment: Equipment: Other equipment
    'B876RX1Q020SBEA', # Real national defense consumption expenditures and gross investment: Gross investment: Equipment: Ships
    'B877RX1Q020SBEA', # Real national defense consumption expenditures and gross investment: Gross investment: Equipment: Vehicles
    'A975RX1Q020SBEA', # Real national defense consumption expenditures and gross investment: Residual
    'B999RX1Q020SBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Aircraft
    'B388RX1Q020SBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Electronics
    'B277RX1Q020SBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Missiles
    'B389RX1Q020SBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Other durable goods
    'B278RX1Q020SBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Ships
    'B288RX1Q020SBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Vehicles
    'B781RX1Q020SBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Ammunition
    'B783RX1Q020SBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Other nondurable goods
    'B780RX1Q020SBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Petroleum products
    'B911RX1Q020SBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Installation support
    'B913RX1Q020SBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Personnel support
    'B786RX1Q020SBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Transportation of material
    'B785RX1Q020SBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Travel of persons
    'B912RX1Q020SBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Weapons support
    'W090RX1Q020SBEA', # Real national defense consumption expenditures: Gross output of general government: Value added: Compensation of general government employees: Civilian
    'B4080X1Q020SBEA', # Real national defense consumption expenditures: Gross output of general government: Value added: Compensation of general government employees: Military
    'W139RX1Q020SBEA', # Real state and local government consumption expenditures: Gross output of general government: Value added
    'B251RX1Q020SBEA', # Real state and local government consumption expenditures: Gross output of general government: Value added: Compensation of general government employees
    'B986RX1Q020SBEA', # Real state and local government consumption expenditures: Gross output of general government: Value added: Consumption of general government fixed capital
    ## Index 2017=100 (NSA)
    'NC000330Q', # Federal Consumption Expenditures and Gross Investment
    'NC000333Q', # Government Consumption Expenditures and Gross Investment
    'NB000330Q', # Real Federal Consumption Expenditures and Gross Investment
    'NB000333Q', # Real Government Consumption Expenditures and Gross Investment
    ## Index 2017=100 (SAAR)
    'GOPIG', # Gross Output by Industry: Government (Chain-Type Price Index)
    'GOQIG', # Gross Output by Industry: Government (Chain-Type Quantity Index)
    'GOPIF', # Gross Output by Industry: Government: Federal (Chain-Type Price Index)
    'GOQIF', # Gross Output by Industry: Government: Federal (Chain-Type Quantity Index)
    'GOPISL', # Gross Output by Industry: Government: State and Local (Chain-Type Price Index)
    'GOQISL', # Gross Output by Industry: Government: State and Local (Chain-Type Quantity Index)
    'IIPIG', # Intermediate Inputs by Industry: Government (Chain-Type Price Index)
    'IIQIG', # Intermediate Inputs by Industry: Government (Chain-Type Quantity Index)
    'IIPIF', # Intermediate Inputs by Industry: Government: Federal (Chain-Type Price Index)
    'IIQIF', # Intermediate Inputs by Industry: Government: Federal (Chain-Type Quantity Index)
    'IIPISL', # Intermediate Inputs by Industry: Government: State and Local (Chain-Type Price Index)
    'IIQISL', # Intermediate Inputs by Industry: Government: State and Local (Chain-Type Quantity Index)
    'VAPIG', # Value Added by Industry: Government (Chain-Type Price Index)
    'VAQIG', # Value Added by Industry: Government (Chain-Type Quantity Index)
    'VAPIF', # Value Added by Industry: Government: Federal (Chain-Type Price Index)
    'VAQIF', # Value Added by Industry: Government: Federal (Chain-Type Quantity Index)
    'VAPISL', # Value Added by Industry: Government: State and Local (Chain-Type Price Index)
    'VAQISL', # Value Added by Industry: Government: State and Local (Chain-Type Quantity Index)
    ## Mil. of $ (NSA)
    'IEACTPN', # Capital transfer payments and other debits
    'IEACTRN', # Capital transfer receipts and other credits
    'NA000330Q', # Federal Consumption Expenditures and Gross Investment
    'NA000304Q', # Federal Government Current Receipts
    'NA000283Q', # Federal Government: Current Expenditures
    'NA000308Q', # Federal government current expenditures: Interest payments
    'NA000302Q', # Federal government current receipts: Contributions for government social insurance
    'NA000285Q', # Federal government current receipts: Current surplus of government enterprises
    'NA000278Q', # Federal government current receipts: Income receipts on assets
    'NA000327Q', # Federal government current tax receipts
    'NA000326Q', # Federal government current tax receipts: Taxes from the rest of the world
    'NA000324Q', # Federal government current tax receipts: Taxes on production and imports
    'NA000293Q', # Federal government current transfer payments
    'NA000295Q', # Federal government current transfer payments: Other current transfer payments
    'NA000306Q', # Federal government current transfer payments: Other current transfer payments to the rest of the world (net)
    'NA000296Q', # Federal government current transfer payments: Other current transfer payments: Grants-in-aid to state and local governments
    'NA000297Q', # Federal government current transfer payments: Other current transfer payments: Grants-in-aid to state and local governments
    'NA000333Q', # Government Consumption Expenditures and Gross Investment
    'NA000314Q', # Net Federal Government Saving
    'NA000315Q', # Net State and Local Government Saving
    'NA000317Q', # State and Local Government Gross Investment
    'NA000294Q', # State and Local government current transfer payments
    'NA000284Q', # State and local government current expenditures
    'NA000305Q', # State and local government current receipts
    'NA000303Q', # State and local government current receipts: Contributions for government social insurance
    'NA000286Q', # State and local government current receipts: Current surplus of government enterprises
    'NA000307Q', # State and local government current receipts: Current transfer payments to the rest of the world
    'NA000299Q', # State and local government current receipts: Government social benefit payments to persons
    'NA000279Q', # State and local government current receipts: Income receipts on assets
    'NA000311Q', # State and local government current receipts: Interest payments
    'NA000319Q', # State and local government current receipts: Subsidies
    'NA000328Q', # State and local government current tax receipts
    'NA000325Q', # State and local government current tax receipts: Taxes on production and imports
    ## Mil. of $ (SA)
    'IEACTP', # Capital transfer payments and other debits
    'IEACTR', # Capital transfer receipts and other credits
    ## Percentage Points (SAAR)
    'CPGDPG', # Contributions to Percent Change in Real GDP by Industry: Government
    'CPGDPF', # Contributions to Percent Change in Real GDP by Industry: Government: Federal
    'CPGDPSL', # Contributions to Percent Change in Real GDP by Industry: Government: State and Local
    'CPGDPPIG', # Contributions to Percent Change in the Chain-Type Price Index for GDP by Industry: Government
    'CPGDPPIF', # Contributions to Percent Change in the Chain-Type Price Index for GDP by Industry: Government: Federal
    'CPGDPPISL', # Contributions to Percent Change in the Chain-Type Price Index for GDP by Industry: Government: State and Local
    ## Percentage Points at Annual Rate (SAAR)
    'Y058RZ2Q224SBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Federal: Gross Investment: Equipment
    'Y059RZ2Q224SBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Federal: Gross Investment: Intellectual Property Products
    'Y061RZ2Q224SBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Federal: Gross Investment: Intellectual Property Products: Research and Development
    'Y060RZ2Q224SBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Federal: Gross Investment: Intellectual Property Products: Software
    'Y050RZ2Q224SBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Federal: National Defense: Gross Investment: Equipment
    'Y052RZ2Q224SBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Federal: National Defense: Gross Investment: Intellectual Property Products
    'Y076RZ2Q224SBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Federal: National Defense: Gross Investment: Intellectual Property Products: Research and Development
    'Y053RZ2Q224SBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Federal: National Defense: Gross Investment: Intellectual Property Products: Software
    'Y066RZ2Q224SBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Federal: Nondefense: Gross Investment: Equipment
    'Y067RZ2Q224SBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Federal: Nondefense: Gross Investment: Intellectual Property Products
    'Y069RZ2Q224SBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Federal: Nondefense: Gross Investment: Intellectual Property Products: Research and Development
    'Y068RZ2Q224SBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Federal: Nondefense: Gross Investment: Intellectual Property Products: Software
    'Y054RZ2Q224SBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Gross Investment: Equipment
    'Y055RZ2Q224SBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Gross Investment: Intellectual Property Products
    'Y057RZ2Q224SBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Gross Investment: Intellectual Property Products: Research and Development
    'Y056RZ2Q224SBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Gross Investment: Intellectual Property Products: Software
    'Y070RZ2Q224SBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: State and Local: Gross Investment: Equipment
    'Y071RZ2Q224SBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: State and Local: Gross Investment: Intellectual Property Products
    'Y073RZ2Q224SBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: State and Local: Gross Investment: Intellectual Property Products: Research and Development
    'Y072RZ2Q224SBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: State and Local: Gross Investment: Intellectual Property Products: Software
    'A997RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures
    'W085RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government
    'W087RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased
    'A998RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods
    'B999RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Aircraft
    'B388RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Electronics
    'B277RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Missiles
    'B389RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Other durable goods
    'B278RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Ships
    'B288RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Vehicles
    'A725RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods
    'B781RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Ammunition
    'B783RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Other nondurable goods
    'B780RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Petroleum products
    'A489RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services
    'B911RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Installation support
    'B913RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Personnel support
    'B786RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Transportation of material
    'B785RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Travel of persons
    'B912RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Weapons support
    'W086RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Value added
    'B237RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Value added: Compensation of general government employees
    'W090RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Value added: Compensation of general government employees: Civilian
    'B408RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Value added: Compensation of general government employees: Military
    'B432RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Value added: Consumption of general government fixed capital
    'W088RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Own-account investment
    'W089RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Sales to other sectors
    'A788RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Gross investment
    'Y050RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Gross investment: Equipment
    'B874RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Gross investment: Equipment: Aircraft
    'Y051RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Gross investment: Equipment: Electronics
    'B875RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Gross investment: Equipment: Missiles
    'B879RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Gross investment: Equipment: Other equipment
    'B876RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Gross investment: Equipment: Ships
    'B877RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Gross investment: Equipment: Vehicles
    'Y052RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Gross investment: Intellectual property products
    'Y076RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Gross investment: Intellectual property products: Research and development
    'Y053RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Gross investment: Intellectual property products: Software
    'A808RN2Q224SBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Gross investment: Structures

    # Gov't Receipts, Expenditures & Investment > Gov't Consumption Expenditures (163)
    ## % Chg. from Qtr.  1 Yr. Ago (NSA)
    'OB000331Q', # Real Government Consumption Expenditures and Gross Investment: Federal: National defense
    'OB000332Q', # Real Government Consumption Expenditures and Gross Investment: Federal: Nondefense
    ## Bil. of $ (NSA)
    'A957RU1Q027NBEA', # Federal government consumption expenditures (DISCONTINUED)
    'A787RU1Q027NBEA', # Federal government gross investment (DISCONTINUED)
    'A991RU1Q027NBEA', # State and local government consumption expenditures (DISCONTINUED)
    ## Bil. of $ (SAAR)
    'A957RC1Q027SBEA', # Federal government consumption expenditures
    'W085RC1Q027SBEA', # Federal government consumption expenditures: Defense consumption expenditures: Gross output of general government
    'W087RC1Q027SBEA', # Federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased
    'A998RC1Q027SBEA', # Federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods
    'A725RC1Q027SBEA', # Federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods
    'A489RC1Q027SBEA', # Federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services
    'W088RC1Q027SBEA', # Federal government consumption expenditures: Defense consumption expenditures: Own-account investment
    'W089RC1Q027SBEA', # Federal government consumption expenditures: Defense consumption expenditures: Sales to other sectors
    'W110RC1Q027SBEA', # Federal government consumption expenditures: Gross output of general government
    'W113RC1Q027SBEA', # Federal government consumption expenditures: Gross output of general government: Intermediate goods and services purchased
    'W114RC1Q027SBEA', # Federal government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods
    'W115RC1Q027SBEA', # Federal government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods
    'W116RC1Q027SBEA', # Federal government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services
    'W128RC1Q027SBEA', # Federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government
    'W131RC1Q027SBEA', # Federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Intermediate goods and services purchased
    'A543RC1Q027SBEA', # Federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods
    'A729RC1Q027SBEA', # Federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods
    'B826RC1Q027SBEA', # Federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Commodity Credit Corporation inventory change
    'B828RC1Q027SBEA', # Federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Other nondurable goods
    'A544RC1Q027SBEA', # Federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services
    'W136RC1Q027SBEA', # Federal government consumption expenditures: Nondefense consumption expenditures: Own-account investment
    'W137RC1Q027SBEA', # Federal government consumption expenditures: Nondefense consumption expenditures: Sales to other sectors
    'W117RC1Q027SBEA', # Federal government consumption expenditures: Own-account investment
    'W118RC1Q027SBEA', # Federal government consumption expenditures: Sales to other sectors
    'A955RC1Q027SBEA', # Government consumption expenditures
    'A997RC1Q027SBEA', # Government consumption expenditures: Federal: National defense
    'A542RC1Q027SBEA', # Government consumption expenditures: Federal: Nondefense
    'W101RC1Q027SBEA', # Government consumption expenditures: Gross output of general government
    'W104RC1Q027SBEA', # Government consumption expenditures: Gross output of general government: Intermediate goods and services purchased
    'W105RC1Q027SBEA', # Government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods
    'W106RC1Q027SBEA', # Government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods
    'W107RC1Q027SBEA', # Government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services
    'W108RC1Q027SBEA', # Government consumption expenditures: Own-account investment
    'W109RC1Q027SBEA', # Government consumption expenditures: Sales to other sectors
    'A991RC1Q027SBEA', # Government consumption expenditures: State and local
    'Y712RC1Q027SBEA', # Government current expenditures: Interest payments: to the rest of the world
    'W138RC1Q027SBEA', # State and Local government consumption expenditures: Gross output of general government
    'W140RC1Q027SBEA', # State and Local government consumption expenditures: Gross output of general government: Intermediate goods and services purchased
    'B989RC1Q027SBEA', # State and Local government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods
    'B337RC1Q027SBEA', # State and Local government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods
    'A988RC1Q027SBEA', # State and Local government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services
    'W144RC1Q027SBEA', # State and Local government consumption expenditures: Own-account investment
    'W145RC1Q027SBEA', # State and Local government consumption expenditures: Sales to other sectors
    'B1066C1Q027SBEA', # State and Local government consumption expenditures: Sales to other sectors: Health and hospital charges
    'W146RC1Q027SBEA', # State and Local government consumption expenditures: Sales to other sectors: Other sales
    'B1065C1Q027SBEA', # State and Local government consumption expenditures: Sales to other sectors: Tuition and related educational charges
    ## Bil. of Chn. 2005 $ (SAAR)
    'A872RX1Q020SBEA', # Real government consumption expenditures and gross investment: Federal: Gross investment: Equipment and software (DISCONTINUED)
    'A873RX1Q020SBEA', # Real government consumption expenditures and gross investment: Federal: National defense: Gross investment: Equipment and software (DISCONTINUED)
    'B880RX1Q020SBEA', # Real government consumption expenditures and gross investment: Federal: Nondefense: Gross investment: Equipment and software (DISCONTINUED)
    'B881RX1Q020SBEA', # Real government consumption expenditures and gross investment: State and local: Gross investment: Equipment and software (DISCONTINUED)
    ## Bil. of Chn. 2017 $ (SAAR)
    'A955RX1Q020SBEA', # Real Government Consumption Expenditures
    'W085RX1Q020SBEA', # Real federal government consumption expenditures: Defense consumption expenditures: Gross output of general government
    'W087RX1Q020SBEA', # Real federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased
    'A998RX1Q020SBEA', # Real federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods
    'A725RX1Q020SBEA', # Real federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods
    'A489RX1Q020SBEA', # Real federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services
    'W088RX1Q020SBEA', # Real federal government consumption expenditures: Defense consumption expenditures: Own-account investment
    'W089RX1Q020SBEA', # Real federal government consumption expenditures: Defense consumption expenditures: Sales to other sectors
    'W110RX1Q020SBEA', # Real federal government consumption expenditures: Gross output of general government
    'W113RX1Q020SBEA', # Real federal government consumption expenditures: Gross output of general government: Intermediate goods and services purchased
    'W114RX1Q020SBEA', # Real federal government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods
    'W115RX1Q020SBEA', # Real federal government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods
    'W116RX1Q020SBEA', # Real federal government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services
    'W128RX1Q020SBEA', # Real federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government
    'W131RX1Q020SBEA', # Real federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Intermediate goods and services purchased
    'A543RX1Q020SBEA', # Real federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods
    'A729RX1Q020SBEA', # Real federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods
    'B826RX1Q020SBEA', # Real federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Commodity Credit Corporation inventory change
    'B828RX1Q020SBEA', # Real federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Other nondurable goods
    'A544RX1Q020SBEA', # Real federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services
    'W136RX1Q020SBEA', # Real federal government consumption expenditures: Nondefense consumption expenditures: Own-account investment
    'W137RX1Q020SBEA', # Real federal government consumption expenditures: Nondefense consumption expenditures: Sales to other sectors
    'W117RX1Q020SBEA', # Real federal government consumption expenditures: Own-account investment
    'W118RX1Q020SBEA', # Real federal government consumption expenditures: Sales to other sectors
    'A957RX1Q020SBEA', # Real government consumption expenditures and gross investment: Federal: Consumption expenditures
    'A787RX1Q020SBEA', # Real government consumption expenditures and gross investment: Federal: Gross investment
    'A801RX1Q020SBEA', # Real government consumption expenditures and gross investment: Federal: Gross investment: Structures
    'A824RX1Q020SBEA', # Real government consumption expenditures and gross investment: Federal: National defense
    'A808RX1Q020SBEA', # Real government consumption expenditures and gross investment: Federal: National defense: Gross investment: Structures
    'A825RX1Q020SBEA', # Real government consumption expenditures and gross investment: Federal: Nondefense
    'A830RX1Q020SBEA', # Real government consumption expenditures and gross investment: Federal: Nondefense: Gross investment: Structures
    'A979RX1Q020SBEA', # Real government consumption expenditures and gross investment: Residual
    'A842RX1Q020SBEA', # Real government consumption expenditures and gross investment: State and local: Gross investment: Structures
    'A997RX1Q020SBEA', # Real government consumption expenditures: Federal: National defense
    'A542RX1Q020SBEA', # Real government consumption expenditures: Federal: Nondefense
    'W101RX1Q020SBEA', # Real government consumption expenditures: Gross output of general government
    'W104RX1Q020SBEA', # Real government consumption expenditures: Gross output of general government: Intermediate goods and services purchased
    'W105RX1Q020SBEA', # Real government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods
    'W106RX1Q020SBEA', # Real government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods
    'W107RX1Q020SBEA', # Real government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services
    'W108RX1Q020SBEA', # Real government consumption expenditures: Own-account investment
    'W100RX1Q020SBEA', # Real government consumption expenditures: Residual
    'W109RX1Q020SBEA', # Real government consumption expenditures: Sales to other sectors
    'A991RX1Q020SBEA', # Real government consumption expenditures: State and local
    'W138RX1Q020SBEA', # Real state and local government consumption expenditures: Gross output of general government
    'W140RX1Q020SBEA', # Real state and local government consumption expenditures: Gross output of general government: Intermediate goods and services purchased
    'B989RX1Q020SBEA', # Real state and local government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods
    'B337RX1Q020SBEA', # Real state and local government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods
    'A988RX1Q020SBEA', # Real state and local government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services
    'W144RX1Q020SBEA', # Real state and local government consumption expenditures: Own-account investment
    'W145RX1Q020SBEA', # Real state and local government consumption expenditures: Sales to other sectors
    'B1066X1Q020SBEA', # Real state and local government consumption expenditures: Sales to other sectors: Health and hospital charges
    'W146RX1Q020SBEA', # Real state and local government consumption expenditures: Sales to other sectors: Other sales
    'B1065X1Q020SBEA', # Real state and local government consumption expenditures: Sales to other sectors: Tuition and related educational charges
    ## Index 2017=100 (NSA)
    'NC000331Q', # Government Consumption Expenditures and Gross Investment: Federal: National defense
    'NC000332Q', # Government Consumption Expenditures and Gross Investment: Federal: Nondefense
    'NB000331Q', # Real Government Consumption Expenditures and Gross Investment: Federal: National defense
    'NB000332Q', # Real Government Consumption Expenditures and Gross Investment: Federal: Nondefense
    ## Mil. of $ (NSA)
    'NA000291Q', # Federal government consumption expenditures
    'NA000331Q', # Government Consumption Expenditures and Gross Investment: Federal: National defense
    'NA000332Q', # Government Consumption Expenditures and Gross Investment: Federal: Nondefense
    'NA000316Q', # Government consumption expenditures: State and local
    ## Percentage Points at Annual Rate (SAAR)
    'A955RZ2Q224SBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Consumption expenditures
    'A823RZ2Q224SBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal
    'A957RZ2Q224SBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: Consumption expenditures
    'A787RZ2Q224SBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: Gross investment
    'A872RZ2Q224SBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: Gross investment: Equipment and software (DISCONTINUED)
    'A801RZ2Q224SBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: Gross investment: Structures
    'A824RZ2Q224SBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: National defense
    'A997RZ2Q224SBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: National defense: Consumption expenditures
    'A788RZ2Q224SBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: National defense: Gross investment
    'A873RZ2Q224SBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: National defense: Gross investment: Equipment and software (DISCONTINUED)
    'A808RZ2Q224SBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: National defense: Gross investment: Structures
    'A825RZ2Q224SBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: Nondefense
    'A542RZ2Q224SBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: Nondefense: Consumption expenditures
    'A798RZ2Q224SBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: Nondefense: Gross investment
    'B880RZ2Q224SBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: Nondefense: Gross investment: Equipment and software (DISCONTINUED)
    'A830RZ2Q224SBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: Nondefense: Gross investment: Structures
    'A782RZ2Q224SBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Gross investment
    'A871RZ2Q224SBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Gross investment: Equipment and software (DISCONTINUED)
    'A760RZ2Q224SBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Gross investment: Structures
    'A829RZ2Q224SBEA', # Contribution to percent change in real government consumption expenditures and gross investment: State and local
    'A991RZ2Q224SBEA', # Contribution to percent change in real government consumption expenditures and gross investment: State and local: Consumption expenditures
    'A799RZ2Q224SBEA', # Contribution to percent change in real government consumption expenditures and gross investment: State and local: Gross investment
    'B881RZ2Q224SBEA', # Contribution to percent change in real government consumption expenditures and gross investment: State and local: Gross investment: Equipment and software (DISCONTINUED)
    'A842RZ2Q224SBEA', # Contribution to percent change in real government consumption expenditures and gross investment: State and local: Gross investment: Structures
    'A822RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Government consumption expenditures and gross investment
    'A823RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Government consumption expenditures and gross investment: Federal
    'A824RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Government consumption expenditures and gross investment: Federal: National defense
    'A997RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Government consumption expenditures and gross investment: Federal: National defense: Consumption expenditures
    'A788RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Government consumption expenditures and gross investment: Federal: National defense: Gross investment
    'A825RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Government consumption expenditures and gross investment: Federal: Nondefense
    'A542RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Government consumption expenditures and gross investment: Federal: Nondefense: Consumption expenditures
    'A798RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Government consumption expenditures and gross investment: Federal: Nondefense: Gross investment
    'A829RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Government consumption expenditures and gross investment: State and local
    'A991RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Government consumption expenditures and gross investment: State and local: Consumption expenditures
    'A799RS2Q224SBEA', # Contributions to percent change in gross domestic purchases: Government consumption expenditures and gross investment: State and local: Gross investment
    'A822RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Government consumption expenditures and gross investment
    'A823RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Government consumption expenditures and gross investment: Federal
    'A824RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Government consumption expenditures and gross investment: Federal: National defense
    'A825RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Government consumption expenditures and gross investment: Federal: Nondefense
    'A829RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Government consumption expenditures and gross investment: State and local
    'A997RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Government consumption expenditures: Federal: National defense
    'A542RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Government consumption expenditures: Federal: Nondefense
    'A991RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Government consumption expenditures: State and local
    'A788RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Government gross investment: Federal: National defense
    'A798RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Government gross investment: Federal: Nondefense
    'A799RY2Q224SBEA', # Contributions to percent change in real gross domestic product: Government gross investment: State and local

    # Gov't Receipts, Expenditures & Investment > Gov't Current Expenditures (84)
    ## % Chg. from Preceding Period (SAAR)
    'W085RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Defense Consumption Expenditures: Gross Output of General Government
    'W087RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased
    'A998RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Durable Goods
    'A725RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Nondurable Goods
    'A489RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Services
    'W086RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Defense Consumption Expenditures: Gross Output of General Government: Value Added
    'B237RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Defense Consumption Expenditures: Gross Output of General Government: Value Added: Compensation of General Government Employees
    'B432RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Defense Consumption Expenditures: Gross Output of General Government: Value Added: Consumption of General Government Fixed Capital
    'W088RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Defense Consumption Expenditures: Less: Own-account Investment
    'W089RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Defense Consumption Expenditures: Less: Sales to Other Sectors
    'W110RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Gross Output of General Government
    'W113RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased
    'W114RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Durable Goods
    'W115RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Nondurable Goods
    'W116RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Services
    'W111RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Gross Output of General Government: Value Added
    'B568RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Gross Output of General Government: Value Added: Compensation of General Government Employees
    'B995RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Gross Output of General Government: Value Added: Consumption of General Government Fixed Capital
    'W128RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Nondefense Consumption Expenditures: Gross Output of General Government
    'W131RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Nondefense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased
    'A543RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Nondefense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Durable Goods
    'B828RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Nondefense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Nondurable Goods: Other Nondurable Goods
    'A544RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Nondefense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Services
    'W129RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Nondefense Consumption Expenditures: Gross Output of General Government: Value Added
    'W130RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Nondefense Consumption Expenditures: Gross Output of General Government: Value Added: Compensation of General Government Employees
    'B546RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Nondefense Consumption Expenditures: Gross Output of General Government: Value Added: Consumption of General Government Fixed Capital
    'W136RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Nondefense Consumption Expenditures: Own-account Investment
    'W137RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Nondefense Consumption Expenditures: Sales to Other Sectors
    'W117RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Own-account Investment
    'W118RL1Q225SBEA', # Real Federal Government Consumption Expenditures: Sales to Other Sectors
    'A955RL1Q225SBEA', # Real Government Consumption Expenditures
    'A957RL1Q225SBEA', # Real Government Consumption Expenditures: Federal: Consumption Expenditures
    'A997RL1Q225SBEA', # Real Government Consumption Expenditures: Federal: National Defense: Consumption Expenditures
    'W108RL1Q225SBEA', # Real Government Consumption Expenditures: Own-account Investment
    'W109RL1Q225SBEA', # Real Government Consumption Expenditures: Sales to Other Sectors
    'A991RL1Q225SBEA', # Real Government Consumption Expenditures: State and Local: Consumption Expenditures
    'W138RL1Q225SBEA', # Real State and Local Government Consumption Expenditures: Gross Output of General Government
    'W140RL1Q225SBEA', # Real State and Local Government Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased
    'B989RL1Q225SBEA', # Real State and Local Government Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Durable Goods
    'B337RL1Q225SBEA', # Real State and Local Government Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Nondurable Goods
    'A988RL1Q225SBEA', # Real State and Local Government Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Services
    'W139RL1Q225SBEA', # Real State and Local Government Consumption Expenditures: Gross Output of General Government: Value Added
    'B251RL1Q225SBEA', # Real State and Local Government Consumption Expenditures: Gross Output of General Government: Value Added: Compensation of General Government Employees
    'B986RL1Q225SBEA', # Real State and Local Government Consumption Expenditures: Gross Output of General Government: Value Added: Consumption of General Government Fixed Capital
    'W144RL1Q225SBEA', # Real State and Local Government Consumption Expenditures: Own-account Investment
    'W145RL1Q225SBEA', # Real State and Local Government Consumption Expenditures: Sales to Other Sectors
    'B1066L1Q225SBEA', # Real State and Local Government Consumption Expenditures: Sales to Other Sectors: Health and Hospital Charges
    'W146RL1Q225SBEA', # Real State and Local Government Consumption Expenditures: Sales to Other Sectors: Other Sales
    'B1065L1Q225SBEA', # Real State and Local Government Consumption Expenditures: Sales to Other Sectors: Tuition and Related Educational Charges
    ## Bil. of $ (NSA)
    'Q089RU1Q027NBEA', # Federal Government Current Expenditures: Current transfer payments: Other current transfer payments: Grants-in-aid to state and local governments (DISCONTINUED)
    'W013RU1Q027NBEA', # Federal government current expenditures (DISCONTINUED)
    'M318491Q027NBEA', # Federal government current expenditures, NIPAs
    'L318441Q027NBEA', # Federal government current expenditures, NIPAs (DISCONTINUED)
    'W014RU1Q027NBEA', # Federal government current expenditures: Current transfer payments (DISCONTINUED)
    'W015RU1Q027NBEA', # Federal government current expenditures: Current transfer payments: Government social benefits (DISCONTINUED)
    'B087RU1Q027NBEA', # Federal government current expenditures: Current transfer payments: Government social benefits: to persons (DISCONTINUED)
    'W016RU1Q027NBEA', # Federal government current expenditures: Current transfer payments: Government social benefits: to the rest of the world (DISCONTINUED)
    'W010RU1Q027NBEA', # Federal government current expenditures: Current transfer payments: Other current transfer payments (DISCONTINUED)
    'B089RU1Q027NBEA', # Federal government current expenditures: Current transfer payments: Other current transfer payments: Grants-in-aid to state and local governments (DISCONTINUED)
    'W017RU1Q027NBEA', # Federal government current expenditures: Current transfer payments: Other current transfer payments: to the rest of the world (net) (DISCONTINUED)
    'A091RU1Q027NBEA', # Federal government current expenditures: Interest payments (DISCONTINUED)
    'B092RU1Q027NBEA', # Federal government current expenditures: Interest payments: to persons and business (DISCONTINUED)
    'B093RU1Q027NBEA', # Federal government current expenditures: Interest payments: to the rest of the world (DISCONTINUED)
    'B096RU1Q027NBEA', # Federal government current expenditures: Subsidies (DISCONTINUED)
    'LA0000241Q027NBEA', # State and Local Government Current Expenditures: Current transfer payments (DISCONTINUED)
    'LA0000251Q027NBEA', # State and Local Government Current Expenditures: Current transfer payments: Current transfer payments to the rest of the world (DISCONTINUED)
    'Y705RU1Q027NBEA', # State and Local Government Current Expenditures: Interest payments: to persons and business (DISCONTINUED)
    'Y706RU1Q027NBEA', # State and Local Government Current Expenditures: Interest payments: to the rest of the world (DISCONTINUED)
    'W024RU1Q027NBEA', # State and local government current expenditures (DISCONTINUED)
    'B109RU1Q027NBEA', # State and local government current expenditures: Government social benefit payments to persons (DISCONTINUED)
    'B111RU1Q027NBEA', # State and local government current expenditures: Interest payments (DISCONTINUED)
    'B114RU1Q027NBEA', # State and local government current expenditures: Subsidies (DISCONTINUED)
    ## Bil. of $ (SAAR)
    'B092RC1Q027SBEA', # Federal government current expenditures: Interest payments: to persons and business
    'B096RC1Q027SBEA', # Federal government current expenditures: Subsidies
    'A180RC1Q027SBEA', # Government current expenditures: Interest payments
    'A204RC1Q027SBEA', # Government current expenditures: Interest payments: to persons and business
    'LA0000171Q027SBEA', # State and local government current expenditures: Current transfer payments
    'LA0000151Q027SBEA', # State and local government current expenditures: Current transfer payments: Current transfer payments to the rest of the world
    'Y705RC1Q027SBEA', # State and local government current expenditures: Interest payments: to persons and business
    'Y706RC1Q027SBEA', # State and local government current expenditures: Interest payments: to the rest of the world
    ## Mil. of $ (NSA)
    'NA000309Q', # Federal government current expenditures: Interest payments: to persons and business
    'NA000318Q', # Federal government current expenditures: Subsidies
    'NA000312Q', # State and local government current expenditures: Interest payments: to persons and business
    'NA000313Q', # State and local government current expenditures: Interest payments: to the rest of the world

    # Gov't Receipts, Expenditures & Investment > Gov't Current Transfer Receipts (22)
    ## Bil. of $ (NSA)
    'W011RU1Q027NBEA', # Federal government current transfer receipts (DISCONTINUED)
    'LA0000231Q027NBEA', # State and Local Government Current Receipts: Current transfer receipts: From the rest of the world (DISCONTINUED)
    ## Bil. of $ (SAAR)
    'LA0000121Q027SBEA', # Federal government current receipts: Contributions for government social insurance: From persons
    'W781RC1Q027SBEA', # Federal government current receipts: Contributions for government social insurance: From the rest of the world
    'LA0000281Q027SBEA', # Federal government current receipts: Current transfer receipts: From the rest of the world
    'W011RC1Q027SBEA', # Federal government current transfer receipts
    'W012RC1Q027SBEA', # Federal government current transfer receipts: from business
    'B233RC1Q027SBEA', # Federal government current transfer receipts: from persons
    'LA0000141Q027SBEA', # Government current receipts: Current transfer receipts: From the rest of the world
    'Y703RC1Q027SBEA', # Government current receipts: Income receipts on assets: Interest and miscellaneous receipts: Interest receipts
    'Y704RC1Q027SBEA', # Government current receipts: Income receipts on assets: Interest and miscellaneous receipts: Rents and royalties
    'W060RC1Q027SBEA', # Government current transfer receipts
    'W969RC1Q027SBEA', # State and Local Government Total receipts: Capital transfer receipts
    'LA0000161Q027SBEA', # State and local government current receipts: Current transfer receipts: From the rest of the world
    'W075RC1Q027SBEA', # State and local government current transfer receipts
    'W076RC1Q027SBEA', # State and local government current transfer receipts: from business (net)
    'B246RC1Q027SBEA', # State and local government current transfer receipts: from persons
    ## Mil. of $ (NSA)
    'NA000288Q', # Federal government current transfer receipts
    'NA000363Q', # State and local government current transfer receipts
    'NA000280Q', # State and local government current transfer receipts: from business (net)
    'NA000287Q', # State and local government current transfer receipts: from persons
    'NA000290Q', # State and local government current transfer receipts: from the rest of the world

    # Gov't Receipts, Expenditures & Investment > Gov't Fixed Investment (14)
    ## Bil. of $ (SAAR)
    'A872RC1Q027SBEA', # Government consumption expenditures and gross investment: Federal: Gross investment: Equipment and software (DISCONTINUED)
    'A801RC1Q027SBEA', # Government consumption expenditures and gross investment: Federal: Gross investment: Structures
    'A873RC1Q027SBEA', # Government consumption expenditures and gross investment: Federal: National defense: Gross investment: Equipment and software (DISCONTINUED)
    'A808RC1Q027SBEA', # Government consumption expenditures and gross investment: Federal: National defense: Gross investment: Structures
    'B880RC1Q027SBEA', # Government consumption expenditures and gross investment: Federal: Nondefense: Gross investment: Equipment and software (DISCONTINUED)
    'A830RC1Q027SBEA', # Government consumption expenditures and gross investment: Federal: Nondefense: Gross investment: Structures
    'B881RC1Q027SBEA', # Government consumption expenditures and gross investment: State and local: Gross investment: Equipment and software (DISCONTINUED)
    'A842RC1Q027SBEA', # Government consumption expenditures and gross investment: State and local: Gross investment: Structures
    'B874RC1Q027SBEA', # National defense consumption expenditures and gross investment: Gross investment: Equipment: Aircraft
    'B875RC1Q027SBEA', # National defense consumption expenditures and gross investment: Gross investment: Equipment: Missiles
    'B879RC1Q027SBEA', # National defense consumption expenditures and gross investment: Gross investment: Equipment: Other equipment
    'B876RC1Q027SBEA', # National defense consumption expenditures and gross investment: Gross investment: Equipment: Ships
    'B877RC1Q027SBEA', # National defense consumption expenditures and gross investment: Gross investment: Equipment: Vehicles
    'B878RC1Q027SBEA', # National defense gross investment: Equipment and software: Electronics and software (DISCONTINUED)

    # Gov't Receipts, Expenditures & Investment > Gov't Investment (91)
    ## % Chg. at Annual Rate (SAAR)
    'GOVNOW', # Nowcast for Real Gross Government Investment
    'FEDGOVNOW', # Nowcast for Real Gross Government Investment: Federal Government
    'SLGOVNOW', # Nowcast for Real Gross Government Investment: State and Local Government
    ## % Chg. from Preceding Period (SAAR)
    'A782RL1Q225SBEA', # Real Government Gross Investment
    'Y054RL1Q225SBEA', # Real Government Gross Investment: Equipment
    'A787RL1Q225SBEA', # Real Government Gross Investment: Federal: Gross Investment
    'Y058RL1Q225SBEA', # Real Government Gross Investment: Federal: Gross Investment: Equipment
    'Y059RL1Q225SBEA', # Real Government Gross Investment: Federal: Gross Investment: Intellectual Property Products
    'Y061RL1Q225SBEA', # Real Government Gross Investment: Federal: Gross Investment: Intellectual Property Products: Research and Development
    'Y060RL1Q225SBEA', # Real Government Gross Investment: Federal: Gross Investment: Intellectual Property Products: Software
    'A801RL1Q225SBEA', # Real Government Gross Investment: Federal: Gross Investment: Structures
    'A788RL1Q225SBEA', # Real Government Gross Investment: Federal: National Defense: Gross Investment
    'Y050RL1Q225SBEA', # Real Government Gross Investment: Federal: National Defense: Gross Investment: Equipment
    'Y052RL1Q225SBEA', # Real Government Gross Investment: Federal: National Defense: Gross Investment: Intellectual Property Products
    'Y076RL1Q225SBEA', # Real Government Gross Investment: Federal: National Defense: Gross Investment: Intellectual Property Products: Research and Development
    'Y053RL1Q225SBEA', # Real Government Gross Investment: Federal: National Defense: Gross Investment: Intellectual Property Products: Software
    'A808RL1Q225SBEA', # Real Government Gross Investment: Federal: National Defense: Gross Investment: Structures
    'A798RL1Q225SBEA', # Real Government Gross Investment: Federal: Nondefense: Gross Investment
    'Y066RL1Q225SBEA', # Real Government Gross Investment: Federal: Nondefense: Gross Investment: Equipment
    'Y067RL1Q225SBEA', # Real Government Gross Investment: Federal: Nondefense: Gross Investment: Intellectual Property Products
    'Y069RL1Q225SBEA', # Real Government Gross Investment: Federal: Nondefense: Gross Investment: Intellectual Property Products: Research and Development
    'Y068RL1Q225SBEA', # Real Government Gross Investment: Federal: Nondefense: Gross Investment: Intellectual Property Products: Software
    'A830RL1Q225SBEA', # Real Government Gross Investment: Federal: Nondefense: Gross Investment: Structures
    'Y055RL1Q225SBEA', # Real Government Gross Investment: Intellectual Property Products
    'Y057RL1Q225SBEA', # Real Government Gross Investment: Intellectual Property Products: Research and Development
    'Y056RL1Q225SBEA', # Real Government Gross Investment: Intellectual Property Products: Software
    'A799RL1Q225SBEA', # Real Government Gross Investment: State and Local: Gross Investment
    'Y070RL1Q225SBEA', # Real Government Gross Investment: State and Local: Gross Investment: Equipment
    'Y071RL1Q225SBEA', # Real Government Gross Investment: State and Local: Gross Investment: Intellectual Property Products
    'Y073RL1Q225SBEA', # Real Government Gross Investment: State and Local: Gross Investment: Intellectual Property Products: Research and Development
    'Y072RL1Q225SBEA', # Real Government Gross Investment: State and Local: Gross Investment: Intellectual Property Products: Software
    'A842RL1Q225SBEA', # Real Government Gross Investment: State and Local: Gross Investment: Structures
    'A760RL1Q225SBEA', # Real Government Gross Investment: Structures
    ## Bil. of $ (NSA)
    'A799RU1Q027NBEA', # State and local government gross government investment (DISCONTINUED)
    ## Bil. of $ (SAAR)
    'Y054RC1Q027SBEA', # Government Gross Investment: Equipment
    'Y058RC1Q027SBEA', # Government Gross Investment: Federal: Gross Investment: Equipment
    'Y059RC1Q027SBEA', # Government Gross Investment: Federal: Gross Investment: Intellectual Property Products
    'Y061RC1Q027SBEA', # Government Gross Investment: Federal: Gross Investment: Intellectual Property Products: Research and Development
    'Y060RC1Q027SBEA', # Government Gross Investment: Federal: Gross Investment: Intellectual Property Products: Software
    'Y050RC1Q027SBEA', # Government Gross Investment: Federal: National Defense: Gross Investment: Equipment
    'Y052RC1Q027SBEA', # Government Gross Investment: Federal: National Defense: Gross Investment: Intellectual Property Products
    'Y076RC1Q027SBEA', # Government Gross Investment: Federal: National Defense: Gross Investment: Intellectual Property Products: Research and Development
    'Y053RC1Q027SBEA', # Government Gross Investment: Federal: National Defense: Gross Investment: Intellectual Property Products: Software
    'Y066RC1Q027SBEA', # Government Gross Investment: Federal: Nondefense: Gross Investment: Equipment
    'Y067RC1Q027SBEA', # Government Gross Investment: Federal: Nondefense: Gross Investment: Intellectual Property Products
    'Y069RC1Q027SBEA', # Government Gross Investment: Federal: Nondefense: Gross Investment: Intellectual Property Products: Research and Development
    'Y068RC1Q027SBEA', # Government Gross Investment: Federal: Nondefense: Gross Investment: Intellectual Property Products: Software
    'Y055RC1Q027SBEA', # Government Gross Investment: Intellectual Property Products
    'Y057RC1Q027SBEA', # Government Gross Investment: Intellectual Property Products: Research and Development
    'Y056RC1Q027SBEA', # Government Gross Investment: Intellectual Property Products: Software
    'Y070RC1Q027SBEA', # Government Gross Investment: State and Local: Gross Investment: Equipment
    'Y071RC1Q027SBEA', # Government Gross Investment: State and Local: Gross Investment: Intellectual Property Products
    'Y073RC1Q027SBEA', # Government Gross Investment: State and Local: Gross Investment: Intellectual Property Products: Research and Development
    'Y072RC1Q027SBEA', # Government Gross Investment: State and Local: Gross Investment: Intellectual Property Products: Software
    'A760RC1Q027SBEA', # Government consumption expenditures and gross investment: Gross investment: Equipment and software: Gross investment: Structures
    'A871RC1Q027SBEA', # Government consumption expenditures and gross investment: State and local: Gross investment: Equipment and software: Gross investment: Equipment and software (DISCONTINUED)
    'A782RC1Q027SBEA', # Gross government investment
    'A787RC1Q027SBEA', # Gross government investment: Federal
    'AB64RC1Q027SBEA', # Motor vehicle output: Gross government investment
    'B144RC1Q027SBEA', # Motor vehicle output: Gross government investment: Autos
    'B708RC1Q027SBEA', # Motor vehicle output: Gross government investment: Trucks
    ## Bil. of Chn. 2005 $ (SAAR)
    'A871RX1Q020SBEA', # Real government consumption expenditures and gross investment: State and local: Gross investment: Equipment and software: Gross investment: Equipment and software (DISCONTINUED)
    ## Bil. of Chn. 2017 $ (SAAR)
    'Y058RX1Q020SBEA', # Real Government Gross Investment: Federal: Gross Investment: Equipment
    'Y059RX1Q020SBEA', # Real Government Gross Investment: Federal: Gross Investment: Intellectual Property Products
    'Y061RX1Q020SBEA', # Real Government Gross Investment: Federal: Gross Investment: Intellectual Property Products: Research and Development
    'Y060RX1Q020SBEA', # Real Government Gross Investment: Federal: Gross Investment: Intellectual Property Products: Software
    'Y050RX1Q020SBEA', # Real Government Gross Investment: Federal: National Defense: Gross Investment: Equipment
    'Y052RX1Q020SBEA', # Real Government Gross Investment: Federal: National Defense: Gross Investment: Intellectual Property Products
    'Y076RX1Q020SBEA', # Real Government Gross Investment: Federal: National Defense: Gross Investment: Intellectual Property Products: Research and Development
    'Y053RX1Q020SBEA', # Real Government Gross Investment: Federal: National Defense: Gross Investment: Intellectual Property Products: Software
    'Y066RX1Q020SBEA', # Real Government Gross Investment: Federal: Nondefense: Gross Investment: Equipment
    'Y067RX1Q020SBEA', # Real Government Gross Investment: Federal: Nondefense: Gross Investment: Intellectual Property Products
    'Y069RX1Q020SBEA', # Real Government Gross Investment: Federal: Nondefense: Gross Investment: Intellectual Property Products: Research and Development
    'Y068RX1Q020SBEA', # Real Government Gross Investment: Federal: Nondefense: Gross Investment: Intellectual Property Products: Software
    'Y054RX1Q020SBEA', # Real Government Gross Investment: Gross Investment: Equipment
    'Y055RX1Q020SBEA', # Real Government Gross Investment: Gross Investment: Intellectual Property Products
    'Y057RX1Q020SBEA', # Real Government Gross Investment: Gross Investment: Intellectual Property Products: Research and Development
    'Y056RX1Q020SBEA', # Real Government Gross Investment: Gross Investment: Intellectual Property Products: Software
    'Y070RX1Q020SBEA', # Real Government Gross Investment: State and Local: Gross Investment: Equipment
    'Y071RX1Q020SBEA', # Real Government Gross Investment: State and Local: Gross Investment: Intellectual Property Products
    'Y073RX1Q020SBEA', # Real Government Gross Investment: State and Local: Gross Investment: Intellectual Property Products: Research and Development
    'Y072RX1Q020SBEA', # Real Government Gross Investment: State and Local: Gross Investment: Intellectual Property Products: Software
    'A782RX1Q020SBEA', # Real government consumption expenditures and gross investment: Gross investment: Equipment and software
    'A760RX1Q020SBEA', # Real government consumption expenditures and gross investment: Gross investment: Equipment and software: Gross investment: Structures
    'AB64RX1Q020SBEA', # Real motor vehicle output: Gross government investment
    'B144RX1Q020SBEA', # Real motor vehicle output: Gross government investment: Autos
    'B708RX1Q020SBEA', # Real motor vehicle output: Gross government investment: Trucks
    ## Mil. of $ (NSA)
    'NA000292Q', # Gross government investment: Federal
    ## Percentage Points (SA)
    'GOVCONTRIBNOW', # Contributions to percent change in GDPNow: Real Gross Government Investment
    'FEDGOVCONTRIBNOW', # Contributions to percent change in GDPNow: Real Gross Government Investment: Federal Government
    'SLGOVCONTRIBNOW', # Contributions to percent change in GDPNow: Real Gross Government Investment: State and Local Government

    # Gov't Receipts, Expenditures & Investment > Gov't Social Benefits (14)
    ## Bil. of $ (SAAR)
    'W015RC1Q027SBEA', # Federal government current transfer payments: Government social benefits
    'B087RC1Q027SBEA', # Federal government current transfer payments: Government social benefits: to persons
    'W016RC1Q027SBEA', # Federal government current transfer payments: Government social benefits: to the rest of the world
    'W063RC1Q027SBEA', # Government current transfer payments: Government social benefits
    'A063RC1Q027SBEA', # Personal current transfer receipts: Government social benefits to persons
    'W729RC1Q027SBEA', # Personal current transfer receipts: Government social benefits to persons: Medicaid
    'W824RC1Q027SBEA', # Personal current transfer receipts: Government social benefits to persons: Medicare
    'W827RC1Q027SBEA', # Personal current transfer receipts: Government social benefits to persons: Other
    'W823RC1Q027SBEA', # Personal current transfer receipts: Government social benefits to persons: Social security
    'W825RC1Q027SBEA', # Personal current transfer receipts: Government social benefits to persons: Unemployment insurance
    'W826RC1Q027SBEA', # Personal current transfer receipts: Government social benefits to persons: Veterans' benefits
    ## Mil. of $ (NSA)
    'NA000298Q', # Federal government current transfer payments: Government social benefits
    'NA000300Q', # Federal government current transfer payments: Government social benefits: to persons
    'NA000301Q', # Federal government current transfer payments: Government social benefits: to the rest of the world

]

# Annually (1675)
ids_Y = [
    # Gov't Receipts, Expenditures & Investment (646)
    ## % Chg. from Preceding Period (NSA)
    'A822RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment
    'A823RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: Federal
    'W620RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: Federal: Economic affairs
    'W632RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: Federal: Economic affairs: Other economic affairs
    'W631RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: Federal: Economic affairs: Space
    'W625RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: Federal: Economic affairs: Transportation
    'W636RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: Federal: Education
    'W634RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: Federal: Health
    'W633RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: Federal: Housing and community services
    'W640RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: Federal: Income security
    'A824RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: Federal: National Defense
    'A825RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: Federal: Nondefense
    'A542RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: Federal: Nondefense: Consumption Expenditures
    'W615RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: Federal: Public order and safety
    'W635RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: Federal: Recreation and culture
    'W611RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: General public service
    'W584RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: Government: Economic affairs
    'W596RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: Government: Economic affairs: Other economic affairs
    'W595RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: Government: Economic affairs: Space
    'W589RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: Government: Economic affairs: Transportation
    'W600RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: Government: Education
    'W575RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: Government: General public service
    'W598RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: Government: Health
    'W597RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: Government: Housing and community services
    'W605RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: Government: Income security
    'W579RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: Government: Public order and safety
    'W599RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: Government: Recreation and culture
    'A829RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: State and Local
    'W655RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: State and Local: Economic affairs
    'W665RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: State and Local: Economic affairs: Other economic affairs
    'W660RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: State and Local: Economic affairs: Transportation
    'W673RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: State and Local: Education
    'W674RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: State and Local: Education: Elementary and secondary
    'W675RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: State and Local: Education: Higher
    'W677RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: State and Local: Education: Libraries and other
    'W646RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: State and Local: General public service
    'W666RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: State and Local: Housing and community services
    'W678RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: State and Local: Income security
    'W671RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: State and Local: Net Health
    'Y650RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: State and Local: Net Health: Gross expenditures
    'Y651RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: State and Local: Net Health: Sales to other sectors
    'W650RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: State and Local: Public order and safety
    'W672RL1A225NBEA', # Real Government Consumption Expenditures and Gross Investment: State and Local: Recreation and culture
    'W101RL1A225NBEA', # Real Gross Output of General Government
    'W104RL1A225NBEA', # Real Gross Output of General Government: Intermediate Goods and Services Purchased
    'W105RL1A225NBEA', # Real Gross Output of General Government: Intermediate Goods and Services Purchased: Durable Goods
    'W106RL1A225NBEA', # Real Gross Output of General Government: Intermediate Goods and Services Purchased: Nondurable Goods
    'W107RL1A225NBEA', # Real Gross Output of General Government: Intermediate Goods and Services Purchased: Services
    'W102RL1A225NBEA', # Real Gross Output of General Government: Value Added
    'A194RL1A225NBEA', # Real Gross Output of General Government: Value Added: Compensation of General Government Employees
    'B999RL1A225NBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Durable Goods: Aircraft
    'B388RL1A225NBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Durable Goods: Electronics
    'B277RL1A225NBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Durable Goods: Missiles
    'B389RL1A225NBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Durable Goods: Other Durable Goods
    'B278RL1A225NBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Durable Goods: Ships
    'B288RL1A225NBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Durable Goods: Vehicles
    'B781RL1A225NBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Nondurable Goods: Ammunition
    'B783RL1A225NBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Nondurable Goods: Other Nondurable Goods
    'B780RL1A225NBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Nondurable Goods: Petroleum Products
    'B911RL1A225NBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Services: Installation Support
    'B913RL1A225NBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Services: Personnel Support
    'B786RL1A225NBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Services: Transportation of Material
    'B785RL1A225NBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Services: Travel of Persons
    'B912RL1A225NBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Services: Weapons Support
    'W090RL1A225NBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Value Added: Compensation of General Government Employees: Civilian
    'B4080L1A225NBEA', # Real National Defense Consumption Expenditures: Gross Output of General Government: Value Added: Compensation of General Government Employees: Military
    'B874RL1A225NBEA', # Real National Defense Gross Investment: Equipment: Aircraft
    'Y051RL1A225NBEA', # Real National Defense Gross Investment: Equipment: Electronics
    'B875RL1A225NBEA', # Real National Defense Gross Investment: Equipment: Missiles
    'B879RL1A225NBEA', # Real National Defense Gross Investment: Equipment: Other Equipment
    'B876RL1A225NBEA', # Real National Defense Gross Investment: Equipment: Ships
    'B877RL1A225NBEA', # Real National Defense Gross Investment: Equipment: Vehicles
    ## Bil. of $ (NSA)
    'L318461A027NBEA', # Cash payments to the public: Coverage differences: Net investment (DISCONTINUED)
    'B202RC1A027NBEA', # Compensation of employees: Wages and salaries: Government
    'A061RC1A027NBEA', # Contributions for government social insurance, domestic
    'B228RC1A027NBEA', # Contributions for government social insurance: Employee and self-employed contributions
    'A1585C1A027NBEA', # Contributions for government social insurance: Employee and self-employed contributions: Federal social insurance funds
    'A1586C1A027NBEA', # Contributions for government social insurance: Employee and self-employed contributions: Federal social insurance funds: Old-age, survivors, disability, and hospital insurance
    'A1587C1A027NBEA', # Contributions for government social insurance: Employee and self-employed contributions: Federal social insurance funds: Old-age, survivors, disability, and hospital insurance: Employees
    'L306231A027NBEA', # Contributions for government social insurance: Employee and self-employed contributions: Federal social insurance funds: Old-age, survivors, disability, and hospital insurance: Employees: Hospital insurance
    'L306221A027NBEA', # Contributions for government social insurance: Employee and self-employed contributions: Federal social insurance funds: Old-age, survivors, disability, and hospital insurance: Employees: Old-age, survivors, and disability insurance
    'CON5201A027NBEA', # Contributions for government social insurance: Employee and self-employed contributions: Federal social insurance funds: Old-age, survivors, disability, and hospital insurance: Self-employed
    'CON5501A027NBEA', # Contributions for government social insurance: Employee and self-employed contributions: Federal social insurance funds: Railroad retirement
    'CON5441A027NBEA', # Contributions for government social insurance: Employee and self-employed contributions: Federal social insurance funds: State unemployment insurance
    'CON5301A027NBEA', # Contributions for government social insurance: Employee and self-employed contributions: Federal social insurance funds: Supplementary medical insurance
    'CON5741A027NBEA', # Contributions for government social insurance: Employee and self-employed contributions: Federal social insurance funds: Veterans life insurance
    'B738RC1A027NBEA', # Contributions for government social insurance: Employee and self-employed contributions: State and local social insurance funds
    'W781RC1A027NBEA', # Contributions for government social insurance: Rest-of-the-world contributions
    'L312121A027NBEA', # Current surplus of government enterprises: Federal: Federal Housing Administration
    'L312141A027NBEA', # Current surplus of government enterprises: Federal: Other
    'L312101A027NBEA', # Current surplus of government enterprises: Federal: Postal Service
    'L312131A027NBEA', # Current surplus of government enterprises: Federal: Tennessee Valley Authority
    'L312221A027NBEA', # Current surplus of government enterprises: State and local: Air and water terminals
    'L312191A027NBEA', # Current surplus of government enterprises: State and local: Gas and electricity
    'L312231A027NBEA', # Current surplus of government enterprises: State and local: Housing and urban renewal
    'L312211A027NBEA', # Current surplus of government enterprises: State and local: Liquor stores
    'L312251A027NBEA', # Current surplus of government enterprises: State and local: Other
    'L312241A027NBEA', # Current surplus of government enterprises: State and local: Public transit
    'L312201A027NBEA', # Current surplus of government enterprises: State and local: Toll facilities
    'L312181A027NBEA', # Current surplus of government enterprises: State and local: Water and sewerage
    'LA0000021A027NBEA', # Current taxes and transfer payments to the rest of the world: From persons
    'LA0000351A027NBEA', # Current taxes, contributions for government social insurance, and transfer receipts from the rest of the world
    'LA0000291A027NBEA', # Current taxes, contributions for government social insurance, and transfer receipts from the rest of the world: to business
    'LA0000371A027NBEA', # Current taxes, contributions for government social insurance, and transfer receipts from the rest of the world: to government
    'LA0000361A027NBEA', # Current taxes, contributions for government social insurance, and transfer receipts from the rest of the world: to persons
    'FGCEA', # Federal Government Consumption Expenditures and Gross Investment
    'AFEXPND', # Federal Government Current Expenditures
    'FRSI', # Federal Government Receipts: Contributions for Social Insurance
    'AFRECPT', # Federal Government: Current Receipts
    'FCTAX', # Federal Government: Tax Receipts on Corporate Income
    'M318501A027NBEA', # Federal government budget surplus or deficit (-)
    'W020RC1A027NBEA', # Federal government capital transfer payments
    'L318191A027NBEA', # Federal government cash payments to the public (DISCONTINUED)
    'L318201A027NBEA', # Federal government cash payments to the public: Coverage differences (DISCONTINUED)
    'L318271A027NBEA', # Federal government cash payments to the public: Coverage differences: District of Columbia (DISCONTINUED)
    'L318281A027NBEA', # Federal government cash payments to the public: Coverage differences: Federal Home Loan Banks and Federal Land Banks (DISCONTINUED)
    'L318221A027NBEA', # Federal government cash payments to the public: Coverage differences: Federal employee retirement plan transactions (DISCONTINUED)
    'L318261A027NBEA', # Federal government cash payments to the public: Coverage differences: Federal employee retirement plan transactions: Administrative expenses (DISCONTINUED)
    'L318251A027NBEA', # Federal government cash payments to the public: Coverage differences: Federal employee retirement plan transactions: Benefits paid (DISCONTINUED)
    'L318241A027NBEA', # Federal government cash payments to the public: Coverage differences: Federal employee retirement plan transactions: Contributions received (employer) (DISCONTINUED)
    'L318231A027NBEA', # Federal government cash payments to the public: Coverage differences: Federal employee retirement plan transactions: Interest received (DISCONTINUED)
    'L318311A027NBEA', # Federal government cash payments to the public: Coverage differences: Financial transactions (DISCONTINUED)
    'L318321A027NBEA', # Federal government cash payments to the public: Coverage differences: Financial transactions: Loan disbursements less loan repayments and sales (DISCONTINUED)
    'L318331A027NBEA', # Federal government cash payments to the public: Coverage differences: Financial transactions: Net purchases of foreign currency (DISCONTINUED)
    'L318291A027NBEA', # Federal government cash payments to the public: Coverage differences: Net investment (DISCONTINUED)
    'L318341A027NBEA', # Federal government cash payments to the public: Coverage differences: Other (DISCONTINUED)
    'L318351A027NBEA', # Federal government cash payments to the public: Netting and grossing differences (DISCONTINUED)
    'W702LC1A027NBEA', # Federal government cash payments to the public: Netting and grossing differences: Current surplus of government enterprises (DISCONTINUED)
    'W703LC1A027NBEA', # Federal government cash payments to the public: Netting and grossing differences: Interest receipts (DISCONTINUED)
    'L318371A027NBEA', # Federal government cash payments to the public: Netting and grossing differences: Other (DISCONTINUED)
    'L318381A027NBEA', # Federal government cash payments to the public: Timing differences (DISCONTINUED)
    'L318431A027NBEA', # Federal government cash payments to the public: Timing differences: Checks outstanding and certain other accounts (DISCONTINUED)
    'L318411A027NBEA', # Federal government cash payments to the public: Timing differences: Current transfer payments (DISCONTINUED)
    'L318401A027NBEA', # Federal government cash payments to the public: Timing differences: Interest payments (DISCONTINUED)
    'L318391A027NBEA', # Federal government cash payments to the public: Timing differences: Purchases (increase in payables net of advances) (DISCONTINUED)
    'L318421A027NBEA', # Federal government cash payments to the public: Timing differences: Subsidies (DISCONTINUED)
    'L318011A027NBEA', # Federal government cash receipts from the public (DISCONTINUED)
    'L318021A027NBEA', # Federal government cash receipts from the public: Coverage differences (DISCONTINUED)
    'L318041A027NBEA', # Federal government cash receipts from the public: Coverage differences: Contributions received by federal employee retirement plans (DISCONTINUED)
    'L318071A027NBEA', # Federal government cash receipts from the public: Coverage differences: District of Columbia (DISCONTINUED)
    'L318061A027NBEA', # Federal government cash receipts from the public: Coverage differences: Financial transactions (DISCONTINUED)
    'L318081A027NBEA', # Federal government cash receipts from the public: Coverage differences: Other (DISCONTINUED)
    'L318091A027NBEA', # Federal government cash receipts from the public: Netting and grossing differences (DISCONTINUED)
    'W700LC1A027NBEA', # Federal government cash receipts from the public: Netting and grossing differences: Current surplus of government enterprises (DISCONTINUED)
    'W701LC1A027NBEA', # Federal government cash receipts from the public: Netting and grossing differences: Interest receipts (DISCONTINUED)
    'L318111A027NBEA', # Federal government cash receipts from the public: Netting and grossing differences: Other (DISCONTINUED)
    'L318121A027NBEA', # Federal government cash receipts from the public: Timing differences (DISCONTINUED)
    'L318161A027NBEA', # Federal government cash receipts from the public: Timing differences: Excise taxes (DISCONTINUED)
    'L318141A027NBEA', # Federal government cash receipts from the public: Timing differences: Federal and state unemployment insurance taxes (DISCONTINUED)
    'L318171A027NBEA', # Federal government cash receipts from the public: Timing differences: Other (DISCONTINUED)
    'L318451A027NBEA', # Federal government consolidated cash budget surplus or deficit (-) (DISCONTINUED)
    'W086RC1A027NBEA', # Federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Value added
    'B237RC1A027NBEA', # Federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Value added: Compensation of general government employees
    'B432RC1A027NBEA', # Federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Value added: Consumption of general government fixed capital
    'W111RC1A027NBEA', # Federal government consumption expenditures: Gross output of general government: Value added
    'W129RC1A027NBEA', # Federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Value added
    'W130RC1A027NBEA', # Federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Value added: Compensation of general government employees
    'B546RC1A027NBEA', # Federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Value added: Consumption of general government fixed capital
    'B098RC1A027NBEA', # Federal government current expenditures: Wage accruals less disbursements (DISCONTINUED)
    'M318181A027NBEA', # Federal government current receipts, NIPAs
    'L318181A027NBEA', # Federal government current receipts, NIPAs (DISCONTINUED)
    'B097RC1A027NBEA', # Federal government current receipts: Current surplus of government enterprises
    'W009RC1A027NBEA', # Federal government current receipts: Income receipts on assets
    'W053RC1A027NBEA', # Federal government current receipts: Income receipts on assets: Dividends
    'B094RC1A027NBEA', # Federal government current receipts: Income receipts on assets: Interest receipts
    'B1040C1A027NBEA', # Federal government current receipts: Income receipts on assets: Rents and royalties
    'W006RC1A027NBEA', # Federal government current tax receipts
    'W007RC1A027NBEA', # Federal government current tax receipts: Taxes on production and imports
    'B235RC1A027NBEA', # Federal government current tax receipts: Taxes on production and imports: Customs duties
    'B234RC1A027NBEA', # Federal government current tax receipts: Taxes on production and imports: Excise taxes
    'W014RC1A027NBEA', # Federal government current transfer payments
    'W010RC1A027NBEA', # Federal government current transfer payments: Other current transfer payments
    'AFGSL', # Federal government current transfer payments: Other current transfer payments: Grants-in-aid to state and local governments
    'M318191A027NBEA', # Federal government expenditures: Budget outlays
    'M318201A027NBEA', # Federal government expenditures: Coverage differences (NIPA vs. Budget)
    'M318221A027NBEA', # Federal government expenditures: Coverage differences: Federal employee retirement plan transactions (NIPA vs. Budget)
    'M318261A027NBEA', # Federal government expenditures: Coverage differences: Federal employee retirement plan transactions: Administrative expenses (NIPA vs. Budget)
    'M318251A027NBEA', # Federal government expenditures: Coverage differences: Federal employee retirement plan transactions: Benefits paid (NIPA vs. Budget)
    'M318241A027NBEA', # Federal government expenditures: Coverage differences: Federal employee retirement plan transactions: Contributions received (employer) (NIPA vs. Budget)
    'M318231A027NBEA', # Federal government expenditures: Coverage differences: Federal employee retirement plan transactions: Interest received (NIPA vs. Budget)
    'M318311A027NBEA', # Federal government expenditures: Coverage differences: Financial transactions (NIPA vs. Budget)
    'B1069C1A027NBEA', # Federal government expenditures: Coverage differences: Financial transactions: Deposit insurance (NIPA vs. Budget)
    'M318321A027NBEA', # Federal government expenditures: Coverage differences: Financial transactions: Loan disbursements less loan repayments and sales (NIPA vs. Budget)
    'M318341A027NBEA', # Federal government expenditures: Coverage differences: Financial transactions: Net purchases of foreign currency (NIPA vs. Budget)
    'M318351A027NBEA', # Federal government expenditures: Coverage differences: Financial transactions: Other (NIPA vs. Budget)
    'M318271A027NBEA', # Federal government expenditures: Coverage differences: Financing disbursements from credit programs (NIPA vs. Budget)
    'M318291A027NBEA', # Federal government expenditures: Coverage differences: Net investment (NIPA vs. Budget)
    'M318511A027NBEA', # Federal government expenditures: Coverage differences: Net investment (NIPA vs. Budget) (DISCONTINUED)
    'M318361A027NBEA', # Federal government expenditures: Coverage differences: Net purchases of nonproduced assets (NIPA vs. Budget)
    'M318381A027NBEA', # Federal government expenditures: Coverage differences: Net purchases of nonproduced assets: Land and other (NIPA vs. Budget) (DISCONTINUED)
    'M318371A027NBEA', # Federal government expenditures: Coverage differences: Net purchases of nonproduced assets: Outer Continental Shelf (NIPA vs. Budget) (DISCONTINUED)
    'M318391A027NBEA', # Federal government expenditures: Coverage differences: Other (NIPA vs. Budget)
    'M318281A027NBEA', # Federal government expenditures: Coverage differences: Other differences in funds covered (NIPA vs. Budget)
    'M318401A027NBEA', # Federal government expenditures: Netting and grossing differences
    'W707MC1A027NBEA', # Federal government expenditures: Netting and grossing differences: Current surplus of government enterprises
    'W706MC1A027NBEA', # Federal government expenditures: Netting and grossing differences: Interest receipts
    'M318431A027NBEA', # Federal government expenditures: Netting and grossing differences: Other
    'M318411A027NBEA', # Federal government expenditures: Netting and grossing differences: Supplementary medical insurance premiums
    'M318441A027NBEA', # Federal government expenditures: Timing differences (NIPA vs. Budget)
    'M318471A027NBEA', # Federal government expenditures: Timing differences: Current transfer payments (NIPA vs. Budget)
    'M318461A027NBEA', # Federal government expenditures: Timing differences: Interest payments (NIPA vs. Budget)
    'W708MC1A027NBEA', # Federal government expenditures: Timing differences: Other (NIPA vs. Budget)
    'M318451A027NBEA', # Federal government expenditures: Timing differences: Purchases (increase in payables net of advances) (NIPA vs. Budget)
    'M318011A027NBEA', # Federal government receipts: Budget receipts
    'M318021A027NBEA', # Federal government receipts: Coverage differences (NIPA vs. Budget)
    'M318041A027NBEA', # Federal government receipts: Coverage differences: Contributions received by federal employee retirement plans (NIPA vs. Budget)
    'M318061A027NBEA', # Federal government receipts: Coverage differences: Financial transactions (NIPA vs. Budget)
    'M318071A027NBEA', # Federal government receipts: Coverage differences: Other (NIPA vs. Budget)
    'M318081A027NBEA', # Federal government receipts: Netting and grossing differences
    'W705MC1A027NBEA', # Federal government receipts: Netting and grossing differences: Current surplus of government enterprises
    'W704MC1A027NBEA', # Federal government receipts: Netting and grossing differences: Interest receipts
    'M318111A027NBEA', # Federal government receipts: Netting and grossing differences: Other
    'M318091A027NBEA', # Federal government receipts: Netting and grossing differences: Supplementary medical insurance premiums
    'M318121A027NBEA', # Federal government receipts: Timing differences (NIPA vs. Budget)
    'M318161A027NBEA', # Federal government receipts: Timing differences: Excise taxes (NIPA vs. Budget)
    'M318141A027NBEA', # Federal government receipts: Timing differences: Federal and state unemployment insurance taxes (NIPA vs. Budget)
    'M318171A027NBEA', # Federal government receipts: Timing differences: Other (NIPA vs. Budget)
    'M318561A027NBEA', # Federal government saving, national income and product accounts
    'G170911A027NBEA', # Federal government subsidies: Economic affairs
    'W697RC1A027NBEA', # Federal government subsidies: Economic affairs: Other economic affairs
    'G170931A027NBEA', # Federal government subsidies: Economic affairs: Other economic affairs: Agriculture
    'G170921A027NBEA', # Federal government subsidies: Economic affairs: Other economic affairs: General economic and labor affairs
    'G170951A027NBEA', # Federal government subsidies: Economic affairs: Other economic affairs: Natural resources
    'G170961A027NBEA', # Federal government subsidies: Economic affairs: Transportation
    'G170981A027NBEA', # Federal government subsidies: Housing and community services
    'W019RC1A027NBEA', # Federal government total expenditures
    'AD08RC1A027NBEA', # Federal government total expenditures: Net purchases of nonproduced assets
    'W018RC1A027NBEA', # Federal government total receipts
    'G170591A027NBEA', # Federal grants-in-aid to state and local governments: Economic affairs
    'W695RC1A027NBEA', # Federal grants-in-aid to state and local governments: Economic affairs: Other economic affairs
    'G170611A027NBEA', # Federal grants-in-aid to state and local governments: Economic affairs: Other economic affairs: Agriculture
    'G170621A027NBEA', # Federal grants-in-aid to state and local governments: Economic affairs: Other economic affairs: Energy
    'G170601A027NBEA', # Federal grants-in-aid to state and local governments: Economic affairs: Other economic affairs: General economic and labor affairs
    'G170631A027NBEA', # Federal grants-in-aid to state and local governments: Economic affairs: Other economic affairs: Natural resources
    'G170651A027NBEA', # Federal grants-in-aid to state and local governments: Economic affairs: Space
    'G170641A027NBEA', # Federal grants-in-aid to state and local governments: Economic affairs: Transportation
    'G170691A027NBEA', # Federal grants-in-aid to state and local governments: Education
    'G170561A027NBEA', # Federal grants-in-aid to state and local governments: General public service
    'G170671A027NBEA', # Federal grants-in-aid to state and local governments: Health
    'G170661A027NBEA', # Federal grants-in-aid to state and local governments: Housing and community services
    'G170701A027NBEA', # Federal grants-in-aid to state and local governments: Income security
    'G170711A027NBEA', # Federal grants-in-aid to state and local governments: Income security: Disability
    'G170751A027NBEA', # Federal grants-in-aid to state and local governments: Income security: Other
    'G170741A027NBEA', # Federal grants-in-aid to state and local governments: Income security: Unemployment
    'G170731A027NBEA', # Federal grants-in-aid to state and local governments: Income security: Welfare and social services
    'G170571A027NBEA', # Federal grants-in-aid to state and local governments: National defense
    'G170581A027NBEA', # Federal grants-in-aid to state and local governments: Public order and safety
    'G170681A027NBEA', # Federal grants-in-aid to state and local governments: Recreation and culture
    'B1188C1A027NBEA', # Federal income and excess profits taxes, IRS
    'B1190C1A027NBEA', # Federal income and excess profits taxes, IRS: Amounts paid to U.S. Treasury by Federal Reserve banks
    'B1189C1A027NBEA', # Federal income and excess profits taxes, IRS: Posttabulation amendments and revisions, including results of audit and renegotiation and carryback refunds
    'B1199C1A027NBEA', # Federal income and excess profits taxes, IRS: Taxes paid by domestic corporations to foreign governments on income earned abroad
    'B1191C1A027NBEA', # Federal income and excess profits taxes, IRS: U.S. tax credits claimed for foreign taxes paid
    'B1192C1A027NBEA', # Federal income and excess profits taxes, IRS: U.S. tax credits claimed: Investment tax credit
    'B1193C1A027NBEA', # Federal income and excess profits taxes, IRS: U.S. tax credits claimed: Other tax credits
    'W543RC1A027NBEA', # Financial services furnished without payment: Borrower services: Government
    'W538RC1A027NBEA', # Financial services furnished without payment: Depositor services: Government
    'GCEA', # Government Consumption Expenditures and Gross Investment
    'Y650RC1A027NBEA', # Government Consumption Expenditures and Gross Investment: State and Local: Net Health: Gross expenditures
    'W069RC1A027NBEA', # Government capital transfer payments
    'W067RC1A027NBEA', # Government capital transfer receipts
    'W102RC1A027NBEA', # Government consumption expenditures: Gross output of general government: Value added
    'A184RC1A027NBEA', # Government current expenditures: Wage accruals less disbursements (DISCONTINUED)
    'W021RC1A027NBEA', # Government current receipts
    'W782RC1A027NBEA', # Government current receipts: Contributions for government social insurance
    'W054RC1A027NBEA', # Government current tax receipts
    'W008RC1A027NBEA', # Government current tax receipts: Taxes from the rest of the world
    'A084RC1A027NBEA', # Government current transfer payments
    'W017RC1A027NBEA', # Government current transfer payments: Other current transfer payments to the rest of the world (net)
    'A882RC1A027NBEA', # Government enterprise gross fixed investment
    'A883RC1A027NBEA', # Government enterprise gross fixed investment: Federal
    'B885RC1A027NBEA', # Government enterprise gross fixed investment: Federal: Equipment and software (DISCONTINUED)
    'B884RC1A027NBEA', # Government enterprise gross fixed investment: Federal: Structures
    'A886RC1A027NBEA', # Government enterprise gross fixed investment: State and local
    'B888RC1A027NBEA', # Government enterprise gross fixed investment: State and local: Equipment and software (DISCONTINUED)
    'B887RC1A027NBEA', # Government enterprise gross fixed investment: State and local: Structures
    'W058RC1A027NBEA', # Government income receipts on assets
    'W059RC1A027NBEA', # Government income receipts on assets: Interest and miscellaneous receipts
    'A391RC1A027NBEA', # Government saving: Other (excluding social insurance funds)
    'A221RC1A027NBEA', # Government saving: Social insurance funds
    'A1670C1A027NBEA', # Government social insurance funds: Current federal expenditures
    'L313091A027NBEA', # Government social insurance funds: Current federal expenditures: Administrative expenses (consumption expenditures)
    'A2046C1A027NBEA', # Government social insurance funds: Current federal receipts
    'L313071A027NBEA', # Government social insurance funds: Current federal receipts: Interest received
    'A745RC1A027NBEA', # Government social insurance funds: Current state and local expenditures
    'B741RC1A027NBEA', # Government social insurance funds: Current state and local expenditures: Administrative expenses (consumption expenditures)
    'B742RC1A027NBEA', # Government social insurance funds: Current state and local expenditures: Government social benefit payments to persons
    'A743RC1A027NBEA', # Government social insurance funds: Current state and local receipts
    'B746RC1A027NBEA', # Government social insurance funds: Current state and local receipts: Interest received
    'G170791A027NBEA', # Government subsidies: Economic affairs
    'W696RC1A027NBEA', # Government subsidies: Economic affairs: Other economic affairs
    'G170811A027NBEA', # Government subsidies: Economic affairs: Other economic affairs: Agriculture
    'G170821A027NBEA', # Government subsidies: Economic affairs: Other economic affairs: Energy
    'G170801A027NBEA', # Government subsidies: Economic affairs: Other economic affairs: General economic and labor affairs
    'G170831A027NBEA', # Government subsidies: Economic affairs: Other economic affairs: Natural resources
    'G170841A027NBEA', # Government subsidies: Economic affairs: Transportation
    'L312041A027NBEA', # Government subsidies: Federal: Agricultural
    'L312071A027NBEA', # Government subsidies: Federal: Air carriers
    'L312051A027NBEA', # Government subsidies: Federal: Housing
    'L312061A027NBEA', # Government subsidies: Federal: Maritime
    'L312081A027NBEA', # Government subsidies: Federal: Other
    'G170871A027NBEA', # Government subsidies: Housing and community services
    'W068RC1A027NBEA', # Government total expenditures
    'AD07RC1A027NBEA', # Government total expenditures: Net purchases of nonproduced assets
    'W066RC1A027NBEA', # Government total receipts
    'A927RC1A027NBEA', # Gross government saving
    'A926RC1A027NBEA', # Gross government saving: Federal
    'A925RC1A027NBEA', # Gross government saving: State and local
    'A765RC1A027NBEA', # Gross value added: GDP: General government
    'A766RC1A027NBEA', # Gross value added: GDP: General government: Federal
    'A767RC1A027NBEA', # Gross value added: GDP: General government: State and local
    'Y709RC1A027NBEA', # Local Government Current Expenditures: Interest payments: to persons and business
    'Y710RC1A027NBEA', # Local Government Current Expenditures: Interest payments: to the rest of the world
    'LA0000211A027NBEA', # Local Government Current transfer payments: Current transfer payments to the rest of the world
    'LA0000221A027NBEA', # Local Government Current transfer receipts: From the rest of the world
    'W864RC1A027NBEA', # Local government capital transfer receipts
    'W858RC1A027NBEA', # Local government current expenditures: Wage accruals less disbursements (DISCONTINUED)
    'W830RC1A027NBEA', # Local government current receipts
    'W850RC1A027NBEA', # Local government current receipts: Current surplus of government enterprises
    'W845RC1A027NBEA', # Local government current receipts: Current transfer receipts
    'W846RC1A027NBEA', # Local government current receipts: Current transfer receipts: Federal grants-in-aid
    'W847RC1A027NBEA', # Local government current receipts: Current transfer receipts: State government grants-in-aid
    'W848RC1A027NBEA', # Local government current receipts: Current transfer receipts: from business (net)
    'W849RC1A027NBEA', # Local government current receipts: Current transfer receipts: from persons
    'W841RC1A027NBEA', # Local government current receipts: Income receipts on assets
    'W842RC1A027NBEA', # Local government current receipts: Income receipts on assets: Interest receipts
    'W844RC1A027NBEA', # Local government current receipts: Income receipts on assets: Rents and royalties
    'W831RC1A027NBEA', # Local government current tax receipts
    'W8735C1A027NBEA', # Local government current tax receipts: Taxes on production and imports
    'W838RC1A027NBEA', # Local government current tax receipts: Taxes on production and imports: Other
    'W837RC1A027NBEA', # Local government current tax receipts: Taxes on production and imports: Property taxes
    'W836RC1A027NBEA', # Local government current tax receipts: Taxes on production and imports: Sales taxes
    'W868RC1A027NBEA', # Local government expenditures: Net purchases of nonproduced assets
    'W861RC1A027NBEA', # Local government saving: Other (DISCONTINUED)
    'W865RC1A027NBEA', # Local government total expenditures
    'W862RC1A027NBEA', # Local government total receipts
    'W870RC1A027NBEA', # Local government: Net lending or net borrowing (-)
    'W065RC1A027NBEA', # Monetary dividends received: Government
    'W500RC1A027NBEA', # Monetary interest paid: Government
    'A091RC1A027NBEA', # Monetary interest paid: Government: Federal
    'Y669RC1A027NBEA', # Monetary interest paid: Government: Federal
    'W497RC1A027NBEA', # Monetary interest paid: Government: State and local
    'Y711RC1A027NBEA', # Monetary interest paid: Rest of the world: to government
    'A2071C1A027NBEA', # Monetary interest received: Government
    'B1139C1A027NBEA', # Monetary interest received: Government: Federal
    'B1140C1A027NBEA', # Monetary interest received: Government: State and local
    'Y051RC1A027NBEA', # National Defense Gross Investment: Equipment: Electronics
    'B999RC1A027NBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Aircraft
    'B388RC1A027NBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Electronics
    'B277RC1A027NBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Missiles
    'B389RC1A027NBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Other durable goods
    'B278RC1A027NBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Ships
    'B288RC1A027NBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Vehicles
    'B781RC1A027NBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Ammunition
    'B783RC1A027NBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Other nondurable goods
    'B780RC1A027NBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Petroleum products
    'B911RC1A027NBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Installation support
    'B913RC1A027NBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Personnel support
    'B784RC1A027NBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Research and development (DISCONTINUED)
    'B786RC1A027NBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Transportation of material
    'B785RC1A027NBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Travel of persons
    'B912RC1A027NBEA', # National defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Weapons support
    'W090RC1A027NBEA', # National defense consumption expenditures: Gross output of general government: Value added: Compensation of general government employees: Civilian
    'B4080C1A027NBEA', # National defense consumption expenditures: Gross output of general government: Value added: Compensation of general government employees: Military
    'B436RC1A027NBEA', # National income without capital consumption adjustment: Government
    'AFDEF', # Net Federal Government Saving
    'L318511A027NBEA', # Net federal government saving, national income and product accounts (DISCONTINUED)
    'B244RC1A027NBEA', # Net federal government saving: Other (excluding social insurance funds)
    'B243RC1A027NBEA', # Net federal government saving: Social insurance funds
    'A922RC1A027NBEA', # Net government saving
    'A924RC1A027NBEA', # Net government saving: State and local
    'A085RC1A027NBEA', # Net interest (paid and received) paid by government
    'AD01RC1A027NBEA', # Net lending or net borrowing (-), NIPAs: Government
    'AD02RC1A027NBEA', # Net lending or net borrowing (-), NIPAs: Government: Federal
    'AD03RC1A027NBEA', # Net lending or net borrowing (-), NIPAs: Government: State and local
    'W859RC1A027NBEA', # Net local government saving
    'B119RC1A027NBEA', # Net state and local government saving: Other (exluding social insurance funds)
    'B118RC1A027NBEA', # Net state and local government saving: Social insurance funds
    'W759RC1A027NBEA', # Net state government saving
    'A194RC1A027NBEA', # Net value added: Net domestic product: General government
    'B568RC1A027NBEA', # Net value added: Net domestic product: General government: Federal
    'B251RC1A027NBEA', # Net value added: Net domestic product: General government: State and local
    'W420RC1A027NBEA', # Nonprofit institution current transfer payments: to government
    'W550RC1A027NBEA', # Premium supplements for property and casualty insurance: Government
    'W775RC1A027NBEA', # Saving and investment: Disaster losses: Government
    'W776RC1A027NBEA', # Saving and investment: Disaster losses: Government: Federal
    'W777RC1A027NBEA', # Saving and investment: Disaster losses: Government: State and local
    'Y651RC1A027NBEA', # Selected Government Consumption Expenditures and Gross Investment: State and Local: Net Health: Sales to other sectors
    'Y707RC1A027NBEA', # State Government Current Expenditures: Interest payments: to persons and business
    'Y708RC1A027NBEA', # State Government Current Expenditures: Interest payments: to the rest of the world
    'LA0000191A027NBEA', # State Government Current transfer payments: Current transfer payments to the rest of the world
    'LA0000201A027NBEA', # State Government Current transfer receipts: From the rest of the world
    'SLCEA', # State and Local Government Consumption Expenditures and Gross Investment
    'ASLEXPND', # State and Local Government Current Expenditures
    'Y705RC1A027NBEA', # State and Local Government Current Receipts and Expenditures: Current Expenditures: Interest payments: to persons and business
    'Y396RC1A027NBEA', # State and Local Government Expenditures: State and local employee retirement plan transactions: Imputed interest for unfunded actuarial liability
    'LA0000321A027NBEA', # State and Local Government Expenditures: Statistical differences, expenditure
    'ASLRSI', # State and Local Government Receipts: Contributions for Social Insurance
    'LA0000311A027NBEA', # State and Local Government Revenue: Statistical differences, revenue
    'ASLRECPT', # State and Local Government: Current Receipts
    'ASLCTAX', # State and Local Government: Tax Receipts on Corporate Income
    'ASLPTAX', # State and Local Government: Taxes on production and imports: Property Taxes
    'ASLSTAX', # State and Local Government: Taxes on production and imports: Sales Taxes
    'W139RC1A027NBEA', # State and Local government consumption expenditures: Gross output of general government: Value added
    'L319011A027NBEA', # State and Local government current receipts: Census total revenue
    'L319021A027NBEA', # State and Local government current receipts: Coverage differences (NIPA vs. Census)
    'W720RC1A027NBEA', # State and Local government current receipts: Coverage differences: Certain dividends (NIPA vs. Census)
    'L319091A027NBEA', # State and Local government current receipts: Coverage differences: Certain grant programs (NIPA vs. Census)
    'W721RC1A027NBEA', # State and Local government current receipts: Coverage differences: Current surplus of Indian tribal government enterprises (NIPA vs. Census)
    'L319111A027NBEA', # State and Local government current receipts: Coverage differences: Financial transactions (NIPA vs. Census)
    'W722RC1A027NBEA', # State and Local government current receipts: Coverage differences: Imputed interest received and net insurance settlements (NIPA vs. Census)
    'L319121A027NBEA', # State and Local government current receipts: Coverage differences: Sale of land (NIPA vs. Census)
    'L319031A027NBEA', # State and Local government current receipts: Coverage differences: State and local employee retirement plan transactions (NIPA vs. Census)
    'L319071A027NBEA', # State and Local government current receipts: Coverage differences: State and local employee retirement plan transactions: Capital gains net of losses (NIPA vs. Census)
    'L319041A027NBEA', # State and Local government current receipts: Coverage differences: State and local employee retirement plan transactions: Contributions (NIPA vs. Census)
    'L319061A027NBEA', # State and Local government current receipts: Coverage differences: State and local employee retirement plan transactions: Dividends received (NIPA vs. Census)
    'L319051A027NBEA', # State and Local government current receipts: Coverage differences: State and local employee retirement plan transactions: Interest received (NIPA vs. Census)
    'L319081A027NBEA', # State and Local government current receipts: Coverage differences: Unemployment insurance fund contributions and earnings (NIPA vs. Census)
    'L319141A027NBEA', # State and Local government current receipts: Netting and grossing differences
    'W723RC1A027NBEA', # State and Local government current receipts: Netting and grossing differences: Current expenditures of government enterprises
    'L319161A027NBEA', # State and Local government current receipts: Netting and grossing differences: Government sales included in Census total revenue
    'W724RC1A027NBEA', # State and Local government current receipts: Netting and grossing differences: Insurance claims included in Census total revenue
    'L319191A027NBEA', # State and Local government current receipts: Timing and other differences (NIPA vs. Census)
    'L319211A027NBEA', # State and Local government current receipts: Timing and other differences: Other timing differences and other (NIPA vs. Census)
    'W080RC1A027NBEA', # State and local government capital transfer payments
    'AD06RC1A027NBEA', # State and local government capital transfer receipts (DISCONTINUED)
    'L319221A027NBEA', # State and local government current receipts, NIPAs
    'B115RC1A027NBEA', # State and local government current receipts: Current surplus of government enterprises
    'B109RC1A027NBEA', # State and local government current receipts: Government social benefit payments to persons
    'W074RC1A027NBEA', # State and local government current receipts: Income receipts on assets
    'B081RC1A027NBEA', # State and local government current receipts: Income receipts on assets: Dividends
    'B112RC1A027NBEA', # State and local government current receipts: Income receipts on assets: Interest receipts
    'S230541A027NBEA', # State and local government current receipts: Income receipts on assets: Rents and royalties
    'B111RC1A027NBEA', # State and local government current receipts: Interest payments
    'B114RC1A027NBEA', # State and local government current receipts: Subsidies
    'B116RC1A027NBEA', # State and local government current receipts: Wage accruals less disbursements (DISCONTINUED)
    'W070RC1A027NBEA', # State and local government current tax receipts
    'ASLPITAX', # State and local government current tax receipts: Personal current taxes: Income taxes
    'W072RC1A027NBEA', # State and local government current tax receipts: Taxes on production and imports
    'W073RC1A027NBEA', # State and local government current tax receipts: Taxes on production and imports: Other
    'AD09RC1A027NBEA', # State and local government expenditures: Net purchases of nonproduced assets
    'L319471A027NBEA', # State and local government net saving, national income and product accounts
    'G171001A027NBEA', # State and local government subsidies: Economic affairs
    'G171011A027NBEA', # State and local government subsidies: Economic affairs: Energy
    'G171021A027NBEA', # State and local government subsidies: Economic affairs: Transportation
    'G171041A027NBEA', # State and local government subsidies: Housing and community services
    'L319411A027NBEA', # State and local government surplus/deficit: Census total revenue minus Census total expenditures
    'W079RC1A027NBEA', # State and local government total expenditures
    'W077RC1A027NBEA', # State and local government total receipts
    'W764RC1A027NBEA', # State government capital transfer receipts
    'W758RC1A027NBEA', # State government current expenditures: Wage accruals less disbursements (DISCONTINUED)
    'W730RC1A027NBEA', # State government current receipts
    'W740RC1A027NBEA', # State government current receipts: Contributions for government social insurance
    'W750RC1A027NBEA', # State government current receipts: Current surplus of government enterprises
    'W745RC1A027NBEA', # State government current receipts: Current transfer receipts
    'W746RC1A027NBEA', # State government current receipts: Current transfer receipts: Federal grants-in-aid
    'W747RC1A027NBEA', # State government current receipts: Current transfer receipts: Local government grants-in-aid
    'W748RC1A027NBEA', # State government current receipts: Current transfer receipts: from business (net)
    'W749RC1A027NBEA', # State government current receipts: Current transfer receipts: from persons
    'W741RC1A027NBEA', # State government current receipts: Income receipts on assets
    'W743RC1A027NBEA', # State government current receipts: Income receipts on assets: Dividends
    'W742RC1A027NBEA', # State government current receipts: Income receipts on assets: Interest receipts
    'W744RC1A027NBEA', # State government current receipts: Income receipts on assets: Rents and royalties
    'W731RC1A027NBEA', # State government current tax receipts
    'W7735C1A027NBEA', # State government current tax receipts: Taxes on production and imports
    'W738RC1A027NBEA', # State government current tax receipts: Taxes on production and imports: Other
    'W737RC1A027NBEA', # State government current tax receipts: Taxes on production and imports: Property taxes
    'W736RC1A027NBEA', # State government current tax receipts: Taxes on production and imports: Sales taxes
    'W768RC1A027NBEA', # State government expenditures: Net purchases of nonproduced assets
    'W761RC1A027NBEA', # State government saving: Other
    'W760RC1A027NBEA', # State government saving: Social insurance funds
    'W765RC1A027NBEA', # State government total expenditures
    'W762RC1A027NBEA', # State government total receipts
    'W770RC1A027NBEA', # State government: Net lending or net borrowing (-)
    'B2004C1A027NBEA', # Taxes on production and imports: Federal: Excise taxes: Air transport
    'B2001C1A027NBEA', # Taxes on production and imports: Federal: Excise taxes: Alcoholic beverages
    'B2005C1A027NBEA', # Taxes on production and imports: Federal: Excise taxes: Crude oil windfall profits tax
    'B2003C1A027NBEA', # Taxes on production and imports: Federal: Excise taxes: Diesel fuel
    'B2000C1A027NBEA', # Taxes on production and imports: Federal: Excise taxes: Gasoline
    'B2006C1A027NBEA', # Taxes on production and imports: Federal: Excise taxes: Other
    'B2002C1A027NBEA', # Taxes on production and imports: Federal: Excise taxes: Tobacco
    'B036RC1A027NBEA', # Taxes on production and imports: Federal: Other
    'A1667C1A027NBEA', # Taxes on production and imports: Local government: Sales taxes
    'L305211A027NBEA', # Taxes on production and imports: Local government: Sales taxes: General
    'L305231A027NBEA', # Taxes on production and imports: Local government: Sales taxes: Other
    'L305221A027NBEA', # Taxes on production and imports: Local government: Sales taxes: Public utilities
    'S230201A027NBEA', # Taxes on production and imports: State and local government: Motor vehicle licenses
    'S230401A027NBEA', # Taxes on production and imports: State and local government: Other taxes (DISCONTINUED)
    'S230431A027NBEA', # Taxes on production and imports: State and local government: Severance taxes
    'S230551A027NBEA', # Taxes on production and imports: State and local government: Special assessments
    'A1666C1A027NBEA', # Taxes on production and imports: State government: Sales taxes
    'L305151A027NBEA', # Taxes on production and imports: State government: Sales taxes: Alcoholic beverages
    'L305141A027NBEA', # Taxes on production and imports: State government: Sales taxes: Gasoline
    'L305131A027NBEA', # Taxes on production and imports: State government: Sales taxes: General
    'L305181A027NBEA', # Taxes on production and imports: State government: Sales taxes: Insurance receipts
    'L305191A027NBEA', # Taxes on production and imports: State government: Sales taxes: Other
    'L305171A027NBEA', # Taxes on production and imports: State government: Sales taxes: Public utilities
    'L305161A027NBEA', # Taxes on production and imports: State government: Sales taxes: Tobacco
    ## Bil. of Chn. 2005 $ (NSA)
    'B885RX1A020NBEA', # Real government enterprise gross fixed investment: Federal: Equipment and software (DISCONTINUED)
    'B888RX1A020NBEA', # Real government enterprise gross fixed investment: State and local: Equipment and software (DISCONTINUED)
    'B784RX1A020NBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Research and development (DISCONTINUED)
    'B878RX1A020NBEA', # Real national defense gross investment: Equipment and software: Electronics and software (DISCONTINUED)
    ## Bil. of Chn. 2017 $ (NSA)
    'FGCECA', # Real Federal Consumption Expenditures and Gross Investment
    'GCECA', # Real Government Consumption Expenditures and Gross Investment
    'Y650RX1A020NBEA', # Real Government Consumption Expenditures and Gross Investment: State and Local: Net Health: Gross expenditures
    'Y651RX1A020NBEA', # Real Government Consumption Expenditures and Gross Investment: State and Local: Net Health: Sales to other sectors
    'Y051RX1A020NBEA', # Real National Defense Gross Investment: Equipment: Electronics
    'SLCECA', # Real State and Local Consumption Expenditures & Gross Investment
    'W086RX1A020NBEA', # Real federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Value added
    'B237RX1A020NBEA', # Real federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Value added: Compensation of general government employees
    'B432RX1A020NBEA', # Real federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Value added: Consumption of general government fixed capital
    'W111RX1A020NBEA', # Real federal government consumption expenditures: Gross output of general government: Value added
    'B995RX1A020NBEA', # Real federal government consumption expenditures: Gross output of general government: Value added: Consumption of general government fixed capital
    'W129RX1A020NBEA', # Real federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Value added
    'W130RX1A020NBEA', # Real federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Value added: Compensation of general government employees
    'B546RX1A020NBEA', # Real federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Value added: Consumption of general government fixed capital
    'W102RX1A020NBEA', # Real government consumption expenditures: Gross output of general government: Value added
    'A882RX1A020NBEA', # Real government enterprise gross fixed investment
    'A883RX1A020NBEA', # Real government enterprise gross fixed investment: Federal
    'B884RX1A020NBEA', # Real government enterprise gross fixed investment: Federal: Structures
    'A886RX1A020NBEA', # Real government enterprise gross fixed investment: State and local
    'B887RX1A020NBEA', # Real government enterprise gross fixed investment: State and local: Structures
    'A765RX1A020NBEA', # Real gross value added: GDP: General government
    'A766RX1A020NBEA', # Real gross value added: GDP: General government: Federal
    'A767RX1A020NBEA', # Real gross value added: GDP: General government: State and local
    'A975RX1A020NBEA', # Real national defense consumption expenditures and gross investment: Residual
    'B999RX1A020NBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Aircraft
    'B388RX1A020NBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Electronics
    'B277RX1A020NBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Missiles
    'B389RX1A020NBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Other durable goods
    'B278RX1A020NBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Ships
    'B288RX1A020NBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Vehicles
    'B781RX1A020NBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Ammunition
    'B783RX1A020NBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Other nondurable goods
    'B780RX1A020NBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Petroleum products
    'B911RX1A020NBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Installation support
    'B913RX1A020NBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Personnel support
    'B786RX1A020NBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Transportation of material
    'B785RX1A020NBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Travel of persons
    'B912RX1A020NBEA', # Real national defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Weapons support
    'W090RX1A020NBEA', # Real national defense consumption expenditures: Gross output of general government: Value added: Compensation of general government employees: Civilian
    'B4080X1A020NBEA', # Real national defense consumption expenditures: Gross output of general government: Value added: Compensation of general government employees: Military
    'B874RX1A020NBEA', # Real national defense gross investment: Equipment: Aircraft
    'B875RX1A020NBEA', # Real national defense gross investment: Equipment: Missiles
    'B879RX1A020NBEA', # Real national defense gross investment: Equipment: Other equipment
    'B876RX1A020NBEA', # Real national defense gross investment: Equipment: Ships
    'B877RX1A020NBEA', # Real national defense gross investment: Equipment: Vehicles
    'A194RX1A020NBEA', # Real net value added: Net domestic product: General government
    'B568RX1A020NBEA', # Real net value added: Net domestic product: General government: Federal
    'B251RX1A020NBEA', # Real net value added: Net domestic product: General government: State and local
    'W139RX1A020NBEA', # Real state and local government consumption expenditures: Gross output of general government: Value added
    'B986RX1A020NBEA', # Real state and local government consumption expenditures: Gross output of general government: Value added: Consumption of general government fixed capital
    ## Mil. of $ (NSA)
    'IEACTPA', # Capital transfer payments and other debits
    'IEACTRA', # Capital transfer receipts and other credits
    ## Percentage Points at Annual Rate (NSA)
    'Y058RZ2A224NBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Federal: Gross Investment: Equipment
    'Y059RZ2A224NBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Federal: Gross Investment: Intellectual Property Products
    'Y061RZ2A224NBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Federal: Gross Investment: Intellectual Property Products: Research and Development
    'Y060RZ2A224NBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Federal: Gross Investment: Intellectual Property Products: Software
    'Y050RZ2A224NBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Federal: National Defense: Gross Investment: Equipment
    'Y052RZ2A224NBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Federal: National Defense: Gross Investment: Intellectual Property Products
    'Y076RZ2A224NBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Federal: National Defense: Gross Investment: Intellectual Property Products: Research and Development
    'Y053RZ2A224NBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Federal: National Defense: Gross Investment: Intellectual Property Products: Software
    'Y066RZ2A224NBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Federal: Nondefense: Gross Investment: Equipment
    'Y067RZ2A224NBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Federal: Nondefense: Gross Investment: Intellectual Property Products
    'Y069RZ2A224NBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Federal: Nondefense: Gross Investment: Intellectual Property Products: Research and Development
    'Y068RZ2A224NBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Federal: Nondefense: Gross Investment: Intellectual Property Products: Software
    'Y054RZ2A224NBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Gross Investment: Equipment
    'Y055RZ2A224NBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Gross Investment: Intellectual Property Products
    'Y057RZ2A224NBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Gross Investment: Intellectual Property Products: Research and Development
    'Y056RZ2A224NBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: Gross Investment: Intellectual Property Products: Software
    'Y070RZ2A224NBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: State and Local: Gross Investment: Equipment
    'Y071RZ2A224NBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: State and Local: Gross Investment: Intellectual Property Products
    'Y073RZ2A224NBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: State and Local: Gross Investment: Intellectual Property Products: Research and Development
    'Y072RZ2A224NBEA', # Contribution to Percent Change in Real Government Consumption Expenditures and Gross Investment: State and Local: Gross Investment: Intellectual Property Products: Software
    'A997RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures
    'W085RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government
    'W087RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased
    'A998RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods
    'B999RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Aircraft
    'B388RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Electronics
    'B277RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Missiles
    'B389RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Other durable goods
    'B278RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Ships
    'B288RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods: Vehicles
    'A725RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods
    'B781RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Ammunition
    'B783RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Other nondurable goods
    'B780RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Petroleum products
    'A489RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services
    'B911RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Installation support
    'B913RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Personnel support
    'B786RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Transportation of material
    'B785RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Travel of persons
    'B912RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services: Weapons support
    'W086RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Value added
    'B237RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Value added: Compensation of general government employees
    'W090RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Value added: Compensation of general government employees: Civilian
    'B408RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Value added: Compensation of general government employees: Military
    'B432RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Gross output of general government: Value added: Consumption of general government fixed capital
    'W088RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Own-account investment
    'W089RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Consumption expenditures: Sales to other sectors
    'A788RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Gross investment
    'Y050RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Gross investment: Equipment
    'B874RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Gross investment: Equipment: Aircraft
    'Y051RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Gross investment: Equipment: Electronics
    'B875RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Gross investment: Equipment: Missiles
    'B879RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Gross investment: Equipment: Other equipment
    'B876RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Gross investment: Equipment: Ships
    'B877RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Gross investment: Equipment: Vehicles
    'Y052RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Gross investment: Intellectual property products
    'Y076RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Gross investment: Intellectual property products: Research and development
    'Y053RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Gross investment: Intellectual property products: Software
    'A808RN2A224NBEA', # Contributions to Percent Change in National Defense Consumption Expenditures and Gross Investment: Gross investment: Structures
    'Y650RZ2A224NBEA', # Contributions to Percent Change in Real Government Consumption Expenditures and Gross Investment: State and Local: Net Health: Gross expenditures
    'Y651RZ2A224NBEA', # Contributions to Percent Change in Real Government Consumption Expenditures and Gross Investment: State and Local: Net Health: Sales to other sectors
    ## Thous. of $ (NSA)
    'USALCOTAX', # State Government Tax Collections, Alcoholic Beverages - Selective Sales Taxes in the United States
    'USALCLICTAX', # State Government Tax Collections, Alcoholic Beverages Licenses in the United States
    'USAMUSTAX', # State Government Tax Collections, Amusements - Selective Sales Taxes in the United States
    'USAMSLICTAX', # State Government Tax Collections, Amusements Licenses in the United States
    'USCORPINCTX', # State Government Tax Collections, Corporation Net Income Taxes in the United States
    'USCORPLICTAX', # State Government Tax Collections, Corporations in General Licenses in the United States
    'USDTHGFTAX', # State Government Tax Collections, Death and Gift Taxes in the United States
    'USDOCUTAX', # State Government Tax Collections, Documentary and Stock Transfer Taxes in the United States
    'USSALESTAX', # State Government Tax Collections, General Sales and Gross Receipts Taxes in the United States
    'USHUNTLICTAX', # State Government Tax Collections, Hunting and Fishing Licenses in the United States
    'USINCTAX', # State Government Tax Collections, Individual Income Taxes in the United States
    'USINSURTAX', # State Government Tax Collections, Insurance Premiums - Selective Sales Taxes in the United States
    'USFUELTAX', # State Government Tax Collections, Motor Fuels - Selective Sales Taxes in the United States
    'USMOTOLICTAX', # State Government Tax Collections, Motor Vehicle Licenses in the United States
    'USMVOPERTAX', # State Government Tax Collections, Motor Vehicle Operators Licenses in the United States
    'USBUSLICTAX', # State Government Tax Collections, Occupation and Business Licenses in the United States
    'USOTHLICTAX', # State Government Tax Collections, Other License Taxes in the United States
    'USOTHSLSTAX', # State Government Tax Collections, Other Selective Sales and Gross Receipts Taxes in the United States
    'USPARITAX', # State Government Tax Collections, Pari-Mutuels - Selective Sales Taxes in the United States
    'USPROPTAX', # State Government Tax Collections, Property Taxes in the United States
    'USUTILITAX', # State Government Tax Collections, Public Utilities - Selective Sales Taxes in the United States
    'USUTILLICTAX', # State Government Tax Collections, Public Utilities Licenses in the United States
    'USSVRNCTAX', # State Government Tax Collections, Severance Taxes in the United States
    'USNOCLSTAX', # State Government Tax Collections, Taxes Not Elsewhere Classified in the United States
    'USTOBACTAX', # State Government Tax Collections, Tobacco Products - Selective Sales Taxes in the United States
    'USTLINCTAX', # State Government Tax Collections, Total Income Taxes in the United States
    'USTLLICTAX', # State Government Tax Collections, Total License Taxes in the United States
    'USTLOTHTAX', # State Government Tax Collections, Total Other Taxes in the United States
    'USSLGRTAX', # State Government Tax Collections, Total Sales and Gross Receipts Taxes in the United States
    'USTLSLTAX', # State Government Tax Collections, Total Selective Sales Taxes in the United States
    'USTOTLTAX', # State Government Tax Collections, Total Taxes in the United States

    # Gov't Receipts, Expenditures & Investment > Gov't Consumption Expenditures (421)
    ## Bil. of $ (NSA)
    'A957RC1A027NBEA', # Federal government consumption expenditures
    'W085RC1A027NBEA', # Federal government consumption expenditures: Defense consumption expenditures: Gross output of general government
    'W087RC1A027NBEA', # Federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased
    'A998RC1A027NBEA', # Federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods
    'A725RC1A027NBEA', # Federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods
    'A489RC1A027NBEA', # Federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services
    'W088RC1A027NBEA', # Federal government consumption expenditures: Defense consumption expenditures: Own-account investment
    'W089RC1A027NBEA', # Federal government consumption expenditures: Defense consumption expenditures: Sales to other sectors
    'W110RC1A027NBEA', # Federal government consumption expenditures: Gross output of general government
    'W113RC1A027NBEA', # Federal government consumption expenditures: Gross output of general government: Intermediate goods and services purchased
    'W114RC1A027NBEA', # Federal government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods
    'W115RC1A027NBEA', # Federal government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods
    'W116RC1A027NBEA', # Federal government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services
    'W128RC1A027NBEA', # Federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government
    'W131RC1A027NBEA', # Federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Intermediate goods and services purchased
    'A543RC1A027NBEA', # Federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods
    'A729RC1A027NBEA', # Federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods
    'B826RC1A027NBEA', # Federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Commodity Credit Corporation inventory change
    'B828RC1A027NBEA', # Federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Other nondurable goods
    'A544RC1A027NBEA', # Federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services
    'W136RC1A027NBEA', # Federal government consumption expenditures: Nondefense consumption expenditures: Own-account investment
    'W137RC1A027NBEA', # Federal government consumption expenditures: Nondefense consumption expenditures: Sales to other sectors
    'W117RC1A027NBEA', # Federal government consumption expenditures: Own-account investment
    'W118RC1A027NBEA', # Federal government consumption expenditures: Sales to other sectors
    'G171191A027NBEA', # Federal government gross investment: Economic affairs
    'G171231A027NBEA', # Federal government gross investment: Education
    'G171161A027NBEA', # Federal government gross investment: General public service
    'G171211A027NBEA', # Federal government gross investment: Health
    'G171201A027NBEA', # Federal government gross investment: Housing and community services
    'G171241A027NBEA', # Federal government gross investment: Income security
    'G171181A027NBEA', # Federal government gross investment: Public order and safety
    'G171221A027NBEA', # Federal government gross investment: Recreation and culture
    'A955RC1A027NBEA', # Government consumption expenditures
    'A824RC1A027NBEA', # Government consumption expenditures and gross investment: Federal: National defense
    'A825RC1A027NBEA', # Government consumption expenditures and gross investment: Federal: Nondefense
    'W584RC1A027NBEA', # Government consumption expenditures and gross investments: Economic affairs
    'W596RC1A027NBEA', # Government consumption expenditures and gross investments: Economic affairs: Other economic affairs
    'W586RC1A027NBEA', # Government consumption expenditures and gross investments: Economic affairs: Other economic affairs: Agriculture
    'W587RC1A027NBEA', # Government consumption expenditures and gross investments: Economic affairs: Other economic affairs: Energy
    'W585RC1A027NBEA', # Government consumption expenditures and gross investments: Economic affairs: Other economic affairs: General economic and labor affairs
    'W588RC1A027NBEA', # Government consumption expenditures and gross investments: Economic affairs: Other economic affairs: Natural resources
    'W684RC1A027NBEA', # Government consumption expenditures and gross investments: Economic affairs: Other economic affairs: Other
    'W594RC1A027NBEA', # Government consumption expenditures and gross investments: Economic affairs: Other economic affairs: Postal service
    'W595RC1A027NBEA', # Government consumption expenditures and gross investments: Economic affairs: Space
    'W589RC1A027NBEA', # Government consumption expenditures and gross investments: Economic affairs: Transportation
    'W591RC1A027NBEA', # Government consumption expenditures and gross investments: Economic affairs: Transportation: Air
    'W590RC1A027NBEA', # Government consumption expenditures and gross investments: Economic affairs: Transportation: Highways
    'W593RC1A027NBEA', # Government consumption expenditures and gross investments: Economic affairs: Transportation: Transit and railroad
    'W592RC1A027NBEA', # Government consumption expenditures and gross investments: Economic affairs: Transportation: Water
    'W600RC1A027NBEA', # Government consumption expenditures and gross investments: Education
    'W601RC1A027NBEA', # Government consumption expenditures and gross investments: Education: Elementary and secondary
    'W602RC1A027NBEA', # Government consumption expenditures and gross investments: Education: Higher
    'W682RC1A027NBEA', # Government consumption expenditures and gross investments: Education: Libraries and other
    'W603RC1A027NBEA', # Government consumption expenditures and gross investments: Education: Libraries and other: Libraries
    'W604RC1A027NBEA', # Government consumption expenditures and gross investments: Education: Libraries and other: Other
    'W620RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Economic affairs
    'W632RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Economic affairs: Other economic affairs
    'W622RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Economic affairs: Other economic affairs: Agriculture
    'W623RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Economic affairs: Other economic affairs: Energy
    'W621RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Economic affairs: Other economic affairs: General economic and labor affairs
    'W624RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Economic affairs: Other economic affairs: Natural resources
    'W630RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Economic affairs: Other economic affairs: Postal service
    'W631RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Economic affairs: Space
    'W625RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Economic affairs: Transportation
    'W627RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Economic affairs: Transportation: Air
    'W626RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Economic affairs: Transportation: Highways
    'W629RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Economic affairs: Transportation: Transit and railroad
    'W628RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Economic affairs: Transportation: Water
    'W636RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Education
    'W637RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Education: Elementary and secondary
    'W638RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Education: Higher
    'W639RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Education: Other
    'W611RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: General public service
    'W612RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: General public service: Executive and legislative
    'W614RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: General public service: Other
    'W613RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: General public service: Tax collection and financial management
    'W634RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Health
    'W633RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Housing and community services
    'W640RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Income security
    'W641RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Income security: Disability
    'W645RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Income security: Other
    'W642RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Income security: Retirement
    'W644RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Income security: Unemployment
    'W643RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Income security: Welfare and social services
    'W615RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Public order and safety
    'W617RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Public order and safety: Fire
    'W618RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Public order and safety: Law courts
    'W616RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Public order and safety: Police
    'W619RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Public order and safety: Prisons
    'W635RC1A027NBEA', # Government consumption expenditures and gross investments: Federal: Recreation and culture
    'W575RC1A027NBEA', # Government consumption expenditures and gross investments: General public service
    'W576RC1A027NBEA', # Government consumption expenditures and gross investments: General public service: Executive and legislative
    'W578RC1A027NBEA', # Government consumption expenditures and gross investments: General public service: Other
    'W577RC1A027NBEA', # Government consumption expenditures and gross investments: General public service: Tax collection and financial management
    'W598RC1A027NBEA', # Government consumption expenditures and gross investments: Health
    'W597RC1A027NBEA', # Government consumption expenditures and gross investments: Housing and community services
    'W605RC1A027NBEA', # Government consumption expenditures and gross investments: Income security
    'W606RC1A027NBEA', # Government consumption expenditures and gross investments: Income security: Disability
    'W610RC1A027NBEA', # Government consumption expenditures and gross investments: Income security: Other
    'W607RC1A027NBEA', # Government consumption expenditures and gross investments: Income security: Retirement
    'W609RC1A027NBEA', # Government consumption expenditures and gross investments: Income security: Unemployment
    'W608RC1A027NBEA', # Government consumption expenditures and gross investments: Income security: Welfare and social services
    'W579RC1A027NBEA', # Government consumption expenditures and gross investments: Public order and safety
    'W581RC1A027NBEA', # Government consumption expenditures and gross investments: Public order and safety: Fire
    'W582RC1A027NBEA', # Government consumption expenditures and gross investments: Public order and safety: Law courts
    'W580RC1A027NBEA', # Government consumption expenditures and gross investments: Public order and safety: Police
    'W583RC1A027NBEA', # Government consumption expenditures and gross investments: Public order and safety: Prisons
    'W599RC1A027NBEA', # Government consumption expenditures and gross investments: Recreation and culture
    'W655RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Economic affairs
    'W665RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Economic affairs: Other economic affairs
    'W657RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Economic affairs: Other economic affairs: Agriculture
    'W658RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Economic affairs: Other economic affairs: Energy
    'W656RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Economic affairs: Other economic affairs: General economic and labor affairs
    'W659RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Economic affairs: Other economic affairs: Natural resources
    'W686RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Economic affairs: Other economic affairs: Other
    'W660RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Economic affairs: Transportation
    'W662RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Economic affairs: Transportation: Air
    'W661RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Economic affairs: Transportation: Highways
    'W664RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Economic affairs: Transportation: Transit and railroad
    'W663RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Economic affairs: Transportation: Water
    'W673RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Education
    'W674RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Education: Elementary and secondary
    'W675RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Education: Higher
    'W677RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Education: Libraries and other
    'W676RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Education: Libraries and other: Libraries
    'W683RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Education: Libraries and other: Other
    'W646RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: General public service
    'W647RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: General public service: Executive and legislative
    'W649RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: General public service: Other
    'W648RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: General public service: Tax collection and financial management
    'W671RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Health
    'W666RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Housing and community services
    'W670RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Housing and community services: Housing and other
    'W669RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Housing and community services: Sanitation
    'W668RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Housing and community services: Sewerage
    'W667RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Housing and community services: Water
    'W678RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Income security
    'W679RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Income security: Disability
    'W680RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Income security: Welfare and social services
    'W650RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Public order and safety
    'W652RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Public order and safety: Fire
    'W653RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Public order and safety: Law courts
    'W651RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Public order and safety: Police
    'W654RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Public order and safety: Prisons
    'W672RC1A027NBEA', # Government consumption expenditures and gross investments: State and local: Recreation and culture
    'G170051A027NBEA', # Government consumption expenditures: Economic affairs
    'G170091A027NBEA', # Government consumption expenditures: Education
    'G170151A027NBEA', # Government consumption expenditures: Federal: Economic affairs
    'G170191A027NBEA', # Government consumption expenditures: Federal: Education
    'G170121A027NBEA', # Government consumption expenditures: Federal: General public service
    'G170171A027NBEA', # Government consumption expenditures: Federal: Health
    'G170161A027NBEA', # Government consumption expenditures: Federal: Housing and community services
    'G170201A027NBEA', # Government consumption expenditures: Federal: Income security
    'A997RC1A027NBEA', # Government consumption expenditures: Federal: National defense
    'A542RC1A027NBEA', # Government consumption expenditures: Federal: Nondefense
    'G170141A027NBEA', # Government consumption expenditures: Federal: Public order and safety
    'G170181A027NBEA', # Government consumption expenditures: Federal: Recreation and culture
    'G170021A027NBEA', # Government consumption expenditures: General public service
    'W101RC1A027NBEA', # Government consumption expenditures: Gross output of general government
    'W104RC1A027NBEA', # Government consumption expenditures: Gross output of general government: Intermediate goods and services purchased
    'W105RC1A027NBEA', # Government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods
    'W106RC1A027NBEA', # Government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods
    'W107RC1A027NBEA', # Government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services
    'G170071A027NBEA', # Government consumption expenditures: Health
    'G170061A027NBEA', # Government consumption expenditures: Housing and community services
    'G170101A027NBEA', # Government consumption expenditures: Income security
    'W108RC1A027NBEA', # Government consumption expenditures: Own-account investment
    'G170041A027NBEA', # Government consumption expenditures: Public order and safety
    'G170081A027NBEA', # Government consumption expenditures: Recreation and culture
    'W109RC1A027NBEA', # Government consumption expenditures: Sales to other sectors
    'A991RC1A027NBEA', # Government consumption expenditures: State and local
    'G170241A027NBEA', # Government consumption expenditures: State and local: Economic affairs
    'G170281A027NBEA', # Government consumption expenditures: State and local: Education
    'G170221A027NBEA', # Government consumption expenditures: State and local: General public service
    'G170261A027NBEA', # Government consumption expenditures: State and local: Health
    'G170251A027NBEA', # Government consumption expenditures: State and local: Housing and community services
    'G170291A027NBEA', # Government consumption expenditures: State and local: Income security
    'G170231A027NBEA', # Government consumption expenditures: State and local: Public order and safety
    'G170271A027NBEA', # Government consumption expenditures: State and local: Recreation and culture
    'G171091A027NBEA', # Government gross investment: Economic affairs
    'G171131A027NBEA', # Government gross investment: Education
    'G171061A027NBEA', # Government gross investment: General public service
    'G171111A027NBEA', # Government gross investment: Health
    'G171101A027NBEA', # Government gross investment: Housing and community services
    'G171141A027NBEA', # Government gross investment: Income security
    'G171081A027NBEA', # Government gross investment: Public order and safety
    'G171121A027NBEA', # Government gross investment: Recreation and culture
    'W852RC1A027NBEA', # Local government consumption expenditures
    'Y654RC1A027NBEA', # Selected Government Current and Capital Expenditures: State and Local: Net Health: Gross expenditures
    'W138RC1A027NBEA', # State and Local government consumption expenditures: Gross output of general government
    'W140RC1A027NBEA', # State and Local government consumption expenditures: Gross output of general government: Intermediate goods and services purchased
    'B989RC1A027NBEA', # State and Local government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods
    'B337RC1A027NBEA', # State and Local government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods
    'A988RC1A027NBEA', # State and Local government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services
    'W144RC1A027NBEA', # State and Local government consumption expenditures: Own-account investment
    'W145RC1A027NBEA', # State and Local government consumption expenditures: Sales to other sectors
    'B1066C1A027NBEA', # State and Local government consumption expenditures: Sales to other sectors: Health and hospital charges
    'W146RC1A027NBEA', # State and Local government consumption expenditures: Sales to other sectors: Other sales
    'B1065C1A027NBEA', # State and Local government consumption expenditures: Sales to other sectors: Tuition and related educational charges
    'G171281A027NBEA', # State and local government gross investment: Economic affairs
    'G171321A027NBEA', # State and local government gross investment: Education
    'G171261A027NBEA', # State and local government gross investment: General public service
    'G171301A027NBEA', # State and local government gross investment: Health
    'G171291A027NBEA', # State and local government gross investment: Housing and community services
    'G171331A027NBEA', # State and local government gross investment: Income security
    'G171271A027NBEA', # State and local government gross investment: Public order and safety
    'G171311A027NBEA', # State and local government gross investment: Recreation and culture
    'W752RC1A027NBEA', # State government consumption expenditures
    ## Bil. of Chn. 2005 $ (NSA)
    'A872RX1A020NBEA', # Real government consumption expenditures and gross investment: Federal: Gross investment: Equipment and software (DISCONTINUED)
    'A873RX1A020NBEA', # Real government consumption expenditures and gross investment: Federal: National defense: Gross investment: Equipment and software (DISCONTINUED)
    'B880RX1A020NBEA', # Real government consumption expenditures and gross investment: Federal: Nondefense: Gross investment: Equipment and software (DISCONTINUED)
    'B881RX1A020NBEA', # Real government consumption expenditures and gross investment: State and local: Gross investment: Equipment and software (DISCONTINUED)
    ## Bil. of Chn. 2017 $ (NSA)
    'A955RX1A020NBEA', # Real Government Consumption Expenditures
    'W085RX1A020NBEA', # Real federal government consumption expenditures: Defense consumption expenditures: Gross output of general government
    'W087RX1A020NBEA', # Real federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased
    'A998RX1A020NBEA', # Real federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods
    'A725RX1A020NBEA', # Real federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods
    'A489RX1A020NBEA', # Real federal government consumption expenditures: Defense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services
    'W088RX1A020NBEA', # Real federal government consumption expenditures: Defense consumption expenditures: Own-account investment
    'W089RX1A020NBEA', # Real federal government consumption expenditures: Defense consumption expenditures: Sales to other sectors
    'W110RX1A020NBEA', # Real federal government consumption expenditures: Gross output of general government
    'W113RX1A020NBEA', # Real federal government consumption expenditures: Gross output of general government: Intermediate goods and services purchased
    'W114RX1A020NBEA', # Real federal government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods
    'W115RX1A020NBEA', # Real federal government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods
    'W116RX1A020NBEA', # Real federal government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services
    'W128RX1A020NBEA', # Real federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government
    'W131RX1A020NBEA', # Real federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Intermediate goods and services purchased
    'A543RX1A020NBEA', # Real federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods
    'A729RX1A020NBEA', # Real federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods
    'B826RX1A020NBEA', # Real federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Commodity Credit Corporation inventory change
    'B828RX1A020NBEA', # Real federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods: Other nondurable goods
    'A544RX1A020NBEA', # Real federal government consumption expenditures: Nondefense consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services
    'W136RX1A020NBEA', # Real federal government consumption expenditures: Nondefense consumption expenditures: Own-account investment
    'W137RX1A020NBEA', # Real federal government consumption expenditures: Nondefense consumption expenditures: Sales to other sectors
    'W117RX1A020NBEA', # Real federal government consumption expenditures: Own-account investment
    'W118RX1A020NBEA', # Real federal government consumption expenditures: Sales to other sectors
    'A957RX1A020NBEA', # Real government consumption expenditures and gross investment: Federal: Consumption expenditures
    'A787RX1A020NBEA', # Real government consumption expenditures and gross investment: Federal: Gross investment
    'A801RX1A020NBEA', # Real government consumption expenditures and gross investment: Federal: Gross investment: Structures
    'A824RX1A020NBEA', # Real government consumption expenditures and gross investment: Federal: National defense
    'A808RX1A020NBEA', # Real government consumption expenditures and gross investment: Federal: National defense: Gross investment: Structures
    'A825RX1A020NBEA', # Real government consumption expenditures and gross investment: Federal: Nondefense
    'A830RX1A020NBEA', # Real government consumption expenditures and gross investment: Federal: Nondefense: Gross investment: Structures
    'A979RX1A020NBEA', # Real government consumption expenditures and gross investment: Residual
    'A842RX1A020NBEA', # Real government consumption expenditures and gross investment: State and local: Gross investment: Structures
    'W584RX1A020NBEA', # Real government consumption expenditures and gross investments: Economic affairs
    'W596RX1A020NBEA', # Real government consumption expenditures and gross investments: Economic affairs: Other economic affairs
    'W595RX1A020NBEA', # Real government consumption expenditures and gross investments: Economic affairs: Space
    'W589RX1A020NBEA', # Real government consumption expenditures and gross investments: Economic affairs: Transportation
    'W600RX1A020NBEA', # Real government consumption expenditures and gross investments: Education
    'W620RX1A020NBEA', # Real government consumption expenditures and gross investments: Federal: Economic affairs
    'W632RX1A020NBEA', # Real government consumption expenditures and gross investments: Federal: Economic affairs: Other economic affairs
    'W631RX1A020NBEA', # Real government consumption expenditures and gross investments: Federal: Economic affairs: Space
    'W625RX1A020NBEA', # Real government consumption expenditures and gross investments: Federal: Economic affairs: Transportation
    'W636RX1A020NBEA', # Real government consumption expenditures and gross investments: Federal: Education
    'W611RX1A020NBEA', # Real government consumption expenditures and gross investments: Federal: General public service
    'W634RX1A020NBEA', # Real government consumption expenditures and gross investments: Federal: Health
    'W633RX1A020NBEA', # Real government consumption expenditures and gross investments: Federal: Housing and community services
    'W640RX1A020NBEA', # Real government consumption expenditures and gross investments: Federal: Income security
    'W615RX1A020NBEA', # Real government consumption expenditures and gross investments: Federal: Public order and safety
    'W635RX1A020NBEA', # Real government consumption expenditures and gross investments: Federal: Recreation and culture
    'W575RX1A020NBEA', # Real government consumption expenditures and gross investments: General public service
    'W598RX1A020NBEA', # Real government consumption expenditures and gross investments: Health
    'W597RX1A020NBEA', # Real government consumption expenditures and gross investments: Housing and community services
    'W605RX1A020NBEA', # Real government consumption expenditures and gross investments: Income security
    'W579RX1A020NBEA', # Real government consumption expenditures and gross investments: Public order and safety
    'W599RX1A020NBEA', # Real government consumption expenditures and gross investments: Recreation and culture
    'W687RX1A020NBEA', # Real government consumption expenditures and gross investments: Residual
    'W655RX1A020NBEA', # Real government consumption expenditures and gross investments: State and local: Economic affairs
    'W665RX1A020NBEA', # Real government consumption expenditures and gross investments: State and local: Economic affairs: Other economic affairs
    'W660RX1A020NBEA', # Real government consumption expenditures and gross investments: State and local: Economic affairs: Transportation
    'W673RX1A020NBEA', # Real government consumption expenditures and gross investments: State and local: Education
    'W674RX1A020NBEA', # Real government consumption expenditures and gross investments: State and local: Education: Elementary and secondary
    'W675RX1A020NBEA', # Real government consumption expenditures and gross investments: State and local: Education: Higher
    'W677RX1A020NBEA', # Real government consumption expenditures and gross investments: State and local: Education: Libraries and other
    'W646RX1A020NBEA', # Real government consumption expenditures and gross investments: State and local: General public service
    'W671RX1A020NBEA', # Real government consumption expenditures and gross investments: State and local: Health
    'W666RX1A020NBEA', # Real government consumption expenditures and gross investments: State and local: Housing and community services
    'W678RX1A020NBEA', # Real government consumption expenditures and gross investments: State and local: Income security
    'W650RX1A020NBEA', # Real government consumption expenditures and gross investments: State and local: Public order and safety
    'W672RX1A020NBEA', # Real government consumption expenditures and gross investments: State and local: Recreation and culture
    'A997RX1A020NBEA', # Real government consumption expenditures: Federal: National defense
    'A542RX1A020NBEA', # Real government consumption expenditures: Federal: Nondefense
    'W101RX1A020NBEA', # Real government consumption expenditures: Gross output of general government
    'W104RX1A020NBEA', # Real government consumption expenditures: Gross output of general government: Intermediate goods and services purchased
    'W105RX1A020NBEA', # Real government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods
    'W106RX1A020NBEA', # Real government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods
    'W107RX1A020NBEA', # Real government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services
    'W108RX1A020NBEA', # Real government consumption expenditures: Own-account investment
    'W100RX1A020NBEA', # Real government consumption expenditures: Residual
    'W109RX1A020NBEA', # Real government consumption expenditures: Sales to other sectors
    'A991RX1A020NBEA', # Real government consumption expenditures: State and local
    'A788RX1A020NBEA', # Real government gross investment: Federal: National defense
    'A798RX1A020NBEA', # Real government gross investment: Federal: Nondefense
    'A799RX1A020NBEA', # Real government gross investment: State and local
    'W138RX1A020NBEA', # Real state and local government consumption expenditures: Gross output of general government
    'W140RX1A020NBEA', # Real state and local government consumption expenditures: Gross output of general government: Intermediate goods and services purchased
    'B989RX1A020NBEA', # Real state and local government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Durable goods
    'B337RX1A020NBEA', # Real state and local government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Nondurable goods
    'A988RX1A020NBEA', # Real state and local government consumption expenditures: Gross output of general government: Intermediate goods and services purchased: Services
    'W144RX1A020NBEA', # Real state and local government consumption expenditures: Own-account investment
    'W145RX1A020NBEA', # Real state and local government consumption expenditures: Sales to other sectors
    'B1066X1A020NBEA', # Real state and local government consumption expenditures: Sales to other sectors: Health and hospital charges
    'W146RX1A020NBEA', # Real state and local government consumption expenditures: Sales to other sectors: Other sales
    'B1065X1A020NBEA', # Real state and local government consumption expenditures: Sales to other sectors: Tuition and related educational charges
    ## Index 2017=100 (NSA)
    'W584RG3A086NBEA', # Government consumption expenditures and gross investment: Economic affairs
    'W596RG3A086NBEA', # Government consumption expenditures and gross investment: Economic affairs: Other economic affairs
    'W595RG3A086NBEA', # Government consumption expenditures and gross investment: Economic affairs: Space
    'W589RG3A086NBEA', # Government consumption expenditures and gross investment: Economic affairs: Transportation
    'W600RG3A086NBEA', # Government consumption expenditures and gross investment: Education
    'W620RG3A086NBEA', # Government consumption expenditures and gross investment: Federal: Economic affairs
    'W632RG3A086NBEA', # Government consumption expenditures and gross investment: Federal: Economic affairs: Other economic affairs
    'W631RG3A086NBEA', # Government consumption expenditures and gross investment: Federal: Economic affairs: Space
    'W625RG3A086NBEA', # Government consumption expenditures and gross investment: Federal: Economic affairs: Transportation
    'W636RG3A086NBEA', # Government consumption expenditures and gross investment: Federal: Education
    'W611RG3A086NBEA', # Government consumption expenditures and gross investment: Federal: General public service
    'W634RG3A086NBEA', # Government consumption expenditures and gross investment: Federal: Health
    'W633RG3A086NBEA', # Government consumption expenditures and gross investment: Federal: Housing and community services
    'W640RG3A086NBEA', # Government consumption expenditures and gross investment: Federal: Income security
    'W615RG3A086NBEA', # Government consumption expenditures and gross investment: Federal: Public order and safety
    'W635RG3A086NBEA', # Government consumption expenditures and gross investment: Federal: Recreation and culture
    'W575RG3A086NBEA', # Government consumption expenditures and gross investment: General public service
    'W598RG3A086NBEA', # Government consumption expenditures and gross investment: Health
    'W597RG3A086NBEA', # Government consumption expenditures and gross investment: Housing and community services
    'W605RG3A086NBEA', # Government consumption expenditures and gross investment: Income security
    'W579RG3A086NBEA', # Government consumption expenditures and gross investment: Public order and safety
    'W599RG3A086NBEA', # Government consumption expenditures and gross investment: Recreation and culture
    'W655RG3A086NBEA', # Government consumption expenditures and gross investment: State and local: Economic affairs
    'W665RG3A086NBEA', # Government consumption expenditures and gross investment: State and local: Economic affairs: Other economic affairs
    'W660RG3A086NBEA', # Government consumption expenditures and gross investment: State and local: Economic affairs: Transportation
    'W673RG3A086NBEA', # Government consumption expenditures and gross investment: State and local: Education
    'W674RG3A086NBEA', # Government consumption expenditures and gross investment: State and local: Education: Elementary and secondary
    'W675RG3A086NBEA', # Government consumption expenditures and gross investment: State and local: Education: Higher
    'W677RG3A086NBEA', # Government consumption expenditures and gross investment: State and local: Education: Libraries and other
    'W646RG3A086NBEA', # Government consumption expenditures and gross investment: State and local: General public service
    'W671RG3A086NBEA', # Government consumption expenditures and gross investment: State and local: Health
    'W666RG3A086NBEA', # Government consumption expenditures and gross investment: State and local: Housing and community services
    'W678RG3A086NBEA', # Government consumption expenditures and gross investment: State and local: Income security
    'W650RG3A086NBEA', # Government consumption expenditures and gross investment: State and local: Public order and safety
    'W672RG3A086NBEA', # Government consumption expenditures and gross investment: State and local: Recreation and culture
    ## Percentage Points at Annual Rate (NSA)
    'A955RZ2A224NBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Consumption expenditures
    'A823RZ2A224NBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal
    'A957RZ2A224NBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: Consumption expenditures
    'A787RZ2A224NBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: Gross investment
    'A872RZ2A224NBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: Gross investment: Equipment and software (DISCONTINUED)
    'A801RZ2A224NBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: Gross investment: Structures
    'A824RZ2A224NBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: National defense
    'A997RZ2A224NBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: National defense: Consumption expenditures
    'A788RZ2A224NBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: National defense: Gross investment
    'A873RZ2A224NBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: National defense: Gross investment: Equipment and software (DISCONTINUED)
    'A808RZ2A224NBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: National defense: Gross investment: Structures
    'A825RZ2A224NBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: Nondefense
    'A542RZ2A224NBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: Nondefense: Consumption expenditures
    'A798RZ2A224NBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: Nondefense: Gross investment
    'B880RZ2A224NBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: Nondefense: Gross investment: Equipment and software (DISCONTINUED)
    'A830RZ2A224NBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Federal: Nondefense: Gross investment: Structures
    'A782RZ2A224NBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Gross investment
    'A871RZ2A224NBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Gross investment: Equipment and software (DISCONTINUED)
    'A760RZ2A224NBEA', # Contribution to percent change in real government consumption expenditures and gross investment: Gross investment: Structures
    'A829RZ2A224NBEA', # Contribution to percent change in real government consumption expenditures and gross investment: State and local
    'A991RZ2A224NBEA', # Contribution to percent change in real government consumption expenditures and gross investment: State and local: Consumption expenditures
    'A799RZ2A224NBEA', # Contribution to percent change in real government consumption expenditures and gross investment: State and local: Gross investment
    'B881RZ2A224NBEA', # Contribution to percent change in real government consumption expenditures and gross investment: State and local: Gross investment: Equipment and software (DISCONTINUED)
    'A842RZ2A224NBEA', # Contribution to percent change in real government consumption expenditures and gross investment: State and local: Gross investment: Structures
    'A822RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Government consumption expenditures and gross investment
    'A823RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Government consumption expenditures and gross investment: Federal
    'A824RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Government consumption expenditures and gross investment: Federal: National defense
    'A997RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Government consumption expenditures and gross investment: Federal: National defense: Consumption expenditures
    'A788RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Government consumption expenditures and gross investment: Federal: National defense: Gross investment
    'A825RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Government consumption expenditures and gross investment: Federal: Nondefense
    'A542RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Government consumption expenditures and gross investment: Federal: Nondefense: Consumption expenditures
    'A798RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Government consumption expenditures and gross investment: Federal: Nondefense: Gross investment
    'A829RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Government consumption expenditures and gross investment: State and local
    'A991RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Government consumption expenditures and gross investment: State and local: Consumption expenditures
    'A799RS2A224NBEA', # Contributions to percent change in gross domestic purchases: Government consumption expenditures and gross investment: State and local: Gross investment
    'W584RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: Economic affairs
    'W596RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: Economic affairs: Other economic affairs
    'W595RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: Economic affairs: Space
    'W589RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: Economic affairs: Transportation
    'W600RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: Education
    'W620RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: Federal: Economic affairs
    'W632RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: Federal: Economic affairs: Other economic affairs
    'W631RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: Federal: Economic affairs: Space
    'W625RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: Federal: Economic affairs: Transportation
    'W636RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: Federal: Education
    'W611RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: Federal: General public service
    'W634RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: Federal: Health
    'W633RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: Federal: Housing and community services
    'W640RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: Federal: Income security
    'W615RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: Federal: Public order and safety
    'W635RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: Federal: Recreation and culture
    'W575RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: General public service
    'W598RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: Health
    'W597RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: Housing and community services
    'W605RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: Income security
    'W579RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: Public order and safety
    'W599RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: Recreation and culture
    'W655RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: State and local: Economic affairs
    'W665RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: State and local: Economic affairs: Other economic affairs
    'W660RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: State and local: Economic affairs: Transportation
    'W673RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: State and local: Education
    'W674RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: State and local: Education: Elementary and secondary
    'W675RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: State and local: Education: Higher
    'W677RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: State and local: Education: Libraries and other
    'W646RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: State and local: General public service
    'W671RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: State and local: Health
    'W666RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: State and local: Housing and community services
    'W678RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: State and local: Income security
    'W650RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: State and local: Public order and safety
    'W672RZ2A224NBEA', # Contributions to percent change in real government consumption expenditures and gross investment: State and local: Recreation and culture
    'A822RY2A224NBEA', # Contributions to percent change in real gross domestic product: Government consumption expenditures and gross investment
    'A823RY2A224NBEA', # Contributions to percent change in real gross domestic product: Government consumption expenditures and gross investment: Federal
    'A824RY2A224NBEA', # Contributions to percent change in real gross domestic product: Government consumption expenditures and gross investment: Federal: National defense
    'A825RY2A224NBEA', # Contributions to percent change in real gross domestic product: Government consumption expenditures and gross investment: Federal: Nondefense
    'A829RY2A224NBEA', # Contributions to percent change in real gross domestic product: Government consumption expenditures and gross investment: State and local
    'A997RY2A224NBEA', # Contributions to percent change in real gross domestic product: Government consumption expenditures: Federal: National defense
    'A542RY2A224NBEA', # Contributions to percent change in real gross domestic product: Government consumption expenditures: Federal: Nondefense
    'A991RY2A224NBEA', # Contributions to percent change in real gross domestic product: Government consumption expenditures: State and local
    'A788RY2A224NBEA', # Contributions to percent change in real gross domestic product: Government gross investment: Federal: National defense
    'A798RY2A224NBEA', # Contributions to percent change in real gross domestic product: Government gross investment: Federal: Nondefense
    'A799RY2A224NBEA', # Contributions to percent change in real gross domestic product: Government gross investment: State and local

    # Gov't Receipts, Expenditures & Investment > Gov't Current Expenditures (200)
    ## % Chg. from Preceding Period (NSA)
    'W085RL1A225NBEA', # Real Federal Government Consumption Expenditures: Defense Consumption Expenditures: Gross Output of General Government
    'W087RL1A225NBEA', # Real Federal Government Consumption Expenditures: Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased
    'A998RL1A225NBEA', # Real Federal Government Consumption Expenditures: Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Durable Goods
    'A725RL1A225NBEA', # Real Federal Government Consumption Expenditures: Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Nondurable Goods
    'A489RL1A225NBEA', # Real Federal Government Consumption Expenditures: Defense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Services
    'W086RL1A225NBEA', # Real Federal Government Consumption Expenditures: Defense Consumption Expenditures: Gross Output of General Government: Value Added
    'B237RL1A225NBEA', # Real Federal Government Consumption Expenditures: Defense Consumption Expenditures: Gross Output of General Government: Value Added: Compensation of General Government Employees
    'B432RL1A225NBEA', # Real Federal Government Consumption Expenditures: Defense Consumption Expenditures: Gross Output of General Government: Value Added: Consumption of General Government Fixed Capital
    'W088RL1A225NBEA', # Real Federal Government Consumption Expenditures: Defense Consumption Expenditures: Less: Own-account Investment
    'W089RL1A225NBEA', # Real Federal Government Consumption Expenditures: Defense Consumption Expenditures: Less: Sales to Other Sectors
    'W110RL1A225NBEA', # Real Federal Government Consumption Expenditures: Gross Output of General Government
    'W113RL1A225NBEA', # Real Federal Government Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased
    'W114RL1A225NBEA', # Real Federal Government Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Durable Goods
    'W115RL1A225NBEA', # Real Federal Government Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Nondurable Goods
    'W116RL1A225NBEA', # Real Federal Government Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Services
    'W111RL1A225NBEA', # Real Federal Government Consumption Expenditures: Gross Output of General Government: Value Added
    'B568RL1A225NBEA', # Real Federal Government Consumption Expenditures: Gross Output of General Government: Value Added: Compensation of General Government Employees
    'B995RL1A225NBEA', # Real Federal Government Consumption Expenditures: Gross Output of General Government: Value Added: Consumption of General Government Fixed Capital
    'W128RL1A225NBEA', # Real Federal Government Consumption Expenditures: Nondefense Consumption Expenditures: Gross Output of General Government
    'W131RL1A225NBEA', # Real Federal Government Consumption Expenditures: Nondefense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased
    'A543RL1A225NBEA', # Real Federal Government Consumption Expenditures: Nondefense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Durable Goods
    'B828RL1A225NBEA', # Real Federal Government Consumption Expenditures: Nondefense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Nondurable Goods: Other Nondurable Goods
    'A544RL1A225NBEA', # Real Federal Government Consumption Expenditures: Nondefense Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Services
    'W129RL1A225NBEA', # Real Federal Government Consumption Expenditures: Nondefense Consumption Expenditures: Gross Output of General Government: Value Added
    'W130RL1A225NBEA', # Real Federal Government Consumption Expenditures: Nondefense Consumption Expenditures: Gross Output of General Government: Value Added: Compensation of General Government Employees
    'B546RL1A225NBEA', # Real Federal Government Consumption Expenditures: Nondefense Consumption Expenditures: Gross Output of General Government: Value Added: Consumption of General Government Fixed Capital
    'W136RL1A225NBEA', # Real Federal Government Consumption Expenditures: Nondefense Consumption Expenditures: Own-account Investment
    'W137RL1A225NBEA', # Real Federal Government Consumption Expenditures: Nondefense Consumption Expenditures: Sales to Other Sectors
    'W117RL1A225NBEA', # Real Federal Government Consumption Expenditures: Own-account Investment
    'W118RL1A225NBEA', # Real Federal Government Consumption Expenditures: Sales to Other Sectors
    'A955RL1A225NBEA', # Real Government Consumption Expenditures
    'A957RL1A225NBEA', # Real Government Consumption Expenditures: Federal: Consumption Expenditures
    'A997RL1A225NBEA', # Real Government Consumption Expenditures: Federal: National Defense: Consumption Expenditures
    'W108RL1A225NBEA', # Real Government Consumption Expenditures: Own-account Investment
    'W109RL1A225NBEA', # Real Government Consumption Expenditures: Sales to Other Sectors
    'A991RL1A225NBEA', # Real Government Consumption Expenditures: State and Local: Consumption Expenditures
    'W138RL1A225NBEA', # Real State and Local Government Consumption Expenditures: Gross Output of General Government
    'W140RL1A225NBEA', # Real State and Local Government Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased
    'B989RL1A225NBEA', # Real State and Local Government Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Durable Goods
    'B337RL1A225NBEA', # Real State and Local Government Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Nondurable Goods
    'A988RL1A225NBEA', # Real State and Local Government Consumption Expenditures: Gross Output of General Government: Intermediate Goods and Services Purchased: Services
    'W139RL1A225NBEA', # Real State and Local Government Consumption Expenditures: Gross Output of General Government: Value Added
    'B251RL1A225NBEA', # Real State and Local Government Consumption Expenditures: Gross Output of General Government: Value Added: Compensation of General Government Employees
    'B986RL1A225NBEA', # Real State and Local Government Consumption Expenditures: Gross Output of General Government: Value Added: Consumption of General Government Fixed Capital
    'W144RL1A225NBEA', # Real State and Local Government Consumption Expenditures: Own-account Investment
    'W145RL1A225NBEA', # Real State and Local Government Consumption Expenditures: Sales to Other Sectors
    'B1066L1A225NBEA', # Real State and Local Government Consumption Expenditures: Sales to Other Sectors: Health and Hospital Charges
    'W146RL1A225NBEA', # Real State and Local Government Consumption Expenditures: Sales to Other Sectors: Other Sales
    'B1065L1A225NBEA', # Real State and Local Government Consumption Expenditures: Sales to Other Sectors: Tuition and Related Educational Charges
    ## Bil. of $ (NSA)
    'M318491A027NBEA', # Federal government current expenditures, NIPAs
    'L318441A027NBEA', # Federal government current expenditures, NIPAs (DISCONTINUED)
    'B092RC1A027NBEA', # Federal government current expenditures: Interest payments: to persons and business
    'B096RC1A027NBEA', # Federal government current expenditures: Subsidies
    'Y652RC1A027NBEA', # Government Current Expenditures: State and Local: Net Health: Gross expenditures
    'W022RC1A027NBEA', # Government current expenditures
    'G160131A027NBEA', # Government current expenditures: Economic affairs
    'W690RC1A027NBEA', # Government current expenditures: Economic affairs: Other economic affairs
    'G160151A027NBEA', # Government current expenditures: Economic affairs: Other economic affairs: Agriculture
    'G160161A027NBEA', # Government current expenditures: Economic affairs: Other economic affairs: Energy
    'G160141A027NBEA', # Government current expenditures: Economic affairs: Other economic affairs: General economic and labor affairs
    'G160171A027NBEA', # Government current expenditures: Economic affairs: Other economic affairs: Natural resources
    'G160251A027NBEA', # Government current expenditures: Economic affairs: Other economic affairs: Other
    'G160231A027NBEA', # Government current expenditures: Economic affairs: Other economic affairs: Postal service
    'G160241A027NBEA', # Government current expenditures: Economic affairs: Space
    'G160181A027NBEA', # Government current expenditures: Economic affairs: Transportation
    'G160201A027NBEA', # Government current expenditures: Economic affairs: Transportation: Air
    'G160191A027NBEA', # Government current expenditures: Economic affairs: Transportation: Highways
    'G160221A027NBEA', # Government current expenditures: Economic affairs: Transportation: Transit and railroad
    'G160211A027NBEA', # Government current expenditures: Economic affairs: Transportation: Water
    'G160291A027NBEA', # Government current expenditures: Education
    'G160301A027NBEA', # Government current expenditures: Education: Elementary and secondary
    'G160311A027NBEA', # Government current expenditures: Education: Higher
    'W691RC1A027NBEA', # Government current expenditures: Education: Libraries and other
    'G160321A027NBEA', # Government current expenditures: Education: Libraries and other: Libraries
    'G160331A027NBEA', # Government current expenditures: Education: Libraries and other: Other
    'G160521A027NBEA', # Government current expenditures: Federal: Economic affairs
    'W692RC1A027NBEA', # Government current expenditures: Federal: Economic affairs: Other economic affairs
    'G160541A027NBEA', # Government current expenditures: Federal: Economic affairs: Other economic affairs: Agriculture
    'G160551A027NBEA', # Government current expenditures: Federal: Economic affairs: Other economic affairs: Energy
    'G160531A027NBEA', # Government current expenditures: Federal: Economic affairs: Other economic affairs: General economic and labor affairs
    'G160561A027NBEA', # Government current expenditures: Federal: Economic affairs: Other economic affairs: Natural resources
    'G160621A027NBEA', # Government current expenditures: Federal: Economic affairs: Other economic affairs: Postal service
    'G160631A027NBEA', # Government current expenditures: Federal: Economic affairs: Space
    'G160571A027NBEA', # Government current expenditures: Federal: Economic affairs: Transportation
    'G160591A027NBEA', # Government current expenditures: Federal: Economic affairs: Transportation: Air
    'G160581A027NBEA', # Government current expenditures: Federal: Economic affairs: Transportation: Highways
    'G160611A027NBEA', # Government current expenditures: Federal: Economic affairs: Transportation: Transit and railroad
    'G160601A027NBEA', # Government current expenditures: Federal: Economic affairs: Transportation: Water
    'G160681A027NBEA', # Government current expenditures: Federal: Education
    'G160691A027NBEA', # Government current expenditures: Federal: Education: Elementary and secondary
    'G160701A027NBEA', # Government current expenditures: Federal: Education: Higher
    'G160711A027NBEA', # Government current expenditures: Federal: Education: Other
    'G160411A027NBEA', # Government current expenditures: Federal: General public service
    'G160421A027NBEA', # Government current expenditures: Federal: General public service: Executive and legislative
    'G160441A027NBEA', # Government current expenditures: Federal: General public service: Interest payments
    'G160451A027NBEA', # Government current expenditures: Federal: General public service: Other
    'G160431A027NBEA', # Government current expenditures: Federal: General public service: Tax collection and financial management
    'G160661A027NBEA', # Government current expenditures: Federal: Health
    'G160651A027NBEA', # Government current expenditures: Federal: Housing and community services
    'G160721A027NBEA', # Government current expenditures: Federal: Income security
    'G160731A027NBEA', # Government current expenditures: Federal: Income security: Disability
    'G160771A027NBEA', # Government current expenditures: Federal: Income security: Other
    'G160741A027NBEA', # Government current expenditures: Federal: Income security: Retirement
    'G160761A027NBEA', # Government current expenditures: Federal: Income security: Unemployment
    'G160751A027NBEA', # Government current expenditures: Federal: Income security: Welfare and social services
    'G160461A027NBEA', # Government current expenditures: Federal: National defense
    'G160471A027NBEA', # Government current expenditures: Federal: Public order and safety
    'G160491A027NBEA', # Government current expenditures: Federal: Public order and safety: Fire
    'G160501A027NBEA', # Government current expenditures: Federal: Public order and safety: Law courts
    'G160481A027NBEA', # Government current expenditures: Federal: Public order and safety: Police
    'G160511A027NBEA', # Government current expenditures: Federal: Public order and safety: Prisons
    'G160671A027NBEA', # Government current expenditures: Federal: Recreation and culture
    'G160021A027NBEA', # Government current expenditures: General public service
    'G160031A027NBEA', # Government current expenditures: General public service: Executive and legislative
    'G160051A027NBEA', # Government current expenditures: General public service: Interest payments
    'G160061A027NBEA', # Government current expenditures: General public service: Other
    'G160041A027NBEA', # Government current expenditures: General public service: Tax collection and financial management
    'G160271A027NBEA', # Government current expenditures: Health
    'G160261A027NBEA', # Government current expenditures: Housing and community services
    'G160341A027NBEA', # Government current expenditures: Income security
    'G160351A027NBEA', # Government current expenditures: Income security: Disability
    'G160391A027NBEA', # Government current expenditures: Income security: Other
    'G160361A027NBEA', # Government current expenditures: Income security: Retirement
    'G160381A027NBEA', # Government current expenditures: Income security: Unemployment
    'G160371A027NBEA', # Government current expenditures: Income security: Welfare and social services
    'A180RC1A027NBEA', # Government current expenditures: Interest payments
    'A204RC1A027NBEA', # Government current expenditures: Interest payments: to persons and business
    'G160071A027NBEA', # Government current expenditures: National defense
    'G160081A027NBEA', # Government current expenditures: Public order and safety
    'G160101A027NBEA', # Government current expenditures: Public order and safety: Fire
    'G160111A027NBEA', # Government current expenditures: Public order and safety: Law courts
    'G160091A027NBEA', # Government current expenditures: Public order and safety: Police
    'G160121A027NBEA', # Government current expenditures: Public order and safety: Prisons
    'G160281A027NBEA', # Government current expenditures: Recreation and culture
    'G160891A027NBEA', # Government current expenditures: State and local: Economic affairs
    'W693RC1A027NBEA', # Government current expenditures: State and local: Economic affairs: Other economic affairs
    'G160911A027NBEA', # Government current expenditures: State and local: Economic affairs: Other economic affairs: Agriculture
    'G160921A027NBEA', # Government current expenditures: State and local: Economic affairs: Other economic affairs: Energy
    'G160901A027NBEA', # Government current expenditures: State and local: Economic affairs: Other economic affairs: General economic and labor affairs
    'G160931A027NBEA', # Government current expenditures: State and local: Economic affairs: Other economic affairs: Natural resources
    'G160991A027NBEA', # Government current expenditures: State and local: Economic affairs: Other economic affairs: Other
    'G160941A027NBEA', # Government current expenditures: State and local: Economic affairs: Transportation
    'G160951A027NBEA', # Government current expenditures: State and local: Economic affairs: Transportation: Highways
    'G160981A027NBEA', # Government current expenditures: State and local: Economic affairs: Transportation: Transit and railroad
    'G161071A027NBEA', # Government current expenditures: State and local: Education
    'G161081A027NBEA', # Government current expenditures: State and local: Education: Elementary and secondary
    'G161091A027NBEA', # Government current expenditures: State and local: Education: Higher
    'W694RC1A027NBEA', # Government current expenditures: State and local: Education: Libraries and other
    'G161101A027NBEA', # Government current expenditures: State and local: Education: Libraries and other: Libraries
    'G161111A027NBEA', # Government current expenditures: State and local: Education: Libraries and other: Other
    'G160791A027NBEA', # Government current expenditures: State and local: General public service
    'G160801A027NBEA', # Government current expenditures: State and local: General public service: Executive and legislative
    'G160821A027NBEA', # Government current expenditures: State and local: General public service: Interest payments
    'G160831A027NBEA', # Government current expenditures: State and local: General public service: Other
    'G160811A027NBEA', # Government current expenditures: State and local: General public service: Tax collection and financial management
    'G161051A027NBEA', # Government current expenditures: State and local: Health
    'G161001A027NBEA', # Government current expenditures: State and local: Housing and community services
    'G161121A027NBEA', # Government current expenditures: State and local: Income security
    'G161131A027NBEA', # Government current expenditures: State and local: Income security: Disability
    'G161141A027NBEA', # Government current expenditures: State and local: Income security: Welfare and social services
    'G160841A027NBEA', # Government current expenditures: State and local: Public order and safety
    'G160861A027NBEA', # Government current expenditures: State and local: Public order and safety: Fire
    'G160871A027NBEA', # Government current expenditures: State and local: Public order and safety: Law courts
    'G160851A027NBEA', # Government current expenditures: State and local: Public order and safety: Police
    'G160881A027NBEA', # Government current expenditures: State and local: Public order and safety: Prisons
    'G161061A027NBEA', # Government current expenditures: State and local: Recreation and culture
    'W851RC1A027NBEA', # Local government current expenditures
    'W853RC1A027NBEA', # Local government current expenditures: Current transfer payments
    'W854RC1A027NBEA', # Local government current expenditures: Current transfer payments: Government social benefit payments to persons
    'W855RC1A027NBEA', # Local government current expenditures: Current transfer payments: Grants-in-aid to state governments
    'W856RC1A027NBEA', # Local government current expenditures: Interest payments
    'W857RC1A027NBEA', # Local government current expenditures: Subsidies
    'LA0000171A027NBEA', # State and Local Government Current Expenditures: Current transfer payments
    'LA0000151A027NBEA', # State and Local Government Current Expenditures: Current transfer payments: Current transfer payments to the rest of the world
    'Y706RC1A027NBEA', # State and Local Government Current Expenditures: Interest payments: to the rest of the world
    'L319231A027NBEA', # State and Local government current expenditures: Census total expenditures
    'L319241A027NBEA', # State and Local government current expenditures: Coverage differences (NIPA vs. Census)
    'W726RC1A027NBEA', # State and Local government current expenditures: Coverage differences: Imputed banking and insurance services (NIPA vs. Census)
    'W725RC1A027NBEA', # State and Local government current expenditures: Coverage differences: Indian tribal government expenditures (NIPA vs. Census)
    'L319301A027NBEA', # State and Local government current expenditures: Coverage differences: Net investment (NIPA vs. Census)
    'L319421A027NBEA', # State and Local government current expenditures: Coverage differences: Net investment (NIPA vs. Census) (DISCONTINUED)
    'L319331A027NBEA', # State and Local government current expenditures: Coverage differences: Other (NIPA vs. Census)
    'L319321A027NBEA', # State and Local government current expenditures: Coverage differences: Purchases of land (NIPA vs. Census)
    'L319311A027NBEA', # State and Local government current expenditures: Coverage differences: Services provided without payment by domestic securities brokers (NIPA vs. Census)
    'L319251A027NBEA', # State and Local government current expenditures: Coverage differences: State and local employee retirement plan transactions (NIPA vs. Census)
    'L319281A027NBEA', # State and Local government current expenditures: Coverage differences: State and local employee retirement plan transactions: Administrative expenses (NIPA vs. Census)
    'L319271A027NBEA', # State and Local government current expenditures: Coverage differences: State and local employee retirement plan transactions: Benefits paid (NIPA vs. Census)
    'L319291A027NBEA', # State and Local government current expenditures: Coverage differences: Unemployment insurance fund benefits paid (NIPA vs. Census)
    'L319341A027NBEA', # State and Local government current expenditures: Netting and grossing differences
    'W727RC1A027NBEA', # State and Local government current expenditures: Netting and grossing differences: Current expenditures of government enterprises (DISCONTINUED)
    'L319361A027NBEA', # State and Local government current expenditures: Netting and grossing differences: Government sales included in Census total revenue (DISCONTINUED)
    'W728RC1A027NBEA', # State and Local government current expenditures: Netting and grossing differences: Insurance claims included in Census total revenue (DISCONTINUED)
    'L319391A027NBEA', # State and Local government current expenditures: Timing and other differences
    'L319401A027NBEA', # State and local government current expenditures, NIPAs
    'W751RC1A027NBEA', # State government current expenditures
    'W753RC1A027NBEA', # State government current expenditures: Current transfer payments
    'W754RC1A027NBEA', # State government current expenditures: Current transfer payments: Government social benefit payments to persons
    'W755RC1A027NBEA', # State government current expenditures: Current transfer payments: Grants-in-aid to local governments
    'W756RC1A027NBEA', # State government current expenditures: Interest payments
    'W757RC1A027NBEA', # State government current expenditures: Subsidies

    # Gov't Receipts, Expenditures & Investment > Gov't Current Transfer Receipts (21)
    ## Bil. of $ (NSA)
    'LA0000121A027NBEA', # Federal Government Current Receipts: Contributions for government social insurance: From persons
    'W798RC1A027NBEA', # Federal Government Social Insurance Funds Current Receipts: Other
    'W011RC1A027NBEA', # Federal government current transfer receipts
    'W012RC1A027NBEA', # Federal government current transfer receipts: from business
    'B233RC1A027NBEA', # Federal government current transfer receipts: from persons
    'Y703RC1A027NBEA', # Government Current Receipts: Income receipts on assets: Interest and miscellaneous receipts: Interest receipts
    'Y704RC1A027NBEA', # Government Current Receipts: Income receipts on assets: Interest and miscellaneous receipts: Rents and royalties
    'LA0000141A027NBEA', # Government Current Transfer Receipts: From the rest of the world
    'LA0000281A027NBEA', # Government Current Transfer Receipts: From the rest of the world: Federal
    'LA0000161A027NBEA', # Government Current Transfer Receipts: From the rest of the world: State and local
    'W060RC1A027NBEA', # Government current transfer receipts
    'B1041C1A027NBEA', # Government current transfer receipts: from business (net): Federal: Deposit insurance premiums
    'B1042C1A027NBEA', # Government current transfer receipts: from business (net): Federal: Other
    'S230561A027NBEA', # Government current transfer receipts: from business (net): State and local (net): Fines
    'W098RC1A027NBEA', # Government current transfer receipts: from business (net): State and local (net): Net insurance settlements
    'S230571A027NBEA', # Government current transfer receipts: from business (net): State and local (net): Other
    'S210661A027NBEA', # Government current transfer receipts: from persons: State and local: Fines
    'S210671A027NBEA', # Government current transfer receipts: from persons: State and local: Other
    'W075RC1A027NBEA', # State and local government current transfer receipts
    'W076RC1A027NBEA', # State and local government current transfer receipts: from business (net)
    'B246RC1A027NBEA', # State and local government current transfer receipts: from persons

    # Gov't Receipts, Expenditures & Investment > Gov't Fixed Investment (127)
    ## Bil. of $ (NSA)
    'A872RC1A027NBEA', # Gross government fixed investment: Equipment and software: Federal (DISCONTINUED)
    'A873RC1A027NBEA', # Gross government fixed investment: Equipment and software: Federal: National defense (DISCONTINUED)
    'B874RC1A027NBEA', # Gross government fixed investment: Equipment and software: Federal: National defense: Aircraft
    'B878RC1A027NBEA', # Gross government fixed investment: Equipment and software: Federal: National defense: Electronics and software (DISCONTINUED)
    'B875RC1A027NBEA', # Gross government fixed investment: Equipment and software: Federal: National defense: Missiles
    'B879RC1A027NBEA', # Gross government fixed investment: Equipment and software: Federal: National defense: Other equipment
    'B876RC1A027NBEA', # Gross government fixed investment: Equipment and software: Federal: National defense: Ships
    'B877RC1A027NBEA', # Gross government fixed investment: Equipment and software: Federal: National defense: Vehicles
    'B880RC1A027NBEA', # Gross government fixed investment: Equipment and software: Federal: Nondefense (DISCONTINUED)
    'B881RC1A027NBEA', # Gross government fixed investment: Equipment and software: State and local (DISCONTINUED)
    'A788RC1A027NBEA', # Gross government fixed investment: Federal: National defense
    'B819RC1A027NBEA', # Gross government fixed investment: Federal: National defense: Net purchases of used structures
    'A798RC1A027NBEA', # Gross government fixed investment: Federal: Nondefense
    'B841RC1A027NBEA', # Gross government fixed investment: Federal: Nondefense: Net purchases of used structures
    'B870RC1A027NBEA', # Gross government fixed investment: State and local: Net purchases of used structures
    'A801RC1A027NBEA', # Gross government fixed investment: Structures: Federal
    'A808RC1A027NBEA', # Gross government fixed investment: Structures: Federal: National defense
    'A814RC1A027NBEA', # Gross government fixed investment: Structures: Federal: National defense: New
    'A815RC1A027NBEA', # Gross government fixed investment: Structures: Federal: National defense: New: Buildings
    'B817RC1A027NBEA', # Gross government fixed investment: Structures: Federal: National defense: New: Buildings: Industrial
    'B816RC1A027NBEA', # Gross government fixed investment: Structures: Federal: National defense: New: Buildings: Residential
    'B818RC1A027NBEA', # Gross government fixed investment: Structures: Federal: National defense: New: Military facilities
    'A830RC1A027NBEA', # Gross government fixed investment: Structures: Federal: Nondefense
    'A831RC1A027NBEA', # Gross government fixed investment: Structures: Federal: Nondefense: New
    'W187RC1A027NBEA', # Gross government fixed investment: Structures: Federal: Nondefense: New: Amusement and recreation
    'A832RC1A027NBEA', # Gross government fixed investment: Structures: Federal: Nondefense: New: Buildings
    'B835RC1A027NBEA', # Gross government fixed investment: Structures: Federal: Nondefense: New: Buildings: Educational
    'B836RC1A027NBEA', # Gross government fixed investment: Structures: Federal: Nondefense: New: Buildings: Hospital
    'B834RC1A027NBEA', # Gross government fixed investment: Structures: Federal: Nondefense: New: Buildings: Industrial
    'B837RC1A027NBEA', # Gross government fixed investment: Structures: Federal: Nondefense: New: Buildings: Other
    'W183RC1A027NBEA', # Gross government fixed investment: Structures: Federal: Nondefense: New: Commercial
    'B839RC1A027NBEA', # Gross government fixed investment: Structures: Federal: Nondefense: New: Conservation and development
    'W191RC1A027NBEA', # Gross government fixed investment: Structures: Federal: Nondefense: New: Conservation and development
    'W185RC1A027NBEA', # Gross government fixed investment: Structures: Federal: Nondefense: New: Educational
    'W184RC1A027NBEA', # Gross government fixed investment: Structures: Federal: Nondefense: New: Health care
    'B838RC1A027NBEA', # Gross government fixed investment: Structures: Federal: Nondefense: New: Highways and streets
    'W190RC1A027NBEA', # Gross government fixed investment: Structures: Federal: Nondefense: New: Highways and streets
    'W182RC1A027NBEA', # Gross government fixed investment: Structures: Federal: Nondefense: New: Office
    'B840RC1A027NBEA', # Gross government fixed investment: Structures: Federal: Nondefense: New: Other
    'W192RC1A027NBEA', # Gross government fixed investment: Structures: Federal: Nondefense: New: Other
    'W189RC1A027NBEA', # Gross government fixed investment: Structures: Federal: Nondefense: New: Power
    'W186RC1A027NBEA', # Gross government fixed investment: Structures: Federal: Nondefense: New: Public safety
    'W188RC1A027NBEA', # Gross government fixed investment: Structures: Federal: Nondefense: New: Transportation
    'A842RC1A027NBEA', # Gross government fixed investment: Structures: State and local
    'A843RC1A027NBEA', # Gross government fixed investment: Structures: State and local: New
    'W197RC1A027NBEA', # Gross government fixed investment: Structures: State and local: New: Amusement and recreation
    'A844RC1A027NBEA', # Gross government fixed investment: Structures: State and local: New: Buildings
    'B847RC1A027NBEA', # Gross government fixed investment: Structures: State and local: New: Buildings: Educational
    'B848RC1A027NBEA', # Gross government fixed investment: Structures: State and local: New: Buildings: Hospital
    'B849RC1A027NBEA', # Gross government fixed investment: Structures: State and local: New: Buildings: Other
    'B845RC1A027NBEA', # Gross government fixed investment: Structures: State and local: New: Buildings: Residential
    'W194RC1A027NBEA', # Gross government fixed investment: Structures: State and local: New: Commercial
    'B857RC1A027NBEA', # Gross government fixed investment: Structures: State and local: New: Conservation and development
    'W169RC1A027NBEA', # Gross government fixed investment: Structures: State and local: New: Conservation and development
    'W148RC1A027NBEA', # Gross government fixed investment: Structures: State and local: New: Educational
    'W195RC1A027NBEA', # Gross government fixed investment: Structures: State and local: New: Health care
    'B851RC1A027NBEA', # Gross government fixed investment: Structures: State and local: New: Highways and streets
    'W149RC1A027NBEA', # Gross government fixed investment: Structures: State and local: New: Highways and streets
    'W193RC1A027NBEA', # Gross government fixed investment: Structures: State and local: New: Office
    'B860RC1A027NBEA', # Gross government fixed investment: Structures: State and local: New: Other
    'W200RC1A027NBEA', # Gross government fixed investment: Structures: State and local: New: Other
    'W199RC1A027NBEA', # Gross government fixed investment: Structures: State and local: New: Power
    'W196RC1A027NBEA', # Gross government fixed investment: Structures: State and local: New: Public safety
    'W147RC1A027NBEA', # Gross government fixed investment: Structures: State and local: New: Residential
    'B858RC1A027NBEA', # Gross government fixed investment: Structures: State and local: New: Sewer systems
    'W150RC1A027NBEA', # Gross government fixed investment: Structures: State and local: New: Sewer systems
    'W198RC1A027NBEA', # Gross government fixed investment: Structures: State and local: New: Transportation
    'B859RC1A027NBEA', # Gross government fixed investment: Structures: State and local: New: Water systems
    'W168RC1A027NBEA', # Gross government fixed investment: Structures: State and local: New: Water systems
    ## Bil. of Chn. 2005 $ (NSA)
    'B815RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: National defense: New: Buildings (DISCONTINUED)
    'B832RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: Nondefense: New: Buildings (DISCONTINUED)
    'B835RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: Nondefense: New: Buildings: Educational (DISCONTINUED)
    'B836RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: Nondefense: New: Buildings: Hospital (DISCONTINUED)
    'B834RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: Nondefense: New: Buildings: Industrial (DISCONTINUED)
    'B837RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: Nondefense: New: Buildings: Other (DISCONTINUED)
    'B839RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: Nondefense: New: Conservation and development (DISCONTINUED)
    'B838RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: Nondefense: New: Highways and streets (DISCONTINUED)
    'B840RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: Nondefense: New: Other (DISCONTINUED)
    'B844RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: New: Buildings (DISCONTINUED)
    'B847RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: New: Buildings: Educational (DISCONTINUED)
    'B848RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: New: Buildings: Hospital (DISCONTINUED)
    'B849RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: New: Buildings: Other (DISCONTINUED)
    'B845RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: New: Buildings: Residential (DISCONTINUED)
    'B857RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: New: Conservation and development (DISCONTINUED)
    'B851RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: New: Highways and streets (DISCONTINUED)
    'B860RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: New: Other (DISCONTINUED)
    'B858RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: New: Sewer systems (DISCONTINUED)
    'B859RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: New: Water systems (DISCONTINUED)
    ## Bil. of Chn. 2017 $ (NSA)
    'Y074RX1A020NBEA', # Real government enterprise gross fixed investment: Federal: Equipment
    'Y075RX1A020NBEA', # Real government enterprise gross fixed investment: Federal: Intellectual property products
    'Y077RX1A020NBEA', # Real government enterprise gross fixed investment: State and local: Equipment
    'Y078RX1A020NBEA', # Real government enterprise gross fixed investment: State and local: Intellectual property products
    'A967RX1A020NBEA', # Real gross government fixed investment: Residual
    'B819RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: National defense: Net purchases of used structures
    'A814RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: National defense: New
    'B817RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: National defense: New: Buildings: Industrial
    'B816RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: National defense: New: Buildings: Residential
    'B818RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: National defense: New: Military facilities
    'B841RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: Nondefense: Net purchases of used structures
    'A831RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: Nondefense: New
    'W187RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: Nondefense: New: Amusement and recreation
    'W183RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: Nondefense: New: Commercial
    'W191RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: Nondefense: New: Conservation and development
    'W185RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: Nondefense: New: Educational
    'W184RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: Nondefense: New: Health care
    'W190RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: Nondefense: New: Highways and streets
    'W182RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: Nondefense: New: Office
    'W192RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: Nondefense: New: Other
    'W189RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: Nondefense: New: Power
    'W186RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: Nondefense: New: Public safety
    'W188RX1A020NBEA', # Real gross government fixed investment: Structures: Federal: Nondefense: New: Transportation
    'B870RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: Net purchases of used structures
    'A843RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: New
    'W197RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: New: Amusement and recreation
    'W194RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: New: Commercial
    'W169RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: New: Conservation and development
    'W148RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: New: Educational
    'W195RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: New: Health care
    'W149RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: New: Highways and streets
    'W193RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: New: Office
    'W200RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: New: Other
    'W199RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: New: Power
    'W196RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: New: Public safety
    'W147RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: New: Residential
    'W150RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: New: Sewer systems
    'W198RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: New: Transportation
    'W168RX1A020NBEA', # Real gross government fixed investment: Structures: State and local: New: Water systems

    # Gov't Receipts, Expenditures & Investment > Gov't Investment (137)
    ## % Chg. from Preceding Period (NSA)
    'A782RL1A225NBEA', # Real Government Gross Investment
    'Y054RL1A225NBEA', # Real Government Gross Investment: Equipment
    'A787RL1A225NBEA', # Real Government Gross Investment: Federal: Gross Investment
    'Y058RL1A225NBEA', # Real Government Gross Investment: Federal: Gross Investment: Equipment
    'Y059RL1A225NBEA', # Real Government Gross Investment: Federal: Gross Investment: Intellectual Property Products
    'Y061RL1A225NBEA', # Real Government Gross Investment: Federal: Gross Investment: Intellectual Property Products: Research and Development
    'Y060RL1A225NBEA', # Real Government Gross Investment: Federal: Gross Investment: Intellectual Property Products: Software
    'A801RL1A225NBEA', # Real Government Gross Investment: Federal: Gross Investment: Structures
    'A788RL1A225NBEA', # Real Government Gross Investment: Federal: National Defense: Gross Investment
    'Y050RL1A225NBEA', # Real Government Gross Investment: Federal: National Defense: Gross Investment: Equipment
    'Y052RL1A225NBEA', # Real Government Gross Investment: Federal: National Defense: Gross Investment: Intellectual Property Products
    'Y076RL1A225NBEA', # Real Government Gross Investment: Federal: National Defense: Gross Investment: Intellectual Property Products: Research and Development
    'Y053RL1A225NBEA', # Real Government Gross Investment: Federal: National Defense: Gross Investment: Intellectual Property Products: Software
    'A808RL1A225NBEA', # Real Government Gross Investment: Federal: National Defense: Gross Investment: Structures
    'A798RL1A225NBEA', # Real Government Gross Investment: Federal: Nondefense: Gross Investment
    'Y066RL1A225NBEA', # Real Government Gross Investment: Federal: Nondefense: Gross Investment: Equipment
    'Y067RL1A225NBEA', # Real Government Gross Investment: Federal: Nondefense: Gross Investment: Intellectual Property Products
    'Y069RL1A225NBEA', # Real Government Gross Investment: Federal: Nondefense: Gross Investment: Intellectual Property Products: Research and Development
    'Y068RL1A225NBEA', # Real Government Gross Investment: Federal: Nondefense: Gross Investment: Intellectual Property Products: Software
    'A830RL1A225NBEA', # Real Government Gross Investment: Federal: Nondefense: Gross Investment: Structures
    'Y055RL1A225NBEA', # Real Government Gross Investment: Intellectual Property Products
    'Y057RL1A225NBEA', # Real Government Gross Investment: Intellectual Property Products: Research and Development
    'Y056RL1A225NBEA', # Real Government Gross Investment: Intellectual Property Products: Software
    'A799RL1A225NBEA', # Real Government Gross Investment: State and Local: Gross Investment
    'Y070RL1A225NBEA', # Real Government Gross Investment: State and Local: Gross Investment: Equipment
    'Y071RL1A225NBEA', # Real Government Gross Investment: State and Local: Gross Investment: Intellectual Property Products
    'Y073RL1A225NBEA', # Real Government Gross Investment: State and Local: Gross Investment: Intellectual Property Products: Research and Development
    'Y072RL1A225NBEA', # Real Government Gross Investment: State and Local: Gross Investment: Intellectual Property Products: Software
    'A842RL1A225NBEA', # Real Government Gross Investment: State and Local: Gross Investment: Structures
    'A760RL1A225NBEA', # Real Government Gross Investment: Structures
    ## Bil. of $ (NSA)
    'B144RC1A027NBEA', # Automobile output: Final sales: Gross government investment
    'Y054RC1A027NBEA', # Government Gross Investment: Equipment
    'Y058RC1A027NBEA', # Government Gross Investment: Federal: Gross Investment: Equipment
    'Y059RC1A027NBEA', # Government Gross Investment: Federal: Gross Investment: Intellectual Property Products
    'Y061RC1A027NBEA', # Government Gross Investment: Federal: Gross Investment: Intellectual Property Products: Research and Development
    'Y060RC1A027NBEA', # Government Gross Investment: Federal: Gross Investment: Intellectual Property Products: Software
    'Y050RC1A027NBEA', # Government Gross Investment: Federal: National Defense: Gross Investment: Equipment
    'Y052RC1A027NBEA', # Government Gross Investment: Federal: National Defense: Gross Investment: Intellectual Property Products
    'Y076RC1A027NBEA', # Government Gross Investment: Federal: National Defense: Gross Investment: Intellectual Property Products: Research and Development
    'Y053RC1A027NBEA', # Government Gross Investment: Federal: National Defense: Gross Investment: Intellectual Property Products: Software
    'Y066RC1A027NBEA', # Government Gross Investment: Federal: Nondefense: Gross Investment: Equipment
    'Y067RC1A027NBEA', # Government Gross Investment: Federal: Nondefense: Gross Investment: Intellectual Property Products
    'Y069RC1A027NBEA', # Government Gross Investment: Federal: Nondefense: Gross Investment: Intellectual Property Products: Research and Development
    'Y068RC1A027NBEA', # Government Gross Investment: Federal: Nondefense: Gross Investment: Intellectual Property Products: Software
    'Y055RC1A027NBEA', # Government Gross Investment: Intellectual Property Products
    'Y057RC1A027NBEA', # Government Gross Investment: Intellectual Property Products: Research and Development
    'Y056RC1A027NBEA', # Government Gross Investment: Intellectual Property Products: Software
    'Y070RC1A027NBEA', # Government Gross Investment: State and Local: Gross Investment: Equipment
    'Y071RC1A027NBEA', # Government Gross Investment: State and Local: Gross Investment: Intellectual Property Products
    'Y073RC1A027NBEA', # Government Gross Investment: State and Local: Gross Investment: Intellectual Property Products: Research and Development
    'Y072RC1A027NBEA', # Government Gross Investment: State and Local: Gross Investment: Intellectual Property Products: Software
    'Y085RC1A027NBEA', # Government investment: Equipment: Consumption of fixed capital
    'Y091RC1A027NBEA', # Government investment: Intellectual property products: Consumption of fixed capital
    'Y086RC1A027NBEA', # Government investment: Net Equipment
    'Y087RC1A027NBEA', # Government investment: Net equipment: Federal
    'Y088RC1A027NBEA', # Government investment: Net equipment: Federal: National defense
    'Y089RC1A027NBEA', # Government investment: Net equipment: Federal: Nondefense
    'Y090RC1A027NBEA', # Government investment: Net equipment: State and local
    'Y092RC1A027NBEA', # Government investment: Net intellectual property products
    'Y093RC1A027NBEA', # Government investment: Net intellectual property products: Federal
    'Y094RC1A027NBEA', # Government investment: Net intellectual property products: Federal: National defense
    'Y095RC1A027NBEA', # Government investment: Net intellectual property products: Federal: Nondefense
    'Y096RC1A027NBEA', # Government investment: Net intellectual property products: State and local
    'A782RC1A027NBEA', # Gross government investment
    'A787RC1A027NBEA', # Gross government investment: Federal
    'A799RC1A027NBEA', # Gross government investment: State and local
    'W867RC1A027NBEA', # Local government expenditures: Gross government investment
    'AB64RC1A027NBEA', # Motor vehicle output: Gross government investment
    'B708RC1A027NBEA', # Motor vehicle output: Gross government investment: Trucks
    'A871RC1A027NBEA', # Net government investment: Equipment and software (DISCONTINUED)
    'B891RC1A027NBEA', # Net government investment: Federal: National defense
    'B892RC1A027NBEA', # Net government investment: Federal: Nondefense
    'A901RC1A027NBEA', # Net government investment: Net equipment and software (DISCONTINUED)
    'A902RC1A027NBEA', # Net government investment: Net equipment and software: Federal (DISCONTINUED)
    'B905RC1A027NBEA', # Net government investment: Net equipment and software: Federal: National defense (DISCONTINUED)
    'B906RC1A027NBEA', # Net government investment: Net equipment and software: Federal: Nondefense (DISCONTINUED)
    'B907RC1A027NBEA', # Net government investment: Net equipment and software: State and local (DISCONTINUED)
    'A895RC1A027NBEA', # Net government investment: Net structures
    'A896RC1A027NBEA', # Net government investment: Net structures: Federal
    'B897RC1A027NBEA', # Net government investment: Net structures: Federal: National defense
    'B898RC1A027NBEA', # Net government investment: Net structures: Federal: Nondefense
    'B899RC1A027NBEA', # Net government investment: Net structures: State and local
    'A760RC1A027NBEA', # Net government investment: Structures
    'W767RC1A027NBEA', # State government expenditures: Gross government investment
    ## Bil. of Chn. 2005 $ (NSA)
    'A871RX1A020NBEA', # Real net government investment: Equipment and software (DISCONTINUED)
    'A901RX1A020NBEA', # Real net government investment: Net equipment and software (DISCONTINUED)
    'A902RX1A020NBEA', # Real net government investment: Net equipment and software: Federal (DISCONTINUED)
    'B905RX1A020NBEA', # Real net government investment: Net equipment and software: Federal: National defense (DISCONTINUED)
    'B906RX1A020NBEA', # Real net government investment: Net equipment and software: Federal: Nondefense (DISCONTINUED)
    'B907RX1A020NBEA', # Real net government investment: Net equipment and software: State and local (DISCONTINUED)
    ## Bil. of Chn. 2017 $ (NSA)
    'Y058RX1A020NBEA', # Real Government Gross Investment: Federal: Gross Investment: Equipment
    'Y059RX1A020NBEA', # Real Government Gross Investment: Federal: Gross Investment: Intellectual Property Products
    'Y061RX1A020NBEA', # Real Government Gross Investment: Federal: Gross Investment: Intellectual Property Products: Research and Development
    'Y060RX1A020NBEA', # Real Government Gross Investment: Federal: Gross Investment: Intellectual Property Products: Software
    'Y050RX1A020NBEA', # Real Government Gross Investment: Federal: National Defense: Gross Investment: Equipment
    'Y052RX1A020NBEA', # Real Government Gross Investment: Federal: National Defense: Gross Investment: Intellectual Property Products
    'Y076RX1A020NBEA', # Real Government Gross Investment: Federal: National Defense: Gross Investment: Intellectual Property Products: Research and Development
    'Y053RX1A020NBEA', # Real Government Gross Investment: Federal: National Defense: Gross Investment: Intellectual Property Products: Software
    'Y066RX1A020NBEA', # Real Government Gross Investment: Federal: Nondefense: Gross Investment: Equipment
    'Y067RX1A020NBEA', # Real Government Gross Investment: Federal: Nondefense: Gross Investment: Intellectual Property Products
    'Y069RX1A020NBEA', # Real Government Gross Investment: Federal: Nondefense: Gross Investment: Intellectual Property Products: Research and Development
    'Y068RX1A020NBEA', # Real Government Gross Investment: Federal: Nondefense: Gross Investment: Intellectual Property Products: Software
    'Y054RX1A020NBEA', # Real Government Gross Investment: Gross Investment: Equipment
    'Y055RX1A020NBEA', # Real Government Gross Investment: Gross Investment: Intellectual Property Products
    'Y057RX1A020NBEA', # Real Government Gross Investment: Gross Investment: Intellectual Property Products: Research and Development
    'Y056RX1A020NBEA', # Real Government Gross Investment: Gross Investment: Intellectual Property Products: Software
    'Y070RX1A020NBEA', # Real Government Gross Investment: State and Local: Gross Investment: Equipment
    'Y071RX1A020NBEA', # Real Government Gross Investment: State and Local: Gross Investment: Intellectual Property Products
    'Y073RX1A020NBEA', # Real Government Gross Investment: State and Local: Gross Investment: Intellectual Property Products: Research and Development
    'Y072RX1A020NBEA', # Real Government Gross Investment: State and Local: Gross Investment: Intellectual Property Products: Software
    'Y085RX1A020NBEA', # Real government investment: Equipment: Consumption of fixed capital
    'Y091RX1A020NBEA', # Real government investment: Intellectual property products: Consumption of fixed capital
    'Y086RX1A020NBEA', # Real government investment: Net Equipment
    'Y087RX1A020NBEA', # Real government investment: Net Equipment: Federal
    'Y088RX1A020NBEA', # Real government investment: Net equipment: Federal: National defense
    'Y089RX1A020NBEA', # Real government investment: Net equipment: Federal: Nondefense
    'Y090RX1A020NBEA', # Real government investment: Net equipment: State and local
    'Y092RX1A020NBEA', # Real government investment: Net intellectual property products
    'Y093RX1A020NBEA', # Real government investment: Net intellectual property products: Federal
    'Y094RX1A020NBEA', # Real government investment: Net intellectual property products: Federal: National defense
    'Y095RX1A020NBEA', # Real government investment: Net intellectual property products: Federal: Nondefense
    'Y096RX1A020NBEA', # Real government investment: Net intellectual property products: State and local
    'A782RX1A020NBEA', # Real gross government investment
    'AB64RX1A020NBEA', # Real motor vehicle output: Gross government investment
    'B144RX1A020NBEA', # Real motor vehicle output: Gross government investment: Autos
    'B708RX1A020NBEA', # Real motor vehicle output: Gross government investment: Trucks
    'A889RX1A020NBEA', # Real net government investment
    'A890RX1A020NBEA', # Real net government investment: Federal
    'B891RX1A020NBEA', # Real net government investment: Federal: National defense
    'B892RX1A020NBEA', # Real net government investment: Federal: Nondefense
    'A895RX1A020NBEA', # Real net government investment: Net structures
    'A896RX1A020NBEA', # Real net government investment: Net structures: Federal
    'B897RX1A020NBEA', # Real net government investment: Net structures: Federal: National defense
    'B898RX1A020NBEA', # Real net government investment: Net structures: Federal: Nondefense
    'B899RX1A020NBEA', # Real net government investment: Net structures: State and local
    'B893RX1A020NBEA', # Real net government investment: State and local
    'A760RX1A020NBEA', # Real net government investment: Structures

    # Gov't Receipts, Expenditures & Investment > Gov't Social Benefits (123)
    ## Bil. of $ (NSA)
    'Y290RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Cash flow
    'Y291RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Cash flow: Actual employer and household contributions
    'Y296RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Cash flow: Administrative expenses
    'Y294RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Cash flow: Benefit payments and withdrawals: Civilian
    'Y295RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Cash flow: Benefit payments and withdrawals: Military
    'Y292RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Cash flow: Monetary income receipts on assets
    'Y284RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Current expenditures, accrual basis
    'Y289RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Current expenditures, accrual basis: Net change in benefit entitlements
    'Y268RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Current receipts, accrual basis
    'Y269RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Current receipts, accrual basis: Contributions
    'Y285RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Current receipts, accrual basis: Contributions: Claims to benefits accrued through service to employers
    'Y270RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Current receipts, accrual basis: Contributions: Claims to benefits accrued through service to employers: Actual employer contributions
    'Y271RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Current receipts, accrual basis: Contributions: Claims to benefits accrued through service to employers: Actual employer contributions: Civilian
    'Y272RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Current receipts, accrual basis: Contributions: Claims to benefits accrued through service to employers: Actual employer contributions: Military
    'Y277RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Current receipts, accrual basis: Contributions: Claims to benefits accrued through service to employers: Actual household contributions: Civilian
    'Y278RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Current receipts, accrual basis: Contributions: Claims to benefits accrued through service to employers: Actual household contributions: Military
    'Y273RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Current receipts, accrual basis: Contributions: Claims to benefits accrued through service to employers: Imputed employer contributions
    'Y274RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Current receipts, accrual basis: Contributions: Claims to benefits accrued through service to employers: Imputed employer contributions: Civilian
    'Y275RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Current receipts, accrual basis: Contributions: Claims to benefits accrued through service to employers: Imputed employer contributions: Military
    'Y280RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Current receipts, accrual basis: Income receipts on assets: Interest
    'Y282RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Current receipts, accrual basis: Income receipts on assets: Interest: Imputed interest on plans' claims on employers
    'Y281RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Current receipts, accrual basis: Income receipts on assets: Interest: Monetary interest
    'Y293RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Effect of participation in defined benefit plans on personal income, saving, and wealth: Benefit payments and withdrawals
    'Y306RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Effect of participation in defined benefit plans on personal income, saving, and wealth: Change in benefit entitlements including implied funding of benefits from holding gains on assets
    'Y303RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Effect of participation in defined benefit plans on personal income, saving, and wealth: Change in personal wealth
    'Y297RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Effect of participation in defined benefit plans on personal income, saving, and wealth: Effect on personal income
    'Y299RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Effect of participation in defined benefit plans on personal income, saving, and wealth: Effect on personal saving
    'Y276RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Effect of participation in defined benefit plans on personal income, saving, and wealth: Household actual contributions
    'Y300RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Effect of participation in defined benefit plans on personal income, saving, and wealth: Implied funding of benefits from holding gains on assets
    'Y301RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Effect of participation in defined benefit plans on personal income, saving, and wealth: Implied funding of benefits from holding gains on assets: Interest accrued on benefit entitlements
    'Y279RC1A027NBEA', # Federal Government Defined Benefit Pension Plans: Effect of participation in defined benefit plans on personal income, saving, and wealth: Implied funding of benefits from holding gains on assets: Interest and dividend income received by plans
    'W015RC1A027NBEA', # Federal government current transfer payments: Government social benefits
    'B087RC1A027NBEA', # Federal government current transfer payments: Government social benefits: to persons
    'W063RC1A027NBEA', # Government current transfer payments: Government social benefits
    'W016RC1A027NBEA', # Government current transfer payments: Government social benefits: to the rest of the world
    'G170331A027NBEA', # Government social benefits: Economic affairs
    'G170371A027NBEA', # Government social benefits: Education
    'G170421A027NBEA', # Government social benefits: Federal: Economic affairs
    'G170461A027NBEA', # Government social benefits: Federal: Education
    'G170401A027NBEA', # Government social benefits: Federal: General public service
    'G170441A027NBEA', # Government social benefits: Federal: Health
    'G170431A027NBEA', # Government social benefits: Federal: Housing and community services
    'G170471A027NBEA', # Government social benefits: Federal: Income security
    'G170411A027NBEA', # Government social benefits: Federal: Public order and safety
    'G170451A027NBEA', # Government social benefits: Federal: Recreation and culture
    'G170311A027NBEA', # Government social benefits: General public service
    'G170351A027NBEA', # Government social benefits: Health
    'G170341A027NBEA', # Government social benefits: Housing and community services
    'G170381A027NBEA', # Government social benefits: Income security
    'G170321A027NBEA', # Government social benefits: Public order and safety
    'G170361A027NBEA', # Government social benefits: Recreation and culture
    'G170511A027NBEA', # Government social benefits: State and local: Economic affairs
    'G170531A027NBEA', # Government social benefits: State and local: Education
    'G170491A027NBEA', # Government social benefits: State and local: General public service
    'G170521A027NBEA', # Government social benefits: State and local: Health
    'G170541A027NBEA', # Government social benefits: State and local: Income security
    'G170501A027NBEA', # Government social benefits: State and local: Public order and safety
    'A1588C1A027NBEA', # Government social benefits: to persons: Federal: Benefits from social insurance funds
    'B1044C1A027NBEA', # Government social benefits: to persons: Federal: Benefits from social insurance funds: Pension benefit guaranty
    'TRP2501A027NBEA', # Government social benefits: to persons: Federal: Benefits from social insurance funds: Railroad retirement
    'A1589C1A027NBEA', # Government social benefits: to persons: Federal: Benefits from social insurance funds: Unemployment insurance
    'B1590C1A027NBEA', # Government social benefits: to persons: Federal: Benefits from social insurance funds: Unemployment insurance: Emergency unemployment compensation
    'W874RC1A027NBEA', # Government social benefits: to persons: Federal: Benefits from social insurance funds: Unemployment insurance: Federal employees
    'TRP2001A027NBEA', # Government social benefits: to persons: Federal: Benefits from social insurance funds: Unemployment insurance: Railroad employees
    'L311071A027NBEA', # Government social benefits: to persons: Federal: Benefits from social insurance funds: Unemployment insurance: State
    'TRP3501A027NBEA', # Government social benefits: to persons: Federal: Benefits from social insurance funds: Veterans' life insurance
    'TRP3751A027NBEA', # Government social benefits: to persons: Federal: Benefits from social insurance funds: Workers' compensation
    'TRP6501A027NBEA', # Government social benefits: to persons: Federal: Black lung benefits
    'TRP7301A027NBEA', # Government social benefits: to persons: Federal: Direct relief
    'W812RC1A027NBEA', # Government social benefits: to persons: Federal: Other
    'W811RC1A027NBEA', # Government social benefits: to persons: Federal: Refundable tax credits
    'TRP6001A027NBEA', # Government social benefits: to persons: Federal: Supplemental Nutrition Assistance Program (SNAP)
    'TRP7001A027NBEA', # Government social benefits: to persons: Federal: Supplemental security income
    'A1594C1A027NBEA', # Government social benefits: to persons: Federal: Veterans' benefits
    'TRP5701A027NBEA', # Government social benefits: to persons: Federal: Veterans' benefits: Other
    'TRP4501A027NBEA', # Government social benefits: to persons: Federal: Veterans' benefits: Pension and disability
    'TRP5001A027NBEA', # Government social benefits: to persons: Federal: Veterans' benefits: Readjustment
    'A1595C1A027NBEA', # Government social benefits: to persons: State and local: Benefits from social insurance funds
    'S122001A027NBEA', # Government social benefits: to persons: State and local: Benefits from social insurance funds: Temporary disability insurance
    'S123001A027NBEA', # Government social benefits: to persons: State and local: Benefits from social insurance funds: Workers' compensation
    'B1603C1A027NBEA', # Government social benefits: to persons: State and local: Education
    'B1604C1A027NBEA', # Government social benefits: to persons: State and local: Employment and training
    'B1605C1A027NBEA', # Government social benefits: to persons: State and local: Other
    'A1596C1A027NBEA', # Government social benefits: to persons: State and local: Public assistance
    'B1601C1A027NBEA', # Government social benefits: to persons: State and local: Public assistance: Energy assistance
    'B1598C1A027NBEA', # Government social benefits: to persons: State and local: Public assistance: Family assistance
    'B1600C1A027NBEA', # Government social benefits: to persons: State and local: Public assistance: General assistance
    'B1597C1A027NBEA', # Government social benefits: to persons: State and local: Public assistance: Medical care
    'TRP8101A027NBEA', # Government social benefits: to persons: State and local: Public assistance: Medical care: Other medical care
    'B1602C1A027NBEA', # Government social benefits: to persons: State and local: Public assistance: Other
    'B1599C1A027NBEA', # Government social benefits: to persons: State and local: Public assistance: Supplemental security income
    'W026RC1A027NBEA', # Government social insurance funds: Current federal expenditures: Government social benefits
    'W872RC1A027NBEA', # Government social insurance funds: Current federal expenditures: Government social benefits: to the rest of the world
    'W401RC1A027NBEA', # Household current transfer receipts: Government social benefits
    'A063RC1A027NBEA', # Personal current transfer receipts: Government social benefits to persons
    'W729RC1A027NBEA', # Personal current transfer receipts: Government social benefits to persons: Medicaid
    'W824RC1A027NBEA', # Personal current transfer receipts: Government social benefits to persons: Medicare
    'W827RC1A027NBEA', # Personal current transfer receipts: Government social benefits to persons: Other
    'W823RC1A027NBEA', # Personal current transfer receipts: Government social benefits to persons: Social security
    'W825RC1A027NBEA', # Personal current transfer receipts: Government social benefits to persons: Unemployment insurance
    'W826RC1A027NBEA', # Personal current transfer receipts: Government social benefits to persons: Veterans' benefits
    'Y323RC1A027NBEA', # State and Local Government Defined Benefit Pension Plans: Cash flow
    'Y324RC1A027NBEA', # State and Local Government Defined Benefit Pension Plans: Cash flow: Actual employer and household contributions
    'Y327RC1A027NBEA', # State and Local Government Defined Benefit Pension Plans: Cash flow: Administrative expenses
    'S121001A027NBEA', # State and Local Government Defined Benefit Pension Plans: Cash flow: Benefit payments and withdrawals
    'Y325RC1A027NBEA', # State and Local Government Defined Benefit Pension Plans: Cash flow: Monetary income receipts on assets
    'Y317RC1A027NBEA', # State and Local Government Defined Benefit Pension Plans: Current expenditures, accrual basis
    'Y313RC1A027NBEA', # State and Local Government Defined Benefit Pension Plans: Current expenditures, accrual basis: Imputed income payments on assets to persons: Interest
    'Y309RC1A027NBEA', # State and Local Government Defined Benefit Pension Plans: Current expenditures, accrual basis: Net change in benefit entitlements
    'Y307RC1A027NBEA', # State and Local Government Defined Benefit Pension Plans: Current receipts, accrual basis
    'Y308RC1A027NBEA', # State and Local Government Defined Benefit Pension Plans: Current receipts, accrual basis: Contributions
    'Y318RC1A027NBEA', # State and Local Government Defined Benefit Pension Plans: Current receipts, accrual basis: Contributions: Claims to benefits accrued through service to employers
    'Y310RC1A027NBEA', # State and Local Government Defined Benefit Pension Plans: Current receipts, accrual basis: Contributions: Claims to benefits accrued through service to employers: Imputed employer contributions
    'Y315RC1A027NBEA', # State and Local Government Defined Benefit Pension Plans: Current receipts, accrual basis: Income receipts on assets: Interest: Imputed interest on plans' claims on employers
    'Y314RC1A027NBEA', # State and Local Government Defined Benefit Pension Plans: Current receipts, accrual basis: Income receipts on assets: Monetary interest
    'Y328RC1A027NBEA', # State and Local Government Defined Benefit Pension Plans: Effect of participation in defined benefit plans on personal income
    'Y337RC1A027NBEA', # State and Local Government Defined Benefit Pension Plans: Effect of participation in defined benefit plans on personal income, saving, and wealth: Change in benefit entitlements including implied funding of benefits from holding gains on assets
    'Y334RC1A027NBEA', # State and Local Government Defined Benefit Pension Plans: Effect of participation in defined benefit plans on personal income, saving, and wealth: Change in personal wealth
    'S251201A027NBEA', # State and Local Government Defined Benefit Pension Plans: Effect of participation in defined benefit plans on personal income, saving, and wealth: Household actual contributions
    'Y331RC1A027NBEA', # State and Local Government Defined Benefit Pension Plans: Effect of participation in defined benefit plans on personal income, saving, and wealth: Implied funding of benefits from holding gains on assets
    'Y332RC1A027NBEA', # State and Local Government Defined Benefit Pension Plans: Effect of participation in defined benefit plans on personal income, saving, and wealth: Implied funding of benefits from holding gains on assets: Interest accrued on benefit entitlements
    'Y312RC1A027NBEA', # State and Local Government Defined Benefit Pension Plans: Effect of participation in defined benefit plans on personal income, saving, and wealth: Implied funding of benefits from holding gains on assets: Interest and dividend income received by plans
    'Y330RC1A027NBEA', # State and Local Government Defined Benefit Pension Plans: Effect of participation in defined benefit plans on personal saving

]
