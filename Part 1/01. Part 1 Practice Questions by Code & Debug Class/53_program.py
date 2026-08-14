# Given a list of numbers , write python code using loop to find and print largest number exists in the list without using built in function
ls = [ 10, 5, 8, 45, 85, 25, 99, 12, 56, 2, 98]
ls = [-10, -5, -20]

largest = ls[0]
for i in ls:
    if i > largest:
        largest = i
print(largest)