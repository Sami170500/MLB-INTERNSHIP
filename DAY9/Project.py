from sklearn.datasets import load_iris
iris=load_iris()
iris.data
import pandas as pd
df=pd.DataFrame(iris.data,columns=(iris.feature_names))
print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

from sklearn.cluster import KMeans
wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,random_state=42)
    kmeans.fit(df)
    wcss.append(kmeans.inertia_)
print(wcss)    

kmeans=KMeans(n_clusters=3,random_state=42)
df["Clusters"]=kmeans.fit_predict(df)
print(df.head())

import matplotlib.pyplot as plt
import seaborn as sns
sns.scatterplot(
    data=df,
    x="sepal length (cm)",
    y="sepal width (cm)",
    hue="Clusters"
)
plt.title("K-Means Clustering")
plt.show()

from sklearn.decomposition import PCA
pca=PCA(n_components=2)
X_pca=pca.fit_transform(df.iloc[:,:-1])
pca_df=pd.DataFrame(X_pca,columns=["Pc1",'Pc2'])
print(pca_df.head())
pca_df["Clusters"]=df["Clusters"]

sns.scatterplot(
    data=pca_df,
    x="Pc1",
    y="Pc2",
    hue="Clusters"
)
plt.show()
