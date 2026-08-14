# ============================================================
#                  MATCH-CASE IN PYTHON
# ============================================================

"""
match-case was introduced in Python 3.10.

It is Python's pattern matching feature.

It is similar to switch-case in languages such as:
    - C
    - C++
    - Java
    - JavaScript

But Python's match-case is more powerful than a traditional
switch statement because it supports PATTERN MATCHING.
"""


# ============================================================
# 1. BASIC SYNTAX
# ============================================================

"""
Syntax:

match expression:
    case pattern1:
        # code
    case pattern2:
        # code
    case _:
        # default case
"""


# ============================================================
# 2. SIMPLE EXAMPLE
# ============================================================

day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")


# ============================================================
# 3. DEFAULT CASE - _
# ============================================================

"""
The underscore `_` is commonly used as the default case.

It means:

    "If none of the previous patterns match,
     execute this case."

Example:
"""

number = 100

match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Something else")


# ============================================================
# 4. MATCHING STRINGS
# ============================================================

command = "start"

match command:
    case "start":
        print("Starting the program")

    case "stop":
        print("Stopping the program")

    case "restart":
        print("Restarting the program")

    case _:
        print("Unknown command")


# ============================================================
# 5. MULTIPLE VALUES USING |
# ============================================================

"""
The | operator means OR.

Example:

case 1 | 2 | 3:

means:

    case 1 OR 2 OR 3
"""


day = 6

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")

    case 6 | 7:
        print("Weekend")

    case _:
        print("Invalid day")


# ============================================================
# 6. MATCH CASE WITH USER INPUT
# ============================================================

choice = int(input("Enter 1, 2 or 3: "))

match choice:
    case 1:
        print("You selected Option 1")

    case 2:
        print("You selected Option 2")

    case 3:
        print("You selected Option 3")

    case _:
        print("Invalid choice")


# ============================================================
# 7. MATCH CASE WITH CALCULATOR
# ============================================================

a = 10
b = 5
operator = "+"

match operator:

    case "+":
        print("Result:", a + b)

    case "-":
        print("Result:", a - b)

    case "*":
        print("Result:", a * b)

    case "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")

    case _:
        print("Invalid operator")


# ============================================================
# 8. MATCH CASE WITH if CONDITION
# ============================================================

"""
A case can have an additional condition using `if`.

This is called a GUARD.

Syntax:

case pattern if condition:
    ...
"""


age = 25

match age:

    case age if age < 18:
        print("Minor")

    case age if age >= 18 and age < 60:
        print("Adult")

    case age if age >= 60:
        print("Senior citizen")


# ============================================================
# 9. MATCH CASE - EVEN OR ODD
# ============================================================

number = 10

match number:
    case n if n % 2 == 0:
        print("Even")

    case n:
        print("Odd")


# ============================================================
# 10. MATCHING LISTS
# ============================================================

"""
match-case can perform structural pattern matching.

Example:
"""

numbers = [1, 2, 3]

match numbers:

    case []:
        print("Empty list")

    case [1, 2, 3]:
        print("List contains 1, 2, 3")

    case _:
        print("Some other list")


# ============================================================
# 11. MATCHING LIST WITH VARIABLES
# ============================================================

numbers = [10, 20]

match numbers:

    case [a, b]:
        print("Two elements")
        print("a =", a)
        print("b =", b)

    case _:
        print("Different structure")


# ============================================================
# 12. MATCHING FIRST ELEMENT
# ============================================================

numbers = [10, 20, 30]

match numbers:

    case [10, rest]:
        print("First element is 10")

    case _:
        print("First element is not 10")


# ============================================================
# 13. STAR PATTERN *
# ============================================================

"""
The * operator can capture multiple elements.

Example:

case [first, *middle, last]

means:

    first = first element
    last = last element
    middle = everything between them
"""


numbers = [10, 20, 30, 40, 50]

match numbers:

    case [first, *middle, last]:
        print("First:", first)
        print("Middle:", middle)
        print("Last:", last)


# ============================================================
# 14. MATCHING TUPLES
# ============================================================

point = (10, 20)

match point:

    case (0, 0):
        print("Origin")

    case (x, 0):
        print("Point lies on X-axis")

    case (0, y):
        print("Point lies on Y-axis")

    case (x, y):
        print("Normal point")
        print("x =", x)
        print("y =", y)


# ============================================================
# 15. MATCHING TUPLES WITH CONDITIONS
# ============================================================

point = (10, 20)

match point:

    case (x, y) if x == y:
        print("x and y are equal")

    case (x, y):
        print("x and y are different")


# ============================================================
# 16. MATCHING DICTIONARIES
# ============================================================

student = {
    "name": "Harshad",
    "age": 21
}

match student:

    case {"name": name, "age": age}:
        print("Name:", name)
        print("Age:", age)

    case _:
        print("Different dictionary structure")


# ============================================================
# 17. MATCHING DICTIONARY KEY
# ============================================================

student = {
    "name": "Harshad",
    "age": 21
}

match student:

    case {"name": "Harshad"}:
        print("Student is Harshad")

    case {"name": name}:
        print("Student:", name)

    case _:
        print("Unknown student")


# ============================================================
# 18. MATCHING DICTIONARY WITH EXTRA VALUES
# ============================================================

student = {
    "name": "Harshad",
    "age": 21,
    "city": "Latur"
}

match student:

    case {"name": name, "age": age}:
        print(name, age)

    case _:
        print("Not matched")


"""
Important:

Dictionary patterns can match the specified keys even when
the dictionary contains additional keys.
"""


# ============================================================
# 19. MATCHING NONE
# ============================================================

value = None

match value:

    case None:
        print("Value is None")

    case _:
        print("Value is not None")


# ============================================================
# 20. MATCHING BOOLEAN
# ============================================================

status = True

match status:

    case True:
        print("Status is True")

    case False:
        print("Status is False")


# ============================================================
# 21. MATCHING MULTIPLE DATA TYPES
# ============================================================

value = 10

match value:

    case int():
        print("It is an integer")

    case float():
        print("It is a float")

    case str():
        print("It is a string")

    case list():
        print("It is a list")

    case _:
        print("Other type")


# ============================================================
# 22. PRACTICAL MENU PROGRAM
# ============================================================

"""
match-case is useful for menu-driven programs.
"""

print("\n===== MENU =====")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice: "))

a = 20
b = 10

match choice:

    case 1:
        print("Addition:", a + b)

    case 2:
        print("Subtraction:", a - b)

    case 3:
        print("Multiplication:", a * b)

    case 4:
        if b != 0:
            print("Division:", a / b)
        else:
            print("Cannot divide by zero")

    case _:
        print("Invalid choice")


# ============================================================
# 23. MATCH CASE VS if-elif-else
# ============================================================

"""
if-elif-else:

    if condition:
        ...
    elif condition:
        ...
    else:
        ...


match-case:

    match value:
        case pattern1:
            ...
        case pattern2:
            ...
        case _:
            ...


Use if-elif when you mainly want to test conditions.

Use match-case when you are matching a value or structure
against patterns.
"""


# ============================================================
# 24. IMPORTANT DIFFERENCE
# ============================================================

"""
This:

    case 10:

means the value must match 10.

But:

    case x:

does NOT mean:

    "value equals variable x"

It captures the matched value into x.

Example:
"""

value = 100

match value:

    case x:
        print("Captured value:", x)


# ============================================================
# 25. CONSTANT-LIKE VALUES
# ============================================================

"""
Be careful with bare names in patterns.

A bare name such as:

    case x:

is a capture pattern.

It captures the value rather than comparing against
an existing variable named x.

This is an important interview / debugging point.
"""


# ============================================================
# 26. MATCH CASE WITH FUNCTIONS
# ============================================================

def check_number(number):

    match number:

        case 0:
            return "Zero"

        case n if n > 0:
            return "Positive"

        case n if n < 0:
            return "Negative"


print(check_number(10))
print(check_number(-5))
print(check_number(0))


# ============================================================
# 27. MATCH CASE WITH COMMANDS
# ============================================================

def execute_command(command):

    match command:

        case "start":
            return "Program started"

        case "stop":
            return "Program stopped"

        case "pause":
            return "Program paused"

        case "restart":
            return "Program restarted"

        case _:
            return "Unknown command"


print(execute_command("start"))
print(execute_command("pause"))
print(execute_command("hello"))


# ============================================================
# 28. NESTED PATTERN MATCHING
# ============================================================

data = ("student", ("Harshad", 21))

match data:

    case ("student", (name, age)):
        print("Name:", name)
        print("Age:", age)

    case _:
        print("No match")


# ============================================================
# 29. IMPORTANT RULES
# ============================================================

"""
RULE 1:

match must be followed by an expression.

    match value:


RULE 2:

case must be indented inside match.

    match value:
        case 1:
            ...


RULE 3:

The default case is commonly:

    case _:


RULE 4:

Multiple alternatives can be written using |.

    case 1 | 2 | 3:


RULE 5:

Conditions can be added using if.

    case x if x > 10:


RULE 6:

match-case was introduced in Python 3.10.


RULE 7:

match-case is more powerful than a traditional switch-case
because it supports structural pattern matching.
"""


# ============================================================
# 30. INTERVIEW QUESTIONS
# ============================================================

"""
Q1. What is match-case in Python?

ANSWER:

match-case is Python's structural pattern matching feature,
introduced in Python 3.10.


Q2. Is match-case the same as switch-case?

ANSWER:

It can be used for switch-like logic, but it is more powerful
because Python supports pattern matching.


Q3. Which Python version introduced match-case?

ANSWER:

Python 3.10.


Q4. What is the purpose of `_` in match-case?

ANSWER:

It is commonly used as a wildcard/default pattern that
matches anything not matched by previous cases.


Q5. How do you match multiple values?

ANSWER:

Use `|`.

Example:

    case 1 | 2 | 3:


Q6. Can match-case use conditions?

ANSWER:

Yes.

Example:

    case x if x > 10:


The condition is called a guard.


Q7. Can match-case work with lists?

ANSWER:

Yes.

It supports structural patterns for sequences.


Q8. Can match-case work with dictionaries?

ANSWER:

Yes.


Q9. Can match-case work with tuples?

ANSWER:

Yes.


Q10. What does `case x:` do?

ANSWER:

It captures the matched value into x.

It is not the same as comparing the value with
an existing variable x.


Q11. What is structural pattern matching?

ANSWER:

It means matching not only the value but also the structure
and shape of data.

For example:

    case [x, y]:

can match a two-element sequence and capture its elements.


Q12. What is a guard?

ANSWER:

An additional condition attached to a pattern.

Example:

    case x if x > 10:


Q13. What is the difference between `_` and a variable
in a case?

ANSWER:

`_` acts as a wildcard and doesn't capture the value.

A name such as `x` captures the matched value.


Q14. Can match-case replace every if-else?

ANSWER:

No.

For simple boolean/range conditions, if-elif-else is often
more natural.

match-case is particularly useful for value and structural
pattern matching.
"""


# ============================================================
# 31. QUICK REVISION
# ============================================================

"""
BASIC:

match value:
    case 1:
        ...
    case 2:
        ...
    case _:
        ...


OR:

case 1 | 2 | 3:


GUARD:

case x if x > 10:


LIST:

case [a, b]:


STAR:

case [first, *middle, last]:


TUPLE:

case (x, y):


DICTIONARY:

case {"name": name, "age": age}:


NONE:

case None:


BOOLEAN:

case True:
case False:


TYPE:

case int():
case str():
case list():
"""


# ============================================================
# 32. FINAL MEMORY TRICK
# ============================================================

"""
Think of match-case as:

        MATCH
          |
          ↓
      "What is this?"
          |
     +----+----+--------+
     ↓    ↓    ↓        ↓
    VALUE STRUCTURE   CONDITION
     |      |          |
    10     [x,y]    x if x > 10
     |
     ↓
   case _     ← default


IMPORTANT:

match-case
    ↓
Python 3.10+
    ↓
Pattern Matching
    ↓
Values + Lists + Tuples + Dictionaries + Types
    ↓
Guards using if
    ↓
Multiple patterns using |
    ↓
Wildcard using _
"""
arr = [1, 2, 3]
# 1. Basic
match choice:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Invalid")


# 2. OR
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")


# 3. Guard
match n:
    case x if x > 0:
        print("Positive")
    case x if x < 0:
        print("Negative")
    case 0:
        print("Zero")


# 4. List pattern
match arr:
    case [a, b]:
        print(a, b)
    case _:
        print("Other")


# 5. Dictionary pattern
match student:
    case {"name": name, "age": age}:
        print(name, age)
    case _:
        print("Invalid")


"\n================================================"
"       MATCH-CASE REVISION COMPLETE"
"================================================"