# FRED > Z.1 Financial Accounts > Table S1M.b Households and nonprofit organizations (release 52, element 1256192)
# https://fred.stlouisfed.org/release/tables?rid=52&eid=1256192  가계·비영리단체 대차대조표 54줄 전체 (macro-dashboard용)
# 원표 https://www.federalreserve.gov/releases/z1/current/html/S1M_b.htm  (연준 원표는 십억 달러, FRED 는 백만 달러)
# 위계: # 표 > ## 단위 (계절조정)
dir='us_macro_Z1_Households_BS'

# Quarterly (54)
ids_Q = [
    # S1M.b (54)
    ## Mil. of $ (NSA) / % (줄 52·54)
    'TABSHNO', # Households and nonprofit organizations; total assets
    'BOGZ1LM152010005Q', # Households and nonprofit organizations; nonfinancial assets
    'HNOREMV', # Households and nonprofit organizations; real estate at market value
    'HOOREVLMHMV', # Households; owner-occupied real estate including vacant land and mobile homes at market value
    'NOREMV', # Nonprofit organizations; real estate at market value
    'BOGZ1LM165015205Q', # Nonprofit organizations; equipment, current cost basis
    'BOGZ1LM165013765Q', # Nonprofit organizations; nonresidential intellectual property products, current cost basis
    'BOGZ1LM155111005Q', # Households and nonprofit organizations; consumer durable goods, current cost basis
    'TFAABSHNO', # Households and nonprofit organizations; total financial assets
    'CDCABSHNO', # Households and nonprofit organizations; checkable deposits and currency; asset
    'TSDABSHNO', # Households and nonprofit organizations; total time and savings deposits; asset
    'BOGZ1LM153030505Q', # Households and nonprofit organizations; other deposits; asset
    'BOGZ1LM154022005Q', # Households and nonprofit organizations; debt securities; asset
    'BOGZ1LM153061105Q', # Households and nonprofit organizations; Treasury securities; asset
    'BOGZ1LM153061705Q', # Households and nonprofit organizations; agency- and GSE-backed securities; asset
    'BOGZ1LM153062005Q', # Households and nonprofit organizations; municipal securities; asset
    'BOGZ1LM153063005Q', # Households and nonprofit organizations; corporate and foreign bonds; asset
    'HNOLA', # Households and nonprofit organizations; loans; asset
    'NOCCSLA', # Nonprofit organizations; consumer credit, student loans; asset
    'MABSHNO', # Households and nonprofit organizations; total mortgages; asset
    'BOGZ1FL153069005Q', # Households and nonprofit organizations; other loans and advances; asset
    'HNOCEA', # Households and nonprofit organizations; corporate equities; asset
    'BOGZ1LM153081115Q', # Households and nonprofit organizations; other equity; asset (IMA)
    'MMFSABSHNO', # Households and nonprofit organizations; money market fund shares; asset
    'HNOMFSA', # Households and nonprofit organizations; mutual fund shares; asset
    'BOGZ1LM153064705Q', # Households and nonprofit organizations; hedge fund shares; asset
    'BOGZ1LM153064505Q', # Households and nonprofit organizations; private debt fund shares; asset
    'LIRABSHNO', # Households and nonprofit organizations; life insurance reserves; asset
    'HNOPFAQ027S', # Households and nonprofit organizations; pension entitlements; asset
    'BOGZ1FL163070005Q', # Nonprofit organizations; grants and trade receivables; asset
    'MAABSHNO', # Households and nonprofit organizations; total miscellaneous assets
    'TLBSHNO', # Households and nonprofit organizations; total liabilities
    'MSLBSHNO', # Nonprofit organizations; municipal securities; liability
    'HNOLL', # Households and nonprofit organizations; loans; liability
    'BLNECLBSHNO', # Households and nonprofit organizations; depository institution loans n.e.c.; liability
    'CCLBSHNO', # Households and nonprofit organizations; consumer credit; liability
    'HMLBSHNO', # Households and nonprofit organizations; one-to-four-family residential mortgages; liability
    'CMLBSHNO', # Nonprofit organizations; commercial mortgages; liability
    'OLALBSHNO', # Households and nonprofit organizations; other loans and advances; liability
    'BOGZ1FL163170005Q', # Nonprofit organizations; trade payables; liability
    'DULIPLBSHNO', # Life insurance companies, general accounts; deferred and unpaid life insurance premiums; asset
    'TNWBSHNO', # Households and nonprofit organizations; net worth
    'ASIRAL', # All sectors; IRAs; liability
    'HNOA529P', # Households and nonprofit organizations; assets in 529 plans
    'HNOA529SP', # Households and nonprofit organizations; assets in 529 savings plans
    'HNOA529PPP', # Households and nonprofit organizations; assets in 529 pre-paid plans
    'BOGZ1LM155012605Q', # Households and nonprofit organizations; residential structures, current cost basis
    'BOGZ1LM155012665Q', # Households; residential structures, current cost basis
    'BOGZ1LM165012665Q', # Nonprofit organizations; residential structures, current cost basis
    'BOGZ1LM165013665Q', # Nonprofit organizations; nonresidential structures, current cost basis
    'HNODPI', # Households and nonprofit organizations; disposable personal income
    'HNONWPDPI', # Households and nonprofit organizations; net worth as a percentage of disposable personal income
    'OEHRENWBSHNO', # Households; owners' equity in real estate
    'HOEREPHRE', # Households; owners' equity in real estate as a percentage of household real estate

]
