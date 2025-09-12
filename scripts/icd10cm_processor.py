import pandas as pd
import re

# Define the path to the input file
file_path = "input/icd10cm_order_2025.txt"

# Initialize a list to hold the codes and descriptions
codes = []

# Open and read the input file line by line with UTF-8 encoding
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # Remove trailing newline and carriage return characters
        line = line.rstrip('\n\r')
        # Skip lines that are too short to contain valid data (less than 15 characters)
        if len(line) < 15:
            continue
        # Parses code from fixed-length format
        code = line[6:13].strip()

        # Parse description from the remaining text
        remaining_text = line[16:]

        # Split by 4+ consecutive spaces to separate description from description_detailed
        parts = re.split(r'\s{4,}', remaining_text, maxsplit=1)
        description = parts[0].strip() if len(parts) > 0 else ""

        # Append the parsed data to the codes list
        codes.append({
            'code': code,
            'description': description,
            'last_updated': '2025-09-12'
        })
## Create a DataFrame from the parsed codes
icdcodes = pd.DataFrame(codes)

## Save the DataFrame to a CSV file
icdcodes.to_csv("output/csv/icd10cm_order_2025.csv", index=False)