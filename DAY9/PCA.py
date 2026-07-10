from sklearn.decomposition import PCA
pca=PCA(n_components=2,)
X_pca=pca.fit_transform(df.iloc[:, :-1])
pca_df=pd.DataFrame(X_pca,columns=("Pc1","Pc2"))
pca_df["clusters"]=df["clusters"]
print(pca_df.head())
sns.scatterplot(
    data=pca_df,
    x="Pc1",
    y="Pc2",
    hue="clusters"
)
plt.title("PCA Visualization")
plt.show()
