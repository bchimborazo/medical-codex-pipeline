import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('input/Loinc.csv')

# Display basic information about the DataFrame to understand its structure
df.info()

# Inspect the LOINC_NUM and LONG_COMMON_NAME columns
df.LOINC_NUM
df.LONG_COMMON_NAME

# Create a subset DataFrame with only the needed columns for output
df_small = df[['LOINC_NUM', 'LONG_COMMON_NAME']]

# Inspect the new DataFrame
df_small

# Add a last_updated column with a fixed date
df_small['last_updated'] = '2025-09-11' 

# Inspect the updated DataFrame
df_small

# Rename columns to match desired output format
df_small = df_small.rename(columns={'LOINC_NUM': 'code', 'LONG_COMMON_NAME': 'description'})
# Inspect the renamed columns
df_small
# Export the processed DataFrame to a CSV without the index
df_small.to_csv('output/csv/loinc_processed.csv', index=False)
