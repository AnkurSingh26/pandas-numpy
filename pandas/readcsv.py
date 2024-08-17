import pandas as pd
csv1=pd.read_csv("test.csv",usecols=[0,2])

print(csv1)
csv2=pd.read_csv("test.csv",header=2)
print(csv2)
csv3 = pd.read_csv("D:\\pandas-numpy\\Diabetes Missing Data.csv")
print(csv3)
df_cleaned = csv3.dropna(subset=["Skin_Fold"])
df_cleaned.to_csv('cleaned_file.csv')

print(df_cleaned)
df_cleaned = csv3.dropna()

print(df_cleaned)
del df_cleaned['Skin_Fold']
print(df_cleaned)
