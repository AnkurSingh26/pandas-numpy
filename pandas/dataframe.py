import pandas as pd
d={"name":["as","ps","ds"],"roll":["22","33","44"]}
c=pd.DataFrame(d)
print(c)

e={"sas":pd.Series([1,2,3,4]),"pas":pd.Series([8,9,2,6])}
var=pd.DataFrame(e)
print(var)