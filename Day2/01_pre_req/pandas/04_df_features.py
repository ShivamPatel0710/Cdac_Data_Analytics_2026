import pandas as pd

df_drinks = pd.read_csv(r"C:\Learning\Data Analytics CDAC\Day2\01_pre_req\pandas\supportfiles\drinks.csv")
print(df_drinks.head(3))
print("="*60)
print("+"*60)
print("Index Objects")
print(df_drinks.index)
print("="*60)
print("Column names")
print(df_drinks.columns)
print("="*60)
print("Datatypes of columns")
print(df_drinks.dtypes)
print("="*60)
print("Underlying shapes and axes")
print("Shape",df_drinks.shape)
print("Axes",df_drinks.axes)
print("="*60)
print("Concise schema Summary")
print(df_drinks.info())
print("="*60)
print(df_drinks.describe())

print(df_drinks.describe().T[["mean","std","min","max"]])
print("="*60)
df_subset = df_drinks[["country","total_litres_of_pure_alcohol","continent"]].copy() # all columns names should be in list and a copy is made so that this do not disturb the original dataset
print(df_subset.head(3))
print("="*60)

df_subset["status"] = "Evaluated" # adding new columns and currentlt all its rows are filled with evaluated
print(df_subset.head())
print("="*60)

df_subset.insert(1,"region_category",value="Standard Market") # inserting at a specific index
print(df_subset.head())
print("="*60)

df_subset["boosted_litres"] = df_subset["total_litres_of_pure_alcohol"].add(2.5)
print(df_subset.head())
print("="*60)


