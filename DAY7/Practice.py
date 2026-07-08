from sklearn.datasets import load_wine
wine=load_wine()
X=wine.data
Y=wine.target
import pandas as pd
import numpy as np
df=pd.DataFrame(X,columns=wine.feature_names)
print(df)
df["Target"]=Y
print(Y)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test =train_test_split(
    X,Y,
    test_size=0.2,
    random_state=42
)
from sklearn.linear_model import LogisticRegression
model=LogisticRegression(max_iter=200)
model.fit(X_train,Y_train)
y_pred=model.predict(X_test)
print(y_pred)
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

print("Accuracy Score:",accuracy_score(Y_test,y_pred))
print("Precision:",precision_score(Y_test,y_pred,average="weighted"))
print("Recall: ",recall_score(Y_test,y_pred,average="weighted"))
print("F1 score:",f1_score(Y_test,y_pred,average="weighted"))

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(Y_test,y_pred)
print('Confusion Matrix:',cm)
