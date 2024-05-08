import fred_getter

###################
# INPUT VARIABLES #
###################

# series_ids = ['M1SL', 'M2SL']
# series_ids = ['CURRCIR']
series_ids = [
    'PAYEMS'
    ]

tickers = ['date']
names = ['date']

for i, series_id in enumerate(series_ids):
    result = fred_getter.getSeriesInfo(series_id)
    print('')
    print('>>>> {} '.format(series_id))
    print('')
    print('-- title : {}'.format(result['seriess'][0]['title']))
    print('-- frequency : {}'.format(result['seriess'][0]['frequency']))
    print('-- period : {} ~ {}'.format(result['seriess'][0]['observation_start'],
                                       result['seriess'][0]['observation_end']))
    print('-- last updated : {}'.format(result['seriess'][0]['last_updated']))
    print('-- units : {}'.format(result['seriess'][0]['units']))
    result = fred_getter.getCategoryBySeriesId(series_id)
    print('-- category : {} ({})'.format(result['categories'][0]['name'], result['categories'][0]['id']))
    # category_id_=result['categories'][0]['id']
    # result = fred_getter.getRelatedCategoriesByCategoryId(category_id=category_id_)
    print(result)
    print('')
    print('')