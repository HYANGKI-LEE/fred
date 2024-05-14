import ssl
import time
import requests
import warnings
import pandas as pd
from datetime import datetime

from config import user_agent, myAPIkey
import fred_getter

def runner(series_ids, save_dir, file_name):
    tickers = ['date']
    names = ['date']
    df = pd.DataFrame()

    for i, series_id in enumerate(series_ids):
        print(">>> {}. {}".format(i, series_id))
        result1 = fred_getter.getSeriesInfo(series_id)
        tickers.append(result1['seriess'][0]['id'])
        names.append(result1['seriess'][0]['title'])
        result2 = fred_getter.getObservations(series_id)
        df_tmp = pd.DataFrame(result2['observations'])[['date', 'value']].rename(columns={'value': i})
        try:
            df = pd.merge(df, df_tmp, left_on='date', right_on='date', how='outer')
        except:
            df = df_tmp
        if ((i // 20) > 1)  and (i % 20 == 0):
            time.sleep(20)

    df = df.sort_values(by=['date'], ascending=True).reset_index(drop=True)
    df.columns = [tickers, names]
    df.to_csv('{}/{}_{}.csv'.format(save_dir, file_name, datetime.today().strftime('%Y%m%d')))