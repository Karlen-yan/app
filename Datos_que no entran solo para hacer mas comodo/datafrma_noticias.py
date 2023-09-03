# import pandas as pd
# import json
# from pandas import json_normalize
import pandas as pd

import csv

# leemos el archivo json 
df = pd.read_csv( 'informacion_ob.csv', encoding= 'unicode_escape')


# df = df.drop(columns=["Cap"]) 

df = df.drop_duplicates(keep=False, inplace=False)


print(df.head())