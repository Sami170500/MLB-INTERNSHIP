import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df= pd.read_csv("StudentsPerformance_Updated.csv")
sns.barplot(x=df.index[:10], y=df["Average"][:10])
plt.title("Average Marks of Students")
plt.xlabel("Student")
plt.ylabel("Average")
plt.show()

sns.histplot(df["Average"])
plt.title("Distribution of Average Scores")
plt.xlabel("Average Score")
plt.ylabel("Frequency")
plt.show()

sns.scatterplot(x="math score 1", y="reading score 1",data=df)
plt.title("Math Score vs Reading Score")
plt.xlabel("Math Score")
plt.ylabel("Reading Score")
plt.show()

performance_count = df["Performance"].value_counts()

plt.pie(
    performance_count,
    labels=performance_count.index,
    autopct="%1.1f%%"
)
plt.title("Distribution of Students by Performance")
plt.show()

sns.boxplot(data=df[["math score 1", "reading score 1", "writing score 1"]])
plt.title("Spread of Marks in All Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()
