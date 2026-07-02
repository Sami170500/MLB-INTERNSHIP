import json

try:
    with open("students.json", "r") as file:
        Students = json.load(file)
except:
    Students = []

def save():
    with open("students.json", "w") as file:
        json.dump(Students, file, indent=4)

while True:
    print("\n--------STUDENT RECORD MANAGEMENT SYSTEM--------")
    print("1. Add STUDENT")
    print("2. VIEW ALL STUDENTS")
    print("3. SEARCH STUDENT")
    print("4. UPDATE DETAILS")
    print("5. REMOVE STUDENT")
    print("6. EXIT")

    try:
        choice = int(input("Please enter choice from 1 to 6: "))
    except ValueError:
        print("Invalid choice!")
        continue

    if choice == 1:
        Name = input("Enter your name: ")
        Rollno = input("Enter your roll number: ")

        duplicate = False
        for student in Students:
            if student["Rollno"].lower() == Rollno.lower():
                duplicate = True
                break

        if duplicate:
            print("Student with this Roll Number already exists!")
            continue

        try:
            Age = int(input("Enter your age: "))
        except ValueError:
            print("Age must be a number!")
            continue

        Course = input("Enter your course: ")

        student = {
            "Name": Name,
            "Rollno": Rollno,
            "Age": Age,
            "Course": Course
        }

        Students.append(student)
        save()
        print("Student details added successfully!")

    elif choice == 2:
        if not Students:
            print("No records found.")
        else:
            print("\nAll Students Record:")
            for student in Students:
                print(student)

    elif choice == 3:
        Rollno = input("Enter roll number to search: ")

        found = False
        for student in Students:
            if student["Rollno"].lower() == Rollno.lower():
                print("\nStudent Found!")
                print("Name:", student["Name"])
                print("Roll No:", student["Rollno"])
                print("Age:", student["Age"])
                print("Course:", student["Course"])
                found = True
                break

        if not found:
            print("Student not found!")

    elif choice == 4:
        Rollno = input("Enter Roll Number to update: ")

        found = False
        for student in Students:
            if student["Rollno"].lower() == Rollno.lower():

                student["Name"] = input("Enter new name: ")

                try:
                    student["Age"] = int(input("Enter new age: "))
                except ValueError:
                    print("Age must be a number!")
                    break

                student["Course"] = input("Enter new course: ")

                save()
                print("Record updated successfully!")
                found = True
                break

        if not found:
            print("Roll Number not found!")

    elif choice == 5:
        Rollno = input("Enter Roll Number to remove: ")

        found = False
        for student in Students:
            if student["Rollno"].lower() == Rollno.lower():
                Students.remove(student)
                save()
                print("Student removed successfully!")
                found = True
                break

        if not found:
            print("Roll Number not found!")

    elif choice == 6:
        print("Thanks for using the system!")
        break

    else:
        print("Please enter a choice between 1 and 6.")
        
