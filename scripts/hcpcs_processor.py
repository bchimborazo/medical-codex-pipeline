import pandas as pd

file_path = "input/HCPC2025_OCT_ANWEB_v2.txt"

colspecs = [(0,11), (11,90)]
columns_names = ["code", "description"]

df = pd.read_fwf(file_path, colspecs=colspecs, names=columns_names)
df['code'] = df['code'].str.strip()
df['description'] = df['description'].str.strip()

today_date = "2025-09-07"
df['last_updated'] = today_date

df = df[['code', 'description', 'last_updated']]

output_path = "output/hcpcs_2025.csv"
df.to_csv(output_path, index=False)