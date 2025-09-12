import pandas as pd

# Define the file path to the input data
file_path = "input/icd102019syst_codes.txt"

# Define all column names as per the dataset structure
columns = ['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code', 
           'icd10_code', 'title_en', 'parent_title', 'detailed_title', 
           'definition', 'mortality_code', 'morbidity_code1', 'morbidity_code2',
           'morbidity_code3', 'morbidity_code4']

# Read the dataset into a DataFrame
# The dataset is semicolon-separated and has no header row
df = pd.read_csv(file_path, sep=';', header=None, names=columns)

# Create a new DataFrame to hold the required columns
new_df = pd.DataFrame()
# Map the relevant columns to the new DataFrame
new_df['code'] = df['icd10_code']
new_df['description'] = df['title_en']
# Add a timestamp column with a fixed date
new_df['last_updated'] = "2025-09-11"
# Export the new DataFrame to a CSV file without the index 
new_df.to_csv("output/csv/icd10WHO_codes.csv", index=False)