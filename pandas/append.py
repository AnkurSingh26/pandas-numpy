import pandas as pd

# Initial DataFrame 'A'
a = {'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 1]}
A = pd.DataFrame(a)

# Another DataFrame 'e'
a_new = {"sas": pd.Series([1, 2, 3, 4]), "pas": pd.Series([8, 9, 2, 6])}
e = pd.DataFrame(a_new)

# Use pd.concat instead of append
result = pd.concat([e, A])
A.to_csv("aishehi.csv")


print(result)
