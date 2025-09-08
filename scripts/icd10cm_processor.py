import pandas as pd
import re

file_path = "input/icd10cm_order_2025.txt"
codes = []
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.rstrip('\n\r')
        if len(line) < 15:
            continue
        code = line[6:13].strip()
        description = line[16:].strip()
        codes.append((code, description))

df = pd.DataFrame(codes, columns=['code', 'description'])
df['last_updated'] = "2025-09-07"

df.to_csv("output/icd10cm_2025.csv", index=False)