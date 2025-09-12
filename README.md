# HHA 507: medical-codex-pipeline
Goal: Create Python scripts that can process the medical codexes listed below into standardized CSV format.
Please refer to assignment instructions here: https://github.com/hantswilliams/HHA-507-2025/blob/main/assignments/assignment1_medicalcodexes.md

## Targeted Medical Codexes
| Codex | Focus | Links |
|--------|---------|-------|
| SNOMED CT (US) | Clinical Terminology | https://www.nlm.nih.gov/healthit/snomedct/archive.html |
| ICD-10-CM (US)| Diagnosis Codes | https://www.cms.gov/medicare/coding-billing/icd-10-codes |
| ICD-10 (WHO) | International Diagnosis Codes| https://icdcdn.who.int/icd10/index.html |
| HCPCS (US) | Healthcare Procedure Codes | https://www.cms.gov/medicare/coding-billing/healthcare-common-procedure-system/quarterly-update |
| LOINC (US) | Laboratory Test Codes| https://loinc.org/downloads/ |
| RxNorm (US) | Medication Codes| https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html |
| NPI (US) | Healthcare Provider Identifiers | https://download.cms.gov/nppes/NPI_Files.html |




## Data Cleaning/Manipulation/Standardization per Script
This section documents some of the data cleaning and manipulation techniques applied to each of the seven medical codex files. For detailed code explanations, refer to the comments within each script file in the "scripts" folder. 

### HCPCS
- I used '.str.strip()' to remove leading and trailing whitespace from the 'code' and 'description' columns 

### ICD10 (US)
- I removed trailing newline and carriage return characters by using: '.rstrip('\n\r')'

- I filtered out invalid records by skipping lines shorter than 15 characters by using: if len(line) < 15: continue

- **code = line[6:13].strip()** slices the string to extract the code and strips extra whitespace

- **description = parts[0].strip() if len(parts) > 0 else ""** this trims whitespace from the description 

- **parts = re.split(r'\s{4,}', remaining text, maxsplit=1)** splits the remaining text into fields on 4+ spaces

### ICD10 (WHO)
- **sep=';'** specifies the delimiter ";" which helps with column naming since this file has no headers

- **new_df['code'] = df['icd10_code'] and new_df['description'] = df['title_en']** These functions select only the specified columns for the new data set

### LOINC
This is the first script I worked on, it served as a guide for all of the other files. The main data manipulation that was done in this file was
selecting the desired working columns by **using df_small = df[['LOINC_NUM', 'LONG_COMMON_NAME']]**. With this file I learned to create a file path and save the final 
dataframe to CSV without indices by using **index=False**.

### NPI
- Limited dataset size by reading only the first 100,000 rows by using **n_rows**

- When I made the first version of this csv, there were several empty fields in the file. I used **.drop_nulls() and .filter()** to remove empty fields and clean the data so that the final csv would be free of empty fields

- **.filter((pl.col('NPI').str.strip_chars() != '')** & **(pl.col('Provider Last Name (Legal Name)').str.strip_chars() != ''))** removes rows where the values
are empty strings

### RxNorm
- **pl.read_csv(..., separator='|', has_header=False, new_columns=columns, truncate_ragged_lines=True)** ensures correct parsing of pipe delimited files, handles files with
no header row and validates/corrects rows with inconsistent column counts (truncates extras)

### SNOMED
- I iltered dataset to include only active records by using **processed_df = df.filter(pl.col('active') == 1)**
- Used lossy UTF-8 for character encoding 
- Handled malformed records with truncate-ragged_lines option
- **.head(100_000)** limits dataset to the first 100,000 rows for better output size

