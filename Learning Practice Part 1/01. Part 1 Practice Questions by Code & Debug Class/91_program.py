# Given an existing dictionary of subjects and their respective marks, use dictionary comprehension to generate a new dictionary that includes only the subjects where the student scored 40 or more (i.e., passed)


marks = {
    "Math": 89,
    "Physics": 92,
    "Chemistry": 38,
    "Biology": 91,
    "C Programming": 35,
    "Python Programming": 87
}

passed = {subject: mark for subject, mark in marks.items() if mark >= 40}
print(passed)