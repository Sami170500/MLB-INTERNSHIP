from sklearn.datasets import load_iris
iris=load_iris()
iris.data
X=iris.target
import pandas as pd
df=pd.DataFrame(iris.data,columns=(iris.feature_names))
print(df)
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())
