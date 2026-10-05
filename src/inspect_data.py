import pandas as pd

file_path = "data/raw/online_retail_II.xlsx"

df = pd.read_excel(file_path)

print(df.columns)
print(df.dtypes)