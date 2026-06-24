name=input("Please enter your name :")
Class=input("Please enter your class :")
subject_num=(int(input("Please enter the number of subjects you have:")))
Subject=[]
Marks=[]
for i in range(subject_num):
    subject=input(f"Please enter your subjects{i+1} name:")
    marks=int(input(f"Please enter your marks for {subject}:"))
    Subject.append(subject)
    Marks.append(marks)

avg= sum(Marks)/len(Marks)

if avg>=90:
    grade="A+"

elif avg>=80:
    grade='A' 

elif avg>=75:
    grade='B+'

elif avg>=70:
    grade="B"

elif avg >=65:
    grade="C+"

elif avg>=60:
    grade="C"

elif avg>=55:
    grade="D+"

elif avg>=50:
    grade="D"

else:
    grade="F"

print("------------Record------------")    
print(f"Name: {name}")
print(f"Class: {Class}")
print(f"Average: {avg}")
print(f"Grade: {grade}")
