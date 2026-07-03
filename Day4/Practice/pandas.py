import pandas as pd
df=pd.read_csv("StudentsPerformance.csv")
print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df[df['math score']>75])
df["Average"]=(df['math score']+df['reading score']+df['writing score'])/3
print(df['Average'])
print(df[df["gender"]=='male'])
print(df[df['math score']<df['Average']])
