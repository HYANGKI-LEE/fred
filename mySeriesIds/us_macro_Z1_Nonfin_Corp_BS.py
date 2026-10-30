# FRED > Z.1 Financial Accounts > Table S11.1.b Nonfinancial corporate business (release 52, element 1256247)
# https://fred.stlouisfed.org/release/tables?rid=52&eid=1256247  비금융기업 대차대조표 59줄 전체 (예전 표 번호 B.103, macro-dashboard용)
# 원표 https://www.federalreserve.gov/releases/z1/current/html/S11_1_b.htm  (연준 원표는 십억 달러, FRED 는 백만 달러)
# 위계: # 표 > ## 단위 (계절조정)
dir='us_macro_Z1_Nonfin_Corp_BS'

# Quarterly (59)
ids_Q = [
    # S11.1.b (59)
    ## Mil. of $ (NSA) / % (줄 48~50)
    'TABSNNCB', # Nonfinancial corporate business; total assets
    'BOGZ1LM102010005Q', # Nonfinancial corporate business; nonfinancial assets
    'NCBREMV', # Nonfinancial corporate business; real estate at market value
    'BOGZ1LM105015205Q', # Nonfinancial corporate business; equipment, current cost basis
    'BOGZ1LM105013765Q', # Nonfinancial corporate business; nonresidential intellectual property products, current cost basis
    'BOGZ1LM105020015Q', # Nonfinancial corporate business; inventories excluding IVA, current cost basis
    'TFAABSNNCB', # Nonfinancial corporate business; total financial assets
    'BOGZ1FL103020005Q', # Nonfinancial corporate business; checkable deposits and currency; asset
    'TSDABSNNCB', # Nonfinancial corporate business; total time and savings deposits; asset
    'FDABSNNCB', # Nonfinancial corporate business; private foreign deposits; asset
    'BOGZ1LM104022005Q', # Nonfinancial corporate business; debt securities; asset
    'CPABSNNCB', # Nonfinancial corporate business; commercial paper; asset
    'BOGZ1LM103061103Q', # Nonfinancial corporate business; Treasury securities; asset
    'BOGZ1LM103061703Q', # Nonfinancial corporate business; agency- and GSE-backed securities; asset
    'BOGZ1LM103062003Q', # Nonfinancial corporate business; municipal securities; asset
    'BOGZ1LM123063003Q', # Equity real estate investment trusts; corporate and foreign bonds; asset
    'NCBTLSQ027S', # Nonfinancial corporate business; total loans; asset
    'SRPSABSNNCB', # Nonfinancial corporate business; security repurchase agreements; asset
    'CCABSNNCB', # Nonfinancial corporate business; consumer credit; asset
    'BOGZ1FL103065005Q', # Nonfinancial corporate business; total mortgages; asset
    'BOGZ1LM103064103Q', # Nonfinancial corporate business; corporate equities; asset
    'BOGZ1LM103092105Q', # Nonfinancial corporate business; U.S. direct investment abroad: equity; asset (market value)
    'NCBMTSQ027S', # Nonfinancial corporate business; equity in Fannie Mae and Farm Credit System; asset
    'BOGZ1FL103034000Q', # Nonfinancial corporate business; money market fund shares; asset
    'NCBMFSA', # Nonfinancial corporate business; mutual fund shares; asset
    'TRABSNNCB', # Nonfinancial corporate business; trade receivables; asset
    'BOGZ1LM103092305Q', # Nonfinancial corporate business; U.S. direct investment abroad: intercompany debt (market value)
    'MAABSNNCB', # Nonfinancial corporate business; total miscellaneous assets
    'NCBLEYQ027S', # Nonfinancial corporate business; total liabilities and equity
    'TLBSNNCB', # Nonfinancial corporate business; total liabilities
    'NCBDBIQ027S', # Nonfinancial corporate business; debt securities; liability
    'CPLBSNNCB', # Nonfinancial corporate business; commercial paper; liability
    'MSLBSNNCB', # Nonfinancial corporate business; municipal securities; liability
    'BOGZ1FL103163005Q', # Nonfinancial corporate business; corporate bonds; liability
    'NCBLILQ027S', # Nonfinancial corporate business; total loans; liability
    'BLNECLBSNNCB', # Nonfinancial corporate business; depository institution loans n.e.c.; liability
    'BOGZ1FL103167205Q', # Nonfinancial corporate business; private credit loans; liability
    'OLALBSNNCB', # Nonfinancial corporate business; other loans and advances; liability
    'MLBSNNCB', # Nonfinancial corporate business; total mortgages; liability
    'TPLBSNNCB', # Nonfinancial corporate business; trade payables; liability
    'BOGZ1FL103178005Q', # Nonfinancial corporate business; total taxes payable; liability
    'BOGZ1LM103192305Q', # Nonfinancial corporate business; foreign direct investment in U.S.: intercompany debt; liability (market value)
    'MLLBSNNCB', # Nonfinancial corporate business; total miscellaneous liabilities
    'BOGZ1LM103181105Q', # Nonfinancial corporate business; total equity; liability (IMA)
    'NCBCEL', # Nonfinancial corporate business; corporate equities; liability
    'BOGZ1LM103192105Q', # Nonfinancial corporate business; foreign direct investment in U.S.; liability (market value)
    'TNWMVBSNNCB', # Nonfinancial corporate business; net worth
    'NCBCEPNW', # Nonfinancial corporate business; corporate equities as a percentage of net worth
    'NCBCMDPMVCE', # Nonfinancial corporate business; debt as a percentage of the market value of corporate equities
    'NCBCMDPNWMV', # Nonfinancial corporate business; debt as a percentage of net worth (market value)
    'TATASHCBSNNCB', # Nonfinancial corporate business; total assets at historical cost
    'TTAATASHCBSHNNCB', # Nonfinancial corporate business; nonfinancial assets at historical cost
    'REATASHCBSNNCB', # Nonfinancial corporate business; real estate, historical cost basis
    'ESATASHCBSNNCB', # Nonfinancial corporate business; nonresidential equipment, historical cost basis
    'NCBNIPPHCB', # Nonfinancial corporate business; nonresidential intellectual property products, historical cost basis
    'IATASHCBSNNCB', # Nonfinancial corporate business; inventories, historical cost basis (SOI)
    'TNWHCBSNNCB', # Nonfinancial corporate business; net worth at historical cost
    'HCVSRNWCHBSNNCB', # Nonfinancial corporate business; residential structures, historical cost basis
    'HCVSNNWHCBSNNCB', # Nonfinancial corporate business; nonresidential structures, historical cost basis

]
