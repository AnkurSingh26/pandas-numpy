import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
y_1=sns.load_dataset("penguins").head(20)
print(y_1)
sns.lineplot(x="bill_depth_mm",y="flipper_length_mm",data=y_1,style="sex")
plt.show()