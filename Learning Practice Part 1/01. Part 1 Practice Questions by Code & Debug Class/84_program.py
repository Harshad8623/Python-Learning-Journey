# Populate a dictionary with six student names and their corresponding marks. Loop through it and print the names of all students who achieved a score above 75.

students = {"Harshad" : 98, "Shreyash" : 85, "Gajanan" : 38, "Tushar" : 68, "Pradeep": 82}
for name, marks in students.items():
    if marks > 75:
        print(name, "→", marks)