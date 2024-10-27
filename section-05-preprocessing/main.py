from tabulate import tabulate
import pandas as pd
raw_csv_data = pd.read_csv("Absenteeism_data.csv")
# print(raw_csv_data)
print(f"Keys: {raw_csv_data.keys()}")

# copy the dataframe
# good practice: changes you made 
df = raw_csv_data.copy()

# apply dataframe view settings
pd.options.display.max_columns = None
pd.options.display.max_rows = None
row_num = 30
df_shot = df.iloc[0:row_num]
print(tabulate(df_shot, headers="keys", tablefmt="pretty"))

# # print info on dataframe
# df.info()
