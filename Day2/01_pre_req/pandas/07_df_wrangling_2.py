'''
missing values

1. Identify
2. Drop
3. Impute
'''

import pandas as pd
import numpy as np

df_titanic = pd.read_csv(r"C:\Learning\Data Analytics CDAC\Day2\01_pre_req\pandas\supportfiles\titanic.csv")
print(df_titanic.head())

print("="*60)
print("Missing Values count per column")
print(df_titanic.isnull().sum())
print("="*60)
median_age = df_titanic["Age"].median()
df_titanic["Age_Imputed"] = df_titanic["Age"].fillna(median_age)  # here we take median because it is not sensitive to outliers or extreme values
df_titanic["Cabin_Filled"] = df_titanic["Cabin"].fillna("Unknown")
print("After Age Imputation ",df_titanic["Age_Imputed"].isna().sum())
print("After Cabin Imputation ",df_titanic["Cabin"].isna().sum())
print("="*60)
print(df_titanic.head()[["Age","Age_Imputed","Cabin","Cabin_Filled"]])
df_titanic_cleaned = df_titanic.copy()
# df_titanic_cleaned["Age"] = df_titanic_cleaned["Age_Imputed"]
# df_titanic_cleaned["Cabin"] = df_titanic_cleaned["Cabin_Filled"]
# df_titanic_cleaned[["Age","Cabin"]] = df_titanic_cleaned[["Age_Imputed","Cabin_Filled"]]
df_titanic_cleaned = df_titanic_cleaned.assign(
    Age = df_titanic_cleaned["Age_Imputed"],
    Cabin = df_titanic_cleaned["Cabin_Filled"]
 )
print(df_titanic_cleaned.isna().sum())
df_titanic_cleaned = df_titanic_cleaned.drop(columns=["Age_Imputed","Cabin_Filled"])
print("="*60)
print(df_titanic_cleaned.isna().sum())
print("="*60)
print(df_titanic_cleaned["Embarked"].value_counts())
'''
Embarked
s 644 Sothampton (England)
c 168 Cherburg (France) - The First
q 77 Queenstown
'''
# most_used = df_titanic_cleaned["Embarked"].mode()
df_titanic_cleaned["Embarked"] = df_titanic_cleaned["Embarked"].fillna(df_titanic_cleaned["Embarked"].mode()[0])
print(df_titanic_cleaned.isna().sum())
print("="*60)
print("="*60)