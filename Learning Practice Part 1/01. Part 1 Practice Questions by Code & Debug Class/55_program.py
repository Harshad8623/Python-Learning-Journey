# Given a list of numbers use a loop to calculate and print their average You can use len() to get the count of elemets but avoid using sum() for the total

lst = [10, 5, 6, 8, 13, 7]
total = 0
for i in lst:
    total += i
print(total)