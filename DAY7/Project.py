from sklearn.datasets import load_iris
iris=load_iris()
print(iris.feature_names)
print(iris)
X=iris.data
Y=iris.target
import pandas as pd
df=pd.DataFrame(X,columns=iris.feature_names)
df["Species"]=Y
print(df)
print(df.head())
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(
    X,Y,
    test_size=0.2,
    random_state=42
)
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(X_train,Y_train)
y_pred=model.predict(X_test)

from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
print("Acuracy: ",accuracy_score(Y_test,y_pred))
print("Precision: ",precision_score(Y_test,y_pred,average="weighted"))
print("Recall:",recall_score(Y_test,y_pred,average="weighted"))
print("F1 score:",f1_score(Y_test,y_pred,average="weighted"))

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(Y_test,y_pred)
print("Confusion_matrix",cm)

for i in range(10):
    print("Actual :",iris.target_names[Y_test[i]])
    print("Prediction:",iris.target_names[y_pred[i]])

from sklearn.metrics import classification_report
print("Classification Report")
Report=classification_report(Y_test,y_pred)
print(Report)    
