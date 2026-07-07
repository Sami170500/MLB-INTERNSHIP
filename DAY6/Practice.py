import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
df=pd.read_csv("StudentRecord.csv")
df=df.drop(columns=['Unnamed: 0.1','Unnamed: 0'])
print(df.columns)
df=pd.get_dummies(
    df, 
    columns=[
        'gender','race/ethnicity','parental level of education',
        'lunch','test preparation course'
    ],
    drop_first=True
)
X=df.drop(columns=["Average"])
Y=df["Average"]
print(X.head())
print(Y.head())

X_train,X_test,Y_train,Y_test= train_test_split(
    X,Y,
    test_size=0.2,
    random_state=40

)
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

model=LinearRegression()
model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)
print(Y_pred)
mae = mean_absolute_error(Y_test, Y_pred)
mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)

print("MAE:", mae)
print("MSE:", mse)
print("R² Score:", r2)
