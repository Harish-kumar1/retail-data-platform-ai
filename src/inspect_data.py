import pandas as pd

file_path = "data/raw/online_retail_II.xlsx"

df = pd.read_excel(file_path)

#Getting to know the types of values  in this data
print(df.columns)
print(df.dtypes)

#Displaying a bit of sample to data so as to have an idea
#print(df.head(20))

#Checking if descriptions are unique to each stockcode
df_grouped = df.groupby("StockCode")
df_stockade_analysis = df_grouped["Description"].nunique()

print(df_stockade_analysis)