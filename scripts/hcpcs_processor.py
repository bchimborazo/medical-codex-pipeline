import pandas as pd

# Define the path to the input file
file_path = "input/HCPC2025_OCT_ANWEB_v2.txt"

# Guess of colspecs column widths
colspecs = [(0, 11), (11, 90)]

# Defining column names
column_names = ["code", "description"]

# Read the fixed-width formatted file and create a dataframe
df = pd.read_fwf(file_path, colspecs=colspecs, names=column_names)

# Clean the 'code' and 'description' columns by removing leading/trailing whitespace
df['code'] = df['code'].str.strip()
df['description'] = df['description'].str.strip()

# Add a 'last_updated' column with today's date in YYYY-MM-DD format
today_date = "2025-09-11"
df['last_updated'] = today_date

# Define the output file path for the processed CSV
output_path = "output/csv/hcpcs_codes.csv"
# Save the dataframe to a CSV file without the index
df.to_csv(output_path, index=False)