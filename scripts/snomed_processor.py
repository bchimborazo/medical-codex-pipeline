import polars as pl
from pathlib import Path

# file path
file_path = Path('input/sct2_Description_Full-en_US1000124_20250301.txt')

# read the tab delimited file
df = pl.read_csv(
    file_path,
    separator='\t', # tab delimited
    has_header=True, # file has header
    quote_char=None, # no quote character
    encoding='utf8-lossy', # handle encoding issues
    truncate_ragged_lines=True, # truncate lines that are too long
    dtypes={ # specify data types for columns
        'id': pl.Utf8, # string
        'effectiveTime': pl.Utf8, # string
        'active': pl.Int32, # integer
        'moduleId': pl.Utf8, # string
        'conceptId': pl.Utf8, 
        'languageCode': pl.Utf8,
        'typeId': pl.Utf8, 
        'term': pl.Utf8, 
        'caseSignificanceId': pl.Utf8
    }
)

# create a new data frame with only the required columns
# filter for active records only
processed_df = (
    df.filter(pl.col('active') == 1).select([
    pl.col('id').alias('code'),
    pl.col('term').alias('description'),
]).with_columns([
    # Add timestamp column
    pl.lit("2025-09-11").alias("last_updated")
])
.head(100_000) # limit to first 100,000 rows to reduce file size for better output
)
# Create output directory if it doesn't exist
output_dir = Path('output/csv')
output_dir.mkdir(exist_ok=True)
# Define output file path
output_path = output_dir / 'snowmed.final.csv'

processed_df.write_csv(output_path)