import numpy as pd
a=pd.array([10,20,40,50])
print(pd.insert(a,1,30))
a=pd.array([[10,20],[30,40],[50,60]])
z=pd.insert(a,1,[30],axis=0)
print(z)