# ============================================================
#              F-STRINGS AND DOCSTRINGS IN PYTHON
# ============================================================

"""
Topics covered:

PART 1 - F-STRINGS
    1. What is an f-string?
    2. Basic syntax
    3. Variables
    4. Expressions
    5. Arithmetic
    6. Function calls
    7. Formatting numbers
    8. Decimal places
    9. Percentage
    10. Comma separators
    11. Alignment
    12. Width
    13. Padding
    14. Dates
    15. Debugging with =
    16. Multiline f-strings
    17. Raw strings + f-strings
    18. Nested expressions
    19. Common mistakes

PART 2 - DOCSTRINGS
    20. What is a docstring?
    21. Function docstrings
    22. Class docstrings
    23. Module docstrings
    24. __doc__
    25. help()
    26. Multi-line docstrings
    27. Parameters and return documentation
    28. Docstring vs comment
    29. Interview questions
"""


# ============================================================
#                     PART 1 - F-STRINGS
# ============================================================


# ============================================================
# 1. WHAT IS AN F-STRING?
# ============================================================

"""
f-string means "formatted string literal".

It allows us to insert variables and expressions directly
inside a string.

It was introduced in Python 3.6.

Syntax:

    f"Hello {variable}"

Example:
"""

name = "Harshad"

print(f"Hello {name}")


# ============================================================
# 2. BASIC F-STRING
# ============================================================

name = "Harshad"
age = 21

print(f"My name is {name}")
print(f"I am {age} years old.")


# ============================================================
# 3. WITHOUT F-STRING
# ============================================================

"""
Before f-strings, programmers commonly used:

    + concatenation
    .format()
    % formatting

Example:
"""

name = "Harshad"
age = 21

print("My name is " + name + " and I am " + str(age) + " years old.")


# ============================================================
# 4. WITH F-STRING
# ============================================================

print(f"My name is {name} and I am {age} years old.")


# ============================================================
# 5. F-STRING WITH MULTIPLE VARIABLES
# ============================================================

name = "Harshad"
age = 21
city = "Latur"

print(f"Name: {name}, Age: {age}, City: {city}")


# ============================================================
# 6. EXPRESSIONS INSIDE F-STRING
# ============================================================

a = 10
b = 20

print(f"Sum = {a + b}")
print(f"Difference = {a - b}")
print(f"Multiplication = {a * b}")
print(f"Division = {a / b}")


# ============================================================
# 7. CONDITIONS INSIDE F-STRING
# ============================================================

age = 21

print(f"Status: {'Adult' if age >= 18 else 'Minor'}")


# ============================================================
# 8. FUNCTION CALL INSIDE F-STRING
# ============================================================

def square(n):
    return n * n


number = 5

print(f"Square of {number} = {square(number)}")


# ============================================================
# 9. METHOD CALL INSIDE F-STRING
# ============================================================

name = "harshad"

print(f"Name: {name.upper()}")
print(f"Name: {name.capitalize()}")


# ============================================================
# 10. FORMAT FLOAT TO DECIMAL PLACES
# ============================================================

percentage = 97.85678

print(f"Percentage: {percentage:.2f}")


"""
:.2f

means:

    .2 = two decimal places
    f  = floating-point number
"""


# ============================================================
# 11. MORE DECIMAL FORMATTING
# ============================================================

number = 12.3456789

print(f"{number:.1f}")
print(f"{number:.2f}")
print(f"{number:.3f}")
print(f"{number:.4f}")


# ============================================================
# 12. PERCENTAGE FORMAT
# ============================================================

value = 0.875

print(f"Percentage: {value:.2%}")


"""
Output:

Percentage: 87.50%

.2% means:

    multiply by 100
    display 2 decimal places
    add %
"""


# ============================================================
# 13. COMMA SEPARATOR
# ============================================================

salary = 1500000

print(f"Salary: {salary:,}")


"""
Output:

Salary: 1,500,000
"""


# ============================================================
# 14. COMMA + DECIMAL
# ============================================================

amount = 1234567.89123

print(f"Amount: {amount:,.2f}")


# ============================================================
# 15. WIDTH
# ============================================================

name = "Harshad"

print(f"{name:10}")


"""
10 means minimum width of 10 characters.
"""


# ============================================================
# 16. LEFT ALIGNMENT
# ============================================================

name = "Harshad"

print(f"{name:<10}")


"""
< means left alignment.
"""


# ============================================================
# 17. RIGHT ALIGNMENT
# ============================================================

print(f"{name:>10}")


"""
> means right alignment.
"""


# ============================================================
# 18. CENTER ALIGNMENT
# ============================================================

print(f"{name:^10}")


"""
^ means center alignment.
"""


# ============================================================
# 19. PADDING WITH ZERO
# ============================================================

number = 42

print(f"{number:05}")


"""
Output:

00042
"""


# ============================================================
# 20. BINARY / HEX / OCTAL
# ============================================================

number = 25

print(f"Decimal: {number}")
print(f"Binary: {number:b}")
print(f"Octal: {number:o}")
print(f"Hexadecimal: {number:x}")


"""
:b = binary
:o = octal
:x = hexadecimal
"""


# ============================================================
# 21. SCIENTIFIC NOTATION
# ============================================================

number = 1234567

print(f"{number:e}")


# ============================================================
# 22. DEBUGGING WITH =
# ============================================================

"""
One very useful feature of f-strings is:

    {variable=}

It prints both the variable name and its value.
"""

name = "Harshad"
age = 21

print(f"{name=}")
print(f"{age=}")


"""
Output:

name='Harshad'
age=21
"""


# ============================================================
# 23. DEBUGGING EXPRESSIONS WITH =
# ============================================================

a = 10
b = 20

print(f"{a + b=}")
print(f"{a * b=}")


# ============================================================
# 24. MULTILINE F-STRING
# ============================================================

name = "Harshad"
age = 21
course = "Engineering"

message = f"""
Name: {name}
Age: {age}
Course: {course}
"""

print(message)


# ============================================================
# 25. F-STRING WITH DICTIONARY
# ============================================================

student = {
    "name": "Harshad",
    "age": 21,
    "marks": 85
}

print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Marks: {student['marks']}")


# ============================================================
# 26. F-STRING WITH LIST
# ============================================================

numbers = [10, 20, 30, 40]

print(f"List: {numbers}")
print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")


# ============================================================
# 27. NESTED F-STRING / EXPRESSIONS
# ============================================================

width = 10
name = "Harshad"

print(f"{name:>{width}}")


"""
Here:

width = 10

is used as the formatting width.
"""


# ============================================================
# 28. F-STRING WITH OBJECT ATTRIBUTES
# ============================================================

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Harshad", 21)

print(f"Name: {student.name}")
print(f"Age: {student.age}")


# ============================================================
# 29. ESCAPING CURLY BRACES
# ============================================================

"""
Normally:

    {variable}

means insert variable value.

If you want actual curly braces,
use double curly braces:

    {{ }}
"""


name = "Harshad"

print(f"Hello {{name}}")
print(f"Hello {name}")


# ============================================================
# 30. COMMON F-STRING MISTAKE
# ============================================================

"""
Wrong:

    print(f"Hello {name")

The closing } is missing.


Correct:

    print(f"Hello {name}")
"""


# ============================================================
# 31. F-STRING VS .format()
# ============================================================

name = "Harshad"
age = 21

# .format()
print("Name: {}, Age: {}".format(name, age))

# f-string
print(f"Name: {name}, Age: {age}")


"""
For modern Python code, f-strings are generally preferred
for readable string formatting.
"""


# ============================================================
# 32. F-STRING VS CONCATENATION
# ============================================================

name = "Harshad"
age = 21

# Concatenation
print("Name: " + name + ", Age: " + str(age))

# F-string
print(f"Name: {name}, Age: {age}")


# ============================================================
# 33. RAW F-STRING
# ============================================================

"""
You can combine raw strings and f-strings:

    rf"..."

Useful when working with paths or regular expressions
containing backslashes.
"""

name = "Harshad"

print(rf"C:\Users\{name}\Documents")


# ============================================================
# 34. IMPORTANT F-STRING FORMAT SPECIFIERS
# ============================================================

"""
Common ones:

    :.2f       -> 2 decimal places

    :.2%       -> percentage with 2 decimal places

    :,         -> comma separator

    :<10       -> left align

    :>10       -> right align

    :^10       -> center align

    :05        -> zero padding

    :b         -> binary

    :o         -> octal

    :x         -> hexadecimal

    :e         -> scientific notation
"""


# ============================================================
#                PART 2 - DOCSTRINGS
# ============================================================


# ============================================================
# 35. WHAT IS A DOCSTRING?
# ============================================================

"""
A docstring is a string used to document:

    - Modules
    - Functions
    - Classes
    - Methods

It is written immediately inside the definition.

Usually triple quotes are used:

    \"\"\"
    Documentation
    \"\"\"
"""


# ============================================================
# 36. FUNCTION DOCSTRING
# ============================================================

def add(a, b):
    """
    Add two numbers and return the result.
    """
    return a + b


print(add(10, 20))


# ============================================================
# 37. ACCESS FUNCTION DOCSTRING
# ============================================================

print(add.__doc__)


# ============================================================
# 38. help()
# ============================================================

help(add)


"""
help() displays documentation about an object.

For example:

    help(add)
"""


# ============================================================
# 39. MULTILINE DOCSTRING
# ============================================================

def calculate_average(a, b, c):
    """
    Calculate the average of three numbers.

    The function accepts three numbers and returns
    their arithmetic average.
    """

    return (a + b + c) / 3


print(calculate_average(10, 20, 30))


# ============================================================
# 40. DOCSTRING WITH PARAMETERS
# ============================================================

def multiply(a, b):
    """
    Multiply two numbers.

    Parameters:
        a (int or float): First number.
        b (int or float): Second number.

    Returns:
        int or float: Product of a and b.
    """

    return a * b


print(multiply(5, 4))


# ============================================================
# 41. DOCSTRING WITH PARAMETERS + RETURN
# ============================================================

def divide(a, b):
    """
    Divide two numbers.

    Parameters:
        a (int or float): Numerator.
        b (int or float): Denominator.

    Returns:
        float: Result of division.

    Raises:
        ZeroDivisionError: If b is zero.
    """

    return a / b


print(divide(10, 2))


# ============================================================
# 42. CLASS DOCSTRING
# ============================================================

class Student:
    """
    Represents a student.

    Attributes:
        name (str): Student's name.
        age (int): Student's age.
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Harshad", 21)

print(student.name)
print(student.age)


# ============================================================
# 43. CLASS DOCSTRING ACCESS
# ============================================================

print(Student.__doc__)


# ============================================================
# 44. METHOD DOCSTRING
# ============================================================

class Calculator:

    def add(self, a, b):
        """
        Return the sum of two numbers.
        """
        return a + b


calculator = Calculator()

print(calculator.add(10, 20))
print(calculator.add.__doc__)


# ============================================================
# 45. MODULE DOCSTRING
# ============================================================

"""
The triple-quoted string at the very beginning of a Python
file can serve as the module's docstring.

Example:

    \"\"\"
    This module contains student-related functions.
    \"\"\"

Then:

    print(__doc__)

can access the module docstring.
"""


# ============================================================
# 46. __doc__
# ============================================================

"""
__doc__ is a special attribute that contains documentation
associated with a module, class, function, or method.
"""


def greet():
    """Print a greeting message."""
    print("Hello!")


print(greet.__doc__)


# ============================================================
# 47. DOCSTRING VS COMMENT
# ============================================================

"""
COMMENT:

A comment is mainly for explaining code to programmers.

Example:

    # This calculates the sum

Comments start with:

    #


DOCSTRING:

A docstring documents a module, function, class, or method.

Example:

    def add(a, b):
        \"\"\"
        Return the sum of a and b.
        \"\"\"
        return a + b


Main difference:

Comment:
    # explanation

Docstring:
    \"\"\"documentation\"\"\"
"""


# ============================================================
# 48. DOCSTRING IS ACCESSIBLE AT RUNTIME
# ============================================================

def greet_user(name):
    """
    Greet the user using their name.
    """

    print(f"Hello, {name}!")


print(greet_user.__doc__)


"""
A docstring is stored and can be accessed using __doc__.

This is one major difference from an ordinary comment.
"""


# ============================================================
# 49. GOOD DOCSTRING EXAMPLE
# ============================================================

def is_prime(n):
    """
    Check whether a number is prime.

    Parameters:
        n (int): Number to check.

    Returns:
        bool: True if n is prime, otherwise False.
    """

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:
            return False

    return True


print(is_prime(7))
print(is_prime(10))


# ============================================================
# 50. DOCSTRING CONVENTIONS
# ============================================================

"""
A good docstring should explain:

    - What the function does
    - Parameters
    - Return value
    - Possible exceptions
    - Important behavior

For larger projects, standardized styles such as
Google-style, NumPy-style, or Sphinx-style docstrings
may be used.
"""


# ============================================================
# 51. F-STRING INTERVIEW QUESTIONS
# ============================================================

"""
Q1. What is an f-string?

ANSWER:

An f-string is a formatted string literal that allows
variables and expressions to be embedded directly inside
a string using curly braces.


Q2. Which Python version introduced f-strings?

ANSWER:

Python 3.6.


Q3. How do you create an f-string?

ANSWER:

Put `f` or `F` before the string.

Example:

    name = "Harshad"

    print(f"Hello {name}")


Q4. Can expressions be used inside f-strings?

ANSWER:

Yes.

Example:

    print(f"Sum = {10 + 20}")


Q5. Can functions be called inside f-strings?

ANSWER:

Yes.

Example:

    print(f"Square = {square(5)}")


Q6. How do you format a float to two decimal places?

ANSWER:

    print(f"{number:.2f}")


Q7. How do you add commas to a number?

ANSWER:

    print(f"{number:,}")


Q8. What does {variable=} do?

ANSWER:

It displays both the variable name and its value.

Example:

    age = 21

    print(f"{age=}")


Q9. How do you display literal curly braces?

ANSWER:

Use double curly braces.

    print(f"{{hello}}")


Q10. Are f-strings generally preferred over .format()
in modern Python?

ANSWER:

For many ordinary formatting tasks, yes, because they are
concise and readable.
"""


# ============================================================
# 52. DOCSTRING INTERVIEW QUESTIONS
# ============================================================

"""
Q1. What is a docstring?

ANSWER:

A docstring is a string used to document a module, function,
class, or method.


Q2. How do you write a docstring?

ANSWER:

Usually using triple-quoted strings immediately inside
the object being documented.

Example:

    def add(a, b):
        \"\"\"
        Return the sum of a and b.
        \"\"\"
        return a + b


Q3. What is __doc__?

ANSWER:

__doc__ is a special attribute that contains the object's
docstring.


Q4. What is the difference between a comment and a docstring?

ANSWER:

A comment is primarily an explanatory note for developers.

A docstring is documentation associated with a module,
function, class, or method and can be accessed at runtime.


Q5. Can classes have docstrings?

ANSWER:

Yes.


Q6. Can modules have docstrings?

ANSWER:

Yes.


Q7. Can methods have docstrings?

ANSWER:

Yes.


Q8. What does help() do?

ANSWER:

help() displays documentation and information about
Python objects.


Q9. Why are docstrings useful?

ANSWER:

They make code easier to understand, maintain, use,
and document.


Q10. What should a good function docstring contain?

ANSWER:

Depending on the project, it can describe:

    - Purpose
    - Parameters
    - Return value
    - Exceptions
    - Important behavior
    - Examples
"""


# ============================================================
# 53. QUICK REVISION
# ============================================================

"""
==================== F-STRING ====================

f"Hello {name}"

    ↓

Insert values into strings


f"{a + b}"

    ↓

Expression


f"{price:.2f}"

    ↓

2 decimal places


f"{number:,}"

    ↓

Comma separator


f"{number:b}"

    ↓

Binary


f"{number=}"

    ↓

Debugging


===================================================


==================== DOCSTRING ====================

def add(a, b):
    \"\"\"
    Add two numbers.
    \"\"\"
    return a + b


    ↓

Documentation


add.__doc__

    ↓

Access docstring


help(add)

    ↓

Display documentation


===================================================
"""


# ============================================================
# 54. FINAL INTERVIEW MEMORY TRICK
# ============================================================

"""
F-STRING:

    f"Hello {name}"

    ↓

    Formatting strings
    + expressions
    + formatting numbers


DOCSTRING:

    \"\"\"Documentation\"\"\"

    ↓

    Documents:
        Module
        Function
        Class
        Method


IMPORTANT:

    f-string -> formatting

    docstring -> documentation

    __doc__  -> access documentation

    help()   -> display documentation
"""


print("\n================================================")
print("     F-STRINGS + DOCSTRINGS REVISION COMPLETE")
print("================================================")