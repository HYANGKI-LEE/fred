
# FRED > Release 22: H.8 Assets and Liabilities of Commercial Banks in the United States
# https://fred.stlouisfed.org/release?rid=22  (중단된 시리즈 포함 전체)
# 위계: # 은행 유형 > ## 잔액(계절조정/원계열)·증가율 > ### 항목
dir='us_macro_banks'
release_ids = [22]  # build_db.py가 이 release의 메타데이터를 일괄 조회

# Weekly (670)
ids_W = [
    # All Commercial Banks (134)
    ## 잔액 (Bil. of U.S. $, 계절조정)
    ### Bank Credit
    'TOTBKCR', # Bank Credit, All Commercial Banks
    ### Borrowings
    'BOWACBW027SBOG', # Borrowings, All Commercial Banks (DISCONTINUED)
    ### Borrowings from Banks in the U.S.
    'BBUACBW027SBOG', # Borrowings from Banks in the U.S., All Commercial Banks (DISCONTINUED)
    ### Borrowings from Others
    'BFOACBW027SBOG', # Borrowings from Others, All Commercial Banks (DISCONTINUED)
    ### Cash Assets
    'CASACBW027SBOG', # Cash Assets, All Commercial Banks
    ### Commercial and Industrial Loans
    'TOTCI', # Commercial and Industrial Loans, All Commercial Banks
    ### Commercial and Industrial Loans to U.S. Addressees
    'CIUACBW027SBOG', # Commercial and Industrial Loans to U.S. Addressees, All Commercial Banks (DISCONTINUED)
    ### Consumer Loans
    'CLSACBW027SBOG', # Consumer Loans, All Commercial Banks
    'CCLACBW027SBOG', # Consumer Loans: Credit Cards and Other Revolving Plans, All Commercial Banks
    'OCLACBW027SBOG', # Consumer Loans: Other Consumer Loans, All Commercial Banks
    'AOCACBW027SBOG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, All Commercial Banks (DISCONTINUED)
    'CARACBW027SBOG', # Consumer Loans: Other Consumer Loans: Automobile Loans, All Commercial Banks
    ### Deposits
    'DPSACBW027SBOG', # Deposits, All Commercial Banks
    ### Derivatives with a Negative Fair Value
    'DNVACBW027SBOG', # Derivatives with a Negative Fair Value, All Commercial Banks (DISCONTINUED)
    ### Derivatives with a Positive Fair Value
    'DFVACBW027SBOG', # Derivatives with a Positive Fair Value, All Commercial Banks (DISCONTINUED)
    ### Fed Funds and Reverse RPs with Banks
    'FRPACBW027SBOG', # Fed Funds and Reverse RPs with Banks, All Commercial Banks (DISCONTINUED)
    ### Interbank Loans
    'IBLACBW027SBOG', # Interbank Loans, All Commercial Banks (DISCONTINUED)
    ### Allowance for Credit Losses on Loans and Leases
    'ALLACBW027SBOG', # LESS: Allowance for Credit Losses on Loans and Leases, All Commercial Banks
    ### Large Time Deposits
    'LTDACBW027SBOG', # Large Time Deposits, All Commercial Banks
    ### Loans Secured by Nonfarm Nonresidential Properties
    'NNPACBW027SBOG', # Loans Secured by Nonfarm Nonresidential Properties, All Commercial Banks (DISCONTINUED)
    ### Loans and Leases in Bank Credit
    'TOTLL', # Loans and Leases in Bank Credit, All Commercial Banks
    ### Loans to Commercial Banks
    'LCBACBW027SBOG', # Loans to Commercial Banks, All Commercial Banks
    ### Loans with Original Amounts of $1,000,000 or Less
    'LLMACBW027SBOG', # Loans with Original Amounts of $1,000,000 or Less, All Commercial Banks (DISCONTINUED)
    ### Net Due to Related Foreign Offices
    'NDFACBW027SBOG', # Net Due to Related Foreign Offices, All Commercial Banks
    ### Net Unrealized Gains (Losses) on Available-for-Sale Securities
    'NUGACBW027SBOG', # Net Unrealized Gains (Losses) on Available-for-Sale Securities, All Commercial Banks (DISCONTINUED)
    ### Other Assets
    'OATACBW027SBOG', # Other Assets, All Commercial Banks (DISCONTINUED)
    ### Other Deposits
    'ODSACBW027SBOG', # Other Deposits, All Commercial Banks
    ### Other Liabilities
    'OLSACBW027SBOG', # Other Liabilities, All Commercial Banks (DISCONTINUED)
    ### Other Loans and Leases
    'OLLACBW027SBOG', # Other Loans and Leases, All Commercial Banks (DISCONTINUED)
    'AOLACBW027SBOG', # Other Loans and Leases: All Other Loans and Leases, All Commercial Banks
    'LNFACBW027SBOG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, All Commercial Banks
    'OLNACBW027SBOG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, All Commercial Banks (DISCONTINUED)
    'OLRACBW027SBOG', # Other Loans and Leases: Fed Funds and Reverse RPs with Nonbanks, All Commercial Banks (DISCONTINUED)
    ### Other Securities
    'OSEACBW027SBOG', # Other Securities, All Commercial Banks
    'OMBACBW027SBOG', # Other Securities: Mortgage-Backed Securities, All Commercial Banks
    'ONMACBW027SBOG', # Other Securities: Non-MBS, All Commercial Banks
    ### Other Securitized Consumer Loans
    'OSCACBW027SBOG', # Other Securitized Consumer Loans, All Commercial Banks (DISCONTINUED)
    ### Other Trading Assets
    'OTAACBW027SBOG', # Other Trading Assets, All Commercial Banks (DISCONTINUED)
    ### Other Trading Liabilities
    'OTLACBW027SBOG', # Other Trading Liabilities, All Commercial Banks (DISCONTINUED)
    ### Real Estate Loans
    'RELACBW027SBOG', # Real Estate Loans, All Commercial Banks
    'CREACBW027SBOG', # Real Estate Loans: Commercial Real Estate Loans, All Commercial Banks
    'CLDACBW027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, All Commercial Banks
    'SBFACBW027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, All Commercial Banks
    'SMPACBW027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, All Commercial Banks
    'SNFACBW027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, All Commercial Banks
    'RREACBW027SBOG', # Real Estate Loans: Residential Real Estate Loans, All Commercial Banks
    'CRLACBW027SBOG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, All Commercial Banks
    'RHEACBW027SBOG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, All Commercial Banks
    ### Residual (Assets Less Liabilities)
    'RALACBW027SBOG', # Residual (Assets Less Liabilities), All Commercial Banks
    ### Securities in Bank Credit
    'SBCACBW027SBOG', # Securities in Bank Credit, All Commercial Banks
    ### Securitized Consumer Loans
    'SCLACBW027SBOG', # Securitized Consumer Loans, All Commercial Banks (DISCONTINUED)
    ### Securitized Credit Cards and Other Revolving Plans
    'SCCACBW027SBOG', # Securitized Credit Cards and Other Revolving Plans, All Commercial Banks (DISCONTINUED)
    ### Securitized Real Estate Loans
    'SREACBW027SBOG', # Securitized Real Estate Loans, All Commercial Banks (DISCONTINUED)
    ### Total Assets
    'TLAACBW027SBOG', # Total Assets, All Commercial Banks
    ### Total Liabilities
    'TLBACBW027SBOG', # Total Liabilities, All Commercial Banks
    ### Trading Assets
    'TDAACBW027SBOG', # Trading Assets, All Commercial Banks (DISCONTINUED)
    ### Trading Liabilities
    'TLSACBW027SBOG', # Trading Liabilities, All Commercial Banks (DISCONTINUED)
    ### Treasury and Agency Securities
    'TASACBW027SBOG', # Treasury and Agency Securities, All Commercial Banks
    'TMBACBW027SBOG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), All Commercial Banks
    'TNMACBW027SBOG', # Treasury and Agency Securities: Non-MBS, All Commercial Banks
    ### U.S. Treasury and Agency Securities, MBS
    'TAMACBW027SBOG', # U.S. Treasury and Agency Securities, MBS, All Commercial Banks (DISCONTINUED)
    ## 잔액 (Mil. of U.S. $, 계절조정)
    ### Borrowings
    'H8B3094NCBA', # Borrowings, All Commercial Banks
    ### Consumer Loans
    'B2245NCBA', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, All Commercial Banks
    ### Other Assets
    'H8B3053NCBA', # Other Assets, All Commercial Banks
    ### Other Liabilities
    'H8B3095NCBA', # Other Liabilities, All Commercial Banks
    ### Other Loans and Leases
    'B2310NCBA', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, All Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NCBA', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, All Commercial Banks
    ## 잔액 (Bil. of U.S. $, 원계열)
    ### Bank Credit
    'TOTBKCRNSA', # Bank Credit, All Commercial Banks
    ### Borrowings
    'BOWACBW027NBOG', # Borrowings, All Commercial Banks (DISCONTINUED)
    ### Borrowings from Banks in the U.S.
    'BBUACBW027NBOG', # Borrowings from Banks in the U.S., All Commercial Banks (DISCONTINUED)
    ### Borrowings from Others
    'BFOACBW027NBOG', # Borrowings from Others, All Commercial Banks (DISCONTINUED)
    ### Cash Assets
    'CASACBW027NBOG', # Cash Assets, All Commercial Banks
    ### Commercial and Industrial Loans
    'TOTCINSA', # Commercial and Industrial Loans, All Commercial Banks
    ### Commercial and Industrial Loans to U.S. Addressees
    'CIUACBW027NBOG', # Commercial and Industrial Loans to U.S. Addressees, All Commercial Banks (DISCONTINUED)
    ### Consumer Loans
    'CLSACBW027NBOG', # Consumer Loans, All Commercial Banks
    'CCLACBW027NBOG', # Consumer Loans: Credit Cards and Other Revolving Plans, All Commercial Banks
    'OCLACBW027NBOG', # Consumer Loans: Other Consumer Loans, All Commercial Banks
    'AOCACBW027NBOG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, All Commercial Banks (DISCONTINUED)
    'CARACBW027NBOG', # Consumer Loans: Other Consumer Loans: Automobile Loans, All Commercial Banks
    ### Deposits
    'DPSACBW027NBOG', # Deposits, All Commercial Banks
    ### Derivatives with a Negative Fair Value
    'DNVACBW027NBOG', # Derivatives with a Negative Fair Value, All Commercial Banks (DISCONTINUED)
    ### Derivatives with a Positive Fair Value
    'DFVACBW027NBOG', # Derivatives with a Positive Fair Value, All Commercial Banks (DISCONTINUED)
    ### Fed Funds and Reverse RPs with Banks
    'FRPACBW027NBOG', # Fed Funds and Reverse RPs with Banks, All Commercial Banks (DISCONTINUED)
    ### Interbank Loans
    'IBLACBW027NBOG', # Interbank Loans, All Commercial Banks (DISCONTINUED)
    ### Allowance for Credit Losses on Loans and Leases
    'ALLACBW027NBOG', # LESS: Allowance for Credit Losses on Loans and Leases, All Commercial Banks
    ### Large Time Deposits
    'LTDACBW027NBOG', # Large Time Deposits, All Commercial Banks
    ### Loans Secured by Nonfarm Nonresidential Properties
    'NNPACBW027NBOG', # Loans Secured by Nonfarm Nonresidential Properties, All Commercial Banks (DISCONTINUED)
    ### Loans and Leases in Bank Credit
    'TOTLLNSA', # Loans and Leases in Bank Credit, All Commercial Banks
    ### Loans to Commercial Banks
    'LCBACBW027NBOG', # Loans to Commercial Banks, All Commercial Banks
    ### Loans with Original Amounts of $1,000,000 or Less
    'LLMACBW027NBOG', # Loans with Original Amounts of $1,000,000 or Less, All Commercial Banks (DISCONTINUED)
    ### Net Due to Related Foreign Offices
    'NDFACBW027NBOG', # Net Due to Related Foreign Offices, All Commercial Banks
    ### Net Unrealized Gains (Losses) on Available-for-Sale Securities
    'NUGACBW027NBOG', # Net Unrealized Gains (Losses) on Available-for-Sale Securities, All Commercial Banks (DISCONTINUED)
    ### Other Assets
    'OATACBW027NBOG', # Other Assets, All Commercial Banks (DISCONTINUED)
    ### Other Deposits
    'ODSACBW027NBOG', # Other Deposits, All Commercial Banks
    ### Other Liabilities
    'OLSACBW027NBOG', # Other Liabilities, All Commercial Banks (DISCONTINUED)
    ### Other Loans and Leases
    'OLLACBW027NBOG', # Other Loans and Leases, All Commercial Banks (DISCONTINUED)
    'AOLACBW027NBOG', # Other Loans and Leases: All Other Loans and Leases, All Commercial Banks
    'LNFACBW027NBOG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, All Commercial Banks
    'OLNACBW027NBOG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, All Commercial Banks (DISCONTINUED)
    'OLRACBW027NBOG', # Other Loans and Leases: Fed Funds and Reverse RPs with Nonbanks, All Commercial Banks (DISCONTINUED)
    ### Other Securities
    'OSEACBW027NBOG', # Other Securities, All Commercial Banks
    'OMBACBW027NBOG', # Other Securities: Mortgage-Backed Securities, All Commercial Banks
    'ONMACBW027NBOG', # Other Securities: Non-MBS, All Commercial Banks
    ### Other Securitized Consumer Loans
    'OSCACBW027NBOG', # Other Securitized Consumer Loans, All Commercial Banks (DISCONTINUED)
    ### Other Trading Assets
    'OTAACBW027NBOG', # Other Trading Assets, All Commercial Banks (DISCONTINUED)
    ### Other Trading Liabilities
    'OTLACBW027NBOG', # Other Trading Liabilities, All Commercial Banks (DISCONTINUED)
    ### Real Estate Loans
    'RELACBW027NBOG', # Real Estate Loans, All Commercial Banks
    'CREACBW027NBOG', # Real Estate Loans: Commercial Real Estate Loans, All Commercial Banks
    'CLDACBW027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, All Commercial Banks
    'SBFACBW027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, All Commercial Banks
    'SMPACBW027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, All Commercial Banks
    'SNFACBW027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, All Commercial Banks
    'RREACBW027NBOG', # Real Estate Loans: Residential Real Estate Loans, All Commercial Banks
    'CRLACBW027NBOG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, All Commercial Banks
    'RHEACBW027NBOG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, All Commercial Banks
    ### Residual (Assets Less Liabilities)
    'RALACBW027NBOG', # Residual (Assets Less Liabilities), All Commercial Banks
    ### Securities in Bank Credit
    'SBCACBW027NBOG', # Securities in Bank Credit, All Commercial Banks
    ### Securitized Consumer Loans
    'SCLACBW027NBOG', # Securitized Consumer Loans, All Commercial Banks (DISCONTINUED)
    ### Securitized Credit Cards and Other Revolving Plans
    'SCCACBW027NBOG', # Securitized Credit Cards and Other Revolving Plans, All Commercial Banks (DISCONTINUED)
    ### Securitized Real Estate Loans
    'SREACBW027NBOG', # Securitized Real Estate Loans, All Commercial Banks (DISCONTINUED)
    ### Total Assets
    'TLAACBW027NBOG', # Total Assets, All Commercial Banks
    ### Total Liabilities
    'TLBACBW027NBOG', # Total Liabilities, All Commercial Banks
    ### Trading Assets
    'TDAACBW027NBOG', # Trading Assets, All Commercial Banks (DISCONTINUED)
    ### Trading Liabilities
    'TLSACBW027NBOG', # Trading Liabilities, All Commercial Banks (DISCONTINUED)
    ### Treasury and Agency Securities
    'TASACBW027NBOG', # Treasury and Agency Securities, All Commercial Banks
    'TMBACBW027NBOG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), All Commercial Banks
    'TNMACBW027NBOG', # Treasury and Agency Securities: Non-MBS, All Commercial Banks
    ### U.S. Treasury and Agency Securities, MBS
    'TAMACBW027NBOG', # U.S. Treasury and Agency Securities, MBS, All Commercial Banks (DISCONTINUED)
    ## 잔액 (Mil. of U.S. $, 원계열)
    ### Borrowings
    'H8B3094NCBD', # Borrowings, All Commercial Banks
    ### Consumer Loans
    'B2245NCBD', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, All Commercial Banks
    ### Other Assets
    'H8B3053NCBD', # Other Assets, All Commercial Banks
    ### Other Liabilities
    'H8B3095NCBD', # Other Liabilities, All Commercial Banks
    ### Other Loans and Leases
    'B2310NCBD', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, All Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NCBD', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, All Commercial Banks

    # Domestically Chartered Commercial Banks (134)
    ## 잔액 (Bil. of U.S. $, 계절조정)
    ### Bank Credit
    'BC0DCBW027SBOG', # Bank Credit, Domestically Chartered Commercial Banks
    ### Borrowings
    'BOWDCBW027SBOG', # Borrowings, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Borrowings from Banks in the U.S.
    'BBUDCBW027SBOG', # Borrowings from Banks in the U.S., Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Borrowings from Others
    'BFODCBW027SBOG', # Borrowings from Others, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Cash Assets
    'CASDCBW027SBOG', # Cash Assets, Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans
    'CILDCBW027SBOG', # Commercial and Industrial Loans, Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans to U.S. Addressees
    'CIUDCBW027SBOG', # Commercial and Industrial Loans to U.S. Addressees, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Consumer Loans
    'CLSDCBW027SBOG', # Consumer Loans, Domestically Chartered Commercial Banks
    'CCLDCBW027SBOG', # Consumer Loans: Credit Cards and Other Revolving Plans, Domestically Chartered Commercial Banks
    'OCLDCBW027SBOG', # Consumer Loans: Other Consumer Loans, Domestically Chartered Commercial Banks
    'AOCDCBW027SBOG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Domestically Chartered Commercial Banks (DISCONTINUED)
    'CARDCBW027SBOG', # Consumer Loans: Other Consumer Loans: Automobile Loans, Domestically Chartered Commercial Banks
    ### Deposits
    'DPSDCBW027SBOG', # Deposits, Domestically Chartered Commercial Banks
    ### Derivatives with a Negative Fair Value
    'DNVDCBW027SBOG', # Derivatives with a Negative Fair Value, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Derivatives with a Positive Fair Value
    'DFVDCBW027SBOG', # Derivatives with a Positive Fair Value, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Fed Funds and Reverse RPs with Banks
    'FRPDCBW027SBOG', # Fed Funds and Reverse RPs with Banks, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Interbank Loans
    'IBLDCBW027SBOG', # Interbank Loans, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Allowance for Credit Losses on Loans and Leases
    'ALLDCBW027SBOG', # LESS: Allowance for Credit Losses on Loans and Leases, Domestically Chartered Commercial Banks
    ### Large Time Deposits
    'LTDDCBW027SBOG', # Large Time Deposits, Domestically Chartered Commercial Banks
    ### Loans Secured by Nonfarm Nonresidential Properties
    'NNPDCBW027SBOG', # Loans Secured by Nonfarm Nonresidential Properties, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Loans and Leases in Bank Credit
    'LLBDCBW027SBOG', # Loans and Leases in Bank Credit, Domestically Chartered Commercial Banks
    ### Loans to Commercial Banks
    'LCBDCBW027SBOG', # Loans to Commercial Banks, Domestically Chartered Commercial Banks
    ### Loans with Original Amounts of $1,000,000 or Less
    'LLMDCBW027SBOG', # Loans with Original Amounts of $1,000,000 or Less, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Net Due to Related Foreign Offices
    'NDFDCBW027SBOG', # Net Due to Related Foreign Offices, Domestically Chartered Commercial Banks
    ### Net Unrealized Gains (Losses) on Available-for-Sale Securities
    'NUGDCBW027SBOG', # Net Unrealized Gains (Losses) on Available-for-Sale Securities, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Assets
    'OATDCBW027SBOG', # Other Assets, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Deposits
    'ODSDCBW027SBOG', # Other Deposits, Domestically Chartered Commercial Banks
    ### Other Liabilities
    'OLSDCBW027SBOG', # Other Liabilities, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Loans and Leases
    'OLLDCBW027SBOG', # Other Loans and Leases, Domestically Chartered Commercial Banks (DISCONTINUED)
    'AOLDCBW027SBOG', # Other Loans and Leases: All Other Loans and Leases, Domestically Chartered Commercial Banks
    'LNFDCBW027SBOG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Domestically Chartered Commercial Banks
    'OLNDCBW027SBOG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Domestically Chartered Commercial Banks (DISCONTINUED)
    'OLRDCBW027SBOG', # Other Loans and Leases: Fed Funds and Reverse RPs with Nonbanks, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Securities
    'OSEDCBW027SBOG', # Other Securities, Domestically Chartered Commercial Banks
    'OMBDCBW027SBOG', # Other Securities: Mortgage-Backed Securities, Domestically Chartered Commercial Banks
    'ONMDCBW027SBOG', # Other Securities: Non-MBS, Domestically Chartered Commercial Banks
    ### Other Securitized Consumer Loans
    'OSCDCBW027SBOG', # Other Securitized Consumer Loans, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Trading Assets
    'OTADCBW027SBOG', # Other Trading Assets, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Trading Liabilities
    'OTLDCBW027SBOG', # Other Trading Liabilities, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Real Estate Loans
    'RELDCBW027SBOG', # Real Estate Loans, Domestically Chartered Commercial Banks
    'CREDCBW027SBOG', # Real Estate Loans: Commercial Real Estate Loans, Domestically Chartered Commercial Banks
    'CLDDCBW027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Domestically Chartered Commercial Banks
    'SBFDCBW027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Domestically Chartered Commercial Banks
    'SMPDCBW027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Domestically Chartered Commercial Banks
    'SNFDCBW027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Domestically Chartered Commercial Banks
    'RREDCBW027SBOG', # Real Estate Loans: Residential Real Estate Loans, Domestically Chartered Commercial Banks
    'CRLDCBW027SBOG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Domestically Chartered Commercial Banks
    'RHEDCBW027SBOG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Domestically Chartered Commercial Banks
    ### Residual (Assets Less Liabilities)
    'RALDCBW027SBOG', # Residual (Assets Less Liabilities), Domestically Chartered Commercial Banks
    ### Securities in Bank Credit
    'SBCDCBW027SBOG', # Securities in Bank Credit, Domestically Chartered Commercial Banks
    ### Securitized Consumer Loans
    'SCLDCBW027SBOG', # Securitized Consumer Loans, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Securitized Credit Cards and Other Revolving Plans
    'SCCDCBW027SBOG', # Securitized Credit Cards and Other Revolving Plans, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Securitized Real Estate Loans
    'SREDCBW027SBOG', # Securitized Real Estate Loans, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Total Assets
    'TLADCBW027SBOG', # Total Assets, Domestically Chartered Commercial Banks
    ### Total Liabilities
    'TLBDCBW027SBOG', # Total Liabilities, Domestically Chartered Commercial Banks
    ### Trading Assets
    'TDADCBW027SBOG', # Trading Assets, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Trading Liabilities
    'TLSDCBW027SBOG', # Trading Liabilities, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Treasury and Agency Securities
    'TASDCBW027SBOG', # Treasury and Agency Securities, Domestically Chartered Commercial Banks
    'TMBDCBW027SBOG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Domestically Chartered Commercial Banks
    'TNMDCBW027SBOG', # Treasury and Agency Securities: Non-MBS, Domestically Chartered Commercial Banks
    ### U.S. Treasury and Agency Securities, MBS
    'TAMDCBW027SBOG', # U.S. Treasury and Agency Securities, MBS, Domestically Chartered Commercial Banks (DISCONTINUED)
    ## 잔액 (Mil. of U.S. $, 계절조정)
    ### Borrowings
    'H8B3094NDMA', # Borrowings, Domestically Chartered Commercial Banks
    ### Consumer Loans
    'B2245NDMA', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Domestically Chartered Commercial Banks
    ### Other Assets
    'H8B3053NDMA', # Other Assets, Domestically Chartered Commercial Banks
    ### Other Liabilities
    'H8B3095NDMA', # Other Liabilities, Domestically Chartered Commercial Banks
    ### Other Loans and Leases
    'B2310NDMA', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Domestically Chartered Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NDMA', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Domestically Chartered Commercial Banks
    ## 잔액 (Bil. of U.S. $, 원계열)
    ### Bank Credit
    'BC0DCBW027NBOG', # Bank Credit, Domestically Chartered Commercial Banks
    ### Borrowings
    'BOWDCBW027NBOG', # Borrowings, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Borrowings from Banks in the U.S.
    'BBUDCBW027NBOG', # Borrowings from Banks in the U.S., Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Borrowings from Others
    'BFODCBW027NBOG', # Borrowings from Others, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Cash Assets
    'CASDCBW027NBOG', # Cash Assets, Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans
    'CILDCBW027NBOG', # Commercial and Industrial Loans, Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans to U.S. Addressees
    'CIUDCBW027NBOG', # Commercial and Industrial Loans to U.S. Addressees, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Consumer Loans
    'CLSDCBW027NBOG', # Consumer Loans, Domestically Chartered Commercial Banks
    'CCLDCBW027NBOG', # Consumer Loans: Credit Cards and Other Revolving Plans, Domestically Chartered Commercial Banks
    'OCLDCBW027NBOG', # Consumer Loans: Other Consumer Loans, Domestically Chartered Commercial Banks
    'AOCDCBW027NBOG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Domestically Chartered Commercial Banks (DISCONTINUED)
    'CARDCBW027NBOG', # Consumer Loans: Other Consumer Loans: Automobile Loans, Domestically Chartered Commercial Banks
    ### Deposits
    'DPSDCBW027NBOG', # Deposits, Domestically Chartered Commercial Banks
    ### Derivatives with a Negative Fair Value
    'DNVDCBW027NBOG', # Derivatives with a Negative Fair Value, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Derivatives with a Positive Fair Value
    'DFVDCBW027NBOG', # Derivatives with a Positive Fair Value, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Fed Funds and Reverse RPs with Banks
    'FRPDCBW027NBOG', # Fed Funds and Reverse RPs with Banks, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Interbank Loans
    'IBLDCBW027NBOG', # Interbank Loans, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Allowance for Credit Losses on Loans and Leases
    'ALLDCBW027NBOG', # LESS: Allowance for Credit Losses on Loans and Leases, Domestically Chartered Commercial Banks
    ### Large Time Deposits
    'LTDDCBW027NBOG', # Large Time Deposits, Domestically Chartered Commercial Banks
    ### Loans Secured by Nonfarm Nonresidential Properties
    'NNPDCBW027NBOG', # Loans Secured by Nonfarm Nonresidential Properties, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Loans and Leases in Bank Credit
    'LLBDCBW027NBOG', # Loans and Leases in Bank Credit, Domestically Chartered Commercial Banks
    ### Loans to Commercial Banks
    'LCBDCBW027NBOG', # Loans to Commercial Banks, Domestically Chartered Commercial Banks
    ### Loans with Original Amounts of $1,000,000 or Less
    'LLMDCBW027NBOG', # Loans with Original Amounts of $1,000,000 or Less, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Net Due to Related Foreign Offices
    'NDFDCBW027NBOG', # Net Due to Related Foreign Offices, Domestically Chartered Commercial Banks
    ### Net Unrealized Gains (Losses) on Available-for-Sale Securities
    'NUGDCBW027NBOG', # Net Unrealized Gains (Losses) on Available-for-Sale Securities, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Assets
    'OATDCBW027NBOG', # Other Assets, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Deposits
    'ODSDCBW027NBOG', # Other Deposits, Domestically Chartered Commercial Banks
    ### Other Liabilities
    'OLSDCBW027NBOG', # Other Liabilities, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Loans and Leases
    'OLLDCBW027NBOG', # Other Loans and Leases, Domestically Chartered Commercial Banks (DISCONTINUED)
    'AOLDCBW027NBOG', # Other Loans and Leases: All Other Loans and Leases, Domestically Chartered Commercial Banks
    'LNFDCBW027NBOG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Domestically Chartered Commercial Banks
    'OLNDCBW027NBOG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Domestically Chartered Commercial Banks (DISCONTINUED)
    'OLRDCBW027NBOG', # Other Loans and Leases: Fed Funds and Reverse RPs with Nonbanks, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Securities
    'OSEDCBW027NBOG', # Other Securities, Domestically Chartered Commercial Banks
    'OMBDCBW027NBOG', # Other Securities: Mortgage-Backed Securities, Domestically Chartered Commercial Banks
    'ONMDCBW027NBOG', # Other Securities: Non-MBS, Domestically Chartered Commercial Banks
    ### Other Securitized Consumer Loans
    'OSCDCBW027NBOG', # Other Securitized Consumer Loans, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Trading Assets
    'OTADCBW027NBOG', # Other Trading Assets, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Trading Liabilities
    'OTLDCBW027NBOG', # Other Trading Liabilities, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Real Estate Loans
    'RELDCBW027NBOG', # Real Estate Loans, Domestically Chartered Commercial Banks
    'CREDCBW027NBOG', # Real Estate Loans: Commercial Real Estate Loans, Domestically Chartered Commercial Banks
    'CLDDCBW027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Domestically Chartered Commercial Banks
    'SBFDCBW027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Domestically Chartered Commercial Banks
    'SMPDCBW027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Domestically Chartered Commercial Banks
    'SNFDCBW027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Domestically Chartered Commercial Banks
    'RREDCBW027NBOG', # Real Estate Loans: Residential Real Estate Loans, Domestically Chartered Commercial Banks
    'CRLDCBW027NBOG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Domestically Chartered Commercial Banks
    'RHEDCBW027NBOG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Domestically Chartered Commercial Banks
    ### Residual (Assets Less Liabilities)
    'RALDCBW027NBOG', # Residual (Assets Less Liabilities), Domestically Chartered Commercial Banks
    ### Securities in Bank Credit
    'SBCDCBW027NBOG', # Securities in Bank Credit, Domestically Chartered Commercial Banks
    ### Securitized Consumer Loans
    'SCLDCBW027NBOG', # Securitized Consumer Loans, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Securitized Credit Cards and Other Revolving Plans
    'SCCDCBW027NBOG', # Securitized Credit Cards and Other Revolving Plans, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Securitized Real Estate Loans
    'SREDCBW027NBOG', # Securitized Real Estate Loans, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Total Assets
    'TLADCBW027NBOG', # Total Assets, Domestically Chartered Commercial Banks
    ### Total Liabilities
    'TLBDCBW027NBOG', # Total Liabilities, Domestically Chartered Commercial Banks
    ### Trading Assets
    'TDADCBW027NBOG', # Trading Assets, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Trading Liabilities
    'TLSDCBW027NBOG', # Trading Liabilities, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Treasury and Agency Securities
    'TASDCBW027NBOG', # Treasury and Agency Securities, Domestically Chartered Commercial Banks
    'TMBDCBW027NBOG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Domestically Chartered Commercial Banks
    'TNMDCBW027NBOG', # Treasury and Agency Securities: Non-MBS, Domestically Chartered Commercial Banks
    ### U.S. Treasury and Agency Securities, MBS
    'TAMDCBW027NBOG', # U.S. Treasury and Agency Securities, MBS, Domestically Chartered Commercial Banks (DISCONTINUED)
    ## 잔액 (Mil. of U.S. $, 원계열)
    ### Borrowings
    'H8B3094NDMD', # Borrowings, Domestically Chartered Commercial Banks
    ### Consumer Loans
    'B2245NDMD', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Domestically Chartered Commercial Banks
    ### Other Assets
    'H8B3053NDMD', # Other Assets, Domestically Chartered Commercial Banks
    ### Other Liabilities
    'H8B3095NDMD', # Other Liabilities, Domestically Chartered Commercial Banks
    ### Other Loans and Leases
    'B2310NDMD', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Domestically Chartered Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NDMD', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Domestically Chartered Commercial Banks

    # Large Domestically Chartered Commercial Banks (134)
    ## 잔액 (Bil. of U.S. $, 계절조정)
    ### Bank Credit
    'BC0LCBW027SBOG', # Bank Credit, Large Domestically Chartered Commercial Banks
    ### Borrowings
    'BOWLCBW027SBOG', # Borrowings, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Borrowings from Banks in the U.S.
    'BBULCBW027SBOG', # Borrowings from Banks in the U.S., Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Borrowings from Others
    'BFOLCBW027SBOG', # Borrowings from Others, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Cash Assets
    'CASLCBW027SBOG', # Cash Assets, Large Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans
    'CIBOARD', # Commercial and Industrial Loans, Large Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans to U.S. Addressees
    'CIULCBW027SBOG', # Commercial and Industrial Loans to U.S. Addressees, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Consumer Loans
    'CLSLCBW027SBOG', # Consumer Loans, Large Domestically Chartered Commercial Banks
    'CCLLCBW027SBOG', # Consumer Loans: Credit Cards and Other Revolving Plans, Large Domestically Chartered Commercial Banks
    'OCLLCBW027SBOG', # Consumer Loans: Other Consumer Loans, Large Domestically Chartered Commercial Banks
    'AOCLCBW027SBOG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    'CARLCBW027SBOG', # Consumer Loans: Other Consumer Loans: Automobile Loans, Large Domestically Chartered Commercial Banks
    ### Deposits
    'DPSLCBW027SBOG', # Deposits, Large Domestically Chartered Commercial Banks
    ### Derivatives with a Negative Fair Value
    'DNVLCBW027SBOG', # Derivatives with a Negative Fair Value, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Derivatives with a Positive Fair Value
    'DFVLCBW027SBOG', # Derivatives with a Positive Fair Value, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Fed Funds and Reverse RPs with Banks
    'FRPLCBW027SBOG', # Fed Funds and Reverse RPs with Banks, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Interbank Loans
    'IBLLCBW027SBOG', # Interbank Loans, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Allowance for Credit Losses on Loans and Leases
    'ALLLCBW027SBOG', # LESS: Allowance for Credit Losses on Loans and Leases, Large Domestically Chartered Commercial Banks
    ### Large Time Deposits
    'LTDLCBW027SBOG', # Large Time Deposits, Large Domestically Chartered Commercial Banks
    ### Loans Secured by Nonfarm Nonresidential Properties
    'NNPLCBW027SBOG', # Loans Secured by Nonfarm Nonresidential Properties, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Loans and Leases in Bank Credit
    'LLBLCBW027SBOG', # Loans and Leases in Bank Credit, Large Domestically Chartered Commercial Banks
    ### Loans to Commercial Banks
    'LCBLCBW027SBOG', # Loans to Commercial Banks, Large Domestically Chartered Commercial Banks
    ### Loans with Original Amounts of $1,000,000 or Less
    'LLMLCBW027SBOG', # Loans with Original Amounts of $1,000,000 or Less, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Net Due to Related Foreign Offices
    'NDFLCBW027SBOG', # Net Due to Related Foreign Offices, Large Domestically Chartered Commercial Banks
    ### Net Unrealized Gains (Losses) on Available-for-Sale Securities
    'NUGLCBW027SBOG', # Net Unrealized Gains (Losses) on Available-for-Sale Securities, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Assets
    'OATLCBW027SBOG', # Other Assets, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Deposits
    'ODSLCBW027SBOG', # Other Deposits, Large Domestically Chartered Commercial Banks
    ### Other Liabilities
    'OLSLCBW027SBOG', # Other Liabilities, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Loans and Leases
    'OLLLCBW027SBOG', # Other Loans and Leases, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    'AOLLCBW027SBOG', # Other Loans and Leases: All Other Loans and Leases, Large Domestically Chartered Commercial Banks
    'LNFLCBW027SBOG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Large Domestically Chartered Commercial Banks
    'OLNLCBW027SBOG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    'OLRLCBW027SBOG', # Other Loans and Leases: Fed Funds and Reverse RPs with Nonbanks, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Securities
    'OSELCBW027SBOG', # Other Securities, Large Domestically Chartered Commercial Banks
    'OMBLCBW027SBOG', # Other Securities: Mortgage-Backed Securities, Large Domestically Chartered Commercial Banks
    'ONMLCBW027SBOG', # Other Securities: Non-MBS, Large Domestically Chartered Commercial Banks
    ### Other Securitized Consumer Loans
    'OSCLCBW027SBOG', # Other Securitized Consumer Loans, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Trading Assets
    'OTALCBW027SBOG', # Other Trading Assets, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Trading Liabilities
    'OTLLCBW027SBOG', # Other Trading Liabilities, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Real Estate Loans
    'RELLCBW027SBOG', # Real Estate Loans, Large Domestically Chartered Commercial Banks
    'CRELCBW027SBOG', # Real Estate Loans: Commercial Real Estate Loans, Large Domestically Chartered Commercial Banks
    'CLDLCBW027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Large Domestically Chartered Commercial Banks
    'SBFLCBW027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Large Domestically Chartered Commercial Banks
    'SMPLCBW027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Large Domestically Chartered Commercial Banks
    'SNFLCBW027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Large Domestically Chartered Commercial Banks
    'RRELCBW027SBOG', # Real Estate Loans: Residential Real Estate Loans, Large Domestically Chartered Commercial Banks
    'CRLLCBW027SBOG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Large Domestically Chartered Commercial Banks
    'RHELCBW027SBOG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Large Domestically Chartered Commercial Banks
    ### Residual (Assets Less Liabilities)
    'RALLCBW027SBOG', # Residual (Assets Less Liabilities), Large Domestically Chartered Commercial Banks
    ### Securities in Bank Credit
    'SBCLCBW027SBOG', # Securities in Bank Credit, Large Domestically Chartered Commercial Banks
    ### Securitized Consumer Loans
    'SCLLCBW027SBOG', # Securitized Consumer Loans, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Securitized Credit Cards and Other Revolving Plans
    'SCCLCBW027SBOG', # Securitized Credit Cards and Other Revolving Plans, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Securitized Real Estate Loans
    'SRELCBW027SBOG', # Securitized Real Estate Loans, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Total Assets
    'TLALCBW027SBOG', # Total Assets, Large Domestically Chartered Commercial Banks
    ### Total Liabilities
    'TLBLCBW027SBOG', # Total Liabilities, Large Domestically Chartered Commercial Banks
    ### Trading Assets
    'TDALCBW027SBOG', # Trading Assets, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Trading Liabilities
    'TLSLCBW027SBOG', # Trading Liabilities, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Treasury and Agency Securities
    'TASLCBW027SBOG', # Treasury and Agency Securities, Large Domestically Chartered Commercial Banks
    'TMBLCBW027SBOG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Large Domestically Chartered Commercial Banks
    'TNMLCBW027SBOG', # Treasury and Agency Securities: Non-MBS, Large Domestically Chartered Commercial Banks
    ### U.S. Treasury and Agency Securities, MBS
    'TAMLCBW027SBOG', # U.S. Treasury and Agency Securities, MBS, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ## 잔액 (Mil. of U.S. $, 계절조정)
    ### Borrowings
    'H8B3094NLGA', # Borrowings, Large Domestically Chartered Commercial Banks
    ### Consumer Loans
    'B2245NLGA', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Large Domestically Chartered Commercial Banks
    ### Other Assets
    'H8B3053NLGA', # Other Assets, Large Domestically Chartered Commercial Banks
    ### Other Liabilities
    'H8B3095NLGA', # Other Liabilities, Large Domestically Chartered Commercial Banks
    ### Other Loans and Leases
    'B2310NLGA', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Large Domestically Chartered Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NLGA', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Large Domestically Chartered Commercial Banks
    ## 잔액 (Bil. of U.S. $, 원계열)
    ### Bank Credit
    'BC0LCBW027NBOG', # Bank Credit, Large Domestically Chartered Commercial Banks
    ### Borrowings
    'BOWLCBW027NBOG', # Borrowings, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Borrowings from Banks in the U.S.
    'BBULCBW027NBOG', # Borrowings from Banks in the U.S., Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Borrowings from Others
    'BFOLCBW027NBOG', # Borrowings from Others, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Cash Assets
    'CASLCBW027NBOG', # Cash Assets, Large Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans
    'CIBOARDNSA', # Commercial and Industrial Loans, Large Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans to U.S. Addressees
    'CIULCBW027NBOG', # Commercial and Industrial Loans to U.S. Addressees, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Consumer Loans
    'CLSLCBW027NBOG', # Consumer Loans, Large Domestically Chartered Commercial Banks
    'CCLLCBW027NBOG', # Consumer Loans: Credit Cards and Other Revolving Plans, Large Domestically Chartered Commercial Banks
    'OCLLCBW027NBOG', # Consumer Loans: Other Consumer Loans, Large Domestically Chartered Commercial Banks
    'AOCLCBW027NBOG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    'CARLCBW027NBOG', # Consumer Loans: Other Consumer Loans: Automobile Loans, Large Domestically Chartered Commercial Banks
    ### Deposits
    'DPSLCBW027NBOG', # Deposits, Large Domestically Chartered Commercial Banks
    ### Derivatives with a Negative Fair Value
    'DNVLCBW027NBOG', # Derivatives with a Negative Fair Value, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Derivatives with a Positive Fair Value
    'DFVLCBW027NBOG', # Derivatives with a Positive Fair Value, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Fed Funds and Reverse RPs with Banks
    'FRPLCBW027NBOG', # Fed Funds and Reverse RPs with Banks, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Interbank Loans
    'IBLLCBW027NBOG', # Interbank Loans, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Allowance for Credit Losses on Loans and Leases
    'ALLLCBW027NBOG', # LESS: Allowance for Credit Losses on Loans and Leases, Large Domestically Chartered Commercial Banks
    ### Large Time Deposits
    'LTDLCBW027NBOG', # Large Time Deposits, Large Domestically Chartered Commercial Banks
    ### Loans Secured by Nonfarm Nonresidential Properties
    'NNPLCBW027NBOG', # Loans Secured by Nonfarm Nonresidential Properties, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Loans and Leases in Bank Credit
    'LLBLCBW027NBOG', # Loans and Leases in Bank Credit, Large Domestically Chartered Commercial Banks
    ### Loans to Commercial Banks
    'LCBLCBW027NBOG', # Loans to Commercial Banks, Large Domestically Chartered Commercial Banks
    ### Loans with Original Amounts of $1,000,000 or Less
    'LLMLCBW027NBOG', # Loans with Original Amounts of $1,000,000 or Less, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Net Due to Related Foreign Offices
    'NDFLCBW027NBOG', # Net Due to Related Foreign Offices, Large Domestically Chartered Commercial Banks
    ### Net Unrealized Gains (Losses) on Available-for-Sale Securities
    'NUGLCBW027NBOG', # Net Unrealized Gains (Losses) on Available-for-Sale Securities, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Assets
    'OATLCBW027NBOG', # Other Assets, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Deposits
    'ODSLCBW027NBOG', # Other Deposits, Large Domestically Chartered Commercial Banks
    ### Other Liabilities
    'OLSLCBW027NBOG', # Other Liabilities, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Loans and Leases
    'OLLLCBW027NBOG', # Other Loans and Leases, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    'AOLLCBW027NBOG', # Other Loans and Leases: All Other Loans and Leases, Large Domestically Chartered Commercial Banks
    'LNFLCBW027NBOG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Large Domestically Chartered Commercial Banks
    'OLNLCBW027NBOG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    'OLRLCBW027NBOG', # Other Loans and Leases: Fed Funds and Reverse RPs with Nonbanks, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Securities
    'OSELCBW027NBOG', # Other Securities, Large Domestically Chartered Commercial Banks
    'OMBLCBW027NBOG', # Other Securities: Mortgage-Backed Securities, Large Domestically Chartered Commercial Banks
    'ONMLCBW027NBOG', # Other Securities: Non-MBS, Large Domestically Chartered Commercial Banks
    ### Other Securitized Consumer Loans
    'OSCLCBW027NBOG', # Other Securitized Consumer Loans, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Trading Assets
    'OTALCBW027NBOG', # Other Trading Assets, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Trading Liabilities
    'OTLLCBW027NBOG', # Other Trading Liabilities, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Real Estate Loans
    'RELLCBW027NBOG', # Real Estate Loans, Large Domestically Chartered Commercial Banks
    'CRELCBW027NBOG', # Real Estate Loans: Commercial Real Estate Loans, Large Domestically Chartered Commercial Banks
    'CLDLCBW027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Large Domestically Chartered Commercial Banks
    'SBFLCBW027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Large Domestically Chartered Commercial Banks
    'SMPLCBW027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Large Domestically Chartered Commercial Banks
    'SNFLCBW027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Large Domestically Chartered Commercial Banks
    'RRELCBW027NBOG', # Real Estate Loans: Residential Real Estate Loans, Large Domestically Chartered Commercial Banks
    'CRLLCBW027NBOG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Large Domestically Chartered Commercial Banks
    'RHELCBW027NBOG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Large Domestically Chartered Commercial Banks
    ### Residual (Assets Less Liabilities)
    'RALLCBW027NBOG', # Residual (Assets Less Liabilities), Large Domestically Chartered Commercial Banks
    ### Securities in Bank Credit
    'SBCLCBW027NBOG', # Securities in Bank Credit, Large Domestically Chartered Commercial Banks
    ### Securitized Consumer Loans
    'SCLLCBW027NBOG', # Securitized Consumer Loans, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Securitized Credit Cards and Other Revolving Plans
    'SCCLCBW027NBOG', # Securitized Credit Cards and Other Revolving Plans, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Securitized Real Estate Loans
    'SRELCBW027NBOG', # Securitized Real Estate Loans, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Total Assets
    'TLALCBW027NBOG', # Total Assets, Large Domestically Chartered Commercial Banks
    ### Total Liabilities
    'TLBLCBW027NBOG', # Total Liabilities, Large Domestically Chartered Commercial Banks
    ### Trading Assets
    'TDALCBW027NBOG', # Trading Assets, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Trading Liabilities
    'TLSLCBW027NBOG', # Trading Liabilities, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Treasury and Agency Securities
    'TASLCBW027NBOG', # Treasury and Agency Securities, Large Domestically Chartered Commercial Banks
    'TMBLCBW027NBOG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Large Domestically Chartered Commercial Banks
    'TNMLCBW027NBOG', # Treasury and Agency Securities: Non-MBS, Large Domestically Chartered Commercial Banks
    ### U.S. Treasury and Agency Securities, MBS
    'TAMLCBW027NBOG', # U.S. Treasury and Agency Securities, MBS, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ## 잔액 (Mil. of U.S. $, 원계열)
    ### Borrowings
    'H8B3094NLGD', # Borrowings, Large Domestically Chartered Commercial Banks
    ### Consumer Loans
    'B2245NLGD', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Large Domestically Chartered Commercial Banks
    ### Other Assets
    'H8B3053NLGD', # Other Assets, Large Domestically Chartered Commercial Banks
    ### Other Liabilities
    'H8B3095NLGD', # Other Liabilities, Large Domestically Chartered Commercial Banks
    ### Other Loans and Leases
    'B2310NLGD', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Large Domestically Chartered Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NLGD', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Large Domestically Chartered Commercial Banks

    # Small Domestically Chartered Commercial Banks (134)
    ## 잔액 (Bil. of U.S. $, 계절조정)
    ### Bank Credit
    'BC0SCBW027SBOG', # Bank Credit, Small Domestically Chartered Commercial Banks
    ### Borrowings
    'BOWSCBW027SBOG', # Borrowings, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Borrowings from Banks in the U.S.
    'BBUSCBW027SBOG', # Borrowings from Banks in the U.S., Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Borrowings from Others
    'BFOSCBW027SBOG', # Borrowings from Others, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Cash Assets
    'CASSCBW027SBOG', # Cash Assets, Small Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans
    'CILSCBW027SBOG', # Commercial and Industrial Loans, Small Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans to U.S. Addressees
    'CIUSCBW027SBOG', # Commercial and Industrial Loans to U.S. Addressees, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Consumer Loans
    'CLSSCBW027SBOG', # Consumer Loans, Small Domestically Chartered Commercial Banks
    'CCLSCBW027SBOG', # Consumer Loans: Credit Cards and Other Revolving Plans, Small Domestically Chartered Commercial Banks
    'OCLSCBW027SBOG', # Consumer Loans: Other Consumer Loans, Small Domestically Chartered Commercial Banks
    'AOCSCBW027SBOG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    'CARSCBW027SBOG', # Consumer Loans: Other Consumer Loans: Automobile Loans, Small Domestically Chartered Commercial Banks
    ### Deposits
    'DPSSCBW027SBOG', # Deposits, Small Domestically Chartered Commercial Banks
    ### Derivatives with a Negative Fair Value
    'DNVSCBW027SBOG', # Derivatives with a Negative Fair Value, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Derivatives with a Positive Fair Value
    'DFVSCBW027SBOG', # Derivatives with a Positive Fair Value, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Fed Funds and Reverse RPs with Banks
    'FRPSCBW027SBOG', # Fed Funds and Reverse RPs with Banks, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Interbank Loans
    'IBLSCBW027SBOG', # Interbank Loans, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Allowance for Credit Losses on Loans and Leases
    'ALLSCBW027SBOG', # LESS: Allowance for Credit Losses on Loans and Leases, Small Domestically Chartered Commercial Banks
    ### Large Time Deposits
    'LTDSCBW027SBOG', # Large Time Deposits, Small Domestically Chartered Commercial Banks
    ### Loans Secured by Nonfarm Nonresidential Properties
    'NNPSCBW027SBOG', # Loans Secured by Nonfarm Nonresidential Properties, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Loans and Leases in Bank Credit
    'LLBSCBW027SBOG', # Loans and Leases in Bank Credit, Small Domestically Chartered Commercial Banks
    ### Loans to Commercial Banks
    'LCBSCBW027SBOG', # Loans to Commercial Banks, Small Domestically Chartered Commercial Banks
    ### Loans with Original Amounts of $1,000,000 or Less
    'LLMSCBW027SBOG', # Loans with Original Amounts of $1,000,000 or Less, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Net Due to Related Foreign Offices
    'NDFSCBW027SBOG', # Net Due to Related Foreign Offices, Small Domestically Chartered Commercial Banks
    ### Net Unrealized Gains (Losses) on Available-for-Sale Securities
    'NUGSCBW027SBOG', # Net Unrealized Gains (Losses) on Available-for-Sale Securities, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Assets
    'OATSCBW027SBOG', # Other Assets, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Deposits
    'ODSSCBW027SBOG', # Other Deposits, Small Domestically Chartered Commercial Banks
    ### Other Liabilities
    'OLSSCBW027SBOG', # Other Liabilities, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Loans and Leases
    'OLLSCBW027SBOG', # Other Loans and Leases, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    'AOLSCBW027SBOG', # Other Loans and Leases: All Other Loans and Leases, Small Domestically Chartered Commercial Banks
    'LNFSCBW027SBOG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Small Domestically Chartered Commercial Banks
    'OLNSCBW027SBOG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    'OLRSCBW027SBOG', # Other Loans and Leases: Fed Funds and Reverse RPs with Nonbanks, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Securities
    'OSESCBW027SBOG', # Other Securities, Small Domestically Chartered Commercial Banks
    'OMBSCBW027SBOG', # Other Securities: Mortgage-Backed Securities, Small Domestically Chartered Commercial Banks
    'ONMSCBW027SBOG', # Other Securities: Non-MBS, Small Domestically Chartered Commercial Banks
    ### Other Securitized Consumer Loans
    'OSCSCBW027SBOG', # Other Securitized Consumer Loans, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Trading Assets
    'OTASCBW027SBOG', # Other Trading Assets, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Trading Liabilities
    'OTLSCBW027SBOG', # Other Trading Liabilities, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Real Estate Loans
    'RELSCBW027SBOG', # Real Estate Loans, Small Domestically Chartered Commercial Banks
    'CRESCBW027SBOG', # Real Estate Loans: Commercial Real Estate Loans, Small Domestically Chartered Commercial Banks
    'CLDSCBW027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Small Domestically Chartered Commercial Banks
    'SBFSCBW027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Small Domestically Chartered Commercial Banks
    'SMPSCBW027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Small Domestically Chartered Commercial Banks
    'SNFSCBW027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Small Domestically Chartered Commercial Banks
    'RRESCBW027SBOG', # Real Estate Loans: Residential Real Estate Loans, Small Domestically Chartered Commercial Banks
    'CRLSCBW027SBOG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Small Domestically Chartered Commercial Banks
    'RHESCBW027SBOG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Small Domestically Chartered Commercial Banks
    ### Residual (Assets Less Liabilities)
    'RALSCBW027SBOG', # Residual (Assets Less Liabilities), Small Domestically Chartered Commercial Banks
    ### Securities in Bank Credit
    'SBCSCBW027SBOG', # Securities in Bank Credit, Small Domestically Chartered Commercial Banks
    ### Securitized Consumer Loans
    'SCLSCBW027SBOG', # Securitized Consumer Loans, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Securitized Credit Cards and Other Revolving Plans
    'SCCSCBW027SBOG', # Securitized Credit Cards and Other Revolving Plans, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Securitized Real Estate Loans
    'SRESCBW027SBOG', # Securitized Real Estate Loans, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Total Assets
    'TLASCBW027SBOG', # Total Assets, Small Domestically Chartered Commercial Banks
    ### Total Liabilities
    'TLBSCBW027SBOG', # Total Liabilities, Small Domestically Chartered Commercial Banks
    ### Trading Assets
    'TDASCBW027SBOG', # Trading Assets, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Trading Liabilities
    'TLSSCBW027SBOG', # Trading Liabilities, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Treasury and Agency Securities
    'TASSCBW027SBOG', # Treasury and Agency Securities, Small Domestically Chartered Commercial Banks
    'TMBSCBW027SBOG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Small Domestically Chartered Commercial Banks
    'TNMSCBW027SBOG', # Treasury and Agency Securities: Non-MBS, Small Domestically Chartered Commercial Banks
    ### U.S. Treasury and Agency Securities, MBS
    'TAMSCBW027SBOG', # U.S. Treasury and Agency Securities, MBS, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ## 잔액 (Mil. of U.S. $, 계절조정)
    ### Borrowings
    'H8B3094NSMA', # Borrowings, Small Domestically Chartered Commercial Banks
    ### Consumer Loans
    'B2245NSMA', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Small Domestically Chartered Commercial Banks
    ### Other Assets
    'H8B3053NSMA', # Other Assets, Small Domestically Chartered Commercial Banks
    ### Other Liabilities
    'H8B3095NSMA', # Other Liabilities, Small Domestically Chartered Commercial Banks
    ### Other Loans and Leases
    'B2310NSMA', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Small Domestically Chartered Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NSMA', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Small Domestically Chartered Commercial Banks
    ## 잔액 (Bil. of U.S. $, 원계열)
    ### Bank Credit
    'BC0SCBW027NBOG', # Bank Credit, Small Domestically Chartered Commercial Banks
    ### Borrowings
    'BOWSCBW027NBOG', # Borrowings, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Borrowings from Banks in the U.S.
    'BBUSCBW027NBOG', # Borrowings from Banks in the U.S., Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Borrowings from Others
    'BFOSCBW027NBOG', # Borrowings from Others, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Cash Assets
    'CASSCBW027NBOG', # Cash Assets, Small Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans
    'CILSCBW027NBOG', # Commercial and Industrial Loans, Small Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans to U.S. Addressees
    'CIUSCBW027NBOG', # Commercial and Industrial Loans to U.S. Addressees, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Consumer Loans
    'CLSSCBW027NBOG', # Consumer Loans, Small Domestically Chartered Commercial Banks
    'CCLSCBW027NBOG', # Consumer Loans: Credit Cards and Other Revolving Plans, Small Domestically Chartered Commercial Banks
    'OCLSCBW027NBOG', # Consumer Loans: Other Consumer Loans, Small Domestically Chartered Commercial Banks
    'AOCSCBW027NBOG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    'CARSCBW027NBOG', # Consumer Loans: Other Consumer Loans: Automobile Loans, Small Domestically Chartered Commercial Banks
    ### Deposits
    'DPSSCBW027NBOG', # Deposits, Small Domestically Chartered Commercial Banks
    ### Derivatives with a Negative Fair Value
    'DNVSCBW027NBOG', # Derivatives with a Negative Fair Value, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Derivatives with a Positive Fair Value
    'DFVSCBW027NBOG', # Derivatives with a Positive Fair Value, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Fed Funds and Reverse RPs with Banks
    'FRPSCBW027NBOG', # Fed Funds and Reverse RPs with Banks, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Interbank Loans
    'IBLSCBW027NBOG', # Interbank Loans, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Allowance for Credit Losses on Loans and Leases
    'ALLSCBW027NBOG', # LESS: Allowance for Credit Losses on Loans and Leases, Small Domestically Chartered Commercial Banks
    ### Large Time Deposits
    'LTDSCBW027NBOG', # Large Time Deposits, Small Domestically Chartered Commercial Banks
    ### Loans Secured by Nonfarm Nonresidential Properties
    'NNPSCBW027NBOG', # Loans Secured by Nonfarm Nonresidential Properties, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Loans and Leases in Bank Credit
    'LLBSCBW027NBOG', # Loans and Leases in Bank Credit, Small Domestically Chartered Commercial Banks
    ### Loans to Commercial Banks
    'LCBSCBW027NBOG', # Loans to Commercial Banks, Small Domestically Chartered Commercial Banks
    ### Loans with Original Amounts of $1,000,000 or Less
    'LLMSCBW027NBOG', # Loans with Original Amounts of $1,000,000 or Less, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Net Due to Related Foreign Offices
    'NDFSCBW027NBOG', # Net Due to Related Foreign Offices, Small Domestically Chartered Commercial Banks
    ### Net Unrealized Gains (Losses) on Available-for-Sale Securities
    'NUGSCBW027NBOG', # Net Unrealized Gains (Losses) on Available-for-Sale Securities, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Assets
    'OATSCBW027NBOG', # Other Assets, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Deposits
    'ODSSCBW027NBOG', # Other Deposits, Small Domestically Chartered Commercial Banks
    ### Other Liabilities
    'OLSSCBW027NBOG', # Other Liabilities, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Loans and Leases
    'OLLSCBW027NBOG', # Other Loans and Leases, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    'AOLSCBW027NBOG', # Other Loans and Leases: All Other Loans and Leases, Small Domestically Chartered Commercial Banks
    'LNFSCBW027NBOG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Small Domestically Chartered Commercial Banks
    'OLNSCBW027NBOG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    'OLRSCBW027NBOG', # Other Loans and Leases: Fed Funds and Reverse RPs with Nonbanks, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Securities
    'OSESCBW027NBOG', # Other Securities, Small Domestically Chartered Commercial Banks
    'OMBSCBW027NBOG', # Other Securities: Mortgage-Backed Securities, Small Domestically Chartered Commercial Banks
    'ONMSCBW027NBOG', # Other Securities: Non-MBS, Small Domestically Chartered Commercial Banks
    ### Other Securitized Consumer Loans
    'OSCSCBW027NBOG', # Other Securitized Consumer Loans, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Trading Assets
    'OTASCBW027NBOG', # Other Trading Assets, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Trading Liabilities
    'OTLSCBW027NBOG', # Other Trading Liabilities, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Real Estate Loans
    'RELSCBW027NBOG', # Real Estate Loans, Small Domestically Chartered Commercial Banks
    'CRESCBW027NBOG', # Real Estate Loans: Commercial Real Estate Loans, Small Domestically Chartered Commercial Banks
    'CLDSCBW027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Small Domestically Chartered Commercial Banks
    'SBFSCBW027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Small Domestically Chartered Commercial Banks
    'SMPSCBW027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Small Domestically Chartered Commercial Banks
    'SNFSCBW027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Small Domestically Chartered Commercial Banks
    'RRESCBW027NBOG', # Real Estate Loans: Residential Real Estate Loans, Small Domestically Chartered Commercial Banks
    'CRLSCBW027NBOG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Small Domestically Chartered Commercial Banks
    'RHESCBW027NBOG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Small Domestically Chartered Commercial Banks
    ### Residual (Assets Less Liabilities)
    'RALSCBW027NBOG', # Residual (Assets Less Liabilities), Small Domestically Chartered Commercial Banks
    ### Securities in Bank Credit
    'SBCSCBW027NBOG', # Securities in Bank Credit, Small Domestically Chartered Commercial Banks
    ### Securitized Consumer Loans
    'SCLSCBW027NBOG', # Securitized Consumer Loans, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Securitized Credit Cards and Other Revolving Plans
    'SCCSCBW027NBOG', # Securitized Credit Cards and Other Revolving Plans, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Securitized Real Estate Loans
    'SRESCBW027NBOG', # Securitized Real Estate Loans, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Total Assets
    'TLASCBW027NBOG', # Total Assets, Small Domestically Chartered Commercial Banks
    ### Total Liabilities
    'TLBSCBW027NBOG', # Total Liabilities, Small Domestically Chartered Commercial Banks
    ### Trading Assets
    'TDASCBW027NBOG', # Trading Assets, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Trading Liabilities
    'TLSSCBW027NBOG', # Trading Liabilities, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Treasury and Agency Securities
    'TASSCBW027NBOG', # Treasury and Agency Securities, Small Domestically Chartered Commercial Banks
    'TMBSCBW027NBOG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Small Domestically Chartered Commercial Banks
    'TNMSCBW027NBOG', # Treasury and Agency Securities: Non-MBS, Small Domestically Chartered Commercial Banks
    ### U.S. Treasury and Agency Securities, MBS
    'TAMSCBW027NBOG', # U.S. Treasury and Agency Securities, MBS, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ## 잔액 (Mil. of U.S. $, 원계열)
    ### Borrowings
    'H8B3094NSMD', # Borrowings, Small Domestically Chartered Commercial Banks
    ### Consumer Loans
    'B2245NSMD', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Small Domestically Chartered Commercial Banks
    ### Other Assets
    'H8B3053NSMD', # Other Assets, Small Domestically Chartered Commercial Banks
    ### Other Liabilities
    'H8B3095NSMD', # Other Liabilities, Small Domestically Chartered Commercial Banks
    ### Other Loans and Leases
    'B2310NSMD', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Small Domestically Chartered Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NSMD', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Small Domestically Chartered Commercial Banks

    # Foreign-Related Institutions (134)
    ## 잔액 (Bil. of U.S. $, 계절조정)
    ### Bank Credit
    'BC0FRIW027SBOG', # Bank Credit, Foreign-Related Institutions
    ### Borrowings
    'BOWFRIW027SBOG', # Borrowings, Foreign-Related Institutions (DISCONTINUED)
    ### Borrowings from Banks in the U.S.
    'BBUFRIW027SBOG', # Borrowings from Banks in the U.S., Foreign-Related Institutions (DISCONTINUED)
    ### Borrowings from Others
    'BFOFRIW027SBOG', # Borrowings from Others, Foreign-Related Institutions (DISCONTINUED)
    ### Cash Assets
    'CASFRIW027SBOG', # Cash Assets, Foreign-Related Institutions
    ### Commercial and Industrial Loans
    'CILFRIW027SBOG', # Commercial and Industrial Loans, Foreign-Related Institutions
    ### Commercial and Industrial Loans to U.S. Addressees
    'CIUFRIW027SBOG', # Commercial and Industrial Loans to U.S. Addressees, Foreign-Related Institutions (DISCONTINUED)
    ### Consumer Loans
    'CLSFRIW027SBOG', # Consumer Loans, Foreign-Related Institutions
    'CCLFRIW027SBOG', # Consumer Loans: Credit Cards and Other Revolving Plans, Foreign-Related Institutions
    'OCLFRIW027SBOG', # Consumer Loans: Other Consumer Loans, Foreign-Related Institutions
    'AOCFRIW027SBOG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Foreign-Related Institutions (DISCONTINUED)
    'CARFRIW027SBOG', # Consumer Loans: Other Consumer Loans: Automobile Loans, Foreign-Related Institutions
    ### Deposits
    'DPSFRIW027SBOG', # Deposits, Foreign-Related Institutions
    ### Derivatives with a Negative Fair Value
    'DNVFRIW027SBOG', # Derivatives with a Negative Fair Value, Foreign-Related Institutions (DISCONTINUED)
    ### Derivatives with a Positive Fair Value
    'DFVFRIW027SBOG', # Derivatives with a Positive Fair Value, Foreign-Related Institutions (DISCONTINUED)
    ### Fed Funds and Reverse RPs with Banks
    'FRPFRIW027SBOG', # Fed Funds and Reverse RPs with Banks, Foreign-Related Institutions (DISCONTINUED)
    ### Interbank Loans
    'IBLFRIW027SBOG', # Interbank Loans, Foreign-Related Institutions (DISCONTINUED)
    ### Allowance for Credit Losses on Loans and Leases
    'ALLFRIW027SBOG', # LESS: Allowance for Credit Losses on Loans and Leases, Foreign-Related Institutions
    ### Large Time Deposits
    'LTDFRIW027SBOG', # Large Time Deposits, Foreign-Related Institutions
    ### Loans Secured by Nonfarm Nonresidential Properties
    'NNPFRIW027SBOG', # Loans Secured by Nonfarm Nonresidential Properties, Foreign-Related Institutions (DISCONTINUED)
    ### Loans and Leases in Bank Credit
    'LLBFRIW027SBOG', # Loans and Leases in Bank Credit, Foreign-Related Institutions
    ### Loans to Commercial Banks
    'LCBFRIW027SBOG', # Loans to Commercial Banks, Foreign-Related Institutions
    ### Loans with Original Amounts of $1,000,000 or Less
    'LLMFRIW027SBOG', # Loans with Original Amounts of $1,000,000 or Less, Foreign-Related Institutions (DISCONTINUED)
    ### Net Due to Related Foreign Offices
    'NDFFRIW027SBOG', # Net Due to Related Foreign Offices, Foreign-Related Institutions
    ### Net Unrealized Gains (Losses) on Available-for-Sale Securities
    'NUGFRIW027SBOG', # Net Unrealized Gains (Losses) on Available-for-Sale Securities, Foreign-Related Institutions (DISCONTINUED)
    ### Other Assets
    'OATFRIW027SBOG', # Other Assets, Foreign-Related Institutions (DISCONTINUED)
    ### Other Deposits
    'ODSFRIW027SBOG', # Other Deposits, Foreign-Related Institutions
    ### Other Liabilities
    'OLSFRIW027SBOG', # Other Liabilities, Foreign-Related Institutions (DISCONTINUED)
    ### Other Loans and Leases
    'OLLFRIW027SBOG', # Other Loans and Leases, Foreign-Related Institutions (DISCONTINUED)
    'AOLFRIW027SBOG', # Other Loans and Leases: All Other Loans and Leases, Foreign-Related Institutions
    'LNFFRIW027SBOG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Foreign-Related Institutions
    'OLNFRIW027SBOG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Foreign-Related Institutions (DISCONTINUED)
    'OLRFRIW027SBOG', # Other Loans and Leases: Fed Funds and Reverse RPs with Nonbanks, Foreign-Related Institutions (DISCONTINUED)
    ### Other Securities
    'OSEFRIW027SBOG', # Other Securities, Foreign-Related Institutions
    'OMBFRIW027SBOG', # Other Securities: Mortgage-Backed Securities, Foreign-Related Institutions
    'ONMFRIW027SBOG', # Other Securities: Non-MBS, Foreign-Related Institutions
    ### Other Securitized Consumer Loans
    'OSCFRIW027SBOG', # Other Securitized Consumer Loans, Foreign-Related Institutions (DISCONTINUED)
    ### Other Trading Assets
    'OTAFRIW027SBOG', # Other Trading Assets, Foreign-Related Institutions (DISCONTINUED)
    ### Other Trading Liabilities
    'OTLFRIW027SBOG', # Other Trading Liabilities, Foreign-Related Institutions (DISCONTINUED)
    ### Real Estate Loans
    'RELFRIW027SBOG', # Real Estate Loans, Foreign-Related Institutions
    'CREFRIW027SBOG', # Real Estate Loans: Commercial Real Estate Loans, Foreign-Related Institutions
    'CLDFRIW027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Foreign-Related Institutions
    'SBFFRIW027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Foreign-Related Institutions
    'SMPFRIW027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Foreign-Related Institutions
    'SNFFRIW027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Foreign-Related Institutions
    'RREFRIW027SBOG', # Real Estate Loans: Residential Real Estate Loans, Foreign-Related Institutions
    'CRLFRIW027SBOG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Foreign-Related Institutions
    'RHEFRIW027SBOG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Foreign-Related Institutions
    ### Residual (Assets Less Liabilities)
    'RALFRIW027SBOG', # Residual (Assets Less Liabilities), Foreign-Related Institutions
    ### Securities in Bank Credit
    'SBCFRIW027SBOG', # Securities in Bank Credit, Foreign-Related Institutions
    ### Securitized Consumer Loans
    'SCLFRIW027SBOG', # Securitized Consumer Loans, Foreign-Related Institutions (DISCONTINUED)
    ### Securitized Credit Cards and Other Revolving Plans
    'SCCFRIW027SBOG', # Securitized Credit Cards and Other Revolving Plans, Foreign-Related Institutions (DISCONTINUED)
    ### Securitized Real Estate Loans
    'SREFRIW027SBOG', # Securitized Real Estate Loans, Foreign-Related Institutions (DISCONTINUED)
    ### Total Assets
    'TLAFRIW027SBOG', # Total Assets, Foreign-Related Institutions
    ### Total Liabilities
    'TLBFRIW027SBOG', # Total Liabilities, Foreign-Related Institutions
    ### Trading Assets
    'TDAFRIW027SBOG', # Trading Assets, Foreign-Related Institutions (DISCONTINUED)
    ### Trading Liabilities
    'TLSFRIW027SBOG', # Trading Liabilities, Foreign-Related Institutions (DISCONTINUED)
    ### Treasury and Agency Securities
    'TASFRIW027SBOG', # Treasury and Agency Securities, Foreign-Related Institutions
    'TMBFRIW027SBOG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Foreign-Related Institutions
    'TNMFRIW027SBOG', # Treasury and Agency Securities: Non-MBS, Foreign-Related Institutions
    ### U.S. Treasury and Agency Securities, MBS
    'TAMFRIW027SBOG', # U.S. Treasury and Agency Securities, MBS, Foreign-Related Institutions (DISCONTINUED)
    ## 잔액 (Mil. of U.S. $, 계절조정)
    ### Borrowings
    'H8B3094NFRA', # Borrowings, Foreign-Related Institutions
    ### Consumer Loans
    'B2245NFRA', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Foreign-Related Institutions
    ### Other Assets
    'H8B3053NFRA', # Other Assets, Foreign-Related Institutions
    ### Other Liabilities
    'H8B3095NFRA', # Other Liabilities, Foreign-Related Institutions
    ### Other Loans and Leases
    'B2310NFRA', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Foreign-Related Institutions
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NFRA', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Foreign-Related Institutions
    ## 잔액 (Bil. of U.S. $, 원계열)
    ### Bank Credit
    'BC0FRIW027NBOG', # Bank Credit, Foreign-Related Institutions
    ### Borrowings
    'BOWFRIW027NBOG', # Borrowings, Foreign-Related Institutions (DISCONTINUED)
    ### Borrowings from Banks in the U.S.
    'BBUFRIW027NBOG', # Borrowings from Banks in the U.S., Foreign-Related Institutions (DISCONTINUED)
    ### Borrowings from Others
    'BFOFRIW027NBOG', # Borrowings from Others, Foreign-Related Institutions (DISCONTINUED)
    ### Cash Assets
    'CASFRIW027NBOG', # Cash Assets, Foreign-Related Institutions
    ### Commercial and Industrial Loans
    'CILFRIW027NBOG', # Commercial and Industrial Loans, Foreign-Related Institutions
    ### Commercial and Industrial Loans to U.S. Addressees
    'CIUFRIW027NBOG', # Commercial and Industrial Loans to U.S. Addressees, Foreign-Related Institutions (DISCONTINUED)
    ### Consumer Loans
    'CLSFRIW027NBOG', # Consumer Loans, Foreign-Related Institutions
    'CCLFRIW027NBOG', # Consumer Loans: Credit Cards and Other Revolving Plans, Foreign-Related Institutions
    'OCLFRIW027NBOG', # Consumer Loans: Other Consumer Loans, Foreign-Related Institutions
    'AOCFRIW027NBOG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Foreign-Related Institutions (DISCONTINUED)
    'CARFRIW027NBOG', # Consumer Loans: Other Consumer Loans: Automobile Loans, Foreign-Related Institutions
    ### Deposits
    'DPSFRIW027NBOG', # Deposits, Foreign-Related Institutions
    ### Derivatives with a Negative Fair Value
    'DNVFRIW027NBOG', # Derivatives with a Negative Fair Value, Foreign-Related Institutions (DISCONTINUED)
    ### Derivatives with a Positive Fair Value
    'DFVFRIW027NBOG', # Derivatives with a Positive Fair Value, Foreign-Related Institutions (DISCONTINUED)
    ### Fed Funds and Reverse RPs with Banks
    'FRPFRIW027NBOG', # Fed Funds and Reverse RPs with Banks, Foreign-Related Institutions (DISCONTINUED)
    ### Interbank Loans
    'IBLFRIW027NBOG', # Interbank Loans, Foreign-Related Institutions (DISCONTINUED)
    ### Allowance for Credit Losses on Loans and Leases
    'ALLFRIW027NBOG', # LESS: Allowance for Credit Losses on Loans and Leases, Foreign-Related Institutions
    ### Large Time Deposits
    'LTDFRIW027NBOG', # Large Time Deposits, Foreign-Related Institutions
    ### Loans Secured by Nonfarm Nonresidential Properties
    'NNPFRIW027NBOG', # Loans Secured by Nonfarm Nonresidential Properties, Foreign-Related Institutions (DISCONTINUED)
    ### Loans and Leases in Bank Credit
    'LLBFRIW027NBOG', # Loans and Leases in Bank Credit, Foreign-Related Institutions
    ### Loans to Commercial Banks
    'LCBFRIW027NBOG', # Loans to Commercial Banks, Foreign-Related Institutions
    ### Loans with Original Amounts of $1,000,000 or Less
    'LLMFRIW027NBOG', # Loans with Original Amounts of $1,000,000 or Less, Foreign-Related Institutions (DISCONTINUED)
    ### Net Due to Related Foreign Offices
    'NDFFRIW027NBOG', # Net Due to Related Foreign Offices, Foreign-Related Institutions
    ### Net Unrealized Gains (Losses) on Available-for-Sale Securities
    'NUGFRIW027NBOG', # Net Unrealized Gains (Losses) on Available-for-Sale Securities, Foreign-Related Institutions (DISCONTINUED)
    ### Other Assets
    'OATFRIW027NBOG', # Other Assets, Foreign-Related Institutions (DISCONTINUED)
    ### Other Deposits
    'ODSFRIW027NBOG', # Other Deposits, Foreign-Related Institutions
    ### Other Liabilities
    'OLSFRIW027NBOG', # Other Liabilities, Foreign-Related Institutions (DISCONTINUED)
    ### Other Loans and Leases
    'OLLFRIW027NBOG', # Other Loans and Leases, Foreign-Related Institutions (DISCONTINUED)
    'AOLFRIW027NBOG', # Other Loans and Leases: All Other Loans and Leases, Foreign-Related Institutions
    'LNFFRIW027NBOG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Foreign-Related Institutions
    'OLNFRIW027NBOG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Foreign-Related Institutions (DISCONTINUED)
    'OLRFRIW027NBOG', # Other Loans and Leases: Fed Funds and Reverse RPs with Nonbanks, Foreign-Related Institutions (DISCONTINUED)
    ### Other Securities
    'OSEFRIW027NBOG', # Other Securities, Foreign-Related Institutions
    'OMBFRIW027NBOG', # Other Securities: Mortgage-Backed Securities, Foreign-Related Institutions
    'ONMFRIW027NBOG', # Other Securities: Non-MBS, Foreign-Related Institutions
    ### Other Securitized Consumer Loans
    'OSCFRIW027NBOG', # Other Securitized Consumer Loans, Foreign-Related Institutions (DISCONTINUED)
    ### Other Trading Assets
    'OTAFRIW027NBOG', # Other Trading Assets, Foreign-Related Institutions (DISCONTINUED)
    ### Other Trading Liabilities
    'OTLFRIW027NBOG', # Other Trading Liabilities, Foreign-Related Institutions (DISCONTINUED)
    ### Real Estate Loans
    'RELFRIW027NBOG', # Real Estate Loans, Foreign-Related Institutions
    'CREFRIW027NBOG', # Real Estate Loans: Commercial Real Estate Loans, Foreign-Related Institutions
    'CLDFRIW027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Foreign-Related Institutions
    'SBFFRIW027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Foreign-Related Institutions
    'SMPFRIW027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Foreign-Related Institutions
    'SNFFRIW027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Foreign-Related Institutions
    'RREFRIW027NBOG', # Real Estate Loans: Residential Real Estate Loans, Foreign-Related Institutions
    'CRLFRIW027NBOG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Foreign-Related Institutions
    'RHEFRIW027NBOG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Foreign-Related Institutions
    ### Residual (Assets Less Liabilities)
    'RALFRIW027NBOG', # Residual (Assets Less Liabilities), Foreign-Related Institutions
    ### Securities in Bank Credit
    'SBCFRIW027NBOG', # Securities in Bank Credit, Foreign-Related Institutions
    ### Securitized Consumer Loans
    'SCLFRIW027NBOG', # Securitized Consumer Loans, Foreign-Related Institutions (DISCONTINUED)
    ### Securitized Credit Cards and Other Revolving Plans
    'SCCFRIW027NBOG', # Securitized Credit Cards and Other Revolving Plans, Foreign-Related Institutions (DISCONTINUED)
    ### Securitized Real Estate Loans
    'SREFRIW027NBOG', # Securitized Real Estate Loans, Foreign-Related Institutions (DISCONTINUED)
    ### Total Assets
    'TLAFRIW027NBOG', # Total Assets, Foreign-Related Institutions
    ### Total Liabilities
    'TLBFRIW027NBOG', # Total Liabilities, Foreign-Related Institutions
    ### Trading Assets
    'TDAFRIW027NBOG', # Trading Assets, Foreign-Related Institutions (DISCONTINUED)
    ### Trading Liabilities
    'TLSFRIW027NBOG', # Trading Liabilities, Foreign-Related Institutions (DISCONTINUED)
    ### Treasury and Agency Securities
    'TASFRIW027NBOG', # Treasury and Agency Securities, Foreign-Related Institutions
    'TMBFRIW027NBOG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Foreign-Related Institutions
    'TNMFRIW027NBOG', # Treasury and Agency Securities: Non-MBS, Foreign-Related Institutions
    ### U.S. Treasury and Agency Securities, MBS
    'TAMFRIW027NBOG', # U.S. Treasury and Agency Securities, MBS, Foreign-Related Institutions (DISCONTINUED)
    ## 잔액 (Mil. of U.S. $, 원계열)
    ### Borrowings
    'H8B3094NFRD', # Borrowings, Foreign-Related Institutions
    ### Consumer Loans
    'B2245NFRD', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Foreign-Related Institutions
    ### Other Assets
    'H8B3053NFRD', # Other Assets, Foreign-Related Institutions
    ### Other Liabilities
    'H8B3095NFRD', # Other Liabilities, Foreign-Related Institutions
    ### Other Loans and Leases
    'B2310NFRD', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Foreign-Related Institutions
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NFRD', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Foreign-Related Institutions
]

# Monthly (867)
ids_M = [
    # All Commercial Banks (174)
    ## 잔액 (Bil. of U.S. $, 계절조정)
    ### Bank Credit
    'LOANINV', # Bank Credit, All Commercial Banks
    ### Borrowings
    'BOWACBM027SBOG', # Borrowings, All Commercial Banks (DISCONTINUED)
    ### Borrowings from Banks in the U.S.
    'BBUACBM027SBOG', # Borrowings from Banks in the U.S., All Commercial Banks (DISCONTINUED)
    ### Borrowings from Others
    'BFOACBM027SBOG', # Borrowings from Others, All Commercial Banks (DISCONTINUED)
    ### Cash Assets
    'CASACBM027SBOG', # Cash Assets, All Commercial Banks
    ### Commercial and Industrial Loans
    'BUSLOANS', # Commercial and Industrial Loans, All Commercial Banks
    ### Commercial and Industrial Loans to U.S. Addressees
    'CIUACBM027SBOG', # Commercial and Industrial Loans to U.S. Addressees, All Commercial Banks (DISCONTINUED)
    ### Consumer Loans
    'CONSUMER', # Consumer Loans, All Commercial Banks
    'CCLACBM027SBOG', # Consumer Loans: Credit Cards and Other Revolving Plans, All Commercial Banks
    'OCLACBM027SBOG', # Consumer Loans: Other Consumer Loans, All Commercial Banks
    'AOCACBM027SBOG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, All Commercial Banks (DISCONTINUED)
    'CARACBM027SBOG', # Consumer Loans: Other Consumer Loans: Automobile Loans, All Commercial Banks
    ### Deposits
    'DPSACBM027SBOG', # Deposits, All Commercial Banks
    ### Derivatives with a Negative Fair Value
    'DNVACBM027SBOG', # Derivatives with a Negative Fair Value, All Commercial Banks (DISCONTINUED)
    ### Derivatives with a Positive Fair Value
    'DFVACBM027SBOG', # Derivatives with a Positive Fair Value, All Commercial Banks (DISCONTINUED)
    ### Fed Funds and Reverse RPs with Banks
    'FRPACBM027SBOG', # Fed Funds and Reverse RPs with Banks, All Commercial Banks (DISCONTINUED)
    ### Interbank Loans
    'IBLACBM027SBOG', # Interbank Loans, All Commercial Banks (DISCONTINUED)
    ### Allowance for Credit Losses on Loans and Leases
    'ALLACBM027SBOG', # LESS: Allowance for Credit Losses on Loans and Leases, All Commercial Banks
    ### Large Time Deposits
    'LTDACBM027SBOG', # Large Time Deposits, All Commercial Banks
    ### Loans Secured by Nonfarm Nonresidential Properties
    'NNPACBM027SBOG', # Loans Secured by Nonfarm Nonresidential Properties, All Commercial Banks (DISCONTINUED)
    ### Loans and Leases in Bank Credit
    'LOANS', # Loans and Leases in Bank Credit, All Commercial Banks
    ### Loans to Commercial Banks
    'LCBACBM027SBOG', # Loans to Commercial Banks, All Commercial Banks
    ### Loans with Original Amounts of $1,000,000 or Less
    'LLMACBM027SBOG', # Loans with Original Amounts of $1,000,000 or Less, All Commercial Banks (DISCONTINUED)
    ### Net Due to Related Foreign Offices
    'NDFACBM027SBOG', # Net Due to Related Foreign Offices, All Commercial Banks
    ### Net Unrealized Gains (Losses) on Available-for-Sale Securities
    'NUGACBM027SBOG', # Net Unrealized Gains (Losses) on Available-for-Sale Securities, All Commercial Banks (DISCONTINUED)
    ### Other Assets
    'OATACBM027SBOG', # Other Assets, All Commercial Banks (DISCONTINUED)
    ### Other Deposits
    'ODSACBM027SBOG', # Other Deposits, All Commercial Banks
    ### Other Liabilities
    'OLSACBM027SBOG', # Other Liabilities, All Commercial Banks (DISCONTINUED)
    ### Other Loans and Leases
    'OLLACBM027SBOG', # Other Loans and Leases, All Commercial Banks (DISCONTINUED)
    'AOLACBM027SBOG', # Other Loans and Leases: All Other Loans and Leases, All Commercial Banks
    'LNFACBM027SBOG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, All Commercial Banks
    'OLNACBM027SBOG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, All Commercial Banks (DISCONTINUED)
    'OLRACBM027SBOG', # Other Loans and Leases: Fed Funds and Reverse RPs with Nonbanks, All Commercial Banks (DISCONTINUED)
    ### Other Securities
    'OTHSEC', # Other Securities, All Commercial Banks
    'OMBACBM027SBOG', # Other Securities: Mortgage-Backed Securities, All Commercial Banks
    'ONMACBM027SBOG', # Other Securities: Non-MBS, All Commercial Banks
    ### Other Securitized Consumer Loans
    'OSCACBM027SBOG', # Other Securitized Consumer Loans, All Commercial Banks (DISCONTINUED)
    ### Other Trading Assets
    'OTAACBM027SBOG', # Other Trading Assets, All Commercial Banks (DISCONTINUED)
    ### Other Trading Liabilities
    'OTLACBM027SBOG', # Other Trading Liabilities, All Commercial Banks (DISCONTINUED)
    ### Real Estate Loans
    'REALLN', # Real Estate Loans, All Commercial Banks
    'CREACBM027SBOG', # Real Estate Loans: Commercial Real Estate Loans, All Commercial Banks
    'CLDACBM027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, All Commercial Banks
    'SBFACBM027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, All Commercial Banks
    'SMPACBM027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, All Commercial Banks
    'SNFACBM027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, All Commercial Banks
    'RREACBM027SBOG', # Real Estate Loans: Residential Real Estate Loans, All Commercial Banks
    'CRLACBM027SBOG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, All Commercial Banks
    'RHEACBM027SBOG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, All Commercial Banks
    ### Residual (Assets Less Liabilities)
    'RALACBM027SBOG', # Residual (Assets Less Liabilities), All Commercial Banks
    ### Securities in Bank Credit
    'INVEST', # Securities in Bank Credit, All Commercial Banks
    ### Securitized Consumer Loans
    'SCLACBM027SBOG', # Securitized Consumer Loans, All Commercial Banks (DISCONTINUED)
    ### Securitized Credit Cards and Other Revolving Plans
    'SCCACBM027SBOG', # Securitized Credit Cards and Other Revolving Plans, All Commercial Banks (DISCONTINUED)
    ### Securitized Real Estate Loans
    'SREACBM027SBOG', # Securitized Real Estate Loans, All Commercial Banks (DISCONTINUED)
    ### Total Assets
    'TLAACBM027SBOG', # Total Assets, All Commercial Banks
    ### Total Liabilities
    'TLBACBM027SBOG', # Total Liabilities, All Commercial Banks
    ### Trading Assets
    'TDAACBM027SBOG', # Trading Assets, All Commercial Banks (DISCONTINUED)
    ### Trading Liabilities
    'TLSACBM027SBOG', # Trading Liabilities, All Commercial Banks (DISCONTINUED)
    ### Treasury and Agency Securities
    'USGSEC', # Treasury and Agency Securities, All Commercial Banks
    'TMBACBM027SBOG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), All Commercial Banks
    'TNMACBM027SBOG', # Treasury and Agency Securities: Non-MBS, All Commercial Banks
    ### U.S. Treasury and Agency Securities, MBS
    'TAMACBM027SBOG', # U.S. Treasury and Agency Securities, MBS, All Commercial Banks (DISCONTINUED)
    ## 잔액 (Mil. of U.S. $, 계절조정)
    ### Borrowings
    'H8B3094NCBAM', # Borrowings, All Commercial Banks
    ### Consumer Loans
    'B2245NCBAM', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, All Commercial Banks
    ### Other Assets
    'H8B3053NCBAM', # Other Assets, All Commercial Banks
    ### Other Liabilities
    'H8B3095NCBAM', # Other Liabilities, All Commercial Banks
    ### Other Loans and Leases
    'B2310NCBAM', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, All Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NCBAM', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, All Commercial Banks
    ## 잔액 (Bil. of U.S. $, 원계열)
    ### Bank Credit
    'LOANINVNSA', # Bank Credit, All Commercial Banks
    ### Borrowings
    'BOWACBM027NBOG', # Borrowings, All Commercial Banks (DISCONTINUED)
    ### Borrowings from Banks in the U.S.
    'BBUACBM027NBOG', # Borrowings from Banks in the U.S., All Commercial Banks (DISCONTINUED)
    ### Borrowings from Others
    'BFOACBM027NBOG', # Borrowings from Others, All Commercial Banks (DISCONTINUED)
    ### Cash Assets
    'CASACBM027NBOG', # Cash Assets, All Commercial Banks
    ### Commercial and Industrial Loans
    'BUSLOANSNSA', # Commercial and Industrial Loans, All Commercial Banks
    ### Commercial and Industrial Loans to U.S. Addressees
    'CIUACBM027NBOG', # Commercial and Industrial Loans to U.S. Addressees, All Commercial Banks (DISCONTINUED)
    ### Consumer Loans
    'CONSUMERNSA', # Consumer Loans, All Commercial Banks
    'CCLACBM027NBOG', # Consumer Loans: Credit Cards and Other Revolving Plans, All Commercial Banks
    'OCLACBM027NBOG', # Consumer Loans: Other Consumer Loans, All Commercial Banks
    'AOCACBM027NBOG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, All Commercial Banks (DISCONTINUED)
    'CARACBM027NBOG', # Consumer Loans: Other Consumer Loans: Automobile Loans, All Commercial Banks
    ### Deposits
    'DPSACBM027NBOG', # Deposits, All Commercial Banks
    ### Derivatives with a Negative Fair Value
    'DNVACBM027NBOG', # Derivatives with a Negative Fair Value, All Commercial Banks (DISCONTINUED)
    ### Derivatives with a Positive Fair Value
    'DFVACBM027NBOG', # Derivatives with a Positive Fair Value, All Commercial Banks (DISCONTINUED)
    ### Fed Funds and Reverse RPs with Banks
    'FRPACBM027NBOG', # Fed Funds and Reverse RPs with Banks, All Commercial Banks (DISCONTINUED)
    ### Interbank Loans
    'IBLACBM027NBOG', # Interbank Loans, All Commercial Banks (DISCONTINUED)
    ### Allowance for Credit Losses on Loans and Leases
    'ALLACBM027NBOG', # LESS: Allowance for Credit Losses on Loans and Leases, All Commercial Banks
    ### Large Time Deposits
    'LTDACBM027NBOG', # Large Time Deposits, All Commercial Banks
    ### Loans Secured by Nonfarm Nonresidential Properties
    'NNPACBM027NBOG', # Loans Secured by Nonfarm Nonresidential Properties, All Commercial Banks (DISCONTINUED)
    ### Loans and Leases in Bank Credit
    'LOANSNSA', # Loans and Leases in Bank Credit, All Commercial Banks
    ### Loans to Commercial Banks
    'LCBACBM027NBOG', # Loans to Commercial Banks, All Commercial Banks
    ### Loans with Original Amounts of $1,000,000 or Less
    'LLMACBM027NBOG', # Loans with Original Amounts of $1,000,000 or Less, All Commercial Banks (DISCONTINUED)
    ### Net Due to Related Foreign Offices
    'NDFACBM027NBOG', # Net Due to Related Foreign Offices, All Commercial Banks
    ### Net Unrealized Gains (Losses) on Available-for-Sale Securities
    'NUGACBM027NBOG', # Net Unrealized Gains (Losses) on Available-for-Sale Securities, All Commercial Banks (DISCONTINUED)
    ### Other Assets
    'OATACBM027NBOG', # Other Assets, All Commercial Banks (DISCONTINUED)
    ### Other Deposits
    'ODSACBM027NBOG', # Other Deposits, All Commercial Banks
    ### Other Liabilities
    'OLSACBM027NBOG', # Other Liabilities, All Commercial Banks (DISCONTINUED)
    ### Other Loans and Leases
    'OLLACBM027NBOG', # Other Loans and Leases, All Commercial Banks (DISCONTINUED)
    'AOLACBM027NBOG', # Other Loans and Leases: All Other Loans and Leases, All Commercial Banks
    'LNFACBM027NBOG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, All Commercial Banks
    'OLNACBM027NBOG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, All Commercial Banks (DISCONTINUED)
    'OLRACBM027NBOG', # Other Loans and Leases: Fed Funds and Reverse RPs with Nonbanks, All Commercial Banks (DISCONTINUED)
    ### Other Securities
    'OTHSECNSA', # Other Securities, All Commercial Banks
    'OMBACBM027NBOG', # Other Securities: Mortgage-Backed Securities, All Commercial Banks
    'ONMACBM027NBOG', # Other Securities: Non-MBS, All Commercial Banks
    ### Other Securitized Consumer Loans
    'OSCACBM027NBOG', # Other Securitized Consumer Loans, All Commercial Banks (DISCONTINUED)
    ### Other Trading Assets
    'OTAACBM027NBOG', # Other Trading Assets, All Commercial Banks (DISCONTINUED)
    ### Other Trading Liabilities
    'OTLACBM027NBOG', # Other Trading Liabilities, All Commercial Banks (DISCONTINUED)
    ### Real Estate Loans
    'REALLNNSA', # Real Estate Loans, All Commercial Banks
    'CREACBM027NBOG', # Real Estate Loans: Commercial Real Estate Loans, All Commercial Banks
    'CLDACBM027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, All Commercial Banks
    'SBFACBM027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, All Commercial Banks
    'SMPACBM027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, All Commercial Banks
    'SNFACBM027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, All Commercial Banks
    'RREACBM027NBOG', # Real Estate Loans: Residential Real Estate Loans, All Commercial Banks
    'CRLACBM027NBOG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, All Commercial Banks
    'RHEACBM027NBOG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, All Commercial Banks
    ### Residual (Assets Less Liabilities)
    'RALACBM027NBOG', # Residual (Assets Less Liabilities), All Commercial Banks
    ### Securities in Bank Credit
    'INVESTNSA', # Securities in Bank Credit, All Commercial Banks
    ### Securitized Consumer Loans
    'SCLACBM027NBOG', # Securitized Consumer Loans, All Commercial Banks (DISCONTINUED)
    ### Securitized Credit Cards and Other Revolving Plans
    'SCCACBM027NBOG', # Securitized Credit Cards and Other Revolving Plans, All Commercial Banks (DISCONTINUED)
    ### Securitized Real Estate Loans
    'SREACBM027NBOG', # Securitized Real Estate Loans, All Commercial Banks (DISCONTINUED)
    ### Total Assets
    'TLAACBM027NBOG', # Total Assets, All Commercial Banks
    ### Total Liabilities
    'TLBACBM027NBOG', # Total Liabilities, All Commercial Banks
    ### Trading Assets
    'TDAACBM027NBOG', # Trading Assets, All Commercial Banks (DISCONTINUED)
    ### Trading Liabilities
    'TLSACBM027NBOG', # Trading Liabilities, All Commercial Banks (DISCONTINUED)
    ### Treasury and Agency Securities
    'USGSECNSA', # Treasury and Agency Securities, All Commercial Banks
    'TMBACBM027NBOG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), All Commercial Banks
    'TNMACBM027NBOG', # Treasury and Agency Securities: Non-MBS, All Commercial Banks
    ### U.S. Treasury and Agency Securities, MBS
    'TAMACBM027NBOG', # U.S. Treasury and Agency Securities, MBS, All Commercial Banks (DISCONTINUED)
    ## 잔액 (Mil. of U.S. $, 원계열)
    ### Borrowings
    'H8B3094NCBDM', # Borrowings, All Commercial Banks
    ### Consumer Loans
    'B2245NCBDM', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, All Commercial Banks
    ### Other Assets
    'H8B3053NCBDM', # Other Assets, All Commercial Banks
    ### Other Liabilities
    'H8B3095NCBDM', # Other Liabilities, All Commercial Banks
    ### Other Loans and Leases
    'B2310NCBDM', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, All Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NCBDM', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, All Commercial Banks
    ## 증가율 (% Chg. at Annual Rate, SA)
    ### Bank Credit
    'H8B1001NCBCMG', # Bank Credit, All Commercial Banks
    ### Borrowings
    'H8B3094NCBCMG', # Borrowings, All Commercial Banks
    ### Cash Assets
    'H8B1048NCBCMG', # Cash Assets, All Commercial Banks
    ### Commercial and Industrial Loans
    'H8B1023NCBCMG', # Commercial and Industrial Loans, All Commercial Banks
    ### Consumer Loans
    'H8B1029NCBCMG', # Consumer Loans, All Commercial Banks
    'H8B1247NCBCMG', # Consumer Loans: Credit Cards and Other Revolving Plans, All Commercial Banks
    'H8B3248NCBCMG', # Consumer Loans: Other Consumer Loans, All Commercial Banks
    'B2245NCBCMG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, All Commercial Banks
    'B1243NCBCMG', # Consumer Loans: Other Consumer Loans: Automobile Loans, All Commercial Banks
    ### Deposits
    'H8B1058NCBCMG', # Deposits, All Commercial Banks
    ### Allowance for Credit Losses on Loans and Leases
    'H8B1043NCBCMG', # LESS: Allowance for Credit Losses on Loans and Leases, All Commercial Banks
    ### Large Time Deposits
    'H8B1072NCBCMG', # Large Time Deposits, All Commercial Banks
    ### Loans and Leases in Bank Credit
    'H8B1020NCBCMG', # Loans and Leases in Bank Credit, All Commercial Banks
    ### Loans to Commercial Banks
    'H8B1047NCBCMG', # Loans to Commercial Banks, All Commercial Banks
    ### Other Assets
    'H8B3053NCBCMG', # Other Assets, All Commercial Banks
    ### Other Deposits
    'H8B1110NCBCMG', # Other Deposits, All Commercial Banks
    ### Other Liabilities
    'H8B3095NCBCMG', # Other Liabilities, All Commercial Banks
    ### Other Loans and Leases
    'H8B3305NCBCMG', # Other Loans and Leases: All Other Loans and Leases, All Commercial Banks
    'B1030NCBCMG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, All Commercial Banks
    'B2310NCBCMG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, All Commercial Banks
    ### Other Securities
    'H8B1011NCBCMG', # Other Securities, All Commercial Banks
    'H8B1303NCBCMG', # Other Securities: Mortgage-Backed Securities, All Commercial Banks
    'H8B1304NCBCMG', # Other Securities: Non-MBS, All Commercial Banks
    ### Real Estate Loans
    'H8B1026NCBCMG', # Real Estate Loans, All Commercial Banks
    'H8B3219NCBCMG', # Real Estate Loans: Commercial Real Estate Loans, All Commercial Banks
    'B1215NCBCMG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, All Commercial Banks
    'B1216NCBCMG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, All Commercial Banks
    'B1217NCBCMG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, All Commercial Banks
    'B1218NCBCMG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, All Commercial Banks
    'H8B1221NCBCMG', # Real Estate Loans: Residential Real Estate Loans, All Commercial Banks
    'H8B1220NCBCMG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, All Commercial Banks
    'H8B1027NCBCMG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, All Commercial Banks
    ### Residual (Assets Less Liabilities)
    'H8B1091NCBCMG', # Residual (Assets Less Liabilities), All Commercial Banks
    ### Securities in Bank Credit
    'H8B1002NCBCMG', # Securities in Bank Credit, All Commercial Banks
    ### Total Assets
    'H8B1151NCBCMG', # Total Assets, All Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NCBCMG', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, All Commercial Banks
    ### Total Liabilities
    'H8B1152NCBCMG', # Total Liabilities, All Commercial Banks
    ### Treasury and Agency Securities
    'H8B1003NCBCMG', # Treasury and Agency Securities, All Commercial Banks
    'H8B1301NCBCMG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), All Commercial Banks
    'H8B1302NCBCMG', # Treasury and Agency Securities: Non-MBS, All Commercial Banks

    # Domestically Chartered Commercial Banks (174)
    ## 잔액 (Bil. of U.S. $, 계절조정)
    ### Bank Credit
    'BC0DCBM027SBOG', # Bank Credit, Domestically Chartered Commercial Banks
    ### Borrowings
    'BOWDCBM027SBOG', # Borrowings, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Borrowings from Banks in the U.S.
    'BBUDCBM027SBOG', # Borrowings from Banks in the U.S., Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Borrowings from Others
    'BFODCBM027SBOG', # Borrowings from Others, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Cash Assets
    'CASDCBM027SBOG', # Cash Assets, Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans
    'CILDCBM027SBOG', # Commercial and Industrial Loans, Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans to U.S. Addressees
    'CIUDCBM027SBOG', # Commercial and Industrial Loans to U.S. Addressees, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Consumer Loans
    'CLSDCBM027SBOG', # Consumer Loans, Domestically Chartered Commercial Banks
    'CCLDCBM027SBOG', # Consumer Loans: Credit Cards and Other Revolving Plans, Domestically Chartered Commercial Banks
    'OCLDCBM027SBOG', # Consumer Loans: Other Consumer Loans, Domestically Chartered Commercial Banks
    'AOCDCBM027SBOG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Domestically Chartered Commercial Banks (DISCONTINUED)
    'CARDCBM027SBOG', # Consumer Loans: Other Consumer Loans: Automobile Loans, Domestically Chartered Commercial Banks
    ### Deposits
    'DPSDCBM027SBOG', # Deposits, Domestically Chartered Commercial Banks
    ### Derivatives with a Negative Fair Value
    'DNVDCBM027SBOG', # Derivatives with a Negative Fair Value, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Derivatives with a Positive Fair Value
    'DFVDCBM027SBOG', # Derivatives with a Positive Fair Value, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Fed Funds and Reverse RPs with Banks
    'FRPDCBM027SBOG', # Fed Funds and Reverse RPs with Banks, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Interbank Loans
    'IBLDCBM027SBOG', # Interbank Loans, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Allowance for Credit Losses on Loans and Leases
    'ALLDCBM027SBOG', # LESS: Allowance for Credit Losses on Loans and Leases, Domestically Chartered Commercial Banks
    ### Large Time Deposits
    'LTDDCBM027SBOG', # Large Time Deposits, Domestically Chartered Commercial Banks
    ### Loans Secured by Nonfarm Nonresidential Properties
    'NNPDCBM027SBOG', # Loans Secured by Nonfarm Nonresidential Properties, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Loans and Leases in Bank Credit
    'LLBDCBM027SBOG', # Loans and Leases in Bank Credit, Domestically Chartered Commercial Banks
    ### Loans to Commercial Banks
    'LCBDCBM027SBOG', # Loans to Commercial Banks, Domestically Chartered Commercial Banks
    ### Loans with Original Amounts of $1,000,000 or Less
    'LLMDCBM027SBOG', # Loans with Original Amounts of $1,000,000 or Less, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Net Due to Related Foreign Offices
    'NDFDCBM027SBOG', # Net Due to Related Foreign Offices, Domestically Chartered Commercial Banks
    ### Net Unrealized Gains (Losses) on Available-for-Sale Securities
    'NUGDCBM027SBOG', # Net Unrealized Gains (Losses) on Available-for-Sale Securities, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Assets
    'OATDCBM027SBOG', # Other Assets, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Deposits
    'ODSDCBM027SBOG', # Other Deposits, Domestically Chartered Commercial Banks
    ### Other Liabilities
    'OLSDCBM027SBOG', # Other Liabilities, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Loans and Leases
    'OLLDCBM027SBOG', # Other Loans and Leases, Domestically Chartered Commercial Banks (DISCONTINUED)
    'AOLDCBM027SBOG', # Other Loans and Leases: All Other Loans and Leases, Domestically Chartered Commercial Banks
    'LNFDCBM027SBOG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Domestically Chartered Commercial Banks
    'OLNDCBM027SBOG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Domestically Chartered Commercial Banks (DISCONTINUED)
    'OLRDCBM027SBOG', # Other Loans and Leases: Fed Funds and Reverse RPs with Nonbanks, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Securities
    'OSEDCBM027SBOG', # Other Securities, Domestically Chartered Commercial Banks
    'OMBDCBM027SBOG', # Other Securities: Mortgage-Backed Securities, Domestically Chartered Commercial Banks
    'ONMDCBM027SBOG', # Other Securities: Non-MBS, Domestically Chartered Commercial Banks
    ### Other Securitized Consumer Loans
    'OSCDCBM027SBOG', # Other Securitized Consumer Loans, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Trading Assets
    'OTADCBM027SBOG', # Other Trading Assets, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Trading Liabilities
    'OTLDCBM027SBOG', # Other Trading Liabilities, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Real Estate Loans
    'RELDCBM027SBOG', # Real Estate Loans, Domestically Chartered Commercial Banks
    'CREDCBM027SBOG', # Real Estate Loans: Commercial Real Estate Loans, Domestically Chartered Commercial Banks
    'CLDDCBM027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Domestically Chartered Commercial Banks
    'SBFDCBM027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Domestically Chartered Commercial Banks
    'SMPDCBM027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Domestically Chartered Commercial Banks
    'SNFDCBM027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Domestically Chartered Commercial Banks
    'RREDCBM027SBOG', # Real Estate Loans: Residential Real Estate Loans, Domestically Chartered Commercial Banks
    'CRLDCBM027SBOG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Domestically Chartered Commercial Banks
    'RHEDCBM027SBOG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Domestically Chartered Commercial Banks
    ### Residual (Assets Less Liabilities)
    'RALDCBM027SBOG', # Residual (Assets Less Liabilities), Domestically Chartered Commercial Banks
    ### Securities in Bank Credit
    'SBCDCBM027SBOG', # Securities in Bank Credit, Domestically Chartered Commercial Banks
    ### Securitized Consumer Loans
    'SCLDCBM027SBOG', # Securitized Consumer Loans, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Securitized Credit Cards and Other Revolving Plans
    'SCCDCBM027SBOG', # Securitized Credit Cards and Other Revolving Plans, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Securitized Real Estate Loans
    'SREDCBM027SBOG', # Securitized Real Estate Loans, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Total Assets
    'TLADCBM027SBOG', # Total Assets, Domestically Chartered Commercial Banks
    ### Total Liabilities
    'TLBDCBM027SBOG', # Total Liabilities, Domestically Chartered Commercial Banks
    ### Trading Assets
    'TDADCBM027SBOG', # Trading Assets, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Trading Liabilities
    'TLSDCBM027SBOG', # Trading Liabilities, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Treasury and Agency Securities
    'TASDCBM027SBOG', # Treasury and Agency Securities, Domestically Chartered Commercial Banks
    'TMBDCBM027SBOG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Domestically Chartered Commercial Banks
    'TNMDCBM027SBOG', # Treasury and Agency Securities: Non-MBS, Domestically Chartered Commercial Banks
    ### U.S. Treasury and Agency Securities, MBS
    'TAMDCBM027SBOG', # U.S. Treasury and Agency Securities, MBS, Domestically Chartered Commercial Banks (DISCONTINUED)
    ## 잔액 (Mil. of U.S. $, 계절조정)
    ### Borrowings
    'H8B3094NDMAM', # Borrowings, Domestically Chartered Commercial Banks
    ### Consumer Loans
    'B2245NDMAM', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Domestically Chartered Commercial Banks
    ### Other Assets
    'H8B3053NDMAM', # Other Assets, Domestically Chartered Commercial Banks
    ### Other Liabilities
    'H8B3095NDMAM', # Other Liabilities, Domestically Chartered Commercial Banks
    ### Other Loans and Leases
    'B2310NDMAM', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Domestically Chartered Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NDMAM', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Domestically Chartered Commercial Banks
    ## 잔액 (Bil. of U.S. $, 원계열)
    ### Bank Credit
    'BC0DCBM027NBOG', # Bank Credit, Domestically Chartered Commercial Banks
    ### Borrowings
    'BOWDCBM027NBOG', # Borrowings, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Borrowings from Banks in the U.S.
    'BBUDCBM027NBOG', # Borrowings from Banks in the U.S., Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Borrowings from Others
    'BFODCBM027NBOG', # Borrowings from Others, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Cash Assets
    'CASDCBM027NBOG', # Cash Assets, Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans
    'CILDCBM027NBOG', # Commercial and Industrial Loans, Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans to U.S. Addressees
    'CIUDCBM027NBOG', # Commercial and Industrial Loans to U.S. Addressees, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Consumer Loans
    'CLSDCBM027NBOG', # Consumer Loans, Domestically Chartered Commercial Banks
    'CCLDCBM027NBOG', # Consumer Loans: Credit Cards and Other Revolving Plans, Domestically Chartered Commercial Banks
    'OCLDCBM027NBOG', # Consumer Loans: Other Consumer Loans, Domestically Chartered Commercial Banks
    'AOCDCBM027NBOG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Domestically Chartered Commercial Banks (DISCONTINUED)
    'CARDCBM027NBOG', # Consumer Loans: Other Consumer Loans: Automobile Loans, Domestically Chartered Commercial Banks
    ### Deposits
    'DPSDCBM027NBOG', # Deposits, Domestically Chartered Commercial Banks
    ### Derivatives with a Negative Fair Value
    'DNVDCBM027NBOG', # Derivatives with a Negative Fair Value, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Derivatives with a Positive Fair Value
    'DFVDCBM027NBOG', # Derivatives with a Positive Fair Value, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Fed Funds and Reverse RPs with Banks
    'FRPDCBM027NBOG', # Fed Funds and Reverse RPs with Banks, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Interbank Loans
    'IBLDCBM027NBOG', # Interbank Loans, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Allowance for Credit Losses on Loans and Leases
    'ALLDCBM027NBOG', # LESS: Allowance for Credit Losses on Loans and Leases, Domestically Chartered Commercial Banks
    ### Large Time Deposits
    'LTDDCBM027NBOG', # Large Time Deposits, Domestically Chartered Commercial Banks
    ### Loans Secured by Nonfarm Nonresidential Properties
    'NNPDCBM027NBOG', # Loans Secured by Nonfarm Nonresidential Properties, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Loans and Leases in Bank Credit
    'LLBDCBM027NBOG', # Loans and Leases in Bank Credit, Domestically Chartered Commercial Banks
    ### Loans to Commercial Banks
    'LCBDCBM027NBOG', # Loans to Commercial Banks, Domestically Chartered Commercial Banks
    ### Loans with Original Amounts of $1,000,000 or Less
    'LLMDCBM027NBOG', # Loans with Original Amounts of $1,000,000 or Less, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Net Due to Related Foreign Offices
    'NDFDCBM027NBOG', # Net Due to Related Foreign Offices, Domestically Chartered Commercial Banks
    ### Net Unrealized Gains (Losses) on Available-for-Sale Securities
    'NUGDCBM027NBOG', # Net Unrealized Gains (Losses) on Available-for-Sale Securities, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Assets
    'OATDCBM027NBOG', # Other Assets, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Deposits
    'ODSDCBM027NBOG', # Other Deposits, Domestically Chartered Commercial Banks
    ### Other Liabilities
    'OLSDCBM027NBOG', # Other Liabilities, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Loans and Leases
    'OLLDCBM027NBOG', # Other Loans and Leases, Domestically Chartered Commercial Banks (DISCONTINUED)
    'AOLDCBM027NBOG', # Other Loans and Leases: All Other Loans and Leases, Domestically Chartered Commercial Banks
    'LNFDCBM027NBOG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Domestically Chartered Commercial Banks
    'OLNDCBM027NBOG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Domestically Chartered Commercial Banks (DISCONTINUED)
    'OLRDCBM027NBOG', # Other Loans and Leases: Fed Funds and Reverse RPs with Nonbanks, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Securities
    'OSEDCBM027NBOG', # Other Securities, Domestically Chartered Commercial Banks
    'OMBDCBM027NBOG', # Other Securities: Mortgage-Backed Securities, Domestically Chartered Commercial Banks
    'ONMDCBM027NBOG', # Other Securities: Non-MBS, Domestically Chartered Commercial Banks
    ### Other Securitized Consumer Loans
    'OSCDCBM027NBOG', # Other Securitized Consumer Loans, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Trading Assets
    'OTADCBM027NBOG', # Other Trading Assets, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Trading Liabilities
    'OTLDCBM027NBOG', # Other Trading Liabilities, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Real Estate Loans
    'RELDCBM027NBOG', # Real Estate Loans, Domestically Chartered Commercial Banks
    'CREDCBM027NBOG', # Real Estate Loans: Commercial Real Estate Loans, Domestically Chartered Commercial Banks
    'CLDDCBM027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Domestically Chartered Commercial Banks
    'SBFDCBM027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Domestically Chartered Commercial Banks
    'SMPDCBM027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Domestically Chartered Commercial Banks
    'SNFDCBM027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Domestically Chartered Commercial Banks
    'RREDCBM027NBOG', # Real Estate Loans: Residential Real Estate Loans, Domestically Chartered Commercial Banks
    'CRLDCBM027NBOG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Domestically Chartered Commercial Banks
    'RHEDCBM027NBOG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Domestically Chartered Commercial Banks
    ### Residual (Assets Less Liabilities)
    'RALDCBM027NBOG', # Residual (Assets Less Liabilities), Domestically Chartered Commercial Banks
    ### Securities in Bank Credit
    'SBCDCBM027NBOG', # Securities in Bank Credit, Domestically Chartered Commercial Banks
    ### Securitized Consumer Loans
    'SCLDCBM027NBOG', # Securitized Consumer Loans, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Securitized Credit Cards and Other Revolving Plans
    'SCCDCBM027NBOG', # Securitized Credit Cards and Other Revolving Plans, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Securitized Real Estate Loans
    'SREDCBM027NBOG', # Securitized Real Estate Loans, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Total Assets
    'TLADCBM027NBOG', # Total Assets, Domestically Chartered Commercial Banks
    ### Total Liabilities
    'TLBDCBM027NBOG', # Total Liabilities, Domestically Chartered Commercial Banks
    ### Trading Assets
    'TDADCBM027NBOG', # Trading Assets, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Trading Liabilities
    'TLSDCBM027NBOG', # Trading Liabilities, Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Treasury and Agency Securities
    'TASDCBM027NBOG', # Treasury and Agency Securities, Domestically Chartered Commercial Banks
    'TMBDCBM027NBOG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Domestically Chartered Commercial Banks
    'TNMDCBM027NBOG', # Treasury and Agency Securities: Non-MBS, Domestically Chartered Commercial Banks
    ### U.S. Treasury and Agency Securities, MBS
    'TAMDCBM027NBOG', # U.S. Treasury and Agency Securities, MBS, Domestically Chartered Commercial Banks (DISCONTINUED)
    ## 잔액 (Mil. of U.S. $, 원계열)
    ### Borrowings
    'H8B3094NDMDM', # Borrowings, Domestically Chartered Commercial Banks
    ### Consumer Loans
    'B2245NDMDM', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Domestically Chartered Commercial Banks
    ### Other Assets
    'H8B3053NDMDM', # Other Assets, Domestically Chartered Commercial Banks
    ### Other Liabilities
    'H8B3095NDMDM', # Other Liabilities, Domestically Chartered Commercial Banks
    ### Other Loans and Leases
    'B2310NDMDM', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Domestically Chartered Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NDMDM', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Domestically Chartered Commercial Banks
    ## 증가율 (% Chg. at Annual Rate, SA)
    ### Bank Credit
    'H8B1001NDMCMG', # Bank Credit, Domestically Chartered Commercial Banks
    ### Borrowings
    'H8B3094NDMCMG', # Borrowings, Domestically Chartered Commercial Banks
    ### Cash Assets
    'H8B1048NDMCMG', # Cash Assets, Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans
    'H8B1023NDMCMG', # Commercial and Industrial Loans, Domestically Chartered Commercial Banks
    ### Consumer Loans
    'H8B1029NDMCMG', # Consumer Loans, Domestically Chartered Commercial Banks
    'H8B1247NDMCMG', # Consumer Loans: Credit Cards and Other Revolving Plans, Domestically Chartered Commercial Banks
    'H8B3248NDMCMG', # Consumer Loans: Other Consumer Loans, Domestically Chartered Commercial Banks
    'B2245NDMCMG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Domestically Chartered Commercial Banks
    'B1243NDMCMG', # Consumer Loans: Other Consumer Loans: Automobile Loans, Domestically Chartered Commercial Banks
    ### Deposits
    'H8B1058NDMCMG', # Deposits, Domestically Chartered Commercial Banks
    ### Allowance for Credit Losses on Loans and Leases
    'H8B1043NDMCMG', # LESS: Allowance for Credit Losses on Loans and Leases, Domestically Chartered Commercial Banks
    ### Large Time Deposits
    'H8B1072NDMCMG', # Large Time Deposits, Domestically Chartered Commercial Banks
    ### Loans and Leases in Bank Credit
    'H8B1020NDMCMG', # Loans and Leases in Bank Credit, Domestically Chartered Commercial Banks
    ### Loans to Commercial Banks
    'H8B1047NDMCMG', # Loans to Commercial Banks, Domestically Chartered Commercial Banks
    ### Other Assets
    'H8B3053NDMCMG', # Other Assets, Domestically Chartered Commercial Banks
    ### Other Deposits
    'H8B1110NDMCMG', # Other Deposits, Domestically Chartered Commercial Banks
    ### Other Liabilities
    'H8B3095NDMCMG', # Other Liabilities, Domestically Chartered Commercial Banks
    ### Other Loans and Leases
    'H8B3305NDMCMG', # Other Loans and Leases: All Other Loans and Leases, Domestically Chartered Commercial Banks
    'B1030NDMCMG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Domestically Chartered Commercial Banks
    'B2310NDMCMG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Domestically Chartered Commercial Banks
    ### Other Securities
    'H8B1011NDMCMG', # Other Securities, Domestically Chartered Commercial Banks
    'H8B1303NDMCMG', # Other Securities: Mortgage-Backed Securities, Domestically Chartered Commercial Banks
    'H8B1304NDMCMG', # Other Securities: Non-MBS, Domestically Chartered Commercial Banks
    ### Real Estate Loans
    'H8B1026NDMCMG', # Real Estate Loans, Domestically Chartered Commercial Banks
    'H8B3219NDMCMG', # Real Estate Loans: Commercial Real Estate Loans, Domestically Chartered Commercial Banks
    'B1215NDMCMG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Domestically Chartered Commercial Banks
    'B1216NDMCMG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Domestically Chartered Commercial Banks
    'B1217NDMCMG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Domestically Chartered Commercial Banks
    'B1218NDMCMG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Domestically Chartered Commercial Banks
    'H8B1221NDMCMG', # Real Estate Loans: Residential Real Estate Loans, Domestically Chartered Commercial Banks
    'H8B1220NDMCMG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Domestically Chartered Commercial Banks
    'H8B1027NDMCMG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Domestically Chartered Commercial Banks
    ### Residual (Assets Less Liabilities)
    'H8B1091NDMCMG', # Residual (Assets Less Liabilities), Domestically Chartered Commercial Banks
    ### Securities in Bank Credit
    'H8B1002NDMCMG', # Securities in Bank Credit, Domestically Chartered Commercial Banks
    ### Total Assets
    'H8B1151NDMCMG', # Total Assets, Domestically Chartered Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NDMCMG', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Domestically Chartered Commercial Banks
    ### Total Liabilities
    'H8B1152NDMCMG', # Total Liabilities, Domestically Chartered Commercial Banks
    ### Treasury and Agency Securities
    'H8B1003NDMCMG', # Treasury and Agency Securities, Domestically Chartered Commercial Banks
    'H8B1301NDMCMG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Domestically Chartered Commercial Banks
    'H8B1302NDMCMG', # Treasury and Agency Securities: Non-MBS, Domestically Chartered Commercial Banks

    # Large Domestically Chartered Commercial Banks (174)
    ## 잔액 (Bil. of U.S. $, 계절조정)
    ### Bank Credit
    'BC0LCBM027SBOG', # Bank Credit, Large Domestically Chartered Commercial Banks
    ### Borrowings
    'BOWLCBM027SBOG', # Borrowings, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Borrowings from Banks in the U.S.
    'BBULCBM027SBOG', # Borrowings from Banks in the U.S., Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Borrowings from Others
    'BFOLCBM027SBOG', # Borrowings from Others, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Cash Assets
    'CASLCBM027SBOG', # Cash Assets, Large Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans
    'CILLCBM027SBOG', # Commercial and Industrial Loans, Large Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans to U.S. Addressees
    'CIULCBM027SBOG', # Commercial and Industrial Loans to U.S. Addressees, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Consumer Loans
    'CLSLCBM027SBOG', # Consumer Loans, Large Domestically Chartered Commercial Banks
    'CCLLCBM027SBOG', # Consumer Loans: Credit Cards and Other Revolving Plans, Large Domestically Chartered Commercial Banks
    'OCLLCBM027SBOG', # Consumer Loans: Other Consumer Loans, Large Domestically Chartered Commercial Banks
    'AOCLCBM027SBOG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    'CARLCBM027SBOG', # Consumer Loans: Other Consumer Loans: Automobile Loans, Large Domestically Chartered Commercial Banks
    ### Deposits
    'DPSLCBM027SBOG', # Deposits, Large Domestically Chartered Commercial Banks
    ### Derivatives with a Negative Fair Value
    'DNVLCBM027SBOG', # Derivatives with a Negative Fair Value, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Derivatives with a Positive Fair Value
    'DFVLCBM027SBOG', # Derivatives with a Positive Fair Value, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Fed Funds and Reverse RPs with Banks
    'FRPLCBM027SBOG', # Fed Funds and Reverse RPs with Banks, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Interbank Loans
    'IBLLCBM027SBOG', # Interbank Loans, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Allowance for Credit Losses on Loans and Leases
    'ALLLCBM027SBOG', # LESS: Allowance for Credit Losses on Loans and Leases, Large Domestically Chartered Commercial Banks
    ### Large Time Deposits
    'LTDLCBM027SBOG', # Large Time Deposits, Large Domestically Chartered Commercial Banks
    ### Loans Secured by Nonfarm Nonresidential Properties
    'NNPLCBM027SBOG', # Loans Secured by Nonfarm Nonresidential Properties, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Loans and Leases in Bank Credit
    'LLBLCBM027SBOG', # Loans and Leases in Bank Credit, Large Domestically Chartered Commercial Banks
    ### Loans to Commercial Banks
    'LCBLCBM027SBOG', # Loans to Commercial Banks, Large Domestically Chartered Commercial Banks
    ### Loans with Original Amounts of $1,000,000 or Less
    'LLMLCBM027SBOG', # Loans with Original Amounts of $1,000,000 or Less, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Net Due to Related Foreign Offices
    'NDFLCBM027SBOG', # Net Due to Related Foreign Offices, Large Domestically Chartered Commercial Banks
    ### Net Unrealized Gains (Losses) on Available-for-Sale Securities
    'NUGLCBM027SBOG', # Net Unrealized Gains (Losses) on Available-for-Sale Securities, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Assets
    'OATLCBM027SBOG', # Other Assets, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Deposits
    'ODSLCBM027SBOG', # Other Deposits, Large Domestically Chartered Commercial Banks
    ### Other Liabilities
    'OLSLCBM027SBOG', # Other Liabilities, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Loans and Leases
    'OLLLCBM027SBOG', # Other Loans and Leases, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    'AOLLCBM027SBOG', # Other Loans and Leases: All Other Loans and Leases, Large Domestically Chartered Commercial Banks
    'LNFLCBM027SBOG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Large Domestically Chartered Commercial Banks
    'OLNLCBM027SBOG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    'OLRLCBM027SBOG', # Other Loans and Leases: Fed Funds and Reverse RPs with Nonbanks, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Securities
    'OSELCBM027SBOG', # Other Securities, Large Domestically Chartered Commercial Banks
    'OMBLCBM027SBOG', # Other Securities: Mortgage-Backed Securities, Large Domestically Chartered Commercial Banks
    'ONMLCBM027SBOG', # Other Securities: Non-MBS, Large Domestically Chartered Commercial Banks
    ### Other Securitized Consumer Loans
    'OSCLCBM027SBOG', # Other Securitized Consumer Loans, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Trading Assets
    'OTALCBM027SBOG', # Other Trading Assets, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Trading Liabilities
    'OTLLCBM027SBOG', # Other Trading Liabilities, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Real Estate Loans
    'RELLCBM027SBOG', # Real Estate Loans, Large Domestically Chartered Commercial Banks
    'CRELCBM027SBOG', # Real Estate Loans: Commercial Real Estate Loans, Large Domestically Chartered Commercial Banks
    'CLDLCBM027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Large Domestically Chartered Commercial Banks
    'SBFLCBM027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Large Domestically Chartered Commercial Banks
    'SMPLCBM027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Large Domestically Chartered Commercial Banks
    'SNFLCBM027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Large Domestically Chartered Commercial Banks
    'RRELCBM027SBOG', # Real Estate Loans: Residential Real Estate Loans, Large Domestically Chartered Commercial Banks
    'CRLLCBM027SBOG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Large Domestically Chartered Commercial Banks
    'RHELCBM027SBOG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Large Domestically Chartered Commercial Banks
    ### Residual (Assets Less Liabilities)
    'RALLCBM027SBOG', # Residual (Assets Less Liabilities), Large Domestically Chartered Commercial Banks
    ### Securities in Bank Credit
    'SBCLCBM027SBOG', # Securities in Bank Credit, Large Domestically Chartered Commercial Banks
    ### Securitized Consumer Loans
    'SCLLCBM027SBOG', # Securitized Consumer Loans, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Securitized Credit Cards and Other Revolving Plans
    'SCCLCBM027SBOG', # Securitized Credit Cards and Other Revolving Plans, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Securitized Real Estate Loans
    'SRELCBM027SBOG', # Securitized Real Estate Loans, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Total Assets
    'TLALCBM027SBOG', # Total Assets, Large Domestically Chartered Commercial Banks
    ### Total Liabilities
    'TLBLCBM027SBOG', # Total Liabilities, Large Domestically Chartered Commercial Banks
    ### Trading Assets
    'TDALCBM027SBOG', # Trading Assets, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Trading Liabilities
    'TLSLCBM027SBOG', # Trading Liabilities, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Treasury and Agency Securities
    'TASLCBM027SBOG', # Treasury and Agency Securities, Large Domestically Chartered Commercial Banks
    'TMBLCBM027SBOG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Large Domestically Chartered Commercial Banks
    'TNMLCBM027SBOG', # Treasury and Agency Securities: Non-MBS, Large Domestically Chartered Commercial Banks
    ### U.S. Treasury and Agency Securities, MBS
    'TAMLCBM027SBOG', # U.S. Treasury and Agency Securities, MBS, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ## 잔액 (Mil. of U.S. $, 계절조정)
    ### Borrowings
    'H8B3094NLGAM', # Borrowings, Large Domestically Chartered Commercial Banks
    ### Consumer Loans
    'B2245NLGAM', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Large Domestically Chartered Commercial Banks
    ### Other Assets
    'H8B3053NLGAM', # Other Assets, Large Domestically Chartered Commercial Banks
    ### Other Liabilities
    'H8B3095NLGAM', # Other Liabilities, Large Domestically Chartered Commercial Banks
    ### Other Loans and Leases
    'B2310NLGAM', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Large Domestically Chartered Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NLGAM', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Large Domestically Chartered Commercial Banks
    ## 잔액 (Bil. of U.S. $, 원계열)
    ### Bank Credit
    'BC0LCBM027NBOG', # Bank Credit, Large Domestically Chartered Commercial Banks
    ### Borrowings
    'BOWLCBM027NBOG', # Borrowings, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Borrowings from Banks in the U.S.
    'BBULCBM027NBOG', # Borrowings from Banks in the U.S., Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Borrowings from Others
    'BFOLCBM027NBOG', # Borrowings from Others, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Cash Assets
    'CASLCBM027NBOG', # Cash Assets, Large Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans
    'CILLCBM027NBOG', # Commercial and Industrial Loans, Large Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans to U.S. Addressees
    'CIULCBM027NBOG', # Commercial and Industrial Loans to U.S. Addressees, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Consumer Loans
    'CLSLCBM027NBOG', # Consumer Loans, Large Domestically Chartered Commercial Banks
    'CCLLCBM027NBOG', # Consumer Loans: Credit Cards and Other Revolving Plans, Large Domestically Chartered Commercial Banks
    'OCLLCBM027NBOG', # Consumer Loans: Other Consumer Loans, Large Domestically Chartered Commercial Banks
    'AOCLCBM027NBOG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    'CARLCBM027NBOG', # Consumer Loans: Other Consumer Loans: Automobile Loans, Large Domestically Chartered Commercial Banks
    ### Deposits
    'DPSLCBM027NBOG', # Deposits, Large Domestically Chartered Commercial Banks
    ### Derivatives with a Negative Fair Value
    'DNVLCBM027NBOG', # Derivatives with a Negative Fair Value, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Derivatives with a Positive Fair Value
    'DFVLCBM027NBOG', # Derivatives with a Positive Fair Value, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Fed Funds and Reverse RPs with Banks
    'FRPLCBM027NBOG', # Fed Funds and Reverse RPs with Banks, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Interbank Loans
    'IBLLCBM027NBOG', # Interbank Loans, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Allowance for Credit Losses on Loans and Leases
    'ALLLCBM027NBOG', # LESS: Allowance for Credit Losses on Loans and Leases, Large Domestically Chartered Commercial Banks
    ### Large Time Deposits
    'LTDLCBM027NBOG', # Large Time Deposits, Large Domestically Chartered Commercial Banks
    ### Loans Secured by Nonfarm Nonresidential Properties
    'NNPLCBM027NBOG', # Loans Secured by Nonfarm Nonresidential Properties, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Loans and Leases in Bank Credit
    'LLBLCBM027NBOG', # Loans and Leases in Bank Credit, Large Domestically Chartered Commercial Banks
    ### Loans to Commercial Banks
    'LCBLCBM027NBOG', # Loans to Commercial Banks, Large Domestically Chartered Commercial Banks
    ### Loans with Original Amounts of $1,000,000 or Less
    'LLMLCBM027NBOG', # Loans with Original Amounts of $1,000,000 or Less, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Net Due to Related Foreign Offices
    'NDFLCBM027NBOG', # Net Due to Related Foreign Offices, Large Domestically Chartered Commercial Banks
    ### Net Unrealized Gains (Losses) on Available-for-Sale Securities
    'NUGLCBM027NBOG', # Net Unrealized Gains (Losses) on Available-for-Sale Securities, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Assets
    'OATLCBM027NBOG', # Other Assets, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Deposits
    'ODSLCBM027NBOG', # Other Deposits, Large Domestically Chartered Commercial Banks
    ### Other Liabilities
    'OLSLCBM027NBOG', # Other Liabilities, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Loans and Leases
    'OLLLCBM027NBOG', # Other Loans and Leases, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    'AOLLCBM027NBOG', # Other Loans and Leases: All Other Loans and Leases, Large Domestically Chartered Commercial Banks
    'LNFLCBM027NBOG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Large Domestically Chartered Commercial Banks
    'OLNLCBM027NBOG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    'OLRLCBM027NBOG', # Other Loans and Leases: Fed Funds and Reverse RPs with Nonbanks, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Securities
    'OSELCBM027NBOG', # Other Securities, Large Domestically Chartered Commercial Banks
    'OMBLCBM027NBOG', # Other Securities: Mortgage-Backed Securities, Large Domestically Chartered Commercial Banks
    'ONMLCBM027NBOG', # Other Securities: Non-MBS, Large Domestically Chartered Commercial Banks
    ### Other Securitized Consumer Loans
    'OSCLCBM027NBOG', # Other Securitized Consumer Loans, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Trading Assets
    'OTALCBM027NBOG', # Other Trading Assets, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Trading Liabilities
    'OTLLCBM027NBOG', # Other Trading Liabilities, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Real Estate Loans
    'RELLCBM027NBOG', # Real Estate Loans, Large Domestically Chartered Commercial Banks
    'CRELCBM027NBOG', # Real Estate Loans: Commercial Real Estate Loans, Large Domestically Chartered Commercial Banks
    'CLDLCBM027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Large Domestically Chartered Commercial Banks
    'SBFLCBM027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Large Domestically Chartered Commercial Banks
    'SMPLCBM027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Large Domestically Chartered Commercial Banks
    'SNFLCBM027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Large Domestically Chartered Commercial Banks
    'RRELCBM027NBOG', # Real Estate Loans: Residential Real Estate Loans, Large Domestically Chartered Commercial Banks
    'CRLLCBM027NBOG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Large Domestically Chartered Commercial Banks
    'RHELCBM027NBOG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Large Domestically Chartered Commercial Banks
    ### Residual (Assets Less Liabilities)
    'RALLCBM027NBOG', # Residual (Assets Less Liabilities), Large Domestically Chartered Commercial Banks
    ### Securities in Bank Credit
    'SBCLCBM027NBOG', # Securities in Bank Credit, Large Domestically Chartered Commercial Banks
    ### Securitized Consumer Loans
    'SCLLCBM027NBOG', # Securitized Consumer Loans, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Securitized Credit Cards and Other Revolving Plans
    'SCCLCBM027NBOG', # Securitized Credit Cards and Other Revolving Plans, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Securitized Real Estate Loans
    'SRELCBM027NBOG', # Securitized Real Estate Loans, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Total Assets
    'TLALCBM027NBOG', # Total Assets, Large Domestically Chartered Commercial Banks
    ### Total Liabilities
    'TLBLCBM027NBOG', # Total Liabilities, Large Domestically Chartered Commercial Banks
    ### Trading Assets
    'TDALCBM027NBOG', # Trading Assets, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Trading Liabilities
    'TLSLCBM027NBOG', # Trading Liabilities, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Treasury and Agency Securities
    'TASLCBM027NBOG', # Treasury and Agency Securities, Large Domestically Chartered Commercial Banks
    'TMBLCBM027NBOG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Large Domestically Chartered Commercial Banks
    'TNMLCBM027NBOG', # Treasury and Agency Securities: Non-MBS, Large Domestically Chartered Commercial Banks
    ### U.S. Treasury and Agency Securities, MBS
    'TAMLCBM027NBOG', # U.S. Treasury and Agency Securities, MBS, Large Domestically Chartered Commercial Banks (DISCONTINUED)
    ## 잔액 (Mil. of U.S. $, 원계열)
    ### Borrowings
    'H8B3094NLGDM', # Borrowings, Large Domestically Chartered Commercial Banks
    ### Consumer Loans
    'B2245NLGDM', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Large Domestically Chartered Commercial Banks
    ### Other Assets
    'H8B3053NLGDM', # Other Assets, Large Domestically Chartered Commercial Banks
    ### Other Liabilities
    'H8B3095NLGDM', # Other Liabilities, Large Domestically Chartered Commercial Banks
    ### Other Loans and Leases
    'B2310NLGDM', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Large Domestically Chartered Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NLGDM', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Large Domestically Chartered Commercial Banks
    ## 증가율 (% Chg. at Annual Rate, SA)
    ### Bank Credit
    'H8B1001NLGCMG', # Bank Credit, Large Domestically Chartered Commercial Banks
    ### Borrowings
    'H8B3094NLGCMG', # Borrowings, Large Domestically Chartered Commercial Banks
    ### Cash Assets
    'H8B1048NLGCMG', # Cash Assets, Large Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans
    'H8B1023NLGCMG', # Commercial and Industrial Loans, Large Domestically Chartered Commercial Banks
    ### Consumer Loans
    'H8B1029NLGCMG', # Consumer Loans, Large Domestically Chartered Commercial Banks
    'H8B1247NLGCMG', # Consumer Loans: Credit Cards and Other Revolving Plans, Large Domestically Chartered Commercial Banks
    'H8B3248NLGCMG', # Consumer Loans: Other Consumer Loans, Large Domestically Chartered Commercial Banks
    'B2245NLGCMG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Large Domestically Chartered Commercial Banks
    'B1243NLGCMG', # Consumer Loans: Other Consumer Loans: Automobile Loans, Large Domestically Chartered Commercial Banks
    ### Deposits
    'H8B1058NLGCMG', # Deposits, Large Domestically Chartered Commercial Banks
    ### Allowance for Credit Losses on Loans and Leases
    'H8B1043NLGCMG', # LESS: Allowance for Credit Losses on Loans and Leases, Large Domestically Chartered Commercial Banks
    ### Large Time Deposits
    'H8B1072NLGCMG', # Large Time Deposits, Large Domestically Chartered Commercial Banks
    ### Loans and Leases in Bank Credit
    'H8B1020NLGCMG', # Loans and Leases in Bank Credit, Large Domestically Chartered Commercial Banks
    ### Loans to Commercial Banks
    'H8B1047NLGCMG', # Loans to Commercial Banks, Large Domestically Chartered Commercial Banks
    ### Other Assets
    'H8B3053NLGCMG', # Other Assets, Large Domestically Chartered Commercial Banks
    ### Other Deposits
    'H8B1110NLGCMG', # Other Deposits, Large Domestically Chartered Commercial Banks
    ### Other Liabilities
    'H8B3095NLGCMG', # Other Liabilities, Large Domestically Chartered Commercial Banks
    ### Other Loans and Leases
    'H8B3305NLGCMG', # Other Loans and Leases: All Other Loans and Leases, Large Domestically Chartered Commercial Banks
    'B1030NLGCMG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Large Domestically Chartered Commercial Banks
    'B2310NLGCMG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Large Domestically Chartered Commercial Banks
    ### Other Securities
    'H8B1011NLGCMG', # Other Securities, Large Domestically Chartered Commercial Banks
    'H8B1303NLGCMG', # Other Securities: Mortgage-Backed Securities, Large Domestically Chartered Commercial Banks
    'H8B1304NLGCMG', # Other Securities: Non-MBS, Large Domestically Chartered Commercial Banks
    ### Real Estate Loans
    'H8B1026NLGCMG', # Real Estate Loans, Large Domestically Chartered Commercial Banks
    'H8B3219NLGCMG', # Real Estate Loans: Commercial Real Estate Loans, Large Domestically Chartered Commercial Banks
    'B1215NLGCMG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Large Domestically Chartered Commercial Banks
    'B1216NLGCMG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Large Domestically Chartered Commercial Banks
    'B1217NLGCMG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Large Domestically Chartered Commercial Banks
    'B1218NLGCMG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Large Domestically Chartered Commercial Banks
    'H8B1221NLGCMG', # Real Estate Loans: Residential Real Estate Loans, Large Domestically Chartered Commercial Banks
    'H8B1220NLGCMG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Large Domestically Chartered Commercial Banks
    'H8B1027NLGCMG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Large Domestically Chartered Commercial Banks
    ### Residual (Assets Less Liabilities)
    'H8B1091NLGCMG', # Residual (Assets Less Liabilities), Large Domestically Chartered Commercial Banks
    ### Securities in Bank Credit
    'H8B1002NLGCMG', # Securities in Bank Credit, Large Domestically Chartered Commercial Banks
    ### Total Assets
    'H8B1151NLGCMG', # Total Assets, Large Domestically Chartered Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NLGCMG', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Large Domestically Chartered Commercial Banks
    ### Total Liabilities
    'H8B1152NLGCMG', # Total Liabilities, Large Domestically Chartered Commercial Banks
    ### Treasury and Agency Securities
    'H8B1003NLGCMG', # Treasury and Agency Securities, Large Domestically Chartered Commercial Banks
    'H8B1301NLGCMG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Large Domestically Chartered Commercial Banks
    'H8B1302NLGCMG', # Treasury and Agency Securities: Non-MBS, Large Domestically Chartered Commercial Banks

    # Small Domestically Chartered Commercial Banks (174)
    ## 잔액 (Bil. of U.S. $, 계절조정)
    ### Bank Credit
    'BC0SCBM027SBOG', # Bank Credit, Small Domestically Chartered Commercial Banks
    ### Borrowings
    'BOWSCBM027SBOG', # Borrowings, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Borrowings from Banks in the U.S.
    'BBUSCBM027SBOG', # Borrowings from Banks in the U.S., Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Borrowings from Others
    'BFOSCBM027SBOG', # Borrowings from Others, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Cash Assets
    'CASSCBM027SBOG', # Cash Assets, Small Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans
    'CILSCBM027SBOG', # Commercial and Industrial Loans, Small Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans to U.S. Addressees
    'CIUSCBM027SBOG', # Commercial and Industrial Loans to U.S. Addressees, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Consumer Loans
    'CLSSCBM027SBOG', # Consumer Loans, Small Domestically Chartered Commercial Banks
    'CCLSCBM027SBOG', # Consumer Loans: Credit Cards and Other Revolving Plans, Small Domestically Chartered Commercial Banks
    'OCLSCBM027SBOG', # Consumer Loans: Other Consumer Loans, Small Domestically Chartered Commercial Banks
    'AOCSCBM027SBOG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    'CARSCBM027SBOG', # Consumer Loans: Other Consumer Loans: Automobile Loans, Small Domestically Chartered Commercial Banks
    ### Deposits
    'DPSSCBM027SBOG', # Deposits, Small Domestically Chartered Commercial Banks
    ### Derivatives with a Negative Fair Value
    'DNVSCBM027SBOG', # Derivatives with a Negative Fair Value, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Derivatives with a Positive Fair Value
    'DFVSCBM027SBOG', # Derivatives with a Positive Fair Value, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Fed Funds and Reverse RPs with Banks
    'FRPSCBM027SBOG', # Fed Funds and Reverse RPs with Banks, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Interbank Loans
    'IBLSCBM027SBOG', # Interbank Loans, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Allowance for Credit Losses on Loans and Leases
    'ALLSCBM027SBOG', # LESS: Allowance for Credit Losses on Loans and Leases, Small Domestically Chartered Commercial Banks
    ### Large Time Deposits
    'LTDSCBM027SBOG', # Large Time Deposits, Small Domestically Chartered Commercial Banks
    ### Loans Secured by Nonfarm Nonresidential Properties
    'NNPSCBM027SBOG', # Loans Secured by Nonfarm Nonresidential Properties, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Loans and Leases in Bank Credit
    'LLBSCBM027SBOG', # Loans and Leases in Bank Credit, Small Domestically Chartered Commercial Banks
    ### Loans to Commercial Banks
    'LCBSCBM027SBOG', # Loans to Commercial Banks, Small Domestically Chartered Commercial Banks
    ### Loans with Original Amounts of $1,000,000 or Less
    'LLMSCBM027SBOG', # Loans with Original Amounts of $1,000,000 or Less, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Net Due to Related Foreign Offices
    'NDFSCBM027SBOG', # Net Due to Related Foreign Offices, Small Domestically Chartered Commercial Banks
    ### Net Unrealized Gains (Losses) on Available-for-Sale Securities
    'NUGSCBM027SBOG', # Net Unrealized Gains (Losses) on Available-for-Sale Securities, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Assets
    'OATSCBM027SBOG', # Other Assets, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Deposits
    'ODSSCBM027SBOG', # Other Deposits, Small Domestically Chartered Commercial Banks
    ### Other Liabilities
    'OLSSCBM027SBOG', # Other Liabilities, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Loans and Leases
    'OLLSCBM027SBOG', # Other Loans and Leases, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    'AOLSCBM027SBOG', # Other Loans and Leases: All Other Loans and Leases, Small Domestically Chartered Commercial Banks
    'LNFSCBM027SBOG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Small Domestically Chartered Commercial Banks
    'OLNSCBM027SBOG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    'OLRSCBM027SBOG', # Other Loans and Leases: Fed Funds and Reverse RPs with Nonbanks, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Securities
    'OSESCBM027SBOG', # Other Securities, Small Domestically Chartered Commercial Banks
    'OMBSCBM027SBOG', # Other Securities: Mortgage-Backed Securities, Small Domestically Chartered Commercial Banks
    'ONMSCBM027SBOG', # Other Securities: Non-MBS, Small Domestically Chartered Commercial Banks
    ### Other Securitized Consumer Loans
    'OSCSCBM027SBOG', # Other Securitized Consumer Loans, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Trading Assets
    'OTASCBM027SBOG', # Other Trading Assets, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Trading Liabilities
    'OTLSCBM027SBOG', # Other Trading Liabilities, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Real Estate Loans
    'RELSCBM027SBOG', # Real Estate Loans, Small Domestically Chartered Commercial Banks
    'CRESCBM027SBOG', # Real Estate Loans: Commercial Real Estate Loans, Small Domestically Chartered Commercial Banks
    'CLDSCBM027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Small Domestically Chartered Commercial Banks
    'SBFSCBM027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Small Domestically Chartered Commercial Banks
    'SMPSCBM027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Small Domestically Chartered Commercial Banks
    'SNFSCBM027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Small Domestically Chartered Commercial Banks
    'RRESCBM027SBOG', # Real Estate Loans: Residential Real Estate Loans, Small Domestically Chartered Commercial Banks
    'CRLSCBM027SBOG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Small Domestically Chartered Commercial Banks
    'RHESCBM027SBOG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Small Domestically Chartered Commercial Banks
    ### Residual (Assets Less Liabilities)
    'RALSCBM027SBOG', # Residual (Assets Less Liabilities), Small Domestically Chartered Commercial Banks
    ### Securities in Bank Credit
    'SBCSCBM027SBOG', # Securities in Bank Credit, Small Domestically Chartered Commercial Banks
    ### Securitized Consumer Loans
    'SCLSCBM027SBOG', # Securitized Consumer Loans, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Securitized Credit Cards and Other Revolving Plans
    'SCCSCBM027SBOG', # Securitized Credit Cards and Other Revolving Plans, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Securitized Real Estate Loans
    'SRESCBM027SBOG', # Securitized Real Estate Loans, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Total Assets
    'TLASCBM027SBOG', # Total Assets, Small Domestically Chartered Commercial Banks
    ### Total Liabilities
    'TLBSCBM027SBOG', # Total Liabilities, Small Domestically Chartered Commercial Banks
    ### Trading Assets
    'TDASCBM027SBOG', # Trading Assets, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Trading Liabilities
    'TLSSCBM027SBOG', # Trading Liabilities, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Treasury and Agency Securities
    'TASSCBM027SBOG', # Treasury and Agency Securities, Small Domestically Chartered Commercial Banks
    'TMBSCBM027SBOG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Small Domestically Chartered Commercial Banks
    'TNMSCBM027SBOG', # Treasury and Agency Securities: Non-MBS, Small Domestically Chartered Commercial Banks
    ### U.S. Treasury and Agency Securities, MBS
    'TAMSCBM027SBOG', # U.S. Treasury and Agency Securities, MBS, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ## 잔액 (Mil. of U.S. $, 계절조정)
    ### Borrowings
    'H8B3094NSMAM', # Borrowings, Small Domestically Chartered Commercial Banks
    ### Consumer Loans
    'B2245NSMAM', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Small Domestically Chartered Commercial Banks
    ### Other Assets
    'H8B3053NSMAM', # Other Assets, Small Domestically Chartered Commercial Banks
    ### Other Liabilities
    'H8B3095NSMAM', # Other Liabilities, Small Domestically Chartered Commercial Banks
    ### Other Loans and Leases
    'B2310NSMAM', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Small Domestically Chartered Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NSMAM', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Small Domestically Chartered Commercial Banks
    ## 잔액 (Bil. of U.S. $, 원계열)
    ### Bank Credit
    'BC0SCBM027NBOG', # Bank Credit, Small Domestically Chartered Commercial Banks
    ### Borrowings
    'BOWSCBM027NBOG', # Borrowings, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Borrowings from Banks in the U.S.
    'BBUSCBM027NBOG', # Borrowings from Banks in the U.S., Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Borrowings from Others
    'BFOSCBM027NBOG', # Borrowings from Others, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Cash Assets
    'CASSCBM027NBOG', # Cash Assets, Small Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans
    'CILSCBM027NBOG', # Commercial and Industrial Loans, Small Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans to U.S. Addressees
    'CIUSCBM027NBOG', # Commercial and Industrial Loans to U.S. Addressees, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Consumer Loans
    'CLSSCBM027NBOG', # Consumer Loans, Small Domestically Chartered Commercial Banks
    'CCLSCBM027NBOG', # Consumer Loans: Credit Cards and Other Revolving Plans, Small Domestically Chartered Commercial Banks
    'OCLSCBM027NBOG', # Consumer Loans: Other Consumer Loans, Small Domestically Chartered Commercial Banks
    'AOCSCBM027NBOG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    'CARSCBM027NBOG', # Consumer Loans: Other Consumer Loans: Automobile Loans, Small Domestically Chartered Commercial Banks
    ### Deposits
    'DPSSCBM027NBOG', # Deposits, Small Domestically Chartered Commercial Banks
    ### Derivatives with a Negative Fair Value
    'DNVSCBM027NBOG', # Derivatives with a Negative Fair Value, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Derivatives with a Positive Fair Value
    'DFVSCBM027NBOG', # Derivatives with a Positive Fair Value, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Fed Funds and Reverse RPs with Banks
    'FRPSCBM027NBOG', # Fed Funds and Reverse RPs with Banks, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Interbank Loans
    'IBLSCBM027NBOG', # Interbank Loans, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Allowance for Credit Losses on Loans and Leases
    'ALLSCBM027NBOG', # LESS: Allowance for Credit Losses on Loans and Leases, Small Domestically Chartered Commercial Banks
    ### Large Time Deposits
    'LTDSCBM027NBOG', # Large Time Deposits, Small Domestically Chartered Commercial Banks
    ### Loans Secured by Nonfarm Nonresidential Properties
    'NNPSCBM027NBOG', # Loans Secured by Nonfarm Nonresidential Properties, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Loans and Leases in Bank Credit
    'LLBSCBM027NBOG', # Loans and Leases in Bank Credit, Small Domestically Chartered Commercial Banks
    ### Loans to Commercial Banks
    'LCBSCBM027NBOG', # Loans to Commercial Banks, Small Domestically Chartered Commercial Banks
    ### Loans with Original Amounts of $1,000,000 or Less
    'LLMSCBM027NBOG', # Loans with Original Amounts of $1,000,000 or Less, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Net Due to Related Foreign Offices
    'NDFSCBM027NBOG', # Net Due to Related Foreign Offices, Small Domestically Chartered Commercial Banks
    ### Net Unrealized Gains (Losses) on Available-for-Sale Securities
    'NUGSCBM027NBOG', # Net Unrealized Gains (Losses) on Available-for-Sale Securities, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Assets
    'OATSCBM027NBOG', # Other Assets, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Deposits
    'ODSSCBM027NBOG', # Other Deposits, Small Domestically Chartered Commercial Banks
    ### Other Liabilities
    'OLSSCBM027NBOG', # Other Liabilities, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Loans and Leases
    'OLLSCBM027NBOG', # Other Loans and Leases, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    'AOLSCBM027NBOG', # Other Loans and Leases: All Other Loans and Leases, Small Domestically Chartered Commercial Banks
    'LNFSCBM027NBOG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Small Domestically Chartered Commercial Banks
    'OLNSCBM027NBOG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    'OLRSCBM027NBOG', # Other Loans and Leases: Fed Funds and Reverse RPs with Nonbanks, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Securities
    'OSESCBM027NBOG', # Other Securities, Small Domestically Chartered Commercial Banks
    'OMBSCBM027NBOG', # Other Securities: Mortgage-Backed Securities, Small Domestically Chartered Commercial Banks
    'ONMSCBM027NBOG', # Other Securities: Non-MBS, Small Domestically Chartered Commercial Banks
    ### Other Securitized Consumer Loans
    'OSCSCBM027NBOG', # Other Securitized Consumer Loans, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Trading Assets
    'OTASCBM027NBOG', # Other Trading Assets, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Other Trading Liabilities
    'OTLSCBM027NBOG', # Other Trading Liabilities, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Real Estate Loans
    'RELSCBM027NBOG', # Real Estate Loans, Small Domestically Chartered Commercial Banks
    'CRESCBM027NBOG', # Real Estate Loans: Commercial Real Estate Loans, Small Domestically Chartered Commercial Banks
    'CLDSCBM027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Small Domestically Chartered Commercial Banks
    'SBFSCBM027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Small Domestically Chartered Commercial Banks
    'SMPSCBM027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Small Domestically Chartered Commercial Banks
    'SNFSCBM027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Small Domestically Chartered Commercial Banks
    'RRESCBM027NBOG', # Real Estate Loans: Residential Real Estate Loans, Small Domestically Chartered Commercial Banks
    'CRLSCBM027NBOG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Small Domestically Chartered Commercial Banks
    'RHESCBM027NBOG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Small Domestically Chartered Commercial Banks
    ### Residual (Assets Less Liabilities)
    'RALSCBM027NBOG', # Residual (Assets Less Liabilities), Small Domestically Chartered Commercial Banks
    ### Securities in Bank Credit
    'SBCSCBM027NBOG', # Securities in Bank Credit, Small Domestically Chartered Commercial Banks
    ### Securitized Consumer Loans
    'SCLSCBM027NBOG', # Securitized Consumer Loans, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Securitized Credit Cards and Other Revolving Plans
    'SCCSCBM027NBOG', # Securitized Credit Cards and Other Revolving Plans, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Securitized Real Estate Loans
    'SRESCBM027NBOG', # Securitized Real Estate Loans, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Total Assets
    'TLASCBM027NBOG', # Total Assets, Small Domestically Chartered Commercial Banks
    ### Total Liabilities
    'TLBSCBM027NBOG', # Total Liabilities, Small Domestically Chartered Commercial Banks
    ### Trading Assets
    'TDASCBM027NBOG', # Trading Assets, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Trading Liabilities
    'TLSSCBM027NBOG', # Trading Liabilities, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ### Treasury and Agency Securities
    'TASSCBM027NBOG', # Treasury and Agency Securities, Small Domestically Chartered Commercial Banks
    'TMBSCBM027NBOG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Small Domestically Chartered Commercial Banks
    'TNMSCBM027NBOG', # Treasury and Agency Securities: Non-MBS, Small Domestically Chartered Commercial Banks
    ### U.S. Treasury and Agency Securities, MBS
    'TAMSCBM027NBOG', # U.S. Treasury and Agency Securities, MBS, Small Domestically Chartered Commercial Banks (DISCONTINUED)
    ## 잔액 (Mil. of U.S. $, 원계열)
    ### Borrowings
    'H8B3094NSMDM', # Borrowings, Small Domestically Chartered Commercial Banks
    ### Consumer Loans
    'B2245NSMDM', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Small Domestically Chartered Commercial Banks
    ### Other Assets
    'H8B3053NSMDM', # Other Assets, Small Domestically Chartered Commercial Banks
    ### Other Liabilities
    'H8B3095NSMDM', # Other Liabilities, Small Domestically Chartered Commercial Banks
    ### Other Loans and Leases
    'B2310NSMDM', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Small Domestically Chartered Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NSMDM', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Small Domestically Chartered Commercial Banks
    ## 증가율 (% Chg. at Annual Rate, SA)
    ### Bank Credit
    'H8B1001NSMCMG', # Bank Credit, Small Domestically Chartered Commercial Banks
    ### Borrowings
    'H8B3094NSMCMG', # Borrowings, Small Domestically Chartered Commercial Banks
    ### Cash Assets
    'H8B1048NSMCMG', # Cash Assets, Small Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans
    'H8B1023NSMCMG', # Commercial and Industrial Loans, Small Domestically Chartered Commercial Banks
    ### Consumer Loans
    'H8B1029NSMCMG', # Consumer Loans, Small Domestically Chartered Commercial Banks
    'H8B1247NSMCMG', # Consumer Loans: Credit Cards and Other Revolving Plans, Small Domestically Chartered Commercial Banks
    'H8B3248NSMCMG', # Consumer Loans: Other Consumer Loans, Small Domestically Chartered Commercial Banks
    'B2245NSMCMG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Small Domestically Chartered Commercial Banks
    'B1243NSMCMG', # Consumer Loans: Other Consumer Loans: Automobile Loans, Small Domestically Chartered Commercial Banks
    ### Deposits
    'H8B1058NSMCMG', # Deposits, Small Domestically Chartered Commercial Banks
    ### Allowance for Credit Losses on Loans and Leases
    'H8B1043NSMCMG', # LESS: Allowance for Credit Losses on Loans and Leases, Small Domestically Chartered Commercial Banks
    ### Large Time Deposits
    'H8B1072NSMCMG', # Large Time Deposits, Small Domestically Chartered Commercial Banks
    ### Loans and Leases in Bank Credit
    'H8B1020NSMCMG', # Loans and Leases in Bank Credit, Small Domestically Chartered Commercial Banks
    ### Loans to Commercial Banks
    'H8B1047NSMCMG', # Loans to Commercial Banks, Small Domestically Chartered Commercial Banks
    ### Other Assets
    'H8B3053NSMCMG', # Other Assets, Small Domestically Chartered Commercial Banks
    ### Other Deposits
    'H8B1110NSMCMG', # Other Deposits, Small Domestically Chartered Commercial Banks
    ### Other Liabilities
    'H8B3095NSMCMG', # Other Liabilities, Small Domestically Chartered Commercial Banks
    ### Other Loans and Leases
    'H8B3305NSMCMG', # Other Loans and Leases: All Other Loans and Leases, Small Domestically Chartered Commercial Banks
    'B1030NSMCMG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Small Domestically Chartered Commercial Banks
    'B2310NSMCMG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Small Domestically Chartered Commercial Banks
    ### Other Securities
    'H8B1011NSMCMG', # Other Securities, Small Domestically Chartered Commercial Banks
    'H8B1303NSMCMG', # Other Securities: Mortgage-Backed Securities, Small Domestically Chartered Commercial Banks
    'H8B1304NSMCMG', # Other Securities: Non-MBS, Small Domestically Chartered Commercial Banks
    ### Real Estate Loans
    'H8B1026NSMCMG', # Real Estate Loans, Small Domestically Chartered Commercial Banks
    'H8B3219NSMCMG', # Real Estate Loans: Commercial Real Estate Loans, Small Domestically Chartered Commercial Banks
    'B1215NSMCMG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Small Domestically Chartered Commercial Banks
    'B1216NSMCMG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Small Domestically Chartered Commercial Banks
    'B1217NSMCMG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Small Domestically Chartered Commercial Banks
    'B1218NSMCMG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Small Domestically Chartered Commercial Banks
    'H8B1221NSMCMG', # Real Estate Loans: Residential Real Estate Loans, Small Domestically Chartered Commercial Banks
    'H8B1220NSMCMG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Small Domestically Chartered Commercial Banks
    'H8B1027NSMCMG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Small Domestically Chartered Commercial Banks
    ### Residual (Assets Less Liabilities)
    'H8B1091NSMCMG', # Residual (Assets Less Liabilities), Small Domestically Chartered Commercial Banks
    ### Securities in Bank Credit
    'H8B1002NSMCMG', # Securities in Bank Credit, Small Domestically Chartered Commercial Banks
    ### Total Assets
    'H8B1151NSMCMG', # Total Assets, Small Domestically Chartered Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NSMCMG', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Small Domestically Chartered Commercial Banks
    ### Total Liabilities
    'H8B1152NSMCMG', # Total Liabilities, Small Domestically Chartered Commercial Banks
    ### Treasury and Agency Securities
    'H8B1003NSMCMG', # Treasury and Agency Securities, Small Domestically Chartered Commercial Banks
    'H8B1301NSMCMG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Small Domestically Chartered Commercial Banks
    'H8B1302NSMCMG', # Treasury and Agency Securities: Non-MBS, Small Domestically Chartered Commercial Banks

    # Foreign-Related Institutions (171)
    ## 잔액 (Bil. of U.S. $, 계절조정)
    ### Bank Credit
    'BC0FRIM027SBOG', # Bank Credit, Foreign-Related Institutions
    ### Borrowings
    'BOWFRIM027SBOG', # Borrowings, Foreign-Related Institutions (DISCONTINUED)
    ### Borrowings from Banks in the U.S.
    'BBUFRIM027SBOG', # Borrowings from Banks in the U.S., Foreign-Related Institutions (DISCONTINUED)
    ### Borrowings from Others
    'BFOFRIM027SBOG', # Borrowings from Others, Foreign-Related Institutions (DISCONTINUED)
    ### Cash Assets
    'CASFRIM027SBOG', # Cash Assets, Foreign-Related Institutions
    ### Commercial and Industrial Loans
    'CILFRIM027SBOG', # Commercial and Industrial Loans, Foreign-Related Institutions
    ### Commercial and Industrial Loans to U.S. Addressees
    'CIUFRIM027SBOG', # Commercial and Industrial Loans to U.S. Addressees, Foreign-Related Institutions (DISCONTINUED)
    ### Consumer Loans
    'CLSFRIM027SBOG', # Consumer Loans, Foreign-Related Institutions
    'CCLFRIM027SBOG', # Consumer Loans: Credit Cards and Other Revolving Plans, Foreign-Related Institutions
    'OCLFRIM027SBOG', # Consumer Loans: Other Consumer Loans, Foreign-Related Institutions
    'AOCFRIM027SBOG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Foreign-Related Institutions (DISCONTINUED)
    'CARFRIM027SBOG', # Consumer Loans: Other Consumer Loans: Automobile Loans, Foreign-Related Institutions
    ### Deposits
    'DPSFRIM027SBOG', # Deposits, Foreign-Related Institutions
    ### Derivatives with a Negative Fair Value
    'DNVFRIM027SBOG', # Derivatives with a Negative Fair Value, Foreign-Related Institutions (DISCONTINUED)
    ### Derivatives with a Positive Fair Value
    'DFVFRIM027SBOG', # Derivatives with a Positive Fair Value, Foreign-Related Institutions (DISCONTINUED)
    ### Fed Funds and Reverse RPs with Banks
    'FRPFRIM027SBOG', # Fed Funds and Reverse RPs with Banks, Foreign-Related Institutions (DISCONTINUED)
    ### Interbank Loans
    'IBLFRIM027SBOG', # Interbank Loans, Foreign-Related Institutions (DISCONTINUED)
    ### Allowance for Credit Losses on Loans and Leases
    'ALLFRIM027SBOG', # LESS: Allowance for Credit Losses on Loans and Leases, Foreign-Related Institutions
    ### Large Time Deposits
    'LTDFRIM027SBOG', # Large Time Deposits, Foreign-Related Institutions
    ### Loans Secured by Nonfarm Nonresidential Properties
    'NNPFRIM027SBOG', # Loans Secured by Nonfarm Nonresidential Properties, Foreign-Related Institutions (DISCONTINUED)
    ### Loans and Leases in Bank Credit
    'LLBFRIM027SBOG', # Loans and Leases in Bank Credit, Foreign-Related Institutions
    ### Loans to Commercial Banks
    'LCBFRIM027SBOG', # Loans to Commercial Banks, Foreign-Related Institutions
    ### Loans with Original Amounts of $1,000,000 or Less
    'LLMFRIM027SBOG', # Loans with Original Amounts of $1,000,000 or Less, Foreign-Related Institutions (DISCONTINUED)
    ### Net Due to Related Foreign Offices
    'NDFFRIM027SBOG', # Net Due to Related Foreign Offices, Foreign-Related Institutions
    ### Net Unrealized Gains (Losses) on Available-for-Sale Securities
    'NUGFRIM027SBOG', # Net Unrealized Gains (Losses) on Available-for-Sale Securities, Foreign-Related Institutions (DISCONTINUED)
    ### Other Assets
    'OATFRIM027SBOG', # Other Assets, Foreign-Related Institutions (DISCONTINUED)
    ### Other Deposits
    'ODSFRIM027SBOG', # Other Deposits, Foreign-Related Institutions
    ### Other Liabilities
    'OLSFRIM027SBOG', # Other Liabilities, Foreign-Related Institutions (DISCONTINUED)
    ### Other Loans and Leases
    'OLLFRIM027SBOG', # Other Loans and Leases, Foreign-Related Institutions (DISCONTINUED)
    'AOLFRIM027SBOG', # Other Loans and Leases: All Other Loans and Leases, Foreign-Related Institutions
    'LNFFRIM027SBOG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Foreign-Related Institutions
    'OLNFRIM027SBOG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Foreign-Related Institutions (DISCONTINUED)
    'OLRFRIM027SBOG', # Other Loans and Leases: Fed Funds and Reverse RPs with Nonbanks, Foreign-Related Institutions (DISCONTINUED)
    ### Other Securities
    'OSEFRIM027SBOG', # Other Securities, Foreign-Related Institutions
    'OMBFRIM027SBOG', # Other Securities: Mortgage-Backed Securities, Foreign-Related Institutions
    'ONMFRIM027SBOG', # Other Securities: Non-MBS, Foreign-Related Institutions
    ### Other Securitized Consumer Loans
    'OSCFRIM027SBOG', # Other Securitized Consumer Loans, Foreign-Related Institutions (DISCONTINUED)
    ### Other Trading Assets
    'OTAFRIM027SBOG', # Other Trading Assets, Foreign-Related Institutions (DISCONTINUED)
    ### Other Trading Liabilities
    'OTLFRIM027SBOG', # Other Trading Liabilities, Foreign-Related Institutions (DISCONTINUED)
    ### Real Estate Loans
    'RELFRIM027SBOG', # Real Estate Loans, Foreign-Related Institutions
    'CREFRIM027SBOG', # Real Estate Loans: Commercial Real Estate Loans, Foreign-Related Institutions
    'CLDFRIM027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Foreign-Related Institutions
    'SBFFRIM027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Foreign-Related Institutions
    'SMPFRIM027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Foreign-Related Institutions
    'SNFFRIM027SBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Foreign-Related Institutions
    'RREFRIM027SBOG', # Real Estate Loans: Residential Real Estate Loans, Foreign-Related Institutions
    'CRLFRIM027SBOG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Foreign-Related Institutions
    'RHEFRIM027SBOG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Foreign-Related Institutions
    ### Residual (Assets Less Liabilities)
    'RALFRIM027SBOG', # Residual (Assets Less Liabilities), Foreign-Related Institutions
    ### Securities in Bank Credit
    'SBCFRIM027SBOG', # Securities in Bank Credit, Foreign-Related Institutions
    ### Securitized Consumer Loans
    'SCLFRIM027SBOG', # Securitized Consumer Loans, Foreign-Related Institutions (DISCONTINUED)
    ### Securitized Credit Cards and Other Revolving Plans
    'SCCFRIM027SBOG', # Securitized Credit Cards and Other Revolving Plans, Foreign-Related Institutions (DISCONTINUED)
    ### Securitized Real Estate Loans
    'SREFRIM027SBOG', # Securitized Real Estate Loans, Foreign-Related Institutions (DISCONTINUED)
    ### Total Assets
    'TLAFRIM027SBOG', # Total Assets, Foreign-Related Institutions
    ### Total Liabilities
    'TLBFRIM027SBOG', # Total Liabilities, Foreign-Related Institutions
    ### Trading Assets
    'TDAFRIM027SBOG', # Trading Assets, Foreign-Related Institutions (DISCONTINUED)
    ### Trading Liabilities
    'TLSFRIM027SBOG', # Trading Liabilities, Foreign-Related Institutions (DISCONTINUED)
    ### Treasury and Agency Securities
    'TASFRIM027SBOG', # Treasury and Agency Securities, Foreign-Related Institutions
    'TMBFRIM027SBOG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Foreign-Related Institutions
    'TNMFRIM027SBOG', # Treasury and Agency Securities: Non-MBS, Foreign-Related Institutions
    ### U.S. Treasury and Agency Securities, MBS
    'TAMFRIM027SBOG', # U.S. Treasury and Agency Securities, MBS, Foreign-Related Institutions (DISCONTINUED)
    ## 잔액 (Mil. of U.S. $, 계절조정)
    ### Borrowings
    'H8B3094NFRAM', # Borrowings, Foreign-Related Institutions
    ### Consumer Loans
    'B2245NFRAM', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Foreign-Related Institutions
    ### Other Assets
    'H8B3053NFRAM', # Other Assets, Foreign-Related Institutions
    ### Other Liabilities
    'H8B3095NFRAM', # Other Liabilities, Foreign-Related Institutions
    ### Other Loans and Leases
    'B2310NFRAM', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Foreign-Related Institutions
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NFRAM', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Foreign-Related Institutions
    ## 잔액 (Bil. of U.S. $, 원계열)
    ### Bank Credit
    'BC0FRIM027NBOG', # Bank Credit, Foreign-Related Institutions
    ### Borrowings
    'BOWFRIM027NBOG', # Borrowings, Foreign-Related Institutions (DISCONTINUED)
    ### Borrowings from Banks in the U.S.
    'BBUFRIM027NBOG', # Borrowings from Banks in the U.S., Foreign-Related Institutions (DISCONTINUED)
    ### Borrowings from Others
    'BFOFRIM027NBOG', # Borrowings from Others, Foreign-Related Institutions (DISCONTINUED)
    ### Cash Assets
    'CASFRIM027NBOG', # Cash Assets, Foreign-Related Institutions
    ### Commercial and Industrial Loans
    'CILFRIM027NBOG', # Commercial and Industrial Loans, Foreign-Related Institutions
    ### Commercial and Industrial Loans to U.S. Addressees
    'CIUFRIM027NBOG', # Commercial and Industrial Loans to U.S. Addressees, Foreign-Related Institutions (DISCONTINUED)
    ### Consumer Loans
    'CLSFRIM027NBOG', # Consumer Loans, Foreign-Related Institutions
    'CCLFRIM027NBOG', # Consumer Loans: Credit Cards and Other Revolving Plans, Foreign-Related Institutions
    'OCLFRIM027NBOG', # Consumer Loans: Other Consumer Loans, Foreign-Related Institutions
    'AOCFRIM027NBOG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Foreign-Related Institutions (DISCONTINUED)
    'CARFRIM027NBOG', # Consumer Loans: Other Consumer Loans: Automobile Loans, Foreign-Related Institutions
    ### Deposits
    'DPSFRIM027NBOG', # Deposits, Foreign-Related Institutions
    ### Derivatives with a Negative Fair Value
    'DNVFRIM027NBOG', # Derivatives with a Negative Fair Value, Foreign-Related Institutions (DISCONTINUED)
    ### Derivatives with a Positive Fair Value
    'DFVFRIM027NBOG', # Derivatives with a Positive Fair Value, Foreign-Related Institutions (DISCONTINUED)
    ### Fed Funds and Reverse RPs with Banks
    'FRPFRIM027NBOG', # Fed Funds and Reverse RPs with Banks, Foreign-Related Institutions (DISCONTINUED)
    ### Interbank Loans
    'IBLFRIM027NBOG', # Interbank Loans, Foreign-Related Institutions (DISCONTINUED)
    ### Allowance for Credit Losses on Loans and Leases
    'ALLFRIM027NBOG', # LESS: Allowance for Credit Losses on Loans and Leases, Foreign-Related Institutions
    ### Large Time Deposits
    'LTDFRIM027NBOG', # Large Time Deposits, Foreign-Related Institutions
    ### Loans Secured by Nonfarm Nonresidential Properties
    'NNPFRIM027NBOG', # Loans Secured by Nonfarm Nonresidential Properties, Foreign-Related Institutions (DISCONTINUED)
    ### Loans and Leases in Bank Credit
    'LLBFRIM027NBOG', # Loans and Leases in Bank Credit, Foreign-Related Institutions
    ### Loans to Commercial Banks
    'LCBFRIM027NBOG', # Loans to Commercial Banks, Foreign-Related Institutions
    ### Loans with Original Amounts of $1,000,000 or Less
    'LLMFRIM027NBOG', # Loans with Original Amounts of $1,000,000 or Less, Foreign-Related Institutions (DISCONTINUED)
    ### Net Due to Related Foreign Offices
    'NDFFRIM027NBOG', # Net Due to Related Foreign Offices, Foreign-Related Institutions
    ### Net Unrealized Gains (Losses) on Available-for-Sale Securities
    'NUGFRIM027NBOG', # Net Unrealized Gains (Losses) on Available-for-Sale Securities, Foreign-Related Institutions (DISCONTINUED)
    ### Other Assets
    'OATFRIM027NBOG', # Other Assets, Foreign-Related Institutions (DISCONTINUED)
    ### Other Deposits
    'ODSFRIM027NBOG', # Other Deposits, Foreign-Related Institutions
    ### Other Liabilities
    'OLSFRIM027NBOG', # Other Liabilities, Foreign-Related Institutions (DISCONTINUED)
    ### Other Loans and Leases
    'OLLFRIM027NBOG', # Other Loans and Leases, Foreign-Related Institutions (DISCONTINUED)
    'AOLFRIM027NBOG', # Other Loans and Leases: All Other Loans and Leases, Foreign-Related Institutions
    'LNFFRIM027NBOG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Foreign-Related Institutions
    'OLNFRIM027NBOG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Foreign-Related Institutions (DISCONTINUED)
    'OLRFRIM027NBOG', # Other Loans and Leases: Fed Funds and Reverse RPs with Nonbanks, Foreign-Related Institutions (DISCONTINUED)
    ### Other Securities
    'OSEFRIM027NBOG', # Other Securities, Foreign-Related Institutions
    'OMBFRIM027NBOG', # Other Securities: Mortgage-Backed Securities, Foreign-Related Institutions
    'ONMFRIM027NBOG', # Other Securities: Non-MBS, Foreign-Related Institutions
    ### Other Securitized Consumer Loans
    'OSCFRIM027NBOG', # Other Securitized Consumer Loans, Foreign-Related Institutions (DISCONTINUED)
    ### Other Trading Assets
    'OTAFRIM027NBOG', # Other Trading Assets, Foreign-Related Institutions (DISCONTINUED)
    ### Other Trading Liabilities
    'OTLFRIM027NBOG', # Other Trading Liabilities, Foreign-Related Institutions (DISCONTINUED)
    ### Real Estate Loans
    'RELFRIM027NBOG', # Real Estate Loans, Foreign-Related Institutions
    'CREFRIM027NBOG', # Real Estate Loans: Commercial Real Estate Loans, Foreign-Related Institutions
    'CLDFRIM027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Foreign-Related Institutions
    'SBFFRIM027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Foreign-Related Institutions
    'SMPFRIM027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Foreign-Related Institutions
    'SNFFRIM027NBOG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Foreign-Related Institutions
    'RREFRIM027NBOG', # Real Estate Loans: Residential Real Estate Loans, Foreign-Related Institutions
    'CRLFRIM027NBOG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Foreign-Related Institutions
    'RHEFRIM027NBOG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Foreign-Related Institutions
    ### Residual (Assets Less Liabilities)
    'RALFRIM027NBOG', # Residual (Assets Less Liabilities), Foreign-Related Institutions
    ### Securities in Bank Credit
    'SBCFRIM027NBOG', # Securities in Bank Credit, Foreign-Related Institutions
    ### Securitized Consumer Loans
    'SCLFRIM027NBOG', # Securitized Consumer Loans, Foreign-Related Institutions (DISCONTINUED)
    ### Securitized Credit Cards and Other Revolving Plans
    'SCCFRIM027NBOG', # Securitized Credit Cards and Other Revolving Plans, Foreign-Related Institutions (DISCONTINUED)
    ### Securitized Real Estate Loans
    'SREFRIM027NBOG', # Securitized Real Estate Loans, Foreign-Related Institutions (DISCONTINUED)
    ### Total Assets
    'TLAFRIM027NBOG', # Total Assets, Foreign-Related Institutions
    ### Total Liabilities
    'TLBFRIM027NBOG', # Total Liabilities, Foreign-Related Institutions
    ### Trading Assets
    'TDAFRIM027NBOG', # Trading Assets, Foreign-Related Institutions (DISCONTINUED)
    ### Trading Liabilities
    'TLSFRIM027NBOG', # Trading Liabilities, Foreign-Related Institutions (DISCONTINUED)
    ### Treasury and Agency Securities
    'TASFRIM027NBOG', # Treasury and Agency Securities, Foreign-Related Institutions
    'TMBFRIM027NBOG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Foreign-Related Institutions
    'TNMFRIM027NBOG', # Treasury and Agency Securities: Non-MBS, Foreign-Related Institutions
    ### U.S. Treasury and Agency Securities, MBS
    'TAMFRIM027NBOG', # U.S. Treasury and Agency Securities, MBS, Foreign-Related Institutions (DISCONTINUED)
    ## 잔액 (Mil. of U.S. $, 원계열)
    ### Borrowings
    'H8B3094NFRDM', # Borrowings, Foreign-Related Institutions
    ### Consumer Loans
    'B2245NFRDM', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Foreign-Related Institutions
    ### Other Assets
    'H8B3053NFRDM', # Other Assets, Foreign-Related Institutions
    ### Other Liabilities
    'H8B3095NFRDM', # Other Liabilities, Foreign-Related Institutions
    ### Other Loans and Leases
    'B2310NFRDM', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Foreign-Related Institutions
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NFRDM', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Foreign-Related Institutions
    ## 증가율 (% Chg. at Annual Rate, SA)
    ### Bank Credit
    'H8B1001NFRCMG', # Bank Credit, Foreign-Related Institutions
    ### Borrowings
    'H8B3094NFRCMG', # Borrowings, Foreign-Related Institutions
    ### Cash Assets
    'H8B1048NFRCMG', # Cash Assets, Foreign-Related Institutions
    ### Commercial and Industrial Loans
    'H8B1023NFRCMG', # Commercial and Industrial Loans, Foreign-Related Institutions
    ### Consumer Loans
    'H8B1029NFRCMG', # Consumer Loans, Foreign-Related Institutions
    'H8B3248NFRCMG', # Consumer Loans: Other Consumer Loans, Foreign-Related Institutions
    ### Deposits
    'H8B1058NFRCMG', # Deposits, Foreign-Related Institutions
    ### Allowance for Credit Losses on Loans and Leases
    'H8B1043NFRCMG', # LESS: Allowance for Credit Losses on Loans and Leases, Foreign-Related Institutions
    ### Large Time Deposits
    'H8B1072NFRCMG', # Large Time Deposits, Foreign-Related Institutions
    ### Loans and Leases in Bank Credit
    'H8B1020NFRCMG', # Loans and Leases in Bank Credit, Foreign-Related Institutions
    ### Loans to Commercial Banks
    'H8B1047NFRCMG', # Loans to Commercial Banks, Foreign-Related Institutions
    ### Other Assets
    'H8B3053NFRCMG', # Other Assets, Foreign-Related Institutions
    ### Other Deposits
    'H8B1110NFRCMG', # Other Deposits, Foreign-Related Institutions
    ### Other Liabilities
    'H8B3095NFRCMG', # Other Liabilities, Foreign-Related Institutions
    ### Other Loans and Leases
    'H8B3305NFRCMG', # Other Loans and Leases: All Other Loans and Leases, Foreign-Related Institutions
    'B1030NFRCMG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Foreign-Related Institutions
    'B2310NFRCMG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Foreign-Related Institutions
    ### Other Securities
    'H8B1011NFRCMG', # Other Securities, Foreign-Related Institutions
    'H8B1303NFRCMG', # Other Securities: Mortgage-Backed Securities, Foreign-Related Institutions
    'H8B1304NFRCMG', # Other Securities: Non-MBS, Foreign-Related Institutions
    ### Real Estate Loans
    'H8B1026NFRCMG', # Real Estate Loans, Foreign-Related Institutions
    'H8B3219NFRCMG', # Real Estate Loans: Commercial Real Estate Loans, Foreign-Related Institutions
    'B1215NFRCMG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Foreign-Related Institutions
    'B1216NFRCMG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Foreign-Related Institutions
    'B1217NFRCMG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Foreign-Related Institutions
    'B1218NFRCMG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Foreign-Related Institutions
    'H8B1221NFRCMG', # Real Estate Loans: Residential Real Estate Loans, Foreign-Related Institutions
    'H8B1220NFRCMG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Foreign-Related Institutions
    'H8B1027NFRCMG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Foreign-Related Institutions
    ### Residual (Assets Less Liabilities)
    'H8B1091NFRCMG', # Residual (Assets Less Liabilities), Foreign-Related Institutions
    ### Securities in Bank Credit
    'H8B1002NFRCMG', # Securities in Bank Credit, Foreign-Related Institutions
    ### Total Assets
    'H8B1151NFRCMG', # Total Assets, Foreign-Related Institutions
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NFRCMG', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Foreign-Related Institutions
    ### Total Liabilities
    'H8B1152NFRCMG', # Total Liabilities, Foreign-Related Institutions
    ### Treasury and Agency Securities
    'H8B1003NFRCMG', # Treasury and Agency Securities, Foreign-Related Institutions
    'H8B1301NFRCMG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Foreign-Related Institutions
    'H8B1302NFRCMG', # Treasury and Agency Securities: Non-MBS, Foreign-Related Institutions
]

# Quarterly (204)
ids_Q = [
    # All Commercial Banks (47)
    ## 증가율 (% Chg. at Annual Rate, SA)
    ### Bank Credit
    'BC0ACBQ158SBOG', # Bank Credit, All Commercial Banks
    ### Borrowings
    'BOWACBQ158SBOG', # Borrowings, All Commercial Banks (DISCONTINUED)
    'H8B3094NCBCQG', # Borrowings, All Commercial Banks
    ### Cash Assets
    'CASACBQ158SBOG', # Cash Assets, All Commercial Banks
    ### Commercial and Industrial Loans
    'CILACBQ158SBOG', # Commercial and Industrial Loans, All Commercial Banks
    ### Consumer Loans
    'CLSACBQ158SBOG', # Consumer Loans, All Commercial Banks
    'CCLACBQ158SBOG', # Consumer Loans: Credit Cards and Other Revolving Plans, All Commercial Banks
    'OCLACBQ158SBOG', # Consumer Loans: Other Consumer Loans, All Commercial Banks
    'B2245NCBCQG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, All Commercial Banks
    'B1243NCBCQG', # Consumer Loans: Other Consumer Loans: Automobile Loans, All Commercial Banks
    ### Deposits
    'DPSACBQ158SBOG', # Deposits, All Commercial Banks
    ### Interbank Loans
    'IBLACBQ158SBOG', # Interbank Loans, All Commercial Banks (DISCONTINUED)
    ### Allowance for Credit Losses on Loans and Leases
    'ALLACBQ158SBOG', # LESS: Allowance for Credit Losses on Loans and Leases, All Commercial Banks
    ### Large Time Deposits
    'LTDACBQ158SBOG', # Large Time Deposits, All Commercial Banks
    ### Loans and Leases in Bank Credit
    'LLBACBQ158SBOG', # Loans and Leases in Bank Credit, All Commercial Banks
    ### Loans to Commercial Banks
    'H8B1047NCBCQG', # Loans to Commercial Banks, All Commercial Banks
    ### Other Assets
    'H8B3053NCBCQG', # Other Assets, All Commercial Banks
    'OATACBQ158SBOG', # Other Assets, All Commercial Banks (DISCONTINUED)
    ### Other Deposits
    'ODSACBQ158SBOG', # Other Deposits, All Commercial Banks
    ### Other Liabilities
    'H8B3095NCBCQG', # Other Liabilities, All Commercial Banks
    'OLSACBQ158SBOG', # Other Liabilities, All Commercial Banks (DISCONTINUED)
    ### Other Loans and Leases
    'OLLACBQ158SBOG', # Other Loans and Leases, All Commercial Banks (DISCONTINUED)
    'H8B3305NCBCQG', # Other Loans and Leases: All Other Loans and Leases, All Commercial Banks
    'B1030NCBCQG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, All Commercial Banks
    'B2310NCBCQG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, All Commercial Banks
    ### Other Securities
    'OSEACBQ158SBOG', # Other Securities, All Commercial Banks
    'H8B1303NCBCQG', # Other Securities: Mortgage-Backed Securities, All Commercial Banks
    'H8B1304NCBCQG', # Other Securities: Non-MBS, All Commercial Banks
    ### Real Estate Loans
    'RELACBQ158SBOG', # Real Estate Loans, All Commercial Banks
    'CREACBQ158SBOG', # Real Estate Loans: Commercial Real Estate Loans, All Commercial Banks
    'B1215NCBCQG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, All Commercial Banks
    'B1216NCBCQG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, All Commercial Banks
    'B1217NCBCQG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, All Commercial Banks
    'B1218NCBCQG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, All Commercial Banks
    'RREACBQ158SBOG', # Real Estate Loans: Residential Real Estate Loans, All Commercial Banks
    'CRLACBQ158SBOG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, All Commercial Banks
    'RHEACBQ158SBOG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, All Commercial Banks
    ### Residual (Assets Less Liabilities)
    'H8B1091NCBCQG', # Residual (Assets Less Liabilities), All Commercial Banks
    ### Securities in Bank Credit
    'SBCACBQ158SBOG', # Securities in Bank Credit, All Commercial Banks
    ### Total Assets
    'TLAACBQ158SBOG', # Total Assets, All Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NCBCQG', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, All Commercial Banks
    ### Total Liabilities
    'TLBACBQ158SBOG', # Total Liabilities, All Commercial Banks
    ### Trading Assets
    'TDAACBQ158SBOG', # Trading Assets, All Commercial Banks (DISCONTINUED)
    ### Trading Liabilities
    'TLSACBQ158SBOG', # Trading Liabilities, All Commercial Banks (DISCONTINUED)
    ### Treasury and Agency Securities
    'TASACBQ158SBOG', # Treasury and Agency Securities, All Commercial Banks
    'H8B1301NCBCQG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), All Commercial Banks
    'H8B1302NCBCQG', # Treasury and Agency Securities: Non-MBS, All Commercial Banks

    # Domestically Chartered Commercial Banks (40)
    ## 증가율 (% Chg. at Annual Rate, SA)
    ### Bank Credit
    'H8B1001NDMCQG', # Bank Credit, Domestically Chartered Commercial Banks
    ### Borrowings
    'H8B3094NDMCQG', # Borrowings, Domestically Chartered Commercial Banks
    ### Cash Assets
    'H8B1048NDMCQG', # Cash Assets, Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans
    'H8B1023NDMCQG', # Commercial and Industrial Loans, Domestically Chartered Commercial Banks
    ### Consumer Loans
    'H8B1029NDMCQG', # Consumer Loans, Domestically Chartered Commercial Banks
    'H8B1247NDMCQG', # Consumer Loans: Credit Cards and Other Revolving Plans, Domestically Chartered Commercial Banks
    'H8B3248NDMCQG', # Consumer Loans: Other Consumer Loans, Domestically Chartered Commercial Banks
    'B2245NDMCQG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Domestically Chartered Commercial Banks
    'B1243NDMCQG', # Consumer Loans: Other Consumer Loans: Automobile Loans, Domestically Chartered Commercial Banks
    ### Deposits
    'H8B1058NDMCQG', # Deposits, Domestically Chartered Commercial Banks
    ### Allowance for Credit Losses on Loans and Leases
    'H8B1043NDMCQG', # LESS: Allowance for Credit Losses on Loans and Leases, Domestically Chartered Commercial Banks
    ### Large Time Deposits
    'H8B1072NDMCQG', # Large Time Deposits, Domestically Chartered Commercial Banks
    ### Loans and Leases in Bank Credit
    'H8B1020NDMCQG', # Loans and Leases in Bank Credit, Domestically Chartered Commercial Banks
    ### Loans to Commercial Banks
    'H8B1047NDMCQG', # Loans to Commercial Banks, Domestically Chartered Commercial Banks
    ### Other Assets
    'H8B3053NDMCQG', # Other Assets, Domestically Chartered Commercial Banks
    ### Other Deposits
    'H8B1110NDMCQG', # Other Deposits, Domestically Chartered Commercial Banks
    ### Other Liabilities
    'H8B3095NDMCQG', # Other Liabilities, Domestically Chartered Commercial Banks
    ### Other Loans and Leases
    'H8B3305NDMCQG', # Other Loans and Leases: All Other Loans and Leases, Domestically Chartered Commercial Banks
    'B1030NDMCQG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Domestically Chartered Commercial Banks
    'B2310NDMCQG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Domestically Chartered Commercial Banks
    ### Other Securities
    'H8B1011NDMCQG', # Other Securities, Domestically Chartered Commercial Banks
    'H8B1303NDMCQG', # Other Securities: Mortgage-Backed Securities, Domestically Chartered Commercial Banks
    'H8B1304NDMCQG', # Other Securities: Non-MBS, Domestically Chartered Commercial Banks
    ### Real Estate Loans
    'H8B1026NDMCQG', # Real Estate Loans, Domestically Chartered Commercial Banks
    'H8B3219NDMCQG', # Real Estate Loans: Commercial Real Estate Loans, Domestically Chartered Commercial Banks
    'B1215NDMCQG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Domestically Chartered Commercial Banks
    'B1216NDMCQG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Domestically Chartered Commercial Banks
    'B1217NDMCQG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Domestically Chartered Commercial Banks
    'B1218NDMCQG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Domestically Chartered Commercial Banks
    'H8B1221NDMCQG', # Real Estate Loans: Residential Real Estate Loans, Domestically Chartered Commercial Banks
    'H8B1220NDMCQG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Domestically Chartered Commercial Banks
    'H8B1027NDMCQG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Domestically Chartered Commercial Banks
    ### Residual (Assets Less Liabilities)
    'H8B1091NDMCQG', # Residual (Assets Less Liabilities), Domestically Chartered Commercial Banks
    ### Securities in Bank Credit
    'H8B1002NDMCQG', # Securities in Bank Credit, Domestically Chartered Commercial Banks
    ### Total Assets
    'H8B1151NDMCQG', # Total Assets, Domestically Chartered Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NDMCQG', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Domestically Chartered Commercial Banks
    ### Total Liabilities
    'H8B1152NDMCQG', # Total Liabilities, Domestically Chartered Commercial Banks
    ### Treasury and Agency Securities
    'H8B1003NDMCQG', # Treasury and Agency Securities, Domestically Chartered Commercial Banks
    'H8B1301NDMCQG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Domestically Chartered Commercial Banks
    'H8B1302NDMCQG', # Treasury and Agency Securities: Non-MBS, Domestically Chartered Commercial Banks

    # Large Domestically Chartered Commercial Banks (40)
    ## 증가율 (% Chg. at Annual Rate, SA)
    ### Bank Credit
    'H8B1001NLGCQG', # Bank Credit, Large Domestically Chartered Commercial Banks
    ### Borrowings
    'H8B3094NLGCQG', # Borrowings, Large Domestically Chartered Commercial Banks
    ### Cash Assets
    'H8B1048NLGCQG', # Cash Assets, Large Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans
    'H8B1023NLGCQG', # Commercial and Industrial Loans, Large Domestically Chartered Commercial Banks
    ### Consumer Loans
    'H8B1029NLGCQG', # Consumer Loans, Large Domestically Chartered Commercial Banks
    'H8B1247NLGCQG', # Consumer Loans: Credit Cards and Other Revolving Plans, Large Domestically Chartered Commercial Banks
    'H8B3248NLGCQG', # Consumer Loans: Other Consumer Loans, Large Domestically Chartered Commercial Banks
    'B2245NLGCQG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Large Domestically Chartered Commercial Banks
    'B1243NLGCQG', # Consumer Loans: Other Consumer Loans: Automobile Loans, Large Domestically Chartered Commercial Banks
    ### Deposits
    'H8B1058NLGCQG', # Deposits, Large Domestically Chartered Commercial Banks
    ### Allowance for Credit Losses on Loans and Leases
    'H8B1043NLGCQG', # LESS: Allowance for Credit Losses on Loans and Leases, Large Domestically Chartered Commercial Banks
    ### Large Time Deposits
    'H8B1072NLGCQG', # Large Time Deposits, Large Domestically Chartered Commercial Banks
    ### Loans and Leases in Bank Credit
    'H8B1020NLGCQG', # Loans and Leases in Bank Credit, Large Domestically Chartered Commercial Banks
    ### Loans to Commercial Banks
    'H8B1047NLGCQG', # Loans to Commercial Banks, Large Domestically Chartered Commercial Banks
    ### Other Assets
    'H8B3053NLGCQG', # Other Assets, Large Domestically Chartered Commercial Banks
    ### Other Deposits
    'H8B1110NLGCQG', # Other Deposits, Large Domestically Chartered Commercial Banks
    ### Other Liabilities
    'H8B3095NLGCQG', # Other Liabilities, Large Domestically Chartered Commercial Banks
    ### Other Loans and Leases
    'H8B3305NLGCQG', # Other Loans and Leases: All Other Loans and Leases, Large Domestically Chartered Commercial Banks
    'B1030NLGCQG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Large Domestically Chartered Commercial Banks
    'B2310NLGCQG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Large Domestically Chartered Commercial Banks
    ### Other Securities
    'H8B1011NLGCQG', # Other Securities, Large Domestically Chartered Commercial Banks
    'H8B1303NLGCQG', # Other Securities: Mortgage-Backed Securities, Large Domestically Chartered Commercial Banks
    'H8B1304NLGCQG', # Other Securities: Non-MBS, Large Domestically Chartered Commercial Banks
    ### Real Estate Loans
    'H8B1026NLGCQG', # Real Estate Loans, Large Domestically Chartered Commercial Banks
    'H8B3219NLGCQG', # Real Estate Loans: Commercial Real Estate Loans, Large Domestically Chartered Commercial Banks
    'B1215NLGCQG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Large Domestically Chartered Commercial Banks
    'B1216NLGCQG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Large Domestically Chartered Commercial Banks
    'B1217NLGCQG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Large Domestically Chartered Commercial Banks
    'B1218NLGCQG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Large Domestically Chartered Commercial Banks
    'H8B1221NLGCQG', # Real Estate Loans: Residential Real Estate Loans, Large Domestically Chartered Commercial Banks
    'H8B1220NLGCQG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Large Domestically Chartered Commercial Banks
    'H8B1027NLGCQG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Large Domestically Chartered Commercial Banks
    ### Residual (Assets Less Liabilities)
    'H8B1091NLGCQG', # Residual (Assets Less Liabilities), Large Domestically Chartered Commercial Banks
    ### Securities in Bank Credit
    'H8B1002NLGCQG', # Securities in Bank Credit, Large Domestically Chartered Commercial Banks
    ### Total Assets
    'H8B1151NLGCQG', # Total Assets, Large Domestically Chartered Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NLGCQG', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Large Domestically Chartered Commercial Banks
    ### Total Liabilities
    'H8B1152NLGCQG', # Total Liabilities, Large Domestically Chartered Commercial Banks
    ### Treasury and Agency Securities
    'H8B1003NLGCQG', # Treasury and Agency Securities, Large Domestically Chartered Commercial Banks
    'H8B1301NLGCQG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Large Domestically Chartered Commercial Banks
    'H8B1302NLGCQG', # Treasury and Agency Securities: Non-MBS, Large Domestically Chartered Commercial Banks

    # Small Domestically Chartered Commercial Banks (40)
    ## 증가율 (% Chg. at Annual Rate, SA)
    ### Bank Credit
    'H8B1001NSMCQG', # Bank Credit, Small Domestically Chartered Commercial Banks
    ### Borrowings
    'H8B3094NSMCQG', # Borrowings, Small Domestically Chartered Commercial Banks
    ### Cash Assets
    'H8B1048NSMCQG', # Cash Assets, Small Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans
    'H8B1023NSMCQG', # Commercial and Industrial Loans, Small Domestically Chartered Commercial Banks
    ### Consumer Loans
    'H8B1029NSMCQG', # Consumer Loans, Small Domestically Chartered Commercial Banks
    'H8B1247NSMCQG', # Consumer Loans: Credit Cards and Other Revolving Plans, Small Domestically Chartered Commercial Banks
    'H8B3248NSMCQG', # Consumer Loans: Other Consumer Loans, Small Domestically Chartered Commercial Banks
    'B2245NSMCQG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Small Domestically Chartered Commercial Banks
    'B1243NSMCQG', # Consumer Loans: Other Consumer Loans: Automobile Loans, Small Domestically Chartered Commercial Banks
    ### Deposits
    'H8B1058NSMCQG', # Deposits, Small Domestically Chartered Commercial Banks
    ### Allowance for Credit Losses on Loans and Leases
    'H8B1043NSMCQG', # LESS: Allowance for Credit Losses on Loans and Leases, Small Domestically Chartered Commercial Banks
    ### Large Time Deposits
    'H8B1072NSMCQG', # Large Time Deposits, Small Domestically Chartered Commercial Banks
    ### Loans and Leases in Bank Credit
    'H8B1020NSMCQG', # Loans and Leases in Bank Credit, Small Domestically Chartered Commercial Banks
    ### Loans to Commercial Banks
    'H8B1047NSMCQG', # Loans to Commercial Banks, Small Domestically Chartered Commercial Banks
    ### Other Assets
    'H8B3053NSMCQG', # Other Assets, Small Domestically Chartered Commercial Banks
    ### Other Deposits
    'H8B1110NSMCQG', # Other Deposits, Small Domestically Chartered Commercial Banks
    ### Other Liabilities
    'H8B3095NSMCQG', # Other Liabilities, Small Domestically Chartered Commercial Banks
    ### Other Loans and Leases
    'H8B3305NSMCQG', # Other Loans and Leases: All Other Loans and Leases, Small Domestically Chartered Commercial Banks
    'B1030NSMCQG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Small Domestically Chartered Commercial Banks
    'B2310NSMCQG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Small Domestically Chartered Commercial Banks
    ### Other Securities
    'H8B1011NSMCQG', # Other Securities, Small Domestically Chartered Commercial Banks
    'H8B1303NSMCQG', # Other Securities: Mortgage-Backed Securities, Small Domestically Chartered Commercial Banks
    'H8B1304NSMCQG', # Other Securities: Non-MBS, Small Domestically Chartered Commercial Banks
    ### Real Estate Loans
    'H8B1026NSMCQG', # Real Estate Loans, Small Domestically Chartered Commercial Banks
    'H8B3219NSMCQG', # Real Estate Loans: Commercial Real Estate Loans, Small Domestically Chartered Commercial Banks
    'B1215NSMCQG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Small Domestically Chartered Commercial Banks
    'B1216NSMCQG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Small Domestically Chartered Commercial Banks
    'B1217NSMCQG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Small Domestically Chartered Commercial Banks
    'B1218NSMCQG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Small Domestically Chartered Commercial Banks
    'H8B1221NSMCQG', # Real Estate Loans: Residential Real Estate Loans, Small Domestically Chartered Commercial Banks
    'H8B1220NSMCQG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Small Domestically Chartered Commercial Banks
    'H8B1027NSMCQG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Small Domestically Chartered Commercial Banks
    ### Residual (Assets Less Liabilities)
    'H8B1091NSMCQG', # Residual (Assets Less Liabilities), Small Domestically Chartered Commercial Banks
    ### Securities in Bank Credit
    'H8B1002NSMCQG', # Securities in Bank Credit, Small Domestically Chartered Commercial Banks
    ### Total Assets
    'H8B1151NSMCQG', # Total Assets, Small Domestically Chartered Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NSMCQG', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Small Domestically Chartered Commercial Banks
    ### Total Liabilities
    'H8B1152NSMCQG', # Total Liabilities, Small Domestically Chartered Commercial Banks
    ### Treasury and Agency Securities
    'H8B1003NSMCQG', # Treasury and Agency Securities, Small Domestically Chartered Commercial Banks
    'H8B1301NSMCQG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Small Domestically Chartered Commercial Banks
    'H8B1302NSMCQG', # Treasury and Agency Securities: Non-MBS, Small Domestically Chartered Commercial Banks

    # Foreign-Related Institutions (37)
    ## 증가율 (% Chg. at Annual Rate, SA)
    ### Bank Credit
    'H8B1001NFRCQG', # Bank Credit, Foreign-Related Institutions
    ### Borrowings
    'H8B3094NFRCQG', # Borrowings, Foreign-Related Institutions
    ### Cash Assets
    'H8B1048NFRCQG', # Cash Assets, Foreign-Related Institutions
    ### Commercial and Industrial Loans
    'H8B1023NFRCQG', # Commercial and Industrial Loans, Foreign-Related Institutions
    ### Consumer Loans
    'H8B1029NFRCQG', # Consumer Loans, Foreign-Related Institutions
    'H8B3248NFRCQG', # Consumer Loans: Other Consumer Loans, Foreign-Related Institutions
    ### Deposits
    'H8B1058NFRCQG', # Deposits, Foreign-Related Institutions
    ### Allowance for Credit Losses on Loans and Leases
    'H8B1043NFRCQG', # LESS: Allowance for Credit Losses on Loans and Leases, Foreign-Related Institutions
    ### Large Time Deposits
    'H8B1072NFRCQG', # Large Time Deposits, Foreign-Related Institutions
    ### Loans and Leases in Bank Credit
    'H8B1020NFRCQG', # Loans and Leases in Bank Credit, Foreign-Related Institutions
    ### Loans to Commercial Banks
    'H8B1047NFRCQG', # Loans to Commercial Banks, Foreign-Related Institutions
    ### Other Assets
    'H8B3053NFRCQG', # Other Assets, Foreign-Related Institutions
    ### Other Deposits
    'H8B1110NFRCQG', # Other Deposits, Foreign-Related Institutions
    ### Other Liabilities
    'H8B3095NFRCQG', # Other Liabilities, Foreign-Related Institutions
    ### Other Loans and Leases
    'H8B3305NFRCQG', # Other Loans and Leases: All Other Loans and Leases, Foreign-Related Institutions
    'B1030NFRCQG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Foreign-Related Institutions
    'B2310NFRCQG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Foreign-Related Institutions
    ### Other Securities
    'H8B1011NFRCQG', # Other Securities, Foreign-Related Institutions
    'H8B1303NFRCQG', # Other Securities: Mortgage-Backed Securities, Foreign-Related Institutions
    'H8B1304NFRCQG', # Other Securities: Non-MBS, Foreign-Related Institutions
    ### Real Estate Loans
    'H8B1026NFRCQG', # Real Estate Loans, Foreign-Related Institutions
    'H8B3219NFRCQG', # Real Estate Loans: Commercial Real Estate Loans, Foreign-Related Institutions
    'B1215NFRCQG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Foreign-Related Institutions
    'B1216NFRCQG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Foreign-Related Institutions
    'B1217NFRCQG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Foreign-Related Institutions
    'B1218NFRCQG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Foreign-Related Institutions
    'H8B1221NFRCQG', # Real Estate Loans: Residential Real Estate Loans, Foreign-Related Institutions
    'H8B1220NFRCQG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Foreign-Related Institutions
    'H8B1027NFRCQG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Foreign-Related Institutions
    ### Residual (Assets Less Liabilities)
    'H8B1091NFRCQG', # Residual (Assets Less Liabilities), Foreign-Related Institutions
    ### Securities in Bank Credit
    'H8B1002NFRCQG', # Securities in Bank Credit, Foreign-Related Institutions
    ### Total Assets
    'H8B1151NFRCQG', # Total Assets, Foreign-Related Institutions
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NFRCQG', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Foreign-Related Institutions
    ### Total Liabilities
    'H8B1152NFRCQG', # Total Liabilities, Foreign-Related Institutions
    ### Treasury and Agency Securities
    'H8B1003NFRCQG', # Treasury and Agency Securities, Foreign-Related Institutions
    'H8B1301NFRCQG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Foreign-Related Institutions
    'H8B1302NFRCQG', # Treasury and Agency Securities: Non-MBS, Foreign-Related Institutions
]

# Annually (197)
ids_Y = [
    # All Commercial Banks (40)
    ## 증가율 (% Chg. at Annual Rate, SA)
    ### Bank Credit
    'H8B1001NCBCAG', # Bank Credit, All Commercial Banks
    ### Borrowings
    'H8B3094NCBCAG', # Borrowings, All Commercial Banks
    ### Cash Assets
    'H8B1048NCBCAG', # Cash Assets, All Commercial Banks
    ### Commercial and Industrial Loans
    'H8B1023NCBCAG', # Commercial and Industrial Loans, All Commercial Banks
    ### Consumer Loans
    'H8B1029NCBCAG', # Consumer Loans, All Commercial Banks
    'H8B1247NCBCAG', # Consumer Loans: Credit Cards and Other Revolving Plans, All Commercial Banks
    'H8B3248NCBCAG', # Consumer Loans: Other Consumer Loans, All Commercial Banks
    'B2245NCBCAG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, All Commercial Banks
    'B1243NCBCAG', # Consumer Loans: Other Consumer Loans: Automobile Loans, All Commercial Banks
    ### Deposits
    'H8B1058NCBCAG', # Deposits, All Commercial Banks
    ### Allowance for Credit Losses on Loans and Leases
    'H8B1043NCBCAG', # LESS: Allowance for Credit Losses on Loans and Leases, All Commercial Banks
    ### Large Time Deposits
    'H8B1072NCBCAG', # Large Time Deposits, All Commercial Banks
    ### Loans and Leases in Bank Credit
    'H8B1020NCBCAG', # Loans and Leases in Bank Credit, All Commercial Banks
    ### Loans to Commercial Banks
    'H8B1047NCBCAG', # Loans to Commercial Banks, All Commercial Banks
    ### Other Assets
    'H8B3053NCBCAG', # Other Assets, All Commercial Banks
    ### Other Deposits
    'H8B1110NCBCAG', # Other Deposits, All Commercial Banks
    ### Other Liabilities
    'H8B3095NCBCAG', # Other Liabilities, All Commercial Banks
    ### Other Loans and Leases
    'H8B3305NCBCAG', # Other Loans and Leases: All Other Loans and Leases, All Commercial Banks
    'B1030NCBCAG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, All Commercial Banks
    'B2310NCBCAG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, All Commercial Banks
    ### Other Securities
    'H8B1011NCBCAG', # Other Securities, All Commercial Banks
    'H8B1303NCBCAG', # Other Securities: Mortgage-Backed Securities, All Commercial Banks
    'H8B1304NCBCAG', # Other Securities: Non-MBS, All Commercial Banks
    ### Real Estate Loans
    'H8B1026NCBCAG', # Real Estate Loans, All Commercial Banks
    'H8B3219NCBCAG', # Real Estate Loans: Commercial Real Estate Loans, All Commercial Banks
    'B1215NCBCAG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, All Commercial Banks
    'B1216NCBCAG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, All Commercial Banks
    'B1217NCBCAG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, All Commercial Banks
    'B1218NCBCAG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, All Commercial Banks
    'H8B1221NCBCAG', # Real Estate Loans: Residential Real Estate Loans, All Commercial Banks
    'H8B1220NCBCAG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, All Commercial Banks
    'H8B1027NCBCAG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, All Commercial Banks
    ### Residual (Assets Less Liabilities)
    'H8B1091NCBCAG', # Residual (Assets Less Liabilities), All Commercial Banks
    ### Securities in Bank Credit
    'H8B1002NCBCAG', # Securities in Bank Credit, All Commercial Banks
    ### Total Assets
    'H8B1151NCBCAG', # Total Assets, All Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NCBCAG', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, All Commercial Banks
    ### Total Liabilities
    'H8B1152NCBCAG', # Total Liabilities, All Commercial Banks
    ### Treasury and Agency Securities
    'H8B1003NCBCAG', # Treasury and Agency Securities, All Commercial Banks
    'H8B1301NCBCAG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), All Commercial Banks
    'H8B1302NCBCAG', # Treasury and Agency Securities: Non-MBS, All Commercial Banks

    # Domestically Chartered Commercial Banks (40)
    ## 증가율 (% Chg. at Annual Rate, SA)
    ### Bank Credit
    'H8B1001NDMCAG', # Bank Credit, Domestically Chartered Commercial Banks
    ### Borrowings
    'H8B3094NDMCAG', # Borrowings, Domestically Chartered Commercial Banks
    ### Cash Assets
    'H8B1048NDMCAG', # Cash Assets, Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans
    'H8B1023NDMCAG', # Commercial and Industrial Loans, Domestically Chartered Commercial Banks
    ### Consumer Loans
    'H8B1029NDMCAG', # Consumer Loans, Domestically Chartered Commercial Banks
    'H8B1247NDMCAG', # Consumer Loans: Credit Cards and Other Revolving Plans, Domestically Chartered Commercial Banks
    'H8B3248NDMCAG', # Consumer Loans: Other Consumer Loans, Domestically Chartered Commercial Banks
    'B2245NDMCAG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Domestically Chartered Commercial Banks
    'B1243NDMCAG', # Consumer Loans: Other Consumer Loans: Automobile Loans, Domestically Chartered Commercial Banks
    ### Deposits
    'H8B1058NDMCAG', # Deposits, Domestically Chartered Commercial Banks
    ### Allowance for Credit Losses on Loans and Leases
    'H8B1043NDMCAG', # LESS: Allowance for Credit Losses on Loans and Leases, Domestically Chartered Commercial Banks
    ### Large Time Deposits
    'H8B1072NDMCAG', # Large Time Deposits, Domestically Chartered Commercial Banks
    ### Loans and Leases in Bank Credit
    'H8B1020NDMCAG', # Loans and Leases in Bank Credit, Domestically Chartered Commercial Banks
    ### Loans to Commercial Banks
    'H8B1047NDMCAG', # Loans to Commercial Banks, Domestically Chartered Commercial Banks
    ### Other Assets
    'H8B3053NDMCAG', # Other Assets, Domestically Chartered Commercial Banks
    ### Other Deposits
    'H8B1110NDMCAG', # Other Deposits, Domestically Chartered Commercial Banks
    ### Other Liabilities
    'H8B3095NDMCAG', # Other Liabilities, Domestically Chartered Commercial Banks
    ### Other Loans and Leases
    'H8B3305NDMCAG', # Other Loans and Leases: All Other Loans and Leases, Domestically Chartered Commercial Banks
    'B1030NDMCAG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Domestically Chartered Commercial Banks
    'B2310NDMCAG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Domestically Chartered Commercial Banks
    ### Other Securities
    'H8B1011NDMCAG', # Other Securities, Domestically Chartered Commercial Banks
    'H8B1303NDMCAG', # Other Securities: Mortgage-Backed Securities, Domestically Chartered Commercial Banks
    'H8B1304NDMCAG', # Other Securities: Non-MBS, Domestically Chartered Commercial Banks
    ### Real Estate Loans
    'H8B1026NDMCAG', # Real Estate Loans, Domestically Chartered Commercial Banks
    'H8B3219NDMCAG', # Real Estate Loans: Commercial Real Estate Loans, Domestically Chartered Commercial Banks
    'B1215NDMCAG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Domestically Chartered Commercial Banks
    'B1216NDMCAG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Domestically Chartered Commercial Banks
    'B1217NDMCAG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Domestically Chartered Commercial Banks
    'B1218NDMCAG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Domestically Chartered Commercial Banks
    'H8B1221NDMCAG', # Real Estate Loans: Residential Real Estate Loans, Domestically Chartered Commercial Banks
    'H8B1220NDMCAG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Domestically Chartered Commercial Banks
    'H8B1027NDMCAG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Domestically Chartered Commercial Banks
    ### Residual (Assets Less Liabilities)
    'H8B1091NDMCAG', # Residual (Assets Less Liabilities), Domestically Chartered Commercial Banks
    ### Securities in Bank Credit
    'H8B1002NDMCAG', # Securities in Bank Credit, Domestically Chartered Commercial Banks
    ### Total Assets
    'H8B1151NDMCAG', # Total Assets, Domestically Chartered Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NDMCAG', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Domestically Chartered Commercial Banks
    ### Total Liabilities
    'H8B1152NDMCAG', # Total Liabilities, Domestically Chartered Commercial Banks
    ### Treasury and Agency Securities
    'H8B1003NDMCAG', # Treasury and Agency Securities, Domestically Chartered Commercial Banks
    'H8B1301NDMCAG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Domestically Chartered Commercial Banks
    'H8B1302NDMCAG', # Treasury and Agency Securities: Non-MBS, Domestically Chartered Commercial Banks

    # Large Domestically Chartered Commercial Banks (40)
    ## 증가율 (% Chg. at Annual Rate, SA)
    ### Bank Credit
    'H8B1001NLGCAG', # Bank Credit, Large Domestically Chartered Commercial Banks
    ### Borrowings
    'H8B3094NLGCAG', # Borrowings, Large Domestically Chartered Commercial Banks
    ### Cash Assets
    'H8B1048NLGCAG', # Cash Assets, Large Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans
    'H8B1023NLGCAG', # Commercial and Industrial Loans, Large Domestically Chartered Commercial Banks
    ### Consumer Loans
    'H8B1029NLGCAG', # Consumer Loans, Large Domestically Chartered Commercial Banks
    'H8B1247NLGCAG', # Consumer Loans: Credit Cards and Other Revolving Plans, Large Domestically Chartered Commercial Banks
    'H8B3248NLGCAG', # Consumer Loans: Other Consumer Loans, Large Domestically Chartered Commercial Banks
    'B2245NLGCAG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Large Domestically Chartered Commercial Banks
    'B1243NLGCAG', # Consumer Loans: Other Consumer Loans: Automobile Loans, Large Domestically Chartered Commercial Banks
    ### Deposits
    'H8B1058NLGCAG', # Deposits, Large Domestically Chartered Commercial Banks
    ### Allowance for Credit Losses on Loans and Leases
    'H8B1043NLGCAG', # LESS: Allowance for Credit Losses on Loans and Leases, Large Domestically Chartered Commercial Banks
    ### Large Time Deposits
    'H8B1072NLGCAG', # Large Time Deposits, Large Domestically Chartered Commercial Banks
    ### Loans and Leases in Bank Credit
    'H8B1020NLGCAG', # Loans and Leases in Bank Credit, Large Domestically Chartered Commercial Banks
    ### Loans to Commercial Banks
    'H8B1047NLGCAG', # Loans to Commercial Banks, Large Domestically Chartered Commercial Banks
    ### Other Assets
    'H8B3053NLGCAG', # Other Assets, Large Domestically Chartered Commercial Banks
    ### Other Deposits
    'H8B1110NLGCAG', # Other Deposits, Large Domestically Chartered Commercial Banks
    ### Other Liabilities
    'H8B3095NLGCAG', # Other Liabilities, Large Domestically Chartered Commercial Banks
    ### Other Loans and Leases
    'H8B3305NLGCAG', # Other Loans and Leases: All Other Loans and Leases, Large Domestically Chartered Commercial Banks
    'B1030NLGCAG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Large Domestically Chartered Commercial Banks
    'B2310NLGCAG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Large Domestically Chartered Commercial Banks
    ### Other Securities
    'H8B1011NLGCAG', # Other Securities, Large Domestically Chartered Commercial Banks
    'H8B1303NLGCAG', # Other Securities: Mortgage-Backed Securities, Large Domestically Chartered Commercial Banks
    'H8B1304NLGCAG', # Other Securities: Non-MBS, Large Domestically Chartered Commercial Banks
    ### Real Estate Loans
    'H8B1026NLGCAG', # Real Estate Loans, Large Domestically Chartered Commercial Banks
    'H8B3219NLGCAG', # Real Estate Loans: Commercial Real Estate Loans, Large Domestically Chartered Commercial Banks
    'B1215NLGCAG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Large Domestically Chartered Commercial Banks
    'B1216NLGCAG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Large Domestically Chartered Commercial Banks
    'B1217NLGCAG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Large Domestically Chartered Commercial Banks
    'B1218NLGCAG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Large Domestically Chartered Commercial Banks
    'H8B1221NLGCAG', # Real Estate Loans: Residential Real Estate Loans, Large Domestically Chartered Commercial Banks
    'H8B1220NLGCAG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Large Domestically Chartered Commercial Banks
    'H8B1027NLGCAG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Large Domestically Chartered Commercial Banks
    ### Residual (Assets Less Liabilities)
    'H8B1091NLGCAG', # Residual (Assets Less Liabilities), Large Domestically Chartered Commercial Banks
    ### Securities in Bank Credit
    'H8B1002NLGCAG', # Securities in Bank Credit, Large Domestically Chartered Commercial Banks
    ### Total Assets
    'H8B1151NLGCAG', # Total Assets, Large Domestically Chartered Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NLGCAG', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Large Domestically Chartered Commercial Banks
    ### Total Liabilities
    'H8B1152NLGCAG', # Total Liabilities, Large Domestically Chartered Commercial Banks
    ### Treasury and Agency Securities
    'H8B1003NLGCAG', # Treasury and Agency Securities, Large Domestically Chartered Commercial Banks
    'H8B1301NLGCAG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Large Domestically Chartered Commercial Banks
    'H8B1302NLGCAG', # Treasury and Agency Securities: Non-MBS, Large Domestically Chartered Commercial Banks

    # Small Domestically Chartered Commercial Banks (40)
    ## 증가율 (% Chg. at Annual Rate, SA)
    ### Bank Credit
    'H8B1001NSMCAG', # Bank Credit, Small Domestically Chartered Commercial Banks
    ### Borrowings
    'H8B3094NSMCAG', # Borrowings, Small Domestically Chartered Commercial Banks
    ### Cash Assets
    'H8B1048NSMCAG', # Cash Assets, Small Domestically Chartered Commercial Banks
    ### Commercial and Industrial Loans
    'H8B1023NSMCAG', # Commercial and Industrial Loans, Small Domestically Chartered Commercial Banks
    ### Consumer Loans
    'H8B1029NSMCAG', # Consumer Loans, Small Domestically Chartered Commercial Banks
    'H8B1247NSMCAG', # Consumer Loans: Credit Cards and Other Revolving Plans, Small Domestically Chartered Commercial Banks
    'H8B3248NSMCAG', # Consumer Loans: Other Consumer Loans, Small Domestically Chartered Commercial Banks
    'B2245NSMCAG', # Consumer Loans: Other Consumer Loans: All Other Consumer Loans, Small Domestically Chartered Commercial Banks
    'B1243NSMCAG', # Consumer Loans: Other Consumer Loans: Automobile Loans, Small Domestically Chartered Commercial Banks
    ### Deposits
    'H8B1058NSMCAG', # Deposits, Small Domestically Chartered Commercial Banks
    ### Allowance for Credit Losses on Loans and Leases
    'H8B1043NSMCAG', # LESS: Allowance for Credit Losses on Loans and Leases, Small Domestically Chartered Commercial Banks
    ### Large Time Deposits
    'H8B1072NSMCAG', # Large Time Deposits, Small Domestically Chartered Commercial Banks
    ### Loans and Leases in Bank Credit
    'H8B1020NSMCAG', # Loans and Leases in Bank Credit, Small Domestically Chartered Commercial Banks
    ### Loans to Commercial Banks
    'H8B1047NSMCAG', # Loans to Commercial Banks, Small Domestically Chartered Commercial Banks
    ### Other Assets
    'H8B3053NSMCAG', # Other Assets, Small Domestically Chartered Commercial Banks
    ### Other Deposits
    'H8B1110NSMCAG', # Other Deposits, Small Domestically Chartered Commercial Banks
    ### Other Liabilities
    'H8B3095NSMCAG', # Other Liabilities, Small Domestically Chartered Commercial Banks
    ### Other Loans and Leases
    'H8B3305NSMCAG', # Other Loans and Leases: All Other Loans and Leases, Small Domestically Chartered Commercial Banks
    'B1030NSMCAG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Small Domestically Chartered Commercial Banks
    'B2310NSMCAG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Small Domestically Chartered Commercial Banks
    ### Other Securities
    'H8B1011NSMCAG', # Other Securities, Small Domestically Chartered Commercial Banks
    'H8B1303NSMCAG', # Other Securities: Mortgage-Backed Securities, Small Domestically Chartered Commercial Banks
    'H8B1304NSMCAG', # Other Securities: Non-MBS, Small Domestically Chartered Commercial Banks
    ### Real Estate Loans
    'H8B1026NSMCAG', # Real Estate Loans, Small Domestically Chartered Commercial Banks
    'H8B3219NSMCAG', # Real Estate Loans: Commercial Real Estate Loans, Small Domestically Chartered Commercial Banks
    'B1215NSMCAG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Small Domestically Chartered Commercial Banks
    'B1216NSMCAG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Small Domestically Chartered Commercial Banks
    'B1217NSMCAG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Small Domestically Chartered Commercial Banks
    'B1218NSMCAG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Small Domestically Chartered Commercial Banks
    'H8B1221NSMCAG', # Real Estate Loans: Residential Real Estate Loans, Small Domestically Chartered Commercial Banks
    'H8B1220NSMCAG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Small Domestically Chartered Commercial Banks
    'H8B1027NSMCAG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Small Domestically Chartered Commercial Banks
    ### Residual (Assets Less Liabilities)
    'H8B1091NSMCAG', # Residual (Assets Less Liabilities), Small Domestically Chartered Commercial Banks
    ### Securities in Bank Credit
    'H8B1002NSMCAG', # Securities in Bank Credit, Small Domestically Chartered Commercial Banks
    ### Total Assets
    'H8B1151NSMCAG', # Total Assets, Small Domestically Chartered Commercial Banks
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NSMCAG', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Small Domestically Chartered Commercial Banks
    ### Total Liabilities
    'H8B1152NSMCAG', # Total Liabilities, Small Domestically Chartered Commercial Banks
    ### Treasury and Agency Securities
    'H8B1003NSMCAG', # Treasury and Agency Securities, Small Domestically Chartered Commercial Banks
    'H8B1301NSMCAG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Small Domestically Chartered Commercial Banks
    'H8B1302NSMCAG', # Treasury and Agency Securities: Non-MBS, Small Domestically Chartered Commercial Banks

    # Foreign-Related Institutions (37)
    ## 증가율 (% Chg. at Annual Rate, SA)
    ### Bank Credit
    'H8B1001NFRCAG', # Bank Credit, Foreign-Related Institutions
    ### Borrowings
    'H8B3094NFRCAG', # Borrowings, Foreign-Related Institutions
    ### Cash Assets
    'H8B1048NFRCAG', # Cash Assets, Foreign-Related Institutions
    ### Commercial and Industrial Loans
    'H8B1023NFRCAG', # Commercial and Industrial Loans, Foreign-Related Institutions
    ### Consumer Loans
    'H8B1029NFRCAG', # Consumer Loans, Foreign-Related Institutions
    'H8B3248NFRCAG', # Consumer Loans: Other Consumer Loans, Foreign-Related Institutions
    ### Deposits
    'H8B1058NFRCAG', # Deposits, Foreign-Related Institutions
    ### Allowance for Credit Losses on Loans and Leases
    'H8B1043NFRCAG', # LESS: Allowance for Credit Losses on Loans and Leases, Foreign-Related Institutions
    ### Large Time Deposits
    'H8B1072NFRCAG', # Large Time Deposits, Foreign-Related Institutions
    ### Loans and Leases in Bank Credit
    'H8B1020NFRCAG', # Loans and Leases in Bank Credit, Foreign-Related Institutions
    ### Loans to Commercial Banks
    'H8B1047NFRCAG', # Loans to Commercial Banks, Foreign-Related Institutions
    ### Other Assets
    'H8B3053NFRCAG', # Other Assets, Foreign-Related Institutions
    ### Other Deposits
    'H8B1110NFRCAG', # Other Deposits, Foreign-Related Institutions
    ### Other Liabilities
    'H8B3095NFRCAG', # Other Liabilities, Foreign-Related Institutions
    ### Other Loans and Leases
    'H8B3305NFRCAG', # Other Loans and Leases: All Other Loans and Leases, Foreign-Related Institutions
    'B1030NFRCAG', # Other Loans and Leases: All Other Loans and Leases: Loans to Nondepository Financial Institutions, Foreign-Related Institutions
    'B2310NFRCAG', # Other Loans and Leases: All Other Loans and Leases: Other Loans Not Elsewhere Classified, Foreign-Related Institutions
    ### Other Securities
    'H8B1011NFRCAG', # Other Securities, Foreign-Related Institutions
    'H8B1303NFRCAG', # Other Securities: Mortgage-Backed Securities, Foreign-Related Institutions
    'H8B1304NFRCAG', # Other Securities: Non-MBS, Foreign-Related Institutions
    ### Real Estate Loans
    'H8B1026NFRCAG', # Real Estate Loans, Foreign-Related Institutions
    'H8B3219NFRCAG', # Real Estate Loans: Commercial Real Estate Loans, Foreign-Related Institutions
    'B1215NFRCAG', # Real Estate Loans: Commercial Real Estate Loans: Construction and Land Development Loans, Foreign-Related Institutions
    'B1216NFRCAG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Farmland, Foreign-Related Institutions
    'B1217NFRCAG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Multifamily Properties, Foreign-Related Institutions
    'B1218NFRCAG', # Real Estate Loans: Commercial Real Estate Loans: Secured by Nonfarm Nonresidential Properties, Foreign-Related Institutions
    'H8B1221NFRCAG', # Real Estate Loans: Residential Real Estate Loans, Foreign-Related Institutions
    'H8B1220NFRCAG', # Real Estate Loans: Residential Real Estate Loans: Closed-End Residential Loans, Foreign-Related Institutions
    'H8B1027NFRCAG', # Real Estate Loans: Residential Real Estate Loans: Revolving Home Equity Loans, Foreign-Related Institutions
    ### Residual (Assets Less Liabilities)
    'H8B1091NFRCAG', # Residual (Assets Less Liabilities), Foreign-Related Institutions
    ### Securities in Bank Credit
    'H8B1002NFRCAG', # Securities in Bank Credit, Foreign-Related Institutions
    ### Total Assets
    'H8B1151NFRCAG', # Total Assets, Foreign-Related Institutions
    ### Total Fed Funds Sold and Securities Purchased Under Agreements to Resell
    'H8B3092NFRCAG', # Total Fed Funds Sold and Securities Purchased Under Agreements to Resell, Foreign-Related Institutions
    ### Total Liabilities
    'H8B1152NFRCAG', # Total Liabilities, Foreign-Related Institutions
    ### Treasury and Agency Securities
    'H8B1003NFRCAG', # Treasury and Agency Securities, Foreign-Related Institutions
    'H8B1301NFRCAG', # Treasury and Agency Securities: Mortgage-Backed Securities (MBS), Foreign-Related Institutions
    'H8B1302NFRCAG', # Treasury and Agency Securities: Non-MBS, Foreign-Related Institutions
]
