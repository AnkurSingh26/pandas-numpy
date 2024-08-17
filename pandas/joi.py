import pandas as pd

# Initial DataFrame 'A'
a = {'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 1]}
A = pd.DataFrame(a)

# Another DataFrame 'e'
a_new = {"sas": pd.Series([1, 2, 3, 4]), "pas": pd.Series([8, 9, 2, 6])}
e = pd.DataFrame(a_new)

# Joining DataFrame 'e' with itself, specifying suffixes
b = e.join(e, how="outer", lsuffix='_left', rsuffix='_right')

print(b)

