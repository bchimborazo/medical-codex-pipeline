import pandas as pd
file_path = "input\npidata_pfile_20050523-20250810.csv"
#loading the first 5 rows to be able to see the column names
df = pd.read_csv(file_path, nrows=5)
print("Column names:")
for i, col in enumerate(df.columns):
    print(f"{i}: '{col}'")

print("\nFirst 5 rows:")
print(df.head())