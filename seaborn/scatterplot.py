import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
y_1=sns.load_dataset("penguins")
print(y_1)
sns.scatterplot(x="bill_length_mm",y="flipper_length_mm",data=y_1,hue="sex")
plt.show()