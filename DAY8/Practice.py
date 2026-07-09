from sklearn.datasets import load_breast_cancer
cancer=load_breast_cancer()
X=cancer.data
Y=cancer.target
print(cancer.feature_names)
print(cancer.target_names)
import pandas as pd
df=pd.DataFrame(X,columns=[cancer.feature_names])
print(df)
print(df.head())
print(df.info())
print(df.describe())
df["target"]=cancer.target
print(df["target"].value_counts())
print(cancer.target_names)
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(
    X,Y,
    test_size=0.2,
    random_state=42
)
from sklearn.linear_model import LogisticRegression
model=LogisticRegression(max_iter=500)
model.fit(X_train,Y_train)
print(model.get_params())
y_pred=model.predict(X_test)

from sklearn.metrics import accuracy_score,precision_score,f1_score
print("Accuracy",accuracy_score(Y_test,y_pred))
print("Precision",precision_score(Y_test,y_pred))
print("F1 Score",f1_score(Y_test,y_pred)) 

from sklearn.model_selection import GridSearchCV
parms={
    'C':[0.01,0.1,1,10,20],
    'max_iter':[100,500,1000]
}
grid=GridSearchCV(
    estimator=LogisticRegression(),
    param_grid=parms,
    cv=5,
    scoring="accuracy"
)
grid.fit(X_train,Y_train)
print(grid.best_params_)
print(grid.best_score_)
print(grid.best_estimator_)
best_model=grid.best_estimator_
y_pred_best=best_model.predict(X_test)
print(accuracy_score(Y_test,y_pred))
print(accuracy_score(Y_test,y_pred_best))
