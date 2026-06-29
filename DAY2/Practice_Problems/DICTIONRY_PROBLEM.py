// Create a student record dictionary
student={
    "name":"Sami",
    "Age":20,
    "CGPA":3.49
}

// Calculate average marks of students.
students={
    "Marks1":60,
    "Marks2":75,
    "Marks3":87
}
total=0
for i in students.values():
    total+=i
avg=total/len(students)
print("Average marks:",avg)


// Count frequency of words in a sentence
sentence = input("Enter a sentence: ")

words = sentence.split()
freq = {}

for word in words:
    freq[word] = words.count(word)

print(freq)
