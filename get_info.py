import fred_getter
from mySeriesIds import us_macro_ids_Q, us_macro_ids_M, us_macro_ids_W, us_macro_ids_D

###################
# INPUT VARIABLES #
###################

# series_ids = ['M1SL', 'M2SL']
# series_ids = ['CURRCIR']
series_ids = ['DPSACBM027NBOG']

tickers = ['date']
names = ['date']

for i, series_id in enumerate(series_ids):
    result = fred_getter.getSeriesInfo(series_id)
    print('>>>> {} '.format(series_id))
    print('')
    print('-- title : {}'.format(result['seriess'][0]['title']))
    print('-- frequency : {}'.format(result['seriess'][0]['frequency']))
    print('-- period : {} ~ {}'.format(result['seriess'][0]['observation_start'],
                                       result['seriess'][0]['observation_end']))
    print('-- last updated : {}'.format(result['seriess'][0]['last_updated']))
    result = fred_getter.getCategoryBySeriesId(series_id)
    print('-- category : {} ({})'.format(result['categories'][0]['name'], result['categories'][0]['id']))
    print('')
    print('')