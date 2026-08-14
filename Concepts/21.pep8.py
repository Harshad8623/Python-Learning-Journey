# ============================================================
#                         PEP 8
#              PYTHON STYLE GUIDE / BEST PRACTICES
# ============================================================

"""
PEP 8 - Python Enhancement Proposal 8

PEP 8 is the official style guide for Python code.

It provides recommendations for writing Python code that is:

    - Readable
    - Consistent
    - Clean
    - Maintainable
    - Professional

PEP 8 is mainly about CODE STYLE.

IMPORTANT:

PEP 8 is mostly a STYLE GUIDE, not a collection of rules
that Python itself enforces.

Python code can run even if it does not follow PEP 8.

However, following PEP 8 is very important in:

    - Interviews
    - Team projects
    - GitHub projects
    - Professional software development
    - Code reviews
"""


# ============================================================
# 1. WHY IS PEP 8 IMPORTANT?
# ============================================================

"""
Imagine two programmers write the same program.

Programmer A:

x=10
y=20
if x<y:
 print(x+y)


Programmer B:

x = 10
y = 20

if x < y:
    print(x + y)


Both programs can work.

But Programmer B's code is easier to:

    - Read
    - Understand
    - Maintain
    - Review
    - Debug


PEP 8 helps programmers write code in a consistent style.
"""


# ============================================================
# 2. INDENTATION
# ============================================================

"""
PEP 8 recommends:

    4 spaces per indentation level.

Do NOT normally use tabs for indentation.
"""


# GOOD:

if True:
    print("Hello")
    print("Python")


# BAD:

"""
if True:
  print("Hello")

Only 2 spaces are used here.
"""


# ============================================================
# 3. NESTED INDENTATION
# ============================================================

# GOOD:

age = 21

if age >= 18:
    if age >= 60:
        print("Senior citizen")
    else:
        print("Adult")


# ============================================================
# 4. MAXIMUM LINE LENGTH
# ============================================================

"""
Traditional PEP 8 guidance recommends keeping code lines
to around 79 characters.

For comments and docstrings, around 72 characters is
traditionally recommended.

Modern projects may configure different limits, especially
when using tools such as Black or Ruff.

The important point:

    Avoid unnecessarily long lines.
"""


# BAD:

"""
result = first_number + second_number + third_number + fourth_number + fifth_number
"""


# GOOD:

result = (
    10
    + 20
    + 30
    + 40
    + 50
)


# ============================================================
# 5. BLANK LINES
# ============================================================

"""
Blank lines help separate logical sections of code.

PEP 8 commonly recommends:

    - Two blank lines around top-level function/class definitions
    - One blank line between methods inside a class


Example:
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


class Calculator:

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


# ============================================================
# 6. SPACES AROUND OPERATORS
# ============================================================

"""
Use spaces around operators.

GOOD:

    x = 10
    result = a + b
    if x == 10:


BAD:

    x=10
    result=a+b
    if x==10:
"""


a = 10
b = 20

result = a + b

print(result)


# ============================================================
# 7. COMMA SPACING
# ============================================================

"""
Use a space after commas.

GOOD:

    numbers = [1, 2, 3, 4]

BAD:

    numbers = [1,2,3,4]
"""


numbers = [1, 2, 3, 4, 5]

student = {
    "name": "Harshad",
    "age": 21
}


# ============================================================
# 8. FUNCTION CALL SPACING
# ============================================================

"""
Do NOT put a space before the opening parenthesis.

GOOD:

    print("Hello")
    len(numbers)

BAD:

    print ("Hello")
    len (numbers)
"""


print("Hello")

print(len(numbers))


# ============================================================
# 9. FUNCTION DEFINITION SPACING
# ============================================================

"""
GOOD:

    def add(a, b):
        return a + b


BAD:

    def add (a, b):
        return a + b
"""


def multiply(a, b):
    return a * b


# ============================================================
# 10. SPACE AFTER KEYWORD
# ============================================================

"""
GOOD:

    if age >= 18:
        ...


BAD:

    if(age >= 18):
        ...


Python allows both in many contexts, but PEP 8 prefers
normal Python keyword spacing.
"""


age = 21

if age >= 18:
    print("Adult")


# ============================================================
# 11. COMPARISON OPERATORS
# ============================================================

"""
Use spaces around:

    ==
    !=
    <
    >
    <=
    >=


GOOD:

    if age >= 18:


BAD:

    if age>=18:
"""


if age >= 18:
    print("Eligible")


# ============================================================
# 12. ASSIGNMENT OPERATORS
# ============================================================

"""
Use spaces around:

    =
    +=
    -=
    *=
    /=
    //=
    %=
    **=
"""


x = 10

x += 5
x -= 2
x *= 2


# ============================================================
# 13. COLON SPACING
# ============================================================

"""
For slices, no unnecessary spaces around the colon:

GOOD:

    numbers[1:5]

BAD:

    numbers[1 : 5]


For dictionaries:

GOOD:

    {"name": "Harshad"}

BAD:

    {"name" : "Harshad"}
"""


numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])

student = {"name": "Harshad", "age": 21}


# ============================================================
# 14. FUNCTION NAMING
# ============================================================

"""
PEP 8 recommends:

    snake_case

for functions and variables.


GOOD:

    calculate_salary()
    get_student_data()
    total_marks


BAD:

    calculateSalary()
    GetStudentData()
    TotalMarks
"""


def calculate_total_marks(marks):
    return sum(marks)


# ============================================================
# 15. VARIABLE NAMING
# ============================================================

"""
Use:

    snake_case


GOOD:

    student_name
    total_marks
    average_score


BAD:

    studentName
    totalMarks
    averageScore
"""


student_name = "Harshad"
total_marks = 450
average_score = 90


# ============================================================
# 16. CONSTANT NAMING
# ============================================================

"""
Constants are conventionally written in:

    UPPER_CASE


GOOD:

    PI = 3.14159
    MAX_SIZE = 100
    DATABASE_URL = "..."


Python does not enforce constants.

UPPER_CASE is a naming convention.
"""


PI = 3.14159
MAX_SIZE = 100


# ============================================================
# 17. CLASS NAMING
# ============================================================

"""
Classes generally use:

    PascalCase

Also called:

    CapWords


GOOD:

    Student
    BankAccount
    EmployeeManager


BAD:

    student
    bank_account
    employee_manager
"""


class StudentDetails:
    pass


class BankAccount:
    pass


# ============================================================
# 18. MODULE NAMING
# ============================================================

"""
Module names should generally be:

    short
    lowercase
    readable


Examples:

    calculator.py
    database.py
    student.py
    user_service.py
"""


# ============================================================
# 19. PACKAGE NAMING
# ============================================================

"""
Package names should generally be:

    lowercase

Prefer short and readable names.

Example:

    utils
    services
    models
"""


# ============================================================
# 20. PRIVATE VARIABLES
# ============================================================

"""
A single leading underscore is a convention indicating
that a name is intended for internal use.

Example:

    _internal_value
    _helper_function()
"""


_internal_value = 100


def _internal_function():
    return "Internal function"


# ============================================================
# 21. SPECIAL / DUNDER NAMES
# ============================================================

"""
Names surrounded by double underscores are often called
"dunder" names.

Examples:

    __init__
    __str__
    __len__
    __name__


These have special meanings in Python.

Do not invent dunder names casually.
"""


class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


# ============================================================
# 22. BOOLEAN VARIABLE NAMES
# ============================================================

"""
Boolean variables should preferably have meaningful names.

GOOD:

    is_active
    is_student
    has_permission
    can_vote


BAD:

    active
    student
    permission
    vote

when the intention is specifically a boolean.
"""


is_student = True
has_permission = False
can_vote = True


# ============================================================
# 23. IMPORTS
# ============================================================

"""
Imports should generally be placed at the top of the file.

Example:

    import math
    import os

    from datetime import datetime


Avoid putting normal imports randomly throughout a file.
"""


import math
import os

from datetime import datetime


# ============================================================
# 24. IMPORT ORDER
# ============================================================

"""
PEP 8 recommends organizing imports into groups:

1. Standard library imports
2. Related/third-party imports
3. Local application imports


Example:

import os
import sys

import requests
import pandas

from myproject import database
"""


# ============================================================
# 25. DON'T USE WILDCARD IMPORTS
# ============================================================

"""
Avoid:

    from math import *


Why?

It can make it unclear where names came from and can
cause naming conflicts.

Prefer:

    import math

or:

    from math import sqrt
"""


# GOOD:

from math import sqrt

print(sqrt(25))


# ============================================================
# 26. COMMENTS
# ============================================================

"""
Comments should explain WHY when the reason is not obvious.

GOOD:

    # Ignore invalid records because the API can return
    # incomplete data.


Avoid comments that simply repeat obvious code.

BAD:

    # Add 10 to x
    x = x + 10
"""


x = 10

# Add bonus points to the student's score.
x += 10


# ============================================================
# 27. INLINE COMMENTS
# ============================================================

"""
Inline comments should be used carefully.

GOOD:

    x = 10  # Maximum retry count

Avoid excessive inline comments.
"""


max_retries = 3  # Maximum number of retries


# ============================================================
# 28. DOCSTRINGS
# ============================================================

"""
Public modules, functions, classes, and methods should have
useful docstrings where appropriate.
"""


def calculate_average(numbers):
    """
    Return the arithmetic average of a list of numbers.
    """

    return sum(numbers) / len(numbers)


# ============================================================
# 29. COMPARING WITH NONE
# ============================================================

"""
Use:

    is None

and:

    is not None


GOOD:

    if value is None:


Avoid:

    if value == None:


Because None is a singleton and identity comparison is
the conventional and correct style here.
"""


value = None

if value is None:
    print("No value")


# ============================================================
# 30. COMPARING BOOLEAN VALUES
# ============================================================

"""
Instead of:

    if is_active == True:

prefer:

    if is_active:


Instead of:

    if is_active == False:

prefer:

    if not is_active:
"""


is_active = True

if is_active:
    print("Active")


# ============================================================
# 31. DON'T COMPARE BOOLEAN WITH == TRUE
# ============================================================

# BAD:

"""
if is_student == True:
    print("Student")
"""


# GOOD:

if is_student:
    print("Student")


# ============================================================
# 32. LIST COMPREHENSION
# ============================================================

"""
List comprehensions are Pythonic, but don't make them
unnecessarily complicated.

GOOD:

squares = [x * x for x in range(10)]
"""


squares = [x * x for x in range(10)]

print(squares)


# ============================================================
# 33. AVOID OVERLY COMPLEX EXPRESSIONS
# ============================================================

"""
If a single line becomes difficult to understand,
break it into multiple steps.

BAD:

    result = very_long_expression + another_expression * x


GOOD:

    first_part = very_long_expression
    second_part = another_expression * x
    result = first_part + second_part


Readability is important.
"""


# ============================================================
# 34. EXPLICIT IS BETTER THAN IMPLICIT
# ============================================================

"""
Python's philosophy strongly values readable and explicit code.

Example:

GOOD:

    if user is not None:
        process(user)


Avoid clever code that is difficult to understand.
"""


# ============================================================
# 35. AVOID UNNECESSARY SEMICOLONS
# ============================================================

"""
Python normally does not need semicolons.

GOOD:

    x = 10
    y = 20


Avoid:

    x = 10; y = 20
"""


x = 10
y = 20


# ============================================================
# 36. STRING QUOTES
# ============================================================

"""
PEP 8 allows either single or double quotes.

Examples:

    "Hello"

    'Hello'


The important thing is CONSISTENCY.

Choose a style and use it consistently.

Triple double quotes are commonly used for docstrings.
"""


name = "Harshad"

message = 'Hello'


# ============================================================
# 37. TRAILING WHITESPACE
# ============================================================

"""
Avoid unnecessary spaces at the end of lines.

BAD:

    print("Hello")<spaces>


This is called trailing whitespace.
"""


# ============================================================
# 38. TRAILING COMMA
# ============================================================

"""
Trailing commas can be useful when writing multi-line
collections or function arguments.

Example:
"""


numbers = [
    10,
    20,
    30,
]


# ============================================================
# 39. MULTI-LINE FUNCTION CALL
# ============================================================

result = calculate_average(
    [10, 20, 30, 40, 50]
)

print(result)


# ============================================================
# 40. MULTI-LINE DICTIONARY
# ============================================================

student = {
    "name": "Harshad",
    "age": 21,
    "course": "Engineering",
    "city": "Latur",
}


# ============================================================
# 41. MULTI-LINE FUNCTION DEFINITION
# ============================================================

def calculate_student_percentage(
    total_marks,
    obtained_marks,
):
    return (obtained_marks / total_marks) * 100


print(calculate_student_percentage(500, 450))


# ============================================================
# 42. DON'T USE SINGLE LETTER NAMES UNNECESSARILY
# ============================================================

"""
Single-letter names can be acceptable in small loops:

    for i in range(10):

But for general variables, meaningful names are better.

BAD:

    x = 450
    y = 500


GOOD:

    obtained_marks = 450
    total_marks = 500
"""


obtained_marks = 450
total_marks = 500


# ============================================================
# 43. LOOP VARIABLE
# ============================================================

"""
Short loop variables are often acceptable:

    i
    j
    k


Especially in simple loops.

Example:
"""


for i in range(5):
    print(i)


# ============================================================
# 44. UNUSED LOOP VARIABLE
# ============================================================

"""
Use `_` when you intentionally don't need the value.

Example:
"""


for _ in range(3):
    print("Hello")


"""
Here `_` communicates:

    "I don't care about this value."
"""


# ============================================================
# 45. AVOID SHADOWING BUILT-IN NAMES
# ============================================================

"""
Avoid using built-in names as variable names.

BAD:

    list = [1, 2, 3]
    str = "Hello"
    sum = 100
    id = 10


Why?

Because you can accidentally hide the built-in function.
"""


# GOOD:

numbers = [1, 2, 3]
text = "Hello"
total = 100
student_id = 10


# ============================================================
# 46. EXAMPLE OF SHADOWING
# ============================================================

"""
BAD:

    sum = 100

After this:

    sum([1, 2, 3])

may no longer work as expected because you replaced
the built-in name `sum` in your current scope.

Avoid this.
"""


# ============================================================
# 47. PYTHONIC NAMING SUMMARY
# ============================================================

"""
VARIABLE:

    student_name


FUNCTION:

    calculate_total()


CLASS:

    StudentManager


CONSTANT:

    MAX_RETRIES


MODULE:

    student_manager.py


PACKAGE:

    student_manager


PRIVATE/INTERNAL:

    _helper_function


SPECIAL:

    __init__
    __name__
"""


# ============================================================
# 48. PEP 8 EXAMPLE - BAD CODE
# ============================================================

"""
BAD CODE:

import os,sys

studentName="Harshad"
age=21
if(age>=18):
 print("Adult")
else:
 print("Minor")

def CalculateAge(x):
 return x+1
"""


# ============================================================
# 49. PEP 8 EXAMPLE - GOOD CODE
# ============================================================

import os
import sys

student_name = "Harshad"
age = 21

if age >= 18:
    print("Adult")
else:
    print("Minor")


def calculate_age(age):
    return age + 1


# ============================================================
# 50. PEP 8 TOOLS
# ============================================================

"""
PEP 8 does not mean you have to manually check everything.

Tools can help.

Popular tools:

1. pycodestyle
2. flake8
3. Ruff
4. Black


These tools can check or format Python code.

Ruff is a modern, very fast tool that can handle many
linting tasks and can also format Python code.

Black is primarily a code formatter.
"""


# ============================================================
# 51. pycodestyle
# ============================================================

"""
Install:

    python -m pip install pycodestyle


Check a file:

    pycodestyle my_file.py
"""


# ============================================================
# 52. FLake8
# ============================================================

"""
Install:

    python -m pip install flake8


Run:

    flake8 my_file.py
"""


# ============================================================
# 53. RUFF
# ============================================================

"""
Install:

    python -m pip install ruff


Check:

    ruff check my_file.py


Format:

    ruff format my_file.py
"""


# ============================================================
# 54. BLACK
# ============================================================

"""
Install:

    python -m pip install black


Format:

    black my_file.py


Black automatically formats code according to its
opinionated style.
"""


# ============================================================
# 55. PEP 8 VS PEP
# ============================================================

"""
PEP stands for:

    Python Enhancement Proposal


A PEP is a document describing a proposed change,
feature, standard, or guidance related to Python.


PEP 8:

    Style Guide for Python Code


PEP 20:

    The Zen of Python


PEP 257:

    Docstring conventions
"""


# ============================================================
# 56. ZEN OF PYTHON
# ============================================================

"""
You can see Python's Zen by running:

    import this

Important ideas include:

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Readability counts.
"""


# ============================================================
# 57. PEP 8 AND DSA
# ============================================================

"""
PEP 8 does NOT directly improve the algorithm.

For example:

    O(n)
    O(log n)
    O(n^2)

are algorithmic concepts, not PEP 8 rules.

However, PEP 8 makes your DSA solutions easier to read.

GOOD:

    left = 0
    right = len(numbers) - 1

    while left <= right:
        ...


BAD:

    l=0;r=len(numbers)-1
"""


# ============================================================
# 58. PEP 8 AND INTERVIEWS
# ============================================================

"""
During coding interviews:

    1. Use meaningful variable names.
    2. Indent correctly.
    3. Keep code readable.
    4. Don't write everything on one line.
    5. Use spaces around operators.
    6. Explain your approach.
    7. Avoid unnecessary clever tricks.
    8. Keep functions reasonably focused.


Interviewers usually care more about:

    Correctness
    Logic
    Complexity
    Communication
    Code readability

than perfect PEP 8 compliance.
"""


# ============================================================
# 59. IMPORTANT PEP 8 INTERVIEW QUESTIONS
# ============================================================

"""
Q1. What is PEP 8?

ANSWER:

PEP 8 is the style guide for Python code. It provides
recommendations for writing readable and consistent Python.


Q2. What does PEP stand for?

ANSWER:

Python Enhancement Proposal.


Q3. How many spaces does PEP 8 recommend for indentation?

ANSWER:

4 spaces per indentation level.


Q4. What naming convention is recommended for variables?

ANSWER:

snake_case.


Q5. What naming convention is recommended for functions?

ANSWER:

snake_case.


Q6. What naming convention is recommended for classes?

ANSWER:

PascalCase / CapWords.


Q7. How should constants normally be named?

ANSWER:

UPPER_CASE.


Q8. How should modules normally be named?

ANSWER:

lowercase, generally short and readable, often using
underscores when needed.


Q9. What is the recommended traditional maximum line length?

ANSWER:

79 characters for code.

Comments/docstrings traditionally use about 72 characters.

Modern projects may configure different limits.


Q10. How should None be compared?

ANSWER:

Use:

    is None

or:

    is not None


Q11. Should wildcard imports be used?

ANSWER:

Generally no.

Avoid:

    from module import *


Prefer explicit imports.


Q12. What is variable shadowing?

ANSWER:

Using a variable name that hides another name, such as
a built-in function.

Example:

    sum = 10

This shadows the built-in sum() in that scope.


Q13. What is the difference between PEP 8 and Black?

ANSWER:

PEP 8 is a style guide.

Black is an automatic code formatter that applies an
opinionated formatting style.


Q14. What is Flake8?

ANSWER:

A Python linting tool that checks code for various
style and programming issues.


Q15. What is Ruff?

ANSWER:

A fast Python linter and formatter that can automate many
style and code-quality checks.


Q16. Is PEP 8 enforced by Python?

ANSWER:

No.

Python can execute code that does not follow PEP 8.

It is a style guide rather than a language requirement.


Q17. Why is PEP 8 important?

ANSWER:

It improves readability, consistency, maintainability,
and collaboration between developers.
"""


# ============================================================
# 60. QUICK PEP 8 CHEAT SHEET
# ============================================================

"""
+----------------------+----------------------------+
| THING                | PEP 8 STYLE                |
+----------------------+----------------------------+
| Indentation          | 4 spaces                  |
| Variable             | snake_case                |
| Function             | snake_case                |
| Class                | PascalCase                |
| Constant             | UPPER_CASE                |
| Module               | lowercase                 |
| Boolean              | is_/has_/can_ preferred   |
| None comparison      | is None                   |
| Boolean check        | if value:                 |
| Operators            | spaces around operators   |
| Comma                | space after comma         |
| Wildcard import      | Avoid                     |
| Line length          | ~79 chars traditionally   |
| Comments             | Explain when useful       |
| Docstrings           | Use for public APIs       |
+----------------------+----------------------------+
"""


# ============================================================
# 61. FINAL MEMORY TRICK
# ============================================================

"""
PEP 8 = READABLE PYTHON

Remember:

    4 spaces
        ↓
    snake_case
        ↓
    PascalCase
        ↓
    UPPER_CASE
        ↓
    spaces around operators
        ↓
    meaningful names
        ↓
    clean imports
        ↓
    useful comments/docstrings
        ↓
    is None
        ↓
    avoid shadowing built-ins
        ↓
    avoid wildcard imports
        ↓
    keep code readable


The main idea of PEP 8:

        "Write Python code that other people
         can easily read and maintain."
"""


# Variable / function
student_name = "Harshad"

def calculate_total():
    pass


# Class
class StudentManager:
    pass


# Constant
MAX_RETRIES = 3


# 4-space indentation
if age >= 18:
    print("Adult")


# Spaces around operators
result = a + b


# None
if value is None:
    pass


# Boolean
if is_active:
    pass


# Avoid wildcard imports
from math import sqrt      # Good
# from math import *       # Avoid


# Don't shadow built-ins
student_id = 10            # Good
# id = 10                  # Avoid


# Meaningful names
obtained_marks = 450       # Good
# x = 450                  # Less descriptive


print("\n================================================")
print("             PEP 8 REVISION COMPLETE")
print("================================================")