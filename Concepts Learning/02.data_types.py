# ============================================================
#                    PYTHON DATA TYPES
# ============================================================

"""
A data type tells Python what kind of value a variable contains.

Python is dynamically typed.

Example:

x = 10

Later we can do:

x = "Hello"

Python allows this because the type belongs to the VALUE,
not permanently to the variable.
"""


# ============================================================
# 1. STRING (str)
# ============================================================

name = "Harshad"

print(name)
print(type(name))

# Output:
# Harshad
# <class 'str'>


# String can contain letters, numbers and special characters.

city = "Latur"
college = "CSMSS"
message = "Python123"


# ============================================================
# 2. INTEGER (int)
# ============================================================

age = 21

print(age)
print(type(age))

# Output:
# 21
# <class 'int'>


# Integers can be positive, negative or zero.

x = 100
y = -50
z = 0

print(type(x))
print(type(y))
print(type(z))


# ============================================================
# 3. FLOAT (float)
# ============================================================

percentage = 85.5

print(percentage)
print(type(percentage))

# Output:
# 85.5
# <class 'float'>


# Floating-point numbers contain decimal values.

price = 99.99
temperature = -5.5


# ============================================================
# 4. BOOLEAN (bool)
# ============================================================

is_student = True

print(is_student)
print(type(is_student))

# Output:
# True
# <class 'bool'>


# Boolean has only two values:

# True
# False

is_logged_in = True
is_admin = False


# ============================================================
# 5. BOOLEAN IS A SUBCLASS OF INTEGER
# ============================================================

"""
IMPORTANT INTERVIEW QUESTION:

In Python:

bool is a subclass of int.

Therefore:

True behaves like 1
False behaves like 0
"""

print(True + True)
print(True + False)
print(False + False)

# Output:
# 2
# 1
# 0


print(isinstance(True, int))

# Output:
# True


# ============================================================
# 6. LIST (list)
# ============================================================

marks = [85, 90, 78]

print(marks)
print(type(marks))

# Output:
# [85, 90, 78]
# <class 'list'>


"""
List:

- Ordered
- Mutable
- Allows duplicate values
- Allows different data types
- Supports indexing
- Supports slicing
"""

numbers = [10, 20, 30, 20, 40]

print(numbers)


# Different data types can exist in a list.

mixed_list = [10, "Hello", 10.5, True]

print(mixed_list)


# ============================================================
# 7. TUPLE (tuple)
# ============================================================

subjects = ("Math", "Science", "History")

print(subjects)
print(type(subjects))

# Output:
# ('Math', 'Science', 'History')
# <class 'tuple'>


"""
Tuple:

- Ordered
- Immutable
- Allows duplicate values
- Allows different data types
- Supports indexing
- Supports slicing
"""


# ============================================================
# 8. SET (set)
# ============================================================

s = {1, 2, 3, 4, 5}

print(s)
print(type(s))

# Output:
# {1, 2, 3, 4, 5}
# <class 'set'>


"""
Set:

- Unordered
- Mutable
- Does NOT allow duplicate elements
- Does not support indexing
- Useful for membership testing
- Useful for removing duplicates
"""

numbers = {1, 2, 2, 3, 3, 4}

print(numbers)

# Duplicate values are removed.


# ============================================================
# 9. DICTIONARY (dict)
# ============================================================

d = {
    "name": "Harshad",
    "age": 21,
    "is_student": True
}

print(d)
print(type(d))

# Output:
# <class 'dict'>


"""
Dictionary stores data in:

KEY : VALUE

Example:

"name"       -> "Harshad"
"age"        -> 21
"is_student" -> True
"""


# ============================================================
# 10. COMPLEX NUMBER (complex)
# ============================================================

comp = 2 + 6j

print(comp)
print(type(comp))

# Output:
# (2+6j)
# <class 'complex'>


"""
Complex numbers contain:

real part + imaginary part

Example:

2 + 6j

2 -> real part
6 -> imaginary part
j -> imaginary unit
"""


print(comp.real)
print(comp.imag)


# ============================================================
# 11. NONE TYPE (NoneType)
# ============================================================

"""
None represents the absence of a value.

It is NOT:

0
False
""
[]

None means there is no value.
"""

result = None

print(result)
print(type(result))

# Output:
# None
# <class 'NoneType'>


# Very common in functions:

def test():
    pass


result = test()

print(result)

# Output:
# None


# ============================================================
# 12. TYPE SUMMARY
# ============================================================

name = "Harshad"                 # str
age = 21                         # int
percentage = 85.5               # float
is_student = True                # bool
marks = [85, 90, 78]            # list
subjects = ("Math", "Science")   # tuple
s = {1, 2, 3}                   # set
d = {"name": "Harshad"}         # dict
comp = 2 + 6j                    # complex
result = None                    # NoneType


print(type(name))
print(type(age))
print(type(percentage))
print(type(is_student))
print(type(marks))
print(type(subjects))
print(type(s))
print(type(d))
print(type(comp))
print(type(result))


# ============================================================
# 13. MUTABLE VS IMMUTABLE
# ============================================================

"""
MUTABLE means:

The object can be changed after creation.

Examples:

list
set
dict


IMMUTABLE means:

The object cannot be changed after creation.

Common immutable types:

int
float
bool
str
tuple
complex
NoneType
"""


# ------------------------------------------------------------
# Mutable example: List
# ------------------------------------------------------------

numbers = [10, 20, 30]

numbers[0] = 100

print(numbers)

# Output:
# [100, 20, 30]


# ------------------------------------------------------------
# Immutable example: String
# ------------------------------------------------------------

name = "Harshad"

# This is NOT allowed:

# name[0] = "h"

# Strings are immutable.


# ============================================================
# 14. ORDERED VS UNORDERED
# ============================================================

"""
ORDERED:

list
tuple
str
dict

UNORDERED:

set

IMPORTANT:

Dictionary maintains insertion order in modern Python
(Python 3.7+ as a language guarantee).

A set should not be relied upon for a particular order.
"""


# ============================================================
# 15. DUPLICATES
# ============================================================

"""
List -> Allows duplicates
Tuple -> Allows duplicates
Set -> Does NOT allow duplicates
Dictionary -> Keys must be unique
"""

lst = [1, 2, 2, 3, 3]

print(lst)


tup = (1, 2, 2, 3, 3)

print(tup)


s = {1, 2, 2, 3, 3}

print(s)


# ============================================================
# 16. INDEXING
# ============================================================

"""
Indexing is supported by:

str
list
tuple

Dictionary uses keys instead of positional indexing.

Set does NOT support indexing.
"""

name = "Harshad"

print(name[0])
print(name[-1])


marks = [85, 90, 78]

print(marks[0])
print(marks[-1])


subjects = ("Math", "Science", "History")

print(subjects[0])
print(subjects[-1])


# ============================================================
# 17. SLICING
# ============================================================

name = "Harshad"

print(name[0:3])

marks = [85, 90, 78, 95, 88]

print(marks[1:4])


subjects = ("Math", "Science", "History", "English")

print(subjects[0:2])


# ============================================================
# 18. SET DOES NOT SUPPORT INDEXING
# ============================================================

s = {10, 20, 30}

# This will cause TypeError:

# print(s[0])


# ============================================================
# 19. DICTIONARY ACCESS
# ============================================================

student = {
    "name": "Harshad",
    "age": 21
}

print(student["name"])
print(student["age"])


"""
Dictionary doesn't use:

student[0]

It uses keys:

student["name"]
student["age"]
"""


# ============================================================
# 20. type()
# ============================================================

"""
type() tells us the exact type of an object.
"""

x = 10

print(type(x))

# <class 'int'>


# ============================================================
# 21. isinstance()
# ============================================================

"""
isinstance() checks whether an object belongs to
a particular type.

Syntax:

isinstance(object, type)
"""

x = 10

print(isinstance(x, int))

# True

print(isinstance(x, str))

# False


# ============================================================
# 22. type() VS isinstance()
# ============================================================

x = True

print(type(x))

print(isinstance(x, bool))

print(isinstance(x, int))


"""
Output:

<class 'bool'>
True
True

Why is the last one True?

Because bool is a subclass of int.
"""


# ============================================================
# 23. DYNAMIC TYPING
# ============================================================

x = 10

print(x)
print(type(x))


x = "Hello"

print(x)
print(type(x))


x = [1, 2, 3]

print(x)
print(type(x))


"""
The same variable can refer to objects of different types
at different times.

This is called dynamic typing.
"""


# ============================================================
# 24. TYPE CHECKING
# ============================================================

value = 100

if isinstance(value, int):

    print("Value is an integer")


# ============================================================
# 25. NESTED DATA TYPES
# ============================================================

"""
Python data types can contain other data types.
"""

students = [
    {"name": "Harshad", "age": 21},
    {"name": "Rahul", "age": 22}
]

print(students)

print(students[0])

print(students[0]["name"])


# ============================================================
# 26. LIST OF TUPLES
# ============================================================

data = [
    ("Harshad", 85),
    ("Rahul", 90),
    ("Sanjay", 78)
]

print(data)


# ============================================================
# 27. DICTIONARY WITH LIST
# ============================================================

student = {
    "name": "Harshad",
    "marks": [85, 90, 78]
}

print(student)

print(student["marks"])

print(student["marks"][0])


# ============================================================
# 28. SET FOR REMOVING DUPLICATES
# ============================================================

numbers = [1, 2, 2, 3, 3, 4, 4, 5]

unique_numbers = set(numbers)

print(unique_numbers)


"""
This is very useful in DSA.

Example:

Input:
[1, 2, 2, 3, 3, 4]

set(input)
    ↓

{1, 2, 3, 4}
"""


# ============================================================
# 29. IMPORTANT DATA TYPES FOR DSA
# ============================================================

"""
You should become very comfortable with:

1. list
2. tuple
3. set
4. dict
5. str

These are especially important for DSA.

LIST:
Used for arrays, stacks, dynamic sequences.

SET:
Used for fast membership checking and duplicates.

DICT:
Used for hash maps / frequency counting.

TUPLE:
Used for fixed collections and returning multiple values.

STRING:
Used heavily in string problems.
"""


# ============================================================
# 30. DATA TYPE COMPARISON
# ============================================================

"""
+-------------+----------+----------+-------------+
| Type        | Ordered  | Mutable  | Duplicates  |
+-------------+----------+----------+-------------+
| str         | Yes      | No       | Yes         |
| list        | Yes      | Yes      | Yes         |
| tuple       | Yes      | No       | Yes         |
| set         | No*      | Yes      | No          |
| dict        | Yes**    | Yes      | Keys: No    |
+-------------+----------+----------+-------------+

* Set has no guaranteed positional order.
** dict preserves insertion order in modern Python.
"""


# ============================================================
# 31. INTERVIEW QUESTIONS
# ============================================================

"""
Q1. What is a data type?

A data type specifies the kind of value an object represents.


Q2. Is Python statically typed or dynamically typed?

Python is dynamically typed.


Q3. What is the difference between list and tuple?

List:
- Mutable
- Uses []

Tuple:
- Immutable
- Uses ()


Q4. What is the difference between list and set?

List:
- Ordered
- Allows duplicates
- Supports indexing

Set:
- No guaranteed positional order
- Does not allow duplicates
- Does not support indexing


Q5. What is a dictionary?

A dictionary stores data as key-value pairs.


Q6. What does None mean?

None represents absence of a value.


Q7. What is the difference between type() and isinstance()?

type() returns the object's type.

isinstance() checks whether an object is an
instance of a specified type, including compatible
subclasses.


Q8. Is string mutable?

No. Strings are immutable.


Q9. Is list mutable?

Yes.


Q10. Is tuple mutable?

No.


Q11. Is set mutable?

Yes.


Q12. Is dictionary mutable?

Yes.


Q13. Can a list contain different data types?

Yes.

Example:

[10, "Hello", 10.5, True]


Q14. Can a set contain duplicate values?

No.


Q15. Can a dictionary contain duplicate keys?

No.

If the same key is assigned again, its value is replaced.


Q16. What is the type of True?

bool


Q17. What is the type of 10?

int


Q18. What is the type of 10.5?

float


Q19. What is the type of 2 + 3j?

complex


Q20. What is the type of None?

NoneType
"""


# ============================================================
# 32. QUICK REVISION
# ============================================================

"""
Python's major built-in data types:

Numeric:
    int
    float
    complex

Boolean:
    bool

Sequence:
    str
    list
    tuple
    range

Set:
    set
    frozenset

Mapping:
    dict

Special:
    NoneType
"""


# ============================================================
#                         END
# ============================================================