# Design a dictionary where each key is a student's name and the corresponding value is a list of their marks in 3 different subjects. Calculate and print the total marks and average marks for each student.


students = {
    "Harshad": [98, 92, 95],
    "Shreyash": [85, 88, 90],
    "Gajanan": [72, 68, 75],
    "Tushar": [80, 76, 84]
}

for name, marks in students.items():
    total = sum(marks)
    average = total / len(marks)

    print("Student:", name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
    print()