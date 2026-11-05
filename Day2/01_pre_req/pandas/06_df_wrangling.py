'''
what is wrangling
discovering
structuring
cleaning
enriching
validating
publishing
'''

import pandas as pd
import numpy as np

df_drinks = pd.read_csv(r'C:\Learning\Data Analytics CDAC\Day2\01_pre_req\pandas\supportfiles\drinks.csv')
print(df_drinks.head())
print("="*60)
print(df_drinks.sort_values(by="spirit_servings",ascending=False).head()[["country","spirit_servings"]])

print("="*60)
print(df_drinks["continent"].value_counts())
print("="*60)
print("=====High Spirit Consumption(>200)(European Countries)===")
print("="*60)
mask_europe = (df_drinks["continent"] == "Europe") & (df_drinks["spirit_servings"] > 200)
df_high_spirit_eu = df_drinks[mask_europe]
print(df_high_spirit_eu[["country","spirit_servings","continent"]])
print("="*60)

print("====Asia and Africa ====")
mask_asia_africa = (df_drinks["continent"]=="Africa") | (df_drinks["continent"]=="Asia") # or (df_drinks["continent"].isin(["Asia","Africa"]))
df_high_spirit_asia_africa = df_drinks[mask_asia_africa]
print(df_high_spirit_asia_africa[["country","continent","spirit_servings"]])
print("Shape :",df_high_spirit_asia_africa.shape)
print(df_high_spirit_asia_africa["continent"].value_counts()) # for finding no of asian and frican countries and we use continent as parameter
print("="*60)