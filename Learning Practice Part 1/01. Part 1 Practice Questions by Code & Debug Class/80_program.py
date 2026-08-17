# Define a dictionary with five subjects and their respective marks. Utilize the get() method to try accessing a subject that is not in the dictionary, ensuring it prints "Not Available" as a default

marks = {"Math" : 98, "Physics" : 92, "Chemistry" : 95, "Biology" : 91, "History" : 96}
print(marks.get("Math"))
print(marks.get("M")) # None
print(marks.get("Ma", 12)) # 12
print(marks.get("Mat", "Not Available")) # Not Available