# Write a Python script that iterates through a list of integers and replaces every negative number found in the list with the value 0.

numbers = [5, -3, 8, -1, 0, -10, 12]
new_numbers = []
for i in numbers:
    if i >= 0:
        new_numbers.append(i)
    else:
        new_numbers.append(0)
print(new_numbers)



# The question says: "replaces every negative number found in the list" : This could mean modify the original list itself.
numbers = [5, -3, 8, -1, 0, -10, 12]
for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0
print(numbers)