import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
y_1=sns.load_dataset("penguins")
print(y_1)
sns.displot(y_1["bill_depth_mm"],bins=[15,16,17,18,20,22,23])
plt.show()