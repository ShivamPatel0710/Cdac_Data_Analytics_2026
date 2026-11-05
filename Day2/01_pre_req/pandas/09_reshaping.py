import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

cricket_stats = {
    "cricketers" : [
        "Sachin Tendulkar","Virat Kohli","Ricky Ponting",
        "Kumar Sangakkra","jacques Kallis", "Hasim Amla",
        "Mahendra Singh Dhoni", "Joe Root", "Kale Williamson","Steve Smith"
    ],
    "fifties" : [164,220,146,153,149,88,108,105,96,78],
    "hunderds" : [100,80,71,63,62,55,16,49,45,44]
}


df_cricket = pd.DataFrame(cricket_stats)
print(df_cricket)
print("="*60)

# unpivot the dataframe
df_long = df_cricket.melt(id_vars="cricketers",var_name="Score Type",value_name="Count")
print(df_long)

#visualization
# render grouped bar plot via seaborn

plt.figure(figsize=(10,5))
sns.barplot(x="cricketers",y="Count",hue = "Score Type",data = df_long)
plt.legend(title="Score Type")
plt.xticks(rotation=45,ha='right')
plt.xlabel("Cricketers")
plt.ylabel("Score Count")
plt.title("International Cricket Performance : Fifties vs Hunderds")
plt.tight_layout()
plt.show()