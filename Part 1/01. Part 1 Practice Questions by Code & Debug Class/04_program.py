# A student scored marks in 3 subjects. Calculate the average marks, total marks and print the result.
marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))

total_marks = marks1 + marks2 + marks3
average_marks = total_marks / 3

print("Total marks:", total_marks)
print("Average marks:", average_marks)
print(f"{marks1}, {marks2}, {marks3} are the marks scored in 3 subjects.")
print(f"Total marks: {total_marks}, Average marks: {average_marks}")