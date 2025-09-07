import pandas as pd
df = pd.read_csv('input/Loinc.csv')
df.info()

df.LOINC_NUM
df.LONG_COMMON_NAME
df_small = df[['LOINC_NUM', 'LONG_COMMON_NAME']]

df_small

df_small['last_updated'] = '2025-09-06' 

df_small

df_small = df_small.rename(columns={'LOINC_NUM': 'code', 'LONG_COMMON_NAME': 'description'})
df_small
df_small.to_csv('output/csv/loinc_processed.csv', index=False)
