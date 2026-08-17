# Create a dictionary of 6 subjects and their respective marks. Print the subject with the highest marks and the one with the lowest, using max() and min() functions alongside a lambda expression.

marks = {
    "Math": 89,
    "Physics": 92,
    "Chemistry": 88,
    "Biology": 91,
    "C programming": 98,
    "Python Programming": 87
}

highest = max(marks.items(), key=lambda x: x[1])
lowest = min(marks.items(), key=lambda x: x[1])

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)