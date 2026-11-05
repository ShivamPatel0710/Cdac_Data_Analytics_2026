import pandas as pd
df_titanic = pd.read_csv(r"C:\Learning\Data Analytics CDAC\Day2\01_pre_req\pandas\supportfiles\titanic.csv")
print("Loaded Titanic CSV Shape",df_titanic.shape)

print(df_titanic.head(3))

print("="*60)

# Export DataFrame to Excel spreadsheet
df_titanic.to_excel(
    r"C:\Learning\Data Analytics CDAC\Day2\01_pre_req\pandas\supportfiles\titanic.xlsx",
    sheet_name="passengers",
    index=False
)

df_titanic_excel = pd.read_excel(r'Day2/01_pre_req/pandas/supportfiles/titanic.xlsx',sheet_name="passengers")
print("Reloaded Excel Passenger Shape",df_titanic_excel.shape)