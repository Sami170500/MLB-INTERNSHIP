import pandas as pd
df = pd.read_csv("StudentsPerformance.csv")

print(df.info())
print(df.head())
print(df.tail())
print(df.describe())

print("Math average:", df["math score"].mean())
print("Reading average:", df["reading score"].mean())
print("Writing average:", df["writing score"].mean())

df["Average"] = (df["math score"]+df["reading score"]+df["writing score"]) / 3
df.to_csv("StudentsPerformance_Analysis.csv", index=False)

class_average = df["Average"].mean()
print("TOP 5 Students")
Top5 = df.nlargest(5, "Average")
print(Top5)
Top5.to_csv("TopStudents.csv", index=False)

print("Below Average Students")
Below_Average = df[df["Average"] < class_average]
print(Below_Average)
Below_Average.to_csv("BelowAverageStudents.csv", index=False)
Total_Students = len(df)
print("Total Students:", Total_Students)
