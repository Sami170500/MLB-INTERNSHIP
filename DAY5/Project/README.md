# Student Performance Dashboard

## Data Cleaning Steps Performed

* Loaded the dataset using Pandas.
* Checked for missing values using `isnull().sum()`.
* Checked for duplicate records using `duplicated().sum()`.
* Renamed the subject score columns for better readability.
* Created a new **Average** column by calculating the mean of Math, Reading, and Writing scores.
* Created a new **Performance** column to classify students into:

  * Excellent
  * Good
  * Average
  * Needs Improvement
* Saved the cleaned dataset as `cleaned_student_performance.csv`.

---

## Visualizations Created

### 1. Average Score of Each Subject (Bar Chart)

**Why:** To compare the average marks of Math, Reading, and Writing and identify the subject with the highest class average.

### 2. Top 5 Performing Students (Bar Chart)

**Why:** To compare the average scores of the five highest-performing students.

### 3. Performance Distribution (Pie Chart)

**Why:** To show the proportion of students in each performance category (Excellent, Good, Average, and Needs Improvement).

---

## Three Key Insights

1. **Reading** had the highest class average among the three subjects.

2. The dataset contains **1000 student records**, and no missing values or duplicate records were found after cleaning.

3. Most students fall into the **Average** and **Good** performance categories, while fewer students are classified as **Excellent** or **Needs Improvement**.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Seaborn
* Matplotlib

---

## Project Files

* `data_cleaning.py`
* `student_dashboard.py`
* `cleaned_student_performance.csv`
* `Charts for project/`
* `README.md`

