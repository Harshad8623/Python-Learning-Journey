# Given a dictionary of subjects and their marks, sort it by marks in descending order. Then, print only the top 3 subjects with the highest marks.


marks = {
    "Math": 89,
    "Physics": 92,
    "Chemistry": 88,
    "Biology": 91,
    "C Programming": 98,
    "Python Programming": 87
}

sorted_marks = sorted(marks.items(), key=lambda x: x[1], reverse=True)

for subject, mark in sorted_marks[:3]:
    print(subject, "→", mark)