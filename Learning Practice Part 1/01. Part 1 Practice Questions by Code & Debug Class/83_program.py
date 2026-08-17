# Given a dictionary of marks for different subjects, loop over its values() to calculate and print the total marks and the average mark obtained.

marks = {"Math" : 92, "Physics" : 85, "Chemistry" : 87, "History" : 89, "Biology" : 91}
total = 0
for i in marks.values():
    total += i
print("Total Marks :",total)
print("Average Marks :",total/len(marks))


# Another way
total = sum(marks.values())
average = total / len(marks)

print("Total Marks :", total)
print("Average Marks :", average)