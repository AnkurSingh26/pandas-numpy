import pandas as pd
x=[1,2,3,4,5]
y=[6,7,8,9,1]
a={'A':[1,2,3,4,5],'B':[6,7,8,9,1]}
A=pd.DataFrame(a)
print(A)
A.insert(1,"python",A['B'])#NOT REQUIRED
print(A)
#var=A.pop("python")
#print(A)
A.to_csv("test.csv",index=False,header=[1,2,3])