# HHA 507: medical-codex-pipeline
Goal: Create Python scripts that can process the medical codexes listed below into standardized CSV format.

## Targeted Medical Codexes
| Codex | Focus |
|--------|---------|
| SNOWMED CT (US) | Clinical Terminology |
| ICD-10-CM (US)| Diagnosis Codes |
| ICD-10 (WHO) | International Diagnosis Codes|
| HCPCS (US) | Healthcare Procedure Codes |
| LOINC (US) | Laboratory Test Codes|
| RxNorm (US) | Medication Codes|
| NPI (US) | Healthcare Provider Identifiers |


## Data Cleaning/Manipulation/Standardization per Script
This section documents some of the data cleaning and manipulation techniques applied to all seven medical codexes files. For detailed code explanations, refer to the comments within each script file in the "scripts" folder. 

### HCPCS
- **Whitespace removal**: Used '.str.strip()' to remove leading and trailing whitespace from the 'code' and 'description' columns 

### ICD10 (US)
**Line processing**: Removes trailing newline and carriage return characters by using: '.rstrip('\n\)r')'
**Data validation**: Filtered out invalid records by skipping lines shorter than 15 characters by using: if len(line) < 15: continue
**Data cleaning**: code = line[6:13].strip() slices the string to extract the code and strips extra whitespace
description = parts[0].strip() if len(parts) > 0 else "" this trims whitespace from the description 
**Data manipulation**: parts = re.split(r'\s{4,}', remaining text, maxsplit=1) splits the remaining text into fields on 4+ spaces

### ICD10 (WHO)
**Data structuring**: sep=';' specifies the delimiter ; which helps with column naming since this file has no headers
new_df['code'] = df['icd10_code'] and new_df['description'] = df['title_en'], these functions select only the specified columns for the new data set

### LOINC
This is the first script I worked on, it served as a guide for all of the other files. The main data manipulation that was done in this file was
selecting the desired working columns by using df_small = df[['LOINC_NUM', 'LONG_COMMON_NAME']]. With this file I learned to save the final 
dataframe to csv wthout indices by using index=False

### NPI
**Data sampling**: limited dataset size by reading only the first 1000,000 rows by using n_rows
.filter((pl.col('NPI').str.strip_chars() != '') & (pl.col('Provider Last Name (Legal Name)').str.strip_chars() != '')) this removes rows where values
are empty strings

### RxNorm
**Data cleaning**: pl.read_csv(..., separator='|', has_header=False, new_columns=columns, truncate_ragged_lines=True) this ensures correct parsing of pipe delimited files, handles 
no header row, validates/corrects rows with insocnsistent column counts (truncates extras)

### SnowMed
**Data filtering**: filtered dataset to include only active records by using processed_df = df.filter(pl.col('active') == 1)
**Encoding handling**: used lossy UTF-8 for character encoding 
**Data cleaning**: handled malformed records with truncate-ragged_lines option
**Data sampling**: .head(100_00) limits dataset to the first 100,000 rows for better size output

