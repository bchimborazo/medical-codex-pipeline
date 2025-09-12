import polars as pl

# Define the file path
file_path = "input/npidata_pfile_20050523-20250810.csv"
# Read the CSV file using Polars with a limited number of rows
df_polars = pl.read_csv(file_path, n_rows=100_000)

# Display columns for reference
print("Columns in the file:")
print(list(df_polars.columns))

# Select the required columns from the full dataset
# Extracts NPI and Provider Last Name (Legal Name) for processing
df_polars_small = df_polars.select([
    'NPI',
    'Provider Last Name (Legal Name)'
])

# Remove rows which are null or empty
df_polars_small = (
    df_polars_small
    .with_columns([
        pl.col('NPI').cast(pl.Utf8),
        pl.col('Provider Last Name (Legal Name)').cast(pl.Utf8)
    ])
    .drop_nulls()
    .filter(
        (pl.col('NPI').str.strip_chars() != '') &
        (pl.col('Provider Last Name (Legal Name)').str.strip_chars() != '')
    )
)

# Add a timestamp column with a fixed date
df_polars_small = df_polars_small.with_columns(
    pl.lit('2025-09-12').alias('last_updated')
)

# Rename columns to match desired output format
df_polars_small = df_polars_small.rename({
    'NPI': 'code',
    'Provider Last Name (Legal Name)': 'description',
})
# Export the processed DataFrame to CSV and Parquet without the index
print("Processed DataFrame:")
df_polars_small.write_csv("output/csv/npi_polars_small.csv")
df_polars_small.write_parquet("output/csv/npi_polars_small.parquet") 