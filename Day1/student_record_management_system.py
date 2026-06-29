Students = []

while True:
    print("\n","--------STUDENT RECORD MANAGEMENT SYSTEM--------")
    print("1. Add STUDENT ")
    print("2. VIEW ALL STUDENTS ")
    print("3. SEARCH STUDENT  ")
    print("4. UPDATE DETAILS ")
    print("5. REMOVE STUDENT ")
    print("6. EXIT ")

    choice = int(input("Please enter choice from 1 to 6 : "))

    if choice == 1:
        Name = input("Enter your name: ")
        Rollno = input("Enter your roll number: ")
        Age = input("Enter your age: ")
        Course = input("Enter your course: ")

        student = {
            "Name": Name,
            "Rollno": Rollno,
            "Age": Age,
            "Course": Course
        }

        Students.append(student)
        print("Student details added successfully!")

    if choice == 2:
        print("All the Students Record :")
        for student in Students:
            print(student)

    if choice == 3:
        Rollno = input("Enter roll number to search: ")
        found = False

        for student in Students:
            if student["Rollno"] == Rollno:
                print("Student found!")
                print("Name:", student["Name"])
                print("Age:", student["Age"])
                print("Rollno:", student["Rollno"])
                print("Course:", student["Course"])
                found = True
                break

        if not found:
            print("Student not found!")

    if choice == 4:
        Rollno = input("Please enter the roll number that you want to update")
        found = False

        for student in Students:
            if student["Rollno"] == Rollno:
                student["Name"] = input("please enter new name: ")
                student["Age"] = input("please enter new age :")
                student["Rollno"] = input("please enter the new roll no:")
                student["Course"] = input("PLease enter the new course :")
                found = True
                break

        if not found:
            print("ROll No not found!")

    if choice == 5:
        Rollno = input("please enter the roll num of student that you want to remove from record:")
        found = False

        for student in Students:
            if student["Rollno"] == Rollno:
                Students.remove(student)
                found = True
                print("Student is Removed")
                break

        if not found:
            print("ROll No not found!")

    if choice == 6:
        print("Thanks!")
        break
