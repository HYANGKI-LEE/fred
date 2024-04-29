import pandas as pd
from pprint import pprint
from util import make_dir
import fred_getter

###################
# INPUT VARIABLES #
###################
category_id = '33078'

####################################



dir_name = 'seriesIds'

output_dir = './output'
make_dir(output_dir)

save_dir = '{}/{}'.format(output_dir, dir_name)
make_dir(save_dir)
result1=fred_getter.getCategoryByCategoryId(category_id=category_id)
category_name=result1['categories'][0]['name']
result2=fred_getter.getSereisIds(category_id=category_id)
pprint(result2)
print('>>>> {} : Total {} series'.format(category_name, result2['count']))
df=pd.DataFrame(result2['seriess'])
del df['realtime_start'], df['realtime_end']

df.to_csv('{}/Category_id_{}({}).csv'.format(save_dir, category_id, category_name))