import numpy as np
c=np.array([[10,20,30],[40,50.0,60]])
print(c)
print(c.shape)
print(c.size)
print(c.dtype)
a=np.array([10,20,30,40,50])
s=np.array_split(a,3)
print(s)
