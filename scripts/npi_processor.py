import polars as pl
import time

file_path = "input/npidata_pfile_20050523-20250810.csv"
df_polars = pl.read_csv(file_path, n_rows=1000000)

print("Columns in the file:")
print(list(df_polars.columns))

df_polars_small = df_polars.select([
    'NPI',
    'Provider Last Name (Legal Name)'
])

df_polars_small = df_polars_small.with_columns(
    pl.lit('2025-09-09').alias('last_updated')
)
df_polars_small = df_polars_small.rename({
    'NPI': 'code',
    'Provider Last Name (Legal Name)': 'description',
    'last_updated': 'last_updated'
})
df_polars_small.write_csv("output/csv/npi_polars_small.csv")
df_polars_small.write_parquet("output/csv/npi_polars_small.parquet") 