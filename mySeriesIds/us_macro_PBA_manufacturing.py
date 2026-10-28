
# FRED > Production & Business Activity > Manufacturing (category_id 32429)
# 하위 카테고리 6개 + 카테고리 직속 시리즈 전체. 주기는 FRED 메타데이터 기준
dir='us_macro_PBA_manufacturing'

# Monthly (1412)
ids_M = [
    # Manufacturing > Inventories (386)
    ## Current Finished Goods Inventories - Texas
    'FGIDSAMFRBDAL', # Current Finished Goods Inventories; Percentage Reporting Decreases for Texas
    'FGIDUAMFRBDAL', # Current Finished Goods Inventories; Percentage Reporting Decreases for Texas (NSA)
    'FGIISAMFRBDAL', # Current Finished Goods Inventories; Percentage Reporting Increases for Texas
    'FGIIUAMFRBDAL', # Current Finished Goods Inventories; Percentage Reporting Increases for Texas (NSA)
    'FGINSAMFRBDAL', # Current Finished Goods Inventories; Percentage Reporting No Change for Texas
    'FGINUAMFRBDAL', # Current Finished Goods Inventories; Percentage Reporting No Change for Texas (NSA)
    'FGISAMFRBDAL', # Current Finished Goods Inventories; Diffusion Index for Texas
    'FGIUAMFRBDAL', # Current Finished Goods Inventories; Diffusion Index for Texas (NSA)
    ## Current Inventories - Federal Reserve District 3: Philadelphia
    'IVCDFNA066MNFRBPHI', # Current Inventories; Diffusion Index for Federal Reserve District 3: Philadelphia (NSA)
    'IVCDFSA066MSFRBPHI', # Current Inventories; Diffusion Index for Federal Reserve District 3: Philadelphia
    'IVCDNA156MNFRBPHI', # Current Inventories; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia (NSA)
    'IVCDSA156MSFRBPHI', # Current Inventories; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia
    'IVCINA156MNFRBPHI', # Current Inventories; Percent Reporting Increases for Federal Reserve District 3: Philadelphia (NSA)
    'IVCISA156MSFRBPHI', # Current Inventories; Percent Reporting Increases for Federal Reserve District 3: Philadelphia
    'IVCNNA156MNFRBPHI', # Current Inventories; Percent Reporting No Change for Federal Reserve District 3: Philadelphia (NSA)
    'IVCNSA156MSFRBPHI', # Current Inventories; Percent Reporting No Change for Federal Reserve District 3: Philadelphia
    ## Current Inventories - New York
    'IVCDINA066MNFRBNY', # Current Inventories; Diffusion Index for New York (NSA)
    'IVCDISA066MSFRBNY', # Current Inventories; Diffusion Index for New York
    'IVCDNA156MNFRBNY', # Current Inventories; Percent Reporting Decreases for New York (NSA)
    'IVCDSA156MSFRBNY', # Current Inventories; Percent Reporting Decreases for New York
    'IVCINA156MNFRBNY', # Current Inventories; Percent Reporting Increases for New York (NSA)
    'IVCISA156MSFRBNY', # Current Inventories; Percent Reporting Increases for New York
    'IVCNNA156MNFRBNY', # Current Inventories; Percent Reporting No Change for New York (NSA)
    'IVCNSA156MSFRBNY', # Current Inventories; Percent Reporting No Change for New York
    ## Current Materials Inventories - Texas
    'MATIDSAMFRBDAL', # Current Materials Inventories; Percentage Reporting Decreases for Texas (DISCONTINUED)
    'MATIDUAMFRBDAL', # Current Materials Inventories; Percentage Reporting Decreases for Texas (DISCONTINUED) (NSA)
    'MATIISAMFRBDAL', # Current Materials Inventories; Percentage Reporting Increases for Texas (DISCONTINUED)
    'MATIIUAMFRBDAL', # Current Materials Inventories; Percentage Reporting Increases for Texas (DISCONTINUED) (NSA)
    'MATINSAMFRBDAL', # Current Materials Inventories; Percentage Reporting No Change for Texas (DISCONTINUED)
    'MATINUAMFRBDAL', # Current Materials Inventories; Percentage Reporting No Change for Texas (DISCONTINUED) (NSA)
    'MATISAMFRBDAL', # Current Materials Inventories; Diffusion Index for Texas (DISCONTINUED)
    'MATIUAMFRBDAL', # Current Materials Inventories; Diffusion Index for Texas (DISCONTINUED) (NSA)
    ## Future Finished Goods Inventories - Texas
    'FFGIDSAMFRBDAL', # Future Finished Goods Inventories; Percentage Reporting Decreases for Texas
    'FFGIDUAMFRBDAL', # Future Finished Goods Inventories; Percentage Reporting Decreases for Texas (NSA)
    'FFGIISAMFRBDAL', # Future Finished Goods Inventories; Percentage Reporting Increases for Texas
    'FFGIIUAMFRBDAL', # Future Finished Goods Inventories; Percentage Reporting Increases for Texas (NSA)
    'FFGINSAMFRBDAL', # Future Finished Goods Inventories; Percentage Reporting No Change for Texas
    'FFGINUAMFRBDAL', # Future Finished Goods Inventories; Percentage Reporting No Change for Texas (NSA)
    'FFGISAMFRBDAL', # Future Finished Goods Inventories; Diffusion Index for Texas
    'FFGIUAMFRBDAL', # Future Finished Goods Inventories; Diffusion Index for Texas (NSA)
    ## Future Inventories - Federal Reserve District 3: Philadelphia
    'IVFDFNA066MNFRBPHI', # Future Inventories; Diffusion Index for Federal Reserve District 3: Philadelphia (NSA)
    'IVFDFSA066MSFRBPHI', # Future Inventories; Diffusion Index for Federal Reserve District 3: Philadelphia
    'IVFDNA156MNFRBPHI', # Future Inventories; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia (NSA)
    'IVFDSA156MSFRBPHI', # Future Inventories; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia
    'IVFINA156MNFRBPHI', # Future Inventories; Percent Reporting Increases for Federal Reserve District 3: Philadelphia (NSA)
    'IVFISA156MSFRBPHI', # Future Inventories; Percent Reporting Increases for Federal Reserve District 3: Philadelphia
    'IVFNNA156MNFRBPHI', # Future Inventories; Percent Reporting No Change for Federal Reserve District 3: Philadelphia (NSA)
    'IVFNSA156MSFRBPHI', # Future Inventories; Percent Reporting No Change for Federal Reserve District 3: Philadelphia
    ## Future Inventories - New York
    'IVFDINA066MNFRBNY', # Future Inventories; Diffusion Index for New York (NSA)
    'IVFDISA066MSFRBNY', # Future Inventories; Diffusion Index for New York
    'IVFDNA156MNFRBNY', # Future Inventories; Percent Expecting Decreases for New York (NSA)
    'IVFDSA156MSFRBNY', # Future Inventories; Percent Expecting Decreases for New York
    'IVFINA156MNFRBNY', # Future Inventories; Percent Expecting Increases for New York (NSA)
    'IVFISA156MSFRBNY', # Future Inventories; Percent Expecting Increases for New York
    'IVFNNA156MNFRBNY', # Future Inventories; Percent Expecting No Change for New York (NSA)
    'IVFNSA156MSFRBNY', # Future Inventories; Percent Expecting No Change for New York
    ## Future Materials Inventories - Texas
    'FMATIDSAMFRBDAL', # Future Materials Inventories; Percentage Reporting Decreases for Texas (DISCONTINUED)
    'FMATIDUAMFRBDAL', # Future Materials Inventories; Percentage Reporting Decreases for Texas (DISCONTINUED) (NSA)
    'FMATIISAMFRBDAL', # Future Materials Inventories; Percentage Reporting Increases for Texas (DISCONTINUED)
    'FMATIIUAMFRBDAL', # Future Materials Inventories; Percentage Reporting Increases for Texas (DISCONTINUED) (NSA)
    'FMATINSAMFRBDAL', # Future Materials Inventories; Percentage Reporting No Change for Texas (DISCONTINUED)
    'FMATINUAMFRBDAL', # Future Materials Inventories; Percentage Reporting No Change for Texas (DISCONTINUED) (NSA)
    'FMATISAMFRBDAL', # Future Materials Inventories; Diffusion Index for Texas (DISCONTINUED)
    'FMATIUAMFRBDAL', # Future Materials Inventories; Diffusion Index for Texas (DISCONTINUED) (NSA)
    ## Manufacturers' Finished Goods Inventories
    'A11SFI', # Manufacturers' Finished Goods Inventories: Food Products
    'A12SFI', # Manufacturers' Finished Goods Inventories: Beverage and Tobacco Products
    'A13SFI', # Manufacturers' Finished Goods Inventories: Textile Mills
    'A14SFI', # Manufacturers' Finished Goods Inventories: Textile Products
    'A15SFI', # Manufacturers' Finished Goods Inventories: Apparel
    'A16SFI', # Manufacturers' Finished Goods Inventories: Leather and Allied Products
    'A21SFI', # Manufacturers' Finished Goods Inventories: Wood Products
    'A22SFI', # Manufacturers' Finished Goods Inventories: Paper Products
    'A23SFI', # Manufacturers' Finished Goods Inventories: Printing
    'A24SFI', # Manufacturers' Finished Goods Inventories: Petroleum and Coal Products
    'A25SFI', # Manufacturers' Finished Goods Inventories: Chemical Products
    'A26SFI', # Manufacturers' Finished Goods Inventories: Plastics and Rubber Products
    'A27SFI', # Manufacturers' Finished Goods Inventories: Nonmetallic Mineral Products
    'A31SFI', # Manufacturers' Finished Goods Inventories: Primary Metals
    'A32SFI', # Manufacturers' Finished Goods Inventories: Fabricated Metal Products
    'A33SFI', # Manufacturers' Finished Goods Inventories: Machinery
    'A34SFI', # Manufacturers' Finished Goods Inventories: Computers and Electronic Products
    'A35SFI', # Manufacturers' Finished Goods Inventories: Electrical Equipment, Appliances and Components
    'A36SFI', # Manufacturers' Finished Goods Inventories: Transportation Equipment
    'A37SFI', # Manufacturers' Finished Goods Inventories: Furniture and Related Products
    'A39SFI', # Manufacturers' Finished Goods Inventories: Miscellaneous Products
    'AMDMFI', # Manufacturers' Finished Goods Inventories: Durable Goods
    'AMNMFI', # Manufacturers' Finished Goods Inventories: Nondurable Goods
    'AMTMFI', # Manufacturers' Finished Goods Inventories: Total Manufacturing
    'U11SFI', # Manufacturers' Finished Goods Inventories: Food Products (NSA)
    'U12SFI', # Manufacturers' Finished Goods Inventories: Beverage and Tobacco Products (NSA)
    'U13SFI', # Manufacturers' Finished Goods Inventories: Textile Mills (NSA)
    'U14SFI', # Manufacturers' Finished Goods Inventories: Textile Products (NSA)
    'U15SFI', # Manufacturers' Finished Goods Inventories: Apparel (NSA)
    'U16SFI', # Manufacturers' Finished Goods Inventories: Leather and Allied Products (NSA)
    'U21SFI', # Manufacturers' Finished Goods Inventories: Wood Products (NSA)
    'U22SFI', # Manufacturers' Finished Goods Inventories: Paper Products (NSA)
    'U23SFI', # Manufacturers' Finished Goods Inventories: Printing (NSA)
    'U24SFI', # Manufacturers' Finished Goods Inventories: Petroleum and Coal Products (NSA)
    'U25SFI', # Manufacturers' Finished Goods Inventories: Chemical Products (NSA)
    'U26SFI', # Manufacturers' Finished Goods Inventories: Plastics and Rubber Products (NSA)
    'U27SFI', # Manufacturers' Finished Goods Inventories: Nonmetallic Mineral Products (NSA)
    'U31SFI', # Manufacturers' Finished Goods Inventories: Primary Metals (NSA)
    'U32SFI', # Manufacturers' Finished Goods Inventories: Fabricated Metal Products (NSA)
    'U33SFI', # Manufacturers' Finished Goods Inventories: Machinery (NSA)
    'U34SFI', # Manufacturers' Finished Goods Inventories: Computers and Electronic Products (NSA)
    'U35SFI', # Manufacturers' Finished Goods Inventories: Electrical Equipment, Appliances and Components (NSA)
    'U36SFI', # Manufacturers' Finished Goods Inventories: Transportation Equipment (NSA)
    'U37SFI', # Manufacturers' Finished Goods Inventories: Furniture and Related Products (NSA)
    'U39SFI', # Manufacturers' Finished Goods Inventories: Miscellaneous Products (NSA)
    'UMDMFI', # Manufacturers' Finished Goods Inventories: Durable Goods (NSA)
    'UMNMFI', # Manufacturers' Finished Goods Inventories: Nondurable Goods (NSA)
    'UMTMFI', # Manufacturers' Finished Goods Inventories: Total Manufacturing (NSA)
    ## Manufacturers' Materials and Supplies Inventories
    'A11SMI', # Manufacturers' Materials and Supplies Inventories: Food Products
    'A12SMI', # Manufacturers' Materials and Supplies Inventories: Beverage and Tobacco Products
    'A13SMI', # Manufacturers' Materials and Supplies Inventories: Textile Mills
    'A14SMI', # Manufacturers' Materials and Supplies Inventories: Textile Products
    'A15SMI', # Manufacturers' Materials and Supplies Inventories: Apparel
    'A16SMI', # Manufacturers' Materials and Supplies Inventories: Leather and Allied Products
    'A21SMI', # Manufacturers' Materials and Supplies Inventories: Wood Products
    'A22SMI', # Manufacturers' Materials and Supplies Inventories: Paper Products
    'A23SMI', # Manufacturers' Materials and Supplies Inventories: Printing
    'A24SMI', # Manufacturers' Materials and Supplies Inventories: Petroleum and Coal Products
    'A25SMI', # Manufacturers' Materials and Supplies Inventories: Chemical Products
    'A26SMI', # Manufacturers' Materials and Supplies Inventories: Plastics and Rubber Products
    'A27SMI', # Manufacturers' Materials and Supplies Inventories: Nonmetallic Mineral Products
    'A31SMI', # Manufacturers' Materials and Supplies Inventories: Primary Metals
    'A32SMI', # Manufacturers' Materials and Supplies Inventories: Fabricated Metal Products
    'A33SMI', # Manufacturers' Materials and Supplies Inventories: Machinery
    'A34SMI', # Manufacturers' Materials and Supplies Inventories: Computers and Electronic Products
    'A35SMI', # Manufacturers' Materials and Supplies Inventories: Electrical Equipment, Appliances and Components
    'A36SMI', # Manufacturers' Materials and Supplies Inventories: Transportation Equipment
    'A37SMI', # Manufacturers' Materials and Supplies Inventories: Furniture and Related Products
    'A39SMI', # Manufacturers' Materials and Supplies Inventories: Miscellaneous Products
    'AMDMMI', # Manufacturers' Materials and Supplies Inventories: Durable Goods
    'AMNMMI', # Manufacturers' Materials and Supplies Inventories: Nondurable Goods
    'AMTMMI', # Manufacturers' Materials and Supplies Inventories: Total Manufacturing
    'U11SMI', # Manufacturers' Materials and Supplies Inventories: Food Products (NSA)
    'U12SMI', # Manufacturers' Materials and Supplies Inventories: Beverage and Tobacco Products (NSA)
    'U13SMI', # Manufacturers' Materials and Supplies Inventories: Textile Mills (NSA)
    'U14SMI', # Manufacturers' Materials and Supplies Inventories: Textile Products (NSA)
    'U15SMI', # Manufacturers' Materials and Supplies Inventories: Apparel (NSA)
    'U16SMI', # Manufacturers' Materials and Supplies Inventories: Leather and Allied Products (NSA)
    'U21SMI', # Manufacturers' Materials and Supplies Inventories: Wood Products (NSA)
    'U22SMI', # Manufacturers' Materials and Supplies Inventories: Paper Products (NSA)
    'U23SMI', # Manufacturers' Materials and Supplies Inventories: Printing (NSA)
    'U24SMI', # Manufacturers' Materials and Supplies Inventories: Petroleum and Coal Products (NSA)
    'U25SMI', # Manufacturers' Materials and Supplies Inventories: Chemical Products (NSA)
    'U26SMI', # Manufacturers' Materials and Supplies Inventories: Plastics and Rubber Products (NSA)
    'U27SMI', # Manufacturers' Materials and Supplies Inventories: Nonmetallic Mineral Products (NSA)
    'U31SMI', # Manufacturers' Materials and Supplies Inventories: Primary Metals (NSA)
    'U32SMI', # Manufacturers' Materials and Supplies Inventories: Fabricated Metal Products (NSA)
    'U33SMI', # Manufacturers' Materials and Supplies Inventories: Machinery (NSA)
    'U34SMI', # Manufacturers' Materials and Supplies Inventories: Computers and Electronic Products (NSA)
    'U35SMI', # Manufacturers' Materials and Supplies Inventories: Electrical Equipment, Appliances and Components (NSA)
    'U36SMI', # Manufacturers' Materials and Supplies Inventories: Transportation Equipment (NSA)
    'U37SMI', # Manufacturers' Materials and Supplies Inventories: Furniture and Related Products (NSA)
    'U39SMI', # Manufacturers' Materials and Supplies Inventories: Miscellaneous Products (NSA)
    'UMDMMI', # Manufacturers' Materials and Supplies Inventories: Durable Goods (NSA)
    'UMNMMI', # Manufacturers' Materials and Supplies Inventories: Nondurable Goods (NSA)
    'UMTMMI', # Manufacturers' Materials and Supplies Inventories: Total Manufacturing (NSA)
    ## Manufacturers' Total Inventories
    'A11ATI', # Manufacturers' Total Inventories: Grain and Oilseed Milling
    'A11BTI', # Manufacturers' Total Inventories: Dairy Product Manufacturing
    'A11CTI', # Manufacturers' Total Inventories: Meat, Poultry, and Seafood Product Processing
    'A11STI', # Manufacturers' Total Inventories: Food Products
    'A12ATI', # Manufacturers' Total Inventories: Beverage Manufacturing
    'A12BTI', # Manufacturers' Total Inventories: Tobacco Manufacturing
    'A12STI', # Manufacturers' Total Inventories: Beverage and Tobacco Products
    'A13STI', # Manufacturers' Total Inventories: Textile Mills
    'A14STI', # Manufacturers' Total Inventories: Textile Products
    'A15STI', # Manufacturers' Total Inventories: Apparel
    'A16STI', # Manufacturers' Total Inventories: Leather and Allied Products
    'A21STI', # Manufacturers' Total Inventories: Wood Products
    'A22ATI', # Manufacturers' Total Inventories: Pulp, Paper, and Paperboard Mills
    'A22BTI', # Manufacturers' Total Inventories: Paperboard Container Manufacturing
    'A22STI', # Manufacturers' Total Inventories: Paper Products
    'A23STI', # Manufacturers' Total Inventories: Printing
    'A24ATI', # Manufacturers' Total Inventories: Petroleum Refineries
    'A24STI', # Manufacturers' Total Inventories: Petroleum and Coal Products
    'A25ATI', # Manufacturers' Total Inventories: Pesticide, Fertilizer, and Other Agricultural Chemical Manufacturing
    'A25BTI', # Manufacturers' Total Inventories: Pharmaceutical and Medicine Manufacturing
    'A25CTI', # Manufacturers' Total Inventories: Paint, Coating, and Adhesive, Manufacturing
    'A25STI', # Manufacturers' Total Inventories: Chemical Products
    'A26STI', # Manufacturers' Total Inventories: Plastics and Rubber Products
    'A27STI', # Manufacturers' Total Inventories: Nonmetallic Mineral Products
    'A31ATI', # Manufacturers' Total Inventories: Iron and Steel Mills and Ferroalloy and Steel Product Manufacturing
    'A31CTI', # Manufacturers' Total Inventories: Ferrous Metal Foundries
    'A31STI', # Manufacturers' Total Inventories: Primary Metals
    'A32STI', # Manufacturers' Total Inventories: Fabricated Metal Products
    'A33ATI', # Manufacturers' Total Inventories: Farm Machinery and Equipment Manufacturing
    'A33CTI', # Manufacturers' Total Inventories: Construction Machinery Manufacturing
    'A33DTI', # Manufacturers' Total Inventories: Mining, Oil, and Gas Field Machinery Manufacturing
    'A33ETI', # Manufacturers' Total Inventories: Industrial Machinery Manufacturing
    'A33GTI', # Manufacturers' Total Inventories: Photographic Equipment Manufacturing
    'A33HTI', # Manufacturers' Total Inventories: Ventilation, Heating, Air-Conditioning, and Refrigeration Equipment Manufacturing
    'A33ITI', # Manufacturers' Total Inventories: Metalworking Machinery Manufacturing
    'A33MTI', # Manufacturers' Total Inventories: Material Handling Equipment Manufacturing
    'A33STI', # Manufacturers' Total Inventories: Machinery
    'A34ATI', # Manufacturers' Total Inventories: Electronic Computer Manufacturing
    'A34BTI', # Manufacturers' Total Inventories: Computer Storage Device Manufacturing
    'A34CTI', # Manufacturers' Total Inventories: Other Computer Peripheral Equipment Manufacturing
    'A34DTI', # Manufacturers' Total Inventories: Communications Equipment, Nondefense
    'A34ETI', # Manufacturers' Total Inventories: Communications Equipment Manufacturing, Defense
    'A34FTI', # Manufacturers' Total Inventories: Audio and Video Equipment
    'A34HTI', # Manufacturers' Total Inventories: Other Electronic Component Manufacturing
    'A34ITI', # Manufacturers' Total Inventories: Search and Navigation Equipment, Nondefense
    'A34JTI', # Manufacturers' Total Inventories: Search and Navigation Equipment, Defense
    'A34KTI', # Manufacturers' Total Inventories: Electromedical, Measuring, and Control Instrument Manufacturing
    'A34STI', # Manufacturers' Total Inventories: Computers and Electronic Products
    'A34XTI', # Manufacturers' Total Inventories: Communications Equipment
    'A35ATI', # Manufacturers' Total Inventories: Electric Lighting Equipment Manufacturing
    'A35BTI', # Manufacturers' Total Inventories: Household Appliance Manufacturing
    'A35CTI', # Manufacturers' Total Inventories: Electrical Equipment Manufacturing
    'A35DTI', # Manufacturers' Total Inventories: Battery Manufacturing
    'A35STI', # Manufacturers' Total Inventories: Electrical Equipment, Appliances and Components
    'A36ATI', # Manufacturers' Total Inventories: Automobile Manufacturing
    'A36BTI', # Manufacturers' Total Inventories: Light Truck and Utility Vehicle Manufacturing
    'A36CTI', # Manufacturers' Total Inventories: Heavy Duty Truck Manufacturing
    'A36STI', # Manufacturers' Total Inventories: Transportation Equipment
    'A36ZTI', # Manufacturers' Total Inventories: Ships and Boats
    'A37STI', # Manufacturers' Total Inventories: Furniture and Related Products
    'A39STI', # Manufacturers' Total Inventories: Miscellaneous Products
    'AANMTI', # Manufacturers' Total Inventories: Aluminum and Nonferrous Metal Products
    'ABTPTI', # Manufacturers' Total Inventories: Motor Vehicle Bodies, Trailers, and Parts
    'ACDGTI', # Manufacturers' Total Inventories: Consumer Durable Goods
    'ACMSTI', # Manufacturers' Total Inventories: Construction Materials and Supplies
    'ACNGTI', # Manufacturers' Total Inventories: Consumer Nondurable Goods
    'ACOGTI', # Manufacturers' Total Inventories: Consumer Goods
    'ACRPTI', # Manufacturers' Total Inventories: Computers and Related Products
    'ADAPTI', # Manufacturers' Total Inventories: Defense Aircraft and Parts
    'ADEFTI', # Manufacturers' Total Inventories: Defense Capital Goods
    'ADXDTI', # Manufacturers' Total Inventories: Durable Goods Excluding Defense
    'ADXTTI', # Manufacturers' Total Inventories: Durable Goods Excluding Transportation
    'AITITI', # Manufacturers' Total Inventories: Information Technology Industries
    'AMDMTI', # Manufacturers' Total Inventories: Durable Goods
    'AMNMTI', # Manufacturers' Total Inventories: Nondurable Goods
    'AMTMTI', # Manufacturers' Total Inventories: Total Manufacturing
    'AMTUTI', # Manufacturers' Total Inventories: Manufacturing with Unfilled Orders
    'AMVPTI', # Manufacturers' Total Inventories: Motor Vehicles and Parts
    'AMXDTI', # Manufacturers' Total Inventories: Manufacturing Excluding Defense
    'AMXTTI', # Manufacturers' Total Inventories: Manufacturing Excluding Transportation
    'ANAPTI', # Manufacturers' Total Inventories: Nondefense Aircraft and Parts
    'ANDETI', # Manufacturers' Total Inventories: Nondefense Capital Goods
    'ANXATI', # Manufacturers' Total Inventories: Nondefense Capital Goods Excluding Aircraft
    'AODGTI', # Manufacturers' Total Inventories: All Other Durable Goods
    'ATCGTI', # Manufacturers' Total Inventories: Capital Goods
    'ATGPTI', # Manufacturers' Total Inventories: Turbines, Generators, and Other Power Transmission Equipment
    'U11ATI', # Manufacturers' Total Inventories: Grain and Oilseed Milling (NSA)
    'U11BTI', # Manufacturers' Total Inventories: Dairy Product Manufacturing (NSA)
    'U11CTI', # Manufacturers' Total Inventories: Meat, Poultry, and Seafood Product Processing (NSA)
    'U11STI', # Manufacturers' Total Inventories: Food Products (NSA)
    'U12ATI', # Manufacturers' Total Inventories: Beverage Manufacturing (NSA)
    'U12BTI', # Manufacturers' Total Inventories: Tobacco Manufacturing (NSA)
    'U12STI', # Manufacturers' Total Inventories: Beverage and Tobacco Products (NSA)
    'U13STI', # Manufacturers' Total Inventories: Textile Mills (NSA)
    'U14STI', # Manufacturers' Total Inventories: Textile Products (NSA)
    'U15STI', # Manufacturers' Total Inventories: Apparel (NSA)
    'U16STI', # Manufacturers' Total Inventories: Leather and Allied Products (NSA)
    'U21STI', # Manufacturers' Total Inventories: Wood Products (NSA)
    'U22ATI', # Manufacturers' Total Inventories: Pulp, Paper, and Paperboard Mills (NSA)
    'U22BTI', # Manufacturers' Total Inventories: Paperboard Container Manufacturing (NSA)
    'U22STI', # Manufacturers' Total Inventories: Paper Products (NSA)
    'U23STI', # Manufacturers' Total Inventories: Printing (NSA)
    'U24ATI', # Manufacturers' Total Inventories: Petroleum Refineries (NSA)
    'U24STI', # Manufacturers' Total Inventories: Petroleum and Coal Products (NSA)
    'U25ATI', # Manufacturers' Total Inventories: Pesticide, Fertilizer, and Other Agricultural Chemical Manufacturing (NSA)
    'U25BTI', # Manufacturers' Total Inventories: Pharmaceutical and Medicine Manufacturing (NSA)
    'U25CTI', # Manufacturers' Total Inventories: Paint, Coating, and Adhesive, Manufacturing (NSA)
    'U25STI', # Manufacturers' Total Inventories: Chemical Products (NSA)
    'U26STI', # Manufacturers' Total Inventories: Plastics and Rubber Products (NSA)
    'U27STI', # Manufacturers' Total Inventories: Nonmetallic Mineral Products (NSA)
    'U31ATI', # Manufacturers' Total Inventories: Iron and Steel Mills and Ferroalloy and Steel Product Manufacturing (NSA)
    'U31CTI', # Manufacturers' Total Inventories: Ferrous Metal Foundries (NSA)
    'U31STI', # Manufacturers' Total Inventories: Primary Metals (NSA)
    'U32STI', # Manufacturers' Total Inventories: Fabricated Metal Products (NSA)
    'U33ATI', # Manufacturers' Total Inventories: Farm Machinery and Equipment Manufacturing (NSA)
    'U33CTI', # Manufacturers' Total Inventories: Construction Machinery Manufacturing (NSA)
    'U33DTI', # Manufacturers' Total Inventories: Mining, Oil, and Gas Field Machinery Manufacturing (NSA)
    'U33ETI', # Manufacturers' Total Inventories: Industrial Machinery Manufacturing (NSA)
    'U33GTI', # Manufacturers' Total Inventories: Photographic Equipment Manufacturing (NSA)
    'U33HTI', # Manufacturers' Total Inventories: Ventilation, Heating, Air-Conditioning, and Refrigeration Equipment Manufacturing (NSA)
    'U33ITI', # Manufacturers' Total Inventories: Metalworking Machinery Manufacturing (NSA)
    'U33MTI', # Manufacturers' Total Inventories: Material Handling Equipment Manufacturing (NSA)
    'U33STI', # Manufacturers' Total Inventories: Machinery (NSA)
    'U34ATI', # Manufacturers' Total Inventories: Electronic Computer Manufacturing (NSA)
    'U34BTI', # Manufacturers' Total Inventories: Computer Storage Device Manufacturing (NSA)
    'U34CTI', # Manufacturers' Total Inventories: Other Computer Peripheral Equipment Manufacturing (NSA)
    'U34DTI', # Manufacturers' Total Inventories: Communications Equipment, Nondefense (NSA)
    'U34ETI', # Manufacturers' Total Inventories: Communications Equipment Manufacturing, Defense (NSA)
    'U34FTI', # Manufacturers' Total Inventories: Audio and Video Equipment (NSA)
    'U34HTI', # Manufacturers' Total Inventories: Other Electronic Component Manufacturing (NSA)
    'U34ITI', # Manufacturers' Total Inventories: Search and Navigation Equipment, Nondefense (NSA)
    'U34JTI', # Manufacturers' Total Inventories: Search and Navigation Equipment, Defense (NSA)
    'U34KTI', # Manufacturers' Total Inventories: Electromedical, Measuring, and Control Instrument Manufacturing (NSA)
    'U34STI', # Manufacturers' Total Inventories: Computers and Electronic Products (NSA)
    'U34XTI', # Manufacturers' Total Inventories: Communications Equipment (NSA)
    'U35ATI', # Manufacturers' Total Inventories: Electric Lighting Equipment Manufacturing (NSA)
    'U35BTI', # Manufacturers' Total Inventories: Household Appliance Manufacturing (NSA)
    'U35CTI', # Manufacturers' Total Inventories: Electrical Equipment Manufacturing (NSA)
    'U35DTI', # Manufacturers' Total Inventories: Battery Manufacturing (NSA)
    'U35STI', # Manufacturers' Total Inventories: Electrical Equipment, Appliances and Components (NSA)
    'U36ATI', # Manufacturers' Total Inventories: Automobile Manufacturing (NSA)
    'U36BTI', # Manufacturers' Total Inventories: Light Truck and Utility Vehicle Manufacturing (NSA)
    'U36CTI', # Manufacturers' Total Inventories: Heavy Duty Truck Manufacturing (NSA)
    'U36STI', # Manufacturers' Total Inventories: Transportation Equipment (NSA)
    'U36ZTI', # Manufacturers' Total Inventories: Ships and Boats (NSA)
    'U37STI', # Manufacturers' Total Inventories: Furniture and Related Products (NSA)
    'U39STI', # Manufacturers' Total Inventories: Miscellaneous Products (NSA)
    'UANMTI', # Manufacturers' Total Inventories: Aluminum and Nonferrous Metal Products (NSA)
    'UBTPTI', # Manufacturers' Total Inventories: Motor Vehicle Bodies, Trailers, and Parts (NSA)
    'UCDGTI', # Manufacturers' Total Inventories: Consumer Durable Goods (NSA)
    'UCMSTI', # Manufacturers' Total Inventories: Construction Materials and Supplies (NSA)
    'UCNGTI', # Manufacturers' Total Inventories: Consumer Nondurable Goods (NSA)
    'UCOGTI', # Manufacturers' Total Inventories: Consumer Goods (NSA)
    'UCRPTI', # Manufacturers' Total Inventories: Computers and Related Products (NSA)
    'UDAPTI', # Manufacturers' Total Inventories: Defense Aircraft and Parts (NSA)
    'UDEFTI', # Manufacturers' Total Inventories: Defense Capital Goods (NSA)
    'UDXDTI', # Manufacturers' Total Inventories: Durable Goods Excluding Defense (NSA)
    'UDXTTI', # Manufacturers' Total Inventories: Durable Goods Excluding Transportation (NSA)
    'UITITI', # Manufacturers' Total Inventories: Information Technology Industries (NSA)
    'UMDMTI', # Manufacturers' Total Inventories: Durable Goods (NSA)
    'UMNMTI', # Manufacturers' Total Inventories: Nondurable Goods (NSA)
    'UMTMTI', # Manufacturers' Total Inventories: Total Manufacturing (NSA)
    'UMTUTI', # Manufacturers' Total Inventories: Manufacturing with Unfilled Orders (NSA)
    'UMVPTI', # Manufacturers' Total Inventories: Motor Vehicles and Parts (NSA)
    'UMXDTI', # Manufacturers' Total Inventories: Manufacturing Excluding Defense (NSA)
    'UMXTTI', # Manufacturers' Total Inventories: Manufacturing Excluding Transportation (NSA)
    'UNAPTI', # Manufacturers' Total Inventories: Nondefense Aircraft and Parts (NSA)
    'UNDETI', # Manufacturers' Total Inventories: Nondefense Capital Goods (NSA)
    'UNXATI', # Manufacturers' Total Inventories: Nondefense Capital Goods Excluding Aircraft (NSA)
    'UODGTI', # Manufacturers' Total Inventories: All Other Durable Goods (NSA)
    'UTCGTI', # Manufacturers' Total Inventories: Capital Goods (NSA)
    'UTGPTI', # Manufacturers' Total Inventories: Turbines, Generators, and Other Power Transmission Equipment (NSA)
    ## Manufacturers' Work in Process Inventories
    'A11SWI', # Manufacturers' Work in Process Inventories: Food Products
    'A12SWI', # Manufacturers' Work in Process Inventories: Beverage and Tobacco Products
    'A13SWI', # Manufacturers' Work in Process Inventories: Textile Mills
    'A14SWI', # Manufacturers' Work in Process Inventories: Textile Products
    'A15SWI', # Manufacturers' Work in Process Inventories: Apparel
    'A16SWI', # Manufacturers' Work in Process Inventories: Leather and Allied Products
    'A21SWI', # Manufacturers' Work in Process Inventories: Wood Products
    'A22SWI', # Manufacturers' Work in Process Inventories: Paper Products
    'A23SWI', # Manufacturers' Work in Process Inventories: Printing
    'A24SWI', # Manufacturers' Work in Process Inventories: Petroleum and Coal Products
    'A25SWI', # Manufacturers' Work in Process Inventories: Chemical Products
    'A26SWI', # Manufacturers' Work in Process Inventories: Plastics and Rubber Products
    'A27SWI', # Manufacturers' Work in Process Inventories: Nonmetallic Mineral Products
    'A31SWI', # Manufacturers' Work in Process Inventories: Primary Metals
    'A32SWI', # Manufacturers' Work in Process Inventories: Fabricated Metal Products
    'A33SWI', # Manufacturers' Work in Process Inventories: Machinery
    'A34SWI', # Manufacturers' Work in Process Inventories: Computers and Electronic Products
    'A35SWI', # Manufacturers' Work in Process Inventories: Electrical Equipment, Appliances and Components
    'A36SWI', # Manufacturers' Work in Process Inventories: Transportation Equipment
    'A37SWI', # Manufacturers' Work in Process Inventories: Furniture and Related Products
    'A39SWI', # Manufacturers' Work in Process Inventories: Miscellaneous Products
    'AMDMWI', # Manufacturers' Work in Process Inventories: Durable Goods
    'AMNMWI', # Manufacturers' Work in Process Inventories: Nondurable Goods
    'AMTMWI', # Manufacturers' Work in Process Inventories: Total Manufacturing
    'U11SWI', # Manufacturers' Work in Process Inventories: Food Products (NSA)
    'U12SWI', # Manufacturers' Work in Process Inventories: Beverage and Tobacco Products (NSA)
    'U13SWI', # Manufacturers' Work in Process Inventories: Textile Mills (NSA)
    'U14SWI', # Manufacturers' Work in Process Inventories: Textile Products (NSA)
    'U15SWI', # Manufacturers' Work in Process Inventories: Apparel (NSA)
    'U16SWI', # Manufacturers' Work in Process Inventories: Leather and Allied Products (NSA)
    'U21SWI', # Manufacturers' Work in Process Inventories: Wood Products (NSA)
    'U22SWI', # Manufacturers' Work in Process Inventories: Paper Products (NSA)
    'U23SWI', # Manufacturers' Work in Process Inventories: Printing (NSA)
    'U24SWI', # Manufacturers' Work in Process Inventories: Petroleum and Coal Products (NSA)
    'U25SWI', # Manufacturers' Work in Process Inventories: Chemical Products (NSA)
    'U26SWI', # Manufacturers' Work in Process Inventories: Plastics and Rubber Products (NSA)
    'U27SWI', # Manufacturers' Work in Process Inventories: Nonmetallic Mineral Products (NSA)
    'U31SWI', # Manufacturers' Work in Process Inventories: Primary Metals (NSA)
    'U32SWI', # Manufacturers' Work in Process Inventories: Fabricated Metal Products (NSA)
    'U33SWI', # Manufacturers' Work in Process Inventories: Machinery (NSA)
    'U34SWI', # Manufacturers' Work in Process Inventories: Computers and Electronic Products (NSA)
    'U35SWI', # Manufacturers' Work in Process Inventories: Electrical Equipment, Appliances and Components (NSA)
    'U36SWI', # Manufacturers' Work in Process Inventories: Transportation Equipment (NSA)
    'U37SWI', # Manufacturers' Work in Process Inventories: Furniture and Related Products (NSA)
    'U39SWI', # Manufacturers' Work in Process Inventories: Miscellaneous Products (NSA)
    'UMDMWI', # Manufacturers' Work in Process Inventories: Durable Goods (NSA)
    'UMNMWI', # Manufacturers' Work in Process Inventories: Nondurable Goods (NSA)
    'UMTMWI', # Manufacturers' Work in Process Inventories: Total Manufacturing (NSA)
    ## Real Manufacturing and Trade Inventories
    'INVCMRMT', # Real Manufacturing and Trade Inventories
    'INVCMRMTSPL', # Real Manufacturing and Trade Inventories
    'INVHMRMT', # Real Manufacturing and Trade Inventories

    # Manufacturing > New Orders (170)
    ## Current Growth Rate of Orders - Texas
    'GRODSAMFRBDAL', # Current Growth Rate of Orders; Percentage Reporting Decreases for Texas
    'GRODUAMFRBDAL', # Current Growth Rate of Orders; Percentage Reporting Decreases for Texas (NSA)
    'GROISAMFRBDAL', # Current Growth Rate of Orders; Percentage Reporting Increases for Texas
    'GROIUAMFRBDAL', # Current Growth Rate of Orders; Percentage Reporting Increases for Texas (NSA)
    'GRONSAMFRBDAL', # Current Growth Rate of Orders; Percentage Reporting No Change for Texas
    'GRONUAMFRBDAL', # Current Growth Rate of Orders; Percentage Reporting No Change for Texas (NSA)
    'GROSAMFRBDAL', # Current Growth Rate of Orders; Diffusion Index for Texas
    'GROUAMFRBDAL', # Current Growth Rate of Orders; Diffusion Index for Texas (NSA)
    ## Current New Orders - Federal Reserve District 3: Philadelphia
    'NOCDFNA066MNFRBPHI', # Current New Orders; Diffusion Index for Federal Reserve District 3: Philadelphia (NSA)
    'NOCDFSA066MSFRBPHI', # Current New Orders; Diffusion Index for Federal Reserve District 3: Philadelphia
    'NOCDNA156MNFRBPHI', # Current New Orders; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia (NSA)
    'NOCDSA156MSFRBPHI', # Current New Orders; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia
    'NOCINA156MNFRBPHI', # Current New Orders; Percent Reporting Increases for Federal Reserve District 3: Philadelphia (NSA)
    'NOCISA156MSFRBPHI', # Current New Orders; Percent Reporting Increases for Federal Reserve District 3: Philadelphia
    'NOCNNA156MNFRBPHI', # Current New Orders; Percent Reporting No Change for Federal Reserve District 3: Philadelphia (NSA)
    'NOCNSA156MSFRBPHI', # Current New Orders; Percent Reporting No Change for Federal Reserve District 3: Philadelphia
    ## Current New Orders - New York
    'NOCDINA066MNFRBNY', # Current New Orders; Diffusion Index for New York (NSA)
    'NOCDISA066MSFRBNY', # Current New Orders; Diffusion Index for New York
    'NOCDNA156MNFRBNY', # Current New Orders; Percent Reporting Decreases for New York (NSA)
    'NOCDSA156MSFRBNY', # Current New Orders; Percent Reporting Decreases for New York
    'NOCINA156MNFRBNY', # Current New Orders; Percent Reporting Increases for New York (NSA)
    'NOCISA156MSFRBNY', # Current New Orders; Percent Reporting Increases for New York
    'NOCNNA156MNFRBNY', # Current New Orders; Percent Reporting No Change for New York (NSA)
    'NOCNSA156MSFRBNY', # Current New Orders; Percent Reporting No Change for New York
    ## Current New Orders - Texas
    'VNWODSAMFRBDAL', # Current New Orders; Percentage Reporting Decreases for Texas
    'VNWODUAMFRBDAL', # Current New Orders; Percentage Reporting Decreases for Texas (NSA)
    'VNWOISAMFRBDAL', # Current New Orders; Percentage Reporting Increases for Texas
    'VNWOIUAMFRBDAL', # Current New Orders; Percentage Reporting Increases for Texas (NSA)
    'VNWONSAMFRBDAL', # Current New Orders; Percentage Reporting No Change for Texas
    'VNWONUAMFRBDAL', # Current New Orders; Percentage Reporting No Change for Texas (NSA)
    'VNWOSAMFRBDAL', # Current New Orders; Diffusion Index for Texas
    'VNWOUAMFRBDAL', # Current New Orders; Diffusion Index for Texas (NSA)
    ## Future Growth Rate of Orders - Texas
    'FGRODSAMFRBDAL', # Future Growth Rate of Orders; Percentage Reporting Decreases for Texas
    'FGRODUAMFRBDAL', # Future Growth Rate of Orders; Percentage Reporting Decreases for Texas (NSA)
    'FGROISAMFRBDAL', # Future Growth Rate of Orders; Percentage Reporting Increases for Texas
    'FGROIUAMFRBDAL', # Future Growth Rate of Orders; Percentage Reporting Increases for Texas (NSA)
    'FGRONSAMFRBDAL', # Future Growth Rate of Orders; Percentage Reporting No Change for Texas
    'FGRONUAMFRBDAL', # Future Growth Rate of Orders; Percentage Reporting No Change for Texas (NSA)
    'FGROSAMFRBDAL', # Future Growth Rate of Orders; Diffusion Index for Texas
    'FGROUAMFRBDAL', # Future Growth Rate of Orders; Diffusion Index for Texas (NSA)
    ## Future New Orders - Federal Reserve District 3: Philadelphia
    'NOFDFNA066MNFRBPHI', # Future New Orders; Diffusion Index for Federal Reserve District 3: Philadelphia (NSA)
    'NOFDFSA066MSFRBPHI', # Future New Orders; Diffusion Index for Federal Reserve District 3: Philadelphia
    'NOFDNA156MNFRBPHI', # Future New Orders; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia (NSA)
    'NOFDSA156MSFRBPHI', # Future New Orders; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia
    'NOFINA156MNFRBPHI', # Future New Orders; Percent Reporting Increases for Federal Reserve District 3: Philadelphia (NSA)
    'NOFISA156MSFRBPHI', # Future New Orders; Percent Reporting Increases for Federal Reserve District 3: Philadelphia
    'NOFNNA156MNFRBPHI', # Future New Orders; Percent Reporting No Change for Federal Reserve District 3: Philadelphia (NSA)
    'NOFNSA156MSFRBPHI', # Future New Orders; Percent Reporting No Change for Federal Reserve District 3: Philadelphia
    ## Future New Orders - New York
    'NOFDINA066MNFRBNY', # Future New Orders; Diffusion Index for New York (NSA)
    'NOFDISA066MSFRBNY', # Future New Orders; Diffusion Index for New York
    'NOFDNA156MNFRBNY', # Future New Orders; Percent Expecting Decreases for New York (NSA)
    'NOFDSA156MSFRBNY', # Future New Orders; Percent Expecting Decreases for New York
    'NOFINA156MNFRBNY', # Future New Orders; Percent Expecting Increases for New York (NSA)
    'NOFISA156MSFRBNY', # Future New Orders; Percent Expecting Increases for New York
    'NOFNNA156MNFRBNY', # Future New Orders; Percent Expecting No Change for New York (NSA)
    'NOFNSA156MSFRBNY', # Future New Orders; Percent Expecting No Change for New York
    ## Future New Orders - Texas
    'FVNWODSAMFRBDAL', # Future New Orders; Percentage Reporting Decreases for Texas
    'FVNWODUAMFRBDAL', # Future New Orders; Percentage Reporting Decreases for Texas (NSA)
    'FVNWOISAMFRBDAL', # Future New Orders; Percentage Reporting Increases for Texas
    'FVNWOIUAMFRBDAL', # Future New Orders; Percentage Reporting Increases for Texas (NSA)
    'FVNWONSAMFRBDAL', # Future New Orders; Percentage Reporting No Change for Texas
    'FVNWONUAMFRBDAL', # Future New Orders; Percentage Reporting No Change for Texas (NSA)
    'FVNWOSAMFRBDAL', # Future New Orders; Diffusion Index for Texas
    'FVNWOUAMFRBDAL', # Future New Orders; Diffusion Index for Texas (NSA)
    ## Manufacturers' New Orders
    'A31ANO', # Manufacturers' New Orders: Iron and Steel Mills and Ferroalloy and Steel Product Manufacturing
    'A31CNO', # Manufacturers' New Orders: Ferrous Metal Foundries
    'A31SNO', # Manufacturers' New Orders: Primary Metals
    'A32SNO', # Manufacturers' New Orders: Fabricated Metal Products
    'A33CNO', # Manufacturers' New Orders: Construction Machinery Manufacturing
    'A33DNO', # Manufacturers' New Orders: Mining, Oil, and Gas Field Machinery Manufacturing
    'A33ENO', # Manufacturers' New Orders: Industrial Machinery Manufacturing
    'A33GNO', # Manufacturers' New Orders: Photographic Equipment Manufacturing
    'A33HNO', # Manufacturers' New Orders: Ventilation, Heating, Air-Conditioning, and Refrigeration Equipment Manufacturing
    'A33INO', # Manufacturers' New Orders: Metalworking Machinery Manufacturing
    'A33MNO', # Manufacturers' New Orders: Material Handling Equipment Manufacturing
    'A33SNO', # Manufacturers' New Orders: Machinery
    'A34ANO', # Manufacturers' New Orders: Electronic Computer Manufacturing
    'A34DNO', # Manufacturers' New Orders: Communications Equipment, Nondefense
    'A34ENO', # Manufacturers' New Orders: Communications Equipment Manufacturing, Defense
    'A34HNO', # Manufacturers' New Orders: Other Electronic Component Manufacturing
    'A34INO', # Manufacturers' New Orders: Search and Navigation Equipment, Nondefense
    'A34JNO', # Manufacturers' New Orders: Search and Navigation Equipment, Defense
    'A34KNO', # Manufacturers' New Orders: Electromedical, Measuring, and Control Instrument Manufacturing
    'A34SNO', # Manufacturers' New Orders: Computers and Electronic Products
    'A34XNO', # Manufacturers' New Orders: Communications Equipment
    'A35ANO', # Manufacturers' New Orders: Electric Lighting Equipment Manufacturing
    'A35BNO', # Manufacturers' New Orders: Household Appliance Manufacturing
    'A35CNO', # Manufacturers' New Orders: Electrical Equipment Manufacturing
    'A35SNO', # Manufacturers' New Orders: Electrical Equipment, Appliances and Components
    'A36SNO', # Manufacturers' New Orders: Transportation Equipment
    'A36ZNO', # Manufacturers' New Orders: Ships and Boats
    'A37SNO', # Manufacturers' New Orders: Furniture and Related Products
    'AANMNO', # Manufacturers' New Orders: Aluminum and Nonferrous Metal Products
    'ABTPNO', # Manufacturers' New Orders: Motor Vehicle Bodies, Trailers, and Parts
    'ACDGNO', # Manufacturers' New Orders: Consumer Durable Goods
    'ACMSNO', # Manufacturers' New Orders: Construction Materials and Supplies
    'ACOGNO', # Manufacturers' New Orders: Consumer Goods
    'ACRPNO', # Manufacturers' New Orders: Computers and Related Products
    'ADAPNO', # Manufacturers' New Orders: Defense Aircraft and Parts
    'ADEFNO', # Manufacturers' New Orders: Defense Capital Goods
    'ADXDNO', # Manufacturers' New Orders: Durable Goods Excluding Defense
    'ADXTNO', # Manufacturers' New Orders: Durable Goods Excluding Transportation
    'AITINO', # Manufacturers' New Orders: Information Technology Industries
    'AMNMNO', # Manufacturers' New Orders: Nondurable Goods
    'AMTMNO', # Manufacturers' New Orders: Total Manufacturing
    'AMTUNO', # Manufacturers' New Orders: Manufacturing with Unfilled Orders
    'AMVPNO', # Manufacturers' New Orders: Motor Vehicles and Parts
    'AMXDNO', # Manufacturers' New Orders: Manufacturing Excluding Defense
    'AMXTNO', # Manufacturers' New Orders: Manufacturing Excluding Transportation
    'ANAPNO', # Manufacturers' New Orders: Nondefense Aircraft and Parts
    'ANDENO', # Manufacturers' New Orders: Nondefense Capital Goods
    'AODGNO', # Manufacturers' New Orders: All Other Durable Goods
    'ATCGNO', # Manufacturers' New Orders: Capital Goods
    'ATGPNO', # Manufacturers' New Orders: Turbines, Generators, and Other Power Transmission Equipment
    'DGORDER', # Manufacturers' New Orders: Durable Goods
    'NEWORDER', # Manufacturers' New Orders: Nondefense Capital Goods Excluding Aircraft
    'U31ANO', # Manufacturers' New Orders: Iron and Steel Mills and Ferroalloy and Steel Product Manufacturing (NSA)
    'U31CNO', # Manufacturers' New Orders: Ferrous Metal Foundries (NSA)
    'U31SNO', # Manufacturers' New Orders: Primary Metals (NSA)
    'U32SNO', # Manufacturers' New Orders: Fabricated Metal Products (NSA)
    'U33CNO', # Manufacturers' New Orders: Construction Machinery Manufacturing (NSA)
    'U33DNO', # Manufacturers' New Orders: Mining, Oil, and Gas Field Machinery Manufacturing (NSA)
    'U33ENO', # Manufacturers' New Orders: Industrial Machinery Manufacturing (NSA)
    'U33GNO', # Manufacturers' New Orders: Photographic Equipment Manufacturing (NSA)
    'U33HNO', # Manufacturers' New Orders: Ventilation, Heating, Air-Conditioning, and Refrigeration Equipment Manufacturing (NSA)
    'U33INO', # Manufacturers' New Orders: Metalworking Machinery Manufacturing (NSA)
    'U33MNO', # Manufacturers' New Orders: Material Handling Equipment Manufacturing (NSA)
    'U33SNO', # Manufacturers' New Orders: Machinery (NSA)
    'U34ANO', # Manufacturers' New Orders: Electronic Computer Manufacturing (NSA)
    'U34DNO', # Manufacturers' New Orders: Communications Equipment, Nondefense (NSA)
    'U34ENO', # Manufacturers' New Orders: Communications Equipment Manufacturing, Defense (NSA)
    'U34HNO', # Manufacturers' New Orders: Other Electronic Component Manufacturing (NSA)
    'U34INO', # Manufacturers' New Orders: Search and Navigation Equipment, Nondefense (NSA)
    'U34JNO', # Manufacturers' New Orders: Search and Navigation Equipment, Defense (NSA)
    'U34KNO', # Manufacturers' New Orders: Electromedical, Measuring, and Control Instrument Manufacturing (NSA)
    'U34SNO', # Manufacturers' New Orders: Computers and Electronic Products (NSA)
    'U34XNO', # Manufacturers' New Orders: Communications Equipment (NSA)
    'U35ANO', # Manufacturers' New Orders: Electric Lighting Equipment Manufacturing (NSA)
    'U35BNO', # Manufacturers' New Orders: Household Appliance Manufacturing (NSA)
    'U35CNO', # Manufacturers' New Orders: Electrical Equipment Manufacturing (NSA)
    'U35SNO', # Manufacturers' New Orders: Electrical Equipment, Appliances and Components (NSA)
    'U36SNO', # Manufacturers' New Orders: Transportation Equipment (NSA)
    'U36ZNO', # Manufacturers' New Orders: Ships and Boats (NSA)
    'U37SNO', # Manufacturers' New Orders: Furniture and Related Products (NSA)
    'UANMNO', # Manufacturers' New Orders: Aluminum and Nonferrous Metal Products (NSA)
    'UBTPNO', # Manufacturers' New Orders: Motor Vehicle Bodies, Trailers, and Parts (NSA)
    'UCDGNO', # Manufacturers' New Orders: Consumer Durable Goods (NSA)
    'UCMSNO', # Manufacturers' New Orders: Construction Materials and Supplies (NSA)
    'UCOGNO', # Manufacturers' New Orders: Consumer Goods (NSA)
    'UCRPNO', # Manufacturers' New Orders: Computers and Related Products (NSA)
    'UDAPNO', # Manufacturers' New Orders: Defense Aircraft and Parts (NSA)
    'UDEFNO', # Manufacturers' New Orders: Defense Capital Goods (NSA)
    'UDXDNO', # Manufacturers' New Orders: Durable Goods Excluding Defense (NSA)
    'UDXTNO', # Manufacturers' New Orders: Durable Goods Excluding Transportation (NSA)
    'UITINO', # Manufacturers' New Orders: Information Technology Industries (NSA)
    'UMDMNO', # Manufacturers' New Orders: Durable Goods (NSA)
    'UMNMNO', # Manufacturers' New Orders: Nondurable Goods (NSA)
    'UMTMNO', # Manufacturers' New Orders: Total Manufacturing (NSA)
    'UMTUNO', # Manufacturers' New Orders: Manufacturing with Unfilled Orders (NSA)
    'UMVPNO', # Manufacturers' New Orders: Motor Vehicles and Parts (NSA)
    'UMXDNO', # Manufacturers' New Orders: Manufacturing Excluding Defense (NSA)
    'UMXTNO', # Manufacturers' New Orders: Manufacturing Excluding Transportation (NSA)
    'UNAPNO', # Manufacturers' New Orders: Nondefense Aircraft and Parts (NSA)
    'UNDENO', # Manufacturers' New Orders: Nondefense Capital Goods (NSA)
    'UNXANO', # Manufacturers' New Orders: Nondefense Capital Goods Excluding Aircraft (NSA)
    'UODGNO', # Manufacturers' New Orders: All Other Durable Goods (NSA)
    'UTCGNO', # Manufacturers' New Orders: Capital Goods (NSA)
    'UTGPNO', # Manufacturers' New Orders: Turbines, Generators, and Other Power Transmission Equipment (NSA)
    ## Value of Manufacturers' New Orders for Consumer Goods
    'ACNGNO', # Value of Manufacturers' New Orders for Consumer Goods: Consumer Nondurable Goods Industries (DISCONTINUED)
    'UCNGNO', # Value of Manufacturers' New Orders for Consumer Goods: Consumer Nondurable Goods Industries (DISCONTINUED) (NSA)

    # Manufacturing > Inventory to Shipments (48)
    ## Manufacturers' Inventories to Shipments Ratios
    'A11SIS', # Manufacturers' Inventories to Shipments Ratios: Food Products
    'A12SIS', # Manufacturers' Inventories to Shipments Ratios: Beverage and Tobacco Products
    'A13SIS', # Manufacturers' Inventories to Shipments Ratios: Textile Mills
    'A14SIS', # Manufacturers' Inventories to Shipments Ratios: Textile Products
    'A15SIS', # Manufacturers' Inventories to Shipments Ratios: Apparel
    'A16SIS', # Manufacturers' Inventories to Shipments Ratios: Leather and Allied Products
    'A21SIS', # Manufacturers' Inventories to Shipments Ratios: Wood Products
    'A22SIS', # Manufacturers' Inventories to Shipments Ratios: Paper Products
    'A23SIS', # Manufacturers' Inventories to Shipments Ratios: Printing
    'A24SIS', # Manufacturers' Inventories to Shipments Ratios: Petroleum and Coal Products
    'A25SIS', # Manufacturers' Inventories to Shipments Ratios: Chemical Products
    'A26SIS', # Manufacturers' Inventories to Shipments Ratios: Plastics and Rubber Products
    'A27SIS', # Manufacturers' Inventories to Shipments Ratios: Nonmetallic Mineral Products
    'A31SIS', # Manufacturers' Inventories to Shipments Ratios: Primary Metals
    'A32SIS', # Manufacturers' Inventories to Shipments Ratios: Fabricated Metal Products
    'A33SIS', # Manufacturers' Inventories to Shipments Ratios: Machinery
    'A34SIS', # Manufacturers' Inventories to Shipments Ratios: Computers and Electronic Products
    'A35SIS', # Manufacturers' Inventories to Shipments Ratios: Electrical Equipment, Appliances and Components
    'A36SIS', # Manufacturers' Inventories to Shipments Ratios: Transportation Equipment
    'A37SIS', # Manufacturers' Inventories to Shipments Ratios: Furniture and Related Products
    'A39SIS', # Manufacturers' Inventories to Shipments Ratios: Miscellaneous Products
    'AMDMIS', # Manufacturers' Inventories to Shipments Ratios: Durable Goods
    'AMNMIS', # Manufacturers' Inventories to Shipments Ratios: Nondurable Goods
    'AMTMIS', # Manufacturers' Inventories to Shipments Ratios: Total Manufacturing
    'U11SIS', # Manufacturers' Inventories to Shipments Ratios: Food Products (NSA)
    'U12SIS', # Manufacturers' Inventories to Shipments Ratios: Beverage and Tobacco Products (NSA)
    'U13SIS', # Manufacturers' Inventories to Shipments Ratios: Textile Mills (NSA)
    'U14SIS', # Manufacturers' Inventories to Shipments Ratios: Textile Products (NSA)
    'U15SIS', # Manufacturers' Inventories to Shipments Ratios: Apparel (NSA)
    'U16SIS', # Manufacturers' Inventories to Shipments Ratios: Leather and Allied Products (NSA)
    'U21SIS', # Manufacturers' Inventories to Shipments Ratios: Wood Products (NSA)
    'U22SIS', # Manufacturers' Inventories to Shipments Ratios: Paper Products (NSA)
    'U23SIS', # Manufacturers' Inventories to Shipments Ratios: Printing (NSA)
    'U24SIS', # Manufacturers' Inventories to Shipments Ratios: Petroleum and Coal Products (NSA)
    'U25SIS', # Manufacturers' Inventories to Shipments Ratios: Chemical Products (NSA)
    'U26SIS', # Manufacturers' Inventories to Shipments Ratios: Plastics and Rubber Products (NSA)
    'U27SIS', # Manufacturers' Inventories to Shipments Ratios: Nonmetallic Mineral Products (NSA)
    'U31SIS', # Manufacturers' Inventories to Shipments Ratios: Primary Metals (NSA)
    'U32SIS', # Manufacturers' Inventories to Shipments Ratios: Fabricated Metal Products (NSA)
    'U33SIS', # Manufacturers' Inventories to Shipments Ratios: Machinery (NSA)
    'U34SIS', # Manufacturers' Inventories to Shipments Ratios: Computers and Electronic Products (NSA)
    'U35SIS', # Manufacturers' Inventories to Shipments Ratios: Electrical Equipment, Appliances and Components (NSA)
    'U36SIS', # Manufacturers' Inventories to Shipments Ratios: Transportation Equipment (NSA)
    'U37SIS', # Manufacturers' Inventories to Shipments Ratios: Furniture and Related Products (NSA)
    'U39SIS', # Manufacturers' Inventories to Shipments Ratios: Miscellaneous Products (NSA)
    'UMDMIS', # Manufacturers' Inventories to Shipments Ratios: Durable Goods (NSA)
    'UMNMIS', # Manufacturers' Inventories to Shipments Ratios: Nondurable Goods (NSA)
    'UMTMIS', # Manufacturers' Inventories to Shipments Ratios: Total Manufacturing (NSA)

    # Manufacturing > Unfilled Orders (148)
    ## Current Unfilled Orders - Federal Reserve District 3: Philadelphia
    'UOCDFNA066MNFRBPHI', # Current Unfilled Orders; Diffusion Index for Federal Reserve District 3: Philadelphia (NSA)
    'UOCDFSA066MSFRBPHI', # Current Unfilled Orders; Diffusion Index for Federal Reserve District 3: Philadelphia
    'UOCDNA156MNFRBPHI', # Current Unfilled Orders; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia (NSA)
    'UOCDSA156MSFRBPHI', # Current Unfilled Orders; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia
    'UOCINA156MNFRBPHI', # Current Unfilled Orders; Percent Reporting Increases for Federal Reserve District 3: Philadelphia (NSA)
    'UOCISA156MSFRBPHI', # Current Unfilled Orders; Percent Reporting Increases for Federal Reserve District 3: Philadelphia
    'UOCNNA156MNFRBPHI', # Current Unfilled Orders; Percent Reporting No Change for Federal Reserve District 3: Philadelphia (NSA)
    'UOCNSA156MSFRBPHI', # Current Unfilled Orders; Percent Reporting No Change for Federal Reserve District 3: Philadelphia
    ## Current Unfilled Orders - New York
    'UOCDINA066MNFRBNY', # Current Unfilled Orders; Diffusion Index for New York (NSA)
    'UOCDISA066MSFRBNY', # Current Unfilled Orders; Diffusion Index for New York
    'UOCDNA156MNFRBNY', # Current Unfilled Orders; Percent Reporting Decreases for New York (NSA)
    'UOCDSA156MSFRBNY', # Current Unfilled Orders; Percent Reporting Decreases for New York
    'UOCINA156MNFRBNY', # Current Unfilled Orders; Percent Reporting Increases for New York (NSA)
    'UOCISA156MSFRBNY', # Current Unfilled Orders; Percent Reporting Increases for New York
    'UOCNNA156MNFRBNY', # Current Unfilled Orders; Percent Reporting No Change for New York (NSA)
    'UOCNSA156MSFRBNY', # Current Unfilled Orders; Percent Reporting No Change for New York
    ## Current Unfilled Orders - Texas
    'UFILDSAMFRBDAL', # Current Unfilled Orders; Percentage Reporting Decreases for Texas
    'UFILDUAMFRBDAL', # Current Unfilled Orders; Percentage Reporting Decreases for Texas (NSA)
    'UFILISAMFRBDAL', # Current Unfilled Orders; Percentage Reporting Increases for Texas
    'UFILIUAMFRBDAL', # Current Unfilled Orders; Percentage Reporting Increases for Texas (NSA)
    'UFILNSAMFRBDAL', # Current Unfilled Orders; Percentage Reporting No Change for Texas
    'UFILNUAMFRBDAL', # Current Unfilled Orders; Percentage Reporting No Change for Texas (NSA)
    'UFILSAMFRBDAL', # Current Unfilled Orders; Diffusion Index for Texas
    'UFILUAMFRBDAL', # Current Unfilled Orders; Diffusion Index for Texas (NSA)
    ## Future Unfilled Orders - Federal Reserve District 3: Philadelphia
    'UOFDFNA066MNFRBPHI', # Future Unfilled Orders; Diffusion Index for Federal Reserve District 3: Philadelphia (NSA)
    'UOFDFSA066MSFRBPHI', # Future Unfilled Orders; Diffusion Index for Federal Reserve District 3: Philadelphia
    'UOFDNA156MNFRBPHI', # Future Unfilled Orders; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia (NSA)
    'UOFDSA156MSFRBPHI', # Future Unfilled Orders; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia
    'UOFINA156MNFRBPHI', # Future Unfilled Orders; Percent Reporting Increases for Federal Reserve District 3: Philadelphia (NSA)
    'UOFISA156MSFRBPHI', # Future Unfilled Orders; Percent Reporting Increases for Federal Reserve District 3: Philadelphia
    'UOFNNA156MNFRBPHI', # Future Unfilled Orders; Percent Reporting No Change for Federal Reserve District 3: Philadelphia (NSA)
    'UOFNSA156MSFRBPHI', # Future Unfilled Orders; Percent Reporting No Change for Federal Reserve District 3: Philadelphia
    ## Future Unfilled Orders - New York
    'UOFDINA066MNFRBNY', # Future Unfilled Orders; Diffusion Index for New York (NSA)
    'UOFDISA066MSFRBNY', # Future Unfilled Orders; Diffusion Index for New York
    'UOFDNA156MNFRBNY', # Future Unfilled Orders; Percent Expecting Decreases for New York (NSA)
    'UOFDSA156MSFRBNY', # Future Unfilled Orders; Percent Expecting Decreases for New York
    'UOFINA156MNFRBNY', # Future Unfilled Orders; Percent Expecting Increases for New York (NSA)
    'UOFISA156MSFRBNY', # Future Unfilled Orders; Percent Expecting Increases for New York
    'UOFNNA156MNFRBNY', # Future Unfilled Orders; Percent Expecting No Change for New York (NSA)
    'UOFNSA156MSFRBNY', # Future Unfilled Orders; Percent Expecting No Change for New York
    ## Future Unfilled Orders - Texas
    'FUFILDSAMFRBDAL', # Future Unfilled Orders; Percentage Reporting Decreases for Texas
    'FUFILDUAMFRBDAL', # Future Unfilled Orders; Percentage Reporting Decreases for Texas (NSA)
    'FUFILISAMFRBDAL', # Future Unfilled Orders; Percentage Reporting Increases for Texas
    'FUFILIUAMFRBDAL', # Future Unfilled Orders; Percentage Reporting Increases for Texas (NSA)
    'FUFILNSAMFRBDAL', # Future Unfilled Orders; Percentage Reporting No Change for Texas
    'FUFILNUAMFRBDAL', # Future Unfilled Orders; Percentage Reporting No Change for Texas (NSA)
    'FUFILSAMFRBDAL', # Future Unfilled Orders; Diffusion Index for Texas
    'FUFILUAMFRBDAL', # Future Unfilled Orders; Diffusion Index for Texas (NSA)
    ## Manufacturers' Unfilled Orders
    'A31AUO', # Manufacturers' Unfilled Orders: Iron and Steel Mills and Ferroalloy and Steel Product Manufacturing
    'A31CUO', # Manufacturers' Unfilled Orders: Ferrous Metal Foundries
    'A31SUO', # Manufacturers' Unfilled Orders: Primary Metals
    'A32SUO', # Manufacturers' Unfilled Orders: Fabricated Metal Products
    'A33CUO', # Manufacturers' Unfilled Orders: Construction Machinery Manufacturing
    'A33DUO', # Manufacturers' Unfilled Orders: Mining, Oil, and Gas Field Machinery Manufacturing
    'A33EUO', # Manufacturers' Unfilled Orders: Industrial Machinery Manufacturing
    'A33GUO', # Manufacturers' Unfilled Orders: Photographic Equipment Manufacturing
    'A33HUO', # Manufacturers' Unfilled Orders: Ventilation, Heating, Air-Conditioning, and Refrigeration Equipment Manufacturing
    'A33IUO', # Manufacturers' Unfilled Orders: Metalworking Machinery Manufacturing
    'A33MUO', # Manufacturers' Unfilled Orders: Material Handling Equipment Manufacturing
    'A33SUO', # Manufacturers' Unfilled Orders: Machinery
    'A34AUO', # Manufacturers' Unfilled Orders: Electronic Computer Manufacturing
    'A34DUO', # Manufacturers' Unfilled Orders: Communications Equipment, Nondefense
    'A34EUO', # Manufacturers' Unfilled Orders: Communications Equipment Manufacturing, Defense
    'A34HUO', # Manufacturers' Unfilled Orders: Other Electronic Component Manufacturing
    'A34IUO', # Manufacturers' Unfilled Orders: Search and Navigation Equipment, Nondefense
    'A34JUO', # Manufacturers' Unfilled Orders: Search and Navigation Equipment, Defense
    'A34KUO', # Manufacturers' Unfilled Orders: Electromedical, Measuring, and Control Instrument Manufacturing
    'A34SUO', # Manufacturers' Unfilled Orders: Computers and Electronic Products
    'A34XUO', # Manufacturers' Unfilled Orders: Communications Equipment
    'A35AUO', # Manufacturers' Unfilled Orders: Electric Lighting Equipment Manufacturing
    'A35BUO', # Manufacturers' Unfilled Orders: Household Appliance Manufacturing
    'A35CUO', # Manufacturers' Unfilled Orders: Electrical Equipment Manufacturing
    'A35SUO', # Manufacturers' Unfilled Orders: Electrical Equipment, Appliances and Components
    'A36SUO', # Manufacturers' Unfilled Orders: Transportation Equipment
    'A36ZUO', # Manufacturers' Unfilled Orders: Ships and Boats
    'A37SUO', # Manufacturers' Unfilled Orders: Furniture and Related Products
    'AANMUO', # Manufacturers' Unfilled Orders: Aluminum and Nonferrous Metal Products
    'ABTPUO', # Manufacturers' Unfilled Orders: Motor Vehicle Bodies, Trailers, and Parts
    'ACDGUO', # Manufacturers' Unfilled Orders: Consumer Durable Goods
    'ACMSUO', # Manufacturers' Unfilled Orders: Construction Materials and Supplies
    'ACOGUO', # Manufacturers' Unfilled Orders: Consumer Goods
    'ACRPUO', # Manufacturers' Unfilled Orders: Computers and Related Products
    'ADAPUO', # Manufacturers' Unfilled Orders: Defense Aircraft and Parts
    'ADEFUO', # Manufacturers' Unfilled Orders: Defense Capital Goods
    'ADXDUO', # Manufacturers' Unfilled Orders: Durable Goods Excluding Defense
    'ADXTUO', # Manufacturers' Unfilled Orders: Durable Goods Excluding Transportation
    'AITIUO', # Manufacturers' Unfilled Orders: Information Technology Industries
    'AMDMUO', # Manufacturers' Unfilled Orders: Durable Goods
    'AMTMUO', # Manufacturers' Unfilled Orders: Total Manufacturing
    'AMVPUO', # Manufacturers' Unfilled Orders: Motor Vehicles and Parts
    'AMXDUO', # Manufacturers' Unfilled Orders: Manufacturing Excluding Defense
    'AMXTUO', # Manufacturers' Unfilled Orders: Manufacturing Excluding Transportation
    'ANAPUO', # Manufacturers' Unfilled Orders: Nondefense Aircraft and Parts
    'ANDEUO', # Manufacturers' Unfilled Orders: Nondefense Capital Goods
    'ANXAUO', # Manufacturers' Unfilled Orders: Nondefense Capital Goods Excluding Aircraft
    'AODGUO', # Manufacturers' Unfilled Orders: All Other Durable Goods
    'ATCGUO', # Manufacturers' Unfilled Orders: Capital Goods
    'ATGPUO', # Manufacturers' Unfilled Orders: Turbines, Generators, and Other Power Transmission Equipment
    'U31AUO', # Manufacturers' Unfilled Orders: Iron and Steel Mills and Ferroalloy and Steel Product Manufacturing (NSA)
    'U31CUO', # Manufacturers' Unfilled Orders: Ferrous Metal Foundries (NSA)
    'U31SUO', # Manufacturers' Unfilled Orders: Primary Metals (NSA)
    'U32SUO', # Manufacturers' Unfilled Orders: Fabricated Metal Products (NSA)
    'U33CUO', # Manufacturers' Unfilled Orders: Construction Machinery Manufacturing (NSA)
    'U33DUO', # Manufacturers' Unfilled Orders: Mining, Oil, and Gas Field Machinery Manufacturing (NSA)
    'U33EUO', # Manufacturers' Unfilled Orders: Industrial Machinery Manufacturing (NSA)
    'U33GUO', # Manufacturers' Unfilled Orders: Photographic Equipment Manufacturing (NSA)
    'U33HUO', # Manufacturers' Unfilled Orders: Ventilation, Heating, Air-Conditioning, and Refrigeration Equipment Manufacturing (NSA)
    'U33IUO', # Manufacturers' Unfilled Orders: Metalworking Machinery Manufacturing (NSA)
    'U33MUO', # Manufacturers' Unfilled Orders: Material Handling Equipment Manufacturing (NSA)
    'U33SUO', # Manufacturers' Unfilled Orders: Machinery (NSA)
    'U34AUO', # Manufacturers' Unfilled Orders: Electronic Computer Manufacturing (NSA)
    'U34DUO', # Manufacturers' Unfilled Orders: Communications Equipment, Nondefense (NSA)
    'U34EUO', # Manufacturers' Unfilled Orders: Communications Equipment Manufacturing, Defense (NSA)
    'U34HUO', # Manufacturers' Unfilled Orders: Other Electronic Component Manufacturing (NSA)
    'U34IUO', # Manufacturers' Unfilled Orders: Search and Navigation Equipment, Nondefense (NSA)
    'U34JUO', # Manufacturers' Unfilled Orders: Search and Navigation Equipment, Defense (NSA)
    'U34KUO', # Manufacturers' Unfilled Orders: Electromedical, Measuring, and Control Instrument Manufacturing (NSA)
    'U34SUO', # Manufacturers' Unfilled Orders: Computers and Electronic Products (NSA)
    'U34XUO', # Manufacturers' Unfilled Orders: Communications Equipment (NSA)
    'U35AUO', # Manufacturers' Unfilled Orders: Electric Lighting Equipment Manufacturing (NSA)
    'U35BUO', # Manufacturers' Unfilled Orders: Household Appliance Manufacturing (NSA)
    'U35CUO', # Manufacturers' Unfilled Orders: Electrical Equipment Manufacturing (NSA)
    'U35SUO', # Manufacturers' Unfilled Orders: Electrical Equipment, Appliances and Components (NSA)
    'U36SUO', # Manufacturers' Unfilled Orders: Transportation Equipment (NSA)
    'U36ZUO', # Manufacturers' Unfilled Orders: Ships and Boats (NSA)
    'U37SUO', # Manufacturers' Unfilled Orders: Furniture and Related Products (NSA)
    'UANMUO', # Manufacturers' Unfilled Orders: Aluminum and Nonferrous Metal Products (NSA)
    'UBTPUO', # Manufacturers' Unfilled Orders: Motor Vehicle Bodies, Trailers, and Parts (NSA)
    'UCDGUO', # Manufacturers' Unfilled Orders: Consumer Durable Goods (NSA)
    'UCMSUO', # Manufacturers' Unfilled Orders: Construction Materials and Supplies (NSA)
    'UCOGUO', # Manufacturers' Unfilled Orders: Consumer Goods (NSA)
    'UCRPUO', # Manufacturers' Unfilled Orders: Computers and Related Products (NSA)
    'UDAPUO', # Manufacturers' Unfilled Orders: Defense Aircraft and Parts (NSA)
    'UDEFUO', # Manufacturers' Unfilled Orders: Defense Capital Goods (NSA)
    'UDXDUO', # Manufacturers' Unfilled Orders: Durable Goods Excluding Defense (NSA)
    'UDXTUO', # Manufacturers' Unfilled Orders: Durable Goods Excluding Transportation (NSA)
    'UITIUO', # Manufacturers' Unfilled Orders: Information Technology Industries (NSA)
    'UMDMUO', # Manufacturers' Unfilled Orders: Durable Goods (NSA)
    'UMTMUO', # Manufacturers' Unfilled Orders: Total Manufacturing (NSA)
    'UMVPUO', # Manufacturers' Unfilled Orders: Motor Vehicles and Parts (NSA)
    'UMXDUO', # Manufacturers' Unfilled Orders: Manufacturing Excluding Defense (NSA)
    'UMXTUO', # Manufacturers' Unfilled Orders: Manufacturing Excluding Transportation (NSA)
    'UNAPUO', # Manufacturers' Unfilled Orders: Nondefense Aircraft and Parts (NSA)
    'UNDEUO', # Manufacturers' Unfilled Orders: Nondefense Capital Goods (NSA)
    'UNXAUO', # Manufacturers' Unfilled Orders: Nondefense Capital Goods Excluding Aircraft (NSA)
    'UODGUO', # Manufacturers' Unfilled Orders: All Other Durable Goods (NSA)
    'UTCGUO', # Manufacturers' Unfilled Orders: Capital Goods (NSA)
    'UTGPUO', # Manufacturers' Unfilled Orders: Turbines, Generators, and Other Power Transmission Equipment (NSA)

    # Manufacturing > Unfilled Orders to Shipments (18)
    ## Manufacturers' Unfilled Orders to Shipments Ratios
    'A31SUS', # Manufacturers' Unfilled Orders to Shipments Ratios: Primary Metals
    'A32SUS', # Manufacturers' Unfilled Orders to Shipments Ratios: Fabricated Metal Products
    'A33SUS', # Manufacturers' Unfilled Orders to Shipments Ratios: Machinery
    'A34SUS', # Manufacturers' Unfilled Orders to Shipments Ratios: Computers and Electronic Products
    'A35SUS', # Manufacturers' Unfilled Orders to Shipments Ratios: Electrical Equipment, Appliances and Components
    'A36SUS', # Manufacturers' Unfilled Orders to Shipments Ratios: Transportation Equipment
    'A37SUS', # Manufacturers' Unfilled Orders to Shipments Ratios: Furniture and Related Products
    'AMDMUS', # Manufacturers' Unfilled Orders to Shipments Ratios: Durable Goods
    'AMTMUS', # Manufacturers' Unfilled Orders to Shipments Ratios: Total Manufacturing
    'U31SUS', # Manufacturers' Unfilled Orders to Shipments Ratios: Primary Metals (NSA)
    'U32SUS', # Manufacturers' Unfilled Orders to Shipments Ratios: Fabricated Metal Products (NSA)
    'U33SUS', # Manufacturers' Unfilled Orders to Shipments Ratios: Machinery (NSA)
    'U34SUS', # Manufacturers' Unfilled Orders to Shipments Ratios: Computers and Electronic Products (NSA)
    'U35SUS', # Manufacturers' Unfilled Orders to Shipments Ratios: Electrical Equipment, Appliances and Components (NSA)
    'U36SUS', # Manufacturers' Unfilled Orders to Shipments Ratios: Transportation Equipment (NSA)
    'U37SUS', # Manufacturers' Unfilled Orders to Shipments Ratios: Furniture and Related Products (NSA)
    'UMDMUS', # Manufacturers' Unfilled Orders to Shipments Ratios: Durable Goods (NSA)
    'UMTMUS', # Manufacturers' Unfilled Orders to Shipments Ratios: Total Manufacturing (NSA)

    # Manufacturing > Shipments (254)
    ## Current Delivery Time - Federal Reserve District 3: Philadelphia
    'DTCDFNA066MNFRBPHI', # Current Delivery Time; Diffusion Index for Federal Reserve District 3: Philadelphia (NSA)
    'DTCDFSA066MSFRBPHI', # Current Delivery Time; Diffusion Index for Federal Reserve District 3: Philadelphia
    'DTCDNA156MNFRBPHI', # Current Delivery Time; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia (NSA)
    'DTCDSA156MSFRBPHI', # Current Delivery Time; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia
    'DTCINA156MNFRBPHI', # Current Delivery Time; Percent Reporting Increases for Federal Reserve District 3: Philadelphia (NSA)
    'DTCISA156MSFRBPHI', # Current Delivery Time; Percent Reporting Increases for Federal Reserve District 3: Philadelphia
    'DTCNNA156MNFRBPHI', # Current Delivery Time; Percent Reporting No Change for Federal Reserve District 3: Philadelphia (NSA)
    'DTCNSA156MSFRBPHI', # Current Delivery Time; Percent Reporting No Change for Federal Reserve District 3: Philadelphia
    ## Current Delivery Time - Texas
    'DTMDSAMFRBDAL', # Current Delivery Time; Percentage Reporting Decreases for Texas
    'DTMDUAMFRBDAL', # Current Delivery Time; Percentage Reporting Decreases for Texas (NSA)
    'DTMISAMFRBDAL', # Current Delivery Time; Percentage Reporting Increases for Texas
    'DTMIUAMFRBDAL', # Current Delivery Time; Percentage Reporting Increases for Texas (NSA)
    'DTMNSAMFRBDAL', # Current Delivery Time; Percentage Reporting No Change for Texas
    'DTMNUAMFRBDAL', # Current Delivery Time; Percentage Reporting No Change for Texas (NSA)
    'DTMSAMFRBDAL', # Current Delivery Time; Diffusion Index for Texas
    'DTMUAMFRBDAL', # Current Delivery Time; Diffusion Index for Texas (NSA)
    ## Current Shipments - Federal Reserve District 3: Philadelphia
    'SHCDFNA066MNFRBPHI', # Current Shipments; Diffusion Index for Federal Reserve District 3: Philadelphia (NSA)
    'SHCDFSA066MSFRBPHI', # Current Shipments; Diffusion Index for Federal Reserve District 3: Philadelphia
    'SHCDNA156MNFRBPHI', # Current Shipments; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia (NSA)
    'SHCDSA156MSFRBPHI', # Current Shipments; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia
    'SHCINA156MNFRBPHI', # Current Shipments; Percent Reporting Increases for Federal Reserve District 3: Philadelphia (NSA)
    'SHCISA156MSFRBPHI', # Current Shipments; Percent Reporting Increases for Federal Reserve District 3: Philadelphia
    'SHCNNA156MNFRBPHI', # Current Shipments; Percent Reporting No Change for Federal Reserve District 3: Philadelphia (NSA)
    'SHCNSA156MSFRBPHI', # Current Shipments; Percent Reporting No Change for Federal Reserve District 3: Philadelphia
    ## Current Shipments - New York
    'SHCDINA066MNFRBNY', # Current Shipments; Diffusion Index for New York (NSA)
    'SHCDISA066MSFRBNY', # Current Shipments; Diffusion Index for New York
    'SHCDNA156MNFRBNY', # Current Shipments; Percent Reporting Decreases for New York (NSA)
    'SHCDSA156MSFRBNY', # Current Shipments; Percent Reporting Decreases for New York
    'SHCINA156MNFRBNY', # Current Shipments; Percent Reporting Increases for New York (NSA)
    'SHCISA156MSFRBNY', # Current Shipments; Percent Reporting Increases for New York
    'SHCNNA156MNFRBNY', # Current Shipments; Percent Reporting No Change for New York (NSA)
    'SHCNSA156MSFRBNY', # Current Shipments; Percent Reporting No Change for New York
    ## Current Shipments - Texas
    'VSHPDSAMFRBDAL', # Current Shipments; Percentage Reporting Decreases for Texas
    'VSHPDUAMFRBDAL', # Current Shipments; Percentage Reporting Decreases for Texas (NSA)
    'VSHPISAMFRBDAL', # Current Shipments; Percentage Reporting Increases for Texas
    'VSHPIUAMFRBDAL', # Current Shipments; Percentage Reporting Increases for Texas (NSA)
    'VSHPNSAMFRBDAL', # Current Shipments; Percentage Reporting No Change for Texas
    'VSHPNUAMFRBDAL', # Current Shipments; Percentage Reporting No Change for Texas (NSA)
    'VSHPSAMFRBDAL', # Current Shipments; Diffusion Index for Texas
    'VSHPUAMFRBDAL', # Current Shipments; Diffusion Index for Texas (NSA)
    ## Future Delivery Time - Federal Reserve District 3: Philadelphia
    'DTFDFNA066MNFRBPHI', # Future Delivery Time; Diffusion Index for Federal Reserve District 3: Philadelphia (NSA)
    'DTFDFSA066MSFRBPHI', # Future Delivery Time; Diffusion Index for Federal Reserve District 3: Philadelphia
    'DTFDNA156MNFRBPHI', # Future Delivery Time; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia (NSA)
    'DTFDSA156MSFRBPHI', # Future Delivery Time; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia
    'DTFINA156MNFRBPHI', # Future Delivery Time; Percent Reporting Increases for Federal Reserve District 3: Philadelphia (NSA)
    'DTFISA156MSFRBPHI', # Future Delivery Time; Percent Reporting Increases for Federal Reserve District 3: Philadelphia
    'DTFNNA156MNFRBPHI', # Future Delivery Time; Percent Reporting No Change for Federal Reserve District 3: Philadelphia (NSA)
    'DTFNSA156MSFRBPHI', # Future Delivery Time; Percent Reporting No Change for Federal Reserve District 3: Philadelphia
    ## Future Delivery Time - Texas
    'FDTMDSAMFRBDAL', # Future Delivery Time; Percentage Reporting Decreases for Texas
    'FDTMDUAMFRBDAL', # Future Delivery Time; Percentage Reporting Decreases for Texas (NSA)
    'FDTMISAMFRBDAL', # Future Delivery Time; Percentage Reporting Increases for Texas
    'FDTMIUAMFRBDAL', # Future Delivery Time; Percentage Reporting Increases for Texas (NSA)
    'FDTMNSAMFRBDAL', # Future Delivery Time; Percentage Reporting No Change for Texas
    'FDTMNUAMFRBDAL', # Future Delivery Time; Percentage Reporting No Change for Texas (NSA)
    'FDTMSAMFRBDAL', # Future Delivery Time; Diffusion Index for Texas
    'FDTMUAMFRBDAL', # Future Delivery Time; Diffusion Index for Texas (NSA)
    ## Future Shipments - Federal Reserve District 3: Philadelphia
    'SHFDFNA066MNFRBPHI', # Future Shipments; Diffusion Index for Federal Reserve District 3: Philadelphia (NSA)
    'SHFDFSA066MSFRBPHI', # Future Shipments; Diffusion Index for Federal Reserve District 3: Philadelphia
    'SHFDNA156MNFRBPHI', # Future Shipments; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia (NSA)
    'SHFDSA156MSFRBPHI', # Future Shipments; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia
    'SHFINA156MNFRBPHI', # Future Shipments; Percent Reporting Increases for Federal Reserve District 3: Philadelphia (NSA)
    'SHFISA156MSFRBPHI', # Future Shipments; Percent Reporting Increases for Federal Reserve District 3: Philadelphia
    'SHFNNA156MNFRBPHI', # Future Shipments; Percent Reporting No Change for Federal Reserve District 3: Philadelphia (NSA)
    'SHFNSA156MSFRBPHI', # Future Shipments; Percent Reporting No Change for Federal Reserve District 3: Philadelphia
    ## Future Shipments - New York
    'SHFDINA066MNFRBNY', # Future Shipments; Diffusion Index for New York (NSA)
    'SHFDISA066MSFRBNY', # Future Shipments; Diffusion Index for New York
    'SHFDNA156MNFRBNY', # Future Shipments; Percent Expecting Decreases for New York (NSA)
    'SHFDSA156MSFRBNY', # Future Shipments; Percent Expecting Decreases for New York
    'SHFINA156MNFRBNY', # Future Shipments; Percent Expecting Increases for New York (NSA)
    'SHFISA156MSFRBNY', # Future Shipments; Percent Expecting Increases for New York
    'SHFNNA156MNFRBNY', # Future Shipments; Percent Expecting No Change for New York (NSA)
    'SHFNSA156MSFRBNY', # Future Shipments; Percent Expecting No Change for New York
    ## Future Shipments - Texas
    'FVSHPDSAMFRBDAL', # Future Shipments; Percentage Reporting Decreases for Texas
    'FVSHPDUAMFRBDAL', # Future Shipments; Percentage Reporting Decreases for Texas (NSA)
    'FVSHPISAMFRBDAL', # Future Shipments; Percentage Reporting Increases for Texas
    'FVSHPIUAMFRBDAL', # Future Shipments; Percentage Reporting Increases for Texas (NSA)
    'FVSHPNSAMFRBDAL', # Future Shipments; Percentage Reporting No Change for Texas
    'FVSHPNUAMFRBDAL', # Future Shipments; Percentage Reporting No Change for Texas (NSA)
    'FVSHPSAMFRBDAL', # Future Shipments; Diffusion Index for Texas
    'FVSHPUAMFRBDAL', # Future Shipments; Diffusion Index for Texas (NSA)
    ## Manufacturers' Value of Shipments
    'A11AVS', # Manufacturers' Value of Shipments: Grain and Oilseed Milling
    'A11BVS', # Manufacturers' Value of Shipments: Dairy Product Manufacturing
    'A11CVS', # Manufacturers' Value of Shipments: Meat, Poultry, and Seafood Product Processing
    'A11SVS', # Manufacturers' Value of Shipments: Food Products
    'A12AVS', # Manufacturers' Value of Shipments: Beverage Manufacturing
    'A12BVS', # Manufacturers' Value of Shipments: Tobacco Manufacturing
    'A12SVS', # Manufacturers' Value of Shipments: Beverage and Tobacco Products
    'A13SVS', # Manufacturers' Value of Shipments: Textile Mills
    'A14SVS', # Manufacturers' Value of Shipments: Textile Products
    'A15SVS', # Manufacturers' Value of Shipments: Apparel
    'A16SVS', # Manufacturers' Value of Shipments: Leather and Allied Products
    'A21SVS', # Manufacturers' Value of Shipments: Wood Products
    'A22AVS', # Manufacturers' Value of Shipments: Pulp, Paper, and Paperboard Mills
    'A22BVS', # Manufacturers' Value of Shipments: Paperboard Container Manufacturing
    'A22SVS', # Manufacturers' Value of Shipments: Paper Products
    'A23SVS', # Manufacturers' Value of Shipments: Printing
    'A24AVS', # Manufacturers' Value of Shipments: Petroleum Refineries
    'A24SVS', # Manufacturers' Value of Shipments: Petroleum and Coal Products
    'A25AVS', # Manufacturers' Value of Shipments: Pesticide, Fertilizer, and Other Agricultural Chemical Manufacturing
    'A25BVS', # Manufacturers' Value of Shipments: Pharmaceutical and Medicine Manufacturing
    'A25CVS', # Manufacturers' Value of Shipments: Paint, Coating, and Adhesive, Manufacturing
    'A25SVS', # Manufacturers' Value of Shipments: Chemical Products
    'A26SVS', # Manufacturers' Value of Shipments: Plastics and Rubber Products
    'A27SVS', # Manufacturers' Value of Shipments: Nonmetallic Mineral Products
    'A31AVS', # Manufacturers' Value of Shipments: Iron and Steel Mills and Ferroalloy and Steel Product Manufacturing
    'A31CVS', # Manufacturers' Value of Shipments: Ferrous Metal Foundries
    'A31SVS', # Manufacturers' Value of Shipments: Primary Metals
    'A32SVS', # Manufacturers' Value of Shipments: Fabricated Metal Products
    'A33AVS', # Manufacturers' Value of Shipments: Farm Machinery and Equipment Manufacturing
    'A33CVS', # Manufacturers' Value of Shipments: Construction Machinery Manufacturing
    'A33DVS', # Manufacturers' Value of Shipments: Mining, Oil, and Gas Field Machinery Manufacturing
    'A33EVS', # Manufacturers' Value of Shipments: Industrial Machinery Manufacturing
    'A33GVS', # Manufacturers' Value of Shipments: Photographic Equipment Manufacturing
    'A33HVS', # Manufacturers' Value of Shipments: Ventilation, Heating, Air-Conditioning, and Refrigeration Equipment Manufacturing
    'A33IVS', # Manufacturers' Value of Shipments: Metalworking Machinery Manufacturing
    'A33MVS', # Manufacturers' Value of Shipments: Material Handling Equipment Manufacturing
    'A33SVS', # Manufacturers' Value of Shipments: Machinery
    'A34AVS', # Manufacturers' Value of Shipments: Electronic Computer Manufacturing
    'A34BVS', # Manufacturers' Value of Shipments: Computer Storage Device Manufacturing
    'A34CVS', # Manufacturers' Value of Shipments: Other Computer Peripheral Equipment Manufacturing
    'A34DVS', # Manufacturers' Value of Shipments: Communications Equipment, Nondefense
    'A34EVS', # Manufacturers' Value of Shipments: Communications Equipment Manufacturing, Defense
    'A34FVS', # Manufacturers' Value of Shipments: Audio and Video Equipment
    'A34HVS', # Manufacturers' Value of Shipments: Other Electronic Component Manufacturing
    'A34IVS', # Manufacturers' Value of Shipments: Search and Navigation Equipment, Nondefense
    'A34JVS', # Manufacturers' Value of Shipments: Search and Navigation Equipment, Defense
    'A34KVS', # Manufacturers' Value of Shipments: Electromedical, Measuring, and Control Instrument Manufacturing
    'A34SVS', # Manufacturers' Value of Shipments: Computers and Electronic Products
    'A34XVS', # Manufacturers' Value of Shipments: Communications Equipment
    'A35AVS', # Manufacturers' Value of Shipments: Electric Lighting Equipment Manufacturing
    'A35BVS', # Manufacturers' Value of Shipments: Household Appliance Manufacturing
    'A35CVS', # Manufacturers' Value of Shipments: Electrical Equipment Manufacturing
    'A35DVS', # Manufacturers' Value of Shipments: Battery Manufacturing
    'A35SVS', # Manufacturers' Value of Shipments: Electrical Equipment, Appliances and Components
    'A36AVS', # Manufacturers' Value of Shipments: Automobile Manufacturing
    'A36BVS', # Manufacturers' Value of Shipments: Light Truck and Utility Vehicle Manufacturing
    'A36CVS', # Manufacturers' Value of Shipments: Heavy Duty Truck Manufacturing
    'A36SVS', # Manufacturers' Value of Shipments: Transportation Equipment
    'A36ZVS', # Manufacturers' Value of Shipments: Ships and Boats
    'A37SVS', # Manufacturers' Value of Shipments: Furniture and Related Products
    'A39SVS', # Manufacturers' Value of Shipments: Miscellaneous Products
    'AANMVS', # Manufacturers' Value of Shipments: Aluminum and Nonferrous Metal Products
    'ABTPVS', # Manufacturers' Value of Shipments: Motor Vehicle Bodies, Trailers, and Parts
    'ACDGVS', # Manufacturers' Value of Shipments: Consumer Durable Goods
    'ACMSVS', # Manufacturers' Value of Shipments: Construction Materials and Supplies
    'ACNGVS', # Manufacturers' Value of Shipments: Consumer Nondurable Goods
    'ACOGVS', # Manufacturers' Value of Shipments: Consumer Goods
    'ACRPVS', # Manufacturers' Value of Shipments: Computers and Related Products
    'ADAPVS', # Manufacturers' Value of Shipments: Defense Aircraft and Parts
    'ADEFVS', # Manufacturers' Value of Shipments: Defense Capital Goods
    'ADXDVS', # Manufacturers' Value of Shipments: Durable Goods Excluding Defense
    'ADXTVS', # Manufacturers' Value of Shipments: Durable Goods Excluding Transportation
    'AITIVS', # Manufacturers' Value of Shipments: Information Technology Industries
    'AMDMVS', # Manufacturers' Value of Shipments: Durable Goods
    'AMNMVS', # Manufacturers' Value of Shipments: Nondurable Goods
    'AMTMVS', # Manufacturers' Value of Shipments: Total Manufacturing
    'AMTUVS', # Manufacturers' Value of Shipments: Manufacturing with Unfilled Orders
    'AMVPVS', # Manufacturers' Value of Shipments: Motor Vehicles and Parts
    'AMXDVS', # Manufacturers' Value of Shipments: Manufacturing Excluding Defense
    'AMXTVS', # Manufacturers' Value of Shipments: Manufacturing Excluding Transportation
    'ANAPVS', # Manufacturers' Value of Shipments: Nondefense Aircraft and Parts
    'ANDEVS', # Manufacturers' Value of Shipments: Nondefense Capital Goods
    'ANXAVS', # Manufacturers' Value of Shipments: Nondefense Capital Goods Excluding Aircraft
    'AODGVS', # Manufacturers' Value of Shipments: All Other Durable Goods
    'ATCGVS', # Manufacturers' Value of Shipments: Capital Goods
    'ATGPVS', # Manufacturers' Value of Shipments: Turbines, Generators, and Other Power Transmission Equipment
    'U11AVS', # Manufacturers' Value of Shipments: Grain and Oilseed Milling (NSA)
    'U11BVS', # Manufacturers' Value of Shipments: Dairy Product Manufacturing (NSA)
    'U11CVS', # Manufacturers' Value of Shipments: Meat, Poultry, and Seafood Product Processing (NSA)
    'U11SVS', # Manufacturers' Value of Shipments: Food Products (NSA)
    'U12AVS', # Manufacturers' Value of Shipments: Beverage Manufacturing (NSA)
    'U12BVS', # Manufacturers' Value of Shipments: Tobacco Manufacturing (NSA)
    'U12SVS', # Manufacturers' Value of Shipments: Beverage and Tobacco Products (NSA)
    'U13SVS', # Manufacturers' Value of Shipments: Textile Mills (NSA)
    'U14SVS', # Manufacturers' Value of Shipments: Textile Products (NSA)
    'U15SVS', # Manufacturers' Value of Shipments: Apparel (NSA)
    'U16SVS', # Manufacturers' Value of Shipments: Leather and Allied Products (NSA)
    'U21SVS', # Manufacturers' Value of Shipments: Wood Products (NSA)
    'U22AVS', # Manufacturers' Value of Shipments: Pulp, Paper, and Paperboard Mills (NSA)
    'U22BVS', # Manufacturers' Value of Shipments: Paperboard Container Manufacturing (NSA)
    'U22SVS', # Manufacturers' Value of Shipments: Paper Products (NSA)
    'U23SVS', # Manufacturers' Value of Shipments: Printing (NSA)
    'U24AVS', # Manufacturers' Value of Shipments: Petroleum Refineries (NSA)
    'U24SVS', # Manufacturers' Value of Shipments: Petroleum and Coal Products (NSA)
    'U25AVS', # Manufacturers' Value of Shipments: Pesticide, Fertilizer, and Other Agricultural Chemical Manufacturing (NSA)
    'U25BVS', # Manufacturers' Value of Shipments: Pharmaceutical and Medicine Manufacturing (NSA)
    'U25CVS', # Manufacturers' Value of Shipments: Paint, Coating, and Adhesive, Manufacturing (NSA)
    'U25SVS', # Manufacturers' Value of Shipments: Chemical Products (NSA)
    'U26SVS', # Manufacturers' Value of Shipments: Plastics and Rubber Products (NSA)
    'U27SVS', # Manufacturers' Value of Shipments: Nonmetallic Mineral Products (NSA)
    'U31AVS', # Manufacturers' Value of Shipments: Iron and Steel Mills and Ferroalloy and Steel Product Manufacturing (NSA)
    'U31CVS', # Manufacturers' Value of Shipments: Ferrous Metal Foundries (NSA)
    'U31SVS', # Manufacturers' Value of Shipments: Primary Metals (NSA)
    'U32SVS', # Manufacturers' Value of Shipments: Fabricated Metal Products (NSA)
    'U33AVS', # Manufacturers' Value of Shipments: Farm Machinery and Equipment Manufacturing (NSA)
    'U33CVS', # Manufacturers' Value of Shipments: Construction Machinery Manufacturing (NSA)
    'U33DVS', # Manufacturers' Value of Shipments: Mining, Oil, and Gas Field Machinery Manufacturing (NSA)
    'U33EVS', # Manufacturers' Value of Shipments: Industrial Machinery Manufacturing (NSA)
    'U33GVS', # Manufacturers' Value of Shipments: Photographic Equipment Manufacturing (NSA)
    'U33HVS', # Manufacturers' Value of Shipments: Ventilation, Heating, Air-Conditioning, and Refrigeration Equipment Manufacturing (NSA)
    'U33IVS', # Manufacturers' Value of Shipments: Metalworking Machinery Manufacturing (NSA)
    'U33MVS', # Manufacturers' Value of Shipments: Material Handling Equipment Manufacturing (NSA)
    'U33SVS', # Manufacturers' Value of Shipments: Machinery (NSA)
    'U34AVS', # Manufacturers' Value of Shipments: Electronic Computer Manufacturing (NSA)
    'U34BVS', # Manufacturers' Value of Shipments: Computer Storage Device Manufacturing (NSA)
    'U34CVS', # Manufacturers' Value of Shipments: Other Computer Peripheral Equipment Manufacturing (NSA)
    'U34DVS', # Manufacturers' Value of Shipments: Communications Equipment, Nondefense (NSA)
    'U34EVS', # Manufacturers' Value of Shipments: Communications Equipment Manufacturing, Defense (NSA)
    'U34FVS', # Manufacturers' Value of Shipments: Audio and Video Equipment (NSA)
    'U34HVS', # Manufacturers' Value of Shipments: Other Electronic Component Manufacturing (NSA)
    'U34IVS', # Manufacturers' Value of Shipments: Search and Navigation Equipment, Nondefense (NSA)
    'U34JVS', # Manufacturers' Value of Shipments: Search and Navigation Equipment, Defense (NSA)
    'U34KVS', # Manufacturers' Value of Shipments: Electromedical, Measuring, and Control Instrument Manufacturing (NSA)
    'U34SVS', # Manufacturers' Value of Shipments: Computers and Electronic Products (NSA)
    'U34XVS', # Manufacturers' Value of Shipments: Communications Equipment (NSA)
    'U35AVS', # Manufacturers' Value of Shipments: Electric Lighting Equipment Manufacturing (NSA)
    'U35BVS', # Manufacturers' Value of Shipments: Household Appliance Manufacturing (NSA)
    'U35CVS', # Manufacturers' Value of Shipments: Electrical Equipment Manufacturing (NSA)
    'U35DVS', # Manufacturers' Value of Shipments: Battery Manufacturing (NSA)
    'U35SVS', # Manufacturers' Value of Shipments: Electrical Equipment, Appliances and Components (NSA)
    'U36AVS', # Manufacturers' Value of Shipments: Automobile Manufacturing (NSA)
    'U36BVS', # Manufacturers' Value of Shipments: Light Truck and Utility Vehicle Manufacturing (NSA)
    'U36CVS', # Manufacturers' Value of Shipments: Heavy Duty Truck Manufacturing (NSA)
    'U36SVS', # Manufacturers' Value of Shipments: Transportation Equipment (NSA)
    'U36ZVS', # Manufacturers' Value of Shipments: Ships and Boats (NSA)
    'U37SVS', # Manufacturers' Value of Shipments: Furniture and Related Products (NSA)
    'U39SVS', # Manufacturers' Value of Shipments: Miscellaneous Products (NSA)
    'UANMVS', # Manufacturers' Value of Shipments: Aluminum and Nonferrous Metal Products (NSA)
    'UBTPVS', # Manufacturers' Value of Shipments: Motor Vehicle Bodies, Trailers, and Parts (NSA)
    'UCDGVS', # Manufacturers' Value of Shipments: Consumer Durable Goods (NSA)
    'UCMSVS', # Manufacturers' Value of Shipments: Construction Materials and Supplies (NSA)
    'UCNGVS', # Manufacturers' Value of Shipments: Consumer Nondurable Goods (NSA)
    'UCOGVS', # Manufacturers' Value of Shipments: Consumer Goods (NSA)
    'UCRPVS', # Manufacturers' Value of Shipments: Computers and Related Products (NSA)
    'UDAPVS', # Manufacturers' Value of Shipments: Defense Aircraft and Parts (NSA)
    'UDEFVS', # Manufacturers' Value of Shipments: Defense Capital Goods (NSA)
    'UDXDVS', # Manufacturers' Value of Shipments: Durable Goods Excluding Defense (NSA)
    'UDXTVS', # Manufacturers' Value of Shipments: Durable Goods Excluding Transportation (NSA)
    'UITIVS', # Manufacturers' Value of Shipments: Information Technology Industries (NSA)
    'UMDMVS', # Manufacturers' Value of Shipments: Durable Goods (NSA)
    'UMNMVS', # Manufacturers' Value of Shipments: Nondurable Goods (NSA)
    'UMTMVS', # Manufacturers' Value of Shipments: Total Manufacturing (NSA)
    'UMTUVS', # Manufacturers' Value of Shipments: Manufacturing with Unfilled Orders (NSA)
    'UMVPVS', # Manufacturers' Value of Shipments: Motor Vehicles and Parts (NSA)
    'UMXDVS', # Manufacturers' Value of Shipments: Manufacturing Excluding Defense (NSA)
    'UMXTVS', # Manufacturers' Value of Shipments: Manufacturing Excluding Transportation (NSA)
    'UNAPVS', # Manufacturers' Value of Shipments: Nondefense Aircraft and Parts (NSA)
    'UNDEVS', # Manufacturers' Value of Shipments: Nondefense Capital Goods (NSA)
    'UNXAVS', # Manufacturers' Value of Shipments: Nondefense Capital Goods Excluding Aircraft (NSA)
    'UODGVS', # Manufacturers' Value of Shipments: All Other Durable Goods (NSA)
    'UTCGVS', # Manufacturers' Value of Shipments: Capital Goods (NSA)
    'UTGPVS', # Manufacturers' Value of Shipments: Turbines, Generators, and Other Power Transmission Equipment (NSA)
    ## Value of Manufacturers' Shipments for Durable Goods Industries
    'A34GVS', # Value of Manufacturers' Shipments for Durable Goods Industries: Computers and Electronic Products: Semiconductors and Related Devices (DISCONTINUED)
    'U34GVS', # Value of Manufacturers' Shipments for Durable Goods Industries: Computers and Electronic Products: Semiconductors and Related Devices (DISCONTINUED) (NSA)

    # Manufacturing > 직속 - 지역 연준 제조업 설문
    ## FRB - New York District
    ### Current Prices Paid
    'PPCDINA066MNFRBNY', # Current Prices Paid; Diffusion Index for FRB - New York District (NSA)
    'PPCDNA156MNFRBNY', # Current Prices Paid; Percent Reporting Decreases for FRB - New York District (NSA)
    'PPCINA156MNFRBNY', # Current Prices Paid; Percent Reporting Increases for FRB - New York District (NSA)
    'PPCNNA156MNFRBNY', # Current Prices Paid; Percent Reporting No Change for FRB - New York District (NSA)
    ### Current Prices Received
    'PRCDINA066MNFRBNY', # Current Prices Received; Diffusion Index for FRB - New York District (NSA)
    'PRCDNA156MNFRBNY', # Current Prices Received; Percent Reporting Decreases for FRB - New York District (NSA)
    'PRCINA156MNFRBNY', # Current Prices Received; Percent Reporting Increases for FRB - New York District (NSA)
    'PRCNNA156MNFRBNY', # Current Prices Received; Percent Reporting No Change for FRB - New York District (NSA)
    ### Future Prices Paid
    'PPFDINA066MNFRBNY', # Future Prices Paid; Diffusion Index for FRB - New York District (NSA)
    'PPFDNA156MNFRBNY', # Future Prices Paid; Percent Expecting Decreases for FRB - New York District (NSA)
    'PPFINA156MNFRBNY', # Future Prices Paid; Percent Expecting Increases for FRB - New York District (NSA)
    'PPFNNA156MNFRBNY', # Future Prices Paid; Percent Expecting No Change for FRB - New York District (NSA)
    ### Future Prices Received
    'PRFDINA066MNFRBNY', # Future Prices Received; Diffusion Index for FRB - New York District (NSA)
    'PRFDNA156MNFRBNY', # Future Prices Received; Percent Expecting Decreases for FRB - New York District (NSA)
    'PRFINA156MNFRBNY', # Future Prices Received; Percent Expecting Increases for FRB - New York District (NSA)
    'PRFNNA156MNFRBNY', # Future Prices Received; Percent Expecting No Change for FRB - New York District (NSA)
    ## Federal Reserve District 3: Philadelphia
    ### Current Employment
    'NECDFNA066MNFRBPHI', # Current Employment; Diffusion Index for Federal Reserve District 3: Philadelphia (NSA)
    'NECDFSA066MSFRBPHI', # Current Employment; Diffusion Index for Federal Reserve District 3: Philadelphia
    'NECDNA156MNFRBPHI', # Current Employment; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia (NSA)
    'NECDSA156MSFRBPHI', # Current Employment; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia
    'NECINA156MNFRBPHI', # Current Employment; Percent Reporting Increases for Federal Reserve District 3: Philadelphia (NSA)
    'NECISA156MSFRBPHI', # Current Employment; Percent Reporting Increases for Federal Reserve District 3: Philadelphia
    'NECNNA156MNFRBPHI', # Current Employment; Percent Reporting No Change for Federal Reserve District 3: Philadelphia (NSA)
    'NECNSA156MSFRBPHI', # Current Employment; Percent Reporting No Change for Federal Reserve District 3: Philadelphia
    ### Current General Activity
    'GACDFNA066MNFRBPHI', # Current General Activity; Diffusion Index for Federal Reserve District 3: Philadelphia (NSA)
    'GACDFSA066MSFRBPHI', # Current General Activity; Diffusion Index for Federal Reserve District 3: Philadelphia
    'GACDNA156MNFRBPHI', # Current General Activity; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia (NSA)
    'GACDSA156MSFRBPHI', # Current General Activity; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia
    'GACINA156MNFRBPHI', # Current General Activity; Percent Reporting Increases for Federal Reserve District 3: Philadelphia (NSA)
    'GACISA156MSFRBPHI', # Current General Activity; Percent Reporting Increases for Federal Reserve District 3: Philadelphia
    'GACNNA156MNFRBPHI', # Current General Activity; Percent Reporting No Change for Federal Reserve District 3: Philadelphia (NSA)
    'GACNSA156MSFRBPHI', # Current General Activity; Percent Reporting No Change for Federal Reserve District 3: Philadelphia
    ### Current Prices Paid
    'PPCDFNA066MNFRBPHI', # Current Prices Paid; Diffusion Index for Federal Reserve District 3: Philadelphia (NSA)
    'PPCDFSA066MSFRBPHI', # Current Prices Paid; Diffusion Index for Federal Reserve District 3: Philadelphia
    'PPCDNA156MNFRBPHI', # Current Prices Paid; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia (NSA)
    'PPCDSA156MSFRBPHI', # Current Prices Paid; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia
    'PPCINA156MNFRBPHI', # Current Prices Paid; Percent Reporting Increases for Federal Reserve District 3: Philadelphia (NSA)
    'PPCISA156MSFRBPHI', # Current Prices Paid; Percent Reporting Increases for Federal Reserve District 3: Philadelphia
    'PPCNNA156MNFRBPHI', # Current Prices Paid; Percent Reporting No Change for Federal Reserve District 3: Philadelphia (NSA)
    'PPCNSA156MSFRBPHI', # Current Prices Paid; Percent Reporting No Change for Federal Reserve District 3: Philadelphia
    ### Current Prices Received
    'PRCDFNA066MNFRBPHI', # Current Prices Received; Diffusion Index for Federal Reserve District 3: Philadelphia (NSA)
    'PRCDFSA066MSFRBPHI', # Current Prices Received; Diffusion Index for Federal Reserve District 3: Philadelphia
    'PRCDNA156MNFRBPHI', # Current Prices Received; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia (NSA)
    'PRCDSA156MSFRBPHI', # Current Prices Received; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia
    'PRCINA156MNFRBPHI', # Current Prices Received; Percent Reporting Increases for Federal Reserve District 3: Philadelphia (NSA)
    'PRCISA156MSFRBPHI', # Current Prices Received; Percent Reporting Increases for Federal Reserve District 3: Philadelphia
    'PRCNNA156MNFRBPHI', # Current Prices Received; Percent Reporting No Change for Federal Reserve District 3: Philadelphia (NSA)
    'PRCNSA156MSFRBPHI', # Current Prices Received; Percent Reporting No Change for Federal Reserve District 3: Philadelphia
    ### Current Work Hours
    'AWCDFNA066MNFRBPHI', # Current Work Hours; Diffusion Index for Federal Reserve District 3: Philadelphia (NSA)
    'AWCDFSA066MSFRBPHI', # Current Work Hours; Diffusion Index for Federal Reserve District 3: Philadelphia
    'AWCDNA156MNFRBPHI', # Current Work Hours; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia (NSA)
    'AWCDSA156MSFRBPHI', # Current Work Hours; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia
    'AWCINA156MNFRBPHI', # Current Work Hours; Percent Reporting Increases for Federal Reserve District 3: Philadelphia (NSA)
    'AWCISA156MSFRBPHI', # Current Work Hours; Percent Reporting Increases for Federal Reserve District 3: Philadelphia
    'AWCNNA156MNFRBPHI', # Current Work Hours; Percent Reporting No Change for Federal Reserve District 3: Philadelphia (NSA)
    'AWCNSA156MSFRBPHI', # Current Work Hours; Percent Reporting No Change for Federal Reserve District 3: Philadelphia
    ### Future Capital Expenditures
    'CEFDFNA066MNFRBPHI', # Future Capital Expenditures; Diffusion Index for Federal Reserve District 3: Philadelphia (NSA)
    'CEFDFSA066MSFRBPHI', # Future Capital Expenditures; Diffusion Index for Federal Reserve District 3: Philadelphia
    'CEFDNA156MNFRBPHI', # Future Capital Expenditures; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia (NSA)
    'CEFDSA156MSFRBPHI', # Future Capital Expenditures; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia
    'CEFINA156MNFRBPHI', # Future Capital Expenditures; Percent Reporting Increases for Federal Reserve District 3: Philadelphia (NSA)
    'CEFISA156MSFRBPHI', # Future Capital Expenditures; Percent Reporting Increases for Federal Reserve District 3: Philadelphia
    'CEFNNA156MNFRBPHI', # Future Capital Expenditures; Percent Reporting No Change for Federal Reserve District 3: Philadelphia (NSA)
    'CEFNSA156MSFRBPHI', # Future Capital Expenditures; Percent Reporting No Change for Federal Reserve District 3: Philadelphia
    ### Future Employment
    'NEFDFNA066MNFRBPHI', # Future Employment; Diffusion Index for Federal Reserve District 3: Philadelphia (NSA)
    'NEFDFSA066MSFRBPHI', # Future Employment; Diffusion Index for Federal Reserve District 3: Philadelphia
    'NEFDNA156MNFRBPHI', # Future Employment; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia (NSA)
    'NEFDSA156MSFRBPHI', # Future Employment; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia
    'NEFINA156MNFRBPHI', # Future Employment; Percent Reporting Increases for Federal Reserve District 3: Philadelphia (NSA)
    'NEFISA156MSFRBPHI', # Future Employment; Percent Reporting Increases for Federal Reserve District 3: Philadelphia
    'NEFNNA156MNFRBPHI', # Future Employment; Percent Reporting No Change for Federal Reserve District 3: Philadelphia (NSA)
    'NEFNSA156MSFRBPHI', # Future Employment; Percent Reporting No Change for Federal Reserve District 3: Philadelphia
    ### Future General Activity
    'GAFDFNA066MNFRBPHI', # Future General Activity; Diffusion Index for Federal Reserve District 3: Philadelphia (NSA)
    'GAFDFSA066MSFRBPHI', # Future General Activity; Diffusion Index for Federal Reserve District 3: Philadelphia
    'GAFDNA156MNFRBPHI', # Future General Activity; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia (NSA)
    'GAFDSA156MSFRBPHI', # Future General Activity; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia
    'GAFINA156MNFRBPHI', # Future General Activity; Percent Reporting Increases for Federal Reserve District 3: Philadelphia (NSA)
    'GAFISA156MSFRBPHI', # Future General Activity; Percent Reporting Increases for Federal Reserve District 3: Philadelphia
    'GAFNNA156MNFRBPHI', # Future General Activity; Percent Reporting No Change for Federal Reserve District 3: Philadelphia (NSA)
    'GAFNSA156MSFRBPHI', # Future General Activity; Percent Reporting No Change for Federal Reserve District 3: Philadelphia
    ### Future Prices Paid
    'PPFDFNA066MNFRBPHI', # Future Prices Paid; Diffusion Index for Federal Reserve District 3: Philadelphia (NSA)
    'PPFDFSA066MSFRBPHI', # Future Prices Paid; Diffusion Index for Federal Reserve District 3: Philadelphia
    'PPFDNA156MNFRBPHI', # Future Prices Paid; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia (NSA)
    'PPFDSA156MSFRBPHI', # Future Prices Paid; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia
    'PPFINA156MNFRBPHI', # Future Prices Paid; Percent Reporting Increases for Federal Reserve District 3: Philadelphia (NSA)
    'PPFISA156MSFRBPHI', # Future Prices Paid; Percent Reporting Increases for Federal Reserve District 3: Philadelphia
    'PPFNNA156MNFRBPHI', # Future Prices Paid; Percent Reporting No Change for Federal Reserve District 3: Philadelphia (NSA)
    'PPFNSA156MSFRBPHI', # Future Prices Paid; Percent Reporting No Change for Federal Reserve District 3: Philadelphia
    ### Future Prices Received
    'PRFDFNA066MNFRBPHI', # Future Prices Received; Diffusion Index for Federal Reserve District 3: Philadelphia (NSA)
    'PRFDFSA066MSFRBPHI', # Future Prices Received; Diffusion Index for Federal Reserve District 3: Philadelphia
    'PRFDNA156MNFRBPHI', # Future Prices Received; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia (NSA)
    'PRFDSA156MSFRBPHI', # Future Prices Received; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia
    'PRFINA156MNFRBPHI', # Future Prices Received; Percent Reporting Increases for Federal Reserve District 3: Philadelphia (NSA)
    'PRFISA156MSFRBPHI', # Future Prices Received; Percent Reporting Increases for Federal Reserve District 3: Philadelphia
    'PRFNNA156MNFRBPHI', # Future Prices Received; Percent Reporting No Change for Federal Reserve District 3: Philadelphia (NSA)
    'PRFNSA156MSFRBPHI', # Future Prices Received; Percent Reporting No Change for Federal Reserve District 3: Philadelphia
    ### Future Work Hours
    'AWFDFNA066MNFRBPHI', # Future Work Hours; Diffusion Index for Federal Reserve District 3: Philadelphia (NSA)
    'AWFDFSA066MSFRBPHI', # Future Work Hours; Diffusion Index for Federal Reserve District 3: Philadelphia
    'AWFDNA156MNFRBPHI', # Future Work Hours; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia (NSA)
    'AWFDSA156MSFRBPHI', # Future Work Hours; Percent Reporting Decreases for Federal Reserve District 3: Philadelphia
    'AWFINA156MNFRBPHI', # Future Work Hours; Percent Reporting Increases for Federal Reserve District 3: Philadelphia (NSA)
    'AWFISA156MSFRBPHI', # Future Work Hours; Percent Reporting Increases for Federal Reserve District 3: Philadelphia
    'AWFNNA156MNFRBPHI', # Future Work Hours; Percent Reporting No Change for Federal Reserve District 3: Philadelphia (NSA)
    'AWFNSA156MSFRBPHI', # Future Work Hours; Percent Reporting No Change for Federal Reserve District 3: Philadelphia
    ## New York
    ### Current Average Employee Workweek
    'AWCDINA066MNFRBNY', # Current Average Employee Workweek; Diffusion Index for New York (NSA)
    'AWCDISA066MSFRBNY', # Current Average Employee Workweek; Diffusion Index for New York
    'AWCDNA156MNFRBNY', # Current Average Employee Workweek; Percent Reporting Decreases for New York (NSA)
    'AWCDSA156MSFRBNY', # Current Average Employee Workweek; Percent Reporting Decreases for New York
    'AWCINA156MNFRBNY', # Current Average Employee Workweek; Percent Reporting Increases for New York (NSA)
    'AWCISA156MSFRBNY', # Current Average Employee Workweek; Percent Reporting Increases for New York
    'AWCNNA156MNFRBNY', # Current Average Employee Workweek; Percent Reporting No Change for New York (NSA)
    'AWCNSA156MSFRBNY', # Current Average Employee Workweek; Percent Reporting No Change for New York
    ### Current Delivery Time
    'DTCDINA066MNFRBNY', # Current Delivery Time; Diffusion Index for New York (NSA)
    'DTCDISA066MSFRBNY', # Current Delivery Time; Diffusion Index for New York
    'DTCDNA156MNFRBNY', # Current Delivery Time; Percent Reporting Decreases for New York (NSA)
    'DTCDSA156MSFRBNY', # Current Delivery Time; Percent Reporting Decreases for New York
    'DTCINA156MNFRBNY', # Current Delivery Time; Percent Reporting Increases for New York (NSA)
    'DTCISA156MSFRBNY', # Current Delivery Time; Percent Reporting Increases for New York
    'DTCNNA156MNFRBNY', # Current Delivery Time; Percent Reporting No Change for New York (NSA)
    'DTCNSA156MSFRBNY', # Current Delivery Time; Percent Reporting No Change for New York
    ### Current General Business Conditions
    'GACDINA066MNFRBNY', # Current General Business Conditions; Diffusion Index for New York (NSA)
    'GACDISA066MSFRBNY', # Current General Business Conditions; Diffusion Index for New York
    'GACDNA156MNFRBNY', # Current General Business Conditions; Percent Reporting Decreases for New York (NSA)
    'GACDSA156MSFRBNY', # Current General Business Conditions; Percent Reporting Decreases for New York
    'GACINA156MNFRBNY', # Current General Business Conditions; Percent Reporting Increases for New York (NSA)
    'GACISA156MSFRBNY', # Current General Business Conditions; Percent Reporting Increases for New York
    'GACNNA156MNFRBNY', # Current General Business Conditions; Percent Reporting No Change for New York (NSA)
    'GACNSA156MSFRBNY', # Current General Business Conditions; Percent Reporting No Change for New York
    ### Current Number of Employees
    'NECDINA066MNFRBNY', # Current Number of Employees; Diffusion Index for New York (NSA)
    'NECDISA066MSFRBNY', # Current Number of Employees; Diffusion Index for New York
    'NECDNA156MNFRBNY', # Current Number of Employees; Percent Reporting Decreases for New York (NSA)
    'NECDSA156MSFRBNY', # Current Number of Employees; Percent Reporting Decreases for New York
    'NECINA156MNFRBNY', # Current Number of Employees; Percent Reporting Increases for New York (NSA)
    'NECISA156MSFRBNY', # Current Number of Employees; Percent Reporting Increases for New York
    'NECNNA156MNFRBNY', # Current Number of Employees; Percent Reporting No Change for New York (NSA)
    'NECNSA156MSFRBNY', # Current Number of Employees; Percent Reporting No Change for New York
    ### Current Prices Paid
    'PPCDINA066MNEMFRBNY', # Current Prices Paid; Diffusion Index for New York (NSA)
    'PPCDISA066MSFRBNY', # Current Prices Paid; Diffusion Index for New York
    'PPCDNA156MNEMFRBNY', # Current Prices Paid; Percent Reporting Decreases for New York (NSA)
    'PPCDSA156MSFRBNY', # Current Prices Paid; Percent Reporting Decreases for New York
    'PPCINA156MNEMFRBNY', # Current Prices Paid; Percent Reporting Increases for New York (NSA)
    'PPCISA156MSFRBNY', # Current Prices Paid; Percent Reporting Increases for New York
    'PPCNNA156MNEMFRBNY', # Current Prices Paid; Percent Reporting No Change for New York (NSA)
    'PPCNSA156MSFRBNY', # Current Prices Paid; Percent Reporting No Change for New York
    ### Current Prices Received
    'PRCDINA066MNEMFRBNY', # Current Prices Received; Diffusion Index for New York (NSA)
    'PRCDISA066MSFRBNY', # Current Prices Received; Diffusion Index for New York
    'PRCDNA156MNEMFRBNY', # Current Prices Received; Percent Reporting Decreases for New York (NSA)
    'PRCDSA156MSFRBNY', # Current Prices Received; Percent Reporting Decreases for New York
    'PRCINA156MNEMFRBNY', # Current Prices Received; Percent Reporting Increases for New York (NSA)
    'PRCISA156MSFRBNY', # Current Prices Received; Percent Reporting Increases for New York
    'PRCNNA156MNEMFRBNY', # Current Prices Received; Percent Reporting No Change for New York (NSA)
    'PRCNSA156MSFRBNY', # Current Prices Received; Percent Reporting No Change for New York
    ### Future Average Employee Workweek
    'AWFDINA066MNFRBNY', # Future Average Employee Workweek; Diffusion Index for New York (NSA)
    'AWFDISA066MSFRBNY', # Future Average Employee Workweek; Diffusion Index for New York
    'AWFDNA156MNFRBNY', # Future Average Employee Workweek; Percent Expecting Decreases for New York (NSA)
    'AWFDSA156MSFRBNY', # Future Average Employee Workweek; Percent Expecting Decreases for New York
    'AWFINA156MNFRBNY', # Future Average Employee Workweek; Percent Expecting Increases for New York (NSA)
    'AWFISA156MSFRBNY', # Future Average Employee Workweek; Percent Expecting Increases for New York
    'AWFNNA156MNFRBNY', # Future Average Employee Workweek; Percent Expecting No Change for New York (NSA)
    'AWFNSA156MSFRBNY', # Future Average Employee Workweek; Percent Expecting No Change for New York
    ### Future Capital Expenditures
    'CEFDINA066MNFRBNY', # Future Capital Expenditures; Diffusion Index for New York (NSA)
    'CEFDISA066MSFRBNY', # Future Capital Expenditures; Diffusion Index for New York
    'CEFDNA156MNFRBNY', # Future Capital Expenditures; Percent Expecting Decreases for New York (NSA)
    'CEFDSA156MSFRBNY', # Future Capital Expenditures; Percent Expecting Decreases for New York
    'CEFINA156MNFRBNY', # Future Capital Expenditures; Percent Expecting Increases for New York (NSA)
    'CEFISA156MSFRBNY', # Future Capital Expenditures; Percent Expecting Increases for New York
    'CEFNNA156MNFRBNY', # Future Capital Expenditures; Percent Expecting No Change for New York (NSA)
    'CEFNSA156MSFRBNY', # Future Capital Expenditures; Percent Expecting No Change for New York
    ### Future Delivery Time
    'DTFDINA066MNFRBNY', # Future Delivery Time; Diffusion Index for New York (NSA)
    'DTFDISA066MSFRBNY', # Future Delivery Time; Diffusion Index for New York
    'DTFDNA156MNFRBNY', # Future Delivery Time; Percent Expecting Decreases for New York (NSA)
    'DTFDSA156MSFRBNY', # Future Delivery Time; Percent Expecting Decreases for New York
    'DTFINA156MNFRBNY', # Future Delivery Time; Percent Expecting Increases for New York (NSA)
    'DTFISA156MSFRBNY', # Future Delivery Time; Percent Expecting Increases for New York
    'DTFNNA156MNFRBNY', # Future Delivery Time; Percent Expecting No Change for New York (NSA)
    'DTFNSA156MSFRBNY', # Future Delivery Time; Percent Expecting No Change for New York
    ### Future General Business Conditions
    'GAFDINA066MNFRBNY', # Future General Business Conditions; Diffusion Index for New York (NSA)
    'GAFDISA066MSFRBNY', # Future General Business Conditions; Diffusion Index for New York
    'GAFDNA156MNFRBNY', # Future General Business Conditions; Percent Expecting Decreases for New York (NSA)
    'GAFDSA156MSFRBNY', # Future General Business Conditions; Percent Expecting Decreases for New York
    'GAFINA156MNFRBNY', # Future General Business Conditions; Percent Expecting Increases for New York (NSA)
    'GAFISA156MSFRBNY', # Future General Business Conditions; Percent Expecting Increases for New York
    'GAFNNA156MNFRBNY', # Future General Business Conditions; Percent Expecting No Change for New York (NSA)
    'GAFNSA156MSFRBNY', # Future General Business Conditions; Percent Expecting No Change for New York
    ### Future Number of Employees
    'NEFDINA066MNFRBNY', # Future Number of Employees; Diffusion Index for New York (NSA)
    'NEFDISA066MSFRBNY', # Future Number of Employees; Diffusion Index for New York
    'NEFDNA156MNFRBNY', # Future Number of Employees; Percent Expecting Decreases for New York (NSA)
    'NEFDSA156MSFRBNY', # Future Number of Employees; Percent Expecting Decreases for New York
    'NEFINA156MNFRBNY', # Future Number of Employees; Percent Expecting Increases for New York (NSA)
    'NEFISA156MSFRBNY', # Future Number of Employees; Percent Expecting Increases for New York
    'NEFNNA156MNFRBNY', # Future Number of Employees; Percent Expecting No Change for New York (NSA)
    'NEFNSA156MSFRBNY', # Future Number of Employees; Percent Expecting No Change for New York
    ### Future Prices Paid
    'PPFDINA066MNEMFRBNY', # Future Prices Paid; Diffusion Index for New York (NSA)
    'PPFDISA066MSFRBNY', # Future Prices Paid; Diffusion Index for New York
    'PPFDNA156MNEMFRBNY', # Future Prices Paid; Percent Expecting Decreases for New York (NSA)
    'PPFDSA156MSFRBNY', # Future Prices Paid; Percent Expecting Decreases for New York
    'PPFINA156MNEMFRBNY', # Future Prices Paid; Percent Expecting Increases for New York (NSA)
    'PPFISA156MSFRBNY', # Future Prices Paid; Percent Expecting Increases for New York
    'PPFNNA156MNEMFRBNY', # Future Prices Paid; Percent Expecting No Change for New York (NSA)
    'PPFNSA156MSFRBNY', # Future Prices Paid; Percent Expecting No Change for New York
    ### Future Prices Received
    'PRFDINA066MNEMFRBNY', # Future Prices Received; Diffusion Index for New York (NSA)
    'PRFDISA066MSFRBNY', # Future Prices Received; Diffusion Index for New York
    'PRFDNA156MNEMFRBNY', # Future Prices Received; Percent Expecting Decreases for New York (NSA)
    'PRFDSA156MSFRBNY', # Future Prices Received; Percent Expecting Decreases for New York
    'PRFINA156MNEMFRBNY', # Future Prices Received; Percent Expecting Increases for New York (NSA)
    'PRFISA156MSFRBNY', # Future Prices Received; Percent Expecting Increases for New York
    'PRFNNA156MNEMFRBNY', # Future Prices Received; Percent Expecting No Change for New York (NSA)
    'PRFNSA156MSFRBNY', # Future Prices Received; Percent Expecting No Change for New York
    ### Future Technology Spending
    'TSFDINA066MNFRBNY', # Future Technology Spending; Diffusion Index for New York (DISCONTINUED) (NSA)
    'TSFDISA066MSFRBNY', # Future Technology Spending; Diffusion Index for New York (DISCONTINUED)
    'TSFDNA156MNFRBNY', # Future Technology Spending; Percent Expecting Decreases for New York (DISCONTINUED) (NSA)
    'TSFDSA156MSFRBNY', # Future Technology Spending; Percent Expecting Decreases for New York (DISCONTINUED)
    'TSFINA156MNFRBNY', # Future Technology Spending; Percent Expecting Increases for New York (DISCONTINUED) (NSA)
    'TSFISA156MSFRBNY', # Future Technology Spending; Percent Expecting Increases for New York (DISCONTINUED)
    'TSFNNA156MNFRBNY', # Future Technology Spending; Percent Expecting No Change for New York (DISCONTINUED) (NSA)
    'TSFNSA156MSFRBNY', # Future Technology Spending; Percent Expecting No Change for New York (DISCONTINUED)
    ## Texas
    ### Current Capacity Utilization
    'CAPUSAMFRBDAL', # Current Capacity Utilization; Diffusion Index for Texas
    'CAPUUAMFRBDAL', # Current Capacity Utilization; Diffusion Index for Texas (NSA)
    'CAPUDSAMFRBDAL', # Current Capacity Utilization; Percentage Reporting Decreases for Texas
    'CAPUDUAMFRBDAL', # Current Capacity Utilization; Percentage Reporting Decreases for Texas (NSA)
    'CAPUISAMFRBDAL', # Current Capacity Utilization; Percentage Reporting Increases for Texas
    'CAPUIUAMFRBDAL', # Current Capacity Utilization; Percentage Reporting Increases for Texas (NSA)
    'CAPUNSAMFRBDAL', # Current Capacity Utilization; Percentage Reporting No Change for Texas
    'CAPUNUAMFRBDAL', # Current Capacity Utilization; Percentage Reporting No Change for Texas (NSA)
    ### Current Capital Expenditures
    'CEXPSAMFRBDAL', # Current Capital Expenditures; Diffusion Index for Texas
    'CEXPUAMFRBDAL', # Current Capital Expenditures; Diffusion Index for Texas (NSA)
    'CEXPDSAMFRBDAL', # Current Capital Expenditures; Percentage Reporting Decreases for Texas
    'CEXPDUAMFRBDAL', # Current Capital Expenditures; Percentage Reporting Decreases for Texas (NSA)
    'CEXPISAMFRBDAL', # Current Capital Expenditures; Percentage Reporting Increases for Texas
    'CEXPIUAMFRBDAL', # Current Capital Expenditures; Percentage Reporting Increases for Texas (NSA)
    'CEXPNSAMFRBDAL', # Current Capital Expenditures; Percentage Reporting No Change for Texas
    'CEXPNUAMFRBDAL', # Current Capital Expenditures; Percentage Reporting No Change for Texas (NSA)
    ### Current Company Outlook
    'COLKSAMFRBDAL', # Current Company Outlook; Diffusion Index for Texas
    'COLKUAMFRBDAL', # Current Company Outlook; Diffusion Index for Texas (NSA)
    'COLKDSAMFRBDAL', # Current Company Outlook; Percentage Reporting Decreases for Texas
    'COLKDUAMFRBDAL', # Current Company Outlook; Percentage Reporting Decreases for Texas (NSA)
    'COLKISAMFRBDAL', # Current Company Outlook; Percentage Reporting Increases for Texas
    'COLKIUAMFRBDAL', # Current Company Outlook; Percentage Reporting Increases for Texas (NSA)
    'COLKNSAMFRBDAL', # Current Company Outlook; Percentage Reporting No Change for Texas
    'COLKNUAMFRBDAL', # Current Company Outlook; Percentage Reporting No Change for Texas (NSA)
    ### Current Employment
    'NEMPSAMFRBDAL', # Current Employment; Diffusion Index for Texas
    'NEMPUAMFRBDAL', # Current Employment; Diffusion Index for Texas (NSA)
    'NEMPDSAMFRBDAL', # Current Employment; Percentage Reporting Decreases for Texas
    'NEMPDUAMFRBDAL', # Current Employment; Percentage Reporting Decreases for Texas (NSA)
    'NEMPISAMFRBDAL', # Current Employment; Percentage Reporting Increases for Texas
    'NEMPIUAMFRBDAL', # Current Employment; Percentage Reporting Increases for Texas (NSA)
    'NEMPNSAMFRBDAL', # Current Employment; Percentage Reporting No Change for Texas
    'NEMPNUAMFRBDAL', # Current Employment; Percentage Reporting No Change for Texas (NSA)
    ### Current General Business Activity
    'BACTSAMFRBDAL', # Current General Business Activity; Diffusion Index for Texas
    'BACTUAMFRBDAL', # Current General Business Activity; Diffusion Index for Texas (NSA)
    'BACTDSAMFRBDAL', # Current General Business Activity; Percentage Reporting Decreases for Texas
    'BACTDUAMFRBDAL', # Current General Business Activity; Percentage Reporting Decreases for Texas (NSA)
    'BACTISAMFRBDAL', # Current General Business Activity; Percentage Reporting Increases for Texas
    'BACTIUAMFRBDAL', # Current General Business Activity; Percentage Reporting Increases for Texas (NSA)
    'BACTNSAMFRBDAL', # Current General Business Activity; Percentage Reporting No Change for Texas
    'BACTNUAMFRBDAL', # Current General Business Activity; Percentage Reporting No Change for Texas (NSA)
    ### Current Hours Worked
    'AVGWKSAMFRBDAL', # Current Hours Worked; Diffusion Index for Texas
    'AVGWKUAMFRBDAL', # Current Hours Worked; Diffusion Index for Texas (NSA)
    'AVGWKDSAMFRBDAL', # Current Hours Worked; Percentage Reporting Decreases for Texas
    'AVGWKDUAMFRBDAL', # Current Hours Worked; Percentage Reporting Decreases for Texas (NSA)
    'AVGWKISAMFRBDAL', # Current Hours Worked; Percentage Reporting Increases for Texas
    'AVGWKIUAMFRBDAL', # Current Hours Worked; Percentage Reporting Increases for Texas (NSA)
    'AVGWKNSAMFRBDAL', # Current Hours Worked; Percentage Reporting No Change for Texas
    'AVGWKNUAMFRBDAL', # Current Hours Worked; Percentage Reporting No Change for Texas (NSA)
    ### Current Prices Paid for Raw Materials
    'PRMSAMFRBDAL', # Current Prices Paid for Raw Materials; Diffusion Index for Texas
    'PRMUAMFRBDAL', # Current Prices Paid for Raw Materials; Diffusion Index for Texas (NSA)
    'PRMDSAMFRBDAL', # Current Prices Paid for Raw Materials; Percentage Reporting Decreases for Texas
    'PRMDUAMFRBDAL', # Current Prices Paid for Raw Materials; Percentage Reporting Decreases for Texas (NSA)
    'PRMISAMFRBDAL', # Current Prices Paid for Raw Materials; Percentage Reporting Increases for Texas
    'PRMIUAMFRBDAL', # Current Prices Paid for Raw Materials; Percentage Reporting Increases for Texas (NSA)
    'PRMNSAMFRBDAL', # Current Prices Paid for Raw Materials; Percentage Reporting No Change for Texas
    'PRMNUAMFRBDAL', # Current Prices Paid for Raw Materials; Percentage Reporting No Change for Texas (NSA)
    ### Current Prices Received for Finished Goods
    'PFGSAMFRBDAL', # Current Prices Received for Finished Goods; Diffusion Index for Texas
    'PFGUAMFRBDAL', # Current Prices Received for Finished Goods; Diffusion Index for Texas (NSA)
    'PFGDSAMFRBDAL', # Current Prices Received for Finished Goods; Percentage Reporting Decreases for Texas
    'PFGDUAMFRBDAL', # Current Prices Received for Finished Goods; Percentage Reporting Decreases for Texas (NSA)
    'PFGISAMFRBDAL', # Current Prices Received for Finished Goods; Percentage Reporting Increases for Texas
    'PFGIUAMFRBDAL', # Current Prices Received for Finished Goods; Percentage Reporting Increases for Texas (NSA)
    'PFGNSAMFRBDAL', # Current Prices Received for Finished Goods; Percentage Reporting No Change for Texas
    'PFGNUAMFRBDAL', # Current Prices Received for Finished Goods; Percentage Reporting No Change for Texas (NSA)
    ### Current Production
    'PRODSAMFRBDAL', # Current Production; Diffusion Index for Texas
    'PRODUAMFRBDAL', # Current Production; Diffusion Index for Texas (NSA)
    'PRODDSAMFRBDAL', # Current Production; Percentage Reporting Decreases for Texas
    'PRODDUAMFRBDAL', # Current Production; Percentage Reporting Decreases for Texas (NSA)
    'PRODISAMFRBDAL', # Current Production; Percentage Reporting Increases for Texas
    'PRODIUAMFRBDAL', # Current Production; Percentage Reporting Increases for Texas (NSA)
    'PRODNSAMFRBDAL', # Current Production; Percentage Reporting No Change for Texas
    'PRODNUAMFRBDAL', # Current Production; Percentage Reporting No Change for Texas (NSA)
    ### Current Wages and Benefits
    'WGSSAMFRBDAL', # Current Wages and Benefits; Diffusion Index for Texas
    'WGSUAMFRBDAL', # Current Wages and Benefits; Diffusion Index for Texas (NSA)
    'WGSDSAMFRBDAL', # Current Wages and Benefits; Percentage Reporting Decreases for Texas
    'WGSDUAMFRBDAL', # Current Wages and Benefits; Percentage Reporting Decreases for Texas (NSA)
    'WGSISAMFRBDAL', # Current Wages and Benefits; Percentage Reporting Increases for Texas
    'WGSIUAMFRBDAL', # Current Wages and Benefits; Percentage Reporting Increases for Texas (NSA)
    'WGSNSAMFRBDAL', # Current Wages and Benefits; Percentage Reporting No Change for Texas
    'WGSNUAMFRBDAL', # Current Wages and Benefits; Percentage Reporting No Change for Texas (NSA)
    ### Future Capacity Utilization
    'FCAPUSAMFRBDAL', # Future Capacity Utilization; Diffusion Index for Texas
    'FCAPUUAMFRBDAL', # Future Capacity Utilization; Diffusion Index for Texas (NSA)
    'FCAPUDSAMFRBDAL', # Future Capacity Utilization; Percentage Reporting Decreases for Texas
    'FCAPUDUAMFRBDAL', # Future Capacity Utilization; Percentage Reporting Decreases for Texas (NSA)
    'FCAPUISAMFRBDAL', # Future Capacity Utilization; Percentage Reporting Increases for Texas
    'FCAPUIUAMFRBDAL', # Future Capacity Utilization; Percentage Reporting Increases for Texas (NSA)
    'FCAPUNSAMFRBDAL', # Future Capacity Utilization; Percentage Reporting No Change for Texas
    'FCAPUNUAMFRBDAL', # Future Capacity Utilization; Percentage Reporting No Change for Texas (NSA)
    ### Future Capital Expenditures
    'FCEXPSAMFRBDAL', # Future Capital Expenditures; Diffusion Index for Texas
    'FCEXPUAMFRBDAL', # Future Capital Expenditures; Diffusion Index for Texas (NSA)
    'FCEXPDSAMFRBDAL', # Future Capital Expenditures; Percentage Reporting Decreases for Texas
    'FCEXPDUAMFRBDAL', # Future Capital Expenditures; Percentage Reporting Decreases for Texas (NSA)
    'FCEXPISAMFRBDAL', # Future Capital Expenditures; Percentage Reporting Increases for Texas
    'FCEXPIUAMFRBDAL', # Future Capital Expenditures; Percentage Reporting Increases for Texas (NSA)
    'FCEXPNSAMFRBDAL', # Future Capital Expenditures; Percentage Reporting No Change for Texas
    'FCEXPNUAMFRBDAL', # Future Capital Expenditures; Percentage Reporting No Change for Texas (NSA)
    ### Future Company Outlook
    'FCOLKSAMFRBDAL', # Future Company Outlook; Diffusion Index for Texas
    'FCOLKUAMFRBDAL', # Future Company Outlook; Diffusion Index for Texas (NSA)
    'FCOLKDSAMFRBDAL', # Future Company Outlook; Percentage Reporting Decreases for Texas
    'FCOLKDUAMFRBDAL', # Future Company Outlook; Percentage Reporting Decreases for Texas (NSA)
    'FCOLKISAMFRBDAL', # Future Company Outlook; Percentage Reporting Increases for Texas
    'FCOLKIUAMFRBDAL', # Future Company Outlook; Percentage Reporting Increases for Texas (NSA)
    'FCOLKNSAMFRBDAL', # Future Company Outlook; Percentage Reporting No Change for Texas
    'FCOLKNUAMFRBDAL', # Future Company Outlook; Percentage Reporting No Change for Texas (NSA)
    ### Future Employment
    'FNEMPSAMFRBDAL', # Future Employment; Diffusion Index for Texas
    'FNEMPUAMFRBDAL', # Future Employment; Diffusion Index for Texas (NSA)
    'FNEMPDSAMFRBDAL', # Future Employment; Percentage Reporting Decreases for Texas
    'FNEMPDUAMFRBDAL', # Future Employment; Percentage Reporting Decreases for Texas (NSA)
    'FNEMPISAMFRBDAL', # Future Employment; Percentage Reporting Increases for Texas
    'FNEMPIUAMFRBDAL', # Future Employment; Percentage Reporting Increases for Texas (NSA)
    'FNEMPNSAMFRBDAL', # Future Employment; Percentage Reporting No Change for Texas
    'FNEMPNUAMFRBDAL', # Future Employment; Percentage Reporting No Change for Texas (NSA)
    ### Future General Business Activity
    'FBACTSAMFRBDAL', # Future General Business Activity; Diffusion Index for Texas
    'FBACTUAMFRBDAL', # Future General Business Activity; Diffusion Index for Texas (NSA)
    'FBACTDSAMFRBDAL', # Future General Business Activity; Percentage Reporting Decreases for Texas
    'FBACTDUAMFRBDAL', # Future General Business Activity; Percentage Reporting Decreases for Texas (NSA)
    'FBACTISAMFRBDAL', # Future General Business Activity; Percentage Reporting Increases for Texas
    'FBACTIUAMFRBDAL', # Future General Business Activity; Percentage Reporting Increases for Texas (NSA)
    'FBACTNSAMFRBDAL', # Future General Business Activity; Percentage Reporting No Change for Texas
    'FBACTNUAMFRBDAL', # Future General Business Activity; Percentage Reporting No Change for Texas (NSA)
    ### Future Hours Worked
    'FAVGWKSAMFRBDAL', # Future Hours Worked; Diffusion Index for Texas
    'FAVGWKUAMFRBDAL', # Future Hours Worked; Diffusion Index for Texas (NSA)
    'FAVGWKDSAMFRBDAL', # Future Hours Worked; Percentage Reporting Decreases for Texas
    'FAVGWKDUAMFRBDAL', # Future Hours Worked; Percentage Reporting Decreases for Texas (NSA)
    'FAVGWKISAMFRBDAL', # Future Hours Worked; Percentage Reporting Increases for Texas
    'FAVGWKIUAMFRBDAL', # Future Hours Worked; Percentage Reporting Increases for Texas (NSA)
    'FAVGWKNSAMFRBDAL', # Future Hours Worked; Percentage Reporting No Change for Texas
    'FAVGWKNUAMFRBDAL', # Future Hours Worked; Percentage Reporting No Change for Texas (NSA)
    ### Future Prices Paid for Raw Materials
    'FPRMSAMFRBDAL', # Future Prices Paid for Raw Materials; Diffusion Index for Texas
    'FPRMUAMFRBDAL', # Future Prices Paid for Raw Materials; Diffusion Index for Texas (NSA)
    'FPRMDSAMFRBDAL', # Future Prices Paid for Raw Materials; Percentage Reporting Decreases for Texas
    'FPRMDUAMFRBDAL', # Future Prices Paid for Raw Materials; Percentage Reporting Decreases for Texas (NSA)
    'FPRMISAMFRBDAL', # Future Prices Paid for Raw Materials; Percentage Reporting Increases for Texas
    'FPRMIUAMFRBDAL', # Future Prices Paid for Raw Materials; Percentage Reporting Increases for Texas (NSA)
    'FPRMNSAMFRBDAL', # Future Prices Paid for Raw Materials; Percentage Reporting No Change for Texas
    'FPRMNUAMFRBDAL', # Future Prices Paid for Raw Materials; Percentage Reporting No Change for Texas (NSA)
    ### Future Prices Received for Finished Goods
    'FPFGSAMFRBDAL', # Future Prices Received for Finished Goods; Diffusion Index for Texas
    'FPFGUAMFRBDAL', # Future Prices Received for Finished Goods; Diffusion Index for Texas (NSA)
    'FPFGDSAMFRBDAL', # Future Prices Received for Finished Goods; Percentage Reporting Decreases for Texas
    'FPFGDUAMFRBDAL', # Future Prices Received for Finished Goods; Percentage Reporting Decreases for Texas (NSA)
    'FPFGISAMFRBDAL', # Future Prices Received for Finished Goods; Percentage Reporting Increases for Texas
    'FPFGIUAMFRBDAL', # Future Prices Received for Finished Goods; Percentage Reporting Increases for Texas (NSA)
    'FPFGNSAMFRBDAL', # Future Prices Received for Finished Goods; Percentage Reporting No Change for Texas
    'FPFGNUAMFRBDAL', # Future Prices Received for Finished Goods; Percentage Reporting No Change for Texas (NSA)
    ### Future Production
    'FPRODSAMFRBDAL', # Future Production; Diffusion Index for Texas
    'FPRODUAMFRBDAL', # Future Production; Diffusion Index for Texas (NSA)
    'FPRODDSAMFRBDAL', # Future Production; Percentage Reporting Decreases for Texas
    'FPRODDUAMFRBDAL', # Future Production; Percentage Reporting Decreases for Texas (NSA)
    'FPRODISAMFRBDAL', # Future Production; Percentage Reporting Increases for Texas
    'FPRODIUAMFRBDAL', # Future Production; Percentage Reporting Increases for Texas (NSA)
    'FPRODNSAMFRBDAL', # Future Production; Percentage Reporting No Change for Texas
    'FPRODNUAMFRBDAL', # Future Production; Percentage Reporting No Change for Texas (NSA)
    ### Future Wages and Benefits
    'FWGSSAMFRBDAL', # Future Wages and Benefits; Diffusion Index for Texas
    'FWGSUAMFRBDAL', # Future Wages and Benefits; Diffusion Index for Texas (NSA)
    'FWGSDSAMFRBDAL', # Future Wages and Benefits; Percentage Reporting Decreases for Texas
    'FWGSDUAMFRBDAL', # Future Wages and Benefits; Percentage Reporting Decreases for Texas (NSA)
    'FWGSISAMFRBDAL', # Future Wages and Benefits; Percentage Reporting Increases for Texas
    'FWGSIUAMFRBDAL', # Future Wages and Benefits; Percentage Reporting Increases for Texas (NSA)
    'FWGSNSAMFRBDAL', # Future Wages and Benefits; Percentage Reporting No Change for Texas
    'FWGSNUAMFRBDAL', # Future Wages and Benefits; Percentage Reporting No Change for Texas (NSA)

    # Manufacturing > 직속 - 기타
    ## DISCONTINUED
    'CFMMI', # Chicago Fed Midwest Manufacturing Index (DISCONTINUED)
    'CFMMIAUTO', # Chicago Fed Midwest Manufacturing Index for the Automobile Sector Production (DISCONTINUED)
    'CFMMIMACHINERY', # Chicago Fed Midwest Manufacturing Index for the Machinery Sector Production (DISCONTINUED)
    'CFMMIRESOURCE', # Chicago Fed Midwest Manufacturing Index for the Resource Sector Output (DISCONTINUED)
    'CFMMISTEEL', # Chicago Fed Midwest Manufacturing Index for the Steel Sector Output (DISCONTINUED)
    ## Manufacturers Inventories
    'MNFCTRIMNSA', # Manufacturers Inventories (NSA)
    'MNFCTRIMSA', # Manufacturers Inventories
    'MNFCTRMPCIMNSA', # Manufacturers Inventories (NSA)
    'MNFCTRMPCIMSA', # Manufacturers Inventories
    ## Manufacturers Sales
    'MNFCTRMPCSMNSA', # Manufacturers Sales (NSA)
    'MNFCTRMPCSMSA', # Manufacturers Sales
    'MNFCTRSMNSA', # Manufacturers Sales (NSA)
    'MNFCTRSMSA', # Manufacturers Sales
    ## Manufacturers
    'MNFCTRIRNSA', # Manufacturers: Inventories to Sales Ratio (NSA)
    'MNFCTRIRSA', # Manufacturers: Inventories to Sales Ratio
]

# Quarterly (3)
ids_Q = [
    # Manufacturing > Inventories (386)
    ## Real Manufacturing and Trade Inventories
    'INVCQRMT', # Real Manufacturing and Trade Inventories
    'INVCQRMTSPL', # Real Manufacturing and Trade Inventories
    'INVHQRMT', # Real Manufacturing and Trade Inventories
]

# Annually (4608)
ids_Y = [
    # Manufacturing > 직속 - Annual Integrated Economic Survey (AIES, Census Bureau)
    ## NAICS 31 Manufacturing
    ### 31 Manufacturing
    'AIES31EMPUS', # Manufacturing: Employees
    'AIES31INFUS', # Manufacturing: Finished Goods Inventories
    'AIES31INMUS', # Manufacturing: Materials and Supplies Inventories
    'AIES31INVUS', # Manufacturing: Total Inventories
    'AIES31INWUS', # Manufacturing: Work In Process Inventories
    'AIES31PAYUS', # Manufacturing: Annual Payroll
    'AIES31PWEUS', # Manufacturing: Production Workers
    'AIES31RCTUS', # Manufacturing: Shipments
    'AIES31TCMUS', # Manufacturing: Total Cost of Materials
    ## NAICS 311 Food Manufacturing
    ### 311 Food Manufacturing
    'AIES311EMPUS', # Food Manufacturing: Employees
    'AIES311INFUS', # Food Manufacturing: Finished Goods Inventories
    'AIES311INMUS', # Food Manufacturing: Materials and Supplies Inventories
    'AIES311INVUS', # Food Manufacturing: Total Inventories
    'AIES311INWUS', # Food Manufacturing: Work In Process Inventories
    'AIES311PAYUS', # Food Manufacturing: Annual Payroll
    'AIES311PWEUS', # Food Manufacturing: Production Workers
    'AIES311RCTUS', # Food Manufacturing: Shipments
    'AIES311TCMUS', # Food Manufacturing: Total Cost of Materials
    ### 3111 Animal Food Manufacturing
    'AIES3111EMPUS', # Animal Food Manufacturing: Employees
    'AIES3111INFUS', # Animal Food Manufacturing: Finished Goods Inventories
    'AIES3111INMUS', # Animal Food Manufacturing: Materials and Supplies Inventories
    'AIES3111INVUS', # Animal Food Manufacturing: Total Inventories
    'AIES3111INWUS', # Animal Food Manufacturing: Work In Process Inventories
    'AIES3111PAYUS', # Animal Food Manufacturing: Annual Payroll
    'AIES3111PWEUS', # Animal Food Manufacturing: Production Workers
    'AIES3111RCTUS', # Animal Food Manufacturing: Shipments
    'AIES3111TCMUS', # Animal Food Manufacturing: Total Cost of Materials
    ### 311111 Dog and Cat Food Manufacturing
    'AIES311111EMPUS', # Dog and Cat Food Manufacturing: Employees
    'AIES311111INFUS', # Dog and Cat Food Manufacturing: Finished Goods Inventories
    'AIES311111INMUS', # Dog and Cat Food Manufacturing: Materials and Supplies Inventories
    'AIES311111INVUS', # Dog and Cat Food Manufacturing: Total Inventories
    'AIES311111INWUS', # Dog and Cat Food Manufacturing: Work In Process Inventories
    'AIES311111PAYUS', # Dog and Cat Food Manufacturing: Annual Payroll
    'AIES311111PWEUS', # Dog and Cat Food Manufacturing: Production Workers
    'AIES311111RCTUS', # Dog and Cat Food Manufacturing: Shipments
    'AIES311111TCMUS', # Dog and Cat Food Manufacturing: Total Cost of Materials
    ### 311119 Other Animal Food Manufacturing
    'AIES311119EMPUS', # Other Animal Food Manufacturing: Employees
    'AIES311119INFUS', # Other Animal Food Manufacturing: Finished Goods Inventories
    'AIES311119INMUS', # Other Animal Food Manufacturing: Materials and Supplies Inventories
    'AIES311119INVUS', # Other Animal Food Manufacturing: Total Inventories
    'AIES311119INWUS', # Other Animal Food Manufacturing: Work In Process Inventories
    'AIES311119PAYUS', # Other Animal Food Manufacturing: Annual Payroll
    'AIES311119PWEUS', # Other Animal Food Manufacturing: Production Workers
    'AIES311119RCTUS', # Other Animal Food Manufacturing: Shipments
    'AIES311119TCMUS', # Other Animal Food Manufacturing: Total Cost of Materials
    ### 3112 Grain and Oilseed Milling
    'AIES3112EMPUS', # Grain and Oilseed Milling: Employees
    'AIES3112INFUS', # Grain and Oilseed Milling: Finished Goods Inventories
    'AIES3112INMUS', # Grain and Oilseed Milling: Materials and Supplies Inventories
    'AIES3112INVUS', # Grain and Oilseed Milling: Total Inventories
    'AIES3112INWUS', # Grain and Oilseed Milling: Work In Process Inventories
    'AIES3112PAYUS', # Grain and Oilseed Milling: Annual Payroll
    'AIES3112PWEUS', # Grain and Oilseed Milling: Production Workers
    'AIES3112RCTUS', # Grain and Oilseed Milling: Shipments
    'AIES3112TCMUS', # Grain and Oilseed Milling: Total Cost of Materials
    ### 31121 Flour Milling and Malt Manufacturing
    'AIES31121EMPUS', # Flour Milling and Malt Manufacturing: Employees
    'AIES31121INFUS', # Flour Milling and Malt Manufacturing: Finished Goods Inventories
    'AIES31121INMUS', # Flour Milling and Malt Manufacturing: Materials and Supplies Inventories
    'AIES31121INVUS', # Flour Milling and Malt Manufacturing: Total Inventories
    'AIES31121INWUS', # Flour Milling and Malt Manufacturing: Work In Process Inventories
    'AIES31121PAYUS', # Flour Milling and Malt Manufacturing: Annual Payroll
    'AIES31121PWEUS', # Flour Milling and Malt Manufacturing: Production Workers
    'AIES31121RCTUS', # Flour Milling and Malt Manufacturing: Shipments
    'AIES31121TCMUS', # Flour Milling and Malt Manufacturing: Total Cost of Materials
    ### 311211 Flour Milling
    'AIES311211EMPUS', # Flour Milling: Employees
    'AIES311211INFUS', # Flour Milling: Finished Goods Inventories
    'AIES311211INMUS', # Flour Milling: Materials and Supplies Inventories
    'AIES311211INVUS', # Flour Milling: Total Inventories
    'AIES311211INWUS', # Flour Milling: Work In Process Inventories
    'AIES311211PAYUS', # Flour Milling: Annual Payroll
    'AIES311211PWEUS', # Flour Milling: Production Workers
    'AIES311211RCTUS', # Flour Milling: Shipments
    'AIES311211TCMUS', # Flour Milling: Total Cost of Materials
    ### 311212 Rice Milling
    'AIES311212EMPUS', # Rice Milling: Employees
    'AIES311212INFUS', # Rice Milling: Finished Goods Inventories
    'AIES311212INMUS', # Rice Milling: Materials and Supplies Inventories
    'AIES311212INVUS', # Rice Milling: Total Inventories
    'AIES311212INWUS', # Rice Milling: Work In Process Inventories
    'AIES311212PAYUS', # Rice Milling: Annual Payroll
    'AIES311212PWEUS', # Rice Milling: Production Workers
    'AIES311212RCTUS', # Rice Milling: Shipments
    'AIES311212TCMUS', # Rice Milling: Total Cost of Materials
    ### 311213 Malt Manufacturing
    'AIES311213EMPUS', # Malt Manufacturing: Employees
    'AIES311213INFUS', # Malt Manufacturing: Finished Goods Inventories
    'AIES311213INMUS', # Malt Manufacturing: Materials and Supplies Inventories
    'AIES311213INVUS', # Malt Manufacturing: Total Inventories
    'AIES311213INWUS', # Malt Manufacturing: Work In Process Inventories
    'AIES311213PAYUS', # Malt Manufacturing: Annual Payroll
    'AIES311213PWEUS', # Malt Manufacturing: Production Workers
    'AIES311213RCTUS', # Malt Manufacturing: Shipments
    'AIES311213TCMUS', # Malt Manufacturing: Total Cost of Materials
    ### 31122 Starch and Vegetable Fats and Oils Manufacturing
    'AIES31122EMPUS', # Starch and Vegetable Fats and Oils Manufacturing: Employees
    'AIES31122INFUS', # Starch and Vegetable Fats and Oils Manufacturing: Finished Goods Inventories
    'AIES31122INMUS', # Starch and Vegetable Fats and Oils Manufacturing: Materials and Supplies Inventories
    'AIES31122INVUS', # Starch and Vegetable Fats and Oils Manufacturing: Total Inventories
    'AIES31122INWUS', # Starch and Vegetable Fats and Oils Manufacturing: Work In Process Inventories
    'AIES31122PAYUS', # Starch and Vegetable Fats and Oils Manufacturing: Annual Payroll
    'AIES31122PWEUS', # Starch and Vegetable Fats and Oils Manufacturing: Production Workers
    'AIES31122RCTUS', # Starch and Vegetable Fats and Oils Manufacturing: Shipments
    'AIES31122TCMUS', # Starch and Vegetable Fats and Oils Manufacturing: Total Cost of Materials
    ### 311221 Wet Corn Milling
    'AIES311221EMPUS', # Wet Corn Milling: Employees
    'AIES311221INFUS', # Wet Corn Milling: Finished Goods Inventories
    'AIES311221INMUS', # Wet Corn Milling: Materials and Supplies Inventories
    'AIES311221INVUS', # Wet Corn Milling: Total Inventories
    'AIES311221INWUS', # Wet Corn Milling: Work In Process Inventories
    'AIES311221PAYUS', # Wet Corn Milling: Annual Payroll
    'AIES311221PWEUS', # Wet Corn Milling: Production Workers
    'AIES311221RCTUS', # Wet Corn Milling: Shipments
    'AIES311221TCMUS', # Wet Corn Milling: Total Cost of Materials
    ### 311224 Soybean and Other Oilseed Processing
    'AIES311224EMPUS', # Soybean and Other Oilseed Processing: Employees
    'AIES311224INFUS', # Soybean and Other Oilseed Processing: Finished Goods Inventories
    'AIES311224INMUS', # Soybean and Other Oilseed Processing: Materials and Supplies Inventories
    'AIES311224INVUS', # Soybean and Other Oilseed Processing: Total Inventories
    'AIES311224INWUS', # Soybean and Other Oilseed Processing: Work In Process Inventories
    'AIES311224PAYUS', # Soybean and Other Oilseed Processing: Annual Payroll
    'AIES311224PWEUS', # Soybean and Other Oilseed Processing: Production Workers
    'AIES311224RCTUS', # Soybean and Other Oilseed Processing: Shipments
    'AIES311224TCMUS', # Soybean and Other Oilseed Processing: Total Cost of Materials
    ### 311225 Fats and Oils Refining and Blending
    'AIES311225EMPUS', # Fats and Oils Refining and Blending: Employees
    'AIES311225INFUS', # Fats and Oils Refining and Blending: Finished Goods Inventories
    'AIES311225INMUS', # Fats and Oils Refining and Blending: Materials and Supplies Inventories
    'AIES311225INVUS', # Fats and Oils Refining and Blending: Total Inventories
    'AIES311225INWUS', # Fats and Oils Refining and Blending: Work In Process Inventories
    'AIES311225PAYUS', # Fats and Oils Refining and Blending: Annual Payroll
    'AIES311225PWEUS', # Fats and Oils Refining and Blending: Production Workers
    'AIES311225RCTUS', # Fats and Oils Refining and Blending: Shipments
    'AIES311225TCMUS', # Fats and Oils Refining and Blending: Total Cost of Materials
    ### 31123 Breakfast Cereal Manufacturing
    'AIES31123EMPUS', # Breakfast Cereal Manufacturing: Employees
    'AIES31123INFUS', # Breakfast Cereal Manufacturing: Finished Goods Inventories
    'AIES31123INMUS', # Breakfast Cereal Manufacturing: Materials and Supplies Inventories
    'AIES31123INVUS', # Breakfast Cereal Manufacturing: Total Inventories
    'AIES31123INWUS', # Breakfast Cereal Manufacturing: Work In Process Inventories
    'AIES31123PAYUS', # Breakfast Cereal Manufacturing: Annual Payroll
    'AIES31123PWEUS', # Breakfast Cereal Manufacturing: Production Workers
    'AIES31123RCTUS', # Breakfast Cereal Manufacturing: Shipments
    'AIES31123TCMUS', # Breakfast Cereal Manufacturing: Total Cost of Materials
    ### 3113 Sugar and Confectionery Product Manufacturing
    'AIES3113EMPUS', # Sugar and Confectionery Product Manufacturing: Employees
    'AIES3113INFUS', # Sugar and Confectionery Product Manufacturing: Finished Goods Inventories
    'AIES3113INMUS', # Sugar and Confectionery Product Manufacturing: Materials and Supplies Inventories
    'AIES3113INVUS', # Sugar and Confectionery Product Manufacturing: Total Inventories
    'AIES3113INWUS', # Sugar and Confectionery Product Manufacturing: Work In Process Inventories
    'AIES3113PAYUS', # Sugar and Confectionery Product Manufacturing: Annual Payroll
    'AIES3113PWEUS', # Sugar and Confectionery Product Manufacturing: Production Workers
    'AIES3113RCTUS', # Sugar and Confectionery Product Manufacturing: Shipments
    'AIES3113TCMUS', # Sugar and Confectionery Product Manufacturing: Total Cost of Materials
    ### 31131 Sugar Manufacturing
    'AIES31131EMPUS', # Sugar Manufacturing: Employees
    'AIES31131INFUS', # Sugar Manufacturing: Finished Goods Inventories
    'AIES31131INMUS', # Sugar Manufacturing: Materials and Supplies Inventories
    'AIES31131INVUS', # Sugar Manufacturing: Total Inventories
    'AIES31131INWUS', # Sugar Manufacturing: Work In Process Inventories
    'AIES31131PAYUS', # Sugar Manufacturing: Annual Payroll
    'AIES31131PWEUS', # Sugar Manufacturing: Production Workers
    'AIES31131RCTUS', # Sugar Manufacturing: Shipments
    'AIES31131TCMUS', # Sugar Manufacturing: Total Cost of Materials
    ### 311313 Beet Sugar Manufacturing
    'AIES311313EMPUS', # Beet Sugar Manufacturing: Employees
    'AIES311313INFUS', # Beet Sugar Manufacturing: Finished Goods Inventories
    'AIES311313INMUS', # Beet Sugar Manufacturing: Materials and Supplies Inventories
    'AIES311313INVUS', # Beet Sugar Manufacturing: Total Inventories
    'AIES311313INWUS', # Beet Sugar Manufacturing: Work In Process Inventories
    'AIES311313PAYUS', # Beet Sugar Manufacturing: Annual Payroll
    'AIES311313PWEUS', # Beet Sugar Manufacturing: Production Workers
    'AIES311313RCTUS', # Beet Sugar Manufacturing: Shipments
    'AIES311313TCMUS', # Beet Sugar Manufacturing: Total Cost of Materials
    ### 311314 Cane Sugar Manufacturing
    'AIES311314EMPUS', # Cane Sugar Manufacturing: Employees
    'AIES311314INFUS', # Cane Sugar Manufacturing: Finished Goods Inventories
    'AIES311314INMUS', # Cane Sugar Manufacturing: Materials and Supplies Inventories
    'AIES311314INVUS', # Cane Sugar Manufacturing: Total Inventories
    'AIES311314INWUS', # Cane Sugar Manufacturing: Work In Process Inventories
    'AIES311314PAYUS', # Cane Sugar Manufacturing: Annual Payroll
    'AIES311314PWEUS', # Cane Sugar Manufacturing: Production Workers
    'AIES311314RCTUS', # Cane Sugar Manufacturing: Shipments
    'AIES311314TCMUS', # Cane Sugar Manufacturing: Total Cost of Materials
    ### 31134 Nonchocolate Confectionery Manufacturing
    'AIES31134EMPUS', # Nonchocolate Confectionery Manufacturing: Employees
    'AIES31134INFUS', # Nonchocolate Confectionery Manufacturing: Finished Goods Inventories
    'AIES31134INMUS', # Nonchocolate Confectionery Manufacturing: Materials and Supplies Inventories
    'AIES31134INVUS', # Nonchocolate Confectionery Manufacturing: Total Inventories
    'AIES31134INWUS', # Nonchocolate Confectionery Manufacturing: Work In Process Inventories
    'AIES31134PAYUS', # Nonchocolate Confectionery Manufacturing: Annual Payroll
    'AIES31134PWEUS', # Nonchocolate Confectionery Manufacturing: Production Workers
    'AIES31134RCTUS', # Nonchocolate Confectionery Manufacturing: Shipments
    'AIES31134TCMUS', # Nonchocolate Confectionery Manufacturing: Total Cost of Materials
    ### 31135 Chocolate and Chocolate Confectionery Manufacturing
    'AIES31135EMPUS', # Chocolate and Chocolate Confectionery Manufacturing: Employees
    'AIES31135INFUS', # Chocolate and Chocolate Confectionery Manufacturing: Finished Goods Inventories
    'AIES31135INMUS', # Chocolate and Chocolate Confectionery Manufacturing: Materials and Supplies Inventories
    'AIES31135INVUS', # Chocolate and Chocolate Confectionery Manufacturing: Total Inventories
    'AIES31135INWUS', # Chocolate and Chocolate Confectionery Manufacturing: Work In Process Inventories
    'AIES31135PAYUS', # Chocolate and Chocolate Confectionery Manufacturing: Annual Payroll
    'AIES31135PWEUS', # Chocolate and Chocolate Confectionery Manufacturing: Production Workers
    'AIES31135RCTUS', # Chocolate and Chocolate Confectionery Manufacturing: Shipments
    'AIES31135TCMUS', # Chocolate and Chocolate Confectionery Manufacturing: Total Cost of Materials
    ### 311351 Chocolate and Confectionery Manufacturing From Cacao Beans
    'AIES311351EMPUS', # Chocolate and Confectionery Manufacturing From Cacao Beans: Employees
    'AIES311351INFUS', # Chocolate and Confectionery Manufacturing From Cacao Beans: Finished Goods Inventories
    'AIES311351INMUS', # Chocolate and Confectionery Manufacturing From Cacao Beans: Materials and Supplies Inventories
    'AIES311351INVUS', # Chocolate and Confectionery Manufacturing From Cacao Beans: Total Inventories
    'AIES311351INWUS', # Chocolate and Confectionery Manufacturing From Cacao Beans: Work In Process Inventories
    'AIES311351PAYUS', # Chocolate and Confectionery Manufacturing From Cacao Beans: Annual Payroll
    'AIES311351PWEUS', # Chocolate and Confectionery Manufacturing From Cacao Beans: Production Workers
    'AIES311351RCTUS', # Chocolate and Confectionery Manufacturing From Cacao Beans: Shipments
    'AIES311351TCMUS', # Chocolate and Confectionery Manufacturing From Cacao Beans: Total Cost of Materials
    ### 311352 Confectionery Manufacturing From Purchased Chocolate
    'AIES311352EMPUS', # Confectionery Manufacturing From Purchased Chocolate: Employees
    'AIES311352INFUS', # Confectionery Manufacturing From Purchased Chocolate: Finished Goods Inventories
    'AIES311352INMUS', # Confectionery Manufacturing From Purchased Chocolate: Materials and Supplies Inventories
    'AIES311352INVUS', # Confectionery Manufacturing From Purchased Chocolate: Total Inventories
    'AIES311352INWUS', # Confectionery Manufacturing From Purchased Chocolate: Work In Process Inventories
    'AIES311352PAYUS', # Confectionery Manufacturing From Purchased Chocolate: Annual Payroll
    'AIES311352PWEUS', # Confectionery Manufacturing From Purchased Chocolate: Production Workers
    'AIES311352RCTUS', # Confectionery Manufacturing From Purchased Chocolate: Shipments
    'AIES311352TCMUS', # Confectionery Manufacturing From Purchased Chocolate: Total Cost of Materials
    ### 3114 Fruit and Vegetable Preserving and Specialty Food Manufacturing
    'AIES3114EMPUS', # Fruit and Vegetable Preserving and Specialty Food Manufacturing: Employees
    'AIES3114INFUS', # Fruit and Vegetable Preserving and Specialty Food Manufacturing: Finished Goods Inventories
    'AIES3114INMUS', # Fruit and Vegetable Preserving and Specialty Food Manufacturing: Materials and Supplies Inventories
    'AIES3114INVUS', # Fruit and Vegetable Preserving and Specialty Food Manufacturing: Total Inventories
    'AIES3114INWUS', # Fruit and Vegetable Preserving and Specialty Food Manufacturing: Work In Process Inventories
    'AIES3114PAYUS', # Fruit and Vegetable Preserving and Specialty Food Manufacturing: Annual Payroll
    'AIES3114PWEUS', # Fruit and Vegetable Preserving and Specialty Food Manufacturing: Production Workers
    'AIES3114RCTUS', # Fruit and Vegetable Preserving and Specialty Food Manufacturing: Shipments
    'AIES3114TCMUS', # Fruit and Vegetable Preserving and Specialty Food Manufacturing: Total Cost of Materials
    ### 31141 Frozen Food Manufacturing
    'AIES31141EMPUS', # Frozen Food Manufacturing: Employees
    'AIES31141INFUS', # Frozen Food Manufacturing: Finished Goods Inventories
    'AIES31141INMUS', # Frozen Food Manufacturing: Materials and Supplies Inventories
    'AIES31141INVUS', # Frozen Food Manufacturing: Total Inventories
    'AIES31141INWUS', # Frozen Food Manufacturing: Work In Process Inventories
    'AIES31141PAYUS', # Frozen Food Manufacturing: Annual Payroll
    'AIES31141PWEUS', # Frozen Food Manufacturing: Production Workers
    'AIES31141RCTUS', # Frozen Food Manufacturing: Shipments
    'AIES31141TCMUS', # Frozen Food Manufacturing: Total Cost of Materials
    ### 311411 Frozen Fruit, Juice, and Vegetable Manufacturing
    'AIES311411EMPUS', # Frozen Fruit, Juice, and Vegetable Manufacturing: Employees
    'AIES311411INFUS', # Frozen Fruit, Juice, and Vegetable Manufacturing: Finished Goods Inventories
    'AIES311411INMUS', # Frozen Fruit, Juice, and Vegetable Manufacturing: Materials and Supplies Inventories
    'AIES311411INVUS', # Frozen Fruit, Juice, and Vegetable Manufacturing: Total Inventories
    'AIES311411INWUS', # Frozen Fruit, Juice, and Vegetable Manufacturing: Work In Process Inventories
    'AIES311411PAYUS', # Frozen Fruit, Juice, and Vegetable Manufacturing: Annual Payroll
    'AIES311411PWEUS', # Frozen Fruit, Juice, and Vegetable Manufacturing: Production Workers
    'AIES311411RCTUS', # Frozen Fruit, Juice, and Vegetable Manufacturing: Shipments
    'AIES311411TCMUS', # Frozen Fruit, Juice, and Vegetable Manufacturing: Total Cost of Materials
    ### 311412 Frozen Specialty Food Manufacturing
    'AIES311412EMPUS', # Frozen Specialty Food Manufacturing: Employees
    'AIES311412INFUS', # Frozen Specialty Food Manufacturing: Finished Goods Inventories
    'AIES311412INMUS', # Frozen Specialty Food Manufacturing: Materials and Supplies Inventories
    'AIES311412INVUS', # Frozen Specialty Food Manufacturing: Total Inventories
    'AIES311412INWUS', # Frozen Specialty Food Manufacturing: Work In Process Inventories
    'AIES311412PAYUS', # Frozen Specialty Food Manufacturing: Annual Payroll
    'AIES311412PWEUS', # Frozen Specialty Food Manufacturing: Production Workers
    'AIES311412RCTUS', # Frozen Specialty Food Manufacturing: Shipments
    'AIES311412TCMUS', # Frozen Specialty Food Manufacturing: Total Cost of Materials
    ### 31142 Fruit and Vegetable Canning, Pickling, and Drying
    'AIES31142EMPUS', # Fruit and Vegetable Canning, Pickling, and Drying: Employees
    'AIES31142INFUS', # Fruit and Vegetable Canning, Pickling, and Drying: Finished Goods Inventories
    'AIES31142INMUS', # Fruit and Vegetable Canning, Pickling, and Drying: Materials and Supplies Inventories
    'AIES31142INVUS', # Fruit and Vegetable Canning, Pickling, and Drying: Total Inventories
    'AIES31142INWUS', # Fruit and Vegetable Canning, Pickling, and Drying: Work In Process Inventories
    'AIES31142PAYUS', # Fruit and Vegetable Canning, Pickling, and Drying: Annual Payroll
    'AIES31142PWEUS', # Fruit and Vegetable Canning, Pickling, and Drying: Production Workers
    'AIES31142RCTUS', # Fruit and Vegetable Canning, Pickling, and Drying: Shipments
    'AIES31142TCMUS', # Fruit and Vegetable Canning, Pickling, and Drying: Total Cost of Materials
    ### 311421 Fruit and Vegetable Canning
    'AIES311421EMPUS', # Fruit and Vegetable Canning: Employees
    'AIES311421INFUS', # Fruit and Vegetable Canning: Finished Goods Inventories
    'AIES311421INMUS', # Fruit and Vegetable Canning: Materials and Supplies Inventories
    'AIES311421INVUS', # Fruit and Vegetable Canning: Total Inventories
    'AIES311421INWUS', # Fruit and Vegetable Canning: Work In Process Inventories
    'AIES311421PAYUS', # Fruit and Vegetable Canning: Annual Payroll
    'AIES311421PWEUS', # Fruit and Vegetable Canning: Production Workers
    'AIES311421RCTUS', # Fruit and Vegetable Canning: Shipments
    'AIES311421TCMUS', # Fruit and Vegetable Canning: Total Cost of Materials
    ### 311422 Specialty Canning
    'AIES311422EMPUS', # Specialty Canning: Employees
    'AIES311422INFUS', # Specialty Canning: Finished Goods Inventories
    'AIES311422INMUS', # Specialty Canning: Materials and Supplies Inventories
    'AIES311422INVUS', # Specialty Canning: Total Inventories
    'AIES311422INWUS', # Specialty Canning: Work In Process Inventories
    'AIES311422PAYUS', # Specialty Canning: Annual Payroll
    'AIES311422PWEUS', # Specialty Canning: Production Workers
    'AIES311422RCTUS', # Specialty Canning: Shipments
    'AIES311422TCMUS', # Specialty Canning: Total Cost of Materials
    ### 311423 Dried and Dehydrated Food Manufacturing
    'AIES311423EMPUS', # Dried and Dehydrated Food Manufacturing: Employees
    'AIES311423INFUS', # Dried and Dehydrated Food Manufacturing: Finished Goods Inventories
    'AIES311423INMUS', # Dried and Dehydrated Food Manufacturing: Materials and Supplies Inventories
    'AIES311423INVUS', # Dried and Dehydrated Food Manufacturing: Total Inventories
    'AIES311423INWUS', # Dried and Dehydrated Food Manufacturing: Work In Process Inventories
    'AIES311423PAYUS', # Dried and Dehydrated Food Manufacturing: Annual Payroll
    'AIES311423PWEUS', # Dried and Dehydrated Food Manufacturing: Production Workers
    'AIES311423RCTUS', # Dried and Dehydrated Food Manufacturing: Shipments
    'AIES311423TCMUS', # Dried and Dehydrated Food Manufacturing: Total Cost of Materials
    ### 3115 Dairy Product Manufacturing
    'AIES3115EMPUS', # Dairy Product Manufacturing: Employees
    'AIES3115INFUS', # Dairy Product Manufacturing: Finished Goods Inventories
    'AIES3115INMUS', # Dairy Product Manufacturing: Materials and Supplies Inventories
    'AIES3115INVUS', # Dairy Product Manufacturing: Total Inventories
    'AIES3115INWUS', # Dairy Product Manufacturing: Work In Process Inventories
    'AIES3115PAYUS', # Dairy Product Manufacturing: Annual Payroll
    'AIES3115PWEUS', # Dairy Product Manufacturing: Production Workers
    'AIES3115RCTUS', # Dairy Product Manufacturing: Shipments
    'AIES3115TCMUS', # Dairy Product Manufacturing: Total Cost of Materials
    ### 31151 Dairy Product (Except Frozen) Manufacturing
    'AIES31151EMPUS', # Dairy Product (Except Frozen) Manufacturing: Employees
    'AIES31151INFUS', # Dairy Product (Except Frozen) Manufacturing: Finished Goods Inventories
    'AIES31151INMUS', # Dairy Product (Except Frozen) Manufacturing: Materials and Supplies Inventories
    'AIES31151INVUS', # Dairy Product (Except Frozen) Manufacturing: Total Inventories
    'AIES31151INWUS', # Dairy Product (Except Frozen) Manufacturing: Work In Process Inventories
    'AIES31151PAYUS', # Dairy Product (Except Frozen) Manufacturing: Annual Payroll
    'AIES31151PWEUS', # Dairy Product (Except Frozen) Manufacturing: Production Workers
    'AIES31151RCTUS', # Dairy Product (Except Frozen) Manufacturing: Shipments
    'AIES31151TCMUS', # Dairy Product (Except Frozen) Manufacturing: Total Cost of Materials
    ### 311511 Fluid Milk Manufacturing
    'AIES311511EMPUS', # Fluid Milk Manufacturing: Employees
    'AIES311511INFUS', # Fluid Milk Manufacturing: Finished Goods Inventories
    'AIES311511INMUS', # Fluid Milk Manufacturing: Materials and Supplies Inventories
    'AIES311511INVUS', # Fluid Milk Manufacturing: Total Inventories
    'AIES311511INWUS', # Fluid Milk Manufacturing: Work In Process Inventories
    'AIES311511PAYUS', # Fluid Milk Manufacturing: Annual Payroll
    'AIES311511PWEUS', # Fluid Milk Manufacturing: Production Workers
    'AIES311511RCTUS', # Fluid Milk Manufacturing: Shipments
    'AIES311511TCMUS', # Fluid Milk Manufacturing: Total Cost of Materials
    ### 311512 Creamery Butter Manufacturing
    'AIES311512EMPUS', # Creamery Butter Manufacturing: Employees
    'AIES311512INFUS', # Creamery Butter Manufacturing: Finished Goods Inventories
    'AIES311512INMUS', # Creamery Butter Manufacturing: Materials and Supplies Inventories
    'AIES311512INVUS', # Creamery Butter Manufacturing: Total Inventories
    'AIES311512INWUS', # Creamery Butter Manufacturing: Work In Process Inventories
    'AIES311512PAYUS', # Creamery Butter Manufacturing: Annual Payroll
    'AIES311512PWEUS', # Creamery Butter Manufacturing: Production Workers
    'AIES311512RCTUS', # Creamery Butter Manufacturing: Shipments
    'AIES311512TCMUS', # Creamery Butter Manufacturing: Total Cost of Materials
    ### 311513 Cheese Manufacturing
    'AIES311513EMPUS', # Cheese Manufacturing: Employees
    'AIES311513INFUS', # Cheese Manufacturing: Finished Goods Inventories
    'AIES311513INMUS', # Cheese Manufacturing: Materials and Supplies Inventories
    'AIES311513INVUS', # Cheese Manufacturing: Total Inventories
    'AIES311513INWUS', # Cheese Manufacturing: Work In Process Inventories
    'AIES311513PAYUS', # Cheese Manufacturing: Annual Payroll
    'AIES311513PWEUS', # Cheese Manufacturing: Production Workers
    'AIES311513RCTUS', # Cheese Manufacturing: Shipments
    'AIES311513TCMUS', # Cheese Manufacturing: Total Cost of Materials
    ### 311514 Dry, Condensed, and Evaporated Dairy Product Manufacturing
    'AIES311514EMPUS', # Dry, Condensed, and Evaporated Dairy Product Manufacturing: Employees
    'AIES311514INFUS', # Dry, Condensed, and Evaporated Dairy Product Manufacturing: Finished Goods Inventories
    'AIES311514INMUS', # Dry, Condensed, and Evaporated Dairy Product Manufacturing: Materials and Supplies Inventories
    'AIES311514INVUS', # Dry, Condensed, and Evaporated Dairy Product Manufacturing: Total Inventories
    'AIES311514INWUS', # Dry, Condensed, and Evaporated Dairy Product Manufacturing: Work In Process Inventories
    'AIES311514PAYUS', # Dry, Condensed, and Evaporated Dairy Product Manufacturing: Annual Payroll
    'AIES311514PWEUS', # Dry, Condensed, and Evaporated Dairy Product Manufacturing: Production Workers
    'AIES311514RCTUS', # Dry, Condensed, and Evaporated Dairy Product Manufacturing: Shipments
    'AIES311514TCMUS', # Dry, Condensed, and Evaporated Dairy Product Manufacturing: Total Cost of Materials
    ### 31152 Ice Cream and Frozen Dessert Manufacturing
    'AIES31152EMPUS', # Ice Cream and Frozen Dessert Manufacturing: Employees
    'AIES31152INFUS', # Ice Cream and Frozen Dessert Manufacturing: Finished Goods Inventories
    'AIES31152INMUS', # Ice Cream and Frozen Dessert Manufacturing: Materials and Supplies Inventories
    'AIES31152INVUS', # Ice Cream and Frozen Dessert Manufacturing: Total Inventories
    'AIES31152INWUS', # Ice Cream and Frozen Dessert Manufacturing: Work In Process Inventories
    'AIES31152PAYUS', # Ice Cream and Frozen Dessert Manufacturing: Annual Payroll
    'AIES31152PWEUS', # Ice Cream and Frozen Dessert Manufacturing: Production Workers
    'AIES31152RCTUS', # Ice Cream and Frozen Dessert Manufacturing: Shipments
    'AIES31152TCMUS', # Ice Cream and Frozen Dessert Manufacturing: Total Cost of Materials
    ### 3116 Animal Slaughtering and Processing
    'AIES3116EMPUS', # Animal Slaughtering and Processing: Employees
    'AIES3116INFUS', # Animal Slaughtering and Processing: Finished Goods Inventories
    'AIES3116INMUS', # Animal Slaughtering and Processing: Materials and Supplies Inventories
    'AIES3116INVUS', # Animal Slaughtering and Processing: Total Inventories
    'AIES3116INWUS', # Animal Slaughtering and Processing: Work In Process Inventories
    'AIES3116PAYUS', # Animal Slaughtering and Processing: Annual Payroll
    'AIES3116PWEUS', # Animal Slaughtering and Processing: Production Workers
    'AIES3116RCTUS', # Animal Slaughtering and Processing: Shipments
    'AIES3116TCMUS', # Animal Slaughtering and Processing: Total Cost of Materials
    ### 311611 Animal (Except Poultry) Slaughtering
    'AIES311611EMPUS', # Animal (Except Poultry) Slaughtering: Employees
    'AIES311611INFUS', # Animal (Except Poultry) Slaughtering: Finished Goods Inventories
    'AIES311611INMUS', # Animal (Except Poultry) Slaughtering: Materials and Supplies Inventories
    'AIES311611INVUS', # Animal (Except Poultry) Slaughtering: Total Inventories
    'AIES311611INWUS', # Animal (Except Poultry) Slaughtering: Work In Process Inventories
    'AIES311611PAYUS', # Animal (Except Poultry) Slaughtering: Annual Payroll
    'AIES311611PWEUS', # Animal (Except Poultry) Slaughtering: Production Workers
    'AIES311611RCTUS', # Animal (Except Poultry) Slaughtering: Shipments
    'AIES311611TCMUS', # Animal (Except Poultry) Slaughtering: Total Cost of Materials
    ### 311612 Meat Processed From Carcasses
    'AIES311612EMPUS', # Meat Processed From Carcasses: Employees
    'AIES311612INFUS', # Meat Processed From Carcasses: Finished Goods Inventories
    'AIES311612INMUS', # Meat Processed From Carcasses: Materials and Supplies Inventories
    'AIES311612INVUS', # Meat Processed From Carcasses: Total Inventories
    'AIES311612INWUS', # Meat Processed From Carcasses: Work In Process Inventories
    'AIES311612PAYUS', # Meat Processed From Carcasses: Annual Payroll
    'AIES311612PWEUS', # Meat Processed From Carcasses: Production Workers
    'AIES311612RCTUS', # Meat Processed From Carcasses: Shipments
    'AIES311612TCMUS', # Meat Processed From Carcasses: Total Cost of Materials
    ### 311613 Rendering and Meat Byproduct Processing
    'AIES311613EMPUS', # Rendering and Meat Byproduct Processing: Employees
    'AIES311613INFUS', # Rendering and Meat Byproduct Processing: Finished Goods Inventories
    'AIES311613INMUS', # Rendering and Meat Byproduct Processing: Materials and Supplies Inventories
    'AIES311613INVUS', # Rendering and Meat Byproduct Processing: Total Inventories
    'AIES311613INWUS', # Rendering and Meat Byproduct Processing: Work In Process Inventories
    'AIES311613PAYUS', # Rendering and Meat Byproduct Processing: Annual Payroll
    'AIES311613PWEUS', # Rendering and Meat Byproduct Processing: Production Workers
    'AIES311613RCTUS', # Rendering and Meat Byproduct Processing: Shipments
    'AIES311613TCMUS', # Rendering and Meat Byproduct Processing: Total Cost of Materials
    ### 311615 Poultry Processing
    'AIES311615EMPUS', # Poultry Processing: Employees
    'AIES311615INFUS', # Poultry Processing: Finished Goods Inventories
    'AIES311615INMUS', # Poultry Processing: Materials and Supplies Inventories
    'AIES311615INVUS', # Poultry Processing: Total Inventories
    'AIES311615INWUS', # Poultry Processing: Work In Process Inventories
    'AIES311615PAYUS', # Poultry Processing: Annual Payroll
    'AIES311615PWEUS', # Poultry Processing: Production Workers
    'AIES311615RCTUS', # Poultry Processing: Shipments
    'AIES311615TCMUS', # Poultry Processing: Total Cost of Materials
    ### 3117 Seafood Product Preparation and Packaging
    'AIES3117EMPUS', # Seafood Product Preparation and Packaging: Employees
    'AIES3117INFUS', # Seafood Product Preparation and Packaging: Finished Goods Inventories
    'AIES3117INMUS', # Seafood Product Preparation and Packaging: Materials and Supplies Inventories
    'AIES3117INVUS', # Seafood Product Preparation and Packaging: Total Inventories
    'AIES3117INWUS', # Seafood Product Preparation and Packaging: Work In Process Inventories
    'AIES3117PAYUS', # Seafood Product Preparation and Packaging: Annual Payroll
    'AIES3117PWEUS', # Seafood Product Preparation and Packaging: Production Workers
    'AIES3117RCTUS', # Seafood Product Preparation and Packaging: Shipments
    'AIES3117TCMUS', # Seafood Product Preparation and Packaging: Total Cost of Materials
    ### 3118 Bakeries and Tortilla Manufacturing
    'AIES3118EMPUS', # Bakeries and Tortilla Manufacturing: Employees
    'AIES3118INFUS', # Bakeries and Tortilla Manufacturing: Finished Goods Inventories
    'AIES3118INMUS', # Bakeries and Tortilla Manufacturing: Materials and Supplies Inventories
    'AIES3118INVUS', # Bakeries and Tortilla Manufacturing: Total Inventories
    'AIES3118INWUS', # Bakeries and Tortilla Manufacturing: Work In Process Inventories
    'AIES3118PAYUS', # Bakeries and Tortilla Manufacturing: Annual Payroll
    'AIES3118PWEUS', # Bakeries and Tortilla Manufacturing: Production Workers
    'AIES3118RCTUS', # Bakeries and Tortilla Manufacturing: Shipments
    'AIES3118TCMUS', # Bakeries and Tortilla Manufacturing: Total Cost of Materials
    ### 31181 Bread and Bakery Product Manufacturing
    'AIES31181EMPUS', # Bread and Bakery Product Manufacturing: Employees
    'AIES31181INFUS', # Bread and Bakery Product Manufacturing: Finished Goods Inventories
    'AIES31181INMUS', # Bread and Bakery Product Manufacturing: Materials and Supplies Inventories
    'AIES31181INVUS', # Bread and Bakery Product Manufacturing: Total Inventories
    'AIES31181INWUS', # Bread and Bakery Product Manufacturing: Work In Process Inventories
    'AIES31181PAYUS', # Bread and Bakery Product Manufacturing: Annual Payroll
    'AIES31181PWEUS', # Bread and Bakery Product Manufacturing: Production Workers
    'AIES31181RCTUS', # Bread and Bakery Product Manufacturing: Shipments
    'AIES31181TCMUS', # Bread and Bakery Product Manufacturing: Total Cost of Materials
    ### 311811 Retail Bakeries
    'AIES311811EMPUS', # Retail Bakeries: Employees
    'AIES311811INFUS', # Retail Bakeries: Finished Goods Inventories
    'AIES311811INMUS', # Retail Bakeries: Materials and Supplies Inventories
    'AIES311811INVUS', # Retail Bakeries: Total Inventories
    'AIES311811INWUS', # Retail Bakeries: Work In Process Inventories
    'AIES311811PAYUS', # Retail Bakeries: Annual Payroll
    'AIES311811PWEUS', # Retail Bakeries: Production Workers
    'AIES311811RCTUS', # Retail Bakeries: Shipments
    'AIES311811TCMUS', # Retail Bakeries: Total Cost of Materials
    ### 311812 Commercial Bakeries
    'AIES311812EMPUS', # Commercial Bakeries: Employees
    'AIES311812INFUS', # Commercial Bakeries: Finished Goods Inventories
    'AIES311812INMUS', # Commercial Bakeries: Materials and Supplies Inventories
    'AIES311812INVUS', # Commercial Bakeries: Total Inventories
    'AIES311812INWUS', # Commercial Bakeries: Work In Process Inventories
    'AIES311812PAYUS', # Commercial Bakeries: Annual Payroll
    'AIES311812PWEUS', # Commercial Bakeries: Production Workers
    'AIES311812RCTUS', # Commercial Bakeries: Shipments
    'AIES311812TCMUS', # Commercial Bakeries: Total Cost of Materials
    ### 311813 Frozen Cakes, Pies, and Other Pastries Manufacturing
    'AIES311813EMPUS', # Frozen Cakes, Pies, and Other Pastries Manufacturing: Employees
    'AIES311813INFUS', # Frozen Cakes, Pies, and Other Pastries Manufacturing: Finished Goods Inventories
    'AIES311813INMUS', # Frozen Cakes, Pies, and Other Pastries Manufacturing: Materials and Supplies Inventories
    'AIES311813INVUS', # Frozen Cakes, Pies, and Other Pastries Manufacturing: Total Inventories
    'AIES311813INWUS', # Frozen Cakes, Pies, and Other Pastries Manufacturing: Work In Process Inventories
    'AIES311813PAYUS', # Frozen Cakes, Pies, and Other Pastries Manufacturing: Annual Payroll
    'AIES311813PWEUS', # Frozen Cakes, Pies, and Other Pastries Manufacturing: Production Workers
    'AIES311813RCTUS', # Frozen Cakes, Pies, and Other Pastries Manufacturing: Shipments
    'AIES311813TCMUS', # Frozen Cakes, Pies, and Other Pastries Manufacturing: Total Cost of Materials
    ### 31182 Cookie, Cracker, and Pasta Manufacturing
    'AIES31182EMPUS', # Cookie, Cracker, and Pasta Manufacturing: Employees
    'AIES31182INFUS', # Cookie, Cracker, and Pasta Manufacturing: Finished Goods Inventories
    'AIES31182INMUS', # Cookie, Cracker, and Pasta Manufacturing: Materials and Supplies Inventories
    'AIES31182INVUS', # Cookie, Cracker, and Pasta Manufacturing: Total Inventories
    'AIES31182INWUS', # Cookie, Cracker, and Pasta Manufacturing: Work In Process Inventories
    'AIES31182PAYUS', # Cookie, Cracker, and Pasta Manufacturing: Annual Payroll
    'AIES31182PWEUS', # Cookie, Cracker, and Pasta Manufacturing: Production Workers
    'AIES31182RCTUS', # Cookie, Cracker, and Pasta Manufacturing: Shipments
    'AIES31182TCMUS', # Cookie, Cracker, and Pasta Manufacturing: Total Cost of Materials
    ### 311821 Cookie and Cracker Manufacturing
    'AIES311821EMPUS', # Cookie and Cracker Manufacturing: Employees
    'AIES311821INFUS', # Cookie and Cracker Manufacturing: Finished Goods Inventories
    'AIES311821INMUS', # Cookie and Cracker Manufacturing: Materials and Supplies Inventories
    'AIES311821INVUS', # Cookie and Cracker Manufacturing: Total Inventories
    'AIES311821INWUS', # Cookie and Cracker Manufacturing: Work In Process Inventories
    'AIES311821PAYUS', # Cookie and Cracker Manufacturing: Annual Payroll
    'AIES311821PWEUS', # Cookie and Cracker Manufacturing: Production Workers
    'AIES311821RCTUS', # Cookie and Cracker Manufacturing: Shipments
    'AIES311821TCMUS', # Cookie and Cracker Manufacturing: Total Cost of Materials
    ### 311824 Pasta, Dough, and Mixes From Purchased Flour
    'AIES311824EMPUS', # Pasta, Dough, and Mixes From Purchased Flour: Employees
    'AIES311824INFUS', # Pasta, Dough, and Mixes From Purchased Flour: Finished Goods Inventories
    'AIES311824INMUS', # Pasta, Dough, and Mixes From Purchased Flour: Materials and Supplies Inventories
    'AIES311824INVUS', # Pasta, Dough, and Mixes From Purchased Flour: Total Inventories
    'AIES311824INWUS', # Pasta, Dough, and Mixes From Purchased Flour: Work In Process Inventories
    'AIES311824PAYUS', # Pasta, Dough, and Mixes From Purchased Flour: Annual Payroll
    'AIES311824PWEUS', # Pasta, Dough, and Mixes From Purchased Flour: Production Workers
    'AIES311824RCTUS', # Pasta, Dough, and Mixes From Purchased Flour: Shipments
    'AIES311824TCMUS', # Pasta, Dough, and Mixes From Purchased Flour: Total Cost of Materials
    ### 31183 Tortilla Manufacturing
    'AIES31183EMPUS', # Tortilla Manufacturing: Employees
    'AIES31183INFUS', # Tortilla Manufacturing: Finished Goods Inventories
    'AIES31183INMUS', # Tortilla Manufacturing: Materials and Supplies Inventories
    'AIES31183INVUS', # Tortilla Manufacturing: Total Inventories
    'AIES31183INWUS', # Tortilla Manufacturing: Work In Process Inventories
    'AIES31183PAYUS', # Tortilla Manufacturing: Annual Payroll
    'AIES31183PWEUS', # Tortilla Manufacturing: Production Workers
    'AIES31183RCTUS', # Tortilla Manufacturing: Shipments
    'AIES31183TCMUS', # Tortilla Manufacturing: Total Cost of Materials
    ### 3119 Other Food Manufacturing
    'AIES3119EMPUS', # Other Food Manufacturing: Employees
    'AIES3119INFUS', # Other Food Manufacturing: Finished Goods Inventories
    'AIES3119INMUS', # Other Food Manufacturing: Materials and Supplies Inventories
    'AIES3119INVUS', # Other Food Manufacturing: Total Inventories
    'AIES3119INWUS', # Other Food Manufacturing: Work In Process Inventories
    'AIES3119PAYUS', # Other Food Manufacturing: Annual Payroll
    'AIES3119PWEUS', # Other Food Manufacturing: Production Workers
    'AIES3119RCTUS', # Other Food Manufacturing: Shipments
    'AIES3119TCMUS', # Other Food Manufacturing: Total Cost of Materials
    ### 31191 Snack Food Manufacturing
    'AIES31191EMPUS', # Snack Food Manufacturing: Employees
    'AIES31191INFUS', # Snack Food Manufacturing: Finished Goods Inventories
    'AIES31191INMUS', # Snack Food Manufacturing: Materials and Supplies Inventories
    'AIES31191INVUS', # Snack Food Manufacturing: Total Inventories
    'AIES31191INWUS', # Snack Food Manufacturing: Work In Process Inventories
    'AIES31191PAYUS', # Snack Food Manufacturing: Annual Payroll
    'AIES31191PWEUS', # Snack Food Manufacturing: Production Workers
    'AIES31191RCTUS', # Snack Food Manufacturing: Shipments
    'AIES31191TCMUS', # Snack Food Manufacturing: Total Cost of Materials
    ### 311911 Roasted Nuts and Peanut Butter Manufacturing
    'AIES311911EMPUS', # Roasted Nuts and Peanut Butter Manufacturing: Employees
    'AIES311911INFUS', # Roasted Nuts and Peanut Butter Manufacturing: Finished Goods Inventories
    'AIES311911INMUS', # Roasted Nuts and Peanut Butter Manufacturing: Materials and Supplies Inventories
    'AIES311911INVUS', # Roasted Nuts and Peanut Butter Manufacturing: Total Inventories
    'AIES311911INWUS', # Roasted Nuts and Peanut Butter Manufacturing: Work In Process Inventories
    'AIES311911PAYUS', # Roasted Nuts and Peanut Butter Manufacturing: Annual Payroll
    'AIES311911PWEUS', # Roasted Nuts and Peanut Butter Manufacturing: Production Workers
    'AIES311911RCTUS', # Roasted Nuts and Peanut Butter Manufacturing: Shipments
    'AIES311911TCMUS', # Roasted Nuts and Peanut Butter Manufacturing: Total Cost of Materials
    ### 311919 Other Snack Food Manufacturing
    'AIES311919EMPUS', # Other Snack Food Manufacturing: Employees
    'AIES311919INFUS', # Other Snack Food Manufacturing: Finished Goods Inventories
    'AIES311919INMUS', # Other Snack Food Manufacturing: Materials and Supplies Inventories
    'AIES311919INVUS', # Other Snack Food Manufacturing: Total Inventories
    'AIES311919INWUS', # Other Snack Food Manufacturing: Work In Process Inventories
    'AIES311919PAYUS', # Other Snack Food Manufacturing: Annual Payroll
    'AIES311919PWEUS', # Other Snack Food Manufacturing: Production Workers
    'AIES311919RCTUS', # Other Snack Food Manufacturing: Shipments
    'AIES311919TCMUS', # Other Snack Food Manufacturing: Total Cost of Materials
    ### 31192 Coffee and Tea Manufacturing
    'AIES31192EMPUS', # Coffee and Tea Manufacturing: Employees
    'AIES31192INFUS', # Coffee and Tea Manufacturing: Finished Goods Inventories
    'AIES31192INMUS', # Coffee and Tea Manufacturing: Materials and Supplies Inventories
    'AIES31192INVUS', # Coffee and Tea Manufacturing: Total Inventories
    'AIES31192INWUS', # Coffee and Tea Manufacturing: Work In Process Inventories
    'AIES31192PAYUS', # Coffee and Tea Manufacturing: Annual Payroll
    'AIES31192PWEUS', # Coffee and Tea Manufacturing: Production Workers
    'AIES31192RCTUS', # Coffee and Tea Manufacturing: Shipments
    'AIES31192TCMUS', # Coffee and Tea Manufacturing: Total Cost of Materials
    ### 31193 Flavoring Syrup and Concentrate Manufacturing
    'AIES31193EMPUS', # Flavoring Syrup and Concentrate Manufacturing: Employees
    'AIES31193INFUS', # Flavoring Syrup and Concentrate Manufacturing: Finished Goods Inventories
    'AIES31193INMUS', # Flavoring Syrup and Concentrate Manufacturing: Materials and Supplies Inventories
    'AIES31193INVUS', # Flavoring Syrup and Concentrate Manufacturing: Total Inventories
    'AIES31193INWUS', # Flavoring Syrup and Concentrate Manufacturing: Work In Process Inventories
    'AIES31193PAYUS', # Flavoring Syrup and Concentrate Manufacturing: Annual Payroll
    'AIES31193PWEUS', # Flavoring Syrup and Concentrate Manufacturing: Production Workers
    'AIES31193RCTUS', # Flavoring Syrup and Concentrate Manufacturing: Shipments
    'AIES31193TCMUS', # Flavoring Syrup and Concentrate Manufacturing: Total Cost of Materials
    ### 31194 Seasoning and Dressing Manufacturing
    'AIES31194EMPUS', # Seasoning and Dressing Manufacturing: Employees
    'AIES31194INFUS', # Seasoning and Dressing Manufacturing: Finished Goods Inventories
    'AIES31194INMUS', # Seasoning and Dressing Manufacturing: Materials and Supplies Inventories
    'AIES31194INVUS', # Seasoning and Dressing Manufacturing: Total Inventories
    'AIES31194INWUS', # Seasoning and Dressing Manufacturing: Work In Process Inventories
    'AIES31194PAYUS', # Seasoning and Dressing Manufacturing: Annual Payroll
    'AIES31194PWEUS', # Seasoning and Dressing Manufacturing: Production Workers
    'AIES31194RCTUS', # Seasoning and Dressing Manufacturing: Shipments
    'AIES31194TCMUS', # Seasoning and Dressing Manufacturing: Total Cost of Materials
    ### 311941 Mayonnaise, Dressing, and Other Prepared Sauce Manufacturing
    'AIES311941EMPUS', # Mayonnaise, Dressing, and Other Prepared Sauce Manufacturing: Employees
    'AIES311941INFUS', # Mayonnaise, Dressing, and Other Prepared Sauce Manufacturing: Finished Goods Inventories
    'AIES311941INMUS', # Mayonnaise, Dressing, and Other Prepared Sauce Manufacturing: Materials and Supplies Inventories
    'AIES311941INVUS', # Mayonnaise, Dressing, and Other Prepared Sauce Manufacturing: Total Inventories
    'AIES311941INWUS', # Mayonnaise, Dressing, and Other Prepared Sauce Manufacturing: Work In Process Inventories
    'AIES311941PAYUS', # Mayonnaise, Dressing, and Other Prepared Sauce Manufacturing: Annual Payroll
    'AIES311941PWEUS', # Mayonnaise, Dressing, and Other Prepared Sauce Manufacturing: Production Workers
    'AIES311941RCTUS', # Mayonnaise, Dressing, and Other Prepared Sauce Manufacturing: Shipments
    'AIES311941TCMUS', # Mayonnaise, Dressing, and Other Prepared Sauce Manufacturing: Total Cost of Materials
    ### 311942 Spice and Extract Manufacturing
    'AIES311942EMPUS', # Spice and Extract Manufacturing: Employees
    'AIES311942INFUS', # Spice and Extract Manufacturing: Finished Goods Inventories
    'AIES311942INMUS', # Spice and Extract Manufacturing: Materials and Supplies Inventories
    'AIES311942INVUS', # Spice and Extract Manufacturing: Total Inventories
    'AIES311942INWUS', # Spice and Extract Manufacturing: Work In Process Inventories
    'AIES311942PAYUS', # Spice and Extract Manufacturing: Annual Payroll
    'AIES311942PWEUS', # Spice and Extract Manufacturing: Production Workers
    'AIES311942RCTUS', # Spice and Extract Manufacturing: Shipments
    'AIES311942TCMUS', # Spice and Extract Manufacturing: Total Cost of Materials
    ### 31199 All Other Food Manufacturing
    'AIES31199EMPUS', # All Other Food Manufacturing: Employees
    'AIES31199INFUS', # All Other Food Manufacturing: Finished Goods Inventories
    'AIES31199INMUS', # All Other Food Manufacturing: Materials and Supplies Inventories
    'AIES31199INVUS', # All Other Food Manufacturing: Total Inventories
    'AIES31199INWUS', # All Other Food Manufacturing: Work In Process Inventories
    'AIES31199PAYUS', # All Other Food Manufacturing: Annual Payroll
    'AIES31199PWEUS', # All Other Food Manufacturing: Production Workers
    'AIES31199RCTUS', # All Other Food Manufacturing: Shipments
    'AIES31199TCMUS', # All Other Food Manufacturing: Total Cost of Materials
    ### 311991 Perishable Prepared Food Manufacturing
    'AIES311991EMPUS', # Perishable Prepared Food Manufacturing: Employees
    'AIES311991INFUS', # Perishable Prepared Food Manufacturing: Finished Goods Inventories
    'AIES311991INMUS', # Perishable Prepared Food Manufacturing: Materials and Supplies Inventories
    'AIES311991INVUS', # Perishable Prepared Food Manufacturing: Total Inventories
    'AIES311991INWUS', # Perishable Prepared Food Manufacturing: Work In Process Inventories
    'AIES311991PAYUS', # Perishable Prepared Food Manufacturing: Annual Payroll
    'AIES311991PWEUS', # Perishable Prepared Food Manufacturing: Production Workers
    'AIES311991RCTUS', # Perishable Prepared Food Manufacturing: Shipments
    'AIES311991TCMUS', # Perishable Prepared Food Manufacturing: Total Cost of Materials
    ### 311999 All Other Miscellaneous Food Manufacturing
    'AIES311999EMPUS', # All Other Miscellaneous Food Manufacturing: Employees
    'AIES311999INFUS', # All Other Miscellaneous Food Manufacturing: Finished Goods Inventories
    'AIES311999INMUS', # All Other Miscellaneous Food Manufacturing: Materials and Supplies Inventories
    'AIES311999INVUS', # All Other Miscellaneous Food Manufacturing: Total Inventories
    'AIES311999INWUS', # All Other Miscellaneous Food Manufacturing: Work In Process Inventories
    'AIES311999PAYUS', # All Other Miscellaneous Food Manufacturing: Annual Payroll
    'AIES311999PWEUS', # All Other Miscellaneous Food Manufacturing: Production Workers
    'AIES311999RCTUS', # All Other Miscellaneous Food Manufacturing: Shipments
    'AIES311999TCMUS', # All Other Miscellaneous Food Manufacturing: Total Cost of Materials
    ## NAICS 312 Beverage and Tobacco Product Manufacturing
    ### 312 Beverage and Tobacco Product Manufacturing
    'AIES312EMPUS', # Beverage and Tobacco Product Manufacturing: Employees
    'AIES312INFUS', # Beverage and Tobacco Product Manufacturing: Finished Goods Inventories
    'AIES312INMUS', # Beverage and Tobacco Product Manufacturing: Materials and Supplies Inventories
    'AIES312INVUS', # Beverage and Tobacco Product Manufacturing: Total Inventories
    'AIES312INWUS', # Beverage and Tobacco Product Manufacturing: Work In Process Inventories
    'AIES312PAYUS', # Beverage and Tobacco Product Manufacturing: Annual Payroll
    'AIES312PWEUS', # Beverage and Tobacco Product Manufacturing: Production Workers
    'AIES312RCTUS', # Beverage and Tobacco Product Manufacturing: Shipments
    'AIES312TCMUS', # Beverage and Tobacco Product Manufacturing: Total Cost of Materials
    ### 3121 Beverage Manufacturing
    'AIES3121EMPUS', # Beverage Manufacturing: Employees
    'AIES3121INFUS', # Beverage Manufacturing: Finished Goods Inventories
    'AIES3121INMUS', # Beverage Manufacturing: Materials and Supplies Inventories
    'AIES3121INVUS', # Beverage Manufacturing: Total Inventories
    'AIES3121INWUS', # Beverage Manufacturing: Work In Process Inventories
    'AIES3121PAYUS', # Beverage Manufacturing: Annual Payroll
    'AIES3121PWEUS', # Beverage Manufacturing: Production Workers
    'AIES3121RCTUS', # Beverage Manufacturing: Shipments
    'AIES3121TCMUS', # Beverage Manufacturing: Total Cost of Materials
    ### 31211 Soft Drink and Ice Manufacturing
    'AIES31211EMPUS', # Soft Drink and Ice Manufacturing: Employees
    'AIES31211INFUS', # Soft Drink and Ice Manufacturing: Finished Goods Inventories
    'AIES31211INMUS', # Soft Drink and Ice Manufacturing: Materials and Supplies Inventories
    'AIES31211INVUS', # Soft Drink and Ice Manufacturing: Total Inventories
    'AIES31211INWUS', # Soft Drink and Ice Manufacturing: Work In Process Inventories
    'AIES31211PAYUS', # Soft Drink and Ice Manufacturing: Annual Payroll
    'AIES31211PWEUS', # Soft Drink and Ice Manufacturing: Production Workers
    'AIES31211RCTUS', # Soft Drink and Ice Manufacturing: Shipments
    'AIES31211TCMUS', # Soft Drink and Ice Manufacturing: Total Cost of Materials
    ### 312111 Soft Drink Manufacturing
    'AIES312111EMPUS', # Soft Drink Manufacturing: Employees
    'AIES312111INFUS', # Soft Drink Manufacturing: Finished Goods Inventories
    'AIES312111INMUS', # Soft Drink Manufacturing: Materials and Supplies Inventories
    'AIES312111INVUS', # Soft Drink Manufacturing: Total Inventories
    'AIES312111INWUS', # Soft Drink Manufacturing: Work In Process Inventories
    'AIES312111PAYUS', # Soft Drink Manufacturing: Annual Payroll
    'AIES312111PWEUS', # Soft Drink Manufacturing: Production Workers
    'AIES312111RCTUS', # Soft Drink Manufacturing: Shipments
    'AIES312111TCMUS', # Soft Drink Manufacturing: Total Cost of Materials
    ### 312112 Bottled Water Manufacturing
    'AIES312112EMPUS', # Bottled Water Manufacturing: Employees
    'AIES312112INFUS', # Bottled Water Manufacturing: Finished Goods Inventories
    'AIES312112INMUS', # Bottled Water Manufacturing: Materials and Supplies Inventories
    'AIES312112INVUS', # Bottled Water Manufacturing: Total Inventories
    'AIES312112INWUS', # Bottled Water Manufacturing: Work In Process Inventories
    'AIES312112PAYUS', # Bottled Water Manufacturing: Annual Payroll
    'AIES312112PWEUS', # Bottled Water Manufacturing: Production Workers
    'AIES312112RCTUS', # Bottled Water Manufacturing: Shipments
    'AIES312112TCMUS', # Bottled Water Manufacturing: Total Cost of Materials
    ### 312113 Ice Manufacturing
    'AIES312113EMPUS', # Ice Manufacturing: Employees
    'AIES312113INFUS', # Ice Manufacturing: Finished Goods Inventories
    'AIES312113INMUS', # Ice Manufacturing: Materials and Supplies Inventories
    'AIES312113INVUS', # Ice Manufacturing: Total Inventories
    'AIES312113INWUS', # Ice Manufacturing: Work In Process Inventories
    'AIES312113PAYUS', # Ice Manufacturing: Annual Payroll
    'AIES312113PWEUS', # Ice Manufacturing: Production Workers
    'AIES312113RCTUS', # Ice Manufacturing: Shipments
    'AIES312113TCMUS', # Ice Manufacturing: Total Cost of Materials
    ### 31212 Breweries
    'AIES31212EMPUS', # Breweries: Employees
    'AIES31212INFUS', # Breweries: Finished Goods Inventories
    'AIES31212INMUS', # Breweries: Materials and Supplies Inventories
    'AIES31212INVUS', # Breweries: Total Inventories
    'AIES31212INWUS', # Breweries: Work In Process Inventories
    'AIES31212PAYUS', # Breweries: Annual Payroll
    'AIES31212PWEUS', # Breweries: Production Workers
    'AIES31212RCTUS', # Breweries: Shipments
    'AIES31212TCMUS', # Breweries: Total Cost of Materials
    ### 31213 Wineries
    'AIES31213EMPUS', # Wineries: Employees
    'AIES31213INFUS', # Wineries: Finished Goods Inventories
    'AIES31213INMUS', # Wineries: Materials and Supplies Inventories
    'AIES31213INVUS', # Wineries: Total Inventories
    'AIES31213INWUS', # Wineries: Work In Process Inventories
    'AIES31213PAYUS', # Wineries: Annual Payroll
    'AIES31213PWEUS', # Wineries: Production Workers
    'AIES31213RCTUS', # Wineries: Shipments
    'AIES31213TCMUS', # Wineries: Total Cost of Materials
    ### 31214 Distilleries
    'AIES31214EMPUS', # Distilleries: Employees
    'AIES31214INFUS', # Distilleries: Finished Goods Inventories
    'AIES31214INMUS', # Distilleries: Materials and Supplies Inventories
    'AIES31214INVUS', # Distilleries: Total Inventories
    'AIES31214INWUS', # Distilleries: Work In Process Inventories
    'AIES31214PAYUS', # Distilleries: Annual Payroll
    'AIES31214PWEUS', # Distilleries: Production Workers
    'AIES31214RCTUS', # Distilleries: Shipments
    'AIES31214TCMUS', # Distilleries: Total Cost of Materials
    ### 3122 Tobacco Manufacturing
    'AIES3122EMPUS', # Tobacco Manufacturing: Employees
    'AIES3122INFUS', # Tobacco Manufacturing: Finished Goods Inventories
    'AIES3122INMUS', # Tobacco Manufacturing: Materials and Supplies Inventories
    'AIES3122INVUS', # Tobacco Manufacturing: Total Inventories
    'AIES3122INWUS', # Tobacco Manufacturing: Work In Process Inventories
    'AIES3122PAYUS', # Tobacco Manufacturing: Annual Payroll
    'AIES3122PWEUS', # Tobacco Manufacturing: Production Workers
    'AIES3122RCTUS', # Tobacco Manufacturing: Shipments
    'AIES3122TCMUS', # Tobacco Manufacturing: Total Cost of Materials
    ## NAICS 313 Textile Mills
    ### 313 Textile Mills
    'AIES313EMPUS', # Textile Mills: Employees
    'AIES313INFUS', # Textile Mills: Finished Goods Inventories
    'AIES313INMUS', # Textile Mills: Materials and Supplies Inventories
    'AIES313INVUS', # Textile Mills: Total Inventories
    'AIES313INWUS', # Textile Mills: Work In Process Inventories
    'AIES313PAYUS', # Textile Mills: Annual Payroll
    'AIES313PWEUS', # Textile Mills: Production Workers
    'AIES313RCTUS', # Textile Mills: Shipments
    'AIES313TCMUS', # Textile Mills: Total Cost of Materials
    ### 3131 Fiber, Yarn, and Thread Mills
    'AIES3131EMPUS', # Fiber, Yarn, and Thread Mills: Employees
    'AIES3131INFUS', # Fiber, Yarn, and Thread Mills: Finished Goods Inventories
    'AIES3131INMUS', # Fiber, Yarn, and Thread Mills: Materials and Supplies Inventories
    'AIES3131INVUS', # Fiber, Yarn, and Thread Mills: Total Inventories
    'AIES3131INWUS', # Fiber, Yarn, and Thread Mills: Work In Process Inventories
    'AIES3131PAYUS', # Fiber, Yarn, and Thread Mills: Annual Payroll
    'AIES3131PWEUS', # Fiber, Yarn, and Thread Mills: Production Workers
    'AIES3131RCTUS', # Fiber, Yarn, and Thread Mills: Shipments
    'AIES3131TCMUS', # Fiber, Yarn, and Thread Mills: Total Cost of Materials
    ### 3132 Fabric Mills
    'AIES3132EMPUS', # Fabric Mills: Employees
    'AIES3132INFUS', # Fabric Mills: Finished Goods Inventories
    'AIES3132INMUS', # Fabric Mills: Materials and Supplies Inventories
    'AIES3132INVUS', # Fabric Mills: Total Inventories
    'AIES3132INWUS', # Fabric Mills: Work In Process Inventories
    'AIES3132PAYUS', # Fabric Mills: Annual Payroll
    'AIES3132PWEUS', # Fabric Mills: Production Workers
    'AIES3132RCTUS', # Fabric Mills: Shipments
    'AIES3132TCMUS', # Fabric Mills: Total Cost of Materials
    ### 31321 Broadwoven Fabric Mills
    'AIES31321EMPUS', # Broadwoven Fabric Mills: Employees
    'AIES31321INFUS', # Broadwoven Fabric Mills: Finished Goods Inventories
    'AIES31321INMUS', # Broadwoven Fabric Mills: Materials and Supplies Inventories
    'AIES31321INVUS', # Broadwoven Fabric Mills: Total Inventories
    'AIES31321INWUS', # Broadwoven Fabric Mills: Work In Process Inventories
    'AIES31321PAYUS', # Broadwoven Fabric Mills: Annual Payroll
    'AIES31321PWEUS', # Broadwoven Fabric Mills: Production Workers
    'AIES31321RCTUS', # Broadwoven Fabric Mills: Shipments
    'AIES31321TCMUS', # Broadwoven Fabric Mills: Total Cost of Materials
    ### 31322 Narrow Fabric Mills and Schiffli Machine Embroidery
    'AIES31322EMPUS', # Narrow Fabric Mills and Schiffli Machine Embroidery: Employees
    'AIES31322INFUS', # Narrow Fabric Mills and Schiffli Machine Embroidery: Finished Goods Inventories
    'AIES31322INMUS', # Narrow Fabric Mills and Schiffli Machine Embroidery: Materials and Supplies Inventories
    'AIES31322INVUS', # Narrow Fabric Mills and Schiffli Machine Embroidery: Total Inventories
    'AIES31322INWUS', # Narrow Fabric Mills and Schiffli Machine Embroidery: Work In Process Inventories
    'AIES31322PAYUS', # Narrow Fabric Mills and Schiffli Machine Embroidery: Annual Payroll
    'AIES31322PWEUS', # Narrow Fabric Mills and Schiffli Machine Embroidery: Production Workers
    'AIES31322RCTUS', # Narrow Fabric Mills and Schiffli Machine Embroidery: Shipments
    'AIES31322TCMUS', # Narrow Fabric Mills and Schiffli Machine Embroidery: Total Cost of Materials
    ### 31323 Nonwoven Fabric Mills
    'AIES31323EMPUS', # Nonwoven Fabric Mills: Employees
    'AIES31323INFUS', # Nonwoven Fabric Mills: Finished Goods Inventories
    'AIES31323INMUS', # Nonwoven Fabric Mills: Materials and Supplies Inventories
    'AIES31323INVUS', # Nonwoven Fabric Mills: Total Inventories
    'AIES31323INWUS', # Nonwoven Fabric Mills: Work In Process Inventories
    'AIES31323PAYUS', # Nonwoven Fabric Mills: Annual Payroll
    'AIES31323PWEUS', # Nonwoven Fabric Mills: Production Workers
    'AIES31323RCTUS', # Nonwoven Fabric Mills: Shipments
    'AIES31323TCMUS', # Nonwoven Fabric Mills: Total Cost of Materials
    ### 31324 Knit Fabric Mills
    'AIES31324EMPUS', # Knit Fabric Mills: Employees
    'AIES31324INFUS', # Knit Fabric Mills: Finished Goods Inventories
    'AIES31324INMUS', # Knit Fabric Mills: Materials and Supplies Inventories
    'AIES31324INVUS', # Knit Fabric Mills: Total Inventories
    'AIES31324INWUS', # Knit Fabric Mills: Work In Process Inventories
    'AIES31324PAYUS', # Knit Fabric Mills: Annual Payroll
    'AIES31324PWEUS', # Knit Fabric Mills: Production Workers
    'AIES31324RCTUS', # Knit Fabric Mills: Shipments
    'AIES31324TCMUS', # Knit Fabric Mills: Total Cost of Materials
    ### 3133 Textile and Fabric Finishing and Fabric Coating Mills
    'AIES3133EMPUS', # Textile and Fabric Finishing and Fabric Coating Mills: Employees
    'AIES3133INFUS', # Textile and Fabric Finishing and Fabric Coating Mills: Finished Goods Inventories
    'AIES3133INMUS', # Textile and Fabric Finishing and Fabric Coating Mills: Materials and Supplies Inventories
    'AIES3133INVUS', # Textile and Fabric Finishing and Fabric Coating Mills: Total Inventories
    'AIES3133INWUS', # Textile and Fabric Finishing and Fabric Coating Mills: Work In Process Inventories
    'AIES3133PAYUS', # Textile and Fabric Finishing and Fabric Coating Mills: Annual Payroll
    'AIES3133PWEUS', # Textile and Fabric Finishing and Fabric Coating Mills: Production Workers
    'AIES3133RCTUS', # Textile and Fabric Finishing and Fabric Coating Mills: Shipments
    'AIES3133TCMUS', # Textile and Fabric Finishing and Fabric Coating Mills: Total Cost of Materials
    ### 31331 Textile and Fabric Finishing Mills
    'AIES31331EMPUS', # Textile and Fabric Finishing Mills: Employees
    'AIES31331INFUS', # Textile and Fabric Finishing Mills: Finished Goods Inventories
    'AIES31331INMUS', # Textile and Fabric Finishing Mills: Materials and Supplies Inventories
    'AIES31331INVUS', # Textile and Fabric Finishing Mills: Total Inventories
    'AIES31331INWUS', # Textile and Fabric Finishing Mills: Work In Process Inventories
    'AIES31331PAYUS', # Textile and Fabric Finishing Mills: Annual Payroll
    'AIES31331PWEUS', # Textile and Fabric Finishing Mills: Production Workers
    'AIES31331RCTUS', # Textile and Fabric Finishing Mills: Shipments
    'AIES31331TCMUS', # Textile and Fabric Finishing Mills: Total Cost of Materials
    ### 31332 Fabric Coating Mills
    'AIES31332EMPUS', # Fabric Coating Mills: Employees
    'AIES31332INFUS', # Fabric Coating Mills: Finished Goods Inventories
    'AIES31332INMUS', # Fabric Coating Mills: Materials and Supplies Inventories
    'AIES31332INVUS', # Fabric Coating Mills: Total Inventories
    'AIES31332INWUS', # Fabric Coating Mills: Work In Process Inventories
    'AIES31332PAYUS', # Fabric Coating Mills: Annual Payroll
    'AIES31332PWEUS', # Fabric Coating Mills: Production Workers
    'AIES31332RCTUS', # Fabric Coating Mills: Shipments
    'AIES31332TCMUS', # Fabric Coating Mills: Total Cost of Materials
    ## NAICS 314 Textile Product Mills
    ### 314 Textile Product Mills
    'AIES314EMPUS', # Textile Product Mills: Employees
    'AIES314INFUS', # Textile Product Mills: Finished Goods Inventories
    'AIES314INMUS', # Textile Product Mills: Materials and Supplies Inventories
    'AIES314INVUS', # Textile Product Mills: Total Inventories
    'AIES314INWUS', # Textile Product Mills: Work In Process Inventories
    'AIES314PAYUS', # Textile Product Mills: Annual Payroll
    'AIES314PWEUS', # Textile Product Mills: Production Workers
    'AIES314RCTUS', # Textile Product Mills: Shipments
    'AIES314TCMUS', # Textile Product Mills: Total Cost of Materials
    ### 3141 Textile Furnishings Mills
    'AIES3141EMPUS', # Textile Furnishings Mills: Employees
    'AIES3141INFUS', # Textile Furnishings Mills: Finished Goods Inventories
    'AIES3141INMUS', # Textile Furnishings Mills: Materials and Supplies Inventories
    'AIES3141INVUS', # Textile Furnishings Mills: Total Inventories
    'AIES3141INWUS', # Textile Furnishings Mills: Work In Process Inventories
    'AIES3141PAYUS', # Textile Furnishings Mills: Annual Payroll
    'AIES3141PWEUS', # Textile Furnishings Mills: Production Workers
    'AIES3141RCTUS', # Textile Furnishings Mills: Shipments
    'AIES3141TCMUS', # Textile Furnishings Mills: Total Cost of Materials
    ### 31411 Carpet and Rug Mills
    'AIES31411EMPUS', # Carpet and Rug Mills: Employees
    'AIES31411INFUS', # Carpet and Rug Mills: Finished Goods Inventories
    'AIES31411INMUS', # Carpet and Rug Mills: Materials and Supplies Inventories
    'AIES31411INVUS', # Carpet and Rug Mills: Total Inventories
    'AIES31411INWUS', # Carpet and Rug Mills: Work In Process Inventories
    'AIES31411PAYUS', # Carpet and Rug Mills: Annual Payroll
    'AIES31411PWEUS', # Carpet and Rug Mills: Production Workers
    'AIES31411RCTUS', # Carpet and Rug Mills: Shipments
    'AIES31411TCMUS', # Carpet and Rug Mills: Total Cost of Materials
    ### 31412 Curtain and Linen Mills
    'AIES31412EMPUS', # Curtain and Linen Mills: Employees
    'AIES31412INFUS', # Curtain and Linen Mills: Finished Goods Inventories
    'AIES31412INMUS', # Curtain and Linen Mills: Materials and Supplies Inventories
    'AIES31412INVUS', # Curtain and Linen Mills: Total Inventories
    'AIES31412INWUS', # Curtain and Linen Mills: Work In Process Inventories
    'AIES31412PAYUS', # Curtain and Linen Mills: Annual Payroll
    'AIES31412PWEUS', # Curtain and Linen Mills: Production Workers
    'AIES31412RCTUS', # Curtain and Linen Mills: Shipments
    'AIES31412TCMUS', # Curtain and Linen Mills: Total Cost of Materials
    ### 3149 Other Textile Product Mills
    'AIES3149EMPUS', # Other Textile Product Mills: Employees
    'AIES3149INFUS', # Other Textile Product Mills: Finished Goods Inventories
    'AIES3149INMUS', # Other Textile Product Mills: Materials and Supplies Inventories
    'AIES3149INVUS', # Other Textile Product Mills: Total Inventories
    'AIES3149INWUS', # Other Textile Product Mills: Work In Process Inventories
    'AIES3149PAYUS', # Other Textile Product Mills: Annual Payroll
    'AIES3149PWEUS', # Other Textile Product Mills: Production Workers
    'AIES3149RCTUS', # Other Textile Product Mills: Shipments
    'AIES3149TCMUS', # Other Textile Product Mills: Total Cost of Materials
    ### 31491 Textile Bag and Canvas Mills
    'AIES31491EMPUS', # Textile Bag and Canvas Mills: Employees
    'AIES31491INFUS', # Textile Bag and Canvas Mills: Finished Goods Inventories
    'AIES31491INMUS', # Textile Bag and Canvas Mills: Materials and Supplies Inventories
    'AIES31491INVUS', # Textile Bag and Canvas Mills: Total Inventories
    'AIES31491INWUS', # Textile Bag and Canvas Mills: Work In Process Inventories
    'AIES31491PAYUS', # Textile Bag and Canvas Mills: Annual Payroll
    'AIES31491PWEUS', # Textile Bag and Canvas Mills: Production Workers
    'AIES31491RCTUS', # Textile Bag and Canvas Mills: Shipments
    'AIES31491TCMUS', # Textile Bag and Canvas Mills: Total Cost of Materials
    ### 31499 All Other Textile Product Mills
    'AIES31499EMPUS', # All Other Textile Product Mills: Employees
    'AIES31499INFUS', # All Other Textile Product Mills: Finished Goods Inventories
    'AIES31499INMUS', # All Other Textile Product Mills: Materials and Supplies Inventories
    'AIES31499INVUS', # All Other Textile Product Mills: Total Inventories
    'AIES31499INWUS', # All Other Textile Product Mills: Work In Process Inventories
    'AIES31499PAYUS', # All Other Textile Product Mills: Annual Payroll
    'AIES31499PWEUS', # All Other Textile Product Mills: Production Workers
    'AIES31499RCTUS', # All Other Textile Product Mills: Shipments
    'AIES31499TCMUS', # All Other Textile Product Mills: Total Cost of Materials
    ### 314994 Rope, Cordage, Twine, Tire Cord, and Tire Fabric Mills
    'AIES314994EMPUS', # Rope, Cordage, Twine, Tire Cord, and Tire Fabric Mills: Employees
    'AIES314994INFUS', # Rope, Cordage, Twine, Tire Cord, and Tire Fabric Mills: Finished Goods Inventories
    'AIES314994INMUS', # Rope, Cordage, Twine, Tire Cord, and Tire Fabric Mills: Materials and Supplies Inventories
    'AIES314994INVUS', # Rope, Cordage, Twine, Tire Cord, and Tire Fabric Mills: Total Inventories
    'AIES314994INWUS', # Rope, Cordage, Twine, Tire Cord, and Tire Fabric Mills: Work In Process Inventories
    'AIES314994PAYUS', # Rope, Cordage, Twine, Tire Cord, and Tire Fabric Mills: Annual Payroll
    'AIES314994PWEUS', # Rope, Cordage, Twine, Tire Cord, and Tire Fabric Mills: Production Workers
    'AIES314994RCTUS', # Rope, Cordage, Twine, Tire Cord, and Tire Fabric Mills: Shipments
    'AIES314994TCMUS', # Rope, Cordage, Twine, Tire Cord, and Tire Fabric Mills: Total Cost of Materials
    ### 314999 All Other Miscellaneous Textile Product Mills
    'AIES314999EMPUS', # All Other Miscellaneous Textile Product Mills: Employees
    'AIES314999INFUS', # All Other Miscellaneous Textile Product Mills: Finished Goods Inventories
    'AIES314999INMUS', # All Other Miscellaneous Textile Product Mills: Materials and Supplies Inventories
    'AIES314999INVUS', # All Other Miscellaneous Textile Product Mills: Total Inventories
    'AIES314999INWUS', # All Other Miscellaneous Textile Product Mills: Work In Process Inventories
    'AIES314999PAYUS', # All Other Miscellaneous Textile Product Mills: Annual Payroll
    'AIES314999PWEUS', # All Other Miscellaneous Textile Product Mills: Production Workers
    'AIES314999RCTUS', # All Other Miscellaneous Textile Product Mills: Shipments
    'AIES314999TCMUS', # All Other Miscellaneous Textile Product Mills: Total Cost of Materials
    ## NAICS 315 Apparel Manufacturing
    ### 315 Apparel Manufacturing
    'AIES315EMPUS', # Apparel Manufacturing: Employees
    'AIES315INFUS', # Apparel Manufacturing: Finished Goods Inventories
    'AIES315INMUS', # Apparel Manufacturing: Materials and Supplies Inventories
    'AIES315INVUS', # Apparel Manufacturing: Total Inventories
    'AIES315INWUS', # Apparel Manufacturing: Work In Process Inventories
    'AIES315PAYUS', # Apparel Manufacturing: Annual Payroll
    'AIES315PWEUS', # Apparel Manufacturing: Production Workers
    'AIES315RCTUS', # Apparel Manufacturing: Shipments
    'AIES315TCMUS', # Apparel Manufacturing: Total Cost of Materials
    ### 3151 Apparel Knitting Mills
    'AIES3151EMPUS', # Apparel Knitting Mills: Employees
    'AIES3151INFUS', # Apparel Knitting Mills: Finished Goods Inventories
    'AIES3151INMUS', # Apparel Knitting Mills: Materials and Supplies Inventories
    'AIES3151INVUS', # Apparel Knitting Mills: Total Inventories
    'AIES3151INWUS', # Apparel Knitting Mills: Work In Process Inventories
    'AIES3151PAYUS', # Apparel Knitting Mills: Annual Payroll
    'AIES3151PWEUS', # Apparel Knitting Mills: Production Workers
    'AIES3151RCTUS', # Apparel Knitting Mills: Shipments
    'AIES3151TCMUS', # Apparel Knitting Mills: Total Cost of Materials
    ### 31511 Hosiery and Sock Mills
    'AIES31511EMPUS', # Hosiery and Sock Mills: Employees
    'AIES31511INFUS', # Hosiery and Sock Mills: Finished Goods Inventories
    'AIES31511INMUS', # Hosiery and Sock Mills: Materials and Supplies Inventories
    'AIES31511INVUS', # Hosiery and Sock Mills: Total Inventories
    'AIES31511INWUS', # Hosiery and Sock Mills: Work In Process Inventories
    'AIES31511PAYUS', # Hosiery and Sock Mills: Annual Payroll
    'AIES31511PWEUS', # Hosiery and Sock Mills: Production Workers
    'AIES31511RCTUS', # Hosiery and Sock Mills: Shipments
    'AIES31511TCMUS', # Hosiery and Sock Mills: Total Cost of Materials
    ### 31519 Other Apparel Knitting Mills
    'AIES31519EMPUS', # Other Apparel Knitting Mills: Employees
    'AIES31519INFUS', # Other Apparel Knitting Mills: Finished Goods Inventories
    'AIES31519INMUS', # Other Apparel Knitting Mills: Materials and Supplies Inventories
    'AIES31519INVUS', # Other Apparel Knitting Mills: Total Inventories
    'AIES31519INWUS', # Other Apparel Knitting Mills: Work In Process Inventories
    'AIES31519PAYUS', # Other Apparel Knitting Mills: Annual Payroll
    'AIES31519PWEUS', # Other Apparel Knitting Mills: Production Workers
    'AIES31519RCTUS', # Other Apparel Knitting Mills: Shipments
    'AIES31519TCMUS', # Other Apparel Knitting Mills: Total Cost of Materials
    ### 3152 Cut and Sew Apparel Manufacturing
    'AIES3152EMPUS', # Cut and Sew Apparel Manufacturing: Employees
    'AIES3152INFUS', # Cut and Sew Apparel Manufacturing: Finished Goods Inventories
    'AIES3152INMUS', # Cut and Sew Apparel Manufacturing: Materials and Supplies Inventories
    'AIES3152INVUS', # Cut and Sew Apparel Manufacturing: Total Inventories
    'AIES3152INWUS', # Cut and Sew Apparel Manufacturing: Work In Process Inventories
    'AIES3152PAYUS', # Cut and Sew Apparel Manufacturing: Annual Payroll
    'AIES3152PWEUS', # Cut and Sew Apparel Manufacturing: Production Workers
    'AIES3152RCTUS', # Cut and Sew Apparel Manufacturing: Shipments
    'AIES3152TCMUS', # Cut and Sew Apparel Manufacturing: Total Cost of Materials
    ### 31521 Cut and Sew Apparel Contractors
    'AIES31521EMPUS', # Cut and Sew Apparel Contractors: Employees
    'AIES31521INFUS', # Cut and Sew Apparel Contractors: Finished Goods Inventories
    'AIES31521INMUS', # Cut and Sew Apparel Contractors: Materials and Supplies Inventories
    'AIES31521INVUS', # Cut and Sew Apparel Contractors: Total Inventories
    'AIES31521INWUS', # Cut and Sew Apparel Contractors: Work In Process Inventories
    'AIES31521PAYUS', # Cut and Sew Apparel Contractors: Annual Payroll
    'AIES31521PWEUS', # Cut and Sew Apparel Contractors: Production Workers
    'AIES31521RCTUS', # Cut and Sew Apparel Contractors: Shipments
    'AIES31521TCMUS', # Cut and Sew Apparel Contractors: Total Cost of Materials
    ### 31522 Men's and Boys' Cut and Sew Apparel Manufacturing
    'AIES31522EMPUS', # Men's and Boys' Cut and Sew Apparel Manufacturing: Employees
    'AIES31522INFUS', # Men's and Boys' Cut and Sew Apparel Manufacturing: Finished Goods Inventories
    'AIES31522INMUS', # Men's and Boys' Cut and Sew Apparel Manufacturing: Materials and Supplies Inventories
    'AIES31522INVUS', # Men's and Boys' Cut and Sew Apparel Manufacturing: Total Inventories
    'AIES31522INWUS', # Men's and Boys' Cut and Sew Apparel Manufacturing: Work In Process Inventories
    'AIES31522PAYUS', # Men's and Boys' Cut and Sew Apparel Manufacturing: Annual Payroll
    'AIES31522PWEUS', # Men's and Boys' Cut and Sew Apparel Manufacturing: Production Workers
    'AIES31522RCTUS', # Men's and Boys' Cut and Sew Apparel Manufacturing: Shipments
    'AIES31522TCMUS', # Men's and Boys' Cut and Sew Apparel Manufacturing: Total Cost of Materials
    ### 31524 Women's, Girls', and Infants' Cut and Sew Apparel Manufacturing
    'AIES31524EMPUS', # Women's, Girls', and Infants' Cut and Sew Apparel Manufacturing: Employees
    'AIES31524INFUS', # Women's, Girls', and Infants' Cut and Sew Apparel Manufacturing: Finished Goods Inventories
    'AIES31524INMUS', # Women's, Girls', and Infants' Cut and Sew Apparel Manufacturing: Materials and Supplies Inventories
    'AIES31524INVUS', # Women's, Girls', and Infants' Cut and Sew Apparel Manufacturing: Total Inventories
    'AIES31524INWUS', # Women's, Girls', and Infants' Cut and Sew Apparel Manufacturing: Work In Process Inventories
    'AIES31524PAYUS', # Women's, Girls', and Infants' Cut and Sew Apparel Manufacturing: Annual Payroll
    'AIES31524PWEUS', # Women's, Girls', and Infants' Cut and Sew Apparel Manufacturing: Production Workers
    'AIES31524RCTUS', # Women's, Girls', and Infants' Cut and Sew Apparel Manufacturing: Shipments
    'AIES31524TCMUS', # Women's, Girls', and Infants' Cut and Sew Apparel Manufacturing: Total Cost of Materials
    ### 31528 Other Cut and Sew Apparel Manufacturing
    'AIES31528EMPUS', # Other Cut and Sew Apparel Manufacturing: Employees
    'AIES31528INFUS', # Other Cut and Sew Apparel Manufacturing: Finished Goods Inventories
    'AIES31528INMUS', # Other Cut and Sew Apparel Manufacturing: Materials and Supplies Inventories
    'AIES31528INVUS', # Other Cut and Sew Apparel Manufacturing: Total Inventories
    'AIES31528INWUS', # Other Cut and Sew Apparel Manufacturing: Work In Process Inventories
    'AIES31528PAYUS', # Other Cut and Sew Apparel Manufacturing: Annual Payroll
    'AIES31528PWEUS', # Other Cut and Sew Apparel Manufacturing: Production Workers
    'AIES31528RCTUS', # Other Cut and Sew Apparel Manufacturing: Shipments
    'AIES31528TCMUS', # Other Cut and Sew Apparel Manufacturing: Total Cost of Materials
    ### 3159 Apparel Accessories and Other Apparel Manufacturing
    'AIES3159EMPUS', # Apparel Accessories and Other Apparel Manufacturing: Employees
    'AIES3159INFUS', # Apparel Accessories and Other Apparel Manufacturing: Finished Goods Inventories
    'AIES3159INMUS', # Apparel Accessories and Other Apparel Manufacturing: Materials and Supplies Inventories
    'AIES3159INVUS', # Apparel Accessories and Other Apparel Manufacturing: Total Inventories
    'AIES3159INWUS', # Apparel Accessories and Other Apparel Manufacturing: Work In Process Inventories
    'AIES3159PAYUS', # Apparel Accessories and Other Apparel Manufacturing: Annual Payroll
    'AIES3159PWEUS', # Apparel Accessories and Other Apparel Manufacturing: Production Workers
    'AIES3159RCTUS', # Apparel Accessories and Other Apparel Manufacturing: Shipments
    'AIES3159TCMUS', # Apparel Accessories and Other Apparel Manufacturing: Total Cost of Materials
    ## NAICS 316 Leather and Allied Product Manufacturing
    ### 316 Leather and Allied Product Manufacturing
    'AIES316EMPUS', # Leather and Allied Product Manufacturing: Employees
    'AIES316INFUS', # Leather and Allied Product Manufacturing: Finished Goods Inventories
    'AIES316INMUS', # Leather and Allied Product Manufacturing: Materials and Supplies Inventories
    'AIES316INVUS', # Leather and Allied Product Manufacturing: Total Inventories
    'AIES316INWUS', # Leather and Allied Product Manufacturing: Work In Process Inventories
    'AIES316PAYUS', # Leather and Allied Product Manufacturing: Annual Payroll
    'AIES316PWEUS', # Leather and Allied Product Manufacturing: Production Workers
    'AIES316RCTUS', # Leather and Allied Product Manufacturing: Shipments
    'AIES316TCMUS', # Leather and Allied Product Manufacturing: Total Cost of Materials
    ### 3161 Leather and Hide Tanning and Finishing
    'AIES3161EMPUS', # Leather and Hide Tanning and Finishing: Employees
    'AIES3161INFUS', # Leather and Hide Tanning and Finishing: Finished Goods Inventories
    'AIES3161INMUS', # Leather and Hide Tanning and Finishing: Materials and Supplies Inventories
    'AIES3161INVUS', # Leather and Hide Tanning and Finishing: Total Inventories
    'AIES3161INWUS', # Leather and Hide Tanning and Finishing: Work In Process Inventories
    'AIES3161PAYUS', # Leather and Hide Tanning and Finishing: Annual Payroll
    'AIES3161PWEUS', # Leather and Hide Tanning and Finishing: Production Workers
    'AIES3161RCTUS', # Leather and Hide Tanning and Finishing: Shipments
    'AIES3161TCMUS', # Leather and Hide Tanning and Finishing: Total Cost of Materials
    ### 3162 Footwear Manufacturing
    'AIES3162EMPUS', # Footwear Manufacturing: Employees
    'AIES3162INFUS', # Footwear Manufacturing: Finished Goods Inventories
    'AIES3162INMUS', # Footwear Manufacturing: Materials and Supplies Inventories
    'AIES3162INVUS', # Footwear Manufacturing: Total Inventories
    'AIES3162INWUS', # Footwear Manufacturing: Work In Process Inventories
    'AIES3162PAYUS', # Footwear Manufacturing: Annual Payroll
    'AIES3162PWEUS', # Footwear Manufacturing: Production Workers
    'AIES3162RCTUS', # Footwear Manufacturing: Shipments
    'AIES3162TCMUS', # Footwear Manufacturing: Total Cost of Materials
    ### 3169 Other Leather and Allied Product Manufacturing
    'AIES3169EMPUS', # Other Leather and Allied Product Manufacturing: Employees
    'AIES3169INFUS', # Other Leather and Allied Product Manufacturing: Finished Goods Inventories
    'AIES3169INMUS', # Other Leather and Allied Product Manufacturing: Materials and Supplies Inventories
    'AIES3169INVUS', # Other Leather and Allied Product Manufacturing: Total Inventories
    'AIES3169INWUS', # Other Leather and Allied Product Manufacturing: Work In Process Inventories
    'AIES3169PAYUS', # Other Leather and Allied Product Manufacturing: Annual Payroll
    'AIES3169PWEUS', # Other Leather and Allied Product Manufacturing: Production Workers
    'AIES3169RCTUS', # Other Leather and Allied Product Manufacturing: Shipments
    'AIES3169TCMUS', # Other Leather and Allied Product Manufacturing: Total Cost of Materials
    ### 316992 Women's Handbag and Purse Manufacturing
    'AIES316992EMPUS', # Women's Handbag and Purse Manufacturing: Employees
    'AIES316992INFUS', # Women's Handbag and Purse Manufacturing: Finished Goods Inventories
    'AIES316992INMUS', # Women's Handbag and Purse Manufacturing: Materials and Supplies Inventories
    'AIES316992INVUS', # Women's Handbag and Purse Manufacturing: Total Inventories
    'AIES316992INWUS', # Women's Handbag and Purse Manufacturing: Work In Process Inventories
    'AIES316992PAYUS', # Women's Handbag and Purse Manufacturing: Annual Payroll
    'AIES316992PWEUS', # Women's Handbag and Purse Manufacturing: Production Workers
    'AIES316992RCTUS', # Women's Handbag and Purse Manufacturing: Shipments
    'AIES316992TCMUS', # Women's Handbag and Purse Manufacturing: Total Cost of Materials
    ### 316998 All Other Leather Good and Allied Product Manufacturing
    'AIES316998EMPUS', # All Other Leather Good and Allied Product Manufacturing: Employees
    'AIES316998INFUS', # All Other Leather Good and Allied Product Manufacturing: Finished Goods Inventories
    'AIES316998INMUS', # All Other Leather Good and Allied Product Manufacturing: Materials and Supplies Inventories
    'AIES316998INVUS', # All Other Leather Good and Allied Product Manufacturing: Total Inventories
    'AIES316998INWUS', # All Other Leather Good and Allied Product Manufacturing: Work In Process Inventories
    'AIES316998PAYUS', # All Other Leather Good and Allied Product Manufacturing: Annual Payroll
    'AIES316998PWEUS', # All Other Leather Good and Allied Product Manufacturing: Production Workers
    'AIES316998RCTUS', # All Other Leather Good and Allied Product Manufacturing: Shipments
    'AIES316998TCMUS', # All Other Leather Good and Allied Product Manufacturing: Total Cost of Materials
    ## NAICS 321 Wood Product Manufacturing
    ### 321 Wood Product Manufacturing
    'AIES321EMPUS', # Wood Product Manufacturing: Employees
    'AIES321INFUS', # Wood Product Manufacturing: Finished Goods Inventories
    'AIES321INMUS', # Wood Product Manufacturing: Materials and Supplies Inventories
    'AIES321INVUS', # Wood Product Manufacturing: Total Inventories
    'AIES321INWUS', # Wood Product Manufacturing: Work In Process Inventories
    'AIES321PAYUS', # Wood Product Manufacturing: Annual Payroll
    'AIES321PWEUS', # Wood Product Manufacturing: Production Workers
    'AIES321RCTUS', # Wood Product Manufacturing: Shipments
    'AIES321TCMUS', # Wood Product Manufacturing: Total Cost of Materials
    ### 3211 Sawmills and Wood Preservation
    'AIES3211EMPUS', # Sawmills and Wood Preservation: Employees
    'AIES3211INFUS', # Sawmills and Wood Preservation: Finished Goods Inventories
    'AIES3211INMUS', # Sawmills and Wood Preservation: Materials and Supplies Inventories
    'AIES3211INVUS', # Sawmills and Wood Preservation: Total Inventories
    'AIES3211INWUS', # Sawmills and Wood Preservation: Work In Process Inventories
    'AIES3211PAYUS', # Sawmills and Wood Preservation: Annual Payroll
    'AIES3211PWEUS', # Sawmills and Wood Preservation: Production Workers
    'AIES3211RCTUS', # Sawmills and Wood Preservation: Shipments
    'AIES3211TCMUS', # Sawmills and Wood Preservation: Total Cost of Materials
    ### 321113 Sawmills
    'AIES321113EMPUS', # Sawmills: Employees
    'AIES321113INFUS', # Sawmills: Finished Goods Inventories
    'AIES321113INMUS', # Sawmills: Materials and Supplies Inventories
    'AIES321113INVUS', # Sawmills: Total Inventories
    'AIES321113INWUS', # Sawmills: Work In Process Inventories
    'AIES321113PAYUS', # Sawmills: Annual Payroll
    'AIES321113PWEUS', # Sawmills: Production Workers
    'AIES321113RCTUS', # Sawmills: Shipments
    'AIES321113TCMUS', # Sawmills: Total Cost of Materials
    ### 321114 Wood Preservation
    'AIES321114EMPUS', # Wood Preservation: Employees
    'AIES321114INFUS', # Wood Preservation: Finished Goods Inventories
    'AIES321114INMUS', # Wood Preservation: Materials and Supplies Inventories
    'AIES321114INVUS', # Wood Preservation: Total Inventories
    'AIES321114INWUS', # Wood Preservation: Work In Process Inventories
    'AIES321114PAYUS', # Wood Preservation: Annual Payroll
    'AIES321114PWEUS', # Wood Preservation: Production Workers
    'AIES321114RCTUS', # Wood Preservation: Shipments
    'AIES321114TCMUS', # Wood Preservation: Total Cost of Materials
    ### 3212 Veneer, Plywood, and Engineered Wood Product Manufacturing
    'AIES3212EMPUS', # Veneer, Plywood, and Engineered Wood Product Manufacturing: Employees
    'AIES3212INFUS', # Veneer, Plywood, and Engineered Wood Product Manufacturing: Finished Goods Inventories
    'AIES3212INMUS', # Veneer, Plywood, and Engineered Wood Product Manufacturing: Materials and Supplies Inventories
    'AIES3212INVUS', # Veneer, Plywood, and Engineered Wood Product Manufacturing: Total Inventories
    'AIES3212INWUS', # Veneer, Plywood, and Engineered Wood Product Manufacturing: Work In Process Inventories
    'AIES3212PAYUS', # Veneer, Plywood, and Engineered Wood Product Manufacturing: Annual Payroll
    'AIES3212PWEUS', # Veneer, Plywood, and Engineered Wood Product Manufacturing: Production Workers
    'AIES3212RCTUS', # Veneer, Plywood, and Engineered Wood Product Manufacturing: Shipments
    'AIES3212TCMUS', # Veneer, Plywood, and Engineered Wood Product Manufacturing: Total Cost of Materials
    ### 321211 Hardwood Veneer and Plywood Manufacturing
    'AIES321211EMPUS', # Hardwood Veneer and Plywood Manufacturing: Employees
    'AIES321211INFUS', # Hardwood Veneer and Plywood Manufacturing: Finished Goods Inventories
    'AIES321211INMUS', # Hardwood Veneer and Plywood Manufacturing: Materials and Supplies Inventories
    'AIES321211INVUS', # Hardwood Veneer and Plywood Manufacturing: Total Inventories
    'AIES321211INWUS', # Hardwood Veneer and Plywood Manufacturing: Work In Process Inventories
    'AIES321211PAYUS', # Hardwood Veneer and Plywood Manufacturing: Annual Payroll
    'AIES321211PWEUS', # Hardwood Veneer and Plywood Manufacturing: Production Workers
    'AIES321211RCTUS', # Hardwood Veneer and Plywood Manufacturing: Shipments
    'AIES321211TCMUS', # Hardwood Veneer and Plywood Manufacturing: Total Cost of Materials
    ### 321212 Softwood Veneer and Plywood Manufacturing
    'AIES321212EMPUS', # Softwood Veneer and Plywood Manufacturing: Employees
    'AIES321212INFUS', # Softwood Veneer and Plywood Manufacturing: Finished Goods Inventories
    'AIES321212INMUS', # Softwood Veneer and Plywood Manufacturing: Materials and Supplies Inventories
    'AIES321212INVUS', # Softwood Veneer and Plywood Manufacturing: Total Inventories
    'AIES321212INWUS', # Softwood Veneer and Plywood Manufacturing: Work In Process Inventories
    'AIES321212PAYUS', # Softwood Veneer and Plywood Manufacturing: Annual Payroll
    'AIES321212PWEUS', # Softwood Veneer and Plywood Manufacturing: Production Workers
    'AIES321212RCTUS', # Softwood Veneer and Plywood Manufacturing: Shipments
    'AIES321212TCMUS', # Softwood Veneer and Plywood Manufacturing: Total Cost of Materials
    ### 321213 Engineered Wood Member (Except Truss) Manufacturing
    'AIES321213EMPUS', # Engineered Wood Member (Except Truss) Manufacturing: Employees
    'AIES321213INFUS', # Engineered Wood Member (Except Truss) Manufacturing: Finished Goods Inventories
    'AIES321213INMUS', # Engineered Wood Member (Except Truss) Manufacturing: Materials and Supplies Inventories
    'AIES321213INVUS', # Engineered Wood Member (Except Truss) Manufacturing: Total Inventories
    'AIES321213INWUS', # Engineered Wood Member (Except Truss) Manufacturing: Work In Process Inventories
    'AIES321213PAYUS', # Engineered Wood Member (Except Truss) Manufacturing: Annual Payroll
    'AIES321213PWEUS', # Engineered Wood Member (Except Truss) Manufacturing: Production Workers
    'AIES321213RCTUS', # Engineered Wood Member (Except Truss) Manufacturing: Shipments
    'AIES321213TCMUS', # Engineered Wood Member (Except Truss) Manufacturing: Total Cost of Materials
    ### 321214 Truss Manufacturing
    'AIES321214EMPUS', # Truss Manufacturing: Employees
    'AIES321214INFUS', # Truss Manufacturing: Finished Goods Inventories
    'AIES321214INMUS', # Truss Manufacturing: Materials and Supplies Inventories
    'AIES321214INVUS', # Truss Manufacturing: Total Inventories
    'AIES321214INWUS', # Truss Manufacturing: Work In Process Inventories
    'AIES321214PAYUS', # Truss Manufacturing: Annual Payroll
    'AIES321214PWEUS', # Truss Manufacturing: Production Workers
    'AIES321214RCTUS', # Truss Manufacturing: Shipments
    'AIES321214TCMUS', # Truss Manufacturing: Total Cost of Materials
    ### 321219 Reconstituted Wood Product Manufacturing
    'AIES321219EMPUS', # Reconstituted Wood Product Manufacturing: Employees
    'AIES321219INFUS', # Reconstituted Wood Product Manufacturing: Finished Goods Inventories
    'AIES321219INMUS', # Reconstituted Wood Product Manufacturing: Materials and Supplies Inventories
    'AIES321219INVUS', # Reconstituted Wood Product Manufacturing: Total Inventories
    'AIES321219INWUS', # Reconstituted Wood Product Manufacturing: Work In Process Inventories
    'AIES321219PAYUS', # Reconstituted Wood Product Manufacturing: Annual Payroll
    'AIES321219PWEUS', # Reconstituted Wood Product Manufacturing: Production Workers
    'AIES321219RCTUS', # Reconstituted Wood Product Manufacturing: Shipments
    'AIES321219TCMUS', # Reconstituted Wood Product Manufacturing: Total Cost of Materials
    ### 3219 Other Wood Product Manufacturing
    'AIES3219EMPUS', # Other Wood Product Manufacturing: Employees
    'AIES3219INFUS', # Other Wood Product Manufacturing: Finished Goods Inventories
    'AIES3219INMUS', # Other Wood Product Manufacturing: Materials and Supplies Inventories
    'AIES3219INVUS', # Other Wood Product Manufacturing: Total Inventories
    'AIES3219INWUS', # Other Wood Product Manufacturing: Work In Process Inventories
    'AIES3219PAYUS', # Other Wood Product Manufacturing: Annual Payroll
    'AIES3219PWEUS', # Other Wood Product Manufacturing: Production Workers
    'AIES3219RCTUS', # Other Wood Product Manufacturing: Shipments
    'AIES3219TCMUS', # Other Wood Product Manufacturing: Total Cost of Materials
    ### 32191 Millwork
    'AIES32191EMPUS', # Millwork: Employees
    'AIES32191INFUS', # Millwork: Finished Goods Inventories
    'AIES32191INMUS', # Millwork: Materials and Supplies Inventories
    'AIES32191INVUS', # Millwork: Total Inventories
    'AIES32191INWUS', # Millwork: Work In Process Inventories
    'AIES32191PAYUS', # Millwork: Annual Payroll
    'AIES32191PWEUS', # Millwork: Production Workers
    'AIES32191RCTUS', # Millwork: Shipments
    'AIES32191TCMUS', # Millwork: Total Cost of Materials
    ### 321911 Wood Window and Door Manufacturing
    'AIES321911EMPUS', # Wood Window and Door Manufacturing: Employees
    'AIES321911INFUS', # Wood Window and Door Manufacturing: Finished Goods Inventories
    'AIES321911INMUS', # Wood Window and Door Manufacturing: Materials and Supplies Inventories
    'AIES321911INVUS', # Wood Window and Door Manufacturing: Total Inventories
    'AIES321911INWUS', # Wood Window and Door Manufacturing: Work In Process Inventories
    'AIES321911PAYUS', # Wood Window and Door Manufacturing: Annual Payroll
    'AIES321911PWEUS', # Wood Window and Door Manufacturing: Production Workers
    'AIES321911RCTUS', # Wood Window and Door Manufacturing: Shipments
    'AIES321911TCMUS', # Wood Window and Door Manufacturing: Total Cost of Materials
    ### 321912 Cut Stock, Resawing Lumber, and Planing
    'AIES321912EMPUS', # Cut Stock, Resawing Lumber, and Planing: Employees
    'AIES321912INFUS', # Cut Stock, Resawing Lumber, and Planing: Finished Goods Inventories
    'AIES321912INMUS', # Cut Stock, Resawing Lumber, and Planing: Materials and Supplies Inventories
    'AIES321912INVUS', # Cut Stock, Resawing Lumber, and Planing: Total Inventories
    'AIES321912INWUS', # Cut Stock, Resawing Lumber, and Planing: Work In Process Inventories
    'AIES321912PAYUS', # Cut Stock, Resawing Lumber, and Planing: Annual Payroll
    'AIES321912PWEUS', # Cut Stock, Resawing Lumber, and Planing: Production Workers
    'AIES321912RCTUS', # Cut Stock, Resawing Lumber, and Planing: Shipments
    'AIES321912TCMUS', # Cut Stock, Resawing Lumber, and Planing: Total Cost of Materials
    ### 321918 Other Millwork (Including Flooring)
    'AIES321918EMPUS', # Other Millwork (Including Flooring): Employees
    'AIES321918INFUS', # Other Millwork (Including Flooring): Finished Goods Inventories
    'AIES321918INMUS', # Other Millwork (Including Flooring): Materials and Supplies Inventories
    'AIES321918INVUS', # Other Millwork (Including Flooring): Total Inventories
    'AIES321918INWUS', # Other Millwork (Including Flooring): Work In Process Inventories
    'AIES321918PAYUS', # Other Millwork (Including Flooring): Annual Payroll
    'AIES321918PWEUS', # Other Millwork (Including Flooring): Production Workers
    'AIES321918RCTUS', # Other Millwork (Including Flooring): Shipments
    'AIES321918TCMUS', # Other Millwork (Including Flooring): Total Cost of Materials
    ### 32192 Wood Container and Pallet Manufacturing
    'AIES32192EMPUS', # Wood Container and Pallet Manufacturing: Employees
    'AIES32192INFUS', # Wood Container and Pallet Manufacturing: Finished Goods Inventories
    'AIES32192INMUS', # Wood Container and Pallet Manufacturing: Materials and Supplies Inventories
    'AIES32192INVUS', # Wood Container and Pallet Manufacturing: Total Inventories
    'AIES32192INWUS', # Wood Container and Pallet Manufacturing: Work In Process Inventories
    'AIES32192PAYUS', # Wood Container and Pallet Manufacturing: Annual Payroll
    'AIES32192PWEUS', # Wood Container and Pallet Manufacturing: Production Workers
    'AIES32192RCTUS', # Wood Container and Pallet Manufacturing: Shipments
    'AIES32192TCMUS', # Wood Container and Pallet Manufacturing: Total Cost of Materials
    ### 32199 All Other Wood Product Manufacturing
    'AIES32199EMPUS', # All Other Wood Product Manufacturing: Employees
    'AIES32199INFUS', # All Other Wood Product Manufacturing: Finished Goods Inventories
    'AIES32199INMUS', # All Other Wood Product Manufacturing: Materials and Supplies Inventories
    'AIES32199INVUS', # All Other Wood Product Manufacturing: Total Inventories
    'AIES32199INWUS', # All Other Wood Product Manufacturing: Work In Process Inventories
    'AIES32199PAYUS', # All Other Wood Product Manufacturing: Annual Payroll
    'AIES32199PWEUS', # All Other Wood Product Manufacturing: Production Workers
    'AIES32199RCTUS', # All Other Wood Product Manufacturing: Shipments
    'AIES32199TCMUS', # All Other Wood Product Manufacturing: Total Cost of Materials
    ### 321991 Manufactured Home (Mobile Home) Manufacturing
    'AIES321991EMPUS', # Manufactured Home (Mobile Home) Manufacturing: Employees
    'AIES321991INFUS', # Manufactured Home (Mobile Home) Manufacturing: Finished Goods Inventories
    'AIES321991INMUS', # Manufactured Home (Mobile Home) Manufacturing: Materials and Supplies Inventories
    'AIES321991INVUS', # Manufactured Home (Mobile Home) Manufacturing: Total Inventories
    'AIES321991INWUS', # Manufactured Home (Mobile Home) Manufacturing: Work In Process Inventories
    'AIES321991PAYUS', # Manufactured Home (Mobile Home) Manufacturing: Annual Payroll
    'AIES321991PWEUS', # Manufactured Home (Mobile Home) Manufacturing: Production Workers
    'AIES321991RCTUS', # Manufactured Home (Mobile Home) Manufacturing: Shipments
    'AIES321991TCMUS', # Manufactured Home (Mobile Home) Manufacturing: Total Cost of Materials
    ### 321992 Prefabricated Wood Building Manufacturing
    'AIES321992EMPUS', # Prefabricated Wood Building Manufacturing: Employees
    'AIES321992INFUS', # Prefabricated Wood Building Manufacturing: Finished Goods Inventories
    'AIES321992INMUS', # Prefabricated Wood Building Manufacturing: Materials and Supplies Inventories
    'AIES321992INVUS', # Prefabricated Wood Building Manufacturing: Total Inventories
    'AIES321992INWUS', # Prefabricated Wood Building Manufacturing: Work In Process Inventories
    'AIES321992PAYUS', # Prefabricated Wood Building Manufacturing: Annual Payroll
    'AIES321992PWEUS', # Prefabricated Wood Building Manufacturing: Production Workers
    'AIES321992RCTUS', # Prefabricated Wood Building Manufacturing: Shipments
    'AIES321992TCMUS', # Prefabricated Wood Building Manufacturing: Total Cost of Materials
    ### 321999 All Other Miscellaneous Wood Product Manufacturing
    'AIES321999EMPUS', # All Other Miscellaneous Wood Product Manufacturing: Employees
    'AIES321999INFUS', # All Other Miscellaneous Wood Product Manufacturing: Finished Goods Inventories
    'AIES321999INMUS', # All Other Miscellaneous Wood Product Manufacturing: Materials and Supplies Inventories
    'AIES321999INVUS', # All Other Miscellaneous Wood Product Manufacturing: Total Inventories
    'AIES321999INWUS', # All Other Miscellaneous Wood Product Manufacturing: Work In Process Inventories
    'AIES321999PAYUS', # All Other Miscellaneous Wood Product Manufacturing: Annual Payroll
    'AIES321999PWEUS', # All Other Miscellaneous Wood Product Manufacturing: Production Workers
    'AIES321999RCTUS', # All Other Miscellaneous Wood Product Manufacturing: Shipments
    'AIES321999TCMUS', # All Other Miscellaneous Wood Product Manufacturing: Total Cost of Materials
    ## NAICS 322 Paper Manufacturing
    ### 322 Paper Manufacturing
    'AIES322EMPUS', # Paper Manufacturing: Employees
    'AIES322INFUS', # Paper Manufacturing: Finished Goods Inventories
    'AIES322INMUS', # Paper Manufacturing: Materials and Supplies Inventories
    'AIES322INVUS', # Paper Manufacturing: Total Inventories
    'AIES322INWUS', # Paper Manufacturing: Work In Process Inventories
    'AIES322PAYUS', # Paper Manufacturing: Annual Payroll
    'AIES322PWEUS', # Paper Manufacturing: Production Workers
    'AIES322RCTUS', # Paper Manufacturing: Shipments
    'AIES322TCMUS', # Paper Manufacturing: Total Cost of Materials
    ### 3221 Pulp, Paper, and Paperboard Mills
    'AIES3221EMPUS', # Pulp, Paper, and Paperboard Mills: Employees
    'AIES3221INFUS', # Pulp, Paper, and Paperboard Mills: Finished Goods Inventories
    'AIES3221INMUS', # Pulp, Paper, and Paperboard Mills: Materials and Supplies Inventories
    'AIES3221INVUS', # Pulp, Paper, and Paperboard Mills: Total Inventories
    'AIES3221INWUS', # Pulp, Paper, and Paperboard Mills: Work In Process Inventories
    'AIES3221PAYUS', # Pulp, Paper, and Paperboard Mills: Annual Payroll
    'AIES3221PWEUS', # Pulp, Paper, and Paperboard Mills: Production Workers
    'AIES3221RCTUS', # Pulp, Paper, and Paperboard Mills: Shipments
    'AIES3221TCMUS', # Pulp, Paper, and Paperboard Mills: Total Cost of Materials
    ### 32211 Pulp Mills
    'AIES32211EMPUS', # Pulp Mills: Employees
    'AIES32211INFUS', # Pulp Mills: Finished Goods Inventories
    'AIES32211INMUS', # Pulp Mills: Materials and Supplies Inventories
    'AIES32211INVUS', # Pulp Mills: Total Inventories
    'AIES32211INWUS', # Pulp Mills: Work In Process Inventories
    'AIES32211PAYUS', # Pulp Mills: Annual Payroll
    'AIES32211PWEUS', # Pulp Mills: Production Workers
    'AIES32211RCTUS', # Pulp Mills: Shipments
    'AIES32211TCMUS', # Pulp Mills: Total Cost of Materials
    ### 32212 Paper Mills
    'AIES32212EMPUS', # Paper Mills: Employees
    'AIES32212INFUS', # Paper Mills: Finished Goods Inventories
    'AIES32212INMUS', # Paper Mills: Materials and Supplies Inventories
    'AIES32212INVUS', # Paper Mills: Total Inventories
    'AIES32212INWUS', # Paper Mills: Work In Process Inventories
    'AIES32212PAYUS', # Paper Mills: Annual Payroll
    'AIES32212PWEUS', # Paper Mills: Production Workers
    'AIES32212RCTUS', # Paper Mills: Shipments
    'AIES32212TCMUS', # Paper Mills: Total Cost of Materials
    ### 322121 Paper (Except Newsprint) Mills
    'AIES322121EMPUS', # Paper (Except Newsprint) Mills: Employees
    'AIES322121INFUS', # Paper (Except Newsprint) Mills: Finished Goods Inventories
    'AIES322121INMUS', # Paper (Except Newsprint) Mills: Materials and Supplies Inventories
    'AIES322121INVUS', # Paper (Except Newsprint) Mills: Total Inventories
    'AIES322121INWUS', # Paper (Except Newsprint) Mills: Work In Process Inventories
    'AIES322121PAYUS', # Paper (Except Newsprint) Mills: Annual Payroll
    'AIES322121PWEUS', # Paper (Except Newsprint) Mills: Production Workers
    'AIES322121RCTUS', # Paper (Except Newsprint) Mills: Shipments
    'AIES322121TCMUS', # Paper (Except Newsprint) Mills: Total Cost of Materials
    ### 322122 Newsprint Mills
    'AIES322122EMPUS', # Newsprint Mills: Employees
    'AIES322122INFUS', # Newsprint Mills: Finished Goods Inventories
    'AIES322122INMUS', # Newsprint Mills: Materials and Supplies Inventories
    'AIES322122INVUS', # Newsprint Mills: Total Inventories
    'AIES322122INWUS', # Newsprint Mills: Work In Process Inventories
    'AIES322122PAYUS', # Newsprint Mills: Annual Payroll
    'AIES322122PWEUS', # Newsprint Mills: Production Workers
    'AIES322122RCTUS', # Newsprint Mills: Shipments
    'AIES322122TCMUS', # Newsprint Mills: Total Cost of Materials
    ### 32213 Paperboard Mills
    'AIES32213EMPUS', # Paperboard Mills: Employees
    'AIES32213INFUS', # Paperboard Mills: Finished Goods Inventories
    'AIES32213INMUS', # Paperboard Mills: Materials and Supplies Inventories
    'AIES32213INVUS', # Paperboard Mills: Total Inventories
    'AIES32213INWUS', # Paperboard Mills: Work In Process Inventories
    'AIES32213PAYUS', # Paperboard Mills: Annual Payroll
    'AIES32213PWEUS', # Paperboard Mills: Production Workers
    'AIES32213RCTUS', # Paperboard Mills: Shipments
    'AIES32213TCMUS', # Paperboard Mills: Total Cost of Materials
    ### 3222 Converted Paper Product Manufacturing
    'AIES3222EMPUS', # Converted Paper Product Manufacturing: Employees
    'AIES3222INFUS', # Converted Paper Product Manufacturing: Finished Goods Inventories
    'AIES3222INMUS', # Converted Paper Product Manufacturing: Materials and Supplies Inventories
    'AIES3222INVUS', # Converted Paper Product Manufacturing: Total Inventories
    'AIES3222INWUS', # Converted Paper Product Manufacturing: Work In Process Inventories
    'AIES3222PAYUS', # Converted Paper Product Manufacturing: Annual Payroll
    'AIES3222PWEUS', # Converted Paper Product Manufacturing: Production Workers
    'AIES3222RCTUS', # Converted Paper Product Manufacturing: Shipments
    'AIES3222TCMUS', # Converted Paper Product Manufacturing: Total Cost of Materials
    ### 32221 Paperboard Container Manufacturing
    'AIES32221EMPUS', # Paperboard Container Manufacturing: Employees
    'AIES32221INFUS', # Paperboard Container Manufacturing: Finished Goods Inventories
    'AIES32221INMUS', # Paperboard Container Manufacturing: Materials and Supplies Inventories
    'AIES32221INVUS', # Paperboard Container Manufacturing: Total Inventories
    'AIES32221INWUS', # Paperboard Container Manufacturing: Work In Process Inventories
    'AIES32221PAYUS', # Paperboard Container Manufacturing: Annual Payroll
    'AIES32221PWEUS', # Paperboard Container Manufacturing: Production Workers
    'AIES32221RCTUS', # Paperboard Container Manufacturing: Shipments
    'AIES32221TCMUS', # Paperboard Container Manufacturing: Total Cost of Materials
    ### 322211 Corrugated and Solid Fiber Box Manufacturing
    'AIES322211EMPUS', # Corrugated and Solid Fiber Box Manufacturing: Employees
    'AIES322211INFUS', # Corrugated and Solid Fiber Box Manufacturing: Finished Goods Inventories
    'AIES322211INMUS', # Corrugated and Solid Fiber Box Manufacturing: Materials and Supplies Inventories
    'AIES322211INVUS', # Corrugated and Solid Fiber Box Manufacturing: Total Inventories
    'AIES322211INWUS', # Corrugated and Solid Fiber Box Manufacturing: Work In Process Inventories
    'AIES322211PAYUS', # Corrugated and Solid Fiber Box Manufacturing: Annual Payroll
    'AIES322211PWEUS', # Corrugated and Solid Fiber Box Manufacturing: Production Workers
    'AIES322211RCTUS', # Corrugated and Solid Fiber Box Manufacturing: Shipments
    'AIES322211TCMUS', # Corrugated and Solid Fiber Box Manufacturing: Total Cost of Materials
    ### 322212 Folding Paperboard Box Manufacturing
    'AIES322212EMPUS', # Folding Paperboard Box Manufacturing: Employees
    'AIES322212INFUS', # Folding Paperboard Box Manufacturing: Finished Goods Inventories
    'AIES322212INMUS', # Folding Paperboard Box Manufacturing: Materials and Supplies Inventories
    'AIES322212INVUS', # Folding Paperboard Box Manufacturing: Total Inventories
    'AIES322212INWUS', # Folding Paperboard Box Manufacturing: Work In Process Inventories
    'AIES322212PAYUS', # Folding Paperboard Box Manufacturing: Annual Payroll
    'AIES322212PWEUS', # Folding Paperboard Box Manufacturing: Production Workers
    'AIES322212RCTUS', # Folding Paperboard Box Manufacturing: Shipments
    'AIES322212TCMUS', # Folding Paperboard Box Manufacturing: Total Cost of Materials
    ### 322219 Other Paperboard Container Manufacturing
    'AIES322219EMPUS', # Other Paperboard Container Manufacturing: Employees
    'AIES322219INFUS', # Other Paperboard Container Manufacturing: Finished Goods Inventories
    'AIES322219INMUS', # Other Paperboard Container Manufacturing: Materials and Supplies Inventories
    'AIES322219INVUS', # Other Paperboard Container Manufacturing: Total Inventories
    'AIES322219INWUS', # Other Paperboard Container Manufacturing: Work In Process Inventories
    'AIES322219PAYUS', # Other Paperboard Container Manufacturing: Annual Payroll
    'AIES322219PWEUS', # Other Paperboard Container Manufacturing: Production Workers
    'AIES322219RCTUS', # Other Paperboard Container Manufacturing: Shipments
    'AIES322219TCMUS', # Other Paperboard Container Manufacturing: Total Cost of Materials
    ### 32222 Paper Bag and Coated and Treated Paper Manufacturing
    'AIES32222EMPUS', # Paper Bag and Coated and Treated Paper Manufacturing: Employees
    'AIES32222INFUS', # Paper Bag and Coated and Treated Paper Manufacturing: Finished Goods Inventories
    'AIES32222INMUS', # Paper Bag and Coated and Treated Paper Manufacturing: Materials and Supplies Inventories
    'AIES32222INVUS', # Paper Bag and Coated and Treated Paper Manufacturing: Total Inventories
    'AIES32222INWUS', # Paper Bag and Coated and Treated Paper Manufacturing: Work In Process Inventories
    'AIES32222PAYUS', # Paper Bag and Coated and Treated Paper Manufacturing: Annual Payroll
    'AIES32222PWEUS', # Paper Bag and Coated and Treated Paper Manufacturing: Production Workers
    'AIES32222RCTUS', # Paper Bag and Coated and Treated Paper Manufacturing: Shipments
    'AIES32222TCMUS', # Paper Bag and Coated and Treated Paper Manufacturing: Total Cost of Materials
    ### 32223 Stationery Product Manufacturing
    'AIES32223EMPUS', # Stationery Product Manufacturing: Employees
    'AIES32223INFUS', # Stationery Product Manufacturing: Finished Goods Inventories
    'AIES32223INMUS', # Stationery Product Manufacturing: Materials and Supplies Inventories
    'AIES32223INVUS', # Stationery Product Manufacturing: Total Inventories
    'AIES32223INWUS', # Stationery Product Manufacturing: Work In Process Inventories
    'AIES32223PAYUS', # Stationery Product Manufacturing: Annual Payroll
    'AIES32223PWEUS', # Stationery Product Manufacturing: Production Workers
    'AIES32223RCTUS', # Stationery Product Manufacturing: Shipments
    'AIES32223TCMUS', # Stationery Product Manufacturing: Total Cost of Materials
    ### 32229 Other Converted Paper Product Manufacturing
    'AIES32229EMPUS', # Other Converted Paper Product Manufacturing: Employees
    'AIES32229INFUS', # Other Converted Paper Product Manufacturing: Finished Goods Inventories
    'AIES32229INMUS', # Other Converted Paper Product Manufacturing: Materials and Supplies Inventories
    'AIES32229INVUS', # Other Converted Paper Product Manufacturing: Total Inventories
    'AIES32229INWUS', # Other Converted Paper Product Manufacturing: Work In Process Inventories
    'AIES32229PAYUS', # Other Converted Paper Product Manufacturing: Annual Payroll
    'AIES32229PWEUS', # Other Converted Paper Product Manufacturing: Production Workers
    'AIES32229RCTUS', # Other Converted Paper Product Manufacturing: Shipments
    'AIES32229TCMUS', # Other Converted Paper Product Manufacturing: Total Cost of Materials
    ### 322291 Sanitary Paper Product Manufacturing
    'AIES322291EMPUS', # Sanitary Paper Product Manufacturing: Employees
    'AIES322291INFUS', # Sanitary Paper Product Manufacturing: Finished Goods Inventories
    'AIES322291INMUS', # Sanitary Paper Product Manufacturing: Materials and Supplies Inventories
    'AIES322291INVUS', # Sanitary Paper Product Manufacturing: Total Inventories
    'AIES322291INWUS', # Sanitary Paper Product Manufacturing: Work In Process Inventories
    'AIES322291PAYUS', # Sanitary Paper Product Manufacturing: Annual Payroll
    'AIES322291PWEUS', # Sanitary Paper Product Manufacturing: Production Workers
    'AIES322291RCTUS', # Sanitary Paper Product Manufacturing: Shipments
    'AIES322291TCMUS', # Sanitary Paper Product Manufacturing: Total Cost of Materials
    ### 322299 All Other Converted Paper Product Manufacturing
    'AIES322299EMPUS', # All Other Converted Paper Product Manufacturing: Employees
    'AIES322299INFUS', # All Other Converted Paper Product Manufacturing: Finished Goods Inventories
    'AIES322299INMUS', # All Other Converted Paper Product Manufacturing: Materials and Supplies Inventories
    'AIES322299INVUS', # All Other Converted Paper Product Manufacturing: Total Inventories
    'AIES322299INWUS', # All Other Converted Paper Product Manufacturing: Work In Process Inventories
    'AIES322299PAYUS', # All Other Converted Paper Product Manufacturing: Annual Payroll
    'AIES322299PWEUS', # All Other Converted Paper Product Manufacturing: Production Workers
    'AIES322299RCTUS', # All Other Converted Paper Product Manufacturing: Shipments
    'AIES322299TCMUS', # All Other Converted Paper Product Manufacturing: Total Cost of Materials
    ## NAICS 323 Printing and Related Support Activities
    ### 323 Printing and Related Support Activities
    'AIES323EMPUS', # Printing and Related Support Activities: Employees
    'AIES323INFUS', # Printing and Related Support Activities: Finished Goods Inventories
    'AIES323INMUS', # Printing and Related Support Activities: Materials and Supplies Inventories
    'AIES323INVUS', # Printing and Related Support Activities: Total Inventories
    'AIES323INWUS', # Printing and Related Support Activities: Work In Process Inventories
    'AIES323PAYUS', # Printing and Related Support Activities: Annual Payroll
    'AIES323PWEUS', # Printing and Related Support Activities: Production Workers
    'AIES323RCTUS', # Printing and Related Support Activities: Shipments
    'AIES323TCMUS', # Printing and Related Support Activities: Total Cost of Materials
    ### 32311 Printing
    'AIES32311EMPUS', # Printing: Employees
    'AIES32311INFUS', # Printing: Finished Goods Inventories
    'AIES32311INMUS', # Printing: Materials and Supplies Inventories
    'AIES32311INVUS', # Printing: Total Inventories
    'AIES32311INWUS', # Printing: Work In Process Inventories
    'AIES32311PAYUS', # Printing: Annual Payroll
    'AIES32311PWEUS', # Printing: Production Workers
    'AIES32311RCTUS', # Printing: Shipments
    'AIES32311TCMUS', # Printing: Total Cost of Materials
    ### 323111 Commercial Printing (Except Screen and Books)
    'AIES323111EMPUS', # Commercial Printing (Except Screen and Books): Employees
    'AIES323111INFUS', # Commercial Printing (Except Screen and Books): Finished Goods Inventories
    'AIES323111INMUS', # Commercial Printing (Except Screen and Books): Materials and Supplies Inventories
    'AIES323111INVUS', # Commercial Printing (Except Screen and Books): Total Inventories
    'AIES323111INWUS', # Commercial Printing (Except Screen and Books): Work In Process Inventories
    'AIES323111PAYUS', # Commercial Printing (Except Screen and Books): Annual Payroll
    'AIES323111PWEUS', # Commercial Printing (Except Screen and Books): Production Workers
    'AIES323111RCTUS', # Commercial Printing (Except Screen and Books): Shipments
    'AIES323111TCMUS', # Commercial Printing (Except Screen and Books): Total Cost of Materials
    ### 323113 Commercial Screen Printing
    'AIES323113EMPUS', # Commercial Screen Printing: Employees
    'AIES323113INFUS', # Commercial Screen Printing: Finished Goods Inventories
    'AIES323113INMUS', # Commercial Screen Printing: Materials and Supplies Inventories
    'AIES323113INVUS', # Commercial Screen Printing: Total Inventories
    'AIES323113INWUS', # Commercial Screen Printing: Work In Process Inventories
    'AIES323113PAYUS', # Commercial Screen Printing: Annual Payroll
    'AIES323113PWEUS', # Commercial Screen Printing: Production Workers
    'AIES323113RCTUS', # Commercial Screen Printing: Shipments
    'AIES323113TCMUS', # Commercial Screen Printing: Total Cost of Materials
    ### 323117 Books Printing
    'AIES323117EMPUS', # Books Printing: Employees
    'AIES323117INFUS', # Books Printing: Finished Goods Inventories
    'AIES323117INMUS', # Books Printing: Materials and Supplies Inventories
    'AIES323117INVUS', # Books Printing: Total Inventories
    'AIES323117INWUS', # Books Printing: Work In Process Inventories
    'AIES323117PAYUS', # Books Printing: Annual Payroll
    'AIES323117PWEUS', # Books Printing: Production Workers
    'AIES323117RCTUS', # Books Printing: Shipments
    'AIES323117TCMUS', # Books Printing: Total Cost of Materials
    ### 32312 Support Activities For Printing
    'AIES32312EMPUS', # Support Activities For Printing: Employees
    'AIES32312INFUS', # Support Activities For Printing: Finished Goods Inventories
    'AIES32312INMUS', # Support Activities For Printing: Materials and Supplies Inventories
    'AIES32312INVUS', # Support Activities For Printing: Total Inventories
    'AIES32312INWUS', # Support Activities For Printing: Work In Process Inventories
    'AIES32312PAYUS', # Support Activities For Printing: Annual Payroll
    'AIES32312PWEUS', # Support Activities For Printing: Production Workers
    'AIES32312RCTUS', # Support Activities For Printing: Shipments
    'AIES32312TCMUS', # Support Activities For Printing: Total Cost of Materials
    ## NAICS 324 Petroleum and Coal Products Manufacturing
    ### 324 Petroleum and Coal Products Manufacturing
    'AIES324EMPUS', # Petroleum and Coal Products Manufacturing: Employees
    'AIES324INFUS', # Petroleum and Coal Products Manufacturing: Finished Goods Inventories
    'AIES324INMUS', # Petroleum and Coal Products Manufacturing: Materials and Supplies Inventories
    'AIES324INVUS', # Petroleum and Coal Products Manufacturing: Total Inventories
    'AIES324INWUS', # Petroleum and Coal Products Manufacturing: Work In Process Inventories
    'AIES324PAYUS', # Petroleum and Coal Products Manufacturing: Annual Payroll
    'AIES324PWEUS', # Petroleum and Coal Products Manufacturing: Production Workers
    'AIES324RCTUS', # Petroleum and Coal Products Manufacturing: Shipments
    'AIES324TCMUS', # Petroleum and Coal Products Manufacturing: Total Cost of Materials
    ### 32411 Petroleum Refineries
    'AIES32411EMPUS', # Petroleum Refineries: Employees
    'AIES32411INFUS', # Petroleum Refineries: Finished Goods Inventories
    'AIES32411INMUS', # Petroleum Refineries: Materials and Supplies Inventories
    'AIES32411INVUS', # Petroleum Refineries: Total Inventories
    'AIES32411INWUS', # Petroleum Refineries: Work In Process Inventories
    'AIES32411PAYUS', # Petroleum Refineries: Annual Payroll
    'AIES32411PWEUS', # Petroleum Refineries: Production Workers
    'AIES32411RCTUS', # Petroleum Refineries: Shipments
    'AIES32411TCMUS', # Petroleum Refineries: Total Cost of Materials
    ### 32412 Asphalt Paving, Roofing, and Saturated Materials Manufacturing
    'AIES32412EMPUS', # Asphalt Paving, Roofing, and Saturated Materials Manufacturing: Employees
    'AIES32412INFUS', # Asphalt Paving, Roofing, and Saturated Materials Manufacturing: Finished Goods Inventories
    'AIES32412INMUS', # Asphalt Paving, Roofing, and Saturated Materials Manufacturing: Materials and Supplies Inventories
    'AIES32412INVUS', # Asphalt Paving, Roofing, and Saturated Materials Manufacturing: Total Inventories
    'AIES32412INWUS', # Asphalt Paving, Roofing, and Saturated Materials Manufacturing: Work In Process Inventories
    'AIES32412PAYUS', # Asphalt Paving, Roofing, and Saturated Materials Manufacturing: Annual Payroll
    'AIES32412PWEUS', # Asphalt Paving, Roofing, and Saturated Materials Manufacturing: Production Workers
    'AIES32412RCTUS', # Asphalt Paving, Roofing, and Saturated Materials Manufacturing: Shipments
    'AIES32412TCMUS', # Asphalt Paving, Roofing, and Saturated Materials Manufacturing: Total Cost of Materials
    ### 324121 Asphalt Paving Mixture and Block Manufacturing
    'AIES324121EMPUS', # Asphalt Paving Mixture and Block Manufacturing: Employees
    'AIES324121INFUS', # Asphalt Paving Mixture and Block Manufacturing: Finished Goods Inventories
    'AIES324121INMUS', # Asphalt Paving Mixture and Block Manufacturing: Materials and Supplies Inventories
    'AIES324121INVUS', # Asphalt Paving Mixture and Block Manufacturing: Total Inventories
    'AIES324121INWUS', # Asphalt Paving Mixture and Block Manufacturing: Work In Process Inventories
    'AIES324121PAYUS', # Asphalt Paving Mixture and Block Manufacturing: Annual Payroll
    'AIES324121PWEUS', # Asphalt Paving Mixture and Block Manufacturing: Production Workers
    'AIES324121RCTUS', # Asphalt Paving Mixture and Block Manufacturing: Shipments
    'AIES324121TCMUS', # Asphalt Paving Mixture and Block Manufacturing: Total Cost of Materials
    ### 324122 Asphalt Shingle and Coating Materials Manufacturing
    'AIES324122EMPUS', # Asphalt Shingle and Coating Materials Manufacturing: Employees
    'AIES324122INFUS', # Asphalt Shingle and Coating Materials Manufacturing: Finished Goods Inventories
    'AIES324122INMUS', # Asphalt Shingle and Coating Materials Manufacturing: Materials and Supplies Inventories
    'AIES324122INVUS', # Asphalt Shingle and Coating Materials Manufacturing: Total Inventories
    'AIES324122INWUS', # Asphalt Shingle and Coating Materials Manufacturing: Work In Process Inventories
    'AIES324122PAYUS', # Asphalt Shingle and Coating Materials Manufacturing: Annual Payroll
    'AIES324122PWEUS', # Asphalt Shingle and Coating Materials Manufacturing: Production Workers
    'AIES324122RCTUS', # Asphalt Shingle and Coating Materials Manufacturing: Shipments
    'AIES324122TCMUS', # Asphalt Shingle and Coating Materials Manufacturing: Total Cost of Materials
    ### 32419 Other Petroleum and Coal Products Manufacturing
    'AIES32419EMPUS', # Other Petroleum and Coal Products Manufacturing: Employees
    'AIES32419INFUS', # Other Petroleum and Coal Products Manufacturing: Finished Goods Inventories
    'AIES32419INMUS', # Other Petroleum and Coal Products Manufacturing: Materials and Supplies Inventories
    'AIES32419INVUS', # Other Petroleum and Coal Products Manufacturing: Total Inventories
    'AIES32419INWUS', # Other Petroleum and Coal Products Manufacturing: Work In Process Inventories
    'AIES32419PAYUS', # Other Petroleum and Coal Products Manufacturing: Annual Payroll
    'AIES32419PWEUS', # Other Petroleum and Coal Products Manufacturing: Production Workers
    'AIES32419RCTUS', # Other Petroleum and Coal Products Manufacturing: Shipments
    'AIES32419TCMUS', # Other Petroleum and Coal Products Manufacturing: Total Cost of Materials
    ### 324191 Petroleum Lubricating Oil and Grease Manufacturing
    'AIES324191EMPUS', # Petroleum Lubricating Oil and Grease Manufacturing: Employees
    'AIES324191INFUS', # Petroleum Lubricating Oil and Grease Manufacturing: Finished Goods Inventories
    'AIES324191INMUS', # Petroleum Lubricating Oil and Grease Manufacturing: Materials and Supplies Inventories
    'AIES324191INVUS', # Petroleum Lubricating Oil and Grease Manufacturing: Total Inventories
    'AIES324191INWUS', # Petroleum Lubricating Oil and Grease Manufacturing: Work In Process Inventories
    'AIES324191PAYUS', # Petroleum Lubricating Oil and Grease Manufacturing: Annual Payroll
    'AIES324191PWEUS', # Petroleum Lubricating Oil and Grease Manufacturing: Production Workers
    'AIES324191RCTUS', # Petroleum Lubricating Oil and Grease Manufacturing: Shipments
    'AIES324191TCMUS', # Petroleum Lubricating Oil and Grease Manufacturing: Total Cost of Materials
    ### 324199 All Other Petroleum and Coal Products Manufacturing
    'AIES324199EMPUS', # All Other Petroleum and Coal Products Manufacturing: Employees
    'AIES324199INFUS', # All Other Petroleum and Coal Products Manufacturing: Finished Goods Inventories
    'AIES324199INMUS', # All Other Petroleum and Coal Products Manufacturing: Materials and Supplies Inventories
    'AIES324199INVUS', # All Other Petroleum and Coal Products Manufacturing: Total Inventories
    'AIES324199INWUS', # All Other Petroleum and Coal Products Manufacturing: Work In Process Inventories
    'AIES324199PAYUS', # All Other Petroleum and Coal Products Manufacturing: Annual Payroll
    'AIES324199PWEUS', # All Other Petroleum and Coal Products Manufacturing: Production Workers
    'AIES324199RCTUS', # All Other Petroleum and Coal Products Manufacturing: Shipments
    'AIES324199TCMUS', # All Other Petroleum and Coal Products Manufacturing: Total Cost of Materials
    ## NAICS 325 Chemical Manufacturing
    ### 325 Chemical Manufacturing
    'AIES325EMPUS', # Chemical Manufacturing: Employees
    'AIES325INFUS', # Chemical Manufacturing: Finished Goods Inventories
    'AIES325INMUS', # Chemical Manufacturing: Materials and Supplies Inventories
    'AIES325INVUS', # Chemical Manufacturing: Total Inventories
    'AIES325INWUS', # Chemical Manufacturing: Work In Process Inventories
    'AIES325PAYUS', # Chemical Manufacturing: Annual Payroll
    'AIES325PWEUS', # Chemical Manufacturing: Production Workers
    'AIES325RCTUS', # Chemical Manufacturing: Shipments
    'AIES325TCMUS', # Chemical Manufacturing: Total Cost of Materials
    ### 3251 Basic Chemical Manufacturing
    'AIES3251EMPUS', # Basic Chemical Manufacturing: Employees
    'AIES3251INFUS', # Basic Chemical Manufacturing: Finished Goods Inventories
    'AIES3251INMUS', # Basic Chemical Manufacturing: Materials and Supplies Inventories
    'AIES3251INVUS', # Basic Chemical Manufacturing: Total Inventories
    'AIES3251INWUS', # Basic Chemical Manufacturing: Work In Process Inventories
    'AIES3251PAYUS', # Basic Chemical Manufacturing: Annual Payroll
    'AIES3251PWEUS', # Basic Chemical Manufacturing: Production Workers
    'AIES3251RCTUS', # Basic Chemical Manufacturing: Shipments
    'AIES3251TCMUS', # Basic Chemical Manufacturing: Total Cost of Materials
    ### 32511 Petrochemical Manufacturing
    'AIES32511EMPUS', # Petrochemical Manufacturing: Employees
    'AIES32511INFUS', # Petrochemical Manufacturing: Finished Goods Inventories
    'AIES32511INMUS', # Petrochemical Manufacturing: Materials and Supplies Inventories
    'AIES32511INVUS', # Petrochemical Manufacturing: Total Inventories
    'AIES32511INWUS', # Petrochemical Manufacturing: Work In Process Inventories
    'AIES32511PAYUS', # Petrochemical Manufacturing: Annual Payroll
    'AIES32511PWEUS', # Petrochemical Manufacturing: Production Workers
    'AIES32511RCTUS', # Petrochemical Manufacturing: Shipments
    'AIES32511TCMUS', # Petrochemical Manufacturing: Total Cost of Materials
    ### 32512 Industrial Gas Manufacturing
    'AIES32512EMPUS', # Industrial Gas Manufacturing: Employees
    'AIES32512INFUS', # Industrial Gas Manufacturing: Finished Goods Inventories
    'AIES32512INMUS', # Industrial Gas Manufacturing: Materials and Supplies Inventories
    'AIES32512INVUS', # Industrial Gas Manufacturing: Total Inventories
    'AIES32512INWUS', # Industrial Gas Manufacturing: Work In Process Inventories
    'AIES32512PAYUS', # Industrial Gas Manufacturing: Annual Payroll
    'AIES32512PWEUS', # Industrial Gas Manufacturing: Production Workers
    'AIES32512RCTUS', # Industrial Gas Manufacturing: Shipments
    'AIES32512TCMUS', # Industrial Gas Manufacturing: Total Cost of Materials
    ### 32513 Synthetic Dye and Pigment Manufacturing
    'AIES32513EMPUS', # Synthetic Dye and Pigment Manufacturing: Employees
    'AIES32513INFUS', # Synthetic Dye and Pigment Manufacturing: Finished Goods Inventories
    'AIES32513INMUS', # Synthetic Dye and Pigment Manufacturing: Materials and Supplies Inventories
    'AIES32513INVUS', # Synthetic Dye and Pigment Manufacturing: Total Inventories
    'AIES32513INWUS', # Synthetic Dye and Pigment Manufacturing: Work In Process Inventories
    'AIES32513PAYUS', # Synthetic Dye and Pigment Manufacturing: Annual Payroll
    'AIES32513PWEUS', # Synthetic Dye and Pigment Manufacturing: Production Workers
    'AIES32513RCTUS', # Synthetic Dye and Pigment Manufacturing: Shipments
    'AIES32513TCMUS', # Synthetic Dye and Pigment Manufacturing: Total Cost of Materials
    ### 32518 Other Basic Inorganic Chemical Manufacturing
    'AIES32518EMPUS', # Other Basic Inorganic Chemical Manufacturing: Employees
    'AIES32518INFUS', # Other Basic Inorganic Chemical Manufacturing: Finished Goods Inventories
    'AIES32518INMUS', # Other Basic Inorganic Chemical Manufacturing: Materials and Supplies Inventories
    'AIES32518INVUS', # Other Basic Inorganic Chemical Manufacturing: Total Inventories
    'AIES32518INWUS', # Other Basic Inorganic Chemical Manufacturing: Work In Process Inventories
    'AIES32518PAYUS', # Other Basic Inorganic Chemical Manufacturing: Annual Payroll
    'AIES32518PWEUS', # Other Basic Inorganic Chemical Manufacturing: Production Workers
    'AIES32518RCTUS', # Other Basic Inorganic Chemical Manufacturing: Shipments
    'AIES32518TCMUS', # Other Basic Inorganic Chemical Manufacturing: Total Cost of Materials
    ### 32519 Other Basic Organic Chemical Manufacturing
    'AIES32519EMPUS', # Other Basic Organic Chemical Manufacturing: Employees
    'AIES32519INFUS', # Other Basic Organic Chemical Manufacturing: Finished Goods Inventories
    'AIES32519INMUS', # Other Basic Organic Chemical Manufacturing: Materials and Supplies Inventories
    'AIES32519INVUS', # Other Basic Organic Chemical Manufacturing: Total Inventories
    'AIES32519INWUS', # Other Basic Organic Chemical Manufacturing: Work In Process Inventories
    'AIES32519PAYUS', # Other Basic Organic Chemical Manufacturing: Annual Payroll
    'AIES32519PWEUS', # Other Basic Organic Chemical Manufacturing: Production Workers
    'AIES32519RCTUS', # Other Basic Organic Chemical Manufacturing: Shipments
    'AIES32519TCMUS', # Other Basic Organic Chemical Manufacturing: Total Cost of Materials
    ### 325193 Ethyl Alcohol Manufacturing
    'AIES325193EMPUS', # Ethyl Alcohol Manufacturing: Employees
    'AIES325193INFUS', # Ethyl Alcohol Manufacturing: Finished Goods Inventories
    'AIES325193INMUS', # Ethyl Alcohol Manufacturing: Materials and Supplies Inventories
    'AIES325193INVUS', # Ethyl Alcohol Manufacturing: Total Inventories
    'AIES325193INWUS', # Ethyl Alcohol Manufacturing: Work In Process Inventories
    'AIES325193PAYUS', # Ethyl Alcohol Manufacturing: Annual Payroll
    'AIES325193PWEUS', # Ethyl Alcohol Manufacturing: Production Workers
    'AIES325193RCTUS', # Ethyl Alcohol Manufacturing: Shipments
    'AIES325193TCMUS', # Ethyl Alcohol Manufacturing: Total Cost of Materials
    ### 325194 Cyclic Crude, Intermediate, Wood Chemical Manufacturing
    'AIES325194EMPUS', # Cyclic Crude, Intermediate, Wood Chemical Manufacturing: Employees
    'AIES325194INFUS', # Cyclic Crude, Intermediate, Wood Chemical Manufacturing: Finished Goods Inventories
    'AIES325194INMUS', # Cyclic Crude, Intermediate, Wood Chemical Manufacturing: Materials and Supplies Inventories
    'AIES325194INVUS', # Cyclic Crude, Intermediate, Wood Chemical Manufacturing: Total Inventories
    'AIES325194INWUS', # Cyclic Crude, Intermediate, Wood Chemical Manufacturing: Work In Process Inventories
    'AIES325194PAYUS', # Cyclic Crude, Intermediate, Wood Chemical Manufacturing: Annual Payroll
    'AIES325194PWEUS', # Cyclic Crude, Intermediate, Wood Chemical Manufacturing: Production Workers
    'AIES325194RCTUS', # Cyclic Crude, Intermediate, Wood Chemical Manufacturing: Shipments
    'AIES325194TCMUS', # Cyclic Crude, Intermediate, Wood Chemical Manufacturing: Total Cost of Materials
    ### 325199 All Other Basic Organic Chemical Manufacturing
    'AIES325199EMPUS', # All Other Basic Organic Chemical Manufacturing: Employees
    'AIES325199INFUS', # All Other Basic Organic Chemical Manufacturing: Finished Goods Inventories
    'AIES325199INMUS', # All Other Basic Organic Chemical Manufacturing: Materials and Supplies Inventories
    'AIES325199INVUS', # All Other Basic Organic Chemical Manufacturing: Total Inventories
    'AIES325199INWUS', # All Other Basic Organic Chemical Manufacturing: Work In Process Inventories
    'AIES325199PAYUS', # All Other Basic Organic Chemical Manufacturing: Annual Payroll
    'AIES325199PWEUS', # All Other Basic Organic Chemical Manufacturing: Production Workers
    'AIES325199RCTUS', # All Other Basic Organic Chemical Manufacturing: Shipments
    'AIES325199TCMUS', # All Other Basic Organic Chemical Manufacturing: Total Cost of Materials
    ### 3252 Resin, Rubber, and Artificial Fibers Manufacturing
    'AIES3252EMPUS', # Resin, Rubber, and Artificial Fibers Manufacturing: Employees
    'AIES3252INFUS', # Resin, Rubber, and Artificial Fibers Manufacturing: Finished Goods Inventories
    'AIES3252INMUS', # Resin, Rubber, and Artificial Fibers Manufacturing: Materials and Supplies Inventories
    'AIES3252INVUS', # Resin, Rubber, and Artificial Fibers Manufacturing: Total Inventories
    'AIES3252INWUS', # Resin, Rubber, and Artificial Fibers Manufacturing: Work In Process Inventories
    'AIES3252PAYUS', # Resin, Rubber, and Artificial Fibers Manufacturing: Annual Payroll
    'AIES3252PWEUS', # Resin, Rubber, and Artificial Fibers Manufacturing: Production Workers
    'AIES3252RCTUS', # Resin, Rubber, and Artificial Fibers Manufacturing: Shipments
    'AIES3252TCMUS', # Resin, Rubber, and Artificial Fibers Manufacturing: Total Cost of Materials
    ### 32521 Resin and Synthetic Rubber Manufacturing
    'AIES32521EMPUS', # Resin and Synthetic Rubber Manufacturing: Employees
    'AIES32521INFUS', # Resin and Synthetic Rubber Manufacturing: Finished Goods Inventories
    'AIES32521INMUS', # Resin and Synthetic Rubber Manufacturing: Materials and Supplies Inventories
    'AIES32521INVUS', # Resin and Synthetic Rubber Manufacturing: Total Inventories
    'AIES32521INWUS', # Resin and Synthetic Rubber Manufacturing: Work In Process Inventories
    'AIES32521PAYUS', # Resin and Synthetic Rubber Manufacturing: Annual Payroll
    'AIES32521PWEUS', # Resin and Synthetic Rubber Manufacturing: Production Workers
    'AIES32521RCTUS', # Resin and Synthetic Rubber Manufacturing: Shipments
    'AIES32521TCMUS', # Resin and Synthetic Rubber Manufacturing: Total Cost of Materials
    ### 325211 Plastics Material and Resin Manufacturing
    'AIES325211EMPUS', # Plastics Material and Resin Manufacturing: Employees
    'AIES325211INFUS', # Plastics Material and Resin Manufacturing: Finished Goods Inventories
    'AIES325211INMUS', # Plastics Material and Resin Manufacturing: Materials and Supplies Inventories
    'AIES325211INVUS', # Plastics Material and Resin Manufacturing: Total Inventories
    'AIES325211INWUS', # Plastics Material and Resin Manufacturing: Work In Process Inventories
    'AIES325211PAYUS', # Plastics Material and Resin Manufacturing: Annual Payroll
    'AIES325211PWEUS', # Plastics Material and Resin Manufacturing: Production Workers
    'AIES325211RCTUS', # Plastics Material and Resin Manufacturing: Shipments
    'AIES325211TCMUS', # Plastics Material and Resin Manufacturing: Total Cost of Materials
    ### 325212 Synthetic Rubber Manufacturing
    'AIES325212EMPUS', # Synthetic Rubber Manufacturing: Employees
    'AIES325212INFUS', # Synthetic Rubber Manufacturing: Finished Goods Inventories
    'AIES325212INMUS', # Synthetic Rubber Manufacturing: Materials and Supplies Inventories
    'AIES325212INVUS', # Synthetic Rubber Manufacturing: Total Inventories
    'AIES325212INWUS', # Synthetic Rubber Manufacturing: Work In Process Inventories
    'AIES325212PAYUS', # Synthetic Rubber Manufacturing: Annual Payroll
    'AIES325212PWEUS', # Synthetic Rubber Manufacturing: Production Workers
    'AIES325212RCTUS', # Synthetic Rubber Manufacturing: Shipments
    'AIES325212TCMUS', # Synthetic Rubber Manufacturing: Total Cost of Materials
    ### 32522 Artificial and Synthetic Fibers and Filaments Manufacturing
    'AIES32522EMPUS', # Artificial and Synthetic Fibers and Filaments Manufacturing: Employees
    'AIES32522INFUS', # Artificial and Synthetic Fibers and Filaments Manufacturing: Finished Goods Inventories
    'AIES32522INMUS', # Artificial and Synthetic Fibers and Filaments Manufacturing: Materials and Supplies Inventories
    'AIES32522INVUS', # Artificial and Synthetic Fibers and Filaments Manufacturing: Total Inventories
    'AIES32522INWUS', # Artificial and Synthetic Fibers and Filaments Manufacturing: Work In Process Inventories
    'AIES32522PAYUS', # Artificial and Synthetic Fibers and Filaments Manufacturing: Annual Payroll
    'AIES32522PWEUS', # Artificial and Synthetic Fibers and Filaments Manufacturing: Production Workers
    'AIES32522RCTUS', # Artificial and Synthetic Fibers and Filaments Manufacturing: Shipments
    'AIES32522TCMUS', # Artificial and Synthetic Fibers and Filaments Manufacturing: Total Cost of Materials
    ### 3253 Agricultural Chemical Manufacturing
    'AIES3253EMPUS', # Agricultural Chemical Manufacturing: Employees
    'AIES3253INFUS', # Agricultural Chemical Manufacturing: Finished Goods Inventories
    'AIES3253INMUS', # Agricultural Chemical Manufacturing: Materials and Supplies Inventories
    'AIES3253INVUS', # Agricultural Chemical Manufacturing: Total Inventories
    'AIES3253INWUS', # Agricultural Chemical Manufacturing: Work In Process Inventories
    'AIES3253PAYUS', # Agricultural Chemical Manufacturing: Annual Payroll
    'AIES3253PWEUS', # Agricultural Chemical Manufacturing: Production Workers
    'AIES3253RCTUS', # Agricultural Chemical Manufacturing: Shipments
    'AIES3253TCMUS', # Agricultural Chemical Manufacturing: Total Cost of Materials
    ### 32531 Fertilizer Manufacturing
    'AIES32531EMPUS', # Fertilizer Manufacturing: Employees
    'AIES32531INFUS', # Fertilizer Manufacturing: Finished Goods Inventories
    'AIES32531INMUS', # Fertilizer Manufacturing: Materials and Supplies Inventories
    'AIES32531INVUS', # Fertilizer Manufacturing: Total Inventories
    'AIES32531INWUS', # Fertilizer Manufacturing: Work In Process Inventories
    'AIES32531PAYUS', # Fertilizer Manufacturing: Annual Payroll
    'AIES32531PWEUS', # Fertilizer Manufacturing: Production Workers
    'AIES32531RCTUS', # Fertilizer Manufacturing: Shipments
    'AIES32531TCMUS', # Fertilizer Manufacturing: Total Cost of Materials
    ### 325311 Nitrogenous Fertilizer Manufacturing
    'AIES325311EMPUS', # Nitrogenous Fertilizer Manufacturing: Employees
    'AIES325311INFUS', # Nitrogenous Fertilizer Manufacturing: Finished Goods Inventories
    'AIES325311INMUS', # Nitrogenous Fertilizer Manufacturing: Materials and Supplies Inventories
    'AIES325311INVUS', # Nitrogenous Fertilizer Manufacturing: Total Inventories
    'AIES325311INWUS', # Nitrogenous Fertilizer Manufacturing: Work In Process Inventories
    'AIES325311PAYUS', # Nitrogenous Fertilizer Manufacturing: Annual Payroll
    'AIES325311PWEUS', # Nitrogenous Fertilizer Manufacturing: Production Workers
    'AIES325311RCTUS', # Nitrogenous Fertilizer Manufacturing: Shipments
    'AIES325311TCMUS', # Nitrogenous Fertilizer Manufacturing: Total Cost of Materials
    ### 325312 Phosphatic Fertilizer Manufacturing
    'AIES325312EMPUS', # Phosphatic Fertilizer Manufacturing: Employees
    'AIES325312INFUS', # Phosphatic Fertilizer Manufacturing: Finished Goods Inventories
    'AIES325312INMUS', # Phosphatic Fertilizer Manufacturing: Materials and Supplies Inventories
    'AIES325312INVUS', # Phosphatic Fertilizer Manufacturing: Total Inventories
    'AIES325312INWUS', # Phosphatic Fertilizer Manufacturing: Work In Process Inventories
    'AIES325312PAYUS', # Phosphatic Fertilizer Manufacturing: Annual Payroll
    'AIES325312PWEUS', # Phosphatic Fertilizer Manufacturing: Production Workers
    'AIES325312RCTUS', # Phosphatic Fertilizer Manufacturing: Shipments
    'AIES325312TCMUS', # Phosphatic Fertilizer Manufacturing: Total Cost of Materials
    ### 325314 Fertilizer (Mixing Only) Manufacturing
    'AIES325314EMPUS', # Fertilizer (Mixing Only) Manufacturing: Employees
    'AIES325314INFUS', # Fertilizer (Mixing Only) Manufacturing: Finished Goods Inventories
    'AIES325314INMUS', # Fertilizer (Mixing Only) Manufacturing: Materials and Supplies Inventories
    'AIES325314INVUS', # Fertilizer (Mixing Only) Manufacturing: Total Inventories
    'AIES325314INWUS', # Fertilizer (Mixing Only) Manufacturing: Work In Process Inventories
    'AIES325314PAYUS', # Fertilizer (Mixing Only) Manufacturing: Annual Payroll
    'AIES325314PWEUS', # Fertilizer (Mixing Only) Manufacturing: Production Workers
    'AIES325314RCTUS', # Fertilizer (Mixing Only) Manufacturing: Shipments
    'AIES325314TCMUS', # Fertilizer (Mixing Only) Manufacturing: Total Cost of Materials
    ### 32532 Pesticide and Other Agricultural Chemical Manufacturing
    'AIES32532EMPUS', # Pesticide and Other Agricultural Chemical Manufacturing: Employees
    'AIES32532INFUS', # Pesticide and Other Agricultural Chemical Manufacturing: Finished Goods Inventories
    'AIES32532INMUS', # Pesticide and Other Agricultural Chemical Manufacturing: Materials and Supplies Inventories
    'AIES32532INVUS', # Pesticide and Other Agricultural Chemical Manufacturing: Total Inventories
    'AIES32532INWUS', # Pesticide and Other Agricultural Chemical Manufacturing: Work In Process Inventories
    'AIES32532PAYUS', # Pesticide and Other Agricultural Chemical Manufacturing: Annual Payroll
    'AIES32532PWEUS', # Pesticide and Other Agricultural Chemical Manufacturing: Production Workers
    'AIES32532RCTUS', # Pesticide and Other Agricultural Chemical Manufacturing: Shipments
    'AIES32532TCMUS', # Pesticide and Other Agricultural Chemical Manufacturing: Total Cost of Materials
    ### 3254 Pharmaceutical and Medicine Manufacturing
    'AIES3254EMPUS', # Pharmaceutical and Medicine Manufacturing: Employees
    'AIES3254INFUS', # Pharmaceutical and Medicine Manufacturing: Finished Goods Inventories
    'AIES3254INMUS', # Pharmaceutical and Medicine Manufacturing: Materials and Supplies Inventories
    'AIES3254INVUS', # Pharmaceutical and Medicine Manufacturing: Total Inventories
    'AIES3254INWUS', # Pharmaceutical and Medicine Manufacturing: Work In Process Inventories
    'AIES3254PAYUS', # Pharmaceutical and Medicine Manufacturing: Annual Payroll
    'AIES3254PWEUS', # Pharmaceutical and Medicine Manufacturing: Production Workers
    'AIES3254RCTUS', # Pharmaceutical and Medicine Manufacturing: Shipments
    'AIES3254TCMUS', # Pharmaceutical and Medicine Manufacturing: Total Cost of Materials
    ### 325411 Medicinal and Botanical Manufacturing
    'AIES325411EMPUS', # Medicinal and Botanical Manufacturing: Employees
    'AIES325411INFUS', # Medicinal and Botanical Manufacturing: Finished Goods Inventories
    'AIES325411INMUS', # Medicinal and Botanical Manufacturing: Materials and Supplies Inventories
    'AIES325411INVUS', # Medicinal and Botanical Manufacturing: Total Inventories
    'AIES325411INWUS', # Medicinal and Botanical Manufacturing: Work In Process Inventories
    'AIES325411PAYUS', # Medicinal and Botanical Manufacturing: Annual Payroll
    'AIES325411PWEUS', # Medicinal and Botanical Manufacturing: Production Workers
    'AIES325411RCTUS', # Medicinal and Botanical Manufacturing: Shipments
    'AIES325411TCMUS', # Medicinal and Botanical Manufacturing: Total Cost of Materials
    ### 325412 Pharmaceutical Preparation Manufacturing
    'AIES325412EMPUS', # Pharmaceutical Preparation Manufacturing: Employees
    'AIES325412INFUS', # Pharmaceutical Preparation Manufacturing: Finished Goods Inventories
    'AIES325412INMUS', # Pharmaceutical Preparation Manufacturing: Materials and Supplies Inventories
    'AIES325412INVUS', # Pharmaceutical Preparation Manufacturing: Total Inventories
    'AIES325412INWUS', # Pharmaceutical Preparation Manufacturing: Work In Process Inventories
    'AIES325412PAYUS', # Pharmaceutical Preparation Manufacturing: Annual Payroll
    'AIES325412PWEUS', # Pharmaceutical Preparation Manufacturing: Production Workers
    'AIES325412RCTUS', # Pharmaceutical Preparation Manufacturing: Shipments
    'AIES325412TCMUS', # Pharmaceutical Preparation Manufacturing: Total Cost of Materials
    ### 325413 In-Vitro Diagnostic Substance Manufacturing
    'AIES325413EMPUS', # In-Vitro Diagnostic Substance Manufacturing: Employees
    'AIES325413INFUS', # In-Vitro Diagnostic Substance Manufacturing: Finished Goods Inventories
    'AIES325413INMUS', # In-Vitro Diagnostic Substance Manufacturing: Materials and Supplies Inventories
    'AIES325413INVUS', # In-Vitro Diagnostic Substance Manufacturing: Total Inventories
    'AIES325413INWUS', # In-Vitro Diagnostic Substance Manufacturing: Work In Process Inventories
    'AIES325413PAYUS', # In-Vitro Diagnostic Substance Manufacturing: Annual Payroll
    'AIES325413PWEUS', # In-Vitro Diagnostic Substance Manufacturing: Production Workers
    'AIES325413RCTUS', # In-Vitro Diagnostic Substance Manufacturing: Shipments
    'AIES325413TCMUS', # In-Vitro Diagnostic Substance Manufacturing: Total Cost of Materials
    ### 325414 Biological Product (Except Diagnostic) Manufacturing
    'AIES325414EMPUS', # Biological Product (Except Diagnostic) Manufacturing: Employees
    'AIES325414INFUS', # Biological Product (Except Diagnostic) Manufacturing: Finished Goods Inventories
    'AIES325414INMUS', # Biological Product (Except Diagnostic) Manufacturing: Materials and Supplies Inventories
    'AIES325414INVUS', # Biological Product (Except Diagnostic) Manufacturing: Total Inventories
    'AIES325414INWUS', # Biological Product (Except Diagnostic) Manufacturing: Work In Process Inventories
    'AIES325414PAYUS', # Biological Product (Except Diagnostic) Manufacturing: Annual Payroll
    'AIES325414PWEUS', # Biological Product (Except Diagnostic) Manufacturing: Production Workers
    'AIES325414RCTUS', # Biological Product (Except Diagnostic) Manufacturing: Shipments
    'AIES325414TCMUS', # Biological Product (Except Diagnostic) Manufacturing: Total Cost of Materials
    ### 3255 Paint, Coating, and Adhesive Manufacturing
    'AIES3255EMPUS', # Paint, Coating, and Adhesive Manufacturing: Employees
    'AIES3255INFUS', # Paint, Coating, and Adhesive Manufacturing: Finished Goods Inventories
    'AIES3255INMUS', # Paint, Coating, and Adhesive Manufacturing: Materials and Supplies Inventories
    'AIES3255INVUS', # Paint, Coating, and Adhesive Manufacturing: Total Inventories
    'AIES3255INWUS', # Paint, Coating, and Adhesive Manufacturing: Work In Process Inventories
    'AIES3255PAYUS', # Paint, Coating, and Adhesive Manufacturing: Annual Payroll
    'AIES3255PWEUS', # Paint, Coating, and Adhesive Manufacturing: Production Workers
    'AIES3255RCTUS', # Paint, Coating, and Adhesive Manufacturing: Shipments
    'AIES3255TCMUS', # Paint, Coating, and Adhesive Manufacturing: Total Cost of Materials
    ### 32551 Paint and Coating Manufacturing
    'AIES32551EMPUS', # Paint and Coating Manufacturing: Employees
    'AIES32551INFUS', # Paint and Coating Manufacturing: Finished Goods Inventories
    'AIES32551INMUS', # Paint and Coating Manufacturing: Materials and Supplies Inventories
    'AIES32551INVUS', # Paint and Coating Manufacturing: Total Inventories
    'AIES32551INWUS', # Paint and Coating Manufacturing: Work In Process Inventories
    'AIES32551PAYUS', # Paint and Coating Manufacturing: Annual Payroll
    'AIES32551PWEUS', # Paint and Coating Manufacturing: Production Workers
    'AIES32551RCTUS', # Paint and Coating Manufacturing: Shipments
    'AIES32551TCMUS', # Paint and Coating Manufacturing: Total Cost of Materials
    ### 32552 Adhesive Manufacturing
    'AIES32552EMPUS', # Adhesive Manufacturing: Employees
    'AIES32552INFUS', # Adhesive Manufacturing: Finished Goods Inventories
    'AIES32552INMUS', # Adhesive Manufacturing: Materials and Supplies Inventories
    'AIES32552INVUS', # Adhesive Manufacturing: Total Inventories
    'AIES32552INWUS', # Adhesive Manufacturing: Work In Process Inventories
    'AIES32552PAYUS', # Adhesive Manufacturing: Annual Payroll
    'AIES32552PWEUS', # Adhesive Manufacturing: Production Workers
    'AIES32552RCTUS', # Adhesive Manufacturing: Shipments
    'AIES32552TCMUS', # Adhesive Manufacturing: Total Cost of Materials
    ### 3256 Soap, Cleaning Compound, and Toilet Preparation Manufacturing
    'AIES3256EMPUS', # Soap, Cleaning Compound, and Toilet Preparation Manufacturing: Employees
    'AIES3256INFUS', # Soap, Cleaning Compound, and Toilet Preparation Manufacturing: Finished Goods Inventories
    'AIES3256INMUS', # Soap, Cleaning Compound, and Toilet Preparation Manufacturing: Materials and Supplies Inventories
    'AIES3256INVUS', # Soap, Cleaning Compound, and Toilet Preparation Manufacturing: Total Inventories
    'AIES3256INWUS', # Soap, Cleaning Compound, and Toilet Preparation Manufacturing: Work In Process Inventories
    'AIES3256PAYUS', # Soap, Cleaning Compound, and Toilet Preparation Manufacturing: Annual Payroll
    'AIES3256PWEUS', # Soap, Cleaning Compound, and Toilet Preparation Manufacturing: Production Workers
    'AIES3256RCTUS', # Soap, Cleaning Compound, and Toilet Preparation Manufacturing: Shipments
    'AIES3256TCMUS', # Soap, Cleaning Compound, and Toilet Preparation Manufacturing: Total Cost of Materials
    ### 32561 Soap and Cleaning Compound Manufacturing
    'AIES32561EMPUS', # Soap and Cleaning Compound Manufacturing: Employees
    'AIES32561INFUS', # Soap and Cleaning Compound Manufacturing: Finished Goods Inventories
    'AIES32561INMUS', # Soap and Cleaning Compound Manufacturing: Materials and Supplies Inventories
    'AIES32561INVUS', # Soap and Cleaning Compound Manufacturing: Total Inventories
    'AIES32561INWUS', # Soap and Cleaning Compound Manufacturing: Work In Process Inventories
    'AIES32561PAYUS', # Soap and Cleaning Compound Manufacturing: Annual Payroll
    'AIES32561PWEUS', # Soap and Cleaning Compound Manufacturing: Production Workers
    'AIES32561RCTUS', # Soap and Cleaning Compound Manufacturing: Shipments
    'AIES32561TCMUS', # Soap and Cleaning Compound Manufacturing: Total Cost of Materials
    ### 325611 Soap and Other Detergent Manufacturing
    'AIES325611EMPUS', # Soap and Other Detergent Manufacturing: Employees
    'AIES325611INFUS', # Soap and Other Detergent Manufacturing: Finished Goods Inventories
    'AIES325611INMUS', # Soap and Other Detergent Manufacturing: Materials and Supplies Inventories
    'AIES325611INVUS', # Soap and Other Detergent Manufacturing: Total Inventories
    'AIES325611INWUS', # Soap and Other Detergent Manufacturing: Work In Process Inventories
    'AIES325611PAYUS', # Soap and Other Detergent Manufacturing: Annual Payroll
    'AIES325611PWEUS', # Soap and Other Detergent Manufacturing: Production Workers
    'AIES325611RCTUS', # Soap and Other Detergent Manufacturing: Shipments
    'AIES325611TCMUS', # Soap and Other Detergent Manufacturing: Total Cost of Materials
    ### 325612 Polish and Other Sanitation Good Manufacturing
    'AIES325612EMPUS', # Polish and Other Sanitation Good Manufacturing: Employees
    'AIES325612INFUS', # Polish and Other Sanitation Good Manufacturing: Finished Goods Inventories
    'AIES325612INMUS', # Polish and Other Sanitation Good Manufacturing: Materials and Supplies Inventories
    'AIES325612INVUS', # Polish and Other Sanitation Good Manufacturing: Total Inventories
    'AIES325612INWUS', # Polish and Other Sanitation Good Manufacturing: Work In Process Inventories
    'AIES325612PAYUS', # Polish and Other Sanitation Good Manufacturing: Annual Payroll
    'AIES325612PWEUS', # Polish and Other Sanitation Good Manufacturing: Production Workers
    'AIES325612RCTUS', # Polish and Other Sanitation Good Manufacturing: Shipments
    'AIES325612TCMUS', # Polish and Other Sanitation Good Manufacturing: Total Cost of Materials
    ### 325613 Surface Active Agent Manufacturing
    'AIES325613EMPUS', # Surface Active Agent Manufacturing: Employees
    'AIES325613INFUS', # Surface Active Agent Manufacturing: Finished Goods Inventories
    'AIES325613INMUS', # Surface Active Agent Manufacturing: Materials and Supplies Inventories
    'AIES325613INVUS', # Surface Active Agent Manufacturing: Total Inventories
    'AIES325613INWUS', # Surface Active Agent Manufacturing: Work In Process Inventories
    'AIES325613PAYUS', # Surface Active Agent Manufacturing: Annual Payroll
    'AIES325613PWEUS', # Surface Active Agent Manufacturing: Production Workers
    'AIES325613RCTUS', # Surface Active Agent Manufacturing: Shipments
    'AIES325613TCMUS', # Surface Active Agent Manufacturing: Total Cost of Materials
    ### 32562 Toilet Preparation Manufacturing
    'AIES32562EMPUS', # Toilet Preparation Manufacturing: Employees
    'AIES32562INFUS', # Toilet Preparation Manufacturing: Finished Goods Inventories
    'AIES32562INMUS', # Toilet Preparation Manufacturing: Materials and Supplies Inventories
    'AIES32562INVUS', # Toilet Preparation Manufacturing: Total Inventories
    'AIES32562INWUS', # Toilet Preparation Manufacturing: Work In Process Inventories
    'AIES32562PAYUS', # Toilet Preparation Manufacturing: Annual Payroll
    'AIES32562PWEUS', # Toilet Preparation Manufacturing: Production Workers
    'AIES32562RCTUS', # Toilet Preparation Manufacturing: Shipments
    'AIES32562TCMUS', # Toilet Preparation Manufacturing: Total Cost of Materials
    ### 3259 Other Chemical Product and Preparation Manufacturing
    'AIES3259EMPUS', # Other Chemical Product and Preparation Manufacturing: Employees
    'AIES3259INFUS', # Other Chemical Product and Preparation Manufacturing: Finished Goods Inventories
    'AIES3259INMUS', # Other Chemical Product and Preparation Manufacturing: Materials and Supplies Inventories
    'AIES3259INVUS', # Other Chemical Product and Preparation Manufacturing: Total Inventories
    'AIES3259INWUS', # Other Chemical Product and Preparation Manufacturing: Work In Process Inventories
    'AIES3259PAYUS', # Other Chemical Product and Preparation Manufacturing: Annual Payroll
    'AIES3259PWEUS', # Other Chemical Product and Preparation Manufacturing: Production Workers
    'AIES3259RCTUS', # Other Chemical Product and Preparation Manufacturing: Shipments
    'AIES3259TCMUS', # Other Chemical Product and Preparation Manufacturing: Total Cost of Materials
    ### 32591 Printing Ink Manufacturing
    'AIES32591EMPUS', # Printing Ink Manufacturing: Employees
    'AIES32591INFUS', # Printing Ink Manufacturing: Finished Goods Inventories
    'AIES32591INMUS', # Printing Ink Manufacturing: Materials and Supplies Inventories
    'AIES32591INVUS', # Printing Ink Manufacturing: Total Inventories
    'AIES32591INWUS', # Printing Ink Manufacturing: Work In Process Inventories
    'AIES32591PAYUS', # Printing Ink Manufacturing: Annual Payroll
    'AIES32591PWEUS', # Printing Ink Manufacturing: Production Workers
    'AIES32591RCTUS', # Printing Ink Manufacturing: Shipments
    'AIES32591TCMUS', # Printing Ink Manufacturing: Total Cost of Materials
    ### 32592 Explosives Manufacturing
    'AIES32592EMPUS', # Explosives Manufacturing: Employees
    'AIES32592INFUS', # Explosives Manufacturing: Finished Goods Inventories
    'AIES32592INMUS', # Explosives Manufacturing: Materials and Supplies Inventories
    'AIES32592INVUS', # Explosives Manufacturing: Total Inventories
    'AIES32592INWUS', # Explosives Manufacturing: Work In Process Inventories
    'AIES32592PAYUS', # Explosives Manufacturing: Annual Payroll
    'AIES32592PWEUS', # Explosives Manufacturing: Production Workers
    'AIES32592RCTUS', # Explosives Manufacturing: Shipments
    'AIES32592TCMUS', # Explosives Manufacturing: Total Cost of Materials
    ### 32599 All Other Chemical Product and Preparation Manufacturing
    'AIES32599EMPUS', # All Other Chemical Product and Preparation Manufacturing: Employees
    'AIES32599INFUS', # All Other Chemical Product and Preparation Manufacturing: Finished Goods Inventories
    'AIES32599INMUS', # All Other Chemical Product and Preparation Manufacturing: Materials and Supplies Inventories
    'AIES32599INVUS', # All Other Chemical Product and Preparation Manufacturing: Total Inventories
    'AIES32599INWUS', # All Other Chemical Product and Preparation Manufacturing: Work In Process Inventories
    'AIES32599PAYUS', # All Other Chemical Product and Preparation Manufacturing: Annual Payroll
    'AIES32599PWEUS', # All Other Chemical Product and Preparation Manufacturing: Production Workers
    'AIES32599RCTUS', # All Other Chemical Product and Preparation Manufacturing: Shipments
    'AIES32599TCMUS', # All Other Chemical Product and Preparation Manufacturing: Total Cost of Materials
    ### 325991 Custom Compounding of Purchased Resins
    'AIES325991EMPUS', # Custom Compounding of Purchased Resins: Employees
    'AIES325991INFUS', # Custom Compounding of Purchased Resins: Finished Goods Inventories
    'AIES325991INMUS', # Custom Compounding of Purchased Resins: Materials and Supplies Inventories
    'AIES325991INVUS', # Custom Compounding of Purchased Resins: Total Inventories
    'AIES325991INWUS', # Custom Compounding of Purchased Resins: Work In Process Inventories
    'AIES325991PAYUS', # Custom Compounding of Purchased Resins: Annual Payroll
    'AIES325991PWEUS', # Custom Compounding of Purchased Resins: Production Workers
    'AIES325991RCTUS', # Custom Compounding of Purchased Resins: Shipments
    'AIES325991TCMUS', # Custom Compounding of Purchased Resins: Total Cost of Materials
    ### 325992 Photographic Film, Paper, Plate, and Chemical Manufacturing
    'AIES325992EMPUS', # Photographic Film, Paper, Plate, and Chemical Manufacturing: Employees
    'AIES325992INFUS', # Photographic Film, Paper, Plate, and Chemical Manufacturing: Finished Goods Inventories
    'AIES325992INMUS', # Photographic Film, Paper, Plate, and Chemical Manufacturing: Materials and Supplies Inventories
    'AIES325992INVUS', # Photographic Film, Paper, Plate, and Chemical Manufacturing: Total Inventories
    'AIES325992INWUS', # Photographic Film, Paper, Plate, and Chemical Manufacturing: Work In Process Inventories
    'AIES325992PAYUS', # Photographic Film, Paper, Plate, and Chemical Manufacturing: Annual Payroll
    'AIES325992PWEUS', # Photographic Film, Paper, Plate, and Chemical Manufacturing: Production Workers
    'AIES325992RCTUS', # Photographic Film, Paper, Plate, and Chemical Manufacturing: Shipments
    'AIES325992TCMUS', # Photographic Film, Paper, Plate, and Chemical Manufacturing: Total Cost of Materials
    ### 325998 Other Miscellaneous Chemical Product Manufacturing
    'AIES325998EMPUS', # Other Miscellaneous Chemical Product Manufacturing: Employees
    'AIES325998INFUS', # Other Miscellaneous Chemical Product Manufacturing: Finished Goods Inventories
    'AIES325998INMUS', # Other Miscellaneous Chemical Product Manufacturing: Materials and Supplies Inventories
    'AIES325998INVUS', # Other Miscellaneous Chemical Product Manufacturing: Total Inventories
    'AIES325998INWUS', # Other Miscellaneous Chemical Product Manufacturing: Work In Process Inventories
    'AIES325998PAYUS', # Other Miscellaneous Chemical Product Manufacturing: Annual Payroll
    'AIES325998PWEUS', # Other Miscellaneous Chemical Product Manufacturing: Production Workers
    'AIES325998RCTUS', # Other Miscellaneous Chemical Product Manufacturing: Shipments
    'AIES325998TCMUS', # Other Miscellaneous Chemical Product Manufacturing: Total Cost of Materials
    ## NAICS 326 Plastics and Rubber Products Manufacturing
    ### 326 Plastics and Rubber Products Manufacturing
    'AIES326EMPUS', # Plastics and Rubber Products Manufacturing: Employees
    'AIES326INFUS', # Plastics and Rubber Products Manufacturing: Finished Goods Inventories
    'AIES326INMUS', # Plastics and Rubber Products Manufacturing: Materials and Supplies Inventories
    'AIES326INVUS', # Plastics and Rubber Products Manufacturing: Total Inventories
    'AIES326INWUS', # Plastics and Rubber Products Manufacturing: Work In Process Inventories
    'AIES326PAYUS', # Plastics and Rubber Products Manufacturing: Annual Payroll
    'AIES326PWEUS', # Plastics and Rubber Products Manufacturing: Production Workers
    'AIES326RCTUS', # Plastics and Rubber Products Manufacturing: Shipments
    'AIES326TCMUS', # Plastics and Rubber Products Manufacturing: Total Cost of Materials
    ### 3261 Plastics Product Manufacturing
    'AIES3261EMPUS', # Plastics Product Manufacturing: Employees
    'AIES3261INFUS', # Plastics Product Manufacturing: Finished Goods Inventories
    'AIES3261INMUS', # Plastics Product Manufacturing: Materials and Supplies Inventories
    'AIES3261INVUS', # Plastics Product Manufacturing: Total Inventories
    'AIES3261INWUS', # Plastics Product Manufacturing: Work In Process Inventories
    'AIES3261PAYUS', # Plastics Product Manufacturing: Annual Payroll
    'AIES3261PWEUS', # Plastics Product Manufacturing: Production Workers
    'AIES3261RCTUS', # Plastics Product Manufacturing: Shipments
    'AIES3261TCMUS', # Plastics Product Manufacturing: Total Cost of Materials
    ### 32611 Plastics Packaging Materials, Film and Sheet
    'AIES32611EMPUS', # Plastics Packaging Materials, Film and Sheet: Employees
    'AIES32611INFUS', # Plastics Packaging Materials, Film and Sheet: Finished Goods Inventories
    'AIES32611INMUS', # Plastics Packaging Materials, Film and Sheet: Materials and Supplies Inventories
    'AIES32611INVUS', # Plastics Packaging Materials, Film and Sheet: Total Inventories
    'AIES32611INWUS', # Plastics Packaging Materials, Film and Sheet: Work In Process Inventories
    'AIES32611PAYUS', # Plastics Packaging Materials, Film and Sheet: Annual Payroll
    'AIES32611PWEUS', # Plastics Packaging Materials, Film and Sheet: Production Workers
    'AIES32611RCTUS', # Plastics Packaging Materials, Film and Sheet: Shipments
    'AIES32611TCMUS', # Plastics Packaging Materials, Film and Sheet: Total Cost of Materials
    ### 326111 Plastics Bag and Pouch Manufacturing
    'AIES326111EMPUS', # Plastics Bag and Pouch Manufacturing: Employees
    'AIES326111INFUS', # Plastics Bag and Pouch Manufacturing: Finished Goods Inventories
    'AIES326111INMUS', # Plastics Bag and Pouch Manufacturing: Materials and Supplies Inventories
    'AIES326111INVUS', # Plastics Bag and Pouch Manufacturing: Total Inventories
    'AIES326111INWUS', # Plastics Bag and Pouch Manufacturing: Work In Process Inventories
    'AIES326111PAYUS', # Plastics Bag and Pouch Manufacturing: Annual Payroll
    'AIES326111PWEUS', # Plastics Bag and Pouch Manufacturing: Production Workers
    'AIES326111RCTUS', # Plastics Bag and Pouch Manufacturing: Shipments
    'AIES326111TCMUS', # Plastics Bag and Pouch Manufacturing: Total Cost of Materials
    ### 326112 Plastics Packaging Film and Sheet Manufacturing
    'AIES326112EMPUS', # Plastics Packaging Film and Sheet Manufacturing: Employees
    'AIES326112INFUS', # Plastics Packaging Film and Sheet Manufacturing: Finished Goods Inventories
    'AIES326112INMUS', # Plastics Packaging Film and Sheet Manufacturing: Materials and Supplies Inventories
    'AIES326112INVUS', # Plastics Packaging Film and Sheet Manufacturing: Total Inventories
    'AIES326112INWUS', # Plastics Packaging Film and Sheet Manufacturing: Work In Process Inventories
    'AIES326112PAYUS', # Plastics Packaging Film and Sheet Manufacturing: Annual Payroll
    'AIES326112PWEUS', # Plastics Packaging Film and Sheet Manufacturing: Production Workers
    'AIES326112RCTUS', # Plastics Packaging Film and Sheet Manufacturing: Shipments
    'AIES326112TCMUS', # Plastics Packaging Film and Sheet Manufacturing: Total Cost of Materials
    ### 326113 Nonpackaging Plastics Film and Sheet Manufacturing
    'AIES326113EMPUS', # Nonpackaging Plastics Film and Sheet Manufacturing: Employees
    'AIES326113INFUS', # Nonpackaging Plastics Film and Sheet Manufacturing: Finished Goods Inventories
    'AIES326113INMUS', # Nonpackaging Plastics Film and Sheet Manufacturing: Materials and Supplies Inventories
    'AIES326113INVUS', # Nonpackaging Plastics Film and Sheet Manufacturing: Total Inventories
    'AIES326113INWUS', # Nonpackaging Plastics Film and Sheet Manufacturing: Work In Process Inventories
    'AIES326113PAYUS', # Nonpackaging Plastics Film and Sheet Manufacturing: Annual Payroll
    'AIES326113PWEUS', # Nonpackaging Plastics Film and Sheet Manufacturing: Production Workers
    'AIES326113RCTUS', # Nonpackaging Plastics Film and Sheet Manufacturing: Shipments
    'AIES326113TCMUS', # Nonpackaging Plastics Film and Sheet Manufacturing: Total Cost of Materials
    ### 32612 Plastics Pipe, Fittings, and Profile Shapes
    'AIES32612EMPUS', # Plastics Pipe, Fittings, and Profile Shapes: Employees
    'AIES32612INFUS', # Plastics Pipe, Fittings, and Profile Shapes: Finished Goods Inventories
    'AIES32612INMUS', # Plastics Pipe, Fittings, and Profile Shapes: Materials and Supplies Inventories
    'AIES32612INVUS', # Plastics Pipe, Fittings, and Profile Shapes: Total Inventories
    'AIES32612INWUS', # Plastics Pipe, Fittings, and Profile Shapes: Work In Process Inventories
    'AIES32612PAYUS', # Plastics Pipe, Fittings, and Profile Shapes: Annual Payroll
    'AIES32612PWEUS', # Plastics Pipe, Fittings, and Profile Shapes: Production Workers
    'AIES32612RCTUS', # Plastics Pipe, Fittings, and Profile Shapes: Shipments
    'AIES32612TCMUS', # Plastics Pipe, Fittings, and Profile Shapes: Total Cost of Materials
    ### 326121 Unlaminated Plastics Profile Shape Manufacturing
    'AIES326121EMPUS', # Unlaminated Plastics Profile Shape Manufacturing: Employees
    'AIES326121INFUS', # Unlaminated Plastics Profile Shape Manufacturing: Finished Goods Inventories
    'AIES326121INMUS', # Unlaminated Plastics Profile Shape Manufacturing: Materials and Supplies Inventories
    'AIES326121INVUS', # Unlaminated Plastics Profile Shape Manufacturing: Total Inventories
    'AIES326121INWUS', # Unlaminated Plastics Profile Shape Manufacturing: Work In Process Inventories
    'AIES326121PAYUS', # Unlaminated Plastics Profile Shape Manufacturing: Annual Payroll
    'AIES326121PWEUS', # Unlaminated Plastics Profile Shape Manufacturing: Production Workers
    'AIES326121RCTUS', # Unlaminated Plastics Profile Shape Manufacturing: Shipments
    'AIES326121TCMUS', # Unlaminated Plastics Profile Shape Manufacturing: Total Cost of Materials
    ### 326122 Plastics Pipe and Pipe Fitting Manufacturing
    'AIES326122EMPUS', # Plastics Pipe and Pipe Fitting Manufacturing: Employees
    'AIES326122INFUS', # Plastics Pipe and Pipe Fitting Manufacturing: Finished Goods Inventories
    'AIES326122INMUS', # Plastics Pipe and Pipe Fitting Manufacturing: Materials and Supplies Inventories
    'AIES326122INVUS', # Plastics Pipe and Pipe Fitting Manufacturing: Total Inventories
    'AIES326122INWUS', # Plastics Pipe and Pipe Fitting Manufacturing: Work In Process Inventories
    'AIES326122PAYUS', # Plastics Pipe and Pipe Fitting Manufacturing: Annual Payroll
    'AIES326122PWEUS', # Plastics Pipe and Pipe Fitting Manufacturing: Production Workers
    'AIES326122RCTUS', # Plastics Pipe and Pipe Fitting Manufacturing: Shipments
    'AIES326122TCMUS', # Plastics Pipe and Pipe Fitting Manufacturing: Total Cost of Materials
    ### 32613 Laminated Plastics Plate, Sheet, and Shapes
    'AIES32613EMPUS', # Laminated Plastics Plate, Sheet, and Shapes: Employees
    'AIES32613INFUS', # Laminated Plastics Plate, Sheet, and Shapes: Finished Goods Inventories
    'AIES32613INMUS', # Laminated Plastics Plate, Sheet, and Shapes: Materials and Supplies Inventories
    'AIES32613INVUS', # Laminated Plastics Plate, Sheet, and Shapes: Total Inventories
    'AIES32613INWUS', # Laminated Plastics Plate, Sheet, and Shapes: Work In Process Inventories
    'AIES32613PAYUS', # Laminated Plastics Plate, Sheet, and Shapes: Annual Payroll
    'AIES32613PWEUS', # Laminated Plastics Plate, Sheet, and Shapes: Production Workers
    'AIES32613RCTUS', # Laminated Plastics Plate, Sheet, and Shapes: Shipments
    'AIES32613TCMUS', # Laminated Plastics Plate, Sheet, and Shapes: Total Cost of Materials
    ### 32614 Polystyrene Foam Product Manufacturing
    'AIES32614EMPUS', # Polystyrene Foam Product Manufacturing: Employees
    'AIES32614INFUS', # Polystyrene Foam Product Manufacturing: Finished Goods Inventories
    'AIES32614INMUS', # Polystyrene Foam Product Manufacturing: Materials and Supplies Inventories
    'AIES32614INVUS', # Polystyrene Foam Product Manufacturing: Total Inventories
    'AIES32614INWUS', # Polystyrene Foam Product Manufacturing: Work In Process Inventories
    'AIES32614PAYUS', # Polystyrene Foam Product Manufacturing: Annual Payroll
    'AIES32614PWEUS', # Polystyrene Foam Product Manufacturing: Production Workers
    'AIES32614RCTUS', # Polystyrene Foam Product Manufacturing: Shipments
    'AIES32614TCMUS', # Polystyrene Foam Product Manufacturing: Total Cost of Materials
    ### 32615 Urethane and Other Foam Product Manufacturing
    'AIES32615EMPUS', # Urethane and Other Foam Product Manufacturing: Employees
    'AIES32615INFUS', # Urethane and Other Foam Product Manufacturing: Finished Goods Inventories
    'AIES32615INMUS', # Urethane and Other Foam Product Manufacturing: Materials and Supplies Inventories
    'AIES32615INVUS', # Urethane and Other Foam Product Manufacturing: Total Inventories
    'AIES32615INWUS', # Urethane and Other Foam Product Manufacturing: Work In Process Inventories
    'AIES32615PAYUS', # Urethane and Other Foam Product Manufacturing: Annual Payroll
    'AIES32615PWEUS', # Urethane and Other Foam Product Manufacturing: Production Workers
    'AIES32615RCTUS', # Urethane and Other Foam Product Manufacturing: Shipments
    'AIES32615TCMUS', # Urethane and Other Foam Product Manufacturing: Total Cost of Materials
    ### 32616 Plastics Bottle Manufacturing
    'AIES32616EMPUS', # Plastics Bottle Manufacturing: Employees
    'AIES32616INFUS', # Plastics Bottle Manufacturing: Finished Goods Inventories
    'AIES32616INMUS', # Plastics Bottle Manufacturing: Materials and Supplies Inventories
    'AIES32616INVUS', # Plastics Bottle Manufacturing: Total Inventories
    'AIES32616INWUS', # Plastics Bottle Manufacturing: Work In Process Inventories
    'AIES32616PAYUS', # Plastics Bottle Manufacturing: Annual Payroll
    'AIES32616PWEUS', # Plastics Bottle Manufacturing: Production Workers
    'AIES32616RCTUS', # Plastics Bottle Manufacturing: Shipments
    'AIES32616TCMUS', # Plastics Bottle Manufacturing: Total Cost of Materials
    ### 32619 Other Plastics Product Manufacturing
    'AIES32619EMPUS', # Other Plastics Product Manufacturing: Employees
    'AIES32619INFUS', # Other Plastics Product Manufacturing: Finished Goods Inventories
    'AIES32619INMUS', # Other Plastics Product Manufacturing: Materials and Supplies Inventories
    'AIES32619INVUS', # Other Plastics Product Manufacturing: Total Inventories
    'AIES32619INWUS', # Other Plastics Product Manufacturing: Work In Process Inventories
    'AIES32619PAYUS', # Other Plastics Product Manufacturing: Annual Payroll
    'AIES32619PWEUS', # Other Plastics Product Manufacturing: Production Workers
    'AIES32619RCTUS', # Other Plastics Product Manufacturing: Shipments
    'AIES32619TCMUS', # Other Plastics Product Manufacturing: Total Cost of Materials
    ### 326191 Plastics Plumbing Fixture Manufacturing
    'AIES326191EMPUS', # Plastics Plumbing Fixture Manufacturing: Employees
    'AIES326191INFUS', # Plastics Plumbing Fixture Manufacturing: Finished Goods Inventories
    'AIES326191INMUS', # Plastics Plumbing Fixture Manufacturing: Materials and Supplies Inventories
    'AIES326191INVUS', # Plastics Plumbing Fixture Manufacturing: Total Inventories
    'AIES326191INWUS', # Plastics Plumbing Fixture Manufacturing: Work In Process Inventories
    'AIES326191PAYUS', # Plastics Plumbing Fixture Manufacturing: Annual Payroll
    'AIES326191PWEUS', # Plastics Plumbing Fixture Manufacturing: Production Workers
    'AIES326191RCTUS', # Plastics Plumbing Fixture Manufacturing: Shipments
    'AIES326191TCMUS', # Plastics Plumbing Fixture Manufacturing: Total Cost of Materials
    ### 326199 All Other Plastics Product Manufacturing
    'AIES326199EMPUS', # All Other Plastics Product Manufacturing: Employees
    'AIES326199INFUS', # All Other Plastics Product Manufacturing: Finished Goods Inventories
    'AIES326199INMUS', # All Other Plastics Product Manufacturing: Materials and Supplies Inventories
    'AIES326199INVUS', # All Other Plastics Product Manufacturing: Total Inventories
    'AIES326199INWUS', # All Other Plastics Product Manufacturing: Work In Process Inventories
    'AIES326199PAYUS', # All Other Plastics Product Manufacturing: Annual Payroll
    'AIES326199PWEUS', # All Other Plastics Product Manufacturing: Production Workers
    'AIES326199RCTUS', # All Other Plastics Product Manufacturing: Shipments
    'AIES326199TCMUS', # All Other Plastics Product Manufacturing: Total Cost of Materials
    ### 3262 Rubber Product Manufacturing
    'AIES3262EMPUS', # Rubber Product Manufacturing: Employees
    'AIES3262INFUS', # Rubber Product Manufacturing: Finished Goods Inventories
    'AIES3262INMUS', # Rubber Product Manufacturing: Materials and Supplies Inventories
    'AIES3262INVUS', # Rubber Product Manufacturing: Total Inventories
    'AIES3262INWUS', # Rubber Product Manufacturing: Work In Process Inventories
    'AIES3262PAYUS', # Rubber Product Manufacturing: Annual Payroll
    'AIES3262PWEUS', # Rubber Product Manufacturing: Production Workers
    'AIES3262RCTUS', # Rubber Product Manufacturing: Shipments
    'AIES3262TCMUS', # Rubber Product Manufacturing: Total Cost of Materials
    ### 32621 Tire Manufacturing
    'AIES32621EMPUS', # Tire Manufacturing: Employees
    'AIES32621INFUS', # Tire Manufacturing: Finished Goods Inventories
    'AIES32621INMUS', # Tire Manufacturing: Materials and Supplies Inventories
    'AIES32621INVUS', # Tire Manufacturing: Total Inventories
    'AIES32621INWUS', # Tire Manufacturing: Work In Process Inventories
    'AIES32621PAYUS', # Tire Manufacturing: Annual Payroll
    'AIES32621PWEUS', # Tire Manufacturing: Production Workers
    'AIES32621RCTUS', # Tire Manufacturing: Shipments
    'AIES32621TCMUS', # Tire Manufacturing: Total Cost of Materials
    ### 326211 Tire Manufacturing (Except Retreading)
    'AIES326211EMPUS', # Tire Manufacturing (Except Retreading): Employees
    'AIES326211INFUS', # Tire Manufacturing (Except Retreading): Finished Goods Inventories
    'AIES326211INMUS', # Tire Manufacturing (Except Retreading): Materials and Supplies Inventories
    'AIES326211INVUS', # Tire Manufacturing (Except Retreading): Total Inventories
    'AIES326211INWUS', # Tire Manufacturing (Except Retreading): Work In Process Inventories
    'AIES326211PAYUS', # Tire Manufacturing (Except Retreading): Annual Payroll
    'AIES326211PWEUS', # Tire Manufacturing (Except Retreading): Production Workers
    'AIES326211RCTUS', # Tire Manufacturing (Except Retreading): Shipments
    'AIES326211TCMUS', # Tire Manufacturing (Except Retreading): Total Cost of Materials
    ### 326212 Tire Retreading
    'AIES326212EMPUS', # Tire Retreading: Employees
    'AIES326212INFUS', # Tire Retreading: Finished Goods Inventories
    'AIES326212INMUS', # Tire Retreading: Materials and Supplies Inventories
    'AIES326212INVUS', # Tire Retreading: Total Inventories
    'AIES326212INWUS', # Tire Retreading: Work In Process Inventories
    'AIES326212PAYUS', # Tire Retreading: Annual Payroll
    'AIES326212PWEUS', # Tire Retreading: Production Workers
    'AIES326212RCTUS', # Tire Retreading: Shipments
    'AIES326212TCMUS', # Tire Retreading: Total Cost of Materials
    ### 32622 Rubber and Plastics Hoses and Belting Manufacturing
    'AIES32622EMPUS', # Rubber and Plastics Hoses and Belting Manufacturing: Employees
    'AIES32622INFUS', # Rubber and Plastics Hoses and Belting Manufacturing: Finished Goods Inventories
    'AIES32622INMUS', # Rubber and Plastics Hoses and Belting Manufacturing: Materials and Supplies Inventories
    'AIES32622INVUS', # Rubber and Plastics Hoses and Belting Manufacturing: Total Inventories
    'AIES32622INWUS', # Rubber and Plastics Hoses and Belting Manufacturing: Work In Process Inventories
    'AIES32622PAYUS', # Rubber and Plastics Hoses and Belting Manufacturing: Annual Payroll
    'AIES32622PWEUS', # Rubber and Plastics Hoses and Belting Manufacturing: Production Workers
    'AIES32622RCTUS', # Rubber and Plastics Hoses and Belting Manufacturing: Shipments
    'AIES32622TCMUS', # Rubber and Plastics Hoses and Belting Manufacturing: Total Cost of Materials
    ### 32629 Other Rubber Product Manufacturing
    'AIES32629EMPUS', # Other Rubber Product Manufacturing: Employees
    'AIES32629INFUS', # Other Rubber Product Manufacturing: Finished Goods Inventories
    'AIES32629INMUS', # Other Rubber Product Manufacturing: Materials and Supplies Inventories
    'AIES32629INVUS', # Other Rubber Product Manufacturing: Total Inventories
    'AIES32629INWUS', # Other Rubber Product Manufacturing: Work In Process Inventories
    'AIES32629PAYUS', # Other Rubber Product Manufacturing: Annual Payroll
    'AIES32629PWEUS', # Other Rubber Product Manufacturing: Production Workers
    'AIES32629RCTUS', # Other Rubber Product Manufacturing: Shipments
    'AIES32629TCMUS', # Other Rubber Product Manufacturing: Total Cost of Materials
    ### 326291 Rubber Product Manufacturing For Mechanical Use
    'AIES326291EMPUS', # Rubber Product Manufacturing For Mechanical Use: Employees
    'AIES326291INFUS', # Rubber Product Manufacturing For Mechanical Use: Finished Goods Inventories
    'AIES326291INMUS', # Rubber Product Manufacturing For Mechanical Use: Materials and Supplies Inventories
    'AIES326291INVUS', # Rubber Product Manufacturing For Mechanical Use: Total Inventories
    'AIES326291INWUS', # Rubber Product Manufacturing For Mechanical Use: Work In Process Inventories
    'AIES326291PAYUS', # Rubber Product Manufacturing For Mechanical Use: Annual Payroll
    'AIES326291PWEUS', # Rubber Product Manufacturing For Mechanical Use: Production Workers
    'AIES326291RCTUS', # Rubber Product Manufacturing For Mechanical Use: Shipments
    'AIES326291TCMUS', # Rubber Product Manufacturing For Mechanical Use: Total Cost of Materials
    ### 326299 All Other Rubber Product Manufacturing
    'AIES326299EMPUS', # All Other Rubber Product Manufacturing: Employees
    'AIES326299INFUS', # All Other Rubber Product Manufacturing: Finished Goods Inventories
    'AIES326299INMUS', # All Other Rubber Product Manufacturing: Materials and Supplies Inventories
    'AIES326299INVUS', # All Other Rubber Product Manufacturing: Total Inventories
    'AIES326299INWUS', # All Other Rubber Product Manufacturing: Work In Process Inventories
    'AIES326299PAYUS', # All Other Rubber Product Manufacturing: Annual Payroll
    'AIES326299PWEUS', # All Other Rubber Product Manufacturing: Production Workers
    'AIES326299RCTUS', # All Other Rubber Product Manufacturing: Shipments
    'AIES326299TCMUS', # All Other Rubber Product Manufacturing: Total Cost of Materials
    ## NAICS 327 Nonmetallic Mineral Product Manufacturing
    ### 327 Nonmetallic Mineral Product Manufacturing
    'AIES327EMPUS', # Nonmetallic Mineral Product Manufacturing: Employees
    'AIES327INFUS', # Nonmetallic Mineral Product Manufacturing: Finished Goods Inventories
    'AIES327INMUS', # Nonmetallic Mineral Product Manufacturing: Materials and Supplies Inventories
    'AIES327INVUS', # Nonmetallic Mineral Product Manufacturing: Total Inventories
    'AIES327INWUS', # Nonmetallic Mineral Product Manufacturing: Work In Process Inventories
    'AIES327PAYUS', # Nonmetallic Mineral Product Manufacturing: Annual Payroll
    'AIES327PWEUS', # Nonmetallic Mineral Product Manufacturing: Production Workers
    'AIES327RCTUS', # Nonmetallic Mineral Product Manufacturing: Shipments
    'AIES327TCMUS', # Nonmetallic Mineral Product Manufacturing: Total Cost of Materials
    ### 3271 Clay Product and Refractory Manufacturing
    'AIES3271EMPUS', # Clay Product and Refractory Manufacturing: Employees
    'AIES3271INFUS', # Clay Product and Refractory Manufacturing: Finished Goods Inventories
    'AIES3271INMUS', # Clay Product and Refractory Manufacturing: Materials and Supplies Inventories
    'AIES3271INVUS', # Clay Product and Refractory Manufacturing: Total Inventories
    'AIES3271INWUS', # Clay Product and Refractory Manufacturing: Work In Process Inventories
    'AIES3271PAYUS', # Clay Product and Refractory Manufacturing: Annual Payroll
    'AIES3271PWEUS', # Clay Product and Refractory Manufacturing: Production Workers
    'AIES3271RCTUS', # Clay Product and Refractory Manufacturing: Shipments
    'AIES3271TCMUS', # Clay Product and Refractory Manufacturing: Total Cost of Materials
    ### 32711 Pottery, Ceramics, and Plumbing Fixture Manufacturing
    'AIES32711EMPUS', # Pottery, Ceramics, and Plumbing Fixture Manufacturing: Employees
    'AIES32711INFUS', # Pottery, Ceramics, and Plumbing Fixture Manufacturing: Finished Goods Inventories
    'AIES32711INMUS', # Pottery, Ceramics, and Plumbing Fixture Manufacturing: Materials and Supplies Inventories
    'AIES32711INVUS', # Pottery, Ceramics, and Plumbing Fixture Manufacturing: Total Inventories
    'AIES32711INWUS', # Pottery, Ceramics, and Plumbing Fixture Manufacturing: Work In Process Inventories
    'AIES32711PAYUS', # Pottery, Ceramics, and Plumbing Fixture Manufacturing: Annual Payroll
    'AIES32711PWEUS', # Pottery, Ceramics, and Plumbing Fixture Manufacturing: Production Workers
    'AIES32711RCTUS', # Pottery, Ceramics, and Plumbing Fixture Manufacturing: Shipments
    'AIES32711TCMUS', # Pottery, Ceramics, and Plumbing Fixture Manufacturing: Total Cost of Materials
    ### 32712 Clay Building Material and Refractories Manufacturing
    'AIES32712EMPUS', # Clay Building Material and Refractories Manufacturing: Employees
    'AIES32712INFUS', # Clay Building Material and Refractories Manufacturing: Finished Goods Inventories
    'AIES32712INMUS', # Clay Building Material and Refractories Manufacturing: Materials and Supplies Inventories
    'AIES32712INVUS', # Clay Building Material and Refractories Manufacturing: Total Inventories
    'AIES32712INWUS', # Clay Building Material and Refractories Manufacturing: Work In Process Inventories
    'AIES32712PAYUS', # Clay Building Material and Refractories Manufacturing: Annual Payroll
    'AIES32712PWEUS', # Clay Building Material and Refractories Manufacturing: Production Workers
    'AIES32712RCTUS', # Clay Building Material and Refractories Manufacturing: Shipments
    'AIES32712TCMUS', # Clay Building Material and Refractories Manufacturing: Total Cost of Materials
    ### 3272 Glass and Glass Product Manufacturing
    'AIES3272EMPUS', # Glass and Glass Product Manufacturing: Employees
    'AIES3272INFUS', # Glass and Glass Product Manufacturing: Finished Goods Inventories
    'AIES3272INMUS', # Glass and Glass Product Manufacturing: Materials and Supplies Inventories
    'AIES3272INVUS', # Glass and Glass Product Manufacturing: Total Inventories
    'AIES3272INWUS', # Glass and Glass Product Manufacturing: Work In Process Inventories
    'AIES3272PAYUS', # Glass and Glass Product Manufacturing: Annual Payroll
    'AIES3272PWEUS', # Glass and Glass Product Manufacturing: Production Workers
    'AIES3272RCTUS', # Glass and Glass Product Manufacturing: Shipments
    'AIES3272TCMUS', # Glass and Glass Product Manufacturing: Total Cost of Materials
    ### 327211 Flat Glass Manufacturing
    'AIES327211EMPUS', # Flat Glass Manufacturing: Employees
    'AIES327211INFUS', # Flat Glass Manufacturing: Finished Goods Inventories
    'AIES327211INMUS', # Flat Glass Manufacturing: Materials and Supplies Inventories
    'AIES327211INVUS', # Flat Glass Manufacturing: Total Inventories
    'AIES327211INWUS', # Flat Glass Manufacturing: Work In Process Inventories
    'AIES327211PAYUS', # Flat Glass Manufacturing: Annual Payroll
    'AIES327211PWEUS', # Flat Glass Manufacturing: Production Workers
    'AIES327211RCTUS', # Flat Glass Manufacturing: Shipments
    'AIES327211TCMUS', # Flat Glass Manufacturing: Total Cost of Materials
    ### 327212 Other Pressed and Blown Glass and Glassware Manufacturing
    'AIES327212EMPUS', # Other Pressed and Blown Glass and Glassware Manufacturing: Employees
    'AIES327212INFUS', # Other Pressed and Blown Glass and Glassware Manufacturing: Finished Goods Inventories
    'AIES327212INMUS', # Other Pressed and Blown Glass and Glassware Manufacturing: Materials and Supplies Inventories
    'AIES327212INVUS', # Other Pressed and Blown Glass and Glassware Manufacturing: Total Inventories
    'AIES327212INWUS', # Other Pressed and Blown Glass and Glassware Manufacturing: Work In Process Inventories
    'AIES327212PAYUS', # Other Pressed and Blown Glass and Glassware Manufacturing: Annual Payroll
    'AIES327212PWEUS', # Other Pressed and Blown Glass and Glassware Manufacturing: Production Workers
    'AIES327212RCTUS', # Other Pressed and Blown Glass and Glassware Manufacturing: Shipments
    'AIES327212TCMUS', # Other Pressed and Blown Glass and Glassware Manufacturing: Total Cost of Materials
    ### 327213 Glass Container Manufacturing
    'AIES327213EMPUS', # Glass Container Manufacturing: Employees
    'AIES327213INFUS', # Glass Container Manufacturing: Finished Goods Inventories
    'AIES327213INMUS', # Glass Container Manufacturing: Materials and Supplies Inventories
    'AIES327213INVUS', # Glass Container Manufacturing: Total Inventories
    'AIES327213INWUS', # Glass Container Manufacturing: Work In Process Inventories
    'AIES327213PAYUS', # Glass Container Manufacturing: Annual Payroll
    'AIES327213PWEUS', # Glass Container Manufacturing: Production Workers
    'AIES327213RCTUS', # Glass Container Manufacturing: Shipments
    'AIES327213TCMUS', # Glass Container Manufacturing: Total Cost of Materials
    ### 327215 Glass Product Manufacturing Made of Purchased Glass
    'AIES327215EMPUS', # Glass Product Manufacturing Made of Purchased Glass: Employees
    'AIES327215INFUS', # Glass Product Manufacturing Made of Purchased Glass: Finished Goods Inventories
    'AIES327215INMUS', # Glass Product Manufacturing Made of Purchased Glass: Materials and Supplies Inventories
    'AIES327215INVUS', # Glass Product Manufacturing Made of Purchased Glass: Total Inventories
    'AIES327215INWUS', # Glass Product Manufacturing Made of Purchased Glass: Work In Process Inventories
    'AIES327215PAYUS', # Glass Product Manufacturing Made of Purchased Glass: Annual Payroll
    'AIES327215PWEUS', # Glass Product Manufacturing Made of Purchased Glass: Production Workers
    'AIES327215RCTUS', # Glass Product Manufacturing Made of Purchased Glass: Shipments
    'AIES327215TCMUS', # Glass Product Manufacturing Made of Purchased Glass: Total Cost of Materials
    ### 3273 Cement and Concrete Product Manufacturing
    'AIES3273EMPUS', # Cement and Concrete Product Manufacturing: Employees
    'AIES3273INFUS', # Cement and Concrete Product Manufacturing: Finished Goods Inventories
    'AIES3273INMUS', # Cement and Concrete Product Manufacturing: Materials and Supplies Inventories
    'AIES3273INVUS', # Cement and Concrete Product Manufacturing: Total Inventories
    'AIES3273INWUS', # Cement and Concrete Product Manufacturing: Work In Process Inventories
    'AIES3273PAYUS', # Cement and Concrete Product Manufacturing: Annual Payroll
    'AIES3273PWEUS', # Cement and Concrete Product Manufacturing: Production Workers
    'AIES3273RCTUS', # Cement and Concrete Product Manufacturing: Shipments
    'AIES3273TCMUS', # Cement and Concrete Product Manufacturing: Total Cost of Materials
    ### 32731 Cement Manufacturing
    'AIES32731EMPUS', # Cement Manufacturing: Employees
    'AIES32731INFUS', # Cement Manufacturing: Finished Goods Inventories
    'AIES32731INMUS', # Cement Manufacturing: Materials and Supplies Inventories
    'AIES32731INVUS', # Cement Manufacturing: Total Inventories
    'AIES32731INWUS', # Cement Manufacturing: Work In Process Inventories
    'AIES32731PAYUS', # Cement Manufacturing: Annual Payroll
    'AIES32731PWEUS', # Cement Manufacturing: Production Workers
    'AIES32731RCTUS', # Cement Manufacturing: Shipments
    'AIES32731TCMUS', # Cement Manufacturing: Total Cost of Materials
    ### 32732 Ready-Mix Concrete Manufacturing
    'AIES32732EMPUS', # Ready-Mix Concrete Manufacturing: Employees
    'AIES32732INFUS', # Ready-Mix Concrete Manufacturing: Finished Goods Inventories
    'AIES32732INMUS', # Ready-Mix Concrete Manufacturing: Materials and Supplies Inventories
    'AIES32732INVUS', # Ready-Mix Concrete Manufacturing: Total Inventories
    'AIES32732INWUS', # Ready-Mix Concrete Manufacturing: Work In Process Inventories
    'AIES32732PAYUS', # Ready-Mix Concrete Manufacturing: Annual Payroll
    'AIES32732PWEUS', # Ready-Mix Concrete Manufacturing: Production Workers
    'AIES32732RCTUS', # Ready-Mix Concrete Manufacturing: Shipments
    'AIES32732TCMUS', # Ready-Mix Concrete Manufacturing: Total Cost of Materials
    ### 32733 Concrete Pipe, Brick, and Block Manufacturing
    'AIES32733EMPUS', # Concrete Pipe, Brick, and Block Manufacturing: Employees
    'AIES32733INFUS', # Concrete Pipe, Brick, and Block Manufacturing: Finished Goods Inventories
    'AIES32733INMUS', # Concrete Pipe, Brick, and Block Manufacturing: Materials and Supplies Inventories
    'AIES32733INVUS', # Concrete Pipe, Brick, and Block Manufacturing: Total Inventories
    'AIES32733INWUS', # Concrete Pipe, Brick, and Block Manufacturing: Work In Process Inventories
    'AIES32733PAYUS', # Concrete Pipe, Brick, and Block Manufacturing: Annual Payroll
    'AIES32733PWEUS', # Concrete Pipe, Brick, and Block Manufacturing: Production Workers
    'AIES32733RCTUS', # Concrete Pipe, Brick, and Block Manufacturing: Shipments
    'AIES32733TCMUS', # Concrete Pipe, Brick, and Block Manufacturing: Total Cost of Materials
    ### 327331 Concrete Block and Brick Manufacturing
    'AIES327331EMPUS', # Concrete Block and Brick Manufacturing: Employees
    'AIES327331INFUS', # Concrete Block and Brick Manufacturing: Finished Goods Inventories
    'AIES327331INMUS', # Concrete Block and Brick Manufacturing: Materials and Supplies Inventories
    'AIES327331INVUS', # Concrete Block and Brick Manufacturing: Total Inventories
    'AIES327331INWUS', # Concrete Block and Brick Manufacturing: Work In Process Inventories
    'AIES327331PAYUS', # Concrete Block and Brick Manufacturing: Annual Payroll
    'AIES327331PWEUS', # Concrete Block and Brick Manufacturing: Production Workers
    'AIES327331RCTUS', # Concrete Block and Brick Manufacturing: Shipments
    'AIES327331TCMUS', # Concrete Block and Brick Manufacturing: Total Cost of Materials
    ### 327332 Concrete Pipe Manufacturing
    'AIES327332EMPUS', # Concrete Pipe Manufacturing: Employees
    'AIES327332INFUS', # Concrete Pipe Manufacturing: Finished Goods Inventories
    'AIES327332INMUS', # Concrete Pipe Manufacturing: Materials and Supplies Inventories
    'AIES327332INVUS', # Concrete Pipe Manufacturing: Total Inventories
    'AIES327332INWUS', # Concrete Pipe Manufacturing: Work In Process Inventories
    'AIES327332PAYUS', # Concrete Pipe Manufacturing: Annual Payroll
    'AIES327332PWEUS', # Concrete Pipe Manufacturing: Production Workers
    'AIES327332RCTUS', # Concrete Pipe Manufacturing: Shipments
    'AIES327332TCMUS', # Concrete Pipe Manufacturing: Total Cost of Materials
    ### 32739 Other Concrete Product Manufacturing
    'AIES32739EMPUS', # Other Concrete Product Manufacturing: Employees
    'AIES32739INFUS', # Other Concrete Product Manufacturing: Finished Goods Inventories
    'AIES32739INMUS', # Other Concrete Product Manufacturing: Materials and Supplies Inventories
    'AIES32739INVUS', # Other Concrete Product Manufacturing: Total Inventories
    'AIES32739INWUS', # Other Concrete Product Manufacturing: Work In Process Inventories
    'AIES32739PAYUS', # Other Concrete Product Manufacturing: Annual Payroll
    'AIES32739PWEUS', # Other Concrete Product Manufacturing: Production Workers
    'AIES32739RCTUS', # Other Concrete Product Manufacturing: Shipments
    'AIES32739TCMUS', # Other Concrete Product Manufacturing: Total Cost of Materials
    ### 3274 Lime and Gypsum Product Manufacturing
    'AIES3274EMPUS', # Lime and Gypsum Product Manufacturing: Employees
    'AIES3274INFUS', # Lime and Gypsum Product Manufacturing: Finished Goods Inventories
    'AIES3274INMUS', # Lime and Gypsum Product Manufacturing: Materials and Supplies Inventories
    'AIES3274INVUS', # Lime and Gypsum Product Manufacturing: Total Inventories
    'AIES3274INWUS', # Lime and Gypsum Product Manufacturing: Work In Process Inventories
    'AIES3274PAYUS', # Lime and Gypsum Product Manufacturing: Annual Payroll
    'AIES3274PWEUS', # Lime and Gypsum Product Manufacturing: Production Workers
    'AIES3274RCTUS', # Lime and Gypsum Product Manufacturing: Shipments
    'AIES3274TCMUS', # Lime and Gypsum Product Manufacturing: Total Cost of Materials
    ### 32741 Lime Manufacturing
    'AIES32741EMPUS', # Lime Manufacturing: Employees
    'AIES32741INFUS', # Lime Manufacturing: Finished Goods Inventories
    'AIES32741INMUS', # Lime Manufacturing: Materials and Supplies Inventories
    'AIES32741INVUS', # Lime Manufacturing: Total Inventories
    'AIES32741INWUS', # Lime Manufacturing: Work In Process Inventories
    'AIES32741PAYUS', # Lime Manufacturing: Annual Payroll
    'AIES32741PWEUS', # Lime Manufacturing: Production Workers
    'AIES32741RCTUS', # Lime Manufacturing: Shipments
    'AIES32741TCMUS', # Lime Manufacturing: Total Cost of Materials
    ### 32742 Gypsum Product Manufacturing
    'AIES32742EMPUS', # Gypsum Product Manufacturing: Employees
    'AIES32742INFUS', # Gypsum Product Manufacturing: Finished Goods Inventories
    'AIES32742INMUS', # Gypsum Product Manufacturing: Materials and Supplies Inventories
    'AIES32742INVUS', # Gypsum Product Manufacturing: Total Inventories
    'AIES32742INWUS', # Gypsum Product Manufacturing: Work In Process Inventories
    'AIES32742PAYUS', # Gypsum Product Manufacturing: Annual Payroll
    'AIES32742PWEUS', # Gypsum Product Manufacturing: Production Workers
    'AIES32742RCTUS', # Gypsum Product Manufacturing: Shipments
    'AIES32742TCMUS', # Gypsum Product Manufacturing: Total Cost of Materials
    ### 3279 Other Nonmetallic Mineral Product Manufacturing
    'AIES3279EMPUS', # Other Nonmetallic Mineral Product Manufacturing: Employees
    'AIES3279INFUS', # Other Nonmetallic Mineral Product Manufacturing: Finished Goods Inventories
    'AIES3279INMUS', # Other Nonmetallic Mineral Product Manufacturing: Materials and Supplies Inventories
    'AIES3279INVUS', # Other Nonmetallic Mineral Product Manufacturing: Total Inventories
    'AIES3279INWUS', # Other Nonmetallic Mineral Product Manufacturing: Work In Process Inventories
    'AIES3279PAYUS', # Other Nonmetallic Mineral Product Manufacturing: Annual Payroll
    'AIES3279PWEUS', # Other Nonmetallic Mineral Product Manufacturing: Production Workers
    'AIES3279RCTUS', # Other Nonmetallic Mineral Product Manufacturing: Shipments
    'AIES3279TCMUS', # Other Nonmetallic Mineral Product Manufacturing: Total Cost of Materials
    ### 32791 Abrasive Product Manufacturing
    'AIES32791EMPUS', # Abrasive Product Manufacturing: Employees
    'AIES32791INFUS', # Abrasive Product Manufacturing: Finished Goods Inventories
    'AIES32791INMUS', # Abrasive Product Manufacturing: Materials and Supplies Inventories
    'AIES32791INVUS', # Abrasive Product Manufacturing: Total Inventories
    'AIES32791INWUS', # Abrasive Product Manufacturing: Work In Process Inventories
    'AIES32791PAYUS', # Abrasive Product Manufacturing: Annual Payroll
    'AIES32791PWEUS', # Abrasive Product Manufacturing: Production Workers
    'AIES32791RCTUS', # Abrasive Product Manufacturing: Shipments
    'AIES32791TCMUS', # Abrasive Product Manufacturing: Total Cost of Materials
    ### 32799 All Other Nonmetallic Mineral Product Manufacturing
    'AIES32799EMPUS', # All Other Nonmetallic Mineral Product Manufacturing: Employees
    'AIES32799INFUS', # All Other Nonmetallic Mineral Product Manufacturing: Finished Goods Inventories
    'AIES32799INMUS', # All Other Nonmetallic Mineral Product Manufacturing: Materials and Supplies Inventories
    'AIES32799INVUS', # All Other Nonmetallic Mineral Product Manufacturing: Total Inventories
    'AIES32799INWUS', # All Other Nonmetallic Mineral Product Manufacturing: Work In Process Inventories
    'AIES32799PAYUS', # All Other Nonmetallic Mineral Product Manufacturing: Annual Payroll
    'AIES32799PWEUS', # All Other Nonmetallic Mineral Product Manufacturing: Production Workers
    'AIES32799RCTUS', # All Other Nonmetallic Mineral Product Manufacturing: Shipments
    'AIES32799TCMUS', # All Other Nonmetallic Mineral Product Manufacturing: Total Cost of Materials
    ### 327991 Cut Stone and Stone Product Manufacturing
    'AIES327991EMPUS', # Cut Stone and Stone Product Manufacturing: Employees
    'AIES327991INFUS', # Cut Stone and Stone Product Manufacturing: Finished Goods Inventories
    'AIES327991INMUS', # Cut Stone and Stone Product Manufacturing: Materials and Supplies Inventories
    'AIES327991INVUS', # Cut Stone and Stone Product Manufacturing: Total Inventories
    'AIES327991INWUS', # Cut Stone and Stone Product Manufacturing: Work In Process Inventories
    'AIES327991PAYUS', # Cut Stone and Stone Product Manufacturing: Annual Payroll
    'AIES327991PWEUS', # Cut Stone and Stone Product Manufacturing: Production Workers
    'AIES327991RCTUS', # Cut Stone and Stone Product Manufacturing: Shipments
    'AIES327991TCMUS', # Cut Stone and Stone Product Manufacturing: Total Cost of Materials
    ### 327992 Ground Or Treated Mineral and Earth Manufacturing
    'AIES327992EMPUS', # Ground Or Treated Mineral and Earth Manufacturing: Employees
    'AIES327992INFUS', # Ground Or Treated Mineral and Earth Manufacturing: Finished Goods Inventories
    'AIES327992INMUS', # Ground Or Treated Mineral and Earth Manufacturing: Materials and Supplies Inventories
    'AIES327992INVUS', # Ground Or Treated Mineral and Earth Manufacturing: Total Inventories
    'AIES327992INWUS', # Ground Or Treated Mineral and Earth Manufacturing: Work In Process Inventories
    'AIES327992PAYUS', # Ground Or Treated Mineral and Earth Manufacturing: Annual Payroll
    'AIES327992PWEUS', # Ground Or Treated Mineral and Earth Manufacturing: Production Workers
    'AIES327992RCTUS', # Ground Or Treated Mineral and Earth Manufacturing: Shipments
    'AIES327992TCMUS', # Ground Or Treated Mineral and Earth Manufacturing: Total Cost of Materials
    ### 327993 Mineral Wool Manufacturing
    'AIES327993EMPUS', # Mineral Wool Manufacturing: Employees
    'AIES327993INFUS', # Mineral Wool Manufacturing: Finished Goods Inventories
    'AIES327993INMUS', # Mineral Wool Manufacturing: Materials and Supplies Inventories
    'AIES327993INVUS', # Mineral Wool Manufacturing: Total Inventories
    'AIES327993INWUS', # Mineral Wool Manufacturing: Work In Process Inventories
    'AIES327993PAYUS', # Mineral Wool Manufacturing: Annual Payroll
    'AIES327993PWEUS', # Mineral Wool Manufacturing: Production Workers
    'AIES327993RCTUS', # Mineral Wool Manufacturing: Shipments
    'AIES327993TCMUS', # Mineral Wool Manufacturing: Total Cost of Materials
    ### 327999 Miscellaneous Nonmetallic Mineral Products Manufacturing
    'AIES327999EMPUS', # Miscellaneous Nonmetallic Mineral Products Manufacturing: Employees
    'AIES327999INFUS', # Miscellaneous Nonmetallic Mineral Products Manufacturing: Finished Goods Inventories
    'AIES327999INMUS', # Miscellaneous Nonmetallic Mineral Products Manufacturing: Materials and Supplies Inventories
    'AIES327999INVUS', # Miscellaneous Nonmetallic Mineral Products Manufacturing: Total Inventories
    'AIES327999INWUS', # Miscellaneous Nonmetallic Mineral Products Manufacturing: Work In Process Inventories
    'AIES327999PAYUS', # Miscellaneous Nonmetallic Mineral Products Manufacturing: Annual Payroll
    'AIES327999PWEUS', # Miscellaneous Nonmetallic Mineral Products Manufacturing: Production Workers
    'AIES327999RCTUS', # Miscellaneous Nonmetallic Mineral Products Manufacturing: Shipments
    'AIES327999TCMUS', # Miscellaneous Nonmetallic Mineral Products Manufacturing: Total Cost of Materials
    ## NAICS 331 Primary Metal Manufacturing
    ### 331 Primary Metal Manufacturing
    'AIES331EMPUS', # Primary Metal Manufacturing: Employees
    'AIES331INFUS', # Primary Metal Manufacturing: Finished Goods Inventories
    'AIES331INMUS', # Primary Metal Manufacturing: Materials and Supplies Inventories
    'AIES331INVUS', # Primary Metal Manufacturing: Total Inventories
    'AIES331INWUS', # Primary Metal Manufacturing: Work In Process Inventories
    'AIES331PAYUS', # Primary Metal Manufacturing: Annual Payroll
    'AIES331PWEUS', # Primary Metal Manufacturing: Production Workers
    'AIES331RCTUS', # Primary Metal Manufacturing: Shipments
    'AIES331TCMUS', # Primary Metal Manufacturing: Total Cost of Materials
    ### 3311 Iron and Steel Mills and Ferroalloy Manufacturing
    'AIES3311EMPUS', # Iron and Steel Mills and Ferroalloy Manufacturing: Employees
    'AIES3311INFUS', # Iron and Steel Mills and Ferroalloy Manufacturing: Finished Goods Inventories
    'AIES3311INMUS', # Iron and Steel Mills and Ferroalloy Manufacturing: Materials and Supplies Inventories
    'AIES3311INVUS', # Iron and Steel Mills and Ferroalloy Manufacturing: Total Inventories
    'AIES3311INWUS', # Iron and Steel Mills and Ferroalloy Manufacturing: Work In Process Inventories
    'AIES3311PAYUS', # Iron and Steel Mills and Ferroalloy Manufacturing: Annual Payroll
    'AIES3311PWEUS', # Iron and Steel Mills and Ferroalloy Manufacturing: Production Workers
    'AIES3311RCTUS', # Iron and Steel Mills and Ferroalloy Manufacturing: Shipments
    'AIES3311TCMUS', # Iron and Steel Mills and Ferroalloy Manufacturing: Total Cost of Materials
    ### 3312 Steel Product Manufacturing From Purchased Steel
    'AIES3312EMPUS', # Steel Product Manufacturing From Purchased Steel: Employees
    'AIES3312INFUS', # Steel Product Manufacturing From Purchased Steel: Finished Goods Inventories
    'AIES3312INMUS', # Steel Product Manufacturing From Purchased Steel: Materials and Supplies Inventories
    'AIES3312INVUS', # Steel Product Manufacturing From Purchased Steel: Total Inventories
    'AIES3312INWUS', # Steel Product Manufacturing From Purchased Steel: Work In Process Inventories
    'AIES3312PAYUS', # Steel Product Manufacturing From Purchased Steel: Annual Payroll
    'AIES3312PWEUS', # Steel Product Manufacturing From Purchased Steel: Production Workers
    'AIES3312RCTUS', # Steel Product Manufacturing From Purchased Steel: Shipments
    'AIES3312TCMUS', # Steel Product Manufacturing From Purchased Steel: Total Cost of Materials
    ### 33121 Iron and Steel Pipe and Tube Manufacturing From Purchased Steel
    'AIES33121EMPUS', # Iron and Steel Pipe and Tube Manufacturing From Purchased Steel: Employees
    'AIES33121INFUS', # Iron and Steel Pipe and Tube Manufacturing From Purchased Steel: Finished Goods Inventories
    'AIES33121INMUS', # Iron and Steel Pipe and Tube Manufacturing From Purchased Steel: Materials and Supplies Inventories
    'AIES33121INVUS', # Iron and Steel Pipe and Tube Manufacturing From Purchased Steel: Total Inventories
    'AIES33121INWUS', # Iron and Steel Pipe and Tube Manufacturing From Purchased Steel: Work In Process Inventories
    'AIES33121PAYUS', # Iron and Steel Pipe and Tube Manufacturing From Purchased Steel: Annual Payroll
    'AIES33121PWEUS', # Iron and Steel Pipe and Tube Manufacturing From Purchased Steel: Production Workers
    'AIES33121RCTUS', # Iron and Steel Pipe and Tube Manufacturing From Purchased Steel: Shipments
    'AIES33121TCMUS', # Iron and Steel Pipe and Tube Manufacturing From Purchased Steel: Total Cost of Materials
    ### 33122 Rolling and Drawing of Purchased Steel
    'AIES33122EMPUS', # Rolling and Drawing of Purchased Steel: Employees
    'AIES33122INFUS', # Rolling and Drawing of Purchased Steel: Finished Goods Inventories
    'AIES33122INMUS', # Rolling and Drawing of Purchased Steel: Materials and Supplies Inventories
    'AIES33122INVUS', # Rolling and Drawing of Purchased Steel: Total Inventories
    'AIES33122INWUS', # Rolling and Drawing of Purchased Steel: Work In Process Inventories
    'AIES33122PAYUS', # Rolling and Drawing of Purchased Steel: Annual Payroll
    'AIES33122PWEUS', # Rolling and Drawing of Purchased Steel: Production Workers
    'AIES33122RCTUS', # Rolling and Drawing of Purchased Steel: Shipments
    'AIES33122TCMUS', # Rolling and Drawing of Purchased Steel: Total Cost of Materials
    ### 331221 Rolled Steel Shape Manufacturing
    'AIES331221EMPUS', # Rolled Steel Shape Manufacturing: Employees
    'AIES331221INFUS', # Rolled Steel Shape Manufacturing: Finished Goods Inventories
    'AIES331221INMUS', # Rolled Steel Shape Manufacturing: Materials and Supplies Inventories
    'AIES331221INVUS', # Rolled Steel Shape Manufacturing: Total Inventories
    'AIES331221INWUS', # Rolled Steel Shape Manufacturing: Work In Process Inventories
    'AIES331221PAYUS', # Rolled Steel Shape Manufacturing: Annual Payroll
    'AIES331221PWEUS', # Rolled Steel Shape Manufacturing: Production Workers
    'AIES331221RCTUS', # Rolled Steel Shape Manufacturing: Shipments
    'AIES331221TCMUS', # Rolled Steel Shape Manufacturing: Total Cost of Materials
    ### 331222 Steel Wire Drawing
    'AIES331222EMPUS', # Steel Wire Drawing: Employees
    'AIES331222INFUS', # Steel Wire Drawing: Finished Goods Inventories
    'AIES331222INMUS', # Steel Wire Drawing: Materials and Supplies Inventories
    'AIES331222INVUS', # Steel Wire Drawing: Total Inventories
    'AIES331222INWUS', # Steel Wire Drawing: Work In Process Inventories
    'AIES331222PAYUS', # Steel Wire Drawing: Annual Payroll
    'AIES331222PWEUS', # Steel Wire Drawing: Production Workers
    'AIES331222RCTUS', # Steel Wire Drawing: Shipments
    'AIES331222TCMUS', # Steel Wire Drawing: Total Cost of Materials
    ### 3313 Alumina and Aluminum Production and Processing
    'AIES3313EMPUS', # Alumina and Aluminum Production and Processing: Employees
    'AIES3313INFUS', # Alumina and Aluminum Production and Processing: Finished Goods Inventories
    'AIES3313INMUS', # Alumina and Aluminum Production and Processing: Materials and Supplies Inventories
    'AIES3313INVUS', # Alumina and Aluminum Production and Processing: Total Inventories
    'AIES3313INWUS', # Alumina and Aluminum Production and Processing: Work In Process Inventories
    'AIES3313PAYUS', # Alumina and Aluminum Production and Processing: Annual Payroll
    'AIES3313PWEUS', # Alumina and Aluminum Production and Processing: Production Workers
    'AIES3313RCTUS', # Alumina and Aluminum Production and Processing: Shipments
    'AIES3313TCMUS', # Alumina and Aluminum Production and Processing: Total Cost of Materials
    ### 331313 Alumina Refining and Primary Aluminum Production
    'AIES331313EMPUS', # Alumina Refining and Primary Aluminum Production: Employees
    'AIES331313INFUS', # Alumina Refining and Primary Aluminum Production: Finished Goods Inventories
    'AIES331313INMUS', # Alumina Refining and Primary Aluminum Production: Materials and Supplies Inventories
    'AIES331313INVUS', # Alumina Refining and Primary Aluminum Production: Total Inventories
    'AIES331313INWUS', # Alumina Refining and Primary Aluminum Production: Work In Process Inventories
    'AIES331313PAYUS', # Alumina Refining and Primary Aluminum Production: Annual Payroll
    'AIES331313PWEUS', # Alumina Refining and Primary Aluminum Production: Production Workers
    'AIES331313RCTUS', # Alumina Refining and Primary Aluminum Production: Shipments
    'AIES331313TCMUS', # Alumina Refining and Primary Aluminum Production: Total Cost of Materials
    ### 331314 Secondary Smelting and Alloying of Aluminum
    'AIES331314EMPUS', # Secondary Smelting and Alloying of Aluminum: Employees
    'AIES331314INFUS', # Secondary Smelting and Alloying of Aluminum: Finished Goods Inventories
    'AIES331314INMUS', # Secondary Smelting and Alloying of Aluminum: Materials and Supplies Inventories
    'AIES331314INVUS', # Secondary Smelting and Alloying of Aluminum: Total Inventories
    'AIES331314INWUS', # Secondary Smelting and Alloying of Aluminum: Work In Process Inventories
    'AIES331314PAYUS', # Secondary Smelting and Alloying of Aluminum: Annual Payroll
    'AIES331314PWEUS', # Secondary Smelting and Alloying of Aluminum: Production Workers
    'AIES331314RCTUS', # Secondary Smelting and Alloying of Aluminum: Shipments
    'AIES331314TCMUS', # Secondary Smelting and Alloying of Aluminum: Total Cost of Materials
    ### 331315 Aluminum Sheet, Plate, and Foil Manufacturing
    'AIES331315EMPUS', # Aluminum Sheet, Plate, and Foil Manufacturing: Employees
    'AIES331315INFUS', # Aluminum Sheet, Plate, and Foil Manufacturing: Finished Goods Inventories
    'AIES331315INMUS', # Aluminum Sheet, Plate, and Foil Manufacturing: Materials and Supplies Inventories
    'AIES331315INVUS', # Aluminum Sheet, Plate, and Foil Manufacturing: Total Inventories
    'AIES331315INWUS', # Aluminum Sheet, Plate, and Foil Manufacturing: Work In Process Inventories
    'AIES331315PAYUS', # Aluminum Sheet, Plate, and Foil Manufacturing: Annual Payroll
    'AIES331315PWEUS', # Aluminum Sheet, Plate, and Foil Manufacturing: Production Workers
    'AIES331315RCTUS', # Aluminum Sheet, Plate, and Foil Manufacturing: Shipments
    'AIES331315TCMUS', # Aluminum Sheet, Plate, and Foil Manufacturing: Total Cost of Materials
    ### 331318 Other Aluminum Rolling, Drawing, and Extruding
    'AIES331318EMPUS', # Other Aluminum Rolling, Drawing, and Extruding: Employees
    'AIES331318INFUS', # Other Aluminum Rolling, Drawing, and Extruding: Finished Goods Inventories
    'AIES331318INMUS', # Other Aluminum Rolling, Drawing, and Extruding: Materials and Supplies Inventories
    'AIES331318INVUS', # Other Aluminum Rolling, Drawing, and Extruding: Total Inventories
    'AIES331318INWUS', # Other Aluminum Rolling, Drawing, and Extruding: Work In Process Inventories
    'AIES331318PAYUS', # Other Aluminum Rolling, Drawing, and Extruding: Annual Payroll
    'AIES331318PWEUS', # Other Aluminum Rolling, Drawing, and Extruding: Production Workers
    'AIES331318RCTUS', # Other Aluminum Rolling, Drawing, and Extruding: Shipments
    'AIES331318TCMUS', # Other Aluminum Rolling, Drawing, and Extruding: Total Cost of Materials
    ### 3314 Nonferrous Metal (Except Aluminum) Production and Processing
    'AIES3314EMPUS', # Nonferrous Metal (Except Aluminum) Production and Processing: Employees
    'AIES3314INFUS', # Nonferrous Metal (Except Aluminum) Production and Processing: Finished Goods Inventories
    'AIES3314INMUS', # Nonferrous Metal (Except Aluminum) Production and Processing: Materials and Supplies Inventories
    'AIES3314INVUS', # Nonferrous Metal (Except Aluminum) Production and Processing: Total Inventories
    'AIES3314INWUS', # Nonferrous Metal (Except Aluminum) Production and Processing: Work In Process Inventories
    'AIES3314PAYUS', # Nonferrous Metal (Except Aluminum) Production and Processing: Annual Payroll
    'AIES3314PWEUS', # Nonferrous Metal (Except Aluminum) Production and Processing: Production Workers
    'AIES3314RCTUS', # Nonferrous Metal (Except Aluminum) Production and Processing: Shipments
    'AIES3314TCMUS', # Nonferrous Metal (Except Aluminum) Production and Processing: Total Cost of Materials
    ### 33141 Nonferrous Metal (Except Aluminum) Smelting and Refining
    'AIES33141EMPUS', # Nonferrous Metal (Except Aluminum) Smelting and Refining: Employees
    'AIES33141INFUS', # Nonferrous Metal (Except Aluminum) Smelting and Refining: Finished Goods Inventories
    'AIES33141INMUS', # Nonferrous Metal (Except Aluminum) Smelting and Refining: Materials and Supplies Inventories
    'AIES33141INVUS', # Nonferrous Metal (Except Aluminum) Smelting and Refining: Total Inventories
    'AIES33141INWUS', # Nonferrous Metal (Except Aluminum) Smelting and Refining: Work In Process Inventories
    'AIES33141PAYUS', # Nonferrous Metal (Except Aluminum) Smelting and Refining: Annual Payroll
    'AIES33141PWEUS', # Nonferrous Metal (Except Aluminum) Smelting and Refining: Production Workers
    'AIES33141RCTUS', # Nonferrous Metal (Except Aluminum) Smelting and Refining: Shipments
    'AIES33141TCMUS', # Nonferrous Metal (Except Aluminum) Smelting and Refining: Total Cost of Materials
    ### 33142 Copper Rolling, Drawing, Extruding, and Alloying
    'AIES33142EMPUS', # Copper Rolling, Drawing, Extruding, and Alloying: Employees
    'AIES33142INFUS', # Copper Rolling, Drawing, Extruding, and Alloying: Finished Goods Inventories
    'AIES33142INMUS', # Copper Rolling, Drawing, Extruding, and Alloying: Materials and Supplies Inventories
    'AIES33142INVUS', # Copper Rolling, Drawing, Extruding, and Alloying: Total Inventories
    'AIES33142INWUS', # Copper Rolling, Drawing, Extruding, and Alloying: Work In Process Inventories
    'AIES33142PAYUS', # Copper Rolling, Drawing, Extruding, and Alloying: Annual Payroll
    'AIES33142PWEUS', # Copper Rolling, Drawing, Extruding, and Alloying: Production Workers
    'AIES33142RCTUS', # Copper Rolling, Drawing, Extruding, and Alloying: Shipments
    'AIES33142TCMUS', # Copper Rolling, Drawing, Extruding, and Alloying: Total Cost of Materials
    ### 33149 Nonferrous Metal, Except Cu and Al, Shaping
    'AIES33149EMPUS', # Nonferrous Metal, Except Cu and Al, Shaping: Employees
    'AIES33149INFUS', # Nonferrous Metal, Except Cu and Al, Shaping: Finished Goods Inventories
    'AIES33149INMUS', # Nonferrous Metal, Except Cu and Al, Shaping: Materials and Supplies Inventories
    'AIES33149INVUS', # Nonferrous Metal, Except Cu and Al, Shaping: Total Inventories
    'AIES33149INWUS', # Nonferrous Metal, Except Cu and Al, Shaping: Work In Process Inventories
    'AIES33149PAYUS', # Nonferrous Metal, Except Cu and Al, Shaping: Annual Payroll
    'AIES33149PWEUS', # Nonferrous Metal, Except Cu and Al, Shaping: Production Workers
    'AIES33149RCTUS', # Nonferrous Metal, Except Cu and Al, Shaping: Shipments
    'AIES33149TCMUS', # Nonferrous Metal, Except Cu and Al, Shaping: Total Cost of Materials
    ### 331492 Secondary Processing of Other Nonferrous
    'AIES331492EMPUS', # Secondary Processing of Other Nonferrous: Employees
    'AIES331492INFUS', # Secondary Processing of Other Nonferrous: Finished Goods Inventories
    'AIES331492INMUS', # Secondary Processing of Other Nonferrous: Materials and Supplies Inventories
    'AIES331492INVUS', # Secondary Processing of Other Nonferrous: Total Inventories
    'AIES331492INWUS', # Secondary Processing of Other Nonferrous: Work In Process Inventories
    'AIES331492PAYUS', # Secondary Processing of Other Nonferrous: Annual Payroll
    'AIES331492PWEUS', # Secondary Processing of Other Nonferrous: Production Workers
    'AIES331492RCTUS', # Secondary Processing of Other Nonferrous: Shipments
    'AIES331492TCMUS', # Secondary Processing of Other Nonferrous: Total Cost of Materials
    ### 3315 Foundries
    'AIES3315EMPUS', # Foundries: Employees
    'AIES3315INFUS', # Foundries: Finished Goods Inventories
    'AIES3315INMUS', # Foundries: Materials and Supplies Inventories
    'AIES3315INVUS', # Foundries: Total Inventories
    'AIES3315INWUS', # Foundries: Work In Process Inventories
    'AIES3315PAYUS', # Foundries: Annual Payroll
    'AIES3315PWEUS', # Foundries: Production Workers
    'AIES3315RCTUS', # Foundries: Shipments
    'AIES3315TCMUS', # Foundries: Total Cost of Materials
    ### 33151 Ferrous Metal Foundries
    'AIES33151EMPUS', # Ferrous Metal Foundries: Employees
    'AIES33151INFUS', # Ferrous Metal Foundries: Finished Goods Inventories
    'AIES33151INMUS', # Ferrous Metal Foundries: Materials and Supplies Inventories
    'AIES33151INVUS', # Ferrous Metal Foundries: Total Inventories
    'AIES33151INWUS', # Ferrous Metal Foundries: Work In Process Inventories
    'AIES33151PAYUS', # Ferrous Metal Foundries: Annual Payroll
    'AIES33151PWEUS', # Ferrous Metal Foundries: Production Workers
    'AIES33151RCTUS', # Ferrous Metal Foundries: Shipments
    'AIES33151TCMUS', # Ferrous Metal Foundries: Total Cost of Materials
    ### 331511 Iron Foundries
    'AIES331511EMPUS', # Iron Foundries: Employees
    'AIES331511INFUS', # Iron Foundries: Finished Goods Inventories
    'AIES331511INMUS', # Iron Foundries: Materials and Supplies Inventories
    'AIES331511INVUS', # Iron Foundries: Total Inventories
    'AIES331511INWUS', # Iron Foundries: Work In Process Inventories
    'AIES331511PAYUS', # Iron Foundries: Annual Payroll
    'AIES331511PWEUS', # Iron Foundries: Production Workers
    'AIES331511RCTUS', # Iron Foundries: Shipments
    'AIES331511TCMUS', # Iron Foundries: Total Cost of Materials
    ### 331512 Steel Investment Foundries
    'AIES331512EMPUS', # Steel Investment Foundries: Employees
    'AIES331512INFUS', # Steel Investment Foundries: Finished Goods Inventories
    'AIES331512INMUS', # Steel Investment Foundries: Materials and Supplies Inventories
    'AIES331512INVUS', # Steel Investment Foundries: Total Inventories
    'AIES331512INWUS', # Steel Investment Foundries: Work In Process Inventories
    'AIES331512PAYUS', # Steel Investment Foundries: Annual Payroll
    'AIES331512PWEUS', # Steel Investment Foundries: Production Workers
    'AIES331512RCTUS', # Steel Investment Foundries: Shipments
    'AIES331512TCMUS', # Steel Investment Foundries: Total Cost of Materials
    ### 331513 Steel Foundries (Except Investment)
    'AIES331513EMPUS', # Steel Foundries (Except Investment): Employees
    'AIES331513INFUS', # Steel Foundries (Except Investment): Finished Goods Inventories
    'AIES331513INMUS', # Steel Foundries (Except Investment): Materials and Supplies Inventories
    'AIES331513INVUS', # Steel Foundries (Except Investment): Total Inventories
    'AIES331513INWUS', # Steel Foundries (Except Investment): Work In Process Inventories
    'AIES331513PAYUS', # Steel Foundries (Except Investment): Annual Payroll
    'AIES331513PWEUS', # Steel Foundries (Except Investment): Production Workers
    'AIES331513RCTUS', # Steel Foundries (Except Investment): Shipments
    'AIES331513TCMUS', # Steel Foundries (Except Investment): Total Cost of Materials
    ### 33152 Nonferrous Metal Foundries
    'AIES33152EMPUS', # Nonferrous Metal Foundries: Employees
    'AIES33152INFUS', # Nonferrous Metal Foundries: Finished Goods Inventories
    'AIES33152INMUS', # Nonferrous Metal Foundries: Materials and Supplies Inventories
    'AIES33152INVUS', # Nonferrous Metal Foundries: Total Inventories
    'AIES33152INWUS', # Nonferrous Metal Foundries: Work In Process Inventories
    'AIES33152PAYUS', # Nonferrous Metal Foundries: Annual Payroll
    'AIES33152PWEUS', # Nonferrous Metal Foundries: Production Workers
    'AIES33152RCTUS', # Nonferrous Metal Foundries: Shipments
    'AIES33152TCMUS', # Nonferrous Metal Foundries: Total Cost of Materials
    ### 331523 Nonferrous Metal Die-Casting Foundries
    'AIES331523EMPUS', # Nonferrous Metal Die-Casting Foundries: Employees
    'AIES331523INFUS', # Nonferrous Metal Die-Casting Foundries: Finished Goods Inventories
    'AIES331523INMUS', # Nonferrous Metal Die-Casting Foundries: Materials and Supplies Inventories
    'AIES331523INVUS', # Nonferrous Metal Die-Casting Foundries: Total Inventories
    'AIES331523INWUS', # Nonferrous Metal Die-Casting Foundries: Work In Process Inventories
    'AIES331523PAYUS', # Nonferrous Metal Die-Casting Foundries: Annual Payroll
    'AIES331523PWEUS', # Nonferrous Metal Die-Casting Foundries: Production Workers
    'AIES331523RCTUS', # Nonferrous Metal Die-Casting Foundries: Shipments
    'AIES331523TCMUS', # Nonferrous Metal Die-Casting Foundries: Total Cost of Materials
    ### 331524 Aluminum Foundries (Except Die-Casting)
    'AIES331524EMPUS', # Aluminum Foundries (Except Die-Casting): Employees
    'AIES331524INFUS', # Aluminum Foundries (Except Die-Casting): Finished Goods Inventories
    'AIES331524INMUS', # Aluminum Foundries (Except Die-Casting): Materials and Supplies Inventories
    'AIES331524INVUS', # Aluminum Foundries (Except Die-Casting): Total Inventories
    'AIES331524INWUS', # Aluminum Foundries (Except Die-Casting): Work In Process Inventories
    'AIES331524PAYUS', # Aluminum Foundries (Except Die-Casting): Annual Payroll
    'AIES331524PWEUS', # Aluminum Foundries (Except Die-Casting): Production Workers
    'AIES331524RCTUS', # Aluminum Foundries (Except Die-Casting): Shipments
    'AIES331524TCMUS', # Aluminum Foundries (Except Die-Casting): Total Cost of Materials
    ### 331529 Other Nonferrous Metal Foundries (Except Die-Casting)
    'AIES331529EMPUS', # Other Nonferrous Metal Foundries (Except Die-Casting): Employees
    'AIES331529INFUS', # Other Nonferrous Metal Foundries (Except Die-Casting): Finished Goods Inventories
    'AIES331529INMUS', # Other Nonferrous Metal Foundries (Except Die-Casting): Materials and Supplies Inventories
    'AIES331529INVUS', # Other Nonferrous Metal Foundries (Except Die-Casting): Total Inventories
    'AIES331529INWUS', # Other Nonferrous Metal Foundries (Except Die-Casting): Work In Process Inventories
    'AIES331529PAYUS', # Other Nonferrous Metal Foundries (Except Die-Casting): Annual Payroll
    'AIES331529PWEUS', # Other Nonferrous Metal Foundries (Except Die-Casting): Production Workers
    'AIES331529RCTUS', # Other Nonferrous Metal Foundries (Except Die-Casting): Shipments
    'AIES331529TCMUS', # Other Nonferrous Metal Foundries (Except Die-Casting): Total Cost of Materials
    ## NAICS 332 Fabricated Metal Product Manufacturing
    ### 332 Fabricated Metal Product Manufacturing
    'AIES332EMPUS', # Fabricated Metal Product Manufacturing: Employees
    'AIES332INFUS', # Fabricated Metal Product Manufacturing: Finished Goods Inventories
    'AIES332INMUS', # Fabricated Metal Product Manufacturing: Materials and Supplies Inventories
    'AIES332INVUS', # Fabricated Metal Product Manufacturing: Total Inventories
    'AIES332INWUS', # Fabricated Metal Product Manufacturing: Work In Process Inventories
    'AIES332PAYUS', # Fabricated Metal Product Manufacturing: Annual Payroll
    'AIES332PWEUS', # Fabricated Metal Product Manufacturing: Production Workers
    'AIES332RCTUS', # Fabricated Metal Product Manufacturing: Shipments
    'AIES332TCMUS', # Fabricated Metal Product Manufacturing: Total Cost of Materials
    ### 3321 Forging and Stamping
    'AIES3321EMPUS', # Forging and Stamping: Employees
    'AIES3321INFUS', # Forging and Stamping: Finished Goods Inventories
    'AIES3321INMUS', # Forging and Stamping: Materials and Supplies Inventories
    'AIES3321INVUS', # Forging and Stamping: Total Inventories
    'AIES3321INWUS', # Forging and Stamping: Work In Process Inventories
    'AIES3321PAYUS', # Forging and Stamping: Annual Payroll
    'AIES3321PWEUS', # Forging and Stamping: Production Workers
    'AIES3321RCTUS', # Forging and Stamping: Shipments
    'AIES3321TCMUS', # Forging and Stamping: Total Cost of Materials
    ### 332111 Iron and Steel Forging
    'AIES332111EMPUS', # Iron and Steel Forging: Employees
    'AIES332111INFUS', # Iron and Steel Forging: Finished Goods Inventories
    'AIES332111INMUS', # Iron and Steel Forging: Materials and Supplies Inventories
    'AIES332111INVUS', # Iron and Steel Forging: Total Inventories
    'AIES332111INWUS', # Iron and Steel Forging: Work In Process Inventories
    'AIES332111PAYUS', # Iron and Steel Forging: Annual Payroll
    'AIES332111PWEUS', # Iron and Steel Forging: Production Workers
    'AIES332111RCTUS', # Iron and Steel Forging: Shipments
    'AIES332111TCMUS', # Iron and Steel Forging: Total Cost of Materials
    ### 332112 Nonferrous Forging
    'AIES332112EMPUS', # Nonferrous Forging: Employees
    'AIES332112INFUS', # Nonferrous Forging: Finished Goods Inventories
    'AIES332112INMUS', # Nonferrous Forging: Materials and Supplies Inventories
    'AIES332112INVUS', # Nonferrous Forging: Total Inventories
    'AIES332112INWUS', # Nonferrous Forging: Work In Process Inventories
    'AIES332112PAYUS', # Nonferrous Forging: Annual Payroll
    'AIES332112PWEUS', # Nonferrous Forging: Production Workers
    'AIES332112RCTUS', # Nonferrous Forging: Shipments
    'AIES332112TCMUS', # Nonferrous Forging: Total Cost of Materials
    ### 332114 Custom Roll Forming
    'AIES332114EMPUS', # Custom Roll Forming: Employees
    'AIES332114INFUS', # Custom Roll Forming: Finished Goods Inventories
    'AIES332114INMUS', # Custom Roll Forming: Materials and Supplies Inventories
    'AIES332114INVUS', # Custom Roll Forming: Total Inventories
    'AIES332114INWUS', # Custom Roll Forming: Work In Process Inventories
    'AIES332114PAYUS', # Custom Roll Forming: Annual Payroll
    'AIES332114PWEUS', # Custom Roll Forming: Production Workers
    'AIES332114RCTUS', # Custom Roll Forming: Shipments
    'AIES332114TCMUS', # Custom Roll Forming: Total Cost of Materials
    ### 332117 Powder Metallurgy Part Manufacturing
    'AIES332117EMPUS', # Powder Metallurgy Part Manufacturing: Employees
    'AIES332117INFUS', # Powder Metallurgy Part Manufacturing: Finished Goods Inventories
    'AIES332117INMUS', # Powder Metallurgy Part Manufacturing: Materials and Supplies Inventories
    'AIES332117INVUS', # Powder Metallurgy Part Manufacturing: Total Inventories
    'AIES332117INWUS', # Powder Metallurgy Part Manufacturing: Work In Process Inventories
    'AIES332117PAYUS', # Powder Metallurgy Part Manufacturing: Annual Payroll
    'AIES332117PWEUS', # Powder Metallurgy Part Manufacturing: Production Workers
    'AIES332117RCTUS', # Powder Metallurgy Part Manufacturing: Shipments
    'AIES332117TCMUS', # Powder Metallurgy Part Manufacturing: Total Cost of Materials
    ### 332119 Other Metal Stamping, Except Automotive
    'AIES332119EMPUS', # Other Metal Stamping, Except Automotive: Employees
    'AIES332119INFUS', # Other Metal Stamping, Except Automotive: Finished Goods Inventories
    'AIES332119INMUS', # Other Metal Stamping, Except Automotive: Materials and Supplies Inventories
    'AIES332119INVUS', # Other Metal Stamping, Except Automotive: Total Inventories
    'AIES332119INWUS', # Other Metal Stamping, Except Automotive: Work In Process Inventories
    'AIES332119PAYUS', # Other Metal Stamping, Except Automotive: Annual Payroll
    'AIES332119PWEUS', # Other Metal Stamping, Except Automotive: Production Workers
    'AIES332119RCTUS', # Other Metal Stamping, Except Automotive: Shipments
    'AIES332119TCMUS', # Other Metal Stamping, Except Automotive: Total Cost of Materials
    ### 3322 Cutlery and Handtool Manufacturing
    'AIES3322EMPUS', # Cutlery and Handtool Manufacturing: Employees
    'AIES3322INFUS', # Cutlery and Handtool Manufacturing: Finished Goods Inventories
    'AIES3322INMUS', # Cutlery and Handtool Manufacturing: Materials and Supplies Inventories
    'AIES3322INVUS', # Cutlery and Handtool Manufacturing: Total Inventories
    'AIES3322INWUS', # Cutlery and Handtool Manufacturing: Work In Process Inventories
    'AIES3322PAYUS', # Cutlery and Handtool Manufacturing: Annual Payroll
    'AIES3322PWEUS', # Cutlery and Handtool Manufacturing: Production Workers
    'AIES3322RCTUS', # Cutlery and Handtool Manufacturing: Shipments
    'AIES3322TCMUS', # Cutlery and Handtool Manufacturing: Total Cost of Materials
    ### 332215 Metal Cookware, Cutlery, and Flatware Manufacturing
    'AIES332215EMPUS', # Metal Cookware, Cutlery, and Flatware Manufacturing: Employees
    'AIES332215INFUS', # Metal Cookware, Cutlery, and Flatware Manufacturing: Finished Goods Inventories
    'AIES332215INMUS', # Metal Cookware, Cutlery, and Flatware Manufacturing: Materials and Supplies Inventories
    'AIES332215INVUS', # Metal Cookware, Cutlery, and Flatware Manufacturing: Total Inventories
    'AIES332215INWUS', # Metal Cookware, Cutlery, and Flatware Manufacturing: Work In Process Inventories
    'AIES332215PAYUS', # Metal Cookware, Cutlery, and Flatware Manufacturing: Annual Payroll
    'AIES332215PWEUS', # Metal Cookware, Cutlery, and Flatware Manufacturing: Production Workers
    'AIES332215RCTUS', # Metal Cookware, Cutlery, and Flatware Manufacturing: Shipments
    'AIES332215TCMUS', # Metal Cookware, Cutlery, and Flatware Manufacturing: Total Cost of Materials
    ### 332216 Saw Blade and Handtool Manufacturing
    'AIES332216EMPUS', # Saw Blade and Handtool Manufacturing: Employees
    'AIES332216INFUS', # Saw Blade and Handtool Manufacturing: Finished Goods Inventories
    'AIES332216INMUS', # Saw Blade and Handtool Manufacturing: Materials and Supplies Inventories
    'AIES332216INVUS', # Saw Blade and Handtool Manufacturing: Total Inventories
    'AIES332216INWUS', # Saw Blade and Handtool Manufacturing: Work In Process Inventories
    'AIES332216PAYUS', # Saw Blade and Handtool Manufacturing: Annual Payroll
    'AIES332216PWEUS', # Saw Blade and Handtool Manufacturing: Production Workers
    'AIES332216RCTUS', # Saw Blade and Handtool Manufacturing: Shipments
    'AIES332216TCMUS', # Saw Blade and Handtool Manufacturing: Total Cost of Materials
    ### 3323 Architectural and Structural Metals Manufacturing
    'AIES3323EMPUS', # Architectural and Structural Metals Manufacturing: Employees
    'AIES3323INFUS', # Architectural and Structural Metals Manufacturing: Finished Goods Inventories
    'AIES3323INMUS', # Architectural and Structural Metals Manufacturing: Materials and Supplies Inventories
    'AIES3323INVUS', # Architectural and Structural Metals Manufacturing: Total Inventories
    'AIES3323INWUS', # Architectural and Structural Metals Manufacturing: Work In Process Inventories
    'AIES3323PAYUS', # Architectural and Structural Metals Manufacturing: Annual Payroll
    'AIES3323PWEUS', # Architectural and Structural Metals Manufacturing: Production Workers
    'AIES3323RCTUS', # Architectural and Structural Metals Manufacturing: Shipments
    'AIES3323TCMUS', # Architectural and Structural Metals Manufacturing: Total Cost of Materials
    ### 33231 Plate Work and Fabricated Structural Product Manufacturing
    'AIES33231EMPUS', # Plate Work and Fabricated Structural Product Manufacturing: Employees
    'AIES33231INFUS', # Plate Work and Fabricated Structural Product Manufacturing: Finished Goods Inventories
    'AIES33231INMUS', # Plate Work and Fabricated Structural Product Manufacturing: Materials and Supplies Inventories
    'AIES33231INVUS', # Plate Work and Fabricated Structural Product Manufacturing: Total Inventories
    'AIES33231INWUS', # Plate Work and Fabricated Structural Product Manufacturing: Work In Process Inventories
    'AIES33231PAYUS', # Plate Work and Fabricated Structural Product Manufacturing: Annual Payroll
    'AIES33231PWEUS', # Plate Work and Fabricated Structural Product Manufacturing: Production Workers
    'AIES33231RCTUS', # Plate Work and Fabricated Structural Product Manufacturing: Shipments
    'AIES33231TCMUS', # Plate Work and Fabricated Structural Product Manufacturing: Total Cost of Materials
    ### 332311 Prefabricated Metal Building and Component Manufacturing
    'AIES332311EMPUS', # Prefabricated Metal Building and Component Manufacturing: Employees
    'AIES332311INFUS', # Prefabricated Metal Building and Component Manufacturing: Finished Goods Inventories
    'AIES332311INMUS', # Prefabricated Metal Building and Component Manufacturing: Materials and Supplies Inventories
    'AIES332311INVUS', # Prefabricated Metal Building and Component Manufacturing: Total Inventories
    'AIES332311INWUS', # Prefabricated Metal Building and Component Manufacturing: Work In Process Inventories
    'AIES332311PAYUS', # Prefabricated Metal Building and Component Manufacturing: Annual Payroll
    'AIES332311PWEUS', # Prefabricated Metal Building and Component Manufacturing: Production Workers
    'AIES332311RCTUS', # Prefabricated Metal Building and Component Manufacturing: Shipments
    'AIES332311TCMUS', # Prefabricated Metal Building and Component Manufacturing: Total Cost of Materials
    ### 332312 Fabricated Structural Metal Manufacturing
    'AIES332312EMPUS', # Fabricated Structural Metal Manufacturing: Employees
    'AIES332312INFUS', # Fabricated Structural Metal Manufacturing: Finished Goods Inventories
    'AIES332312INMUS', # Fabricated Structural Metal Manufacturing: Materials and Supplies Inventories
    'AIES332312INVUS', # Fabricated Structural Metal Manufacturing: Total Inventories
    'AIES332312INWUS', # Fabricated Structural Metal Manufacturing: Work In Process Inventories
    'AIES332312PAYUS', # Fabricated Structural Metal Manufacturing: Annual Payroll
    'AIES332312PWEUS', # Fabricated Structural Metal Manufacturing: Production Workers
    'AIES332312RCTUS', # Fabricated Structural Metal Manufacturing: Shipments
    'AIES332312TCMUS', # Fabricated Structural Metal Manufacturing: Total Cost of Materials
    ### 332313 Plate Work Manufacturing
    'AIES332313EMPUS', # Plate Work Manufacturing: Employees
    'AIES332313INFUS', # Plate Work Manufacturing: Finished Goods Inventories
    'AIES332313INMUS', # Plate Work Manufacturing: Materials and Supplies Inventories
    'AIES332313INVUS', # Plate Work Manufacturing: Total Inventories
    'AIES332313INWUS', # Plate Work Manufacturing: Work In Process Inventories
    'AIES332313PAYUS', # Plate Work Manufacturing: Annual Payroll
    'AIES332313PWEUS', # Plate Work Manufacturing: Production Workers
    'AIES332313RCTUS', # Plate Work Manufacturing: Shipments
    'AIES332313TCMUS', # Plate Work Manufacturing: Total Cost of Materials
    ### 33232 Ornamental and Architectural Metal Products Manufacturing
    'AIES33232EMPUS', # Ornamental and Architectural Metal Products Manufacturing: Employees
    'AIES33232INFUS', # Ornamental and Architectural Metal Products Manufacturing: Finished Goods Inventories
    'AIES33232INMUS', # Ornamental and Architectural Metal Products Manufacturing: Materials and Supplies Inventories
    'AIES33232INVUS', # Ornamental and Architectural Metal Products Manufacturing: Total Inventories
    'AIES33232INWUS', # Ornamental and Architectural Metal Products Manufacturing: Work In Process Inventories
    'AIES33232PAYUS', # Ornamental and Architectural Metal Products Manufacturing: Annual Payroll
    'AIES33232PWEUS', # Ornamental and Architectural Metal Products Manufacturing: Production Workers
    'AIES33232RCTUS', # Ornamental and Architectural Metal Products Manufacturing: Shipments
    'AIES33232TCMUS', # Ornamental and Architectural Metal Products Manufacturing: Total Cost of Materials
    ### 332321 Metal Window and Door Manufacturing
    'AIES332321EMPUS', # Metal Window and Door Manufacturing: Employees
    'AIES332321INFUS', # Metal Window and Door Manufacturing: Finished Goods Inventories
    'AIES332321INMUS', # Metal Window and Door Manufacturing: Materials and Supplies Inventories
    'AIES332321INVUS', # Metal Window and Door Manufacturing: Total Inventories
    'AIES332321INWUS', # Metal Window and Door Manufacturing: Work In Process Inventories
    'AIES332321PAYUS', # Metal Window and Door Manufacturing: Annual Payroll
    'AIES332321PWEUS', # Metal Window and Door Manufacturing: Production Workers
    'AIES332321RCTUS', # Metal Window and Door Manufacturing: Shipments
    'AIES332321TCMUS', # Metal Window and Door Manufacturing: Total Cost of Materials
    ### 332322 Sheet Metal Work Manufacturing
    'AIES332322EMPUS', # Sheet Metal Work Manufacturing: Employees
    'AIES332322INFUS', # Sheet Metal Work Manufacturing: Finished Goods Inventories
    'AIES332322INMUS', # Sheet Metal Work Manufacturing: Materials and Supplies Inventories
    'AIES332322INVUS', # Sheet Metal Work Manufacturing: Total Inventories
    'AIES332322INWUS', # Sheet Metal Work Manufacturing: Work In Process Inventories
    'AIES332322PAYUS', # Sheet Metal Work Manufacturing: Annual Payroll
    'AIES332322PWEUS', # Sheet Metal Work Manufacturing: Production Workers
    'AIES332322RCTUS', # Sheet Metal Work Manufacturing: Shipments
    'AIES332322TCMUS', # Sheet Metal Work Manufacturing: Total Cost of Materials
    ### 332323 Ornamental and Architectural Metal Work Manufacturing
    'AIES332323EMPUS', # Ornamental and Architectural Metal Work Manufacturing: Employees
    'AIES332323INFUS', # Ornamental and Architectural Metal Work Manufacturing: Finished Goods Inventories
    'AIES332323INMUS', # Ornamental and Architectural Metal Work Manufacturing: Materials and Supplies Inventories
    'AIES332323INVUS', # Ornamental and Architectural Metal Work Manufacturing: Total Inventories
    'AIES332323INWUS', # Ornamental and Architectural Metal Work Manufacturing: Work In Process Inventories
    'AIES332323PAYUS', # Ornamental and Architectural Metal Work Manufacturing: Annual Payroll
    'AIES332323PWEUS', # Ornamental and Architectural Metal Work Manufacturing: Production Workers
    'AIES332323RCTUS', # Ornamental and Architectural Metal Work Manufacturing: Shipments
    'AIES332323TCMUS', # Ornamental and Architectural Metal Work Manufacturing: Total Cost of Materials
    ### 3324 Boiler, Tank, and Shipping Container Manufacturing
    'AIES3324EMPUS', # Boiler, Tank, and Shipping Container Manufacturing: Employees
    'AIES3324INFUS', # Boiler, Tank, and Shipping Container Manufacturing: Finished Goods Inventories
    'AIES3324INMUS', # Boiler, Tank, and Shipping Container Manufacturing: Materials and Supplies Inventories
    'AIES3324INVUS', # Boiler, Tank, and Shipping Container Manufacturing: Total Inventories
    'AIES3324INWUS', # Boiler, Tank, and Shipping Container Manufacturing: Work In Process Inventories
    'AIES3324PAYUS', # Boiler, Tank, and Shipping Container Manufacturing: Annual Payroll
    'AIES3324PWEUS', # Boiler, Tank, and Shipping Container Manufacturing: Production Workers
    'AIES3324RCTUS', # Boiler, Tank, and Shipping Container Manufacturing: Shipments
    'AIES3324TCMUS', # Boiler, Tank, and Shipping Container Manufacturing: Total Cost of Materials
    ### 33241 Power Boiler and Heat Exchanger Manufacturing
    'AIES33241EMPUS', # Power Boiler and Heat Exchanger Manufacturing: Employees
    'AIES33241INFUS', # Power Boiler and Heat Exchanger Manufacturing: Finished Goods Inventories
    'AIES33241INMUS', # Power Boiler and Heat Exchanger Manufacturing: Materials and Supplies Inventories
    'AIES33241INVUS', # Power Boiler and Heat Exchanger Manufacturing: Total Inventories
    'AIES33241INWUS', # Power Boiler and Heat Exchanger Manufacturing: Work In Process Inventories
    'AIES33241PAYUS', # Power Boiler and Heat Exchanger Manufacturing: Annual Payroll
    'AIES33241PWEUS', # Power Boiler and Heat Exchanger Manufacturing: Production Workers
    'AIES33241RCTUS', # Power Boiler and Heat Exchanger Manufacturing: Shipments
    'AIES33241TCMUS', # Power Boiler and Heat Exchanger Manufacturing: Total Cost of Materials
    ### 33242 Metal Tank (Heavy Gauge) Manufacturing
    'AIES33242EMPUS', # Metal Tank (Heavy Gauge) Manufacturing: Employees
    'AIES33242INFUS', # Metal Tank (Heavy Gauge) Manufacturing: Finished Goods Inventories
    'AIES33242INMUS', # Metal Tank (Heavy Gauge) Manufacturing: Materials and Supplies Inventories
    'AIES33242INVUS', # Metal Tank (Heavy Gauge) Manufacturing: Total Inventories
    'AIES33242INWUS', # Metal Tank (Heavy Gauge) Manufacturing: Work In Process Inventories
    'AIES33242PAYUS', # Metal Tank (Heavy Gauge) Manufacturing: Annual Payroll
    'AIES33242PWEUS', # Metal Tank (Heavy Gauge) Manufacturing: Production Workers
    'AIES33242RCTUS', # Metal Tank (Heavy Gauge) Manufacturing: Shipments
    'AIES33242TCMUS', # Metal Tank (Heavy Gauge) Manufacturing: Total Cost of Materials
    ### 33243 Metal Can, Box, and Other Container Manufacturing
    'AIES33243EMPUS', # Metal Can, Box, and Other Container Manufacturing: Employees
    'AIES33243INFUS', # Metal Can, Box, and Other Container Manufacturing: Finished Goods Inventories
    'AIES33243INMUS', # Metal Can, Box, and Other Container Manufacturing: Materials and Supplies Inventories
    'AIES33243INVUS', # Metal Can, Box, and Other Container Manufacturing: Total Inventories
    'AIES33243INWUS', # Metal Can, Box, and Other Container Manufacturing: Work In Process Inventories
    'AIES33243PAYUS', # Metal Can, Box, and Other Container Manufacturing: Annual Payroll
    'AIES33243PWEUS', # Metal Can, Box, and Other Container Manufacturing: Production Workers
    'AIES33243RCTUS', # Metal Can, Box, and Other Container Manufacturing: Shipments
    'AIES33243TCMUS', # Metal Can, Box, and Other Container Manufacturing: Total Cost of Materials
    ### 332431 Metal Can Manufacturing
    'AIES332431EMPUS', # Metal Can Manufacturing: Employees
    'AIES332431INFUS', # Metal Can Manufacturing: Finished Goods Inventories
    'AIES332431INMUS', # Metal Can Manufacturing: Materials and Supplies Inventories
    'AIES332431INVUS', # Metal Can Manufacturing: Total Inventories
    'AIES332431INWUS', # Metal Can Manufacturing: Work In Process Inventories
    'AIES332431PAYUS', # Metal Can Manufacturing: Annual Payroll
    'AIES332431PWEUS', # Metal Can Manufacturing: Production Workers
    'AIES332431RCTUS', # Metal Can Manufacturing: Shipments
    'AIES332431TCMUS', # Metal Can Manufacturing: Total Cost of Materials
    ### 332439 Other Metal Container Manufacturing
    'AIES332439EMPUS', # Other Metal Container Manufacturing: Employees
    'AIES332439INFUS', # Other Metal Container Manufacturing: Finished Goods Inventories
    'AIES332439INMUS', # Other Metal Container Manufacturing: Materials and Supplies Inventories
    'AIES332439INVUS', # Other Metal Container Manufacturing: Total Inventories
    'AIES332439INWUS', # Other Metal Container Manufacturing: Work In Process Inventories
    'AIES332439PAYUS', # Other Metal Container Manufacturing: Annual Payroll
    'AIES332439PWEUS', # Other Metal Container Manufacturing: Production Workers
    'AIES332439RCTUS', # Other Metal Container Manufacturing: Shipments
    'AIES332439TCMUS', # Other Metal Container Manufacturing: Total Cost of Materials
    ### 3325 Hardware Manufacturing
    'AIES3325EMPUS', # Hardware Manufacturing: Employees
    'AIES3325INFUS', # Hardware Manufacturing: Finished Goods Inventories
    'AIES3325INMUS', # Hardware Manufacturing: Materials and Supplies Inventories
    'AIES3325INVUS', # Hardware Manufacturing: Total Inventories
    'AIES3325INWUS', # Hardware Manufacturing: Work In Process Inventories
    'AIES3325PAYUS', # Hardware Manufacturing: Annual Payroll
    'AIES3325PWEUS', # Hardware Manufacturing: Production Workers
    'AIES3325RCTUS', # Hardware Manufacturing: Shipments
    'AIES3325TCMUS', # Hardware Manufacturing: Total Cost of Materials
    ### 3326 Spring and Wire Product Manufacturing
    'AIES3326EMPUS', # Spring and Wire Product Manufacturing: Employees
    'AIES3326INFUS', # Spring and Wire Product Manufacturing: Finished Goods Inventories
    'AIES3326INMUS', # Spring and Wire Product Manufacturing: Materials and Supplies Inventories
    'AIES3326INVUS', # Spring and Wire Product Manufacturing: Total Inventories
    'AIES3326INWUS', # Spring and Wire Product Manufacturing: Work In Process Inventories
    'AIES3326PAYUS', # Spring and Wire Product Manufacturing: Annual Payroll
    'AIES3326PWEUS', # Spring and Wire Product Manufacturing: Production Workers
    'AIES3326RCTUS', # Spring and Wire Product Manufacturing: Shipments
    'AIES3326TCMUS', # Spring and Wire Product Manufacturing: Total Cost of Materials
    ### 332613 Spring Manufacturing
    'AIES332613EMPUS', # Spring Manufacturing: Employees
    'AIES332613INFUS', # Spring Manufacturing: Finished Goods Inventories
    'AIES332613INMUS', # Spring Manufacturing: Materials and Supplies Inventories
    'AIES332613INVUS', # Spring Manufacturing: Total Inventories
    'AIES332613INWUS', # Spring Manufacturing: Work In Process Inventories
    'AIES332613PAYUS', # Spring Manufacturing: Annual Payroll
    'AIES332613PWEUS', # Spring Manufacturing: Production Workers
    'AIES332613RCTUS', # Spring Manufacturing: Shipments
    'AIES332613TCMUS', # Spring Manufacturing: Total Cost of Materials
    ### 332618 Other Fabricated Wire Product Manufacturing
    'AIES332618EMPUS', # Other Fabricated Wire Product Manufacturing: Employees
    'AIES332618INFUS', # Other Fabricated Wire Product Manufacturing: Finished Goods Inventories
    'AIES332618INMUS', # Other Fabricated Wire Product Manufacturing: Materials and Supplies Inventories
    'AIES332618INVUS', # Other Fabricated Wire Product Manufacturing: Total Inventories
    'AIES332618INWUS', # Other Fabricated Wire Product Manufacturing: Work In Process Inventories
    'AIES332618PAYUS', # Other Fabricated Wire Product Manufacturing: Annual Payroll
    'AIES332618PWEUS', # Other Fabricated Wire Product Manufacturing: Production Workers
    'AIES332618RCTUS', # Other Fabricated Wire Product Manufacturing: Shipments
    'AIES332618TCMUS', # Other Fabricated Wire Product Manufacturing: Total Cost of Materials
    ### 3327 Machine Shops and Threaded Product Manufacturing
    'AIES3327EMPUS', # Machine Shops and Threaded Product Manufacturing: Employees
    'AIES3327INFUS', # Machine Shops and Threaded Product Manufacturing: Finished Goods Inventories
    'AIES3327INMUS', # Machine Shops and Threaded Product Manufacturing: Materials and Supplies Inventories
    'AIES3327INVUS', # Machine Shops and Threaded Product Manufacturing: Total Inventories
    'AIES3327INWUS', # Machine Shops and Threaded Product Manufacturing: Work In Process Inventories
    'AIES3327PAYUS', # Machine Shops and Threaded Product Manufacturing: Annual Payroll
    'AIES3327PWEUS', # Machine Shops and Threaded Product Manufacturing: Production Workers
    'AIES3327RCTUS', # Machine Shops and Threaded Product Manufacturing: Shipments
    'AIES3327TCMUS', # Machine Shops and Threaded Product Manufacturing: Total Cost of Materials
    ### 33271 Machine Shops
    'AIES33271EMPUS', # Machine Shops: Employees
    'AIES33271INFUS', # Machine Shops: Finished Goods Inventories
    'AIES33271INMUS', # Machine Shops: Materials and Supplies Inventories
    'AIES33271INVUS', # Machine Shops: Total Inventories
    'AIES33271INWUS', # Machine Shops: Work In Process Inventories
    'AIES33271PAYUS', # Machine Shops: Annual Payroll
    'AIES33271PWEUS', # Machine Shops: Production Workers
    'AIES33271RCTUS', # Machine Shops: Shipments
    'AIES33271TCMUS', # Machine Shops: Total Cost of Materials
    ### 33272 Turned Product and Screw, Nut, and Bolt Manufacturing
    'AIES33272EMPUS', # Turned Product and Screw, Nut, and Bolt Manufacturing: Employees
    'AIES33272INFUS', # Turned Product and Screw, Nut, and Bolt Manufacturing: Finished Goods Inventories
    'AIES33272INMUS', # Turned Product and Screw, Nut, and Bolt Manufacturing: Materials and Supplies Inventories
    'AIES33272INVUS', # Turned Product and Screw, Nut, and Bolt Manufacturing: Total Inventories
    'AIES33272INWUS', # Turned Product and Screw, Nut, and Bolt Manufacturing: Work In Process Inventories
    'AIES33272PAYUS', # Turned Product and Screw, Nut, and Bolt Manufacturing: Annual Payroll
    'AIES33272PWEUS', # Turned Product and Screw, Nut, and Bolt Manufacturing: Production Workers
    'AIES33272RCTUS', # Turned Product and Screw, Nut, and Bolt Manufacturing: Shipments
    'AIES33272TCMUS', # Turned Product and Screw, Nut, and Bolt Manufacturing: Total Cost of Materials
    ### 332721 Precision Turned Product Manufacturing
    'AIES332721EMPUS', # Precision Turned Product Manufacturing: Employees
    'AIES332721INFUS', # Precision Turned Product Manufacturing: Finished Goods Inventories
    'AIES332721INMUS', # Precision Turned Product Manufacturing: Materials and Supplies Inventories
    'AIES332721INVUS', # Precision Turned Product Manufacturing: Total Inventories
    'AIES332721INWUS', # Precision Turned Product Manufacturing: Work In Process Inventories
    'AIES332721PAYUS', # Precision Turned Product Manufacturing: Annual Payroll
    'AIES332721PWEUS', # Precision Turned Product Manufacturing: Production Workers
    'AIES332721RCTUS', # Precision Turned Product Manufacturing: Shipments
    'AIES332721TCMUS', # Precision Turned Product Manufacturing: Total Cost of Materials
    ### 332722 Bolt, Nut, Screw, Rivet, and Washer Manufacturing
    'AIES332722EMPUS', # Bolt, Nut, Screw, Rivet, and Washer Manufacturing: Employees
    'AIES332722INFUS', # Bolt, Nut, Screw, Rivet, and Washer Manufacturing: Finished Goods Inventories
    'AIES332722INMUS', # Bolt, Nut, Screw, Rivet, and Washer Manufacturing: Materials and Supplies Inventories
    'AIES332722INVUS', # Bolt, Nut, Screw, Rivet, and Washer Manufacturing: Total Inventories
    'AIES332722INWUS', # Bolt, Nut, Screw, Rivet, and Washer Manufacturing: Work In Process Inventories
    'AIES332722PAYUS', # Bolt, Nut, Screw, Rivet, and Washer Manufacturing: Annual Payroll
    'AIES332722PWEUS', # Bolt, Nut, Screw, Rivet, and Washer Manufacturing: Production Workers
    'AIES332722RCTUS', # Bolt, Nut, Screw, Rivet, and Washer Manufacturing: Shipments
    'AIES332722TCMUS', # Bolt, Nut, Screw, Rivet, and Washer Manufacturing: Total Cost of Materials
    ### 3328 Coating, Engraving, Heat Treating, and Allied Activities
    'AIES3328EMPUS', # Coating, Engraving, Heat Treating, and Allied Activities: Employees
    'AIES3328INFUS', # Coating, Engraving, Heat Treating, and Allied Activities: Finished Goods Inventories
    'AIES3328INMUS', # Coating, Engraving, Heat Treating, and Allied Activities: Materials and Supplies Inventories
    'AIES3328INVUS', # Coating, Engraving, Heat Treating, and Allied Activities: Total Inventories
    'AIES3328INWUS', # Coating, Engraving, Heat Treating, and Allied Activities: Work In Process Inventories
    'AIES3328PAYUS', # Coating, Engraving, Heat Treating, and Allied Activities: Annual Payroll
    'AIES3328PWEUS', # Coating, Engraving, Heat Treating, and Allied Activities: Production Workers
    'AIES3328RCTUS', # Coating, Engraving, Heat Treating, and Allied Activities: Shipments
    'AIES3328TCMUS', # Coating, Engraving, Heat Treating, and Allied Activities: Total Cost of Materials
    ### 332811 Metal Heat Treating
    'AIES332811EMPUS', # Metal Heat Treating: Employees
    'AIES332811INFUS', # Metal Heat Treating: Finished Goods Inventories
    'AIES332811INMUS', # Metal Heat Treating: Materials and Supplies Inventories
    'AIES332811INVUS', # Metal Heat Treating: Total Inventories
    'AIES332811INWUS', # Metal Heat Treating: Work In Process Inventories
    'AIES332811PAYUS', # Metal Heat Treating: Annual Payroll
    'AIES332811PWEUS', # Metal Heat Treating: Production Workers
    'AIES332811RCTUS', # Metal Heat Treating: Shipments
    'AIES332811TCMUS', # Metal Heat Treating: Total Cost of Materials
    ### 332812 Metal Coating and Nonprecious Engraving
    'AIES332812EMPUS', # Metal Coating and Nonprecious Engraving: Employees
    'AIES332812INFUS', # Metal Coating and Nonprecious Engraving: Finished Goods Inventories
    'AIES332812INMUS', # Metal Coating and Nonprecious Engraving: Materials and Supplies Inventories
    'AIES332812INVUS', # Metal Coating and Nonprecious Engraving: Total Inventories
    'AIES332812INWUS', # Metal Coating and Nonprecious Engraving: Work In Process Inventories
    'AIES332812PAYUS', # Metal Coating and Nonprecious Engraving: Annual Payroll
    'AIES332812PWEUS', # Metal Coating and Nonprecious Engraving: Production Workers
    'AIES332812RCTUS', # Metal Coating and Nonprecious Engraving: Shipments
    'AIES332812TCMUS', # Metal Coating and Nonprecious Engraving: Total Cost of Materials
    ### 332813 Electroplating, Plating, Polishing, Anodizing, and Coloring
    'AIES332813EMPUS', # Electroplating, Plating, Polishing, Anodizing, and Coloring: Employees
    'AIES332813INFUS', # Electroplating, Plating, Polishing, Anodizing, and Coloring: Finished Goods Inventories
    'AIES332813INMUS', # Electroplating, Plating, Polishing, Anodizing, and Coloring: Materials and Supplies Inventories
    'AIES332813INVUS', # Electroplating, Plating, Polishing, Anodizing, and Coloring: Total Inventories
    'AIES332813INWUS', # Electroplating, Plating, Polishing, Anodizing, and Coloring: Work In Process Inventories
    'AIES332813PAYUS', # Electroplating, Plating, Polishing, Anodizing, and Coloring: Annual Payroll
    'AIES332813PWEUS', # Electroplating, Plating, Polishing, Anodizing, and Coloring: Production Workers
    'AIES332813RCTUS', # Electroplating, Plating, Polishing, Anodizing, and Coloring: Shipments
    'AIES332813TCMUS', # Electroplating, Plating, Polishing, Anodizing, and Coloring: Total Cost of Materials
    ### 3329 Other Fabricated Metal Product Manufacturing
    'AIES3329EMPUS', # Other Fabricated Metal Product Manufacturing: Employees
    'AIES3329INFUS', # Other Fabricated Metal Product Manufacturing: Finished Goods Inventories
    'AIES3329INMUS', # Other Fabricated Metal Product Manufacturing: Materials and Supplies Inventories
    'AIES3329INVUS', # Other Fabricated Metal Product Manufacturing: Total Inventories
    'AIES3329INWUS', # Other Fabricated Metal Product Manufacturing: Work In Process Inventories
    'AIES3329PAYUS', # Other Fabricated Metal Product Manufacturing: Annual Payroll
    'AIES3329PWEUS', # Other Fabricated Metal Product Manufacturing: Production Workers
    'AIES3329RCTUS', # Other Fabricated Metal Product Manufacturing: Shipments
    'AIES3329TCMUS', # Other Fabricated Metal Product Manufacturing: Total Cost of Materials
    ### 33291 Metal Valve Manufacturing
    'AIES33291EMPUS', # Metal Valve Manufacturing: Employees
    'AIES33291INFUS', # Metal Valve Manufacturing: Finished Goods Inventories
    'AIES33291INMUS', # Metal Valve Manufacturing: Materials and Supplies Inventories
    'AIES33291INVUS', # Metal Valve Manufacturing: Total Inventories
    'AIES33291INWUS', # Metal Valve Manufacturing: Work In Process Inventories
    'AIES33291PAYUS', # Metal Valve Manufacturing: Annual Payroll
    'AIES33291PWEUS', # Metal Valve Manufacturing: Production Workers
    'AIES33291RCTUS', # Metal Valve Manufacturing: Shipments
    'AIES33291TCMUS', # Metal Valve Manufacturing: Total Cost of Materials
    ### 332911 Industrial Valve Manufacturing
    'AIES332911EMPUS', # Industrial Valve Manufacturing: Employees
    'AIES332911INFUS', # Industrial Valve Manufacturing: Finished Goods Inventories
    'AIES332911INMUS', # Industrial Valve Manufacturing: Materials and Supplies Inventories
    'AIES332911INVUS', # Industrial Valve Manufacturing: Total Inventories
    'AIES332911INWUS', # Industrial Valve Manufacturing: Work In Process Inventories
    'AIES332911PAYUS', # Industrial Valve Manufacturing: Annual Payroll
    'AIES332911PWEUS', # Industrial Valve Manufacturing: Production Workers
    'AIES332911RCTUS', # Industrial Valve Manufacturing: Shipments
    'AIES332911TCMUS', # Industrial Valve Manufacturing: Total Cost of Materials
    ### 332912 Fluid Power Valve and Hose Fitting Manufacturing
    'AIES332912EMPUS', # Fluid Power Valve and Hose Fitting Manufacturing: Employees
    'AIES332912INFUS', # Fluid Power Valve and Hose Fitting Manufacturing: Finished Goods Inventories
    'AIES332912INMUS', # Fluid Power Valve and Hose Fitting Manufacturing: Materials and Supplies Inventories
    'AIES332912INVUS', # Fluid Power Valve and Hose Fitting Manufacturing: Total Inventories
    'AIES332912INWUS', # Fluid Power Valve and Hose Fitting Manufacturing: Work In Process Inventories
    'AIES332912PAYUS', # Fluid Power Valve and Hose Fitting Manufacturing: Annual Payroll
    'AIES332912PWEUS', # Fluid Power Valve and Hose Fitting Manufacturing: Production Workers
    'AIES332912RCTUS', # Fluid Power Valve and Hose Fitting Manufacturing: Shipments
    'AIES332912TCMUS', # Fluid Power Valve and Hose Fitting Manufacturing: Total Cost of Materials
    ### 332913 Plumbing Fixture Fitting and Trim Manufacturing
    'AIES332913EMPUS', # Plumbing Fixture Fitting and Trim Manufacturing: Employees
    'AIES332913INFUS', # Plumbing Fixture Fitting and Trim Manufacturing: Finished Goods Inventories
    'AIES332913INMUS', # Plumbing Fixture Fitting and Trim Manufacturing: Materials and Supplies Inventories
    'AIES332913INVUS', # Plumbing Fixture Fitting and Trim Manufacturing: Total Inventories
    'AIES332913INWUS', # Plumbing Fixture Fitting and Trim Manufacturing: Work In Process Inventories
    'AIES332913PAYUS', # Plumbing Fixture Fitting and Trim Manufacturing: Annual Payroll
    'AIES332913PWEUS', # Plumbing Fixture Fitting and Trim Manufacturing: Production Workers
    'AIES332913RCTUS', # Plumbing Fixture Fitting and Trim Manufacturing: Shipments
    'AIES332913TCMUS', # Plumbing Fixture Fitting and Trim Manufacturing: Total Cost of Materials
    ### 332919 Other Metal Valve and Pipe Fitting Manufacturing
    'AIES332919EMPUS', # Other Metal Valve and Pipe Fitting Manufacturing: Employees
    'AIES332919INFUS', # Other Metal Valve and Pipe Fitting Manufacturing: Finished Goods Inventories
    'AIES332919INMUS', # Other Metal Valve and Pipe Fitting Manufacturing: Materials and Supplies Inventories
    'AIES332919INVUS', # Other Metal Valve and Pipe Fitting Manufacturing: Total Inventories
    'AIES332919INWUS', # Other Metal Valve and Pipe Fitting Manufacturing: Work In Process Inventories
    'AIES332919PAYUS', # Other Metal Valve and Pipe Fitting Manufacturing: Annual Payroll
    'AIES332919PWEUS', # Other Metal Valve and Pipe Fitting Manufacturing: Production Workers
    'AIES332919RCTUS', # Other Metal Valve and Pipe Fitting Manufacturing: Shipments
    'AIES332919TCMUS', # Other Metal Valve and Pipe Fitting Manufacturing: Total Cost of Materials
    ### 33299 All Other Fabricated Metal Product Manufacturing
    'AIES33299EMPUS', # All Other Fabricated Metal Product Manufacturing: Employees
    'AIES33299INFUS', # All Other Fabricated Metal Product Manufacturing: Finished Goods Inventories
    'AIES33299INMUS', # All Other Fabricated Metal Product Manufacturing: Materials and Supplies Inventories
    'AIES33299INVUS', # All Other Fabricated Metal Product Manufacturing: Total Inventories
    'AIES33299INWUS', # All Other Fabricated Metal Product Manufacturing: Work In Process Inventories
    'AIES33299PAYUS', # All Other Fabricated Metal Product Manufacturing: Annual Payroll
    'AIES33299PWEUS', # All Other Fabricated Metal Product Manufacturing: Production Workers
    'AIES33299RCTUS', # All Other Fabricated Metal Product Manufacturing: Shipments
    'AIES33299TCMUS', # All Other Fabricated Metal Product Manufacturing: Total Cost of Materials
    ### 332991 Ball and Roller Bearing Manufacturing
    'AIES332991EMPUS', # Ball and Roller Bearing Manufacturing: Employees
    'AIES332991INFUS', # Ball and Roller Bearing Manufacturing: Finished Goods Inventories
    'AIES332991INMUS', # Ball and Roller Bearing Manufacturing: Materials and Supplies Inventories
    'AIES332991INVUS', # Ball and Roller Bearing Manufacturing: Total Inventories
    'AIES332991INWUS', # Ball and Roller Bearing Manufacturing: Work In Process Inventories
    'AIES332991PAYUS', # Ball and Roller Bearing Manufacturing: Annual Payroll
    'AIES332991PWEUS', # Ball and Roller Bearing Manufacturing: Production Workers
    'AIES332991RCTUS', # Ball and Roller Bearing Manufacturing: Shipments
    'AIES332991TCMUS', # Ball and Roller Bearing Manufacturing: Total Cost of Materials
    ### 332992 Small Arms Ammunition Manufacturing
    'AIES332992EMPUS', # Small Arms Ammunition Manufacturing: Employees
    'AIES332992INFUS', # Small Arms Ammunition Manufacturing: Finished Goods Inventories
    'AIES332992INMUS', # Small Arms Ammunition Manufacturing: Materials and Supplies Inventories
    'AIES332992INVUS', # Small Arms Ammunition Manufacturing: Total Inventories
    'AIES332992INWUS', # Small Arms Ammunition Manufacturing: Work In Process Inventories
    'AIES332992PAYUS', # Small Arms Ammunition Manufacturing: Annual Payroll
    'AIES332992PWEUS', # Small Arms Ammunition Manufacturing: Production Workers
    'AIES332992RCTUS', # Small Arms Ammunition Manufacturing: Shipments
    'AIES332992TCMUS', # Small Arms Ammunition Manufacturing: Total Cost of Materials
    ### 332993 Ammunition (Except Small Arms) Manufacturing
    'AIES332993EMPUS', # Ammunition (Except Small Arms) Manufacturing: Employees
    'AIES332993INFUS', # Ammunition (Except Small Arms) Manufacturing: Finished Goods Inventories
    'AIES332993INMUS', # Ammunition (Except Small Arms) Manufacturing: Materials and Supplies Inventories
    'AIES332993INVUS', # Ammunition (Except Small Arms) Manufacturing: Total Inventories
    'AIES332993INWUS', # Ammunition (Except Small Arms) Manufacturing: Work In Process Inventories
    'AIES332993PAYUS', # Ammunition (Except Small Arms) Manufacturing: Annual Payroll
    'AIES332993PWEUS', # Ammunition (Except Small Arms) Manufacturing: Production Workers
    'AIES332993RCTUS', # Ammunition (Except Small Arms) Manufacturing: Shipments
    'AIES332993TCMUS', # Ammunition (Except Small Arms) Manufacturing: Total Cost of Materials
    ### 332994 Small Arms, Ordnance, and Ordnance Accessories Manufacturing
    'AIES332994EMPUS', # Small Arms, Ordnance, and Ordnance Accessories Manufacturing: Employees
    'AIES332994INFUS', # Small Arms, Ordnance, and Ordnance Accessories Manufacturing: Finished Goods Inventories
    'AIES332994INMUS', # Small Arms, Ordnance, and Ordnance Accessories Manufacturing: Materials and Supplies Inventories
    'AIES332994INVUS', # Small Arms, Ordnance, and Ordnance Accessories Manufacturing: Total Inventories
    'AIES332994INWUS', # Small Arms, Ordnance, and Ordnance Accessories Manufacturing: Work In Process Inventories
    'AIES332994PAYUS', # Small Arms, Ordnance, and Ordnance Accessories Manufacturing: Annual Payroll
    'AIES332994PWEUS', # Small Arms, Ordnance, and Ordnance Accessories Manufacturing: Production Workers
    'AIES332994RCTUS', # Small Arms, Ordnance, and Ordnance Accessories Manufacturing: Shipments
    'AIES332994TCMUS', # Small Arms, Ordnance, and Ordnance Accessories Manufacturing: Total Cost of Materials
    ### 332996 Fabricated Pipe and Pipe Fitting Manufacturing
    'AIES332996EMPUS', # Fabricated Pipe and Pipe Fitting Manufacturing: Employees
    'AIES332996INFUS', # Fabricated Pipe and Pipe Fitting Manufacturing: Finished Goods Inventories
    'AIES332996INMUS', # Fabricated Pipe and Pipe Fitting Manufacturing: Materials and Supplies Inventories
    'AIES332996INVUS', # Fabricated Pipe and Pipe Fitting Manufacturing: Total Inventories
    'AIES332996INWUS', # Fabricated Pipe and Pipe Fitting Manufacturing: Work In Process Inventories
    'AIES332996PAYUS', # Fabricated Pipe and Pipe Fitting Manufacturing: Annual Payroll
    'AIES332996PWEUS', # Fabricated Pipe and Pipe Fitting Manufacturing: Production Workers
    'AIES332996RCTUS', # Fabricated Pipe and Pipe Fitting Manufacturing: Shipments
    'AIES332996TCMUS', # Fabricated Pipe and Pipe Fitting Manufacturing: Total Cost of Materials
    ### 332999 All Other Miscellaneous Fabricated Metal Product Manufacturing
    'AIES332999EMPUS', # All Other Miscellaneous Fabricated Metal Product Manufacturing: Employees
    'AIES332999INFUS', # All Other Miscellaneous Fabricated Metal Product Manufacturing: Finished Goods Inventories
    'AIES332999INMUS', # All Other Miscellaneous Fabricated Metal Product Manufacturing: Materials and Supplies Inventories
    'AIES332999INVUS', # All Other Miscellaneous Fabricated Metal Product Manufacturing: Total Inventories
    'AIES332999INWUS', # All Other Miscellaneous Fabricated Metal Product Manufacturing: Work In Process Inventories
    'AIES332999PAYUS', # All Other Miscellaneous Fabricated Metal Product Manufacturing: Annual Payroll
    'AIES332999PWEUS', # All Other Miscellaneous Fabricated Metal Product Manufacturing: Production Workers
    'AIES332999RCTUS', # All Other Miscellaneous Fabricated Metal Product Manufacturing: Shipments
    'AIES332999TCMUS', # All Other Miscellaneous Fabricated Metal Product Manufacturing: Total Cost of Materials
    ## NAICS 333 Machinery Manufacturing
    ### 333 Machinery Manufacturing
    'AIES333EMPUS', # Machinery Manufacturing: Employees
    'AIES333INFUS', # Machinery Manufacturing: Finished Goods Inventories
    'AIES333INMUS', # Machinery Manufacturing: Materials and Supplies Inventories
    'AIES333INVUS', # Machinery Manufacturing: Total Inventories
    'AIES333INWUS', # Machinery Manufacturing: Work In Process Inventories
    'AIES333PAYUS', # Machinery Manufacturing: Annual Payroll
    'AIES333PWEUS', # Machinery Manufacturing: Production Workers
    'AIES333RCTUS', # Machinery Manufacturing: Shipments
    'AIES333TCMUS', # Machinery Manufacturing: Total Cost of Materials
    ### 3331 Agriculture, Construction, and Mining Machinery Manufacturing
    'AIES3331EMPUS', # Agriculture, Construction, and Mining Machinery Manufacturing: Employees
    'AIES3331INFUS', # Agriculture, Construction, and Mining Machinery Manufacturing: Finished Goods Inventories
    'AIES3331INMUS', # Agriculture, Construction, and Mining Machinery Manufacturing: Materials and Supplies Inventories
    'AIES3331INVUS', # Agriculture, Construction, and Mining Machinery Manufacturing: Total Inventories
    'AIES3331INWUS', # Agriculture, Construction, and Mining Machinery Manufacturing: Work In Process Inventories
    'AIES3331PAYUS', # Agriculture, Construction, and Mining Machinery Manufacturing: Annual Payroll
    'AIES3331PWEUS', # Agriculture, Construction, and Mining Machinery Manufacturing: Production Workers
    'AIES3331RCTUS', # Agriculture, Construction, and Mining Machinery Manufacturing: Shipments
    'AIES3331TCMUS', # Agriculture, Construction, and Mining Machinery Manufacturing: Total Cost of Materials
    ### 33311 Agricultural Implement Manufacturing
    'AIES33311EMPUS', # Agricultural Implement Manufacturing: Employees
    'AIES33311INFUS', # Agricultural Implement Manufacturing: Finished Goods Inventories
    'AIES33311INMUS', # Agricultural Implement Manufacturing: Materials and Supplies Inventories
    'AIES33311INVUS', # Agricultural Implement Manufacturing: Total Inventories
    'AIES33311INWUS', # Agricultural Implement Manufacturing: Work In Process Inventories
    'AIES33311PAYUS', # Agricultural Implement Manufacturing: Annual Payroll
    'AIES33311PWEUS', # Agricultural Implement Manufacturing: Production Workers
    'AIES33311RCTUS', # Agricultural Implement Manufacturing: Shipments
    'AIES33311TCMUS', # Agricultural Implement Manufacturing: Total Cost of Materials
    ### 333111 Farm Machinery and Equipment Manufacturing
    'AIES333111EMPUS', # Farm Machinery and Equipment Manufacturing: Employees
    'AIES333111INFUS', # Farm Machinery and Equipment Manufacturing: Finished Goods Inventories
    'AIES333111INMUS', # Farm Machinery and Equipment Manufacturing: Materials and Supplies Inventories
    'AIES333111INVUS', # Farm Machinery and Equipment Manufacturing: Total Inventories
    'AIES333111INWUS', # Farm Machinery and Equipment Manufacturing: Work In Process Inventories
    'AIES333111PAYUS', # Farm Machinery and Equipment Manufacturing: Annual Payroll
    'AIES333111PWEUS', # Farm Machinery and Equipment Manufacturing: Production Workers
    'AIES333111RCTUS', # Farm Machinery and Equipment Manufacturing: Shipments
    'AIES333111TCMUS', # Farm Machinery and Equipment Manufacturing: Total Cost of Materials
    ### 333112 Lawn and Garden Equipment Manufacturing
    'AIES333112EMPUS', # Lawn and Garden Equipment Manufacturing: Employees
    'AIES333112INFUS', # Lawn and Garden Equipment Manufacturing: Finished Goods Inventories
    'AIES333112INMUS', # Lawn and Garden Equipment Manufacturing: Materials and Supplies Inventories
    'AIES333112INVUS', # Lawn and Garden Equipment Manufacturing: Total Inventories
    'AIES333112INWUS', # Lawn and Garden Equipment Manufacturing: Work In Process Inventories
    'AIES333112PAYUS', # Lawn and Garden Equipment Manufacturing: Annual Payroll
    'AIES333112PWEUS', # Lawn and Garden Equipment Manufacturing: Production Workers
    'AIES333112RCTUS', # Lawn and Garden Equipment Manufacturing: Shipments
    'AIES333112TCMUS', # Lawn and Garden Equipment Manufacturing: Total Cost of Materials
    ### 33312 Construction Machinery Manufacturing
    'AIES33312EMPUS', # Construction Machinery Manufacturing: Employees
    'AIES33312INFUS', # Construction Machinery Manufacturing: Finished Goods Inventories
    'AIES33312INMUS', # Construction Machinery Manufacturing: Materials and Supplies Inventories
    'AIES33312INVUS', # Construction Machinery Manufacturing: Total Inventories
    'AIES33312INWUS', # Construction Machinery Manufacturing: Work In Process Inventories
    'AIES33312PAYUS', # Construction Machinery Manufacturing: Annual Payroll
    'AIES33312PWEUS', # Construction Machinery Manufacturing: Production Workers
    'AIES33312RCTUS', # Construction Machinery Manufacturing: Shipments
    'AIES33312TCMUS', # Construction Machinery Manufacturing: Total Cost of Materials
    ### 33313 Mining and Oil and Gas Field Machinery Manufacturing
    'AIES33313EMPUS', # Mining and Oil and Gas Field Machinery Manufacturing: Employees
    'AIES33313INFUS', # Mining and Oil and Gas Field Machinery Manufacturing: Finished Goods Inventories
    'AIES33313INMUS', # Mining and Oil and Gas Field Machinery Manufacturing: Materials and Supplies Inventories
    'AIES33313INVUS', # Mining and Oil and Gas Field Machinery Manufacturing: Total Inventories
    'AIES33313INWUS', # Mining and Oil and Gas Field Machinery Manufacturing: Work In Process Inventories
    'AIES33313PAYUS', # Mining and Oil and Gas Field Machinery Manufacturing: Annual Payroll
    'AIES33313PWEUS', # Mining and Oil and Gas Field Machinery Manufacturing: Production Workers
    'AIES33313RCTUS', # Mining and Oil and Gas Field Machinery Manufacturing: Shipments
    'AIES33313TCMUS', # Mining and Oil and Gas Field Machinery Manufacturing: Total Cost of Materials
    ### 333131 Mining Machinery and Equipment Manufacturing
    'AIES333131EMPUS', # Mining Machinery and Equipment Manufacturing: Employees
    'AIES333131INFUS', # Mining Machinery and Equipment Manufacturing: Finished Goods Inventories
    'AIES333131INMUS', # Mining Machinery and Equipment Manufacturing: Materials and Supplies Inventories
    'AIES333131INVUS', # Mining Machinery and Equipment Manufacturing: Total Inventories
    'AIES333131INWUS', # Mining Machinery and Equipment Manufacturing: Work In Process Inventories
    'AIES333131PAYUS', # Mining Machinery and Equipment Manufacturing: Annual Payroll
    'AIES333131PWEUS', # Mining Machinery and Equipment Manufacturing: Production Workers
    'AIES333131RCTUS', # Mining Machinery and Equipment Manufacturing: Shipments
    'AIES333131TCMUS', # Mining Machinery and Equipment Manufacturing: Total Cost of Materials
    ### 333132 Oil and Gas Field Machinery and Equipment Manufacturing
    'AIES333132EMPUS', # Oil and Gas Field Machinery and Equipment Manufacturing: Employees
    'AIES333132INFUS', # Oil and Gas Field Machinery and Equipment Manufacturing: Finished Goods Inventories
    'AIES333132INMUS', # Oil and Gas Field Machinery and Equipment Manufacturing: Materials and Supplies Inventories
    'AIES333132INVUS', # Oil and Gas Field Machinery and Equipment Manufacturing: Total Inventories
    'AIES333132INWUS', # Oil and Gas Field Machinery and Equipment Manufacturing: Work In Process Inventories
    'AIES333132PAYUS', # Oil and Gas Field Machinery and Equipment Manufacturing: Annual Payroll
    'AIES333132PWEUS', # Oil and Gas Field Machinery and Equipment Manufacturing: Production Workers
    'AIES333132RCTUS', # Oil and Gas Field Machinery and Equipment Manufacturing: Shipments
    'AIES333132TCMUS', # Oil and Gas Field Machinery and Equipment Manufacturing: Total Cost of Materials
    ### 3332 Industrial Machinery Manufacturing
    'AIES3332EMPUS', # Industrial Machinery Manufacturing: Employees
    'AIES3332INFUS', # Industrial Machinery Manufacturing: Finished Goods Inventories
    'AIES3332INMUS', # Industrial Machinery Manufacturing: Materials and Supplies Inventories
    'AIES3332INVUS', # Industrial Machinery Manufacturing: Total Inventories
    'AIES3332INWUS', # Industrial Machinery Manufacturing: Work In Process Inventories
    'AIES3332PAYUS', # Industrial Machinery Manufacturing: Annual Payroll
    'AIES3332PWEUS', # Industrial Machinery Manufacturing: Production Workers
    'AIES3332RCTUS', # Industrial Machinery Manufacturing: Shipments
    'AIES3332TCMUS', # Industrial Machinery Manufacturing: Total Cost of Materials
    ### 333241 Food Product Machinery Manufacturing
    'AIES333241EMPUS', # Food Product Machinery Manufacturing: Employees
    'AIES333241INFUS', # Food Product Machinery Manufacturing: Finished Goods Inventories
    'AIES333241INMUS', # Food Product Machinery Manufacturing: Materials and Supplies Inventories
    'AIES333241INVUS', # Food Product Machinery Manufacturing: Total Inventories
    'AIES333241INWUS', # Food Product Machinery Manufacturing: Work In Process Inventories
    'AIES333241PAYUS', # Food Product Machinery Manufacturing: Annual Payroll
    'AIES333241PWEUS', # Food Product Machinery Manufacturing: Production Workers
    'AIES333241RCTUS', # Food Product Machinery Manufacturing: Shipments
    'AIES333241TCMUS', # Food Product Machinery Manufacturing: Total Cost of Materials
    ### 333242 Semiconductor Machinery Manufacturing
    'AIES333242EMPUS', # Semiconductor Machinery Manufacturing: Employees
    'AIES333242INFUS', # Semiconductor Machinery Manufacturing: Finished Goods Inventories
    'AIES333242INMUS', # Semiconductor Machinery Manufacturing: Materials and Supplies Inventories
    'AIES333242INVUS', # Semiconductor Machinery Manufacturing: Total Inventories
    'AIES333242INWUS', # Semiconductor Machinery Manufacturing: Work In Process Inventories
    'AIES333242PAYUS', # Semiconductor Machinery Manufacturing: Annual Payroll
    'AIES333242PWEUS', # Semiconductor Machinery Manufacturing: Production Workers
    'AIES333242RCTUS', # Semiconductor Machinery Manufacturing: Shipments
    'AIES333242TCMUS', # Semiconductor Machinery Manufacturing: Total Cost of Materials
    ### 333243 Sawmill, Woodworking, and Paper Machinery Manufacturing
    'AIES333243EMPUS', # Sawmill, Woodworking, and Paper Machinery Manufacturing: Employees
    'AIES333243INFUS', # Sawmill, Woodworking, and Paper Machinery Manufacturing: Finished Goods Inventories
    'AIES333243INMUS', # Sawmill, Woodworking, and Paper Machinery Manufacturing: Materials and Supplies Inventories
    'AIES333243INVUS', # Sawmill, Woodworking, and Paper Machinery Manufacturing: Total Inventories
    'AIES333243INWUS', # Sawmill, Woodworking, and Paper Machinery Manufacturing: Work In Process Inventories
    'AIES333243PAYUS', # Sawmill, Woodworking, and Paper Machinery Manufacturing: Annual Payroll
    'AIES333243PWEUS', # Sawmill, Woodworking, and Paper Machinery Manufacturing: Production Workers
    'AIES333243RCTUS', # Sawmill, Woodworking, and Paper Machinery Manufacturing: Shipments
    'AIES333243TCMUS', # Sawmill, Woodworking, and Paper Machinery Manufacturing: Total Cost of Materials
    ### 333244 Printing Machinery and Equipment Manufacturing
    'AIES333244EMPUS', # Printing Machinery and Equipment Manufacturing: Employees
    'AIES333244INFUS', # Printing Machinery and Equipment Manufacturing: Finished Goods Inventories
    'AIES333244INMUS', # Printing Machinery and Equipment Manufacturing: Materials and Supplies Inventories
    'AIES333244INVUS', # Printing Machinery and Equipment Manufacturing: Total Inventories
    'AIES333244INWUS', # Printing Machinery and Equipment Manufacturing: Work In Process Inventories
    'AIES333244PAYUS', # Printing Machinery and Equipment Manufacturing: Annual Payroll
    'AIES333244PWEUS', # Printing Machinery and Equipment Manufacturing: Production Workers
    'AIES333244RCTUS', # Printing Machinery and Equipment Manufacturing: Shipments
    'AIES333244TCMUS', # Printing Machinery and Equipment Manufacturing: Total Cost of Materials
    ### 333249 Other Industrial Machinery Manufacturing
    'AIES333249EMPUS', # Other Industrial Machinery Manufacturing: Employees
    'AIES333249INFUS', # Other Industrial Machinery Manufacturing: Finished Goods Inventories
    'AIES333249INMUS', # Other Industrial Machinery Manufacturing: Materials and Supplies Inventories
    'AIES333249INVUS', # Other Industrial Machinery Manufacturing: Total Inventories
    'AIES333249INWUS', # Other Industrial Machinery Manufacturing: Work In Process Inventories
    'AIES333249PAYUS', # Other Industrial Machinery Manufacturing: Annual Payroll
    'AIES333249PWEUS', # Other Industrial Machinery Manufacturing: Production Workers
    'AIES333249RCTUS', # Other Industrial Machinery Manufacturing: Shipments
    'AIES333249TCMUS', # Other Industrial Machinery Manufacturing: Total Cost of Materials
    ### 3333 Commercial and Service Industry Machinery Manufacturing
    'AIES3333EMPUS', # Commercial and Service Industry Machinery Manufacturing: Employees
    'AIES3333INFUS', # Commercial and Service Industry Machinery Manufacturing: Finished Goods Inventories
    'AIES3333INMUS', # Commercial and Service Industry Machinery Manufacturing: Materials and Supplies Inventories
    'AIES3333INVUS', # Commercial and Service Industry Machinery Manufacturing: Total Inventories
    'AIES3333INWUS', # Commercial and Service Industry Machinery Manufacturing: Work In Process Inventories
    'AIES3333PAYUS', # Commercial and Service Industry Machinery Manufacturing: Annual Payroll
    'AIES3333PWEUS', # Commercial and Service Industry Machinery Manufacturing: Production Workers
    'AIES3333RCTUS', # Commercial and Service Industry Machinery Manufacturing: Shipments
    'AIES3333TCMUS', # Commercial and Service Industry Machinery Manufacturing: Total Cost of Materials
    ### 333314 Optical Instrument and Lens Manufacturing
    'AIES333314EMPUS', # Optical Instrument and Lens Manufacturing: Employees
    'AIES333314INFUS', # Optical Instrument and Lens Manufacturing: Finished Goods Inventories
    'AIES333314INMUS', # Optical Instrument and Lens Manufacturing: Materials and Supplies Inventories
    'AIES333314INVUS', # Optical Instrument and Lens Manufacturing: Total Inventories
    'AIES333314INWUS', # Optical Instrument and Lens Manufacturing: Work In Process Inventories
    'AIES333314PAYUS', # Optical Instrument and Lens Manufacturing: Annual Payroll
    'AIES333314PWEUS', # Optical Instrument and Lens Manufacturing: Production Workers
    'AIES333314RCTUS', # Optical Instrument and Lens Manufacturing: Shipments
    'AIES333314TCMUS', # Optical Instrument and Lens Manufacturing: Total Cost of Materials
    ### 333316 Photographic and Photocopying Equipment Manufacturing
    'AIES333316EMPUS', # Photographic and Photocopying Equipment Manufacturing: Employees
    'AIES333316INFUS', # Photographic and Photocopying Equipment Manufacturing: Finished Goods Inventories
    'AIES333316INMUS', # Photographic and Photocopying Equipment Manufacturing: Materials and Supplies Inventories
    'AIES333316INVUS', # Photographic and Photocopying Equipment Manufacturing: Total Inventories
    'AIES333316INWUS', # Photographic and Photocopying Equipment Manufacturing: Work In Process Inventories
    'AIES333316PAYUS', # Photographic and Photocopying Equipment Manufacturing: Annual Payroll
    'AIES333316PWEUS', # Photographic and Photocopying Equipment Manufacturing: Production Workers
    'AIES333316RCTUS', # Photographic and Photocopying Equipment Manufacturing: Shipments
    'AIES333316TCMUS', # Photographic and Photocopying Equipment Manufacturing: Total Cost of Materials
    ### 333318 Other Commercial and Service Industry Machinery Manufacturing
    'AIES333318EMPUS', # Other Commercial and Service Industry Machinery Manufacturing: Employees
    'AIES333318INFUS', # Other Commercial and Service Industry Machinery Manufacturing: Finished Goods Inventories
    'AIES333318INMUS', # Other Commercial and Service Industry Machinery Manufacturing: Materials and Supplies Inventories
    'AIES333318INVUS', # Other Commercial and Service Industry Machinery Manufacturing: Total Inventories
    'AIES333318INWUS', # Other Commercial and Service Industry Machinery Manufacturing: Work In Process Inventories
    'AIES333318PAYUS', # Other Commercial and Service Industry Machinery Manufacturing: Annual Payroll
    'AIES333318PWEUS', # Other Commercial and Service Industry Machinery Manufacturing: Production Workers
    'AIES333318RCTUS', # Other Commercial and Service Industry Machinery Manufacturing: Shipments
    'AIES333318TCMUS', # Other Commercial and Service Industry Machinery Manufacturing: Total Cost of Materials
    ### 3334 Hvac and Commercial Refrigeration Equipment
    'AIES3334EMPUS', # Hvac and Commercial Refrigeration Equipment: Employees
    'AIES3334INFUS', # Hvac and Commercial Refrigeration Equipment: Finished Goods Inventories
    'AIES3334INMUS', # Hvac and Commercial Refrigeration Equipment: Materials and Supplies Inventories
    'AIES3334INVUS', # Hvac and Commercial Refrigeration Equipment: Total Inventories
    'AIES3334INWUS', # Hvac and Commercial Refrigeration Equipment: Work In Process Inventories
    'AIES3334PAYUS', # Hvac and Commercial Refrigeration Equipment: Annual Payroll
    'AIES3334PWEUS', # Hvac and Commercial Refrigeration Equipment: Production Workers
    'AIES3334RCTUS', # Hvac and Commercial Refrigeration Equipment: Shipments
    'AIES3334TCMUS', # Hvac and Commercial Refrigeration Equipment: Total Cost of Materials
    ### 333413 Fan, Blower, Air Purification Equipment Manufacturing
    'AIES333413EMPUS', # Fan, Blower, Air Purification Equipment Manufacturing: Employees
    'AIES333413INFUS', # Fan, Blower, Air Purification Equipment Manufacturing: Finished Goods Inventories
    'AIES333413INMUS', # Fan, Blower, Air Purification Equipment Manufacturing: Materials and Supplies Inventories
    'AIES333413INVUS', # Fan, Blower, Air Purification Equipment Manufacturing: Total Inventories
    'AIES333413INWUS', # Fan, Blower, Air Purification Equipment Manufacturing: Work In Process Inventories
    'AIES333413PAYUS', # Fan, Blower, Air Purification Equipment Manufacturing: Annual Payroll
    'AIES333413PWEUS', # Fan, Blower, Air Purification Equipment Manufacturing: Production Workers
    'AIES333413RCTUS', # Fan, Blower, Air Purification Equipment Manufacturing: Shipments
    'AIES333413TCMUS', # Fan, Blower, Air Purification Equipment Manufacturing: Total Cost of Materials
    ### 333414 Heating Equipment (Except Warm Air Furnaces) Manufacturing
    'AIES333414EMPUS', # Heating Equipment (Except Warm Air Furnaces) Manufacturing: Employees
    'AIES333414INFUS', # Heating Equipment (Except Warm Air Furnaces) Manufacturing: Finished Goods Inventories
    'AIES333414INMUS', # Heating Equipment (Except Warm Air Furnaces) Manufacturing: Materials and Supplies Inventories
    'AIES333414INVUS', # Heating Equipment (Except Warm Air Furnaces) Manufacturing: Total Inventories
    'AIES333414INWUS', # Heating Equipment (Except Warm Air Furnaces) Manufacturing: Work In Process Inventories
    'AIES333414PAYUS', # Heating Equipment (Except Warm Air Furnaces) Manufacturing: Annual Payroll
    'AIES333414PWEUS', # Heating Equipment (Except Warm Air Furnaces) Manufacturing: Production Workers
    'AIES333414RCTUS', # Heating Equipment (Except Warm Air Furnaces) Manufacturing: Shipments
    'AIES333414TCMUS', # Heating Equipment (Except Warm Air Furnaces) Manufacturing: Total Cost of Materials
    ### 333415 Ac, Refrigeration, and Forced Air Heating
    'AIES333415EMPUS', # Ac, Refrigeration, and Forced Air Heating: Employees
    'AIES333415INFUS', # Ac, Refrigeration, and Forced Air Heating: Finished Goods Inventories
    'AIES333415INMUS', # Ac, Refrigeration, and Forced Air Heating: Materials and Supplies Inventories
    'AIES333415INVUS', # Ac, Refrigeration, and Forced Air Heating: Total Inventories
    'AIES333415INWUS', # Ac, Refrigeration, and Forced Air Heating: Work In Process Inventories
    'AIES333415PAYUS', # Ac, Refrigeration, and Forced Air Heating: Annual Payroll
    'AIES333415PWEUS', # Ac, Refrigeration, and Forced Air Heating: Production Workers
    'AIES333415RCTUS', # Ac, Refrigeration, and Forced Air Heating: Shipments
    'AIES333415TCMUS', # Ac, Refrigeration, and Forced Air Heating: Total Cost of Materials
    ### 3335 Metalworking Machinery Manufacturing
    'AIES3335EMPUS', # Metalworking Machinery Manufacturing: Employees
    'AIES3335INFUS', # Metalworking Machinery Manufacturing: Finished Goods Inventories
    'AIES3335INMUS', # Metalworking Machinery Manufacturing: Materials and Supplies Inventories
    'AIES3335INVUS', # Metalworking Machinery Manufacturing: Total Inventories
    'AIES3335INWUS', # Metalworking Machinery Manufacturing: Work In Process Inventories
    'AIES3335PAYUS', # Metalworking Machinery Manufacturing: Annual Payroll
    'AIES3335PWEUS', # Metalworking Machinery Manufacturing: Production Workers
    'AIES3335RCTUS', # Metalworking Machinery Manufacturing: Shipments
    'AIES3335TCMUS', # Metalworking Machinery Manufacturing: Total Cost of Materials
    ### 333511 Industrial Mold Manufacturing
    'AIES333511EMPUS', # Industrial Mold Manufacturing: Employees
    'AIES333511INFUS', # Industrial Mold Manufacturing: Finished Goods Inventories
    'AIES333511INMUS', # Industrial Mold Manufacturing: Materials and Supplies Inventories
    'AIES333511INVUS', # Industrial Mold Manufacturing: Total Inventories
    'AIES333511INWUS', # Industrial Mold Manufacturing: Work In Process Inventories
    'AIES333511PAYUS', # Industrial Mold Manufacturing: Annual Payroll
    'AIES333511PWEUS', # Industrial Mold Manufacturing: Production Workers
    'AIES333511RCTUS', # Industrial Mold Manufacturing: Shipments
    'AIES333511TCMUS', # Industrial Mold Manufacturing: Total Cost of Materials
    ### 333514 Special Die and Tool, Die Set, Jig, and Fixture Manufacturing
    'AIES333514EMPUS', # Special Die and Tool, Die Set, Jig, and Fixture Manufacturing: Employees
    'AIES333514INFUS', # Special Die and Tool, Die Set, Jig, and Fixture Manufacturing: Finished Goods Inventories
    'AIES333514INMUS', # Special Die and Tool, Die Set, Jig, and Fixture Manufacturing: Materials and Supplies Inventories
    'AIES333514INVUS', # Special Die and Tool, Die Set, Jig, and Fixture Manufacturing: Total Inventories
    'AIES333514INWUS', # Special Die and Tool, Die Set, Jig, and Fixture Manufacturing: Work In Process Inventories
    'AIES333514PAYUS', # Special Die and Tool, Die Set, Jig, and Fixture Manufacturing: Annual Payroll
    'AIES333514PWEUS', # Special Die and Tool, Die Set, Jig, and Fixture Manufacturing: Production Workers
    'AIES333514RCTUS', # Special Die and Tool, Die Set, Jig, and Fixture Manufacturing: Shipments
    'AIES333514TCMUS', # Special Die and Tool, Die Set, Jig, and Fixture Manufacturing: Total Cost of Materials
    ### 333515 Cutting Tool and Machine Tool Accessory Manufacturing
    'AIES333515EMPUS', # Cutting Tool and Machine Tool Accessory Manufacturing: Employees
    'AIES333515INFUS', # Cutting Tool and Machine Tool Accessory Manufacturing: Finished Goods Inventories
    'AIES333515INMUS', # Cutting Tool and Machine Tool Accessory Manufacturing: Materials and Supplies Inventories
    'AIES333515INVUS', # Cutting Tool and Machine Tool Accessory Manufacturing: Total Inventories
    'AIES333515INWUS', # Cutting Tool and Machine Tool Accessory Manufacturing: Work In Process Inventories
    'AIES333515PAYUS', # Cutting Tool and Machine Tool Accessory Manufacturing: Annual Payroll
    'AIES333515PWEUS', # Cutting Tool and Machine Tool Accessory Manufacturing: Production Workers
    'AIES333515RCTUS', # Cutting Tool and Machine Tool Accessory Manufacturing: Shipments
    'AIES333515TCMUS', # Cutting Tool and Machine Tool Accessory Manufacturing: Total Cost of Materials
    ### 333517 Machine Tool Manufacturing
    'AIES333517EMPUS', # Machine Tool Manufacturing: Employees
    'AIES333517INFUS', # Machine Tool Manufacturing: Finished Goods Inventories
    'AIES333517INMUS', # Machine Tool Manufacturing: Materials and Supplies Inventories
    'AIES333517INVUS', # Machine Tool Manufacturing: Total Inventories
    'AIES333517INWUS', # Machine Tool Manufacturing: Work In Process Inventories
    'AIES333517PAYUS', # Machine Tool Manufacturing: Annual Payroll
    'AIES333517PWEUS', # Machine Tool Manufacturing: Production Workers
    'AIES333517RCTUS', # Machine Tool Manufacturing: Shipments
    'AIES333517TCMUS', # Machine Tool Manufacturing: Total Cost of Materials
    ### 333519 Rolling Mill and Other Metalworking Machinery Manufacturing
    'AIES333519EMPUS', # Rolling Mill and Other Metalworking Machinery Manufacturing: Employees
    'AIES333519INFUS', # Rolling Mill and Other Metalworking Machinery Manufacturing: Finished Goods Inventories
    'AIES333519INMUS', # Rolling Mill and Other Metalworking Machinery Manufacturing: Materials and Supplies Inventories
    'AIES333519INVUS', # Rolling Mill and Other Metalworking Machinery Manufacturing: Total Inventories
    'AIES333519INWUS', # Rolling Mill and Other Metalworking Machinery Manufacturing: Work In Process Inventories
    'AIES333519PAYUS', # Rolling Mill and Other Metalworking Machinery Manufacturing: Annual Payroll
    'AIES333519PWEUS', # Rolling Mill and Other Metalworking Machinery Manufacturing: Production Workers
    'AIES333519RCTUS', # Rolling Mill and Other Metalworking Machinery Manufacturing: Shipments
    'AIES333519TCMUS', # Rolling Mill and Other Metalworking Machinery Manufacturing: Total Cost of Materials
    ### 3336 Engine, Turbine, and Power Transmission Equipment Manufacturing
    'AIES3336EMPUS', # Engine, Turbine, and Power Transmission Equipment Manufacturing: Employees
    'AIES3336INFUS', # Engine, Turbine, and Power Transmission Equipment Manufacturing: Finished Goods Inventories
    'AIES3336INMUS', # Engine, Turbine, and Power Transmission Equipment Manufacturing: Materials and Supplies Inventories
    'AIES3336INVUS', # Engine, Turbine, and Power Transmission Equipment Manufacturing: Total Inventories
    'AIES3336INWUS', # Engine, Turbine, and Power Transmission Equipment Manufacturing: Work In Process Inventories
    'AIES3336PAYUS', # Engine, Turbine, and Power Transmission Equipment Manufacturing: Annual Payroll
    'AIES3336PWEUS', # Engine, Turbine, and Power Transmission Equipment Manufacturing: Production Workers
    'AIES3336RCTUS', # Engine, Turbine, and Power Transmission Equipment Manufacturing: Shipments
    'AIES3336TCMUS', # Engine, Turbine, and Power Transmission Equipment Manufacturing: Total Cost of Materials
    ### 333611 Turbine and Turbine Generator Set Units Manufacturing
    'AIES333611EMPUS', # Turbine and Turbine Generator Set Units Manufacturing: Employees
    'AIES333611INFUS', # Turbine and Turbine Generator Set Units Manufacturing: Finished Goods Inventories
    'AIES333611INMUS', # Turbine and Turbine Generator Set Units Manufacturing: Materials and Supplies Inventories
    'AIES333611INVUS', # Turbine and Turbine Generator Set Units Manufacturing: Total Inventories
    'AIES333611INWUS', # Turbine and Turbine Generator Set Units Manufacturing: Work In Process Inventories
    'AIES333611PAYUS', # Turbine and Turbine Generator Set Units Manufacturing: Annual Payroll
    'AIES333611PWEUS', # Turbine and Turbine Generator Set Units Manufacturing: Production Workers
    'AIES333611RCTUS', # Turbine and Turbine Generator Set Units Manufacturing: Shipments
    'AIES333611TCMUS', # Turbine and Turbine Generator Set Units Manufacturing: Total Cost of Materials
    ### 333612 Speed Changer, Drive, and Gear Manufacturing
    'AIES333612EMPUS', # Speed Changer, Drive, and Gear Manufacturing: Employees
    'AIES333612INFUS', # Speed Changer, Drive, and Gear Manufacturing: Finished Goods Inventories
    'AIES333612INMUS', # Speed Changer, Drive, and Gear Manufacturing: Materials and Supplies Inventories
    'AIES333612INVUS', # Speed Changer, Drive, and Gear Manufacturing: Total Inventories
    'AIES333612INWUS', # Speed Changer, Drive, and Gear Manufacturing: Work In Process Inventories
    'AIES333612PAYUS', # Speed Changer, Drive, and Gear Manufacturing: Annual Payroll
    'AIES333612PWEUS', # Speed Changer, Drive, and Gear Manufacturing: Production Workers
    'AIES333612RCTUS', # Speed Changer, Drive, and Gear Manufacturing: Shipments
    'AIES333612TCMUS', # Speed Changer, Drive, and Gear Manufacturing: Total Cost of Materials
    ### 333613 Mechanical Power Transmission Equipment Manufacturing
    'AIES333613EMPUS', # Mechanical Power Transmission Equipment Manufacturing: Employees
    'AIES333613INFUS', # Mechanical Power Transmission Equipment Manufacturing: Finished Goods Inventories
    'AIES333613INMUS', # Mechanical Power Transmission Equipment Manufacturing: Materials and Supplies Inventories
    'AIES333613INVUS', # Mechanical Power Transmission Equipment Manufacturing: Total Inventories
    'AIES333613INWUS', # Mechanical Power Transmission Equipment Manufacturing: Work In Process Inventories
    'AIES333613PAYUS', # Mechanical Power Transmission Equipment Manufacturing: Annual Payroll
    'AIES333613PWEUS', # Mechanical Power Transmission Equipment Manufacturing: Production Workers
    'AIES333613RCTUS', # Mechanical Power Transmission Equipment Manufacturing: Shipments
    'AIES333613TCMUS', # Mechanical Power Transmission Equipment Manufacturing: Total Cost of Materials
    ### 333618 Other Engine Equipment Manufacturing
    'AIES333618EMPUS', # Other Engine Equipment Manufacturing: Employees
    'AIES333618INFUS', # Other Engine Equipment Manufacturing: Finished Goods Inventories
    'AIES333618INMUS', # Other Engine Equipment Manufacturing: Materials and Supplies Inventories
    'AIES333618INVUS', # Other Engine Equipment Manufacturing: Total Inventories
    'AIES333618INWUS', # Other Engine Equipment Manufacturing: Work In Process Inventories
    'AIES333618PAYUS', # Other Engine Equipment Manufacturing: Annual Payroll
    'AIES333618PWEUS', # Other Engine Equipment Manufacturing: Production Workers
    'AIES333618RCTUS', # Other Engine Equipment Manufacturing: Shipments
    'AIES333618TCMUS', # Other Engine Equipment Manufacturing: Total Cost of Materials
    ### 3339 Other General Purpose Machinery Manufacturing
    'AIES3339EMPUS', # Other General Purpose Machinery Manufacturing: Employees
    'AIES3339INFUS', # Other General Purpose Machinery Manufacturing: Finished Goods Inventories
    'AIES3339INMUS', # Other General Purpose Machinery Manufacturing: Materials and Supplies Inventories
    'AIES3339INVUS', # Other General Purpose Machinery Manufacturing: Total Inventories
    'AIES3339INWUS', # Other General Purpose Machinery Manufacturing: Work In Process Inventories
    'AIES3339PAYUS', # Other General Purpose Machinery Manufacturing: Annual Payroll
    'AIES3339PWEUS', # Other General Purpose Machinery Manufacturing: Production Workers
    'AIES3339RCTUS', # Other General Purpose Machinery Manufacturing: Shipments
    'AIES3339TCMUS', # Other General Purpose Machinery Manufacturing: Total Cost of Materials
    ### 33391 Pump and Compressor Manufacturing
    'AIES33391EMPUS', # Pump and Compressor Manufacturing: Employees
    'AIES33391INFUS', # Pump and Compressor Manufacturing: Finished Goods Inventories
    'AIES33391INMUS', # Pump and Compressor Manufacturing: Materials and Supplies Inventories
    'AIES33391INVUS', # Pump and Compressor Manufacturing: Total Inventories
    'AIES33391INWUS', # Pump and Compressor Manufacturing: Work In Process Inventories
    'AIES33391PAYUS', # Pump and Compressor Manufacturing: Annual Payroll
    'AIES33391PWEUS', # Pump and Compressor Manufacturing: Production Workers
    'AIES33391RCTUS', # Pump and Compressor Manufacturing: Shipments
    'AIES33391TCMUS', # Pump and Compressor Manufacturing: Total Cost of Materials
    ### 333912 Air and Gas Compressor Manufacturing
    'AIES333912EMPUS', # Air and Gas Compressor Manufacturing: Employees
    'AIES333912INFUS', # Air and Gas Compressor Manufacturing: Finished Goods Inventories
    'AIES333912INMUS', # Air and Gas Compressor Manufacturing: Materials and Supplies Inventories
    'AIES333912INVUS', # Air and Gas Compressor Manufacturing: Total Inventories
    'AIES333912INWUS', # Air and Gas Compressor Manufacturing: Work In Process Inventories
    'AIES333912PAYUS', # Air and Gas Compressor Manufacturing: Annual Payroll
    'AIES333912PWEUS', # Air and Gas Compressor Manufacturing: Production Workers
    'AIES333912RCTUS', # Air and Gas Compressor Manufacturing: Shipments
    'AIES333912TCMUS', # Air and Gas Compressor Manufacturing: Total Cost of Materials
    ### 333914 Measuring, Dispensing, and Other Pumping Equipment Manufacturing
    'AIES333914EMPUS', # Measuring, Dispensing, and Other Pumping Equipment Manufacturing: Employees
    'AIES333914INFUS', # Measuring, Dispensing, and Other Pumping Equipment Manufacturing: Finished Goods Inventories
    'AIES333914INMUS', # Measuring, Dispensing, and Other Pumping Equipment Manufacturing: Materials and Supplies Inventories
    'AIES333914INVUS', # Measuring, Dispensing, and Other Pumping Equipment Manufacturing: Total Inventories
    'AIES333914INWUS', # Measuring, Dispensing, and Other Pumping Equipment Manufacturing: Work In Process Inventories
    'AIES333914PAYUS', # Measuring, Dispensing, and Other Pumping Equipment Manufacturing: Annual Payroll
    'AIES333914PWEUS', # Measuring, Dispensing, and Other Pumping Equipment Manufacturing: Production Workers
    'AIES333914RCTUS', # Measuring, Dispensing, and Other Pumping Equipment Manufacturing: Shipments
    'AIES333914TCMUS', # Measuring, Dispensing, and Other Pumping Equipment Manufacturing: Total Cost of Materials
    ### 33392 Material Handling Equipment Manufacturing
    'AIES33392EMPUS', # Material Handling Equipment Manufacturing: Employees
    'AIES33392INFUS', # Material Handling Equipment Manufacturing: Finished Goods Inventories
    'AIES33392INMUS', # Material Handling Equipment Manufacturing: Materials and Supplies Inventories
    'AIES33392INVUS', # Material Handling Equipment Manufacturing: Total Inventories
    'AIES33392INWUS', # Material Handling Equipment Manufacturing: Work In Process Inventories
    'AIES33392PAYUS', # Material Handling Equipment Manufacturing: Annual Payroll
    'AIES33392PWEUS', # Material Handling Equipment Manufacturing: Production Workers
    'AIES33392RCTUS', # Material Handling Equipment Manufacturing: Shipments
    'AIES33392TCMUS', # Material Handling Equipment Manufacturing: Total Cost of Materials
    ### 333921 Elevator and Moving Stairway Manufacturing
    'AIES333921EMPUS', # Elevator and Moving Stairway Manufacturing: Employees
    'AIES333921INFUS', # Elevator and Moving Stairway Manufacturing: Finished Goods Inventories
    'AIES333921INMUS', # Elevator and Moving Stairway Manufacturing: Materials and Supplies Inventories
    'AIES333921INVUS', # Elevator and Moving Stairway Manufacturing: Total Inventories
    'AIES333921INWUS', # Elevator and Moving Stairway Manufacturing: Work In Process Inventories
    'AIES333921PAYUS', # Elevator and Moving Stairway Manufacturing: Annual Payroll
    'AIES333921PWEUS', # Elevator and Moving Stairway Manufacturing: Production Workers
    'AIES333921RCTUS', # Elevator and Moving Stairway Manufacturing: Shipments
    'AIES333921TCMUS', # Elevator and Moving Stairway Manufacturing: Total Cost of Materials
    ### 333922 Conveyor and Conveying Equipment Manufacturing
    'AIES333922EMPUS', # Conveyor and Conveying Equipment Manufacturing: Employees
    'AIES333922INFUS', # Conveyor and Conveying Equipment Manufacturing: Finished Goods Inventories
    'AIES333922INMUS', # Conveyor and Conveying Equipment Manufacturing: Materials and Supplies Inventories
    'AIES333922INVUS', # Conveyor and Conveying Equipment Manufacturing: Total Inventories
    'AIES333922INWUS', # Conveyor and Conveying Equipment Manufacturing: Work In Process Inventories
    'AIES333922PAYUS', # Conveyor and Conveying Equipment Manufacturing: Annual Payroll
    'AIES333922PWEUS', # Conveyor and Conveying Equipment Manufacturing: Production Workers
    'AIES333922RCTUS', # Conveyor and Conveying Equipment Manufacturing: Shipments
    'AIES333922TCMUS', # Conveyor and Conveying Equipment Manufacturing: Total Cost of Materials
    ### 333923 Overhead Cranes, Hoists, and Monorail Systems
    'AIES333923EMPUS', # Overhead Cranes, Hoists, and Monorail Systems: Employees
    'AIES333923INFUS', # Overhead Cranes, Hoists, and Monorail Systems: Finished Goods Inventories
    'AIES333923INMUS', # Overhead Cranes, Hoists, and Monorail Systems: Materials and Supplies Inventories
    'AIES333923INVUS', # Overhead Cranes, Hoists, and Monorail Systems: Total Inventories
    'AIES333923INWUS', # Overhead Cranes, Hoists, and Monorail Systems: Work In Process Inventories
    'AIES333923PAYUS', # Overhead Cranes, Hoists, and Monorail Systems: Annual Payroll
    'AIES333923PWEUS', # Overhead Cranes, Hoists, and Monorail Systems: Production Workers
    'AIES333923RCTUS', # Overhead Cranes, Hoists, and Monorail Systems: Shipments
    'AIES333923TCMUS', # Overhead Cranes, Hoists, and Monorail Systems: Total Cost of Materials
    ### 333924 Industrial Truck, Trailer, and Stacker Machinery Manufacturing
    'AIES333924EMPUS', # Industrial Truck, Trailer, and Stacker Machinery Manufacturing: Employees
    'AIES333924INFUS', # Industrial Truck, Trailer, and Stacker Machinery Manufacturing: Finished Goods Inventories
    'AIES333924INMUS', # Industrial Truck, Trailer, and Stacker Machinery Manufacturing: Materials and Supplies Inventories
    'AIES333924INVUS', # Industrial Truck, Trailer, and Stacker Machinery Manufacturing: Total Inventories
    'AIES333924INWUS', # Industrial Truck, Trailer, and Stacker Machinery Manufacturing: Work In Process Inventories
    'AIES333924PAYUS', # Industrial Truck, Trailer, and Stacker Machinery Manufacturing: Annual Payroll
    'AIES333924PWEUS', # Industrial Truck, Trailer, and Stacker Machinery Manufacturing: Production Workers
    'AIES333924RCTUS', # Industrial Truck, Trailer, and Stacker Machinery Manufacturing: Shipments
    'AIES333924TCMUS', # Industrial Truck, Trailer, and Stacker Machinery Manufacturing: Total Cost of Materials
    ### 33399 All Other General Purpose Machinery Manufacturing
    'AIES33399EMPUS', # All Other General Purpose Machinery Manufacturing: Employees
    'AIES33399INFUS', # All Other General Purpose Machinery Manufacturing: Finished Goods Inventories
    'AIES33399INMUS', # All Other General Purpose Machinery Manufacturing: Materials and Supplies Inventories
    'AIES33399INVUS', # All Other General Purpose Machinery Manufacturing: Total Inventories
    'AIES33399INWUS', # All Other General Purpose Machinery Manufacturing: Work In Process Inventories
    'AIES33399PAYUS', # All Other General Purpose Machinery Manufacturing: Annual Payroll
    'AIES33399PWEUS', # All Other General Purpose Machinery Manufacturing: Production Workers
    'AIES33399RCTUS', # All Other General Purpose Machinery Manufacturing: Shipments
    'AIES33399TCMUS', # All Other General Purpose Machinery Manufacturing: Total Cost of Materials
    ### 333991 Power-Driven Handtool Manufacturing
    'AIES333991EMPUS', # Power-Driven Handtool Manufacturing: Employees
    'AIES333991INFUS', # Power-Driven Handtool Manufacturing: Finished Goods Inventories
    'AIES333991INMUS', # Power-Driven Handtool Manufacturing: Materials and Supplies Inventories
    'AIES333991INVUS', # Power-Driven Handtool Manufacturing: Total Inventories
    'AIES333991INWUS', # Power-Driven Handtool Manufacturing: Work In Process Inventories
    'AIES333991PAYUS', # Power-Driven Handtool Manufacturing: Annual Payroll
    'AIES333991PWEUS', # Power-Driven Handtool Manufacturing: Production Workers
    'AIES333991RCTUS', # Power-Driven Handtool Manufacturing: Shipments
    'AIES333991TCMUS', # Power-Driven Handtool Manufacturing: Total Cost of Materials
    ### 333992 Welding and Soldering Equipment Manufacturing
    'AIES333992EMPUS', # Welding and Soldering Equipment Manufacturing: Employees
    'AIES333992INFUS', # Welding and Soldering Equipment Manufacturing: Finished Goods Inventories
    'AIES333992INMUS', # Welding and Soldering Equipment Manufacturing: Materials and Supplies Inventories
    'AIES333992INVUS', # Welding and Soldering Equipment Manufacturing: Total Inventories
    'AIES333992INWUS', # Welding and Soldering Equipment Manufacturing: Work In Process Inventories
    'AIES333992PAYUS', # Welding and Soldering Equipment Manufacturing: Annual Payroll
    'AIES333992PWEUS', # Welding and Soldering Equipment Manufacturing: Production Workers
    'AIES333992RCTUS', # Welding and Soldering Equipment Manufacturing: Shipments
    'AIES333992TCMUS', # Welding and Soldering Equipment Manufacturing: Total Cost of Materials
    ### 333993 Packaging Machinery Manufacturing
    'AIES333993EMPUS', # Packaging Machinery Manufacturing: Employees
    'AIES333993INFUS', # Packaging Machinery Manufacturing: Finished Goods Inventories
    'AIES333993INMUS', # Packaging Machinery Manufacturing: Materials and Supplies Inventories
    'AIES333993INVUS', # Packaging Machinery Manufacturing: Total Inventories
    'AIES333993INWUS', # Packaging Machinery Manufacturing: Work In Process Inventories
    'AIES333993PAYUS', # Packaging Machinery Manufacturing: Annual Payroll
    'AIES333993PWEUS', # Packaging Machinery Manufacturing: Production Workers
    'AIES333993RCTUS', # Packaging Machinery Manufacturing: Shipments
    'AIES333993TCMUS', # Packaging Machinery Manufacturing: Total Cost of Materials
    ### 333994 Industrial Process Furnace and Oven Manufacturing
    'AIES333994EMPUS', # Industrial Process Furnace and Oven Manufacturing: Employees
    'AIES333994INFUS', # Industrial Process Furnace and Oven Manufacturing: Finished Goods Inventories
    'AIES333994INMUS', # Industrial Process Furnace and Oven Manufacturing: Materials and Supplies Inventories
    'AIES333994INVUS', # Industrial Process Furnace and Oven Manufacturing: Total Inventories
    'AIES333994INWUS', # Industrial Process Furnace and Oven Manufacturing: Work In Process Inventories
    'AIES333994PAYUS', # Industrial Process Furnace and Oven Manufacturing: Annual Payroll
    'AIES333994PWEUS', # Industrial Process Furnace and Oven Manufacturing: Production Workers
    'AIES333994RCTUS', # Industrial Process Furnace and Oven Manufacturing: Shipments
    'AIES333994TCMUS', # Industrial Process Furnace and Oven Manufacturing: Total Cost of Materials
    ### 333995 Fluid Power Cylinder and Actuator Manufacturing
    'AIES333995EMPUS', # Fluid Power Cylinder and Actuator Manufacturing: Employees
    'AIES333995INFUS', # Fluid Power Cylinder and Actuator Manufacturing: Finished Goods Inventories
    'AIES333995INMUS', # Fluid Power Cylinder and Actuator Manufacturing: Materials and Supplies Inventories
    'AIES333995INVUS', # Fluid Power Cylinder and Actuator Manufacturing: Total Inventories
    'AIES333995INWUS', # Fluid Power Cylinder and Actuator Manufacturing: Work In Process Inventories
    'AIES333995PAYUS', # Fluid Power Cylinder and Actuator Manufacturing: Annual Payroll
    'AIES333995PWEUS', # Fluid Power Cylinder and Actuator Manufacturing: Production Workers
    'AIES333995RCTUS', # Fluid Power Cylinder and Actuator Manufacturing: Shipments
    'AIES333995TCMUS', # Fluid Power Cylinder and Actuator Manufacturing: Total Cost of Materials
    ### 333996 Fluid Power Pump and Motor Manufacturing
    'AIES333996EMPUS', # Fluid Power Pump and Motor Manufacturing: Employees
    'AIES333996INFUS', # Fluid Power Pump and Motor Manufacturing: Finished Goods Inventories
    'AIES333996INMUS', # Fluid Power Pump and Motor Manufacturing: Materials and Supplies Inventories
    'AIES333996INVUS', # Fluid Power Pump and Motor Manufacturing: Total Inventories
    'AIES333996INWUS', # Fluid Power Pump and Motor Manufacturing: Work In Process Inventories
    'AIES333996PAYUS', # Fluid Power Pump and Motor Manufacturing: Annual Payroll
    'AIES333996PWEUS', # Fluid Power Pump and Motor Manufacturing: Production Workers
    'AIES333996RCTUS', # Fluid Power Pump and Motor Manufacturing: Shipments
    'AIES333996TCMUS', # Fluid Power Pump and Motor Manufacturing: Total Cost of Materials
    ### 333997 Scale and Balance Manufacturing
    'AIES333997EMPUS', # Scale and Balance Manufacturing: Employees
    'AIES333997INFUS', # Scale and Balance Manufacturing: Finished Goods Inventories
    'AIES333997INMUS', # Scale and Balance Manufacturing: Materials and Supplies Inventories
    'AIES333997INVUS', # Scale and Balance Manufacturing: Total Inventories
    'AIES333997INWUS', # Scale and Balance Manufacturing: Work In Process Inventories
    'AIES333997PAYUS', # Scale and Balance Manufacturing: Annual Payroll
    'AIES333997PWEUS', # Scale and Balance Manufacturing: Production Workers
    'AIES333997RCTUS', # Scale and Balance Manufacturing: Shipments
    'AIES333997TCMUS', # Scale and Balance Manufacturing: Total Cost of Materials
    ### 333999 All Other Miscellaneous General Purpose Machinery Manufacturing
    'AIES333999EMPUS', # All Other Miscellaneous General Purpose Machinery Manufacturing: Employees
    'AIES333999INFUS', # All Other Miscellaneous General Purpose Machinery Manufacturing: Finished Goods Inventories
    'AIES333999INMUS', # All Other Miscellaneous General Purpose Machinery Manufacturing: Materials and Supplies Inventories
    'AIES333999INVUS', # All Other Miscellaneous General Purpose Machinery Manufacturing: Total Inventories
    'AIES333999INWUS', # All Other Miscellaneous General Purpose Machinery Manufacturing: Work In Process Inventories
    'AIES333999PAYUS', # All Other Miscellaneous General Purpose Machinery Manufacturing: Annual Payroll
    'AIES333999PWEUS', # All Other Miscellaneous General Purpose Machinery Manufacturing: Production Workers
    'AIES333999RCTUS', # All Other Miscellaneous General Purpose Machinery Manufacturing: Shipments
    'AIES333999TCMUS', # All Other Miscellaneous General Purpose Machinery Manufacturing: Total Cost of Materials
    ## NAICS 334 Computer and Electronic Product Manufacturing
    ### 334 Computer and Electronic Product Manufacturing
    'AIES334EMPUS', # Computer and Electronic Product Manufacturing: Employees
    'AIES334INFUS', # Computer and Electronic Product Manufacturing: Finished Goods Inventories
    'AIES334INMUS', # Computer and Electronic Product Manufacturing: Materials and Supplies Inventories
    'AIES334INVUS', # Computer and Electronic Product Manufacturing: Total Inventories
    'AIES334INWUS', # Computer and Electronic Product Manufacturing: Work In Process Inventories
    'AIES334PAYUS', # Computer and Electronic Product Manufacturing: Annual Payroll
    'AIES334PWEUS', # Computer and Electronic Product Manufacturing: Production Workers
    'AIES334RCTUS', # Computer and Electronic Product Manufacturing: Shipments
    'AIES334TCMUS', # Computer and Electronic Product Manufacturing: Total Cost of Materials
    ### 3341 Computer and Peripheral Equipment Manufacturing
    'AIES3341EMPUS', # Computer and Peripheral Equipment Manufacturing: Employees
    'AIES3341INFUS', # Computer and Peripheral Equipment Manufacturing: Finished Goods Inventories
    'AIES3341INMUS', # Computer and Peripheral Equipment Manufacturing: Materials and Supplies Inventories
    'AIES3341INVUS', # Computer and Peripheral Equipment Manufacturing: Total Inventories
    'AIES3341INWUS', # Computer and Peripheral Equipment Manufacturing: Work In Process Inventories
    'AIES3341PAYUS', # Computer and Peripheral Equipment Manufacturing: Annual Payroll
    'AIES3341PWEUS', # Computer and Peripheral Equipment Manufacturing: Production Workers
    'AIES3341RCTUS', # Computer and Peripheral Equipment Manufacturing: Shipments
    'AIES3341TCMUS', # Computer and Peripheral Equipment Manufacturing: Total Cost of Materials
    ### 334111 Electronic Computer Manufacturing
    'AIES334111EMPUS', # Electronic Computer Manufacturing: Employees
    'AIES334111INFUS', # Electronic Computer Manufacturing: Finished Goods Inventories
    'AIES334111INMUS', # Electronic Computer Manufacturing: Materials and Supplies Inventories
    'AIES334111INVUS', # Electronic Computer Manufacturing: Total Inventories
    'AIES334111INWUS', # Electronic Computer Manufacturing: Work In Process Inventories
    'AIES334111PAYUS', # Electronic Computer Manufacturing: Annual Payroll
    'AIES334111PWEUS', # Electronic Computer Manufacturing: Production Workers
    'AIES334111RCTUS', # Electronic Computer Manufacturing: Shipments
    'AIES334111TCMUS', # Electronic Computer Manufacturing: Total Cost of Materials
    ### 334112 Computer Storage Device Manufacturing
    'AIES334112EMPUS', # Computer Storage Device Manufacturing: Employees
    'AIES334112INFUS', # Computer Storage Device Manufacturing: Finished Goods Inventories
    'AIES334112INMUS', # Computer Storage Device Manufacturing: Materials and Supplies Inventories
    'AIES334112INVUS', # Computer Storage Device Manufacturing: Total Inventories
    'AIES334112INWUS', # Computer Storage Device Manufacturing: Work In Process Inventories
    'AIES334112PAYUS', # Computer Storage Device Manufacturing: Annual Payroll
    'AIES334112PWEUS', # Computer Storage Device Manufacturing: Production Workers
    'AIES334112RCTUS', # Computer Storage Device Manufacturing: Shipments
    'AIES334112TCMUS', # Computer Storage Device Manufacturing: Total Cost of Materials
    ### 334118 Other Computer Peripheral Equipment Manufacturing
    'AIES334118EMPUS', # Other Computer Peripheral Equipment Manufacturing: Employees
    'AIES334118INFUS', # Other Computer Peripheral Equipment Manufacturing: Finished Goods Inventories
    'AIES334118INMUS', # Other Computer Peripheral Equipment Manufacturing: Materials and Supplies Inventories
    'AIES334118INVUS', # Other Computer Peripheral Equipment Manufacturing: Total Inventories
    'AIES334118INWUS', # Other Computer Peripheral Equipment Manufacturing: Work In Process Inventories
    'AIES334118PAYUS', # Other Computer Peripheral Equipment Manufacturing: Annual Payroll
    'AIES334118PWEUS', # Other Computer Peripheral Equipment Manufacturing: Production Workers
    'AIES334118RCTUS', # Other Computer Peripheral Equipment Manufacturing: Shipments
    'AIES334118TCMUS', # Other Computer Peripheral Equipment Manufacturing: Total Cost of Materials
    ### 3342 Communications Equipment Manufacturing
    'AIES3342EMPUS', # Communications Equipment Manufacturing: Employees
    'AIES3342INFUS', # Communications Equipment Manufacturing: Finished Goods Inventories
    'AIES3342INMUS', # Communications Equipment Manufacturing: Materials and Supplies Inventories
    'AIES3342INVUS', # Communications Equipment Manufacturing: Total Inventories
    'AIES3342INWUS', # Communications Equipment Manufacturing: Work In Process Inventories
    'AIES3342PAYUS', # Communications Equipment Manufacturing: Annual Payroll
    'AIES3342PWEUS', # Communications Equipment Manufacturing: Production Workers
    'AIES3342RCTUS', # Communications Equipment Manufacturing: Shipments
    'AIES3342TCMUS', # Communications Equipment Manufacturing: Total Cost of Materials
    ### 33421 Telephone Apparatus Manufacturing
    'AIES33421EMPUS', # Telephone Apparatus Manufacturing: Employees
    'AIES33421INFUS', # Telephone Apparatus Manufacturing: Finished Goods Inventories
    'AIES33421INMUS', # Telephone Apparatus Manufacturing: Materials and Supplies Inventories
    'AIES33421INVUS', # Telephone Apparatus Manufacturing: Total Inventories
    'AIES33421INWUS', # Telephone Apparatus Manufacturing: Work In Process Inventories
    'AIES33421PAYUS', # Telephone Apparatus Manufacturing: Annual Payroll
    'AIES33421PWEUS', # Telephone Apparatus Manufacturing: Production Workers
    'AIES33421RCTUS', # Telephone Apparatus Manufacturing: Shipments
    'AIES33421TCMUS', # Telephone Apparatus Manufacturing: Total Cost of Materials
    ### 33422 Broadcast and Wireless Communications Equip.
    'AIES33422EMPUS', # Broadcast and Wireless Communications Equip.: Employees
    'AIES33422INFUS', # Broadcast and Wireless Communications Equip.: Finished Goods Inventories
    'AIES33422INMUS', # Broadcast and Wireless Communications Equip.: Materials and Supplies Inventories
    'AIES33422INVUS', # Broadcast and Wireless Communications Equip.: Total Inventories
    'AIES33422INWUS', # Broadcast and Wireless Communications Equip.: Work In Process Inventories
    'AIES33422PAYUS', # Broadcast and Wireless Communications Equip.: Annual Payroll
    'AIES33422PWEUS', # Broadcast and Wireless Communications Equip.: Production Workers
    'AIES33422RCTUS', # Broadcast and Wireless Communications Equip.: Shipments
    'AIES33422TCMUS', # Broadcast and Wireless Communications Equip.: Total Cost of Materials
    ### 33429 Other Communications Equipment Manufacturing
    'AIES33429EMPUS', # Other Communications Equipment Manufacturing: Employees
    'AIES33429INFUS', # Other Communications Equipment Manufacturing: Finished Goods Inventories
    'AIES33429INMUS', # Other Communications Equipment Manufacturing: Materials and Supplies Inventories
    'AIES33429INVUS', # Other Communications Equipment Manufacturing: Total Inventories
    'AIES33429INWUS', # Other Communications Equipment Manufacturing: Work In Process Inventories
    'AIES33429PAYUS', # Other Communications Equipment Manufacturing: Annual Payroll
    'AIES33429PWEUS', # Other Communications Equipment Manufacturing: Production Workers
    'AIES33429RCTUS', # Other Communications Equipment Manufacturing: Shipments
    'AIES33429TCMUS', # Other Communications Equipment Manufacturing: Total Cost of Materials
    ### 3343 Audio and Video Equipment Manufacturing
    'AIES3343EMPUS', # Audio and Video Equipment Manufacturing: Employees
    'AIES3343INFUS', # Audio and Video Equipment Manufacturing: Finished Goods Inventories
    'AIES3343INMUS', # Audio and Video Equipment Manufacturing: Materials and Supplies Inventories
    'AIES3343INVUS', # Audio and Video Equipment Manufacturing: Total Inventories
    'AIES3343INWUS', # Audio and Video Equipment Manufacturing: Work In Process Inventories
    'AIES3343PAYUS', # Audio and Video Equipment Manufacturing: Annual Payroll
    'AIES3343PWEUS', # Audio and Video Equipment Manufacturing: Production Workers
    'AIES3343RCTUS', # Audio and Video Equipment Manufacturing: Shipments
    'AIES3343TCMUS', # Audio and Video Equipment Manufacturing: Total Cost of Materials
    ### 3344 Semiconductor and Other Electronic Component Manufacturing
    'AIES3344EMPUS', # Semiconductor and Other Electronic Component Manufacturing: Employees
    'AIES3344INFUS', # Semiconductor and Other Electronic Component Manufacturing: Finished Goods Inventories
    'AIES3344INMUS', # Semiconductor and Other Electronic Component Manufacturing: Materials and Supplies Inventories
    'AIES3344INVUS', # Semiconductor and Other Electronic Component Manufacturing: Total Inventories
    'AIES3344INWUS', # Semiconductor and Other Electronic Component Manufacturing: Work In Process Inventories
    'AIES3344PAYUS', # Semiconductor and Other Electronic Component Manufacturing: Annual Payroll
    'AIES3344PWEUS', # Semiconductor and Other Electronic Component Manufacturing: Production Workers
    'AIES3344RCTUS', # Semiconductor and Other Electronic Component Manufacturing: Shipments
    'AIES3344TCMUS', # Semiconductor and Other Electronic Component Manufacturing: Total Cost of Materials
    ### 334412 Bare Printed Circuit Board Manufacturing
    'AIES334412EMPUS', # Bare Printed Circuit Board Manufacturing: Employees
    'AIES334412INFUS', # Bare Printed Circuit Board Manufacturing: Finished Goods Inventories
    'AIES334412INMUS', # Bare Printed Circuit Board Manufacturing: Materials and Supplies Inventories
    'AIES334412INVUS', # Bare Printed Circuit Board Manufacturing: Total Inventories
    'AIES334412INWUS', # Bare Printed Circuit Board Manufacturing: Work In Process Inventories
    'AIES334412PAYUS', # Bare Printed Circuit Board Manufacturing: Annual Payroll
    'AIES334412PWEUS', # Bare Printed Circuit Board Manufacturing: Production Workers
    'AIES334412RCTUS', # Bare Printed Circuit Board Manufacturing: Shipments
    'AIES334412TCMUS', # Bare Printed Circuit Board Manufacturing: Total Cost of Materials
    ### 334413 Semiconductor and Related Device Manufacturing
    'AIES334413EMPUS', # Semiconductor and Related Device Manufacturing: Employees
    'AIES334413INFUS', # Semiconductor and Related Device Manufacturing: Finished Goods Inventories
    'AIES334413INMUS', # Semiconductor and Related Device Manufacturing: Materials and Supplies Inventories
    'AIES334413INVUS', # Semiconductor and Related Device Manufacturing: Total Inventories
    'AIES334413INWUS', # Semiconductor and Related Device Manufacturing: Work In Process Inventories
    'AIES334413PAYUS', # Semiconductor and Related Device Manufacturing: Annual Payroll
    'AIES334413PWEUS', # Semiconductor and Related Device Manufacturing: Production Workers
    'AIES334413RCTUS', # Semiconductor and Related Device Manufacturing: Shipments
    'AIES334413TCMUS', # Semiconductor and Related Device Manufacturing: Total Cost of Materials
    ### 334416 Capacitor, Resistor, and Inductor Manufacturing
    'AIES334416EMPUS', # Capacitor, Resistor, and Inductor Manufacturing: Employees
    'AIES334416INFUS', # Capacitor, Resistor, and Inductor Manufacturing: Finished Goods Inventories
    'AIES334416INMUS', # Capacitor, Resistor, and Inductor Manufacturing: Materials and Supplies Inventories
    'AIES334416INVUS', # Capacitor, Resistor, and Inductor Manufacturing: Total Inventories
    'AIES334416INWUS', # Capacitor, Resistor, and Inductor Manufacturing: Work In Process Inventories
    'AIES334416PAYUS', # Capacitor, Resistor, and Inductor Manufacturing: Annual Payroll
    'AIES334416PWEUS', # Capacitor, Resistor, and Inductor Manufacturing: Production Workers
    'AIES334416RCTUS', # Capacitor, Resistor, and Inductor Manufacturing: Shipments
    'AIES334416TCMUS', # Capacitor, Resistor, and Inductor Manufacturing: Total Cost of Materials
    ### 334417 Electronic Connector Manufacturing
    'AIES334417EMPUS', # Electronic Connector Manufacturing: Employees
    'AIES334417INFUS', # Electronic Connector Manufacturing: Finished Goods Inventories
    'AIES334417INMUS', # Electronic Connector Manufacturing: Materials and Supplies Inventories
    'AIES334417INVUS', # Electronic Connector Manufacturing: Total Inventories
    'AIES334417INWUS', # Electronic Connector Manufacturing: Work In Process Inventories
    'AIES334417PAYUS', # Electronic Connector Manufacturing: Annual Payroll
    'AIES334417PWEUS', # Electronic Connector Manufacturing: Production Workers
    'AIES334417RCTUS', # Electronic Connector Manufacturing: Shipments
    'AIES334417TCMUS', # Electronic Connector Manufacturing: Total Cost of Materials
    ### 334418 Printed Circuit Assembly (Electronic Assembly) Manufacturing
    'AIES334418EMPUS', # Printed Circuit Assembly (Electronic Assembly) Manufacturing: Employees
    'AIES334418INFUS', # Printed Circuit Assembly (Electronic Assembly) Manufacturing: Finished Goods Inventories
    'AIES334418INMUS', # Printed Circuit Assembly (Electronic Assembly) Manufacturing: Materials and Supplies Inventories
    'AIES334418INVUS', # Printed Circuit Assembly (Electronic Assembly) Manufacturing: Total Inventories
    'AIES334418INWUS', # Printed Circuit Assembly (Electronic Assembly) Manufacturing: Work In Process Inventories
    'AIES334418PAYUS', # Printed Circuit Assembly (Electronic Assembly) Manufacturing: Annual Payroll
    'AIES334418PWEUS', # Printed Circuit Assembly (Electronic Assembly) Manufacturing: Production Workers
    'AIES334418RCTUS', # Printed Circuit Assembly (Electronic Assembly) Manufacturing: Shipments
    'AIES334418TCMUS', # Printed Circuit Assembly (Electronic Assembly) Manufacturing: Total Cost of Materials
    ### 334419 Other Electronic Component Manufacturing
    'AIES334419EMPUS', # Other Electronic Component Manufacturing: Employees
    'AIES334419INFUS', # Other Electronic Component Manufacturing: Finished Goods Inventories
    'AIES334419INMUS', # Other Electronic Component Manufacturing: Materials and Supplies Inventories
    'AIES334419INVUS', # Other Electronic Component Manufacturing: Total Inventories
    'AIES334419INWUS', # Other Electronic Component Manufacturing: Work In Process Inventories
    'AIES334419PAYUS', # Other Electronic Component Manufacturing: Annual Payroll
    'AIES334419PWEUS', # Other Electronic Component Manufacturing: Production Workers
    'AIES334419RCTUS', # Other Electronic Component Manufacturing: Shipments
    'AIES334419TCMUS', # Other Electronic Component Manufacturing: Total Cost of Materials
    ### 3345 Electronic Instrument Manufacturing
    'AIES3345EMPUS', # Electronic Instrument Manufacturing: Employees
    'AIES3345INFUS', # Electronic Instrument Manufacturing: Finished Goods Inventories
    'AIES3345INMUS', # Electronic Instrument Manufacturing: Materials and Supplies Inventories
    'AIES3345INVUS', # Electronic Instrument Manufacturing: Total Inventories
    'AIES3345INWUS', # Electronic Instrument Manufacturing: Work In Process Inventories
    'AIES3345PAYUS', # Electronic Instrument Manufacturing: Annual Payroll
    'AIES3345PWEUS', # Electronic Instrument Manufacturing: Production Workers
    'AIES3345RCTUS', # Electronic Instrument Manufacturing: Shipments
    'AIES3345TCMUS', # Electronic Instrument Manufacturing: Total Cost of Materials
    ### 334510 Electromedical and Electrotherapeutic Apparatus Manufacturing
    'AIES334510EMPUS', # Electromedical and Electrotherapeutic Apparatus Manufacturing: Employees
    'AIES334510INFUS', # Electromedical and Electrotherapeutic Apparatus Manufacturing: Finished Goods Inventories
    'AIES334510INMUS', # Electromedical and Electrotherapeutic Apparatus Manufacturing: Materials and Supplies Inventories
    'AIES334510INVUS', # Electromedical and Electrotherapeutic Apparatus Manufacturing: Total Inventories
    'AIES334510INWUS', # Electromedical and Electrotherapeutic Apparatus Manufacturing: Work In Process Inventories
    'AIES334510PAYUS', # Electromedical and Electrotherapeutic Apparatus Manufacturing: Annual Payroll
    'AIES334510PWEUS', # Electromedical and Electrotherapeutic Apparatus Manufacturing: Production Workers
    'AIES334510RCTUS', # Electromedical and Electrotherapeutic Apparatus Manufacturing: Shipments
    'AIES334510TCMUS', # Electromedical and Electrotherapeutic Apparatus Manufacturing: Total Cost of Materials
    ### 334511 Search, Detection, and Navigation Instruments
    'AIES334511EMPUS', # Search, Detection, and Navigation Instruments: Employees
    'AIES334511INFUS', # Search, Detection, and Navigation Instruments: Finished Goods Inventories
    'AIES334511INMUS', # Search, Detection, and Navigation Instruments: Materials and Supplies Inventories
    'AIES334511INVUS', # Search, Detection, and Navigation Instruments: Total Inventories
    'AIES334511INWUS', # Search, Detection, and Navigation Instruments: Work In Process Inventories
    'AIES334511PAYUS', # Search, Detection, and Navigation Instruments: Annual Payroll
    'AIES334511PWEUS', # Search, Detection, and Navigation Instruments: Production Workers
    'AIES334511RCTUS', # Search, Detection, and Navigation Instruments: Shipments
    'AIES334511TCMUS', # Search, Detection, and Navigation Instruments: Total Cost of Materials
    ### 334512 Automatic Environmental Control Manufacturing
    'AIES334512EMPUS', # Automatic Environmental Control Manufacturing: Employees
    'AIES334512INFUS', # Automatic Environmental Control Manufacturing: Finished Goods Inventories
    'AIES334512INMUS', # Automatic Environmental Control Manufacturing: Materials and Supplies Inventories
    'AIES334512INVUS', # Automatic Environmental Control Manufacturing: Total Inventories
    'AIES334512INWUS', # Automatic Environmental Control Manufacturing: Work In Process Inventories
    'AIES334512PAYUS', # Automatic Environmental Control Manufacturing: Annual Payroll
    'AIES334512PWEUS', # Automatic Environmental Control Manufacturing: Production Workers
    'AIES334512RCTUS', # Automatic Environmental Control Manufacturing: Shipments
    'AIES334512TCMUS', # Automatic Environmental Control Manufacturing: Total Cost of Materials
    ### 334513 Industrial Process Variable Instruments
    'AIES334513EMPUS', # Industrial Process Variable Instruments: Employees
    'AIES334513INFUS', # Industrial Process Variable Instruments: Finished Goods Inventories
    'AIES334513INMUS', # Industrial Process Variable Instruments: Materials and Supplies Inventories
    'AIES334513INVUS', # Industrial Process Variable Instruments: Total Inventories
    'AIES334513INWUS', # Industrial Process Variable Instruments: Work In Process Inventories
    'AIES334513PAYUS', # Industrial Process Variable Instruments: Annual Payroll
    'AIES334513PWEUS', # Industrial Process Variable Instruments: Production Workers
    'AIES334513RCTUS', # Industrial Process Variable Instruments: Shipments
    'AIES334513TCMUS', # Industrial Process Variable Instruments: Total Cost of Materials
    ### 334514 Totalizing Fluid Meter and Counting Device Manufacturing
    'AIES334514EMPUS', # Totalizing Fluid Meter and Counting Device Manufacturing: Employees
    'AIES334514INFUS', # Totalizing Fluid Meter and Counting Device Manufacturing: Finished Goods Inventories
    'AIES334514INMUS', # Totalizing Fluid Meter and Counting Device Manufacturing: Materials and Supplies Inventories
    'AIES334514INVUS', # Totalizing Fluid Meter and Counting Device Manufacturing: Total Inventories
    'AIES334514INWUS', # Totalizing Fluid Meter and Counting Device Manufacturing: Work In Process Inventories
    'AIES334514PAYUS', # Totalizing Fluid Meter and Counting Device Manufacturing: Annual Payroll
    'AIES334514PWEUS', # Totalizing Fluid Meter and Counting Device Manufacturing: Production Workers
    'AIES334514RCTUS', # Totalizing Fluid Meter and Counting Device Manufacturing: Shipments
    'AIES334514TCMUS', # Totalizing Fluid Meter and Counting Device Manufacturing: Total Cost of Materials
    ### 334515 Electricity and Signal Testing Instruments
    'AIES334515EMPUS', # Electricity and Signal Testing Instruments: Employees
    'AIES334515INFUS', # Electricity and Signal Testing Instruments: Finished Goods Inventories
    'AIES334515INMUS', # Electricity and Signal Testing Instruments: Materials and Supplies Inventories
    'AIES334515INVUS', # Electricity and Signal Testing Instruments: Total Inventories
    'AIES334515INWUS', # Electricity and Signal Testing Instruments: Work In Process Inventories
    'AIES334515PAYUS', # Electricity and Signal Testing Instruments: Annual Payroll
    'AIES334515PWEUS', # Electricity and Signal Testing Instruments: Production Workers
    'AIES334515RCTUS', # Electricity and Signal Testing Instruments: Shipments
    'AIES334515TCMUS', # Electricity and Signal Testing Instruments: Total Cost of Materials
    ### 334516 Analytical Laboratory Instrument Manufacturing
    'AIES334516EMPUS', # Analytical Laboratory Instrument Manufacturing: Employees
    'AIES334516INFUS', # Analytical Laboratory Instrument Manufacturing: Finished Goods Inventories
    'AIES334516INMUS', # Analytical Laboratory Instrument Manufacturing: Materials and Supplies Inventories
    'AIES334516INVUS', # Analytical Laboratory Instrument Manufacturing: Total Inventories
    'AIES334516INWUS', # Analytical Laboratory Instrument Manufacturing: Work In Process Inventories
    'AIES334516PAYUS', # Analytical Laboratory Instrument Manufacturing: Annual Payroll
    'AIES334516PWEUS', # Analytical Laboratory Instrument Manufacturing: Production Workers
    'AIES334516RCTUS', # Analytical Laboratory Instrument Manufacturing: Shipments
    'AIES334516TCMUS', # Analytical Laboratory Instrument Manufacturing: Total Cost of Materials
    ### 334517 Irradiation Apparatus Manufacturing
    'AIES334517EMPUS', # Irradiation Apparatus Manufacturing: Employees
    'AIES334517INFUS', # Irradiation Apparatus Manufacturing: Finished Goods Inventories
    'AIES334517INMUS', # Irradiation Apparatus Manufacturing: Materials and Supplies Inventories
    'AIES334517INVUS', # Irradiation Apparatus Manufacturing: Total Inventories
    'AIES334517INWUS', # Irradiation Apparatus Manufacturing: Work In Process Inventories
    'AIES334517PAYUS', # Irradiation Apparatus Manufacturing: Annual Payroll
    'AIES334517PWEUS', # Irradiation Apparatus Manufacturing: Production Workers
    'AIES334517RCTUS', # Irradiation Apparatus Manufacturing: Shipments
    'AIES334517TCMUS', # Irradiation Apparatus Manufacturing: Total Cost of Materials
    ### 334519 Other Measuring and Controlling Device Manufacturing
    'AIES334519EMPUS', # Other Measuring and Controlling Device Manufacturing: Employees
    'AIES334519INFUS', # Other Measuring and Controlling Device Manufacturing: Finished Goods Inventories
    'AIES334519INMUS', # Other Measuring and Controlling Device Manufacturing: Materials and Supplies Inventories
    'AIES334519INVUS', # Other Measuring and Controlling Device Manufacturing: Total Inventories
    'AIES334519INWUS', # Other Measuring and Controlling Device Manufacturing: Work In Process Inventories
    'AIES334519PAYUS', # Other Measuring and Controlling Device Manufacturing: Annual Payroll
    'AIES334519PWEUS', # Other Measuring and Controlling Device Manufacturing: Production Workers
    'AIES334519RCTUS', # Other Measuring and Controlling Device Manufacturing: Shipments
    'AIES334519TCMUS', # Other Measuring and Controlling Device Manufacturing: Total Cost of Materials
    ### 3346 Manufacturing and Reproducing Magnetic and Optical Media
    'AIES3346EMPUS', # Manufacturing and Reproducing Magnetic and Optical Media: Employees
    'AIES3346INFUS', # Manufacturing and Reproducing Magnetic and Optical Media: Finished Goods Inventories
    'AIES3346INMUS', # Manufacturing and Reproducing Magnetic and Optical Media: Materials and Supplies Inventories
    'AIES3346INVUS', # Manufacturing and Reproducing Magnetic and Optical Media: Total Inventories
    'AIES3346INWUS', # Manufacturing and Reproducing Magnetic and Optical Media: Work In Process Inventories
    'AIES3346PAYUS', # Manufacturing and Reproducing Magnetic and Optical Media: Annual Payroll
    'AIES3346PWEUS', # Manufacturing and Reproducing Magnetic and Optical Media: Production Workers
    'AIES3346RCTUS', # Manufacturing and Reproducing Magnetic and Optical Media: Shipments
    'AIES3346TCMUS', # Manufacturing and Reproducing Magnetic and Optical Media: Total Cost of Materials
    ### 334613 Blank Magnetic and Optical Recording Media Manufacturing
    'AIES334613EMPUS', # Blank Magnetic and Optical Recording Media Manufacturing: Employees
    'AIES334613INFUS', # Blank Magnetic and Optical Recording Media Manufacturing: Finished Goods Inventories
    'AIES334613INMUS', # Blank Magnetic and Optical Recording Media Manufacturing: Materials and Supplies Inventories
    'AIES334613INVUS', # Blank Magnetic and Optical Recording Media Manufacturing: Total Inventories
    'AIES334613INWUS', # Blank Magnetic and Optical Recording Media Manufacturing: Work In Process Inventories
    'AIES334613PAYUS', # Blank Magnetic and Optical Recording Media Manufacturing: Annual Payroll
    'AIES334613PWEUS', # Blank Magnetic and Optical Recording Media Manufacturing: Production Workers
    'AIES334613RCTUS', # Blank Magnetic and Optical Recording Media Manufacturing: Shipments
    'AIES334613TCMUS', # Blank Magnetic and Optical Recording Media Manufacturing: Total Cost of Materials
    ### 334614 Software and Prerecorded Media Reproducing
    'AIES334614EMPUS', # Software and Prerecorded Media Reproducing: Employees
    'AIES334614INFUS', # Software and Prerecorded Media Reproducing: Finished Goods Inventories
    'AIES334614INMUS', # Software and Prerecorded Media Reproducing: Materials and Supplies Inventories
    'AIES334614INVUS', # Software and Prerecorded Media Reproducing: Total Inventories
    'AIES334614INWUS', # Software and Prerecorded Media Reproducing: Work In Process Inventories
    'AIES334614PAYUS', # Software and Prerecorded Media Reproducing: Annual Payroll
    'AIES334614PWEUS', # Software and Prerecorded Media Reproducing: Production Workers
    'AIES334614RCTUS', # Software and Prerecorded Media Reproducing: Shipments
    'AIES334614TCMUS', # Software and Prerecorded Media Reproducing: Total Cost of Materials
    ## NAICS 335 Electrical Equipment, Appliance, and Component Manufacturing
    ### 335 Electrical Equipment, Appliance, and Component Manufacturing
    'AIES335EMPUS', # Electrical Equipment, Appliance, and Component Manufacturing: Employees
    'AIES335INFUS', # Electrical Equipment, Appliance, and Component Manufacturing: Finished Goods Inventories
    'AIES335INMUS', # Electrical Equipment, Appliance, and Component Manufacturing: Materials and Supplies Inventories
    'AIES335INVUS', # Electrical Equipment, Appliance, and Component Manufacturing: Total Inventories
    'AIES335INWUS', # Electrical Equipment, Appliance, and Component Manufacturing: Work In Process Inventories
    'AIES335PAYUS', # Electrical Equipment, Appliance, and Component Manufacturing: Annual Payroll
    'AIES335PWEUS', # Electrical Equipment, Appliance, and Component Manufacturing: Production Workers
    'AIES335RCTUS', # Electrical Equipment, Appliance, and Component Manufacturing: Shipments
    'AIES335TCMUS', # Electrical Equipment, Appliance, and Component Manufacturing: Total Cost of Materials
    ### 3351 Electric Lighting Equipment Manufacturing
    'AIES3351EMPUS', # Electric Lighting Equipment Manufacturing: Employees
    'AIES3351INFUS', # Electric Lighting Equipment Manufacturing: Finished Goods Inventories
    'AIES3351INMUS', # Electric Lighting Equipment Manufacturing: Materials and Supplies Inventories
    'AIES3351INVUS', # Electric Lighting Equipment Manufacturing: Total Inventories
    'AIES3351INWUS', # Electric Lighting Equipment Manufacturing: Work In Process Inventories
    'AIES3351PAYUS', # Electric Lighting Equipment Manufacturing: Annual Payroll
    'AIES3351PWEUS', # Electric Lighting Equipment Manufacturing: Production Workers
    'AIES3351RCTUS', # Electric Lighting Equipment Manufacturing: Shipments
    'AIES3351TCMUS', # Electric Lighting Equipment Manufacturing: Total Cost of Materials
    ### 33511 Electric Lamp Bulb and Part Manufacturing
    'AIES33511EMPUS', # Electric Lamp Bulb and Part Manufacturing: Employees
    'AIES33511INFUS', # Electric Lamp Bulb and Part Manufacturing: Finished Goods Inventories
    'AIES33511INMUS', # Electric Lamp Bulb and Part Manufacturing: Materials and Supplies Inventories
    'AIES33511INVUS', # Electric Lamp Bulb and Part Manufacturing: Total Inventories
    'AIES33511INWUS', # Electric Lamp Bulb and Part Manufacturing: Work In Process Inventories
    'AIES33511PAYUS', # Electric Lamp Bulb and Part Manufacturing: Annual Payroll
    'AIES33511PWEUS', # Electric Lamp Bulb and Part Manufacturing: Production Workers
    'AIES33511RCTUS', # Electric Lamp Bulb and Part Manufacturing: Shipments
    'AIES33511TCMUS', # Electric Lamp Bulb and Part Manufacturing: Total Cost of Materials
    ### 33512 Lighting Fixture Manufacturing
    'AIES33512EMPUS', # Lighting Fixture Manufacturing: Employees
    'AIES33512INFUS', # Lighting Fixture Manufacturing: Finished Goods Inventories
    'AIES33512INMUS', # Lighting Fixture Manufacturing: Materials and Supplies Inventories
    'AIES33512INVUS', # Lighting Fixture Manufacturing: Total Inventories
    'AIES33512INWUS', # Lighting Fixture Manufacturing: Work In Process Inventories
    'AIES33512PAYUS', # Lighting Fixture Manufacturing: Annual Payroll
    'AIES33512PWEUS', # Lighting Fixture Manufacturing: Production Workers
    'AIES33512RCTUS', # Lighting Fixture Manufacturing: Shipments
    'AIES33512TCMUS', # Lighting Fixture Manufacturing: Total Cost of Materials
    ### 335121 Residential Electric Lighting Fixture Manufacturing
    'AIES335121EMPUS', # Residential Electric Lighting Fixture Manufacturing: Employees
    'AIES335121INFUS', # Residential Electric Lighting Fixture Manufacturing: Finished Goods Inventories
    'AIES335121INMUS', # Residential Electric Lighting Fixture Manufacturing: Materials and Supplies Inventories
    'AIES335121INVUS', # Residential Electric Lighting Fixture Manufacturing: Total Inventories
    'AIES335121INWUS', # Residential Electric Lighting Fixture Manufacturing: Work In Process Inventories
    'AIES335121PAYUS', # Residential Electric Lighting Fixture Manufacturing: Annual Payroll
    'AIES335121PWEUS', # Residential Electric Lighting Fixture Manufacturing: Production Workers
    'AIES335121RCTUS', # Residential Electric Lighting Fixture Manufacturing: Shipments
    'AIES335121TCMUS', # Residential Electric Lighting Fixture Manufacturing: Total Cost of Materials
    ### 335122 Nonresidential Electric Lighting Fixture Manufacturing
    'AIES335122EMPUS', # Nonresidential Electric Lighting Fixture Manufacturing: Employees
    'AIES335122INFUS', # Nonresidential Electric Lighting Fixture Manufacturing: Finished Goods Inventories
    'AIES335122INMUS', # Nonresidential Electric Lighting Fixture Manufacturing: Materials and Supplies Inventories
    'AIES335122INVUS', # Nonresidential Electric Lighting Fixture Manufacturing: Total Inventories
    'AIES335122INWUS', # Nonresidential Electric Lighting Fixture Manufacturing: Work In Process Inventories
    'AIES335122PAYUS', # Nonresidential Electric Lighting Fixture Manufacturing: Annual Payroll
    'AIES335122PWEUS', # Nonresidential Electric Lighting Fixture Manufacturing: Production Workers
    'AIES335122RCTUS', # Nonresidential Electric Lighting Fixture Manufacturing: Shipments
    'AIES335122TCMUS', # Nonresidential Electric Lighting Fixture Manufacturing: Total Cost of Materials
    ### 335129 Other Lighting Equipment Manufacturing
    'AIES335129EMPUS', # Other Lighting Equipment Manufacturing: Employees
    'AIES335129INFUS', # Other Lighting Equipment Manufacturing: Finished Goods Inventories
    'AIES335129INMUS', # Other Lighting Equipment Manufacturing: Materials and Supplies Inventories
    'AIES335129INVUS', # Other Lighting Equipment Manufacturing: Total Inventories
    'AIES335129INWUS', # Other Lighting Equipment Manufacturing: Work In Process Inventories
    'AIES335129PAYUS', # Other Lighting Equipment Manufacturing: Annual Payroll
    'AIES335129PWEUS', # Other Lighting Equipment Manufacturing: Production Workers
    'AIES335129RCTUS', # Other Lighting Equipment Manufacturing: Shipments
    'AIES335129TCMUS', # Other Lighting Equipment Manufacturing: Total Cost of Materials
    ### 3352 Household Appliance Manufacturing
    'AIES3352EMPUS', # Household Appliance Manufacturing: Employees
    'AIES3352INFUS', # Household Appliance Manufacturing: Finished Goods Inventories
    'AIES3352INMUS', # Household Appliance Manufacturing: Materials and Supplies Inventories
    'AIES3352INVUS', # Household Appliance Manufacturing: Total Inventories
    'AIES3352INWUS', # Household Appliance Manufacturing: Work In Process Inventories
    'AIES3352PAYUS', # Household Appliance Manufacturing: Annual Payroll
    'AIES3352PWEUS', # Household Appliance Manufacturing: Production Workers
    'AIES3352RCTUS', # Household Appliance Manufacturing: Shipments
    'AIES3352TCMUS', # Household Appliance Manufacturing: Total Cost of Materials
    ### 33521 Small Electrical Appliance Manufacturing
    'AIES33521EMPUS', # Small Electrical Appliance Manufacturing: Employees
    'AIES33521INFUS', # Small Electrical Appliance Manufacturing: Finished Goods Inventories
    'AIES33521INMUS', # Small Electrical Appliance Manufacturing: Materials and Supplies Inventories
    'AIES33521INVUS', # Small Electrical Appliance Manufacturing: Total Inventories
    'AIES33521INWUS', # Small Electrical Appliance Manufacturing: Work In Process Inventories
    'AIES33521PAYUS', # Small Electrical Appliance Manufacturing: Annual Payroll
    'AIES33521PWEUS', # Small Electrical Appliance Manufacturing: Production Workers
    'AIES33521RCTUS', # Small Electrical Appliance Manufacturing: Shipments
    'AIES33521TCMUS', # Small Electrical Appliance Manufacturing: Total Cost of Materials
    ### 33522 Major Appliance Manufacturing
    'AIES33522EMPUS', # Major Appliance Manufacturing: Employees
    'AIES33522INFUS', # Major Appliance Manufacturing: Finished Goods Inventories
    'AIES33522INMUS', # Major Appliance Manufacturing: Materials and Supplies Inventories
    'AIES33522INVUS', # Major Appliance Manufacturing: Total Inventories
    'AIES33522INWUS', # Major Appliance Manufacturing: Work In Process Inventories
    'AIES33522PAYUS', # Major Appliance Manufacturing: Annual Payroll
    'AIES33522PWEUS', # Major Appliance Manufacturing: Production Workers
    'AIES33522RCTUS', # Major Appliance Manufacturing: Shipments
    'AIES33522TCMUS', # Major Appliance Manufacturing: Total Cost of Materials
    ### 335220 Major Household Appliance Manufacturing
    'AIES335220EMPUS', # Major Household Appliance Manufacturing: Employees
    'AIES335220INFUS', # Major Household Appliance Manufacturing: Finished Goods Inventories
    'AIES335220INMUS', # Major Household Appliance Manufacturing: Materials and Supplies Inventories
    'AIES335220INVUS', # Major Household Appliance Manufacturing: Total Inventories
    'AIES335220INWUS', # Major Household Appliance Manufacturing: Work In Process Inventories
    'AIES335220PAYUS', # Major Household Appliance Manufacturing: Annual Payroll
    'AIES335220PWEUS', # Major Household Appliance Manufacturing: Production Workers
    'AIES335220RCTUS', # Major Household Appliance Manufacturing: Shipments
    'AIES335220TCMUS', # Major Household Appliance Manufacturing: Total Cost of Materials
    ### 3353 Electrical Equipment Manufacturing
    'AIES3353EMPUS', # Electrical Equipment Manufacturing: Employees
    'AIES3353INFUS', # Electrical Equipment Manufacturing: Finished Goods Inventories
    'AIES3353INMUS', # Electrical Equipment Manufacturing: Materials and Supplies Inventories
    'AIES3353INVUS', # Electrical Equipment Manufacturing: Total Inventories
    'AIES3353INWUS', # Electrical Equipment Manufacturing: Work In Process Inventories
    'AIES3353PAYUS', # Electrical Equipment Manufacturing: Annual Payroll
    'AIES3353PWEUS', # Electrical Equipment Manufacturing: Production Workers
    'AIES3353RCTUS', # Electrical Equipment Manufacturing: Shipments
    'AIES3353TCMUS', # Electrical Equipment Manufacturing: Total Cost of Materials
    ### 335311 Power, Distribution, and Specialty Transformer Manufacturing
    'AIES335311EMPUS', # Power, Distribution, and Specialty Transformer Manufacturing: Employees
    'AIES335311INFUS', # Power, Distribution, and Specialty Transformer Manufacturing: Finished Goods Inventories
    'AIES335311INMUS', # Power, Distribution, and Specialty Transformer Manufacturing: Materials and Supplies Inventories
    'AIES335311INVUS', # Power, Distribution, and Specialty Transformer Manufacturing: Total Inventories
    'AIES335311INWUS', # Power, Distribution, and Specialty Transformer Manufacturing: Work In Process Inventories
    'AIES335311PAYUS', # Power, Distribution, and Specialty Transformer Manufacturing: Annual Payroll
    'AIES335311PWEUS', # Power, Distribution, and Specialty Transformer Manufacturing: Production Workers
    'AIES335311RCTUS', # Power, Distribution, and Specialty Transformer Manufacturing: Shipments
    'AIES335311TCMUS', # Power, Distribution, and Specialty Transformer Manufacturing: Total Cost of Materials
    ### 335312 Motor and Generator Manufacturing
    'AIES335312EMPUS', # Motor and Generator Manufacturing: Employees
    'AIES335312INFUS', # Motor and Generator Manufacturing: Finished Goods Inventories
    'AIES335312INMUS', # Motor and Generator Manufacturing: Materials and Supplies Inventories
    'AIES335312INVUS', # Motor and Generator Manufacturing: Total Inventories
    'AIES335312INWUS', # Motor and Generator Manufacturing: Work In Process Inventories
    'AIES335312PAYUS', # Motor and Generator Manufacturing: Annual Payroll
    'AIES335312PWEUS', # Motor and Generator Manufacturing: Production Workers
    'AIES335312RCTUS', # Motor and Generator Manufacturing: Shipments
    'AIES335312TCMUS', # Motor and Generator Manufacturing: Total Cost of Materials
    ### 335313 Switchgear and Switchboard Apparatus Manufacturing
    'AIES335313EMPUS', # Switchgear and Switchboard Apparatus Manufacturing: Employees
    'AIES335313INFUS', # Switchgear and Switchboard Apparatus Manufacturing: Finished Goods Inventories
    'AIES335313INMUS', # Switchgear and Switchboard Apparatus Manufacturing: Materials and Supplies Inventories
    'AIES335313INVUS', # Switchgear and Switchboard Apparatus Manufacturing: Total Inventories
    'AIES335313INWUS', # Switchgear and Switchboard Apparatus Manufacturing: Work In Process Inventories
    'AIES335313PAYUS', # Switchgear and Switchboard Apparatus Manufacturing: Annual Payroll
    'AIES335313PWEUS', # Switchgear and Switchboard Apparatus Manufacturing: Production Workers
    'AIES335313RCTUS', # Switchgear and Switchboard Apparatus Manufacturing: Shipments
    'AIES335313TCMUS', # Switchgear and Switchboard Apparatus Manufacturing: Total Cost of Materials
    ### 335314 Relay and Industrial Control Manufacturing
    'AIES335314EMPUS', # Relay and Industrial Control Manufacturing: Employees
    'AIES335314INFUS', # Relay and Industrial Control Manufacturing: Finished Goods Inventories
    'AIES335314INMUS', # Relay and Industrial Control Manufacturing: Materials and Supplies Inventories
    'AIES335314INVUS', # Relay and Industrial Control Manufacturing: Total Inventories
    'AIES335314INWUS', # Relay and Industrial Control Manufacturing: Work In Process Inventories
    'AIES335314PAYUS', # Relay and Industrial Control Manufacturing: Annual Payroll
    'AIES335314PWEUS', # Relay and Industrial Control Manufacturing: Production Workers
    'AIES335314RCTUS', # Relay and Industrial Control Manufacturing: Shipments
    'AIES335314TCMUS', # Relay and Industrial Control Manufacturing: Total Cost of Materials
    ### 3359 Other Electrical Equipment and Component Manufacturing
    'AIES3359EMPUS', # Other Electrical Equipment and Component Manufacturing: Employees
    'AIES3359INFUS', # Other Electrical Equipment and Component Manufacturing: Finished Goods Inventories
    'AIES3359INMUS', # Other Electrical Equipment and Component Manufacturing: Materials and Supplies Inventories
    'AIES3359INVUS', # Other Electrical Equipment and Component Manufacturing: Total Inventories
    'AIES3359INWUS', # Other Electrical Equipment and Component Manufacturing: Work In Process Inventories
    'AIES3359PAYUS', # Other Electrical Equipment and Component Manufacturing: Annual Payroll
    'AIES3359PWEUS', # Other Electrical Equipment and Component Manufacturing: Production Workers
    'AIES3359RCTUS', # Other Electrical Equipment and Component Manufacturing: Shipments
    'AIES3359TCMUS', # Other Electrical Equipment and Component Manufacturing: Total Cost of Materials
    ### 33591 Battery Manufacturing
    'AIES33591EMPUS', # Battery Manufacturing: Employees
    'AIES33591INFUS', # Battery Manufacturing: Finished Goods Inventories
    'AIES33591INMUS', # Battery Manufacturing: Materials and Supplies Inventories
    'AIES33591INVUS', # Battery Manufacturing: Total Inventories
    'AIES33591INWUS', # Battery Manufacturing: Work In Process Inventories
    'AIES33591PAYUS', # Battery Manufacturing: Annual Payroll
    'AIES33591PWEUS', # Battery Manufacturing: Production Workers
    'AIES33591RCTUS', # Battery Manufacturing: Shipments
    'AIES33591TCMUS', # Battery Manufacturing: Total Cost of Materials
    ### 335911 Storage Battery Manufacturing
    'AIES335911EMPUS', # Storage Battery Manufacturing: Employees
    'AIES335911INFUS', # Storage Battery Manufacturing: Finished Goods Inventories
    'AIES335911INMUS', # Storage Battery Manufacturing: Materials and Supplies Inventories
    'AIES335911INVUS', # Storage Battery Manufacturing: Total Inventories
    'AIES335911INWUS', # Storage Battery Manufacturing: Work In Process Inventories
    'AIES335911PAYUS', # Storage Battery Manufacturing: Annual Payroll
    'AIES335911PWEUS', # Storage Battery Manufacturing: Production Workers
    'AIES335911RCTUS', # Storage Battery Manufacturing: Shipments
    'AIES335911TCMUS', # Storage Battery Manufacturing: Total Cost of Materials
    ### 335912 Primary Battery Manufacturing
    'AIES335912EMPUS', # Primary Battery Manufacturing: Employees
    'AIES335912INFUS', # Primary Battery Manufacturing: Finished Goods Inventories
    'AIES335912INMUS', # Primary Battery Manufacturing: Materials and Supplies Inventories
    'AIES335912INVUS', # Primary Battery Manufacturing: Total Inventories
    'AIES335912INWUS', # Primary Battery Manufacturing: Work In Process Inventories
    'AIES335912PAYUS', # Primary Battery Manufacturing: Annual Payroll
    'AIES335912PWEUS', # Primary Battery Manufacturing: Production Workers
    'AIES335912RCTUS', # Primary Battery Manufacturing: Shipments
    'AIES335912TCMUS', # Primary Battery Manufacturing: Total Cost of Materials
    ### 33592 Communication and Energy Wire and Cable Manufacturing
    'AIES33592EMPUS', # Communication and Energy Wire and Cable Manufacturing: Employees
    'AIES33592INFUS', # Communication and Energy Wire and Cable Manufacturing: Finished Goods Inventories
    'AIES33592INMUS', # Communication and Energy Wire and Cable Manufacturing: Materials and Supplies Inventories
    'AIES33592INVUS', # Communication and Energy Wire and Cable Manufacturing: Total Inventories
    'AIES33592INWUS', # Communication and Energy Wire and Cable Manufacturing: Work In Process Inventories
    'AIES33592PAYUS', # Communication and Energy Wire and Cable Manufacturing: Annual Payroll
    'AIES33592PWEUS', # Communication and Energy Wire and Cable Manufacturing: Production Workers
    'AIES33592RCTUS', # Communication and Energy Wire and Cable Manufacturing: Shipments
    'AIES33592TCMUS', # Communication and Energy Wire and Cable Manufacturing: Total Cost of Materials
    ### 335921 Fiber Optic Cable Manufacturing
    'AIES335921EMPUS', # Fiber Optic Cable Manufacturing: Employees
    'AIES335921INFUS', # Fiber Optic Cable Manufacturing: Finished Goods Inventories
    'AIES335921INMUS', # Fiber Optic Cable Manufacturing: Materials and Supplies Inventories
    'AIES335921INVUS', # Fiber Optic Cable Manufacturing: Total Inventories
    'AIES335921INWUS', # Fiber Optic Cable Manufacturing: Work In Process Inventories
    'AIES335921PAYUS', # Fiber Optic Cable Manufacturing: Annual Payroll
    'AIES335921PWEUS', # Fiber Optic Cable Manufacturing: Production Workers
    'AIES335921RCTUS', # Fiber Optic Cable Manufacturing: Shipments
    'AIES335921TCMUS', # Fiber Optic Cable Manufacturing: Total Cost of Materials
    ### 335929 Other Communication and Energy Wire Manufacturing
    'AIES335929EMPUS', # Other Communication and Energy Wire Manufacturing: Employees
    'AIES335929INFUS', # Other Communication and Energy Wire Manufacturing: Finished Goods Inventories
    'AIES335929INMUS', # Other Communication and Energy Wire Manufacturing: Materials and Supplies Inventories
    'AIES335929INVUS', # Other Communication and Energy Wire Manufacturing: Total Inventories
    'AIES335929INWUS', # Other Communication and Energy Wire Manufacturing: Work In Process Inventories
    'AIES335929PAYUS', # Other Communication and Energy Wire Manufacturing: Annual Payroll
    'AIES335929PWEUS', # Other Communication and Energy Wire Manufacturing: Production Workers
    'AIES335929RCTUS', # Other Communication and Energy Wire Manufacturing: Shipments
    'AIES335929TCMUS', # Other Communication and Energy Wire Manufacturing: Total Cost of Materials
    ### 33593 Wiring Device Manufacturing
    'AIES33593EMPUS', # Wiring Device Manufacturing: Employees
    'AIES33593INFUS', # Wiring Device Manufacturing: Finished Goods Inventories
    'AIES33593INMUS', # Wiring Device Manufacturing: Materials and Supplies Inventories
    'AIES33593INVUS', # Wiring Device Manufacturing: Total Inventories
    'AIES33593INWUS', # Wiring Device Manufacturing: Work In Process Inventories
    'AIES33593PAYUS', # Wiring Device Manufacturing: Annual Payroll
    'AIES33593PWEUS', # Wiring Device Manufacturing: Production Workers
    'AIES33593RCTUS', # Wiring Device Manufacturing: Shipments
    'AIES33593TCMUS', # Wiring Device Manufacturing: Total Cost of Materials
    ### 335931 Current-Carrying Wiring Device Manufacturing
    'AIES335931EMPUS', # Current-Carrying Wiring Device Manufacturing: Employees
    'AIES335931INFUS', # Current-Carrying Wiring Device Manufacturing: Finished Goods Inventories
    'AIES335931INMUS', # Current-Carrying Wiring Device Manufacturing: Materials and Supplies Inventories
    'AIES335931INVUS', # Current-Carrying Wiring Device Manufacturing: Total Inventories
    'AIES335931INWUS', # Current-Carrying Wiring Device Manufacturing: Work In Process Inventories
    'AIES335931PAYUS', # Current-Carrying Wiring Device Manufacturing: Annual Payroll
    'AIES335931PWEUS', # Current-Carrying Wiring Device Manufacturing: Production Workers
    'AIES335931RCTUS', # Current-Carrying Wiring Device Manufacturing: Shipments
    'AIES335931TCMUS', # Current-Carrying Wiring Device Manufacturing: Total Cost of Materials
    ### 335932 Noncurrent-Carrying Wiring Device Manufacturing
    'AIES335932EMPUS', # Noncurrent-Carrying Wiring Device Manufacturing: Employees
    'AIES335932INFUS', # Noncurrent-Carrying Wiring Device Manufacturing: Finished Goods Inventories
    'AIES335932INMUS', # Noncurrent-Carrying Wiring Device Manufacturing: Materials and Supplies Inventories
    'AIES335932INVUS', # Noncurrent-Carrying Wiring Device Manufacturing: Total Inventories
    'AIES335932INWUS', # Noncurrent-Carrying Wiring Device Manufacturing: Work In Process Inventories
    'AIES335932PAYUS', # Noncurrent-Carrying Wiring Device Manufacturing: Annual Payroll
    'AIES335932PWEUS', # Noncurrent-Carrying Wiring Device Manufacturing: Production Workers
    'AIES335932RCTUS', # Noncurrent-Carrying Wiring Device Manufacturing: Shipments
    'AIES335932TCMUS', # Noncurrent-Carrying Wiring Device Manufacturing: Total Cost of Materials
    ### 33599 All Other Electrical Equipment and Component Manufacturing
    'AIES33599EMPUS', # All Other Electrical Equipment and Component Manufacturing: Employees
    'AIES33599INFUS', # All Other Electrical Equipment and Component Manufacturing: Finished Goods Inventories
    'AIES33599INMUS', # All Other Electrical Equipment and Component Manufacturing: Materials and Supplies Inventories
    'AIES33599INVUS', # All Other Electrical Equipment and Component Manufacturing: Total Inventories
    'AIES33599INWUS', # All Other Electrical Equipment and Component Manufacturing: Work In Process Inventories
    'AIES33599PAYUS', # All Other Electrical Equipment and Component Manufacturing: Annual Payroll
    'AIES33599PWEUS', # All Other Electrical Equipment and Component Manufacturing: Production Workers
    'AIES33599RCTUS', # All Other Electrical Equipment and Component Manufacturing: Shipments
    'AIES33599TCMUS', # All Other Electrical Equipment and Component Manufacturing: Total Cost of Materials
    ### 335991 Carbon and Graphite Product Manufacturing
    'AIES335991EMPUS', # Carbon and Graphite Product Manufacturing: Employees
    'AIES335991INFUS', # Carbon and Graphite Product Manufacturing: Finished Goods Inventories
    'AIES335991INMUS', # Carbon and Graphite Product Manufacturing: Materials and Supplies Inventories
    'AIES335991INVUS', # Carbon and Graphite Product Manufacturing: Total Inventories
    'AIES335991INWUS', # Carbon and Graphite Product Manufacturing: Work In Process Inventories
    'AIES335991PAYUS', # Carbon and Graphite Product Manufacturing: Annual Payroll
    'AIES335991PWEUS', # Carbon and Graphite Product Manufacturing: Production Workers
    'AIES335991RCTUS', # Carbon and Graphite Product Manufacturing: Shipments
    'AIES335991TCMUS', # Carbon and Graphite Product Manufacturing: Total Cost of Materials
    ### 335999 Miscellaneous Electrical Equipment Manufacturing
    'AIES335999EMPUS', # Miscellaneous Electrical Equipment Manufacturing: Employees
    'AIES335999INFUS', # Miscellaneous Electrical Equipment Manufacturing: Finished Goods Inventories
    'AIES335999INMUS', # Miscellaneous Electrical Equipment Manufacturing: Materials and Supplies Inventories
    'AIES335999INVUS', # Miscellaneous Electrical Equipment Manufacturing: Total Inventories
    'AIES335999INWUS', # Miscellaneous Electrical Equipment Manufacturing: Work In Process Inventories
    'AIES335999PAYUS', # Miscellaneous Electrical Equipment Manufacturing: Annual Payroll
    'AIES335999PWEUS', # Miscellaneous Electrical Equipment Manufacturing: Production Workers
    'AIES335999RCTUS', # Miscellaneous Electrical Equipment Manufacturing: Shipments
    'AIES335999TCMUS', # Miscellaneous Electrical Equipment Manufacturing: Total Cost of Materials
    ## NAICS 336 Transportation Equipment Manufacturing
    ### 336 Transportation Equipment Manufacturing
    'AIES336EMPUS', # Transportation Equipment Manufacturing: Employees
    'AIES336INFUS', # Transportation Equipment Manufacturing: Finished Goods Inventories
    'AIES336INMUS', # Transportation Equipment Manufacturing: Materials and Supplies Inventories
    'AIES336INVUS', # Transportation Equipment Manufacturing: Total Inventories
    'AIES336INWUS', # Transportation Equipment Manufacturing: Work In Process Inventories
    'AIES336PAYUS', # Transportation Equipment Manufacturing: Annual Payroll
    'AIES336PWEUS', # Transportation Equipment Manufacturing: Production Workers
    'AIES336RCTUS', # Transportation Equipment Manufacturing: Shipments
    'AIES336TCMUS', # Transportation Equipment Manufacturing: Total Cost of Materials
    ### 3361 Motor Vehicle Manufacturing
    'AIES3361EMPUS', # Motor Vehicle Manufacturing: Employees
    'AIES3361INFUS', # Motor Vehicle Manufacturing: Finished Goods Inventories
    'AIES3361INMUS', # Motor Vehicle Manufacturing: Materials and Supplies Inventories
    'AIES3361INVUS', # Motor Vehicle Manufacturing: Total Inventories
    'AIES3361INWUS', # Motor Vehicle Manufacturing: Work In Process Inventories
    'AIES3361PAYUS', # Motor Vehicle Manufacturing: Annual Payroll
    'AIES3361PWEUS', # Motor Vehicle Manufacturing: Production Workers
    'AIES3361RCTUS', # Motor Vehicle Manufacturing: Shipments
    'AIES3361TCMUS', # Motor Vehicle Manufacturing: Total Cost of Materials
    ### 33611 Automobile and Light Duty Motor Vehicle Manufacturing
    'AIES33611EMPUS', # Automobile and Light Duty Motor Vehicle Manufacturing: Employees
    'AIES33611INFUS', # Automobile and Light Duty Motor Vehicle Manufacturing: Finished Goods Inventories
    'AIES33611INMUS', # Automobile and Light Duty Motor Vehicle Manufacturing: Materials and Supplies Inventories
    'AIES33611INVUS', # Automobile and Light Duty Motor Vehicle Manufacturing: Total Inventories
    'AIES33611INWUS', # Automobile and Light Duty Motor Vehicle Manufacturing: Work In Process Inventories
    'AIES33611PAYUS', # Automobile and Light Duty Motor Vehicle Manufacturing: Annual Payroll
    'AIES33611PWEUS', # Automobile and Light Duty Motor Vehicle Manufacturing: Production Workers
    'AIES33611RCTUS', # Automobile and Light Duty Motor Vehicle Manufacturing: Shipments
    'AIES33611TCMUS', # Automobile and Light Duty Motor Vehicle Manufacturing: Total Cost of Materials
    ### 336111 Automobile Manufacturing
    'AIES336111EMPUS', # Automobile Manufacturing: Employees
    'AIES336111INFUS', # Automobile Manufacturing: Finished Goods Inventories
    'AIES336111INMUS', # Automobile Manufacturing: Materials and Supplies Inventories
    'AIES336111INVUS', # Automobile Manufacturing: Total Inventories
    'AIES336111INWUS', # Automobile Manufacturing: Work In Process Inventories
    'AIES336111PAYUS', # Automobile Manufacturing: Annual Payroll
    'AIES336111PWEUS', # Automobile Manufacturing: Production Workers
    'AIES336111RCTUS', # Automobile Manufacturing: Shipments
    'AIES336111TCMUS', # Automobile Manufacturing: Total Cost of Materials
    ### 336112 Light Truck and Utility Vehicle Manufacturing
    'AIES336112EMPUS', # Light Truck and Utility Vehicle Manufacturing: Employees
    'AIES336112INFUS', # Light Truck and Utility Vehicle Manufacturing: Finished Goods Inventories
    'AIES336112INMUS', # Light Truck and Utility Vehicle Manufacturing: Materials and Supplies Inventories
    'AIES336112INVUS', # Light Truck and Utility Vehicle Manufacturing: Total Inventories
    'AIES336112INWUS', # Light Truck and Utility Vehicle Manufacturing: Work In Process Inventories
    'AIES336112PAYUS', # Light Truck and Utility Vehicle Manufacturing: Annual Payroll
    'AIES336112PWEUS', # Light Truck and Utility Vehicle Manufacturing: Production Workers
    'AIES336112RCTUS', # Light Truck and Utility Vehicle Manufacturing: Shipments
    'AIES336112TCMUS', # Light Truck and Utility Vehicle Manufacturing: Total Cost of Materials
    ### 33612 Heavy Duty Truck Manufacturing
    'AIES33612EMPUS', # Heavy Duty Truck Manufacturing: Employees
    'AIES33612INFUS', # Heavy Duty Truck Manufacturing: Finished Goods Inventories
    'AIES33612INMUS', # Heavy Duty Truck Manufacturing: Materials and Supplies Inventories
    'AIES33612INVUS', # Heavy Duty Truck Manufacturing: Total Inventories
    'AIES33612INWUS', # Heavy Duty Truck Manufacturing: Work In Process Inventories
    'AIES33612PAYUS', # Heavy Duty Truck Manufacturing: Annual Payroll
    'AIES33612PWEUS', # Heavy Duty Truck Manufacturing: Production Workers
    'AIES33612RCTUS', # Heavy Duty Truck Manufacturing: Shipments
    'AIES33612TCMUS', # Heavy Duty Truck Manufacturing: Total Cost of Materials
    ### 3362 Motor Vehicle Body and Trailer Manufacturing
    'AIES3362EMPUS', # Motor Vehicle Body and Trailer Manufacturing: Employees
    'AIES3362INFUS', # Motor Vehicle Body and Trailer Manufacturing: Finished Goods Inventories
    'AIES3362INMUS', # Motor Vehicle Body and Trailer Manufacturing: Materials and Supplies Inventories
    'AIES3362INVUS', # Motor Vehicle Body and Trailer Manufacturing: Total Inventories
    'AIES3362INWUS', # Motor Vehicle Body and Trailer Manufacturing: Work In Process Inventories
    'AIES3362PAYUS', # Motor Vehicle Body and Trailer Manufacturing: Annual Payroll
    'AIES3362PWEUS', # Motor Vehicle Body and Trailer Manufacturing: Production Workers
    'AIES3362RCTUS', # Motor Vehicle Body and Trailer Manufacturing: Shipments
    'AIES3362TCMUS', # Motor Vehicle Body and Trailer Manufacturing: Total Cost of Materials
    ### 336211 Motor Vehicle Body Manufacturing
    'AIES336211EMPUS', # Motor Vehicle Body Manufacturing: Employees
    'AIES336211INFUS', # Motor Vehicle Body Manufacturing: Finished Goods Inventories
    'AIES336211INMUS', # Motor Vehicle Body Manufacturing: Materials and Supplies Inventories
    'AIES336211INVUS', # Motor Vehicle Body Manufacturing: Total Inventories
    'AIES336211INWUS', # Motor Vehicle Body Manufacturing: Work In Process Inventories
    'AIES336211PAYUS', # Motor Vehicle Body Manufacturing: Annual Payroll
    'AIES336211PWEUS', # Motor Vehicle Body Manufacturing: Production Workers
    'AIES336211RCTUS', # Motor Vehicle Body Manufacturing: Shipments
    'AIES336211TCMUS', # Motor Vehicle Body Manufacturing: Total Cost of Materials
    ### 336212 Truck Trailer Manufacturing
    'AIES336212EMPUS', # Truck Trailer Manufacturing: Employees
    'AIES336212INFUS', # Truck Trailer Manufacturing: Finished Goods Inventories
    'AIES336212INMUS', # Truck Trailer Manufacturing: Materials and Supplies Inventories
    'AIES336212INVUS', # Truck Trailer Manufacturing: Total Inventories
    'AIES336212INWUS', # Truck Trailer Manufacturing: Work In Process Inventories
    'AIES336212PAYUS', # Truck Trailer Manufacturing: Annual Payroll
    'AIES336212PWEUS', # Truck Trailer Manufacturing: Production Workers
    'AIES336212RCTUS', # Truck Trailer Manufacturing: Shipments
    'AIES336212TCMUS', # Truck Trailer Manufacturing: Total Cost of Materials
    ### 336213 Motor Home Manufacturing
    'AIES336213EMPUS', # Motor Home Manufacturing: Employees
    'AIES336213INFUS', # Motor Home Manufacturing: Finished Goods Inventories
    'AIES336213INMUS', # Motor Home Manufacturing: Materials and Supplies Inventories
    'AIES336213INVUS', # Motor Home Manufacturing: Total Inventories
    'AIES336213INWUS', # Motor Home Manufacturing: Work In Process Inventories
    'AIES336213PAYUS', # Motor Home Manufacturing: Annual Payroll
    'AIES336213PWEUS', # Motor Home Manufacturing: Production Workers
    'AIES336213RCTUS', # Motor Home Manufacturing: Shipments
    'AIES336213TCMUS', # Motor Home Manufacturing: Total Cost of Materials
    ### 336214 Travel Trailer and Camper Manufacturing
    'AIES336214EMPUS', # Travel Trailer and Camper Manufacturing: Employees
    'AIES336214INFUS', # Travel Trailer and Camper Manufacturing: Finished Goods Inventories
    'AIES336214INMUS', # Travel Trailer and Camper Manufacturing: Materials and Supplies Inventories
    'AIES336214INVUS', # Travel Trailer and Camper Manufacturing: Total Inventories
    'AIES336214INWUS', # Travel Trailer and Camper Manufacturing: Work In Process Inventories
    'AIES336214PAYUS', # Travel Trailer and Camper Manufacturing: Annual Payroll
    'AIES336214PWEUS', # Travel Trailer and Camper Manufacturing: Production Workers
    'AIES336214RCTUS', # Travel Trailer and Camper Manufacturing: Shipments
    'AIES336214TCMUS', # Travel Trailer and Camper Manufacturing: Total Cost of Materials
    ### 3363 Motor Vehicle Parts Manufacturing
    'AIES3363EMPUS', # Motor Vehicle Parts Manufacturing: Employees
    'AIES3363INFUS', # Motor Vehicle Parts Manufacturing: Finished Goods Inventories
    'AIES3363INMUS', # Motor Vehicle Parts Manufacturing: Materials and Supplies Inventories
    'AIES3363INVUS', # Motor Vehicle Parts Manufacturing: Total Inventories
    'AIES3363INWUS', # Motor Vehicle Parts Manufacturing: Work In Process Inventories
    'AIES3363PAYUS', # Motor Vehicle Parts Manufacturing: Annual Payroll
    'AIES3363PWEUS', # Motor Vehicle Parts Manufacturing: Production Workers
    'AIES3363RCTUS', # Motor Vehicle Parts Manufacturing: Shipments
    'AIES3363TCMUS', # Motor Vehicle Parts Manufacturing: Total Cost of Materials
    ### 33631 Motor Vehicle Gasoline Engine and Engine Parts Manufacturing
    'AIES33631EMPUS', # Motor Vehicle Gasoline Engine and Engine Parts Manufacturing: Employees
    'AIES33631INFUS', # Motor Vehicle Gasoline Engine and Engine Parts Manufacturing: Finished Goods Inventories
    'AIES33631INMUS', # Motor Vehicle Gasoline Engine and Engine Parts Manufacturing: Materials and Supplies Inventories
    'AIES33631INVUS', # Motor Vehicle Gasoline Engine and Engine Parts Manufacturing: Total Inventories
    'AIES33631INWUS', # Motor Vehicle Gasoline Engine and Engine Parts Manufacturing: Work In Process Inventories
    'AIES33631PAYUS', # Motor Vehicle Gasoline Engine and Engine Parts Manufacturing: Annual Payroll
    'AIES33631PWEUS', # Motor Vehicle Gasoline Engine and Engine Parts Manufacturing: Production Workers
    'AIES33631RCTUS', # Motor Vehicle Gasoline Engine and Engine Parts Manufacturing: Shipments
    'AIES33631TCMUS', # Motor Vehicle Gasoline Engine and Engine Parts Manufacturing: Total Cost of Materials
    ### 33632 Motor Vehicle Electrical and Electronic Equipment Manufacturing
    'AIES33632EMPUS', # Motor Vehicle Electrical and Electronic Equipment Manufacturing: Employees
    'AIES33632INFUS', # Motor Vehicle Electrical and Electronic Equipment Manufacturing: Finished Goods Inventories
    'AIES33632INMUS', # Motor Vehicle Electrical and Electronic Equipment Manufacturing: Materials and Supplies Inventories
    'AIES33632INVUS', # Motor Vehicle Electrical and Electronic Equipment Manufacturing: Total Inventories
    'AIES33632INWUS', # Motor Vehicle Electrical and Electronic Equipment Manufacturing: Work In Process Inventories
    'AIES33632PAYUS', # Motor Vehicle Electrical and Electronic Equipment Manufacturing: Annual Payroll
    'AIES33632PWEUS', # Motor Vehicle Electrical and Electronic Equipment Manufacturing: Production Workers
    'AIES33632RCTUS', # Motor Vehicle Electrical and Electronic Equipment Manufacturing: Shipments
    'AIES33632TCMUS', # Motor Vehicle Electrical and Electronic Equipment Manufacturing: Total Cost of Materials
    ### 33633 Motor Vehicle Steering and Suspension Parts
    'AIES33633EMPUS', # Motor Vehicle Steering and Suspension Parts: Employees
    'AIES33633INFUS', # Motor Vehicle Steering and Suspension Parts: Finished Goods Inventories
    'AIES33633INMUS', # Motor Vehicle Steering and Suspension Parts: Materials and Supplies Inventories
    'AIES33633INVUS', # Motor Vehicle Steering and Suspension Parts: Total Inventories
    'AIES33633INWUS', # Motor Vehicle Steering and Suspension Parts: Work In Process Inventories
    'AIES33633PAYUS', # Motor Vehicle Steering and Suspension Parts: Annual Payroll
    'AIES33633PWEUS', # Motor Vehicle Steering and Suspension Parts: Production Workers
    'AIES33633RCTUS', # Motor Vehicle Steering and Suspension Parts: Shipments
    'AIES33633TCMUS', # Motor Vehicle Steering and Suspension Parts: Total Cost of Materials
    ### 33634 Motor Vehicle Brake System Manufacturing
    'AIES33634EMPUS', # Motor Vehicle Brake System Manufacturing: Employees
    'AIES33634INFUS', # Motor Vehicle Brake System Manufacturing: Finished Goods Inventories
    'AIES33634INMUS', # Motor Vehicle Brake System Manufacturing: Materials and Supplies Inventories
    'AIES33634INVUS', # Motor Vehicle Brake System Manufacturing: Total Inventories
    'AIES33634INWUS', # Motor Vehicle Brake System Manufacturing: Work In Process Inventories
    'AIES33634PAYUS', # Motor Vehicle Brake System Manufacturing: Annual Payroll
    'AIES33634PWEUS', # Motor Vehicle Brake System Manufacturing: Production Workers
    'AIES33634RCTUS', # Motor Vehicle Brake System Manufacturing: Shipments
    'AIES33634TCMUS', # Motor Vehicle Brake System Manufacturing: Total Cost of Materials
    ### 33635 Motor Vehicle Transmission and Power Train Parts Manufacturing
    'AIES33635EMPUS', # Motor Vehicle Transmission and Power Train Parts Manufacturing: Employees
    'AIES33635INFUS', # Motor Vehicle Transmission and Power Train Parts Manufacturing: Finished Goods Inventories
    'AIES33635INMUS', # Motor Vehicle Transmission and Power Train Parts Manufacturing: Materials and Supplies Inventories
    'AIES33635INVUS', # Motor Vehicle Transmission and Power Train Parts Manufacturing: Total Inventories
    'AIES33635INWUS', # Motor Vehicle Transmission and Power Train Parts Manufacturing: Work In Process Inventories
    'AIES33635PAYUS', # Motor Vehicle Transmission and Power Train Parts Manufacturing: Annual Payroll
    'AIES33635PWEUS', # Motor Vehicle Transmission and Power Train Parts Manufacturing: Production Workers
    'AIES33635RCTUS', # Motor Vehicle Transmission and Power Train Parts Manufacturing: Shipments
    'AIES33635TCMUS', # Motor Vehicle Transmission and Power Train Parts Manufacturing: Total Cost of Materials
    ### 33636 Motor Vehicle Seating and Interior Trim Manufacturing
    'AIES33636EMPUS', # Motor Vehicle Seating and Interior Trim Manufacturing: Employees
    'AIES33636INFUS', # Motor Vehicle Seating and Interior Trim Manufacturing: Finished Goods Inventories
    'AIES33636INMUS', # Motor Vehicle Seating and Interior Trim Manufacturing: Materials and Supplies Inventories
    'AIES33636INVUS', # Motor Vehicle Seating and Interior Trim Manufacturing: Total Inventories
    'AIES33636INWUS', # Motor Vehicle Seating and Interior Trim Manufacturing: Work In Process Inventories
    'AIES33636PAYUS', # Motor Vehicle Seating and Interior Trim Manufacturing: Annual Payroll
    'AIES33636PWEUS', # Motor Vehicle Seating and Interior Trim Manufacturing: Production Workers
    'AIES33636RCTUS', # Motor Vehicle Seating and Interior Trim Manufacturing: Shipments
    'AIES33636TCMUS', # Motor Vehicle Seating and Interior Trim Manufacturing: Total Cost of Materials
    ### 33637 Motor Vehicle Metal Stamping
    'AIES33637EMPUS', # Motor Vehicle Metal Stamping: Employees
    'AIES33637INFUS', # Motor Vehicle Metal Stamping: Finished Goods Inventories
    'AIES33637INMUS', # Motor Vehicle Metal Stamping: Materials and Supplies Inventories
    'AIES33637INVUS', # Motor Vehicle Metal Stamping: Total Inventories
    'AIES33637INWUS', # Motor Vehicle Metal Stamping: Work In Process Inventories
    'AIES33637PAYUS', # Motor Vehicle Metal Stamping: Annual Payroll
    'AIES33637PWEUS', # Motor Vehicle Metal Stamping: Production Workers
    'AIES33637RCTUS', # Motor Vehicle Metal Stamping: Shipments
    'AIES33637TCMUS', # Motor Vehicle Metal Stamping: Total Cost of Materials
    ### 33639 Other Motor Vehicle Parts Manufacturing
    'AIES33639EMPUS', # Other Motor Vehicle Parts Manufacturing: Employees
    'AIES33639INFUS', # Other Motor Vehicle Parts Manufacturing: Finished Goods Inventories
    'AIES33639INMUS', # Other Motor Vehicle Parts Manufacturing: Materials and Supplies Inventories
    'AIES33639INVUS', # Other Motor Vehicle Parts Manufacturing: Total Inventories
    'AIES33639INWUS', # Other Motor Vehicle Parts Manufacturing: Work In Process Inventories
    'AIES33639PAYUS', # Other Motor Vehicle Parts Manufacturing: Annual Payroll
    'AIES33639PWEUS', # Other Motor Vehicle Parts Manufacturing: Production Workers
    'AIES33639RCTUS', # Other Motor Vehicle Parts Manufacturing: Shipments
    'AIES33639TCMUS', # Other Motor Vehicle Parts Manufacturing: Total Cost of Materials
    ### 3364 Aerospace Product and Parts Manufacturing
    'AIES3364EMPUS', # Aerospace Product and Parts Manufacturing: Employees
    'AIES3364INFUS', # Aerospace Product and Parts Manufacturing: Finished Goods Inventories
    'AIES3364INMUS', # Aerospace Product and Parts Manufacturing: Materials and Supplies Inventories
    'AIES3364INVUS', # Aerospace Product and Parts Manufacturing: Total Inventories
    'AIES3364INWUS', # Aerospace Product and Parts Manufacturing: Work In Process Inventories
    'AIES3364PAYUS', # Aerospace Product and Parts Manufacturing: Annual Payroll
    'AIES3364PWEUS', # Aerospace Product and Parts Manufacturing: Production Workers
    'AIES3364RCTUS', # Aerospace Product and Parts Manufacturing: Shipments
    'AIES3364TCMUS', # Aerospace Product and Parts Manufacturing: Total Cost of Materials
    ### 336411 Aircraft Manufacturing
    'AIES336411EMPUS', # Aircraft Manufacturing: Employees
    'AIES336411INFUS', # Aircraft Manufacturing: Finished Goods Inventories
    'AIES336411INMUS', # Aircraft Manufacturing: Materials and Supplies Inventories
    'AIES336411INVUS', # Aircraft Manufacturing: Total Inventories
    'AIES336411INWUS', # Aircraft Manufacturing: Work In Process Inventories
    'AIES336411PAYUS', # Aircraft Manufacturing: Annual Payroll
    'AIES336411PWEUS', # Aircraft Manufacturing: Production Workers
    'AIES336411RCTUS', # Aircraft Manufacturing: Shipments
    'AIES336411TCMUS', # Aircraft Manufacturing: Total Cost of Materials
    ### 336412 Aircraft Engine and Engine Parts Manufacturing
    'AIES336412EMPUS', # Aircraft Engine and Engine Parts Manufacturing: Employees
    'AIES336412INFUS', # Aircraft Engine and Engine Parts Manufacturing: Finished Goods Inventories
    'AIES336412INMUS', # Aircraft Engine and Engine Parts Manufacturing: Materials and Supplies Inventories
    'AIES336412INVUS', # Aircraft Engine and Engine Parts Manufacturing: Total Inventories
    'AIES336412INWUS', # Aircraft Engine and Engine Parts Manufacturing: Work In Process Inventories
    'AIES336412PAYUS', # Aircraft Engine and Engine Parts Manufacturing: Annual Payroll
    'AIES336412PWEUS', # Aircraft Engine and Engine Parts Manufacturing: Production Workers
    'AIES336412RCTUS', # Aircraft Engine and Engine Parts Manufacturing: Shipments
    'AIES336412TCMUS', # Aircraft Engine and Engine Parts Manufacturing: Total Cost of Materials
    ### 336413 Other Aircraft Parts and Auxiliary Equipment Manufacturing
    'AIES336413EMPUS', # Other Aircraft Parts and Auxiliary Equipment Manufacturing: Employees
    'AIES336413INFUS', # Other Aircraft Parts and Auxiliary Equipment Manufacturing: Finished Goods Inventories
    'AIES336413INMUS', # Other Aircraft Parts and Auxiliary Equipment Manufacturing: Materials and Supplies Inventories
    'AIES336413INVUS', # Other Aircraft Parts and Auxiliary Equipment Manufacturing: Total Inventories
    'AIES336413INWUS', # Other Aircraft Parts and Auxiliary Equipment Manufacturing: Work In Process Inventories
    'AIES336413PAYUS', # Other Aircraft Parts and Auxiliary Equipment Manufacturing: Annual Payroll
    'AIES336413PWEUS', # Other Aircraft Parts and Auxiliary Equipment Manufacturing: Production Workers
    'AIES336413RCTUS', # Other Aircraft Parts and Auxiliary Equipment Manufacturing: Shipments
    'AIES336413TCMUS', # Other Aircraft Parts and Auxiliary Equipment Manufacturing: Total Cost of Materials
    ### 336414 Guided Missile and Space Vehicle Manufacturing
    'AIES336414EMPUS', # Guided Missile and Space Vehicle Manufacturing: Employees
    'AIES336414INFUS', # Guided Missile and Space Vehicle Manufacturing: Finished Goods Inventories
    'AIES336414INMUS', # Guided Missile and Space Vehicle Manufacturing: Materials and Supplies Inventories
    'AIES336414INVUS', # Guided Missile and Space Vehicle Manufacturing: Total Inventories
    'AIES336414INWUS', # Guided Missile and Space Vehicle Manufacturing: Work In Process Inventories
    'AIES336414PAYUS', # Guided Missile and Space Vehicle Manufacturing: Annual Payroll
    'AIES336414PWEUS', # Guided Missile and Space Vehicle Manufacturing: Production Workers
    'AIES336414RCTUS', # Guided Missile and Space Vehicle Manufacturing: Shipments
    'AIES336414TCMUS', # Guided Missile and Space Vehicle Manufacturing: Total Cost of Materials
    ### 336415 Space Vehicle Propulsion Units and Parts Manufacturing
    'AIES336415EMPUS', # Space Vehicle Propulsion Units and Parts Manufacturing: Employees
    'AIES336415INFUS', # Space Vehicle Propulsion Units and Parts Manufacturing: Finished Goods Inventories
    'AIES336415INMUS', # Space Vehicle Propulsion Units and Parts Manufacturing: Materials and Supplies Inventories
    'AIES336415INVUS', # Space Vehicle Propulsion Units and Parts Manufacturing: Total Inventories
    'AIES336415INWUS', # Space Vehicle Propulsion Units and Parts Manufacturing: Work In Process Inventories
    'AIES336415PAYUS', # Space Vehicle Propulsion Units and Parts Manufacturing: Annual Payroll
    'AIES336415PWEUS', # Space Vehicle Propulsion Units and Parts Manufacturing: Production Workers
    'AIES336415RCTUS', # Space Vehicle Propulsion Units and Parts Manufacturing: Shipments
    'AIES336415TCMUS', # Space Vehicle Propulsion Units and Parts Manufacturing: Total Cost of Materials
    ### 336419 Other Guided Missile and Space Vehicle Parts
    'AIES336419EMPUS', # Other Guided Missile and Space Vehicle Parts: Employees
    'AIES336419INFUS', # Other Guided Missile and Space Vehicle Parts: Finished Goods Inventories
    'AIES336419INMUS', # Other Guided Missile and Space Vehicle Parts: Materials and Supplies Inventories
    'AIES336419INVUS', # Other Guided Missile and Space Vehicle Parts: Total Inventories
    'AIES336419INWUS', # Other Guided Missile and Space Vehicle Parts: Work In Process Inventories
    'AIES336419PAYUS', # Other Guided Missile and Space Vehicle Parts: Annual Payroll
    'AIES336419PWEUS', # Other Guided Missile and Space Vehicle Parts: Production Workers
    'AIES336419RCTUS', # Other Guided Missile and Space Vehicle Parts: Shipments
    'AIES336419TCMUS', # Other Guided Missile and Space Vehicle Parts: Total Cost of Materials
    ### 3365 Railroad Rolling Stock Manufacturing
    'AIES3365EMPUS', # Railroad Rolling Stock Manufacturing: Employees
    'AIES3365INFUS', # Railroad Rolling Stock Manufacturing: Finished Goods Inventories
    'AIES3365INMUS', # Railroad Rolling Stock Manufacturing: Materials and Supplies Inventories
    'AIES3365INVUS', # Railroad Rolling Stock Manufacturing: Total Inventories
    'AIES3365INWUS', # Railroad Rolling Stock Manufacturing: Work In Process Inventories
    'AIES3365PAYUS', # Railroad Rolling Stock Manufacturing: Annual Payroll
    'AIES3365PWEUS', # Railroad Rolling Stock Manufacturing: Production Workers
    'AIES3365RCTUS', # Railroad Rolling Stock Manufacturing: Shipments
    'AIES3365TCMUS', # Railroad Rolling Stock Manufacturing: Total Cost of Materials
    ### 3366 Ship and Boat Building
    'AIES3366EMPUS', # Ship and Boat Building: Employees
    'AIES3366INFUS', # Ship and Boat Building: Finished Goods Inventories
    'AIES3366INMUS', # Ship and Boat Building: Materials and Supplies Inventories
    'AIES3366INVUS', # Ship and Boat Building: Total Inventories
    'AIES3366INWUS', # Ship and Boat Building: Work In Process Inventories
    'AIES3366PAYUS', # Ship and Boat Building: Annual Payroll
    'AIES3366PWEUS', # Ship and Boat Building: Production Workers
    'AIES3366RCTUS', # Ship and Boat Building: Shipments
    'AIES3366TCMUS', # Ship and Boat Building: Total Cost of Materials
    ### 336611 Ship Building and Repairing
    'AIES336611EMPUS', # Ship Building and Repairing: Employees
    'AIES336611INFUS', # Ship Building and Repairing: Finished Goods Inventories
    'AIES336611INMUS', # Ship Building and Repairing: Materials and Supplies Inventories
    'AIES336611INVUS', # Ship Building and Repairing: Total Inventories
    'AIES336611INWUS', # Ship Building and Repairing: Work In Process Inventories
    'AIES336611PAYUS', # Ship Building and Repairing: Annual Payroll
    'AIES336611PWEUS', # Ship Building and Repairing: Production Workers
    'AIES336611RCTUS', # Ship Building and Repairing: Shipments
    'AIES336611TCMUS', # Ship Building and Repairing: Total Cost of Materials
    ### 336612 Boat Building
    'AIES336612EMPUS', # Boat Building: Employees
    'AIES336612INFUS', # Boat Building: Finished Goods Inventories
    'AIES336612INMUS', # Boat Building: Materials and Supplies Inventories
    'AIES336612INVUS', # Boat Building: Total Inventories
    'AIES336612INWUS', # Boat Building: Work In Process Inventories
    'AIES336612PAYUS', # Boat Building: Annual Payroll
    'AIES336612PWEUS', # Boat Building: Production Workers
    'AIES336612RCTUS', # Boat Building: Shipments
    'AIES336612TCMUS', # Boat Building: Total Cost of Materials
    ### 3369 Other Transportation Equipment Manufacturing
    'AIES3369EMPUS', # Other Transportation Equipment Manufacturing: Employees
    'AIES3369INFUS', # Other Transportation Equipment Manufacturing: Finished Goods Inventories
    'AIES3369INMUS', # Other Transportation Equipment Manufacturing: Materials and Supplies Inventories
    'AIES3369INVUS', # Other Transportation Equipment Manufacturing: Total Inventories
    'AIES3369INWUS', # Other Transportation Equipment Manufacturing: Work In Process Inventories
    'AIES3369PAYUS', # Other Transportation Equipment Manufacturing: Annual Payroll
    'AIES3369PWEUS', # Other Transportation Equipment Manufacturing: Production Workers
    'AIES3369RCTUS', # Other Transportation Equipment Manufacturing: Shipments
    'AIES3369TCMUS', # Other Transportation Equipment Manufacturing: Total Cost of Materials
    ### 336991 Motorcycle, Bicycle, and Parts Manufacturing
    'AIES336991EMPUS', # Motorcycle, Bicycle, and Parts Manufacturing: Employees
    'AIES336991INFUS', # Motorcycle, Bicycle, and Parts Manufacturing: Finished Goods Inventories
    'AIES336991INMUS', # Motorcycle, Bicycle, and Parts Manufacturing: Materials and Supplies Inventories
    'AIES336991INVUS', # Motorcycle, Bicycle, and Parts Manufacturing: Total Inventories
    'AIES336991INWUS', # Motorcycle, Bicycle, and Parts Manufacturing: Work In Process Inventories
    'AIES336991PAYUS', # Motorcycle, Bicycle, and Parts Manufacturing: Annual Payroll
    'AIES336991PWEUS', # Motorcycle, Bicycle, and Parts Manufacturing: Production Workers
    'AIES336991RCTUS', # Motorcycle, Bicycle, and Parts Manufacturing: Shipments
    'AIES336991TCMUS', # Motorcycle, Bicycle, and Parts Manufacturing: Total Cost of Materials
    ### 336992 Military Armored Vehicle, Tank, and Tank Component Manufacturing
    'AIES336992EMPUS', # Military Armored Vehicle, Tank, and Tank Component Manufacturing: Employees
    'AIES336992INFUS', # Military Armored Vehicle, Tank, and Tank Component Manufacturing: Finished Goods Inventories
    'AIES336992INMUS', # Military Armored Vehicle, Tank, and Tank Component Manufacturing: Materials and Supplies Inventories
    'AIES336992INVUS', # Military Armored Vehicle, Tank, and Tank Component Manufacturing: Total Inventories
    'AIES336992INWUS', # Military Armored Vehicle, Tank, and Tank Component Manufacturing: Work In Process Inventories
    'AIES336992PAYUS', # Military Armored Vehicle, Tank, and Tank Component Manufacturing: Annual Payroll
    'AIES336992PWEUS', # Military Armored Vehicle, Tank, and Tank Component Manufacturing: Production Workers
    'AIES336992RCTUS', # Military Armored Vehicle, Tank, and Tank Component Manufacturing: Shipments
    'AIES336992TCMUS', # Military Armored Vehicle, Tank, and Tank Component Manufacturing: Total Cost of Materials
    ### 336999 All Other Transportation Equipment Manufacturing
    'AIES336999EMPUS', # All Other Transportation Equipment Manufacturing: Employees
    'AIES336999INFUS', # All Other Transportation Equipment Manufacturing: Finished Goods Inventories
    'AIES336999INMUS', # All Other Transportation Equipment Manufacturing: Materials and Supplies Inventories
    'AIES336999INVUS', # All Other Transportation Equipment Manufacturing: Total Inventories
    'AIES336999INWUS', # All Other Transportation Equipment Manufacturing: Work In Process Inventories
    'AIES336999PAYUS', # All Other Transportation Equipment Manufacturing: Annual Payroll
    'AIES336999PWEUS', # All Other Transportation Equipment Manufacturing: Production Workers
    'AIES336999RCTUS', # All Other Transportation Equipment Manufacturing: Shipments
    'AIES336999TCMUS', # All Other Transportation Equipment Manufacturing: Total Cost of Materials
    ## NAICS 337 Furniture and Related Product Manufacturing
    ### 337 Furniture and Related Product Manufacturing
    'AIES337EMPUS', # Furniture and Related Product Manufacturing: Employees
    'AIES337INFUS', # Furniture and Related Product Manufacturing: Finished Goods Inventories
    'AIES337INMUS', # Furniture and Related Product Manufacturing: Materials and Supplies Inventories
    'AIES337INVUS', # Furniture and Related Product Manufacturing: Total Inventories
    'AIES337INWUS', # Furniture and Related Product Manufacturing: Work In Process Inventories
    'AIES337PAYUS', # Furniture and Related Product Manufacturing: Annual Payroll
    'AIES337PWEUS', # Furniture and Related Product Manufacturing: Production Workers
    'AIES337RCTUS', # Furniture and Related Product Manufacturing: Shipments
    'AIES337TCMUS', # Furniture and Related Product Manufacturing: Total Cost of Materials
    ### 3371 Household and Institutional Furniture Manufacturing
    'AIES3371EMPUS', # Household and Institutional Furniture Manufacturing: Employees
    'AIES3371INFUS', # Household and Institutional Furniture Manufacturing: Finished Goods Inventories
    'AIES3371INMUS', # Household and Institutional Furniture Manufacturing: Materials and Supplies Inventories
    'AIES3371INVUS', # Household and Institutional Furniture Manufacturing: Total Inventories
    'AIES3371INWUS', # Household and Institutional Furniture Manufacturing: Work In Process Inventories
    'AIES3371PAYUS', # Household and Institutional Furniture Manufacturing: Annual Payroll
    'AIES3371PWEUS', # Household and Institutional Furniture Manufacturing: Production Workers
    'AIES3371RCTUS', # Household and Institutional Furniture Manufacturing: Shipments
    'AIES3371TCMUS', # Household and Institutional Furniture Manufacturing: Total Cost of Materials
    ### 33711 Wood Kitchen Cabinet and Countertop Manufacturing
    'AIES33711EMPUS', # Wood Kitchen Cabinet and Countertop Manufacturing: Employees
    'AIES33711INFUS', # Wood Kitchen Cabinet and Countertop Manufacturing: Finished Goods Inventories
    'AIES33711INMUS', # Wood Kitchen Cabinet and Countertop Manufacturing: Materials and Supplies Inventories
    'AIES33711INVUS', # Wood Kitchen Cabinet and Countertop Manufacturing: Total Inventories
    'AIES33711INWUS', # Wood Kitchen Cabinet and Countertop Manufacturing: Work In Process Inventories
    'AIES33711PAYUS', # Wood Kitchen Cabinet and Countertop Manufacturing: Annual Payroll
    'AIES33711PWEUS', # Wood Kitchen Cabinet and Countertop Manufacturing: Production Workers
    'AIES33711RCTUS', # Wood Kitchen Cabinet and Countertop Manufacturing: Shipments
    'AIES33711TCMUS', # Wood Kitchen Cabinet and Countertop Manufacturing: Total Cost of Materials
    ### 33712 Household and Institutional Furniture Manufacturing
    'AIES33712EMPUS', # Household and Institutional Furniture Manufacturing: Employees
    'AIES33712INFUS', # Household and Institutional Furniture Manufacturing: Finished Goods Inventories
    'AIES33712INMUS', # Household and Institutional Furniture Manufacturing: Materials and Supplies Inventories
    'AIES33712INVUS', # Household and Institutional Furniture Manufacturing: Total Inventories
    'AIES33712INWUS', # Household and Institutional Furniture Manufacturing: Work In Process Inventories
    'AIES33712PAYUS', # Household and Institutional Furniture Manufacturing: Annual Payroll
    'AIES33712PWEUS', # Household and Institutional Furniture Manufacturing: Production Workers
    'AIES33712RCTUS', # Household and Institutional Furniture Manufacturing: Shipments
    'AIES33712TCMUS', # Household and Institutional Furniture Manufacturing: Total Cost of Materials
    ### 337121 Upholstered Household Furniture Manufacturing
    'AIES337121EMPUS', # Upholstered Household Furniture Manufacturing: Employees
    'AIES337121INFUS', # Upholstered Household Furniture Manufacturing: Finished Goods Inventories
    'AIES337121INMUS', # Upholstered Household Furniture Manufacturing: Materials and Supplies Inventories
    'AIES337121INVUS', # Upholstered Household Furniture Manufacturing: Total Inventories
    'AIES337121INWUS', # Upholstered Household Furniture Manufacturing: Work In Process Inventories
    'AIES337121PAYUS', # Upholstered Household Furniture Manufacturing: Annual Payroll
    'AIES337121PWEUS', # Upholstered Household Furniture Manufacturing: Production Workers
    'AIES337121RCTUS', # Upholstered Household Furniture Manufacturing: Shipments
    'AIES337121TCMUS', # Upholstered Household Furniture Manufacturing: Total Cost of Materials
    ### 337122 Nonupholstered Wood Household Furniture Manufacturing
    'AIES337122EMPUS', # Nonupholstered Wood Household Furniture Manufacturing: Employees
    'AIES337122INFUS', # Nonupholstered Wood Household Furniture Manufacturing: Finished Goods Inventories
    'AIES337122INMUS', # Nonupholstered Wood Household Furniture Manufacturing: Materials and Supplies Inventories
    'AIES337122INVUS', # Nonupholstered Wood Household Furniture Manufacturing: Total Inventories
    'AIES337122INWUS', # Nonupholstered Wood Household Furniture Manufacturing: Work In Process Inventories
    'AIES337122PAYUS', # Nonupholstered Wood Household Furniture Manufacturing: Annual Payroll
    'AIES337122PWEUS', # Nonupholstered Wood Household Furniture Manufacturing: Production Workers
    'AIES337122RCTUS', # Nonupholstered Wood Household Furniture Manufacturing: Shipments
    'AIES337122TCMUS', # Nonupholstered Wood Household Furniture Manufacturing: Total Cost of Materials
    ### 337124 Metal Household Furniture Manufacturing
    'AIES337124EMPUS', # Metal Household Furniture Manufacturing: Employees
    'AIES337124INFUS', # Metal Household Furniture Manufacturing: Finished Goods Inventories
    'AIES337124INMUS', # Metal Household Furniture Manufacturing: Materials and Supplies Inventories
    'AIES337124INVUS', # Metal Household Furniture Manufacturing: Total Inventories
    'AIES337124INWUS', # Metal Household Furniture Manufacturing: Work In Process Inventories
    'AIES337124PAYUS', # Metal Household Furniture Manufacturing: Annual Payroll
    'AIES337124PWEUS', # Metal Household Furniture Manufacturing: Production Workers
    'AIES337124RCTUS', # Metal Household Furniture Manufacturing: Shipments
    'AIES337124TCMUS', # Metal Household Furniture Manufacturing: Total Cost of Materials
    ### 337125 Household Furniture (Except Wood and Metal) Manufacturing
    'AIES337125EMPUS', # Household Furniture (Except Wood and Metal) Manufacturing: Employees
    'AIES337125INFUS', # Household Furniture (Except Wood and Metal) Manufacturing: Finished Goods Inventories
    'AIES337125INMUS', # Household Furniture (Except Wood and Metal) Manufacturing: Materials and Supplies Inventories
    'AIES337125INVUS', # Household Furniture (Except Wood and Metal) Manufacturing: Total Inventories
    'AIES337125INWUS', # Household Furniture (Except Wood and Metal) Manufacturing: Work In Process Inventories
    'AIES337125PAYUS', # Household Furniture (Except Wood and Metal) Manufacturing: Annual Payroll
    'AIES337125PWEUS', # Household Furniture (Except Wood and Metal) Manufacturing: Production Workers
    'AIES337125RCTUS', # Household Furniture (Except Wood and Metal) Manufacturing: Shipments
    'AIES337125TCMUS', # Household Furniture (Except Wood and Metal) Manufacturing: Total Cost of Materials
    ### 337127 Institutional Furniture Manufacturing
    'AIES337127EMPUS', # Institutional Furniture Manufacturing: Employees
    'AIES337127INFUS', # Institutional Furniture Manufacturing: Finished Goods Inventories
    'AIES337127INMUS', # Institutional Furniture Manufacturing: Materials and Supplies Inventories
    'AIES337127INVUS', # Institutional Furniture Manufacturing: Total Inventories
    'AIES337127INWUS', # Institutional Furniture Manufacturing: Work In Process Inventories
    'AIES337127PAYUS', # Institutional Furniture Manufacturing: Annual Payroll
    'AIES337127PWEUS', # Institutional Furniture Manufacturing: Production Workers
    'AIES337127RCTUS', # Institutional Furniture Manufacturing: Shipments
    'AIES337127TCMUS', # Institutional Furniture Manufacturing: Total Cost of Materials
    ### 3372 Office Furniture (Including Fixtures) Manufacturing
    'AIES3372EMPUS', # Office Furniture (Including Fixtures) Manufacturing: Employees
    'AIES3372INFUS', # Office Furniture (Including Fixtures) Manufacturing: Finished Goods Inventories
    'AIES3372INMUS', # Office Furniture (Including Fixtures) Manufacturing: Materials and Supplies Inventories
    'AIES3372INVUS', # Office Furniture (Including Fixtures) Manufacturing: Total Inventories
    'AIES3372INWUS', # Office Furniture (Including Fixtures) Manufacturing: Work In Process Inventories
    'AIES3372PAYUS', # Office Furniture (Including Fixtures) Manufacturing: Annual Payroll
    'AIES3372PWEUS', # Office Furniture (Including Fixtures) Manufacturing: Production Workers
    'AIES3372RCTUS', # Office Furniture (Including Fixtures) Manufacturing: Shipments
    'AIES3372TCMUS', # Office Furniture (Including Fixtures) Manufacturing: Total Cost of Materials
    ### 337211 Wood Office Furniture Manufacturing
    'AIES337211EMPUS', # Wood Office Furniture Manufacturing: Employees
    'AIES337211INFUS', # Wood Office Furniture Manufacturing: Finished Goods Inventories
    'AIES337211INMUS', # Wood Office Furniture Manufacturing: Materials and Supplies Inventories
    'AIES337211INVUS', # Wood Office Furniture Manufacturing: Total Inventories
    'AIES337211INWUS', # Wood Office Furniture Manufacturing: Work In Process Inventories
    'AIES337211PAYUS', # Wood Office Furniture Manufacturing: Annual Payroll
    'AIES337211PWEUS', # Wood Office Furniture Manufacturing: Production Workers
    'AIES337211RCTUS', # Wood Office Furniture Manufacturing: Shipments
    'AIES337211TCMUS', # Wood Office Furniture Manufacturing: Total Cost of Materials
    ### 337212 Custom Architectural Woodwork and Millwork Manufacturing
    'AIES337212EMPUS', # Custom Architectural Woodwork and Millwork Manufacturing: Employees
    'AIES337212INFUS', # Custom Architectural Woodwork and Millwork Manufacturing: Finished Goods Inventories
    'AIES337212INMUS', # Custom Architectural Woodwork and Millwork Manufacturing: Materials and Supplies Inventories
    'AIES337212INVUS', # Custom Architectural Woodwork and Millwork Manufacturing: Total Inventories
    'AIES337212INWUS', # Custom Architectural Woodwork and Millwork Manufacturing: Work In Process Inventories
    'AIES337212PAYUS', # Custom Architectural Woodwork and Millwork Manufacturing: Annual Payroll
    'AIES337212PWEUS', # Custom Architectural Woodwork and Millwork Manufacturing: Production Workers
    'AIES337212RCTUS', # Custom Architectural Woodwork and Millwork Manufacturing: Shipments
    'AIES337212TCMUS', # Custom Architectural Woodwork and Millwork Manufacturing: Total Cost of Materials
    ### 337214 Office Furniture (Except Wood) Manufacturing
    'AIES337214EMPUS', # Office Furniture (Except Wood) Manufacturing: Employees
    'AIES337214INFUS', # Office Furniture (Except Wood) Manufacturing: Finished Goods Inventories
    'AIES337214INMUS', # Office Furniture (Except Wood) Manufacturing: Materials and Supplies Inventories
    'AIES337214INVUS', # Office Furniture (Except Wood) Manufacturing: Total Inventories
    'AIES337214INWUS', # Office Furniture (Except Wood) Manufacturing: Work In Process Inventories
    'AIES337214PAYUS', # Office Furniture (Except Wood) Manufacturing: Annual Payroll
    'AIES337214PWEUS', # Office Furniture (Except Wood) Manufacturing: Production Workers
    'AIES337214RCTUS', # Office Furniture (Except Wood) Manufacturing: Shipments
    'AIES337214TCMUS', # Office Furniture (Except Wood) Manufacturing: Total Cost of Materials
    ### 337215 Showcase, Partition, Shelving, and Locker Manufacturing
    'AIES337215EMPUS', # Showcase, Partition, Shelving, and Locker Manufacturing: Employees
    'AIES337215INFUS', # Showcase, Partition, Shelving, and Locker Manufacturing: Finished Goods Inventories
    'AIES337215INMUS', # Showcase, Partition, Shelving, and Locker Manufacturing: Materials and Supplies Inventories
    'AIES337215INVUS', # Showcase, Partition, Shelving, and Locker Manufacturing: Total Inventories
    'AIES337215INWUS', # Showcase, Partition, Shelving, and Locker Manufacturing: Work In Process Inventories
    'AIES337215PAYUS', # Showcase, Partition, Shelving, and Locker Manufacturing: Annual Payroll
    'AIES337215PWEUS', # Showcase, Partition, Shelving, and Locker Manufacturing: Production Workers
    'AIES337215RCTUS', # Showcase, Partition, Shelving, and Locker Manufacturing: Shipments
    'AIES337215TCMUS', # Showcase, Partition, Shelving, and Locker Manufacturing: Total Cost of Materials
    ### 3379 Other Furniture Related Product Manufacturing
    'AIES3379EMPUS', # Other Furniture Related Product Manufacturing: Employees
    'AIES3379INFUS', # Other Furniture Related Product Manufacturing: Finished Goods Inventories
    'AIES3379INMUS', # Other Furniture Related Product Manufacturing: Materials and Supplies Inventories
    'AIES3379INVUS', # Other Furniture Related Product Manufacturing: Total Inventories
    'AIES3379INWUS', # Other Furniture Related Product Manufacturing: Work In Process Inventories
    'AIES3379PAYUS', # Other Furniture Related Product Manufacturing: Annual Payroll
    'AIES3379PWEUS', # Other Furniture Related Product Manufacturing: Production Workers
    'AIES3379RCTUS', # Other Furniture Related Product Manufacturing: Shipments
    'AIES3379TCMUS', # Other Furniture Related Product Manufacturing: Total Cost of Materials
    ### 33791 Mattress Manufacturing
    'AIES33791EMPUS', # Mattress Manufacturing: Employees
    'AIES33791INFUS', # Mattress Manufacturing: Finished Goods Inventories
    'AIES33791INMUS', # Mattress Manufacturing: Materials and Supplies Inventories
    'AIES33791INVUS', # Mattress Manufacturing: Total Inventories
    'AIES33791INWUS', # Mattress Manufacturing: Work In Process Inventories
    'AIES33791PAYUS', # Mattress Manufacturing: Annual Payroll
    'AIES33791PWEUS', # Mattress Manufacturing: Production Workers
    'AIES33791RCTUS', # Mattress Manufacturing: Shipments
    'AIES33791TCMUS', # Mattress Manufacturing: Total Cost of Materials
    ### 33792 Blind and Shade Manufacturing
    'AIES33792EMPUS', # Blind and Shade Manufacturing: Employees
    'AIES33792INFUS', # Blind and Shade Manufacturing: Finished Goods Inventories
    'AIES33792INMUS', # Blind and Shade Manufacturing: Materials and Supplies Inventories
    'AIES33792INVUS', # Blind and Shade Manufacturing: Total Inventories
    'AIES33792INWUS', # Blind and Shade Manufacturing: Work In Process Inventories
    'AIES33792PAYUS', # Blind and Shade Manufacturing: Annual Payroll
    'AIES33792PWEUS', # Blind and Shade Manufacturing: Production Workers
    'AIES33792RCTUS', # Blind and Shade Manufacturing: Shipments
    'AIES33792TCMUS', # Blind and Shade Manufacturing: Total Cost of Materials
    ## NAICS 339 Miscellaneous Manufacturing
    ### 339 Miscellaneous Manufacturing
    'AIES339EMPUS', # Miscellaneous Manufacturing: Employees
    'AIES339INFUS', # Miscellaneous Manufacturing: Finished Goods Inventories
    'AIES339INMUS', # Miscellaneous Manufacturing: Materials and Supplies Inventories
    'AIES339INVUS', # Miscellaneous Manufacturing: Total Inventories
    'AIES339INWUS', # Miscellaneous Manufacturing: Work In Process Inventories
    'AIES339PAYUS', # Miscellaneous Manufacturing: Annual Payroll
    'AIES339PWEUS', # Miscellaneous Manufacturing: Production Workers
    'AIES339RCTUS', # Miscellaneous Manufacturing: Shipments
    'AIES339TCMUS', # Miscellaneous Manufacturing: Total Cost of Materials
    ### 3391 Medical Equipment and Supplies Manufacturing
    'AIES3391EMPUS', # Medical Equipment and Supplies Manufacturing: Employees
    'AIES3391INFUS', # Medical Equipment and Supplies Manufacturing: Finished Goods Inventories
    'AIES3391INMUS', # Medical Equipment and Supplies Manufacturing: Materials and Supplies Inventories
    'AIES3391INVUS', # Medical Equipment and Supplies Manufacturing: Total Inventories
    'AIES3391INWUS', # Medical Equipment and Supplies Manufacturing: Work In Process Inventories
    'AIES3391PAYUS', # Medical Equipment and Supplies Manufacturing: Annual Payroll
    'AIES3391PWEUS', # Medical Equipment and Supplies Manufacturing: Production Workers
    'AIES3391RCTUS', # Medical Equipment and Supplies Manufacturing: Shipments
    'AIES3391TCMUS', # Medical Equipment and Supplies Manufacturing: Total Cost of Materials
    ### 339112 Surgical and Medical Instrument Manufacturing
    'AIES339112EMPUS', # Surgical and Medical Instrument Manufacturing: Employees
    'AIES339112INFUS', # Surgical and Medical Instrument Manufacturing: Finished Goods Inventories
    'AIES339112INMUS', # Surgical and Medical Instrument Manufacturing: Materials and Supplies Inventories
    'AIES339112INVUS', # Surgical and Medical Instrument Manufacturing: Total Inventories
    'AIES339112INWUS', # Surgical and Medical Instrument Manufacturing: Work In Process Inventories
    'AIES339112PAYUS', # Surgical and Medical Instrument Manufacturing: Annual Payroll
    'AIES339112PWEUS', # Surgical and Medical Instrument Manufacturing: Production Workers
    'AIES339112RCTUS', # Surgical and Medical Instrument Manufacturing: Shipments
    'AIES339112TCMUS', # Surgical and Medical Instrument Manufacturing: Total Cost of Materials
    ### 339114 Dental Equipment and Supplies Manufacturing
    'AIES339114EMPUS', # Dental Equipment and Supplies Manufacturing: Employees
    'AIES339114INFUS', # Dental Equipment and Supplies Manufacturing: Finished Goods Inventories
    'AIES339114INMUS', # Dental Equipment and Supplies Manufacturing: Materials and Supplies Inventories
    'AIES339114INVUS', # Dental Equipment and Supplies Manufacturing: Total Inventories
    'AIES339114INWUS', # Dental Equipment and Supplies Manufacturing: Work In Process Inventories
    'AIES339114PAYUS', # Dental Equipment and Supplies Manufacturing: Annual Payroll
    'AIES339114PWEUS', # Dental Equipment and Supplies Manufacturing: Production Workers
    'AIES339114RCTUS', # Dental Equipment and Supplies Manufacturing: Shipments
    'AIES339114TCMUS', # Dental Equipment and Supplies Manufacturing: Total Cost of Materials
    ### 339115 Ophthalmic Goods Manufacturing
    'AIES339115EMPUS', # Ophthalmic Goods Manufacturing: Employees
    'AIES339115INFUS', # Ophthalmic Goods Manufacturing: Finished Goods Inventories
    'AIES339115INMUS', # Ophthalmic Goods Manufacturing: Materials and Supplies Inventories
    'AIES339115INVUS', # Ophthalmic Goods Manufacturing: Total Inventories
    'AIES339115INWUS', # Ophthalmic Goods Manufacturing: Work In Process Inventories
    'AIES339115PAYUS', # Ophthalmic Goods Manufacturing: Annual Payroll
    'AIES339115PWEUS', # Ophthalmic Goods Manufacturing: Production Workers
    'AIES339115RCTUS', # Ophthalmic Goods Manufacturing: Shipments
    'AIES339115TCMUS', # Ophthalmic Goods Manufacturing: Total Cost of Materials
    ### 339116 Dental Laboratories
    'AIES339116EMPUS', # Dental Laboratories: Employees
    'AIES339116INFUS', # Dental Laboratories: Finished Goods Inventories
    'AIES339116INMUS', # Dental Laboratories: Materials and Supplies Inventories
    'AIES339116INVUS', # Dental Laboratories: Total Inventories
    'AIES339116INWUS', # Dental Laboratories: Work In Process Inventories
    'AIES339116PAYUS', # Dental Laboratories: Annual Payroll
    'AIES339116PWEUS', # Dental Laboratories: Production Workers
    'AIES339116RCTUS', # Dental Laboratories: Shipments
    'AIES339116TCMUS', # Dental Laboratories: Total Cost of Materials
    ### 3399 Other Miscellaneous Manufacturing
    'AIES3399EMPUS', # Other Miscellaneous Manufacturing: Employees
    'AIES3399INFUS', # Other Miscellaneous Manufacturing: Finished Goods Inventories
    'AIES3399INMUS', # Other Miscellaneous Manufacturing: Materials and Supplies Inventories
    'AIES3399INVUS', # Other Miscellaneous Manufacturing: Total Inventories
    'AIES3399INWUS', # Other Miscellaneous Manufacturing: Work In Process Inventories
    'AIES3399PAYUS', # Other Miscellaneous Manufacturing: Annual Payroll
    'AIES3399PWEUS', # Other Miscellaneous Manufacturing: Production Workers
    'AIES3399RCTUS', # Other Miscellaneous Manufacturing: Shipments
    'AIES3399TCMUS', # Other Miscellaneous Manufacturing: Total Cost of Materials
    ### 33991 Jewelry and Silverware Manufacturing
    'AIES33991EMPUS', # Jewelry and Silverware Manufacturing: Employees
    'AIES33991INFUS', # Jewelry and Silverware Manufacturing: Finished Goods Inventories
    'AIES33991INMUS', # Jewelry and Silverware Manufacturing: Materials and Supplies Inventories
    'AIES33991INVUS', # Jewelry and Silverware Manufacturing: Total Inventories
    'AIES33991INWUS', # Jewelry and Silverware Manufacturing: Work In Process Inventories
    'AIES33991PAYUS', # Jewelry and Silverware Manufacturing: Annual Payroll
    'AIES33991PWEUS', # Jewelry and Silverware Manufacturing: Production Workers
    'AIES33991RCTUS', # Jewelry and Silverware Manufacturing: Shipments
    'AIES33991TCMUS', # Jewelry and Silverware Manufacturing: Total Cost of Materials
    ### 33992 Sporting and Athletic Goods Manufacturing
    'AIES33992EMPUS', # Sporting and Athletic Goods Manufacturing: Employees
    'AIES33992INFUS', # Sporting and Athletic Goods Manufacturing: Finished Goods Inventories
    'AIES33992INMUS', # Sporting and Athletic Goods Manufacturing: Materials and Supplies Inventories
    'AIES33992INVUS', # Sporting and Athletic Goods Manufacturing: Total Inventories
    'AIES33992INWUS', # Sporting and Athletic Goods Manufacturing: Work In Process Inventories
    'AIES33992PAYUS', # Sporting and Athletic Goods Manufacturing: Annual Payroll
    'AIES33992PWEUS', # Sporting and Athletic Goods Manufacturing: Production Workers
    'AIES33992RCTUS', # Sporting and Athletic Goods Manufacturing: Shipments
    'AIES33992TCMUS', # Sporting and Athletic Goods Manufacturing: Total Cost of Materials
    ### 33993 Doll, Toy, and Game Manufacturing
    'AIES33993EMPUS', # Doll, Toy, and Game Manufacturing: Employees
    'AIES33993INFUS', # Doll, Toy, and Game Manufacturing: Finished Goods Inventories
    'AIES33993INMUS', # Doll, Toy, and Game Manufacturing: Materials and Supplies Inventories
    'AIES33993INVUS', # Doll, Toy, and Game Manufacturing: Total Inventories
    'AIES33993INWUS', # Doll, Toy, and Game Manufacturing: Work In Process Inventories
    'AIES33993PAYUS', # Doll, Toy, and Game Manufacturing: Annual Payroll
    'AIES33993PWEUS', # Doll, Toy, and Game Manufacturing: Production Workers
    'AIES33993RCTUS', # Doll, Toy, and Game Manufacturing: Shipments
    'AIES33993TCMUS', # Doll, Toy, and Game Manufacturing: Total Cost of Materials
    ### 33994 Office Supplies (Except Paper) Manufacturing
    'AIES33994EMPUS', # Office Supplies (Except Paper) Manufacturing: Employees
    'AIES33994INFUS', # Office Supplies (Except Paper) Manufacturing: Finished Goods Inventories
    'AIES33994INMUS', # Office Supplies (Except Paper) Manufacturing: Materials and Supplies Inventories
    'AIES33994INVUS', # Office Supplies (Except Paper) Manufacturing: Total Inventories
    'AIES33994INWUS', # Office Supplies (Except Paper) Manufacturing: Work In Process Inventories
    'AIES33994PAYUS', # Office Supplies (Except Paper) Manufacturing: Annual Payroll
    'AIES33994PWEUS', # Office Supplies (Except Paper) Manufacturing: Production Workers
    'AIES33994RCTUS', # Office Supplies (Except Paper) Manufacturing: Shipments
    'AIES33994TCMUS', # Office Supplies (Except Paper) Manufacturing: Total Cost of Materials
    ### 33995 Sign Manufacturing
    'AIES33995EMPUS', # Sign Manufacturing: Employees
    'AIES33995INFUS', # Sign Manufacturing: Finished Goods Inventories
    'AIES33995INMUS', # Sign Manufacturing: Materials and Supplies Inventories
    'AIES33995INVUS', # Sign Manufacturing: Total Inventories
    'AIES33995INWUS', # Sign Manufacturing: Work In Process Inventories
    'AIES33995PAYUS', # Sign Manufacturing: Annual Payroll
    'AIES33995PWEUS', # Sign Manufacturing: Production Workers
    'AIES33995RCTUS', # Sign Manufacturing: Shipments
    'AIES33995TCMUS', # Sign Manufacturing: Total Cost of Materials
    ### 33999 All Other Miscellaneous Manufacturing
    'AIES33999EMPUS', # All Other Miscellaneous Manufacturing: Employees
    'AIES33999INFUS', # All Other Miscellaneous Manufacturing: Finished Goods Inventories
    'AIES33999INMUS', # All Other Miscellaneous Manufacturing: Materials and Supplies Inventories
    'AIES33999INVUS', # All Other Miscellaneous Manufacturing: Total Inventories
    'AIES33999INWUS', # All Other Miscellaneous Manufacturing: Work In Process Inventories
    'AIES33999PAYUS', # All Other Miscellaneous Manufacturing: Annual Payroll
    'AIES33999PWEUS', # All Other Miscellaneous Manufacturing: Production Workers
    'AIES33999RCTUS', # All Other Miscellaneous Manufacturing: Shipments
    'AIES33999TCMUS', # All Other Miscellaneous Manufacturing: Total Cost of Materials
    ### 339991 Gasket, Packing, and Sealing Device Manufacturing
    'AIES339991EMPUS', # Gasket, Packing, and Sealing Device Manufacturing: Employees
    'AIES339991INFUS', # Gasket, Packing, and Sealing Device Manufacturing: Finished Goods Inventories
    'AIES339991INMUS', # Gasket, Packing, and Sealing Device Manufacturing: Materials and Supplies Inventories
    'AIES339991INVUS', # Gasket, Packing, and Sealing Device Manufacturing: Total Inventories
    'AIES339991INWUS', # Gasket, Packing, and Sealing Device Manufacturing: Work In Process Inventories
    'AIES339991PAYUS', # Gasket, Packing, and Sealing Device Manufacturing: Annual Payroll
    'AIES339991PWEUS', # Gasket, Packing, and Sealing Device Manufacturing: Production Workers
    'AIES339991RCTUS', # Gasket, Packing, and Sealing Device Manufacturing: Shipments
    'AIES339991TCMUS', # Gasket, Packing, and Sealing Device Manufacturing: Total Cost of Materials
    ### 339992 Musical Instrument Manufacturing
    'AIES339992EMPUS', # Musical Instrument Manufacturing: Employees
    'AIES339992INFUS', # Musical Instrument Manufacturing: Finished Goods Inventories
    'AIES339992INMUS', # Musical Instrument Manufacturing: Materials and Supplies Inventories
    'AIES339992INVUS', # Musical Instrument Manufacturing: Total Inventories
    'AIES339992INWUS', # Musical Instrument Manufacturing: Work In Process Inventories
    'AIES339992PAYUS', # Musical Instrument Manufacturing: Annual Payroll
    'AIES339992PWEUS', # Musical Instrument Manufacturing: Production Workers
    'AIES339992RCTUS', # Musical Instrument Manufacturing: Shipments
    'AIES339992TCMUS', # Musical Instrument Manufacturing: Total Cost of Materials
    ### 339993 Fastener, Button, Needle, and Pin Manufacturing
    'AIES339993EMPUS', # Fastener, Button, Needle, and Pin Manufacturing: Employees
    'AIES339993INFUS', # Fastener, Button, Needle, and Pin Manufacturing: Finished Goods Inventories
    'AIES339993INMUS', # Fastener, Button, Needle, and Pin Manufacturing: Materials and Supplies Inventories
    'AIES339993INVUS', # Fastener, Button, Needle, and Pin Manufacturing: Total Inventories
    'AIES339993INWUS', # Fastener, Button, Needle, and Pin Manufacturing: Work In Process Inventories
    'AIES339993PAYUS', # Fastener, Button, Needle, and Pin Manufacturing: Annual Payroll
    'AIES339993PWEUS', # Fastener, Button, Needle, and Pin Manufacturing: Production Workers
    'AIES339993RCTUS', # Fastener, Button, Needle, and Pin Manufacturing: Shipments
    'AIES339993TCMUS', # Fastener, Button, Needle, and Pin Manufacturing: Total Cost of Materials
    ### 339994 Broom, Brush, and Mop Manufacturing
    'AIES339994EMPUS', # Broom, Brush, and Mop Manufacturing: Employees
    'AIES339994INFUS', # Broom, Brush, and Mop Manufacturing: Finished Goods Inventories
    'AIES339994INMUS', # Broom, Brush, and Mop Manufacturing: Materials and Supplies Inventories
    'AIES339994INVUS', # Broom, Brush, and Mop Manufacturing: Total Inventories
    'AIES339994INWUS', # Broom, Brush, and Mop Manufacturing: Work In Process Inventories
    'AIES339994PAYUS', # Broom, Brush, and Mop Manufacturing: Annual Payroll
    'AIES339994PWEUS', # Broom, Brush, and Mop Manufacturing: Production Workers
    'AIES339994RCTUS', # Broom, Brush, and Mop Manufacturing: Shipments
    'AIES339994TCMUS', # Broom, Brush, and Mop Manufacturing: Total Cost of Materials
    ### 339995 Burial Casket Manufacturing
    'AIES339995EMPUS', # Burial Casket Manufacturing: Employees
    'AIES339995INFUS', # Burial Casket Manufacturing: Finished Goods Inventories
    'AIES339995INMUS', # Burial Casket Manufacturing: Materials and Supplies Inventories
    'AIES339995INVUS', # Burial Casket Manufacturing: Total Inventories
    'AIES339995INWUS', # Burial Casket Manufacturing: Work In Process Inventories
    'AIES339995PAYUS', # Burial Casket Manufacturing: Annual Payroll
    'AIES339995PWEUS', # Burial Casket Manufacturing: Production Workers
    'AIES339995RCTUS', # Burial Casket Manufacturing: Shipments
    'AIES339995TCMUS', # Burial Casket Manufacturing: Total Cost of Materials
    ### 339999 All Other Miscellaneous Manufacturing
    'AIES339999EMPUS', # All Other Miscellaneous Manufacturing: Employees
    'AIES339999INFUS', # All Other Miscellaneous Manufacturing: Finished Goods Inventories
    'AIES339999INMUS', # All Other Miscellaneous Manufacturing: Materials and Supplies Inventories
    'AIES339999INVUS', # All Other Miscellaneous Manufacturing: Total Inventories
    'AIES339999INWUS', # All Other Miscellaneous Manufacturing: Work In Process Inventories
    'AIES339999PAYUS', # All Other Miscellaneous Manufacturing: Annual Payroll
    'AIES339999PWEUS', # All Other Miscellaneous Manufacturing: Production Workers
    'AIES339999RCTUS', # All Other Miscellaneous Manufacturing: Shipments
    'AIES339999TCMUS', # All Other Miscellaneous Manufacturing: Total Cost of Materials
]
