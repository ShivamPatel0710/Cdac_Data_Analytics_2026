import pandas as pd
import numpy as np

df_drinks = pd.read_csv(r'C:\Learning\Data Analytics CDAC\Day2\01_pre_req\pandas\supportfiles\drinks.csv')
print(df_drinks.head())
print("="*60)

# split apply combine workflow
continent_stats = df_drinks.groupby("continent").agg(
    avg_beer = ("beer_servings",'mean'),
    max_wine = ("wine_servings",'max'),
    total_pure_alcohol = ("total_litres_of_pure_alcohol",'sum'),
    country_count = ("country",'count')
)


print("======Continent Drink Aggregation========")
print(continent_stats)

continent_stats_2 = df_drinks.groupby("continent").agg({
    'beer_servings' : ['mean','max','std'], 
    'wine_servings': ['sum'],
    'country': ['count']
})

print("======Continent Drink Aggregation 2========")
print(continent_stats_2)