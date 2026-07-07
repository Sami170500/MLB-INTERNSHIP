import pandas as pd
import numpy as np
df=pd.read_csv("student_performance (1).csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.columns)
df["Average"]=df[['Python','Mathematics','Statistics','Machine_Learning']].mean(axis=1)
print(df.head())
df=pd.get_dummies(
    df,columns=['Program'],drop_first=True,dtype=int
    )
print(df.columns)
X=df.drop(columns=['Student_ID','Name','Age','Average'])
Y=df['Average']
print(X.head())
print(Y.head())
df.to_csv("preprocessed_student_performance.csv", index=False)

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(
    X,Y,
    test_size=0.2,
    random_state=42
)
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X_train,Y_train)
Y_pred=model.predict(X_test)
print("Model Pridiction :",Y_pred)
from sklearn.metrics import mean_squared_error,root_mean_squared_error,r2_score
MSE=mean_squared_error(Y_test,Y_pred)
RMSE=root_mean_squared_error(Y_test,Y_pred)
R2S=r2_score(Y_test,Y_pred)
print("Mean Square error : ",MSE)
print("Root Mean Square error :",RMSE)
print("R2 score errro:",R2S)
comparison=pd.DataFrame({
    "Actual":Y_test,
    "Prediction":Y_pred
})
print(comparison)

import matplotlib.pyplot as plt
import seaborn as sns
sns.scatterplot(
    x=Y_test,
    y=Y_pred
)
plt.xlabel("Actual Average Score")
plt.ylabel("Predicted Average Score")
plt.title("Actual vs Predicted Average Score")
plt.grid(True)
plt.show()
