import pandas as pd
import numpy as np
df_indexed = pd.read_csv(r"C:\Learning\Data Analytics CDAC\Day2\01_pre_req\pandas\supportfiles\drinks.csv",index_col="country")
print("Custom Country Index Preview:\n",df_indexed.head(5))

# look at ram footprint
mem_original = df_indexed.memory_usage().sum()
print("Original dataframe usage in bytes :",mem_original)
mem_original_element_level = df_indexed.memory_usage(deep=True).sum()
print("Original  deep Memory Usage :",mem_original_element_level)

print("+"*60)
print(df_indexed.info())
print("="*60)
print("{0:<35}{1:<15}{2:<15}{3:<15}{4:<15}".format("Column Name","Min","Max","Type","Can Hold"))
for col in df_indexed.select_dtypes(include=[np.number]).columns: # selects only numeric columns other method will be in place of np.number we write datatypes in a list 
    dt = df_indexed[col].dtype
    max_can_hold = np.iinfo(dt).max if np.issubdtype(dt,np.integer) else np.finfo(dt).max
    print("{0:<35}{1:<15}{2:<15}{3:<15}{4:<15}".format(col.capitalize(),
                                                df_indexed[col].min(),
                                                df_indexed[col].max(),
                                                df_indexed[col].dtype.__str__(),
                                                max_can_hold))
print("="*60)

# downcasting

df_optimized = df_indexed.copy()
for col in df_optimized.select_dtypes(include=[np.number]).columns:
    dt = df_optimized[col].dtype
    cast_to_str = "integer" if np.issubdtype(dt,np.integer) else "float"
    df_optimized[col] = pd.to_numeric(df_optimized[col],downcast=cast_to_str)
print("+"*60)

print(df_optimized.info())
print("+"*60)

mem_original = df_optimized.memory_usage().sum()
print("Original dataframe usage in bytes :",mem_original)
mem_original_element_level = df_optimized.memory_usage(deep=True).sum()
print("Original  deep Memory Usage :",mem_original_element_level)
