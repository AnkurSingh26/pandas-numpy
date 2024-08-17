import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
y_1=sns.load_dataset("penguins")
sns.heatmap(data=y_1)
plt.show()