# ============================================================
#                     TUPLES IN PYTHON
# ============================================================

"""
A tuple is an ordered, immutable collection in Python.

Example:

    numbers = (10, 20, 30, 40)

Important properties of tuples:

    1. Ordered
    2. Immutable
    3. Allows duplicate values
    4. Allows different data types
    5. Supports indexing
    6. Supports slicing
    7. Iterable
    8. Can be nested
    9. Can contain mutable objects
   10. Can be used as dictionary keys if all elements are hashable

Tuple syntax:

    (value1, value2, value3)
"""


# ============================================================
# 1. CREATING A TUPLE
# ============================================================

numbers = (10, 20, 30, 40, 50)

print(numbers)
print(type(numbers))


# ============================================================
# 2. EMPTY TUPLE
# ============================================================

empty_tuple = ()

print(empty_tuple)
print(type(empty_tuple))


# ============================================================
# 3. TUPLE WITH DIFFERENT DATA TYPES
# ============================================================

data = (
    "Harshad",
    21,
    85.5,
    True,
    10 + 5j
)

print(data)


# ============================================================
# 4. TUPLE ALLOWS DUPLICATES
# ============================================================

numbers = (10, 20, 10, 30, 20, 10)

print(numbers)


# ============================================================
# 5. TUPLE IS ORDERED
# ============================================================

numbers = (10, 20, 30, 40)

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])


# ============================================================
# 6. SINGLE ELEMENT TUPLE
# ============================================================

"""
IMPORTANT:

This is NOT a tuple:

    x = (10)

It is an integer.

To create a single-element tuple, use a comma:

    x = (10,)
"""

x = (10)

print(x)
print(type(x))


x = (10,)

print(x)
print(type(x))


# ============================================================
# 7. SINGLE STRING TUPLE
# ============================================================

name = ("Harshad",)

print(name)
print(type(name))


# ============================================================
# 8. TUPLE WITHOUT PARENTHESES
# ============================================================

"""
Python supports tuple packing.

Parentheses are not always required.
"""

numbers = 10, 20, 30, 40

print(numbers)
print(type(numbers))


# ============================================================
# 9. TUPLE CONSTRUCTOR
# ============================================================

numbers = tuple([10, 20, 30, 40])

print(numbers)
print(type(numbers))


# ============================================================
# 10. CONVERT LIST TO TUPLE
# ============================================================

numbers_list = [10, 20, 30, 40]

numbers_tuple = tuple(numbers_list)

print(numbers_tuple)


# ============================================================
# 11. CONVERT STRING TO TUPLE
# ============================================================

name = "Harshad"

result = tuple(name)

print(result)


"""
Output:

('H', 'a', 'r', 's', 'h', 'a', 'd')
"""


# ============================================================
# 12. CONVERT RANGE TO TUPLE
# ============================================================

numbers = tuple(range(1, 6))

print(numbers)


# ============================================================
# 13. TUPLE INDEXING
# ============================================================

numbers = (10, 20, 30, 40, 50)

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])


# ============================================================
# 14. NEGATIVE INDEXING
# ============================================================

numbers = (10, 20, 30, 40, 50)

print(numbers[-1])
print(numbers[-2])
print(numbers[-3])


"""
Negative indexing:

    -1 -> last element
    -2 -> second last
    -3 -> third last
"""


# ============================================================
# 15. INDEXERROR
# ============================================================

"""
numbers = (10, 20, 30)

print(numbers[10])

This produces:

IndexError

because index 10 does not exist.
"""


# ============================================================
# 16. TUPLE SLICING
# ============================================================

numbers = (10, 20, 30, 40, 50, 60)

print(numbers[1:4])
print(numbers[:4])
print(numbers[2:])
print(numbers[:])
print(numbers[::2])
print(numbers[::3])


# ============================================================
# 17. REVERSE A TUPLE
# ============================================================

numbers = (10, 20, 30, 40, 50)

print(numbers[::-1])


# ============================================================
# 18. NEGATIVE SLICING
# ============================================================

numbers = (10, 20, 30, 40, 50)

print(numbers[-4:-1])
print(numbers[-1:-4:-1])


# ============================================================
# 19. TUPLE IS IMMUTABLE
# ============================================================

"""
Once a tuple is created, its elements cannot be changed.

Example:

    numbers = (10, 20, 30)

    numbers[0] = 100

This produces:

TypeError


Tuple does not support item assignment.
"""


# ============================================================
# 20. WHY IMMUTABILITY?
# ============================================================

"""
Immutable means:

    The tuple itself cannot be modified after creation.

You cannot directly:

    - Change an element
    - Add an element
    - Remove an element

This makes tuples useful when data should remain fixed.
"""


# ============================================================
# 21. TUPLE VS LIST
# ============================================================

"""
LIST:

    numbers = [10, 20, 30]

    Mutable
    Can be modified


TUPLE:

    numbers = (10, 20, 30)

    Immutable
    Cannot be modified


Example:

list_data = [10, 20, 30]
list_data[0] = 100

tuple_data = (10, 20, 30)
tuple_data[0] = 100   # TypeError
"""


# ============================================================
# 22. TUPLE CONCATENATION
# ============================================================

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print(result)


# ============================================================
# 23. TUPLE REPETITION
# ============================================================

numbers = (1, 2, 3)

print(numbers * 3)


"""
Output:

(1, 2, 3, 1, 2, 3, 1, 2, 3)
"""


# ============================================================
# 24. TUPLE MEMBERSHIP
# ============================================================

numbers = (10, 20, 30, 40)

print(20 in numbers)
print(50 in numbers)

print(20 not in numbers)
print(50 not in numbers)


# ============================================================
# 25. len()
# ============================================================

numbers = (10, 20, 30, 40)

print(len(numbers))


# ============================================================
# 26. min()
# ============================================================

numbers = (10, 20, 30, 40)

print(min(numbers))


# ============================================================
# 27. max()
# ============================================================

numbers = (10, 20, 30, 40)

print(max(numbers))


# ============================================================
# 28. sum()
# ============================================================

numbers = (10, 20, 30, 40)

print(sum(numbers))


# ============================================================
# 29. sorted()
# ============================================================

"""
sorted() returns a LIST, not a tuple.
"""

numbers = (50, 20, 40, 10, 30)

result = sorted(numbers)

print(result)
print(type(result))


# ============================================================
# 30. SORTED IN DESCENDING ORDER
# ============================================================

numbers = (50, 20, 40, 10, 30)

result = sorted(numbers, reverse=True)

print(result)


# ============================================================
# 31. tuple.index()
# ============================================================

numbers = (10, 20, 30, 40, 30)

print(numbers.index(30))


"""
index() returns the first matching index.
"""


# ============================================================
# 32. tuple.index() WITH START
# ============================================================

numbers = (10, 20, 30, 40, 30)

print(numbers.index(30, 3))


"""
Search for 30 starting from index 3.
"""


# ============================================================
# 33. tuple.count()
# ============================================================

numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))
print(numbers.count(30))
print(numbers.count(100))


"""
If element does not exist:

count() returns 0.
"""


# ============================================================
# 34. TUPLE METHODS
# ============================================================

"""
Tuple has only TWO built-in methods:

    1. count()
    2. index()

Because tuples are immutable, methods such as:

    append()
    remove()
    insert()
    pop()
    sort()
    reverse()
    clear()
    extend()

are NOT available on tuples.
"""


# ============================================================
# 35. LOOP THROUGH TUPLE
# ============================================================

numbers = (10, 20, 30, 40)

for number in numbers:
    print(number)


# ============================================================
# 36. LOOP USING INDEX
# ============================================================

numbers = (10, 20, 30, 40)

for i in range(len(numbers)):
    print(numbers[i])


# ============================================================
# 37. ENUMERATE WITH TUPLE
# ============================================================

students = ("Harshad", "Rahul", "Sanjay")

for index, student in enumerate(students):
    print(index, student)


# ============================================================
# 38. ENUMERATE WITH START
# ============================================================

students = ("Harshad", "Rahul", "Sanjay")

for index, student in enumerate(students, start=1):
    print(index, student)


# ============================================================
# 39. TUPLE UNPACKING
# ============================================================

student = ("Harshad", 21, 85.5)

name, age, percentage = student

print(name)
print(age)
print(percentage)


"""
The number of variables must normally match the number
of tuple elements.
"""


# ============================================================
# 40. UNPACKING ERROR
# ============================================================

"""
student = ("Harshad", 21, 85.5)

name, age = student

This produces:

ValueError

because there are 3 values but only 2 variables.
"""


# ============================================================
# 41. STAR / EXTENDED UNPACKING
# ============================================================

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)
print(middle)
print(last)


"""
Output:

first  -> 10
middle -> [20, 30, 40]
last   -> 50


IMPORTANT:

The starred variable becomes a LIST.
"""


# ============================================================
# 42. STAR UNPACKING AT BEGINNING
# ============================================================

numbers = (10, 20, 30, 40, 50)

*start, last = numbers

print(start)
print(last)


# ============================================================
# 43. STAR UNPACKING AT END
# ============================================================

numbers = (10, 20, 30, 40, 50)

first, *remaining = numbers

print(first)
print(remaining)


# ============================================================
# 44. SWAPPING VARIABLES
# ============================================================

a = 10
b = 20

a, b = b, a

print(a)
print(b)


"""
Python internally uses tuple packing/unpacking.

Conceptually:

    a, b = (b, a)
"""


# ============================================================
# 45. TUPLE PACKING
# ============================================================

"""
Packing means putting multiple values into one tuple.
"""

student = "Harshad", 21, 85.5

print(student)


# ============================================================
# 46. PACKING + UNPACKING
# ============================================================

student = "Harshad", 21, 85.5

name, age, marks = student

print(name)
print(age)
print(marks)


# ============================================================
# 47. NESTED TUPLE
# ============================================================

data = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(data)


# ============================================================
# 48. ACCESS NESTED TUPLE
# ============================================================

data = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(data[0])
print(data[0][0])
print(data[1][2])
print(data[2][1])


# ============================================================
# 49. LOOP THROUGH NESTED TUPLE
# ============================================================

matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

for row in matrix:
    for value in row:
        print(value, end=" ")

    print()


# ============================================================
# 50. TUPLE CONTAINING LIST
# ============================================================

"""
A tuple can contain a mutable object such as a list.

Example:
"""

data = (10, 20, [30, 40])

print(data)


# ============================================================
# 51. MUTABLE OBJECT INSIDE IMMUTABLE TUPLE
# ============================================================

data = (10, 20, [30, 40])

data[2].append(50)

print(data)


"""
This works!

Why?

The tuple itself has not changed.

The LIST inside the tuple has changed.

The tuple still points to the same list object.
"""


# ============================================================
# 52. IMPORTANT INTERVIEW CONCEPT
# ============================================================

"""
Tuple immutability does NOT mean that every object inside
the tuple is immutable.

Example:

    data = (1, 2, [3, 4])

The tuple structure is immutable.

But the list inside it is mutable.
"""


# ============================================================
# 53. TUPLE AND HASHABILITY
# ============================================================

"""
A tuple can be hashable IF all of its elements are hashable.

Example:

    numbers = (1, 2, 3)

This tuple can be used as a dictionary key.

But:

    data = (1, 2, [3, 4])

cannot be used as a dictionary key because list is
unhashable.
"""


# ============================================================
# 54. TUPLE AS DICTIONARY KEY
# ============================================================

location = {
    (18.52, 73.85): "Pune"
}

print(location[(18.52, 73.85)])


# ============================================================
# 55. TUPLE AS SET ELEMENT
# ============================================================

data = {
    (1, 2),
    (3, 4),
    (5, 6)
}

print(data)


# ============================================================
# 56. UNHASHABLE TUPLE
# ============================================================

"""
This would produce:

TypeError: unhashable type: 'list'

because the tuple contains a list.
"""


# ============================================================
# 57. TUPLE COMPARISON
# ============================================================

"""
Tuples can be compared.

Python compares elements from left to right.
"""

print((1, 2) == (1, 2))
print((1, 2) == (1, 3))

print((1, 2) < (1, 3))


# ============================================================
# 58. LEXICOGRAPHIC COMPARISON
# ============================================================

"""
Tuple comparison works similarly to dictionary ordering
in a dictionary.

Example:

    (1, 2) < (1, 3)

First elements:

    1 == 1

Then compare:

    2 < 3

Therefore:

    True
"""


# ============================================================
# 59. TUPLE WITH DIFFERENT TYPES
# ============================================================

"""
Be careful when comparing incompatible types.

For example:

    (1, 2) < ("a", "b")

may produce TypeError because Python cannot order int
and str directly.
"""


# ============================================================
# 60. TUPLE MEMORY / PERFORMANCE IDEA
# ============================================================

"""
Tuples are immutable, so they can sometimes be more
memory-efficient than lists for fixed data.

Tuples can also be slightly faster for some operations.

But:

Do NOT choose tuple just because it is "faster".

Choose based on whether the data should be mutable.

Use LIST when:

    data needs modification.

Use TUPLE when:

    data represents a fixed collection.
"""


# ============================================================
# 61. TUPLE VS LIST
# ============================================================

"""
+--------------------+------------------+------------------+
| Feature            | List             | Tuple            |
+--------------------+------------------+------------------+
| Syntax             | [1, 2, 3]        | (1, 2, 3)        |
| Mutable            | Yes              | No               |
| Ordered            | Yes              | Yes              |
| Duplicates         | Yes              | Yes              |
| Indexing           | Yes              | Yes              |
| Slicing            | Yes              | Yes              |
| Iterable           | Yes              | Yes              |
| Hashable           | No               | Sometimes        |
| Methods            | Many             | 2                |
| Dictionary key     | No               | Sometimes        |
+--------------------+------------------+------------------+
"""


# ============================================================
# 62. LIST METHODS VS TUPLE METHODS
# ============================================================

"""
LIST:

    append()
    extend()
    insert()
    remove()
    pop()
    clear()
    sort()
    reverse()
    copy()
    count()
    index()


TUPLE:

    count()
    index()


Why fewer tuple methods?

Because tuples cannot be modified.
"""


# ============================================================
# 63. tuple() CONSTRUCTOR
# ============================================================

"""
tuple() creates a tuple from an iterable.

Examples:

    tuple(list)
    tuple(string)
    tuple(range)
    tuple(set)
"""


print(tuple([1, 2, 3]))
print(tuple("ABC"))
print(tuple(range(5)))


# ============================================================
# 64. ITERABLE AND TUPLE
# ============================================================

"""
An iterable is something that can be iterated over.

Examples:

    list
    tuple
    string
    set
    dictionary
    range
"""


# ============================================================
# 65. TUPLE FROM SET
# ============================================================

numbers = {10, 20, 30}

result = tuple(numbers)

print(result)


"""
Remember:

Set is unordered.

Therefore, do not rely on a particular order when converting
a set to a tuple.
"""


# ============================================================
# 66. TUPLE FROM DICTIONARY
# ============================================================

student = {
    "name": "Harshad",
    "age": 21
}

result = tuple(student)

print(result)


"""
tuple(dictionary)

converts the dictionary's keys into a tuple.
"""


# ============================================================
# 67. TUPLE FROM DICTIONARY KEYS
# ============================================================

student = {
    "name": "Harshad",
    "age": 21
}

print(tuple(student.keys()))


# ============================================================
# 68. TUPLE FROM DICTIONARY VALUES
# ============================================================

print(tuple(student.values()))


# ============================================================
# 69. TUPLE FROM DICTIONARY ITEMS
# ============================================================

print(tuple(student.items()))


"""
Output is approximately:

(
    ('name', 'Harshad'),
    ('age', 21)
)
"""


# ============================================================
# 70. ZIP RETURNS AN ITERABLE OF TUPLES
# ============================================================

names = ("Harshad", "Rahul", "Sanjay")
marks = (90, 85, 88)

result = zip(names, marks)

print(tuple(result))


"""
zip() commonly produces pairs as tuples.

Example:

    ('Harshad', 90)
    ('Rahul', 85)
    ('Sanjay', 88)
"""


# ============================================================
# 71. TUPLE WITH ZIP
# ============================================================

names = ["Harshad", "Rahul", "Sanjay"]
marks = [90, 85, 88]

for name, mark in zip(names, marks):
    print(name, mark)


# ============================================================
# 72. TUPLE IN DSA
# ============================================================

"""
Tuples are VERY useful in DSA.

Common use cases:

    1. Coordinate pairs
    2. Graph edges
    3. Priority queues
    4. Sorting by multiple values
    5. Dictionary keys
    6. Returning multiple values
    7. Storing fixed pairs
"""


# ============================================================
# 73. COORDINATES
# ============================================================

point = (10, 20)

x, y = point

print(x)
print(y)


# ============================================================
# 74. GRAPH EDGE
# ============================================================

edge = (1, 2)

print(edge)


"""
Could represent:

    Node 1 ---- Node 2
"""


# ============================================================
# 75. WEIGHTED GRAPH EDGE
# ============================================================

edge = (1, 2, 10)

"""
Could represent:

    source = 1
    destination = 2
    weight = 10
"""


source, destination, weight = edge

print(source)
print(destination)
print(weight)


# ============================================================
# 76. RETURN MULTIPLE VALUES
# ============================================================

def calculate(a, b):
    return a + b, a - b


result = calculate(10, 5)

print(result)
print(type(result))


"""
Python actually returns a tuple:

    (15, 5)
"""


# ============================================================
# 77. UNPACK RETURN VALUE
# ============================================================

addition, subtraction = calculate(10, 5)

print(addition)
print(subtraction)


# ============================================================
# 78. SORTING TUPLES
# ============================================================

students = (
    ("Harshad", 85),
    ("Rahul", 92),
    ("Sanjay", 78)
)

result = sorted(students, key=lambda student: student[1])

print(result)


# ============================================================
# 79. SORT DESCENDING
# ============================================================

students = (
    ("Harshad", 85),
    ("Rahul", 92),
    ("Sanjay", 78)
)

result = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print(result)


# ============================================================
# 80. TUPLES IN HEAP / PRIORITY QUEUE
# ============================================================

"""
Python's heapq commonly works with tuples.

Example:

    (priority, value)

The smallest priority comes first.
"""

import heapq

heap = []

heapq.heappush(heap, (3, "Task C"))
heapq.heappush(heap, (1, "Task A"))
heapq.heappush(heap, (2, "Task B"))

print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))


# ============================================================
# 81. TUPLE AND for LOOP
# ============================================================

students = (
    ("Harshad", 90),
    ("Rahul", 85),
    ("Sanjay", 88)
)

for name, marks in students:
    print(f"{name}: {marks}")


# ============================================================
# 82. TUPLE WITH enumerate()
# ============================================================

students = ("Harshad", "Rahul", "Sanjay")

for index, name in enumerate(students):
    print(index, name)


# ============================================================
# 83. TUPLE UNPACKING IN for LOOP
# ============================================================

data = (
    (1, 10),
    (2, 20),
    (3, 30)
)

for key, value in data:
    print(key, value)


# ============================================================
# 84. TUPLE COPY
# ============================================================

"""
Since tuples are immutable, you generally don't need a
copy() method like lists have.

If you assign:

    tuple2 = tuple1

both names refer to the same tuple object.

Because the tuple is immutable, this is usually not
a problem.
"""


tuple1 = (1, 2, 3)
tuple2 = tuple1

print(tuple1 is tuple2)


# ============================================================
# 85. TUPLE IDENTITY
# ============================================================

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)

print(tuple1 == tuple2)

"""
== checks VALUE equality.

is checks OBJECT IDENTITY.

Do not use `is` to compare tuple values.
"""


# ============================================================
# 86. TUPLE MUTABILITY INTERVIEW TRICK
# ============================================================

data = ([1, 2], [3, 4])

data[0].append(100)

print(data)


"""
This is valid.

The tuple cannot replace data[0] with another object:

    data[0] = [10, 20]

would fail.

But the existing list object can itself be modified.
"""


# ============================================================
# 87. TUPLE MEMORY CONCEPT
# ============================================================

"""
A tuple stores references to objects.

For example:

    data = (10, [20, 30])

The tuple contains references to:

    10
    list object [20, 30]

The tuple structure is immutable.

The list object remains mutable.
"""


# ============================================================
# 88. COMMON MISTAKE - SINGLE ELEMENT
# ============================================================

# NOT a tuple:
x = (10)

print(type(x))


# Tuple:
x = (10,)

print(type(x))


# ============================================================
# 89. COMMON MISTAKE - tuple() WITH INTEGER
# ============================================================

"""
This does NOT work:

    tuple(10)

because int is not iterable.

tuple() expects an iterable.

Examples that work:

    tuple([1, 2, 3])
    tuple("ABC")
    tuple(range(5))
"""


# ============================================================
# 90. COMMON MISTAKE - MODIFYING TUPLE
# ============================================================

"""
numbers = (1, 2, 3)

numbers.append(4)

ERROR:

AttributeError

Tuple has no append() method.
"""


# ============================================================
# 91. HOW TO "MODIFY" A TUPLE
# ============================================================

"""
You cannot directly modify a tuple.

But you can create a new tuple.
"""


numbers = (1, 2, 3)

numbers = numbers + (4,)

print(numbers)


# ============================================================
# 92. TUPLE TO LIST TO TUPLE
# ============================================================

"""
If you really need to modify tuple data:

    tuple
      ↓
    list
      ↓
    modify
      ↓
    tuple
"""


numbers = (1, 2, 3)

temp = list(numbers)

temp.append(4)

numbers = tuple(temp)

print(numbers)


# ============================================================
# 93. TUPLE COMPREHENSION - IMPORTANT TRICK
# ============================================================

"""
Python does NOT have tuple comprehension.

This:

    (x * x for x in range(5))

is NOT a tuple.

It is a generator expression.
"""


result = (x * x for x in range(5))

print(type(result))


# ============================================================
# 94. CREATE TUPLE USING GENERATOR
# ============================================================

result = tuple(x * x for x in range(5))

print(result)
print(type(result))


# ============================================================
# 95. TUPLE GENERATOR INTERVIEW QUESTION
# ============================================================

"""
Question:

Is this a tuple?

    (x for x in range(5))

Answer:

NO.

It is a generator expression.

To create a tuple:

    tuple(x for x in range(5))
"""


# ============================================================
# 96. TUPLE AND MEMORY
# ============================================================

"""
Tuple:

    (1, 2, 3)

List:

    [1, 2, 3]

The exact memory difference depends on Python implementation
and contents, but tuples generally have lower per-element
overhead than lists because tuples are fixed-size.

Do not rely on exact memory sizes without measuring.
"""


# ============================================================
# 97. GET MEMORY SIZE
# ============================================================

import sys

numbers_list = [1, 2, 3, 4, 5]
numbers_tuple = (1, 2, 3, 4, 5)

print(sys.getsizeof(numbers_list))
print(sys.getsizeof(numbers_tuple))


# ============================================================
# 98. TUPLE AS FUNCTION ARGUMENT
# ============================================================

def print_student(student):
    name, age, marks = student

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Marks: {marks}")


student = ("Harshad", 21, 85)

print_student(student)


# ============================================================
# 99. *args USES TUPLE
# ============================================================

def add_numbers(*args):
    print(args)
    print(type(args))

    return sum(args)


print(add_numbers(10, 20, 30, 40))


"""
IMPORTANT INTERVIEW POINT:

Inside a function:

    *args

collects positional arguments into a TUPLE.
"""


# ============================================================
# 100. *args EXAMPLE
# ============================================================

def calculate_sum(*numbers):
    return sum(numbers)


print(calculate_sum(10, 20))
print(calculate_sum(10, 20, 30))
print(calculate_sum(10, 20, 30, 40))


# ============================================================
# 101. TUPLE UNPACKING WITH *
# ============================================================

numbers = (1, 2, 3)

print(*numbers)


"""
This UNPACKS the tuple into separate arguments.

Equivalent conceptually to:

    print(1, 2, 3)
"""


# ============================================================
# 102. TUPLE + * IN FUNCTION
# ============================================================

numbers = (10, 20, 30)

print(*numbers, sep=" | ")


# ============================================================
# 103. TUPLE AND zip()
# ============================================================

names = ("Harshad", "Rahul", "Sanjay")
marks = (90, 85, 88)

pairs = tuple(zip(names, marks))

print(pairs)


# ============================================================
# 104. TUPLE AND map()
# ============================================================

numbers = (1, 2, 3, 4)

result = tuple(map(lambda x: x * x, numbers))

print(result)


# ============================================================
# 105. TUPLE AND filter()
# ============================================================

numbers = (1, 2, 3, 4, 5, 6)

result = tuple(filter(lambda x: x % 2 == 0, numbers))

print(result)


# ============================================================
# 106. TUPLE AND any()
# ============================================================

numbers = (1, 3, 5, 8)

print(any(x % 2 == 0 for x in numbers))


# ============================================================
# 107. TUPLE AND all()
# ============================================================

numbers = (2, 4, 6, 8)

print(all(x % 2 == 0 for x in numbers))


# ============================================================
# 108. TUPLE AND sum()
# ============================================================

numbers = (10, 20, 30)

print(sum(numbers))


# ============================================================
# 109. TUPLE AND max/min
# ============================================================

numbers = (10, 50, 20, 40, 30)

print(max(numbers))
print(min(numbers))


# ============================================================
# 110. TUPLE AND reversed()
# ============================================================

numbers = (10, 20, 30, 40)

result = reversed(numbers)

print(tuple(result))


"""
reversed() returns an iterator.

Convert it to tuple if you need a tuple.
"""


# ============================================================
# 111. TUPLE AND sorted()
# ============================================================

numbers = (50, 10, 40, 20, 30)

result = sorted(numbers)

print(result)
print(type(result))


"""
Remember:

sorted(tuple)

returns LIST.
"""


# ============================================================
# 112. TUPLE AND SORTED + TUPLE
# ============================================================

numbers = (50, 10, 40, 20, 30)

result = tuple(sorted(numbers))

print(result)


# ============================================================
# 113. TUPLE WITH MIXED NESTING
# ============================================================

data = (
    10,
    [20, 30],
    {
        "name": "Harshad"
    },
    (40, 50)
)

print(data)


# ============================================================
# 114. TUPLE AS RECORD
# ============================================================

"""
A tuple can represent a fixed record:

    (name, age, salary)
"""

employee = ("Harshad", 21, 50000)

name, age, salary = employee

print(name)
print(age)
print(salary)


# ============================================================
# 115. NAMEDTUPLE
# ============================================================

"""
Python also provides collections.namedtuple.

It creates tuple-like objects where fields can be accessed
by name as well as index.
"""

from collections import namedtuple

Student = namedtuple(
    "Student",
    ["name", "age", "marks"]
)

student = Student("Harshad", 21, 85)

print(student)
print(student.name)
print(student.age)
print(student.marks)
print(student[0])


# ============================================================
# 116. TUPLE VS NAMEDTUPLE
# ============================================================

"""
Normal tuple:

    student = ("Harshad", 21, 85)

Access:

    student[0]


Namedtuple:

    student.name

Namedtuple is useful when tuple positions have meaningful
names.
"""


# ============================================================
# 117. TUPLE AND DSA - COORDINATE
# ============================================================

point = (3, 5)

x, y = point

print(x, y)


# ============================================================
# 118. TUPLE AND DSA - MATRIX POSITION
# ============================================================

row = 2
column = 3

position = (row, column)

print(position)


# ============================================================
# 119. TUPLE AND DSA - GRAPH
# ============================================================

edges = [
    (0, 1),
    (1, 2),
    (2, 3)
]

for source, destination in edges:
    print(source, destination)


# ============================================================
# 120. TUPLE AND DSA - FREQUENCY
# ============================================================

frequency = {
    ("A", 1): 10,
    ("B", 2): 20
}

print(frequency)


# ============================================================
# 121. TUPLE AND DSA - SORTING
# ============================================================

data = [
    ("A", 30),
    ("B", 10),
    ("C", 20)
]

data.sort(key=lambda x: x[1])

print(data)


# ============================================================
# 122. TUPLE AND DSA - PRIORITY QUEUE
# ============================================================

import heapq

heap = []

heapq.heappush(heap, (2, "B"))
heapq.heappush(heap, (1, "A"))
heapq.heappush(heap, (3, "C"))

while heap:
    priority, value = heapq.heappop(heap)
    print(priority, value)


# ============================================================
# 123. TUPLE AND DSA - BFS / DFS
# ============================================================

"""
Coordinates and graph edges are frequently represented
using tuples.

Example:

    (row, column)

or:

    (node, neighbor)
"""


# ============================================================
# 124. IMPORTANT TUPLE INTERVIEW QUESTIONS
# ============================================================

"""
Q1. What is a tuple?

ANSWER:

A tuple is an ordered and immutable collection in Python.


Q2. How do you create a tuple?

ANSWER:

    numbers = (1, 2, 3)


Q3. How do you create a single-element tuple?

ANSWER:

Use a trailing comma:

    (10,)

Not:

    (10)


Q4. Are tuples mutable?

ANSWER:

No. Tuples are immutable.


Q5. Can tuples contain mutable objects?

ANSWER:

Yes.

Example:

    data = (1, [2, 3])


Q6. Can a tuple be used as a dictionary key?

ANSWER:

Yes, if all elements inside the tuple are hashable.


Q7. Why can a tuple containing a list not be a dictionary key?

ANSWER:

Because lists are unhashable.


Q8. How many methods does a tuple have?

ANSWER:

Two commonly exposed tuple-specific methods:

    count()
    index()


Q9. Difference between list and tuple?

ANSWER:

List is mutable.

Tuple is immutable.


Q10. Can tuples contain duplicate values?

ANSWER:

Yes.


Q11. Are tuples ordered?

ANSWER:

Yes.


Q12. Does tuple support indexing?

ANSWER:

Yes.


Q13. Does tuple support slicing?

ANSWER:

Yes.


Q14. Can we append to a tuple?

ANSWER:

No.


Q15. Can we remove an element from a tuple?

ANSWER:

No.


Q16. What does tuple() do?

ANSWER:

It creates a tuple from an iterable.


Q17. What is tuple unpacking?

ANSWER:

Assigning tuple elements to multiple variables.

Example:

    a, b, c = (10, 20, 30)


Q18. What is tuple packing?

ANSWER:

Combining multiple values into a tuple.

Example:

    data = 10, 20, 30


Q19. What does *args store?

ANSWER:

Positional arguments are collected into a tuple.


Q20. Is this a tuple?

    (x for x in range(5))

ANSWER:

No.

It is a generator expression.


Q21. What does sorted(tuple) return?

ANSWER:

A list.


Q22. What does tuple(sorted(tuple)) return?

ANSWER:

A tuple.


Q23. Can tuple values be changed?

ANSWER:

No, but mutable objects contained inside the tuple can
still be modified.


Q24. Why are tuples useful in DSA?

ANSWER:

They are useful for:

    - Coordinates
    - Graph edges
    - Priority queues
    - Dictionary keys
    - Multiple return values
    - Sorting records
    - Fixed data
"""


# ============================================================
# 125. COMMON INTERVIEW OUTPUT QUESTIONS
# ============================================================

"""
Question 1:

x = (10)

What is type(x)?

Answer:

<class 'int'>


Question 2:

x = (10,)

What is type(x)?

Answer:

<class 'tuple'>


Question 3:

x = (1, 2, 3)

x[0] = 100

Answer:

TypeError


Question 4:

x = (1, 2, [3, 4])

x[2].append(5)

Answer:

Works.

Result:

(1, 2, [3, 4, 5])


Question 5:

x = (1, 2, 3)

print(x * 2)

Answer:

(1, 2, 3, 1, 2, 3)


Question 6:

x = (10, 20, 30)

a, b, c = x

Answer:

a = 10
b = 20
c = 30


Question 7:

x = (10, 20, 30, 40, 50)

a, *b, c = x

Answer:

a = 10
b = [20, 30, 40]
c = 50
"""


# ============================================================
# 126. QUICK REVISION
# ============================================================

"""
TUPLE CHEAT SHEET
=================

Create:

    numbers = (1, 2, 3)


Single element:

    numbers = (1,)


Indexing:

    numbers[0]


Negative indexing:

    numbers[-1]


Slicing:

    numbers[1:4]


Reverse:

    numbers[::-1]


Length:

    len(numbers)


Count:

    numbers.count(2)


Index:

    numbers.index(2)


Membership:

    2 in numbers


Concatenation:

    (1, 2) + (3, 4)


Repetition:

    (1, 2) * 3


Unpacking:

    a, b, c = (1, 2, 3)


Extended unpacking:

    a, *b, c = (1, 2, 3, 4)


Conversion:

    tuple([1, 2, 3])


Sort:

    sorted(numbers)        # LIST


Tuple sort:

    tuple(sorted(numbers))


Dictionary key:

    {(1, 2): "value"}


Methods:

    count()
    index()


Immutable:

    YES


Ordered:

    YES


Duplicates:

    YES


Indexing:

    YES


Slicing:

    YES


Hashable:

    Sometimes


DSA:

    VERY IMPORTANT
"""


# ============================================================
# 127. MOST IMPORTANT THINGS FOR YOUR DSA
# ============================================================

"""
Since you are preparing for DSA, prioritize these tuple
concepts:

    ★★★★★  Indexing
    ★★★★★  Slicing
    ★★★★★  Unpacking
    ★★★★★  Tuple inside dictionary/set
    ★★★★★  Tuple sorting with key
    ★★★★★  zip()
    ★★★★★  enumerate()
    ★★★★★  *args
    ★★★★★  Coordinates
    ★★★★★  Graph edges
    ★★★★★  Heap / Priority Queue
    ★★★★☆  Immutability
    ★★★★☆  Hashability
    ★★★★☆  Nested tuples
    ★★★☆☆  namedtuple
"""


print("\n================================================")
print("            TUPLE REVISION COMPLETE")
print("================================================")