# ============================================================
#              * OPERATOR IN PYTHON
#                UNPACKING + *args 
# ============================================================

"""
The * operator has different uses in Python.

In this file we will learn:

1. * with print()
2. Iterable unpacking
3. List unpacking
4. Tuple unpacking
5. String unpacking
6. Range unpacking
7. Function argument unpacking
8. Assignment unpacking
9. First + middle + last unpacking
10. Combining lists using *
11. *args
12. Difference between * and **
13. Dictionary unpacking using **
"""


# ============================================================
# 1. * WITH print()
# ============================================================

arr = [1, 2, 3, 4, 5]

# Without *
print(arr)

# Output:
# [1, 2, 3, 4, 5]


# With *
print(*arr)

# Output:
# 1 2 3 4 5


"""
IMPORTANT:

print(arr)

passes the entire list as ONE argument.

print(*arr)

unpacks the list and passes each element separately.

So:

print(*arr)

is conceptually similar to:

print(1, 2, 3, 4, 5)
"""


# ============================================================
# 2. HOW * UNPACKS A LIST
# ============================================================

arr = [10, 20, 30]

print(*arr)

# Conceptually:

print(10, 20, 30)


# ============================================================
# 3. * WITH sep
# ============================================================

arr = [1, 2, 3, 4, 5]

print(*arr, sep=", ")

# Output:
# 1, 2, 3, 4, 5


print(*arr, sep=" | ")

# Output:
# 1 | 2 | 3 | 4 | 5


print(*arr, sep=" -> ")

# Output:
# 1 -> 2 -> 3 -> 4 -> 5


# ============================================================
# 4. * WITH TUPLE
# ============================================================

numbers = (10, 20, 30, 40)

print(numbers)

# Output:
# (10, 20, 30, 40)


print(*numbers)

# Output:
# 10 20 30 40


"""
The tuple is unpacked into separate arguments.
"""


# ============================================================
# 5. * WITH STRING
# ============================================================

name = "Python"

print(name)

# Output:
# Python


print(*name)

# Output:
# P y t h o n


"""
A string is iterable.

Therefore:

*name

unpacks the string character by character.

Conceptually:

print("P", "y", "t", "h", "o", "n")
"""


# ============================================================
# 6. * WITH RANGE
# ============================================================

numbers = range(1, 6)

print(numbers)

# Output looks like:
# range(1, 6)


print(*numbers)

# Output:
# 1 2 3 4 5


# ============================================================
# 7. * WITH SET
# ============================================================

numbers = {10, 20, 30, 40}

print(*numbers)

"""
Note:

Sets are unordered collections.

Therefore, the output order of a set
should not be relied upon.
"""


# ============================================================
# 8. FUNCTION ARGUMENT UNPACKING
# ============================================================

def add(a, b, c):
    return a + b + c


numbers = [10, 20, 30]

result = add(*numbers)

print(result)

# Output:
# 60


"""
This:

add(*numbers)

is equivalent to:

add(10, 20, 30)
"""


# ============================================================
# 9. WITHOUT * IN FUNCTION
# ============================================================

def student(name, age, city):
    print(name)
    print(age)
    print(city)


data = ["Harshad", 21, "Latur"]

student(*data)

"""
This becomes:

student("Harshad", 21, "Latur")
"""


# ============================================================
# 10. ASSIGNMENT UNPACKING
# ============================================================

numbers = [10, 20, 30]

a, b, c = numbers

print(a)
print(b)
print(c)

"""
Output:

10
20
30
"""


# ============================================================
# 11. * DURING ASSIGNMENT
# ============================================================

numbers = [10, 20, 30, 40, 50]

a, *b = numbers

print(a)
print(b)

"""
Output:

10
[20, 30, 40, 50]

Here:

a -> first element

b -> remaining elements
"""


# ============================================================
# 12. * FOR REMAINING ELEMENTS
# ============================================================

numbers = [10, 20, 30, 40, 50]

*a, b = numbers

print(a)
print(b)

"""
Output:

[10, 20, 30, 40]
50

Here:

a -> all elements except last

b -> last element
"""


# ============================================================
# 13. FIRST + MIDDLE + LAST
# ============================================================

numbers = [10, 20, 30, 40, 50]

a, *b, c = numbers

print(a)
print(b)
print(c)

"""
Output:

10
[20, 30, 40]
50

Here:

a -> first element
b -> middle elements
c -> last element
"""


# ============================================================
# 14. * WITH A STRING DURING ASSIGNMENT
# ============================================================

name = "Python"

first, *middle, last = name

print(first)
print(middle)
print(last)

"""
Output:

P
['y', 't', 'h', 'o']
n
"""


# ============================================================
# 15. COMBINING TWO LISTS USING *
# ============================================================

arr1 = [1, 2, 3]

arr2 = [4, 5, 6]

result = [*arr1, *arr2]

print(result)

# Output:
# [1, 2, 3, 4, 5, 6]


"""
This is conceptually similar to:

result = [1, 2, 3, 4, 5, 6]
"""


# ============================================================
# 16. ADD ELEMENTS WHILE UNPACKING
# ============================================================

arr = [1, 2, 3]

result = [0, *arr, 4]

print(result)

# Output:
# [0, 1, 2, 3, 4]


# ============================================================
# 17. COMBINE MULTIPLE LISTS
# ============================================================

a = [1, 2]

b = [3, 4]

c = [5, 6]

result = [*a, *b, *c]

print(result)

# Output:
# [1, 2, 3, 4, 5, 6]


# ============================================================
# 18. *args
# ============================================================

"""
*args is used in functions when we don't know
how many positional arguments will be passed.
"""


def show_numbers(*args):

    print(args)


show_numbers(10, 20, 30)

show_numbers(1, 2, 3, 4, 5)


"""
Output:

(10, 20, 30)

(1, 2, 3, 4, 5)


IMPORTANT:

Inside the function:

args is a TUPLE.
"""


# ============================================================
# 19. *args WITH LOOP
# ============================================================

def print_numbers(*args):

    for number in args:

        print(number)


print_numbers(10, 20, 30, 40)


# ============================================================
# 20. *args FOR SUM
# ============================================================

def total(*numbers):

    result = 0

    for number in numbers:

        result += number

    return result


print(total(10, 20))

print(total(10, 20, 30))

print(total(1, 2, 3, 4, 5))


# ============================================================
# 21. *args AND LIST UNPACKING TOGETHER
# ============================================================

def total(*numbers):

    result = 0

    for number in numbers:

        result += number

    return result


arr = [10, 20, 30, 40]

print(total(*arr))


"""
Here:

arr = [10, 20, 30, 40]

total(*arr)

becomes:

total(10, 20, 30, 40)

Then *numbers collects them:

numbers = (10, 20, 30, 40)
"""


# ============================================================
# 22. *args WITH NORMAL PARAMETERS
# ============================================================

def student(name, *marks):

    print("Name:", name)

    print("Marks:", marks)


student("Harshad", 80, 85, 90)


"""
Output:

Name: Harshad
Marks: (80, 85, 90)
"""


# ============================================================
# 23. *args CAN ACCEPT ZERO ARGUMENTS
# ============================================================

def test(*args):

    print(args)


test()

# Output:
# ()


# ============================================================
# 24. *args CAN ACCEPT MANY ARGUMENTS
# ============================================================

def test(*args):

    print(args)


test(10)

test(10, 20)

test(10, 20, 30, 40, 50)


# ============================================================
# 25. * VS ** 
# ============================================================

"""
There are two important unpacking operators:

*  -> positional / iterable unpacking

** -> keyword / dictionary unpacking
"""


# ============================================================
# 26. DICTIONARY UNPACKING USING **
# ============================================================

data = {
    "name": "Harshad",
    "age": 21
}


def student(name, age):

    print("Name:", name)

    print("Age:", age)


student(**data)


"""
This:

student(**data)

is equivalent to:

student(
    name="Harshad",
    age=21
)
"""


# ============================================================
# 27. **kwargs
# ============================================================

"""
**kwargs collects keyword arguments into a dictionary.
"""


def student_info(**kwargs):

    print(kwargs)


student_info(
    name="Harshad",
    age=21,
    city="Latur"
)


"""
Output:

{
    'name': 'Harshad',
    'age': 21,
    'city': 'Latur'
}
"""


# ============================================================
# 28. *args VS **kwargs
# ============================================================

def example(*args, **kwargs):

    print("args:", args)

    print("kwargs:", kwargs)


example(
    10,
    20,
    30,
    name="Harshad",
    age=21
)


"""
args:

(10, 20, 30)


kwargs:

{
    'name': 'Harshad',
    'age': 21
}
"""


# ============================================================
# 29. * IN FUNCTION CALL VS *args IN DEFINITION
# ============================================================

"""
IMPORTANT DIFFERENCE:

When calling a function:

    function(*arr)

means:

    UNPACK

When defining a function:

    def function(*args):

means:

    COLLECT
"""


# ============================================================
# 30. DSA EXAMPLE - PRINT ARRAY
# ============================================================

arr = [10, 20, 30, 40, 50]

print(*arr)


# ============================================================
# 31. DSA EXAMPLE - PRINT REVERSE ARRAY
# ============================================================

arr = [10, 20, 30, 40, 50]

print(*arr[::-1])


# ============================================================
# 32. DSA EXAMPLE - PRINT WITH SEPARATOR
# ============================================================

arr = [10, 20, 30, 40, 50]

print(*arr, sep=" -> ")


# Output:
# 10 -> 20 -> 30 -> 40 -> 50


# ============================================================
# 33. DSA EXAMPLE - FIRST AND REST
# ============================================================

arr = [10, 20, 30, 40, 50]

first, *rest = arr

print("First:", first)

print("Rest:", rest)


# ============================================================
# 34. DSA EXAMPLE - LAST ELEMENT
# ============================================================

arr = [10, 20, 30, 40, 50]

*start, last = arr

print("Start:", start)

print("Last:", last)


# ============================================================
# 35. INTERVIEW QUESTIONS
# ============================================================

"""
Q1. What does * do in print(*arr)?

Answer:

It unpacks the elements of an iterable and passes
them as separate positional arguments.


Q2. What is:

arr = [1, 2, 3]

print(*arr)

equivalent to?

Answer:

print(1, 2, 3)


Q3. Does * modify the original list?

No.

It only unpacks the elements.


Q4. What is *args?

It collects multiple positional arguments into a tuple.


Q5. What is **kwargs?

It collects multiple keyword arguments into a dictionary.


Q6. What is the difference between:

function(*arr)

and:

def function(*args)


function(*arr):

UNPACKS


def function(*args):

COLLECTS


Q7. What does this do?

a, *b = [1, 2, 3, 4]

Answer:

a = 1

b = [2, 3, 4]


Q8. What does this do?

a, *b, c = [1, 2, 3, 4, 5]

Answer:

a = 1

b = [2, 3, 4]

c = 5


Q9. What does ** do?

It performs keyword/dictionary unpacking.


Q10. What is the type of args in *args?

tuple


Q11. What is the type of kwargs in **kwargs?

dict
"""


# ============================================================
# 36. QUICK REVISION
# ============================================================

"""
*arr
    ↓
UNPACK iterable


print(*arr)
    ↓
Print elements separately


function(*arr)
    ↓
Pass list elements as separate arguments


a, *b = arr
    ↓
First element + remaining elements


*a, b = arr
    ↓
All except last + last element


a, *b, c = arr
    ↓
First + middle + last


[*a, *b]
    ↓
Combine / unpack iterables


*args
    ↓
Collect positional arguments into a tuple


**data
    ↓
Unpack dictionary into keyword arguments


**kwargs
    ↓
Collect keyword arguments into a dictionary
"""

a, *b, c = [1, 2, 3, 4, 5]

# *arr       → UNPACK
# *args      → COLLECT
# **dict     → UNPACK
# **kwargs   → COLLECT
# ============================================================
#                         END
# ============================================================

