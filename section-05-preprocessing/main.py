from tabulate import tabulate
import pandas as pd
raw_csv_data = pd.read_csv("Absenteeism_data.csv")
# print(raw_csv_data)
print(f"Keys: {raw_csv_data.keys()}")

# copy the dataframe
df = raw_csv_data.copy()

# apply dataframe view settings
pd.options.display.max_columns = None
pd.options.display.max_rows = None
print(tabulate(df, headers="keys", tablefmt="psql"))

# # print info on dataframe
# df.info()