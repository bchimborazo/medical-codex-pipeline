import polars as pl
from pathlib import Path

# Define the path to the RXNATOMARCHIVE.RRF file
file_path = Path('input/RXNATOMARCHIVE.RRF')

# Column names
columns = [
    'rxaui', 'aui', 'str', 'archive_timestamp', 'created_timestamp', 
    'updated_timestamp', 'code', 'is_brand', 'lat', 'last_released', 
    'saui', 'vsab', 'rxcui', 'sab', 'tty', 'merged_to_rxcui'
]
# Read the file using Polars, specifying the delimiter and column names
# No header in the file, so we set has_header=False
df = pl.read_csv(
    file_path,
    separator='|',
    has_header=False,
    new_columns=columns,
    truncate_ragged_lines=True
)
# Create new DataFrame with the specified columns
df_final = df.select([
    pl.col('code'),
    pl.col('str').alias('description')
]).with_columns(
    # Add new column with the date
    pl.lit('2025-09-11').alias('last_updated')
)
# Ensure the output directory exists
output_dir = Path('output/csv')
output_dir.mkdir(exist_ok=True)
output_path = output_dir / 'RXNATOMARCHIVE_final.csv'

df_final.write_csv(output_path)

print(f"Successfully parsed {len(df)} records from RXNATOMARCHIVE.RRF")
print(f"Final dataset contains {len(df_final)} records with 3 columns: code, description, last_updated")
print(f"Saved to {output_path}")
print(f"Final dataset shape: {df_final.shape}")
print(f"\nFirst 5 rows:")
print(df_final.head())
print(f"\nMemory usage (MB): {df_final.estimated_size() / 1024**2:.2f}")