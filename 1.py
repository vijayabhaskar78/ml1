import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

print(df.describe())
df.hist(); plt.show()
sns.boxplot(data=df.iloc[:, :-1]); plt.show()
df.plot.scatter(x='sepal length (cm)', y='petal length (cm)', c=df['target']); plt.show()
