import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance_Updated.csv")

total_students = len(df)
print("Total Students:", total_students)
df["Average"] = df[["math score 1", "reading score 1", "writing score 1"]].mean(axis=1)
top5 = df.sort_values(by="Average", ascending=False).head(5)
print("Top 5 Students:")
print(top5)
need_improvement = df[df["Performance"] == "Need Improvement"]
print("Students Needing Improvement:")
print(need_improvement)
subject_average = df["Average"]
highest_subject = subject_average.nlargest(1)
print("Subject with Highest Class Average:")
print(highest_subject)
sns.barplot(x=subject_average.index,y=subject_average.values,data=df)
plt.title("Average score for each subject")
plt.xlabel("Subjects")
plt.ylabel("Score")
plt.show()
sns.barplot(x=top5.index, y=top5["Average"])

plt.title("Top 5 Performing Students")
plt.xlabel("Student")
plt.ylabel("Average Score")
plt.show() 

count = df["Performance"].value_counts()
plt.pie(count, labels=count.index, autopct="%1.1f%%")
plt.title("Performance Distribution")
plt.show()
