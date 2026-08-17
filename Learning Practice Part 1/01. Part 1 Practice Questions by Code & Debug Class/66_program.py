# Using list comprehension, create a list of squares of all odd numbers from 1 to 20

lst = [i * i for i in range(1, 21) if i % 2 != 0 ] # if i % 2 == 1 is also accptable
print(lst)