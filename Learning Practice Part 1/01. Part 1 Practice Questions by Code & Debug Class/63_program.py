# Create a list containing the squares of numbers from 1 to 10 (i.e., [1, 4, 9, ..., 100]).

lst = []
for i in range(1, 11):
    lst.append(i * i)
print(lst)

# There is also a more Pythonic solution using list comprehension:
lst = [i * i for i in range(1, 11)]
print(lst)