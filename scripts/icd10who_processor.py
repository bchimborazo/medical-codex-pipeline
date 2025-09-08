import pandas as pd
file_path = "input/icd102019syst_codes.txt"

columns = ['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code', 'icd10_code', 'title.en', 'parent_title', 'detailed_title', 'definition', 'mortality_code', 'morbidity_code1', 'morbidity_code2', 'morbidity_code3', 'morbidity_code4']
df = pd.read_csv(file_path, sep=';', header=None, names=columns)

new_df = pd.DataFrame()
new_df['code'] = df['icd10_code']
new_df['description'] = df['title.en']
new_df['last_updated'] = "2025-09-07"

new_df.to_csv("output/icd10WHO_codes.csv", index=False)