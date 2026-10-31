# ============================================================
# 1. CREATING A LIST
# ============================================================

student = ["Harshad", "Rahul", "Sanjay"]

# Creating a list using list()
ls1 = list((1, 2, 3, 4, 5))

# A string is iterable, so each character becomes an element
ls2 = list("harshad")

print(student)
print(ls1)
print(ls2)


# ============================================================
# 2. LIST OPERATORS
# ============================================================

ls3 = [1, 2, 3, 4]
ls4 = [5, 6, 7]

# + operator -> concatenates two lists
print(ls3 + ls4)
# Output: [1, 2, 3, 4, 5, 6, 7]

# * operator -> repeats a list
print(ls3 * 3)
# Output: [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

# Lists do NOT support arithmetic operations like:
# -, /, //, **
#
# But lists support:
# +  -> concatenation
# *  -> repetition
#
# Lists can also be compared:
print([1, 2] == [1, 2])   # True
print([1, 2] != [3, 4])   # True


# ============================================================
# 3. BUILT-IN FUNCTIONS USED WITH LISTS
# ============================================================

numbers = [10, 20, 30, 40, 50]

# len() -> number of elements
print("Length:", len(numbers))

# max() -> largest element
print("Maximum:", max(numbers))

# min() -> smallest element
print("Minimum:", min(numbers))

# sum() -> sum of all elements
print("Sum:", sum(numbers))

# sorted() -> returns a NEW sorted list
print("Sorted:", sorted(numbers))

# sorted(reverse=True) -> descending order
print("Descending:", sorted(numbers, reverse=True))


# ============================================================
# 4. INDEXING
# ============================================================

ls5 = [1, 2, 65, 85.5, 12, "Hello", "Hi", 98.6, 9]

# Positive indexing starts from 0
print(ls5[0])
print(ls5[1])
print(ls5[2])
print(ls5[3])
print(ls5[4])

# Negative indexing starts from -1
print(ls5[-1])   # Last element
print(ls5[-2])   # Second last element

# Invalid index gives IndexError
# print(ls5[99])

# Last element can be accessed in two ways
print(ls5[len(ls5) - 1])
print(ls5[-1])


# ============================================================
# 5. UPDATING LIST ELEMENTS
# ============================================================

ls5[1] = 12

print(ls5)


# ============================================================
# 6. LIST SLICING
# ============================================================

nums = [10, 20, 30, 40, 50, 60]

# Syntax:
# list[start : stop : step]
#
# start -> included
# stop  -> excluded
# step  -> jump size

print(nums[1:5])
# [20, 30, 40, 50]

print(nums[::2])
# [10, 30, 50]

print(nums[::3])
# [10, 40]

print(nums[1:3])
# [20, 30]

# Reverse a list using slicing
print(nums[::-1])
# [60, 50, 40, 30, 20, 10]

# Reverse with step 2
print(nums[::-2])
# [60, 40, 20]


# ============================================================
# 7. LOOPING THROUGH A LIST
# ============================================================

fruit = ["Apple", "Mango", "Banana", "Orange"]

# Directly iterate through values
for item in fruit:
    print(item)


# Using index
for i in range(len(fruit)):
    print(fruit[i])


# Reverse iteration using slicing
for item in fruit[::-1]:
    print(item)


# ============================================================
# 8. enumerate() - VERY IMPORTANT FOR INTERVIEWS
# ============================================================

# enumerate() gives both index and value

for index, value in enumerate(fruit):
    print(index, value)

# Example:
# 0 Apple
# 1 Mango
# 2 Banana
# 3 Orange


# ============================================================
# 9. reversed()
# ============================================================

# reversed() returns elements in reverse order
# It does not modify the original list

for item in reversed(fruit):
    print(item)


# ============================================================
# 10. append()
# ============================================================

ls = [1, 2, 3]

# append() adds ONE object at the end
result = ls.append(4)

print(result)   # None
print(ls)       # [1, 2, 3, 4]


# ============================================================
# 11. append() WITH A LIST
# ============================================================

ls = [1, 2, 3]

ls.append([4, 5])

# The complete list [4, 5] becomes ONE element
print(ls)
# [1, 2, 3, [4, 5]]


# ============================================================
# 12. extend()
# ============================================================
 
ls = [1, 2, 3]

# extend() adds elements individually
result = ls.extend([4, 5])

print(result)   # None
print(ls)       # [1, 2, 3, 4, 5]


# extend() works with any iterable
ls = [1, 2, 3]

ls.extend("JSW")

print(ls)
# [1, 2, 3, 'J', 'S', 'W']


# ============================================================
# 13. append() VS extend()
# ============================================================

a = [1, 2, 3]

a.append([4, 5])
print(a)
# [1, 2, 3, [4, 5]]


b = [1, 2, 3]

b.extend([4, 5])
print(b)
# [1, 2, 3, 4, 5]


# ============================================================
# 14. insert()
# ============================================================

ls = [1, 2, 3, 4]

# insert(index, value)
ls.insert(1, 100)

print(ls)
# [1, 100, 2, 3, 4]


# ============================================================
# 15. pop()
# ============================================================

ls = [10, 20, 30, 40]

# Without index -> removes last element
removed = ls.pop()

print("Removed:", removed)
print(ls)


# With index -> removes element at that index
removed = ls.pop(1)

print("Removed:", removed)
print(ls)


# ============================================================
# 16. remove()
# ============================================================

ls = [10, 20, 30, 20, 40]

# remove() removes the FIRST occurrence of the given value
result = ls.remove(20)

print(result)   # None
print(ls)
# [10, 30, 20, 40]


# ============================================================
# 17. del
# ============================================================

ls = [10, 20, 30, 40]

# Delete using index
del ls[1]

print(ls)
# [10, 30, 40]


# Delete a range
del ls[1:3]

print(ls)


# ============================================================
# 18. clear()
# ============================================================

ls = [1, 2, 3, 4]

result = ls.clear()

print(result)   # None
print(ls)       # []


# ============================================================
# 19. sort()
# ============================================================

lst1 = [4, 5, 1, 2, 6, 5, 12, 8]

# sort() modifies the original list
result = lst1.sort()

print(result)   # None
print(lst1)


# Descending order
lst1.sort(reverse=True)

print(lst1)


# ============================================================
# 20. sorted() VS sort()
# ============================================================

numbers = [3, 1, 5, 2, 4]

# sorted() creates a NEW list
new_list = sorted(numbers)

print("Original:", numbers)
print("New list:", new_list)


# sort() modifies original list
numbers.sort()

print("After sort():", numbers)


# ============================================================
# 21. reverse()
# ============================================================

lst = [1, 2, 3, 4, 5]

# reverse() modifies the original list
result = lst.reverse()

print(result)   # None
print(lst)


# ============================================================
# 22. reverse() VS [::-1]
# ============================================================

lst = [1, 2, 3, 4]

# reverse() -> modifies original
lst.reverse()

print(lst)


# [::-1] -> creates a reversed copy
lst = [1, 2, 3, 4]

new_lst = lst[::-1]

print("Original:", lst)
print("New:", new_lst)


# ============================================================
# 23. index()
# ============================================================

lst = [10, 20, 30, 40, 20]

# index() returns the index of FIRST occurrence
print(lst.index(20))
# 1


# ============================================================
# 24. count()
# ============================================================

lst = [10, 20, 20, 30, 20, 40]

# count() returns number of occurrences
print(lst.count(20))
# 3


# If element does not exist, count() returns 0
print(lst.count(100))
# 0


# ============================================================
# 25. copy()
# ============================================================

lst1 = [1, 2, 3]

lst2 = lst1.copy()

lst2.append(4)

print("Original:", lst1)
print("Copy:", lst2)


# ============================================================
# 26. ALIASING VS COPYING - IMPORTANT INTERVIEW CONCEPT
# ============================================================

# This does NOT create a new list

a = [1, 2, 3]

b = a

b.append(4)

print("a:", a)
print("b:", b)

# Both are changed because a and b refer to the same list.


# ============================================================
# 27. COPY
# ============================================================

a = [1, 2, 3]

b = a.copy()

b.append(4)

print("a:", a)
print("b:", b)

# Here a and b are separate lists.


# ============================================================
# 28. MEMBERSHIP OPERATORS
# ============================================================

lst = [10, 20, 30, 40]

# in
print(20 in lst)
# True

print(100 in lst)
# False

# not in
print(100 not in lst)
# True


# ============================================================
# 29. any()
# ============================================================

numbers = [0, 0, 0, 5, 0]

# any() returns True if at least ONE element is truthy
print(any(numbers))
# True


# ============================================================
# 30. all()
# ============================================================

numbers = [1, 2, 3, 4]

# all() returns True if ALL elements are truthy
print(all(numbers))
# True

numbers = [1, 2, 0, 4]

print(all(numbers))
# False


# ============================================================
# 31. zip()
# ============================================================

names = ["Harshad", "Rahul", "Sanjay"]
marks = [85, 90, 78]

# zip() combines corresponding elements

for name, mark in zip(names, marks):
    print(name, mark)


# ============================================================
# 32. LIST COMPREHENSION - VERY IMPORTANT
# ============================================================

numbers = [1, 2, 3, 4, 5]

# Normal approach
squares = []

for x in numbers:
    squares.append(x * x)

print(squares)


# List comprehension
squares = [x * x for x in numbers]

print(squares)


# ============================================================
# 33. LIST COMPREHENSION WITH CONDITION
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

# Get only even numbers
even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)
# [2, 4, 6]


# Get only odd numbers
odd_numbers = [x for x in numbers if x % 2 != 0]

print(odd_numbers)
# [1, 3, 5]


# ============================================================
# 34. NESTED LISTS
# ============================================================

# A list inside another list

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access elements
print(matrix[0][0])
# 1

print(matrix[1][2])
# 6

print(matrix[2][1])
# 8


# ============================================================
# 35. LOOP THROUGH NESTED LIST
# ============================================================

for row in matrix:

    for value in row:
        print(value)


# ============================================================
# 36. MATRIX / 2D LIST - DSA IMPORTANT
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
columns = len(matrix[0])

print("Rows:", rows)
print("Columns:", columns)

for i in range(rows):

    for j in range(columns):
        print(matrix[i][j], end=" ")

    print()


# ============================================================
# 37. IMPORTANT NESTED LIST TRAP
# ============================================================

# DON'T use this when creating a matrix:

matrix = [[0] * 3] * 3

# The inner lists refer to the SAME list.
# This can create unexpected behavior.


# Correct way:

matrix = [[0] * 3 for _ in range(3)]

print(matrix)


# ============================================================
# 38. LIST UNPACKING
# ============================================================

numbers = [10, 20, 30]

a, b, c = numbers

print(a)
print(b)
print(c)


# ============================================================
# 39. STAR UNPACKING
# ============================================================

numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers

print(first)
print(middle)
print(last)

# first = 1
# middle = [2, 3, 4]
# last = 5


# ============================================================
# 40. SLICING ASSIGNMENT
# ============================================================

lst = [1, 2, 3, 4]

# Replace elements from index 1 to 2
lst[1:3] = [20, 30]

print(lst)
# [1, 20, 30, 4]


# Number of replacement elements can be different

lst = [1, 2, 3, 4]

lst[1:3] = [100, 200, 300, 400]

print(lst)
# [1, 100, 200, 300, 400, 4]


# ============================================================
# 41. MUTABLE VS IMMUTABLE
# ============================================================

# Lists are MUTABLE.
# That means we can change their elements.

lst = [10, 20, 30]

lst[0] = 100

print(lst)


# Strings are IMMUTABLE.

text = "hello"

# This gives an error:
# text[0] = "H"


# ============================================================
# 42. FINDING LARGEST ELEMENT
# DSA PRACTICE
# ============================================================

numbers = [10, 25, 5, 40, 15]

largest = numbers[0]

for num in numbers:

    if num > largest:
        largest = num

print("Largest:", largest)


# ============================================================
# 43. FINDING SMALLEST ELEMENT
# ============================================================

numbers = [10, 25, 5, 40, 15]

smallest = numbers[0]

for num in numbers:

    if num < smallest:
        smallest = num

print("Smallest:", smallest)


# ============================================================
# 44. FIND SECOND LARGEST
# ============================================================

numbers = [10, 25, 5, 40, 15]

largest = float("-inf")
second_largest = float("-inf")

for num in numbers:

    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        second_largest = num

print("Largest:", largest)
print("Second largest:", second_largest)


# ============================================================
# 45. REVERSE A LIST USING LOOP
# ============================================================

numbers = [1, 2, 3, 4, 5]

reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print(reversed_list)


# ============================================================
# 46. CHECK WHETHER LIST IS SORTED
# ============================================================

numbers = [1, 2, 3, 4, 5]

is_sorted = True

for i in range(len(numbers) - 1):

    if numbers[i] > numbers[i + 1]:
        is_sorted = False
        break

print("Sorted:", is_sorted)


# ============================================================
# 47. COUNT FREQUENCY OF AN ELEMENT
# ============================================================

numbers = [1, 2, 2, 3, 2, 4, 2]

target = 2

count = 0

for num in numbers:

    if num == target:
        count += 1

print("Frequency:", count)


# ============================================================
# 48. FIND DUPLICATES
# ============================================================

numbers = [1, 2, 3, 2, 4, 3, 5]

duplicates = []

for i in range(len(numbers)):

    for j in range(i + 1, len(numbers)):

        if numbers[i] == numbers[j] and numbers[i] not in duplicates:
            duplicates.append(numbers[i])

print("Duplicates:", duplicates)


# ============================================================
# 49. FIND PAIR WITH TARGET SUM
# ============================================================

numbers = [2, 7, 11, 15]

target = 9

for i in range(len(numbers)):

    for j in range(i + 1, len(numbers)):

        if numbers[i] + numbers[j] == target:

            print("Pair:", numbers[i], numbers[j])


# ============================================================
# 50. MOVE ZEROS TO END
# ============================================================

numbers = [0, 1, 0, 3, 12]

result = []

# Add non-zero elements first
for num in numbers:

    if num != 0:
        result.append(num)

# Add zeros at the end
zero_count = numbers.count(0)

for i in range(zero_count):
    result.append(0)

print(result)
# [1, 3, 12, 0, 0]


# ============================================================
# 51. LIST TIME COMPLEXITY - DSA
# ============================================================

"""
IMPORTANT LIST TIME COMPLEXITIES

Operation                  Average Time Complexity
--------------------------------------------------
lst[i]                     O(1)
lst[i] = value             O(1)
append()                   O(1) amortized
pop()                      O(1)
pop(0)                     O(n)
insert(0, value)           O(n)
insert(i, value)           O(n)
remove(value)              O(n)
value in lst               O(n)
index(value)               O(n)
count(value)               O(n)
copy()                     O(n)
reverse()                  O(n)
sort()                     O(n log n)
sorted()                   O(n log n)

IMPORTANT:

Accessing an element by index is FAST:
    lst[5]                  -> O(1)

Searching for an element is LINEAR:
    50 in lst               -> O(n)

Removing from the beginning is slower:
    lst.pop(0)              -> O(n)

Removing from the end is fast:
    lst.pop()               -> O(1)
"""


# ============================================================
# 52. IMPORTANT INTERVIEW DIFFERENCES
# ============================================================

"""
append() vs extend()

append([1, 2])
    -> adds [1, 2] as ONE element

extend([1, 2])
    -> adds 1 and 2 separately


pop() vs remove()

pop(index)
    -> removes using INDEX
    -> returns removed element

remove(value)
    -> removes using VALUE
    -> returns None


sort() vs sorted()

sort()
    -> modifies original list
    -> returns None

sorted()
    -> creates a new sorted list
    -> original list remains unchanged


reverse() vs [::-1]

reverse()
    -> modifies original list
    -> returns None

[::-1]
    -> creates a new reversed list


a = b vs a.copy()

a = b
    -> both variables refer to same list

a = b.copy()
    -> creates a separate list


List vs String

List
    -> Mutable

String
    -> Immutable
"""


# ============================================================
#                    END OF LISTS
# ============================================================