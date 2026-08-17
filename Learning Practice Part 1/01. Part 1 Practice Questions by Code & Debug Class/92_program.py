# You have two separate lists: one containing subject names and another containing corresponding marks. Create a dictionary from these two lists using dictionary comprehension, mapping each subject to its mark.


subjects = ["Math", "Physics", "Chemistry", "Biology", "Python"]
marks = [89, 92, 88, 91, 97]

result = {subject: mark for subject, mark in zip(subjects, marks)}
print(result)