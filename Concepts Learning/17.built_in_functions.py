# ============================================================
#        IMPORTANT PYTHON BUILT-IN FUNCTIONS
# ============================================================

"""
This file covers important Python built-in functions that are
very useful for:

1. Python interviews
2. Coding rounds
3. DSA
4. Problem solving

IMPORTANT FUNCTIONS:

range()
enumerate()
zip()
ord()
chr()
id()
abs()
round()
sum()
min()
max()
len()
sorted()
reversed()
any()
all()
map()
filter()
type()
isinstance()
input()
"""

# ============================================================
# 1. range()
# ============================================================

"""
range() generates a sequence of numbers.

Common forms:

range(stop)
range(start, stop)
range(start, stop, step)

IMPORTANT:
The stop value is NOT included.
"""

print(range(5))

# Output:
# range(0, 5)

print(list(range(5)))

# Output:
# [0, 1, 2, 3, 4]


# start, stop
print(list(range(2, 7)))

# [2, 3, 4, 5, 6]


# start, stop, step
print(list(range(2, 10, 2)))

# [2, 4, 6, 8]


# Reverse range
print(list(range(10, 0, -1)))

# [10, 9, 8, ..., 1]


# ============================================================
# range() IN LOOPS
# ============================================================

for i in range(5):
    print(i)


# ============================================================
# range() WITH LIST INDEX
# ============================================================

arr = [10, 20, 30, 40]

for i in range(len(arr)):
    print(i, arr[i])


# ============================================================
# 2. enumerate()
# ============================================================

"""
enumerate() gives:

index + value

Syntax:

enumerate(iterable, start=0)
"""

names = ["Harshad", "Rahul", "Sanjay"]

for index, name in enumerate(names):
    print(index, name)


"""
Output:

0 Harshad
1 Rahul
2 Sanjay
"""


# ============================================================
# enumerate() WITH CUSTOM START
# ============================================================

for index, name in enumerate(names, start=1):
    print(index, name)


"""
Output:

1 Harshad
2 Rahul
3 Sanjay
"""


# ============================================================
# WITHOUT enumerate()
# ============================================================

for i in range(len(names)):
    print(i, names[i])


# ============================================================
# WITH enumerate()
# ============================================================

for i, name in enumerate(names):
    print(i, name)


"""
For DSA, enumerate() is useful when you need both:

index
value
"""


# ============================================================
# 3. zip()
# ============================================================

"""
zip() combines elements from multiple iterables.

Example:

names = ["Harshad", "Rahul", "Sanjay"]
marks = [90, 85, 88]

zip(names, marks)

creates pairs:

Harshad -> 90
Rahul   -> 85
Sanjay  -> 88
"""

names = ["Harshad", "Rahul", "Sanjay"]

marks = [90, 85, 88]

result = zip(names, marks)

print(list(result))


# ============================================================
# zip() IN LOOP
# ============================================================

names = ["Harshad", "Rahul", "Sanjay"]

marks = [90, 85, 88]

for name, mark in zip(names, marks):

    print(name, mark)


# ============================================================
# zip() WITH 3 LISTS
# ============================================================

names = ["Harshad", "Rahul", "Sanjay"]

ages = [21, 22, 20]

marks = [90, 85, 88]

for name, age, mark in zip(names, ages, marks):

    print(name, age, mark)


# ============================================================
# IMPORTANT zip() BEHAVIOR
# ============================================================

"""
If the lists have different lengths,
zip() normally stops at the shortest iterable.
"""

a = [1, 2, 3, 4]

b = [10, 20]

print(list(zip(a, b)))

# Output:
# [(1, 10), (2, 20)]


# ============================================================
# 4. ord()
# ============================================================

"""
ord() returns the Unicode code point of a character.

Example:

ord('A') -> 65
ord('a') -> 97
"""

print(ord('A'))

print(ord('B'))

print(ord('a'))

print(ord('z'))

print(ord('0'))


# ============================================================
# ord() IN DSA
# ============================================================

"""
Very useful in:

- Character problems
- String problems
- Frequency arrays
- Alphabet problems
"""

char = 'C'

position = ord(char) - ord('A')

print(position)

# C -> 2


"""
For uppercase:

A -> 0
B -> 1
C -> 2
...
Z -> 25
"""


# ============================================================
# LOWERCASE
# ============================================================

char = 'd'

position = ord(char) - ord('a')

print(position)

# d -> 3


# ============================================================
# 5. chr()
# ============================================================

"""
chr() does the reverse of ord().

ord():

character -> number

chr():

number -> character
"""

print(chr(65))

# A

print(chr(97))

# a


# ============================================================
# ord() AND chr() TOGETHER
# ============================================================

char = 'A'

number = ord(char)

new_char = chr(number)

print(number)

print(new_char)


# ============================================================
# 6. id()
# ============================================================

"""
id() returns the identity of an object.

Example:
"""

x = 10

print(id(x))


"""
The exact number can vary between executions.

Don't memorize the number.

Think:

id(object)
    ↓
identity of object
"""


# ============================================================
# id() WITH LISTS
# ============================================================

a = [1, 2, 3]

b = a

print(id(a))

print(id(b))


"""
Both IDs are the same because:

b = a

means both variables refer to the same list.
"""


# ============================================================
# COPY
# ============================================================

a = [1, 2, 3]

b = a.copy()

print(id(a))

print(id(b))


"""
IDs are different because a.copy()
creates another list object.
"""


# ============================================================
# 7. len()
# ============================================================

"""
len() returns the number of elements/characters.
"""

arr = [10, 20, 30, 40]

print(len(arr))

# 4


name = "Harshad"

print(len(name))

# 7


# ============================================================
# len() IN DSA
# ============================================================

arr = [10, 20, 30, 40, 50]

print(len(arr))

# Very commonly used in:
# loops
# arrays
# strings
# sliding window
# two pointers


# ============================================================
# 8. sum()
# ============================================================

numbers = [10, 20, 30, 40]

print(sum(numbers))

# 100


# Start value can be specified

print(sum(numbers, 100))

# 200


# ============================================================
# DSA EXAMPLE
# ============================================================

arr = [1, 2, 3, 4, 5]

total = sum(arr)

print(total)


# ============================================================
# 9. min()
# ============================================================

numbers = [10, 5, 20, 3, 15]

print(min(numbers))

# 3


# ============================================================
# 10. max()
# ============================================================

numbers = [10, 5, 20, 3, 15]

print(max(numbers))

# 20


# ============================================================
# min() AND max() IN DSA
# ============================================================

arr = [10, 20, 5, 40, 15]

minimum = min(arr)

maximum = max(arr)

print(minimum)

print(maximum)


# ============================================================
# 11. abs()
# ============================================================

"""
abs() returns absolute value.

It removes the negative sign.
"""

print(abs(10))

print(abs(-10))

print(abs(-25.5))


# ============================================================
# DSA EXAMPLE
# ============================================================

a = 10

b = 25

difference = abs(a - b)

print(difference)

# 15


# ============================================================
# 12. round()
# ============================================================

"""
round() rounds a number.
"""

print(round(10.4))

print(round(10.6))


# Specify decimal places

print(round(10.4567, 2))

# 10.46


# ============================================================
# 13. sorted()
# ============================================================

"""
sorted() returns a NEW sorted list.

It does NOT modify the original list.
"""

arr = [5, 2, 8, 1, 3]

result = sorted(arr)

print(result)

print(arr)


# ============================================================
# DESCENDING ORDER
# ============================================================

print(sorted(arr, reverse=True))


# ============================================================
# sorted() WITH STRING
# ============================================================

name = "python"

print(sorted(name))

# ['h', 'n', 'o', 'p', 't', 'y']


# ============================================================
# 14. sort() VS sorted()
# ============================================================

"""
sort():

- List method
- Modifies original list
- Returns None

sorted():

- Built-in function
- Creates a new sorted list
- Original remains unchanged
"""

arr = [5, 1, 4, 2]

result = sorted(arr)

print(result)

print(arr)


arr.sort()

print(arr)


# ============================================================
# 15. reversed()
# ============================================================

"""
reversed() returns an iterator that goes
through elements in reverse order.
"""

arr = [1, 2, 3, 4, 5]

print(list(reversed(arr)))


# ============================================================
# reversed() VS [::-1]
# ============================================================

arr = [1, 2, 3, 4, 5]

print(arr[::-1])

print(list(reversed(arr)))


"""
Both can be used to iterate in reverse.

arr[::-1]:

creates a reversed copy.

reversed(arr):

returns a reverse iterator.
"""


# ============================================================
# 16. any()
# ============================================================

"""
any() returns True if AT LEAST ONE element is truthy.
"""

values = [False, False, True, False]

print(any(values))

# True


values = [False, False, False]

print(any(values))

# False


# ============================================================
# DSA EXAMPLE
# ============================================================

numbers = [1, 3, 5, 8, 9]

result = any(number % 2 == 0 for number in numbers)

print(result)

# True


# ============================================================
# 17. all()
# ============================================================

"""
all() returns True only if EVERY element is truthy.
"""

values = [True, True, True]

print(all(values))

# True


values = [True, False, True]

print(all(values))

# False


# ============================================================
# DSA EXAMPLE
# ============================================================

numbers = [2, 4, 6, 8]

result = all(number % 2 == 0 for number in numbers)

print(result)

# True


# ============================================================
# 18. map()
# ============================================================

"""
map() applies a function to every element.
"""

numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x * 2, numbers)

print(list(result))

# [2, 4, 6, 8, 10]


# ============================================================
# map() WITH NORMAL FUNCTION
# ============================================================

def square(n):

    return n * n


numbers = [1, 2, 3, 4]

result = map(square, numbers)

print(list(result))


# ============================================================
# 19. filter()
# ============================================================

"""
filter() keeps elements for which the function
returns True.
"""

numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))

# [2, 4, 6]


# ============================================================
# 20. map() VS filter()
# ============================================================

"""
map():

Transform every element.

Example:

[1, 2, 3]

->

[2, 4, 6]


filter():

Select elements based on condition.

Example:

[1, 2, 3, 4]

->

[2, 4]
"""


# ============================================================
# 21. type()
# ============================================================

x = 10

print(type(x))

# <class 'int'>


name = "Harshad"

print(type(name))

# <class 'str'>


# ============================================================
# 22. isinstance()
# ============================================================

x = 10

print(isinstance(x, int))

# True

print(isinstance(x, str))

# False


# ============================================================
# type() VS isinstance()
# ============================================================

"""
type(x):

Returns the exact type.

isinstance(x, int):

Checks whether x is an instance of int
or a compatible subclass.
"""


# ============================================================
# 23. input()
# ============================================================

"""
input() takes input from the user.

IMPORTANT:

input() ALWAYS returns a string.
"""

# name = input("Enter name: ")

# print(name)


# ============================================================
# input() WITH int()
# ============================================================

"""
If we want an integer:

age = int(input())
"""

# age = int(input("Enter age: "))

# print(age)


# ============================================================
# 24. list()
# ============================================================

"""
list() converts an iterable into a list.
"""

text = "Python"

print(list(text))

# ['P', 'y', 't', 'h', 'o', 'n']


numbers = range(5)

print(list(numbers))

# [0, 1, 2, 3, 4]


# ============================================================
# 25. tuple()
# ============================================================

numbers = [1, 2, 3]

result = tuple(numbers)

print(result)

# (1, 2, 3)


# ============================================================
# 26. set()
# ============================================================

numbers = [1, 2, 2, 3, 3, 4]

result = set(numbers)

print(result)

# {1, 2, 3, 4}


"""
Very useful for removing duplicates.
"""


# ============================================================
# 27. dict()
# ============================================================

data = [
    ("name", "Harshad"),
    ("age", 21)
]

student = dict(data)

print(student)


# ============================================================
# 28. reversed() + enumerate()
# ============================================================

arr = [10, 20, 30, 40]

for index, value in enumerate(reversed(arr)):

    print(index, value)


# ============================================================
# 29. zip() + enumerate()
# ============================================================

names = ["Harshad", "Rahul", "Sanjay"]

marks = [90, 85, 88]

for index, (name, mark) in enumerate(zip(names, marks)):

    print(index, name, mark)


# ============================================================
# 30. range() + len() + enumerate()
# ============================================================

arr = [10, 20, 30, 40]

# Traditional

for i in range(len(arr)):

    print(i, arr[i])


# Better when index + value are needed

for i, value in enumerate(arr):

    print(i, value)


# ============================================================
# 31. DSA EXAMPLE - CHARACTER FREQUENCY
# ============================================================

text = "banana"

frequency = {}

for char in text:

    if char in frequency:

        frequency[char] += 1

    else:

        frequency[char] = 1


print(frequency)


# ============================================================
# 32. DSA EXAMPLE - ord()
# ============================================================

text = "abc"

frequency = [0] * 26

for char in text:

    index = ord(char) - ord('a')

    frequency[index] += 1


print(frequency)


"""
For:

'a' -> 0
'b' -> 1
'c' -> 2

This technique is VERY useful in string DSA problems.
"""


# ============================================================
# 33. DSA EXAMPLE - ZIP
# ============================================================

arr1 = [1, 2, 3]

arr2 = [4, 5, 6]

result = []

for a, b in zip(arr1, arr2):

    result.append(a + b)


print(result)

# [5, 7, 9]


# ============================================================
# 34. DSA EXAMPLE - ENUMERATE
# ============================================================

arr = [10, 20, 30, 40, 50]

target = 30

for index, value in enumerate(arr):

    if value == target:

        print("Target found at index:", index)

        break


# ============================================================
# 35. DSA EXAMPLE - MAXIMUM
# ============================================================

arr = [10, 50, 20, 80, 30]

maximum = max(arr)

print(maximum)


# ============================================================
# 36. DSA EXAMPLE - MINIMUM
# ============================================================

arr = [10, 50, 20, 80, 30]

minimum = min(arr)

print(minimum)


# ============================================================
# 37. DSA EXAMPLE - SUM
# ============================================================

arr = [10, 20, 30, 40]

total = sum(arr)

print(total)


# ============================================================
# 38. DSA EXAMPLE - ANY
# ============================================================

arr = [1, 3, 5, 7, 8]

has_even = any(x % 2 == 0 for x in arr)

print(has_even)


# ============================================================
# 39. DSA EXAMPLE - ALL
# ============================================================

arr = [2, 4, 6, 8]

all_even = all(x % 2 == 0 for x in arr)

print(all_even)


# ============================================================
# 40. IMPORTANT INTERVIEW QUESTIONS
# ============================================================

"""
Q1. What does range(5) produce?

0, 1, 2, 3, 4


Q2. Is the stop value of range() included?

NO.


Q3. What does enumerate() provide?

Index + value.


Q4. Why use enumerate() instead of range(len(arr))?

It directly provides both index and value and is
usually cleaner.


Q5. What does zip() do?

Combines elements from multiple iterables
position by position.


Q6. What happens if zip() inputs have different lengths?

Normally it stops at the shortest iterable.


Q7. What does ord('A') return?

65


Q8. What does chr(65) return?

'A'


Q9. What does id() return?

The identity of an object during its lifetime.


Q10. What does len() return?

The number of elements/characters in an object.


Q11. Difference between sort() and sorted()?

sort():
- list method
- modifies original list
- returns None

sorted():
- built-in function
- returns a new sorted list


Q12. What does any() do?

Returns True if at least one element is truthy.


Q13. What does all() do?

Returns True only if every element is truthy.


Q14. What does map() do?

Transforms elements using a function.


Q15. What does filter() do?

Keeps elements for which the condition is True.


Q16. What does input() return?

A string.


Q17. What is the difference between type() and
isinstance()?

type() gives the exact type.

isinstance() checks whether an object is an instance
of a specified type or compatible subclass.
"""


# ============================================================
# 41. QUICK DSA CHEAT SHEET
# ============================================================

"""
+----------------+--------------------------------------+
| FUNCTION       | MAIN USE                             |
+----------------+--------------------------------------+
| range()        | Generate number sequence             |
| enumerate()    | Index + value                        |
| zip()          | Combine iterables                   |
| ord()          | Character -> Unicode number         |
| chr()          | Number -> Character                 |
| id()           | Object identity                     |
| len()          | Number of elements                  |
| sum()          | Sum of elements                     |
| min()          | Minimum value                       |
| max()          | Maximum value                       |
| abs()          | Absolute value                      |
| round()        | Rounding                            |
| sorted()       | New sorted list                     |
| reversed()     | Reverse iterator                    |
| any()          | At least one True                   |
| all()          | Every value True                    |
| map()          | Transform elements                  |
| filter()       | Select elements                     |
| type()         | Check exact type                   |
| isinstance()   | Check type/subclass relationship    |
| input()        | User input                          |
| list()         | Convert to list                     |
| tuple()        | Convert to tuple                    |
| set()          | Convert to set/remove duplicates    |
| dict()         | Create dictionary                   |
+----------------+--------------------------------------+
"""


# ============================================================
# 42. MOST IMPORTANT FOR DSA
# ============================================================

"""
If you are learning these specifically for DSA,
prioritize them in this order:

VERY IMPORTANT:

1. range()
2. len()
3. enumerate()
4. zip()
5. ord()
6. min()
7. max()
8. sum()
9. sorted()
10. reversed()


IMPORTANT:

11. abs()
12. any()
13. all()
14. set()
15. dict()


NEXT LEVEL:

16. map()
17. filter()
18. lambda
19. chr()
20. id()


The most important ones will repeatedly appear in
coding problems.
"""


# ============================================================
#                         END
# ============================================================