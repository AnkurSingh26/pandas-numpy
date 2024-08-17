import seaborn as sns
import matplotlib.pyplot as plt

var1=[1,2,3,4,5,6,7]
var2=[2,3,4,5,6,8,9]
abx=sns.lineplot(x=var1,y=var2)
plt.show()
plt.plot(var1,var2)
#plt.show()