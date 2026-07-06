import pandas as pd

df=pd.read_csv("StudentsPerformance.csv")
print(df.isnull().sum())
print( "Duplicates:",df.duplicated().sum())
print(df.columns)
df.rename(columns={"math score":"math score 1","reading score":"reading score 1","writing score":"writing score 1"}, inplace=True)
print(df.columns)
df["Average"]=df[["math score 1","reading score 1","writing score 1"]].mean(axis=1)
print(df.head())
df["Performance"]=None
print(df.columns)
import numpy as np
conditions=[
    df["Average"]>=90,
    (df["Average"]>=80) & (df["Average"]<90),
    (df["Average"]>=70) & (df["Average"]<80),
    df["Average"]<60
]
choice=[
    'Excillent',
    'Very Good',
    'Good',
    'Need Improvement'

]
df["Performance"]=np.select(conditions,choice,default='')
print(df.head())
df.to_csv("StudentsPerformance_Updated.csv", )
