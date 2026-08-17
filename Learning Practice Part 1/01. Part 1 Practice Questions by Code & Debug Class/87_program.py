# Create a nested dictionary containing details for 4 students, where each student entry includes their name, age, and city. Write a loop to print the full details of each student in a clear, readable format.

students = {
    1: {
        "name": "Harshad",
        "age": 21,
        "city": "Latur"
    },
    2: {
        "name": "Shreyash",
        "age": 21,
        "city": "Pune"
    },
    3: {
        "name": "Gajanan",
        "age": 22,
        "city": "Nanded"
    },
    4: {
        "name": "Tushar",
        "age": 20,
        "city": "Mumbai"
    }
}

for student_id, details in students.items():
    print("Student ID:", student_id)
    print("Name:", details["name"])
    print("Age:", details["age"])
    print("City:", details["city"])
    print()