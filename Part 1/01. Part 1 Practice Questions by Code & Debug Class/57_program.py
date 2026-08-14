# Write a program that takes a list of numbers and using a loop determine whether it is sorted in ascending order or not

numbers = [1, 5, 7, 8, 12]
result = True
for i in range(len(numbers) - 1):
    if numbers[i] >= numbers[i + 1]:
        result = False
        break
print(result)