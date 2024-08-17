import pandas as pd
a={"sas":pd.Series([1,2,3,4]),"pas":pd.Series([8,9,2,6])}
e=pd.DataFrame(a)
e["c"]=e["sas"]+e["pas"]
print(e)