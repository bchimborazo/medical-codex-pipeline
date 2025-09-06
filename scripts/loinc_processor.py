import pandas as pd
df = pd.read_csv('input/Loinc.csv')
df.info()

df.LOINC_NUM
df.DefinitionDescription

df_small = df[['LOINC_NUM', 'DefinitionDescription']]

df_small

df_small['last_updated'] = '2025-09-06' 

df_small

df_small = df_small.rename(columns={'LOINC_NUM': 'Code', 'DefinitionDescription': 'Description'})
df_small
df_small.to_csv('output/csv/loinc_processed.csv', index=False)
