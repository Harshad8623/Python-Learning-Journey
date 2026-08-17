# ============================================================
#                  PYTHON CONDITIONAL STATEMENTS
#       Complete Notes + Examples + Interview Preparation
# ============================================================

"""
Conditional statements are used to make decisions in Python.

Main conditional statements:

1. if
2. if-else
3. if-elif-else
4. nested if
5. shorthand if
6. conditional expression (ternary operator)

Conditions are generally created using:

- comparison operators
- logical operators
- membership operators
- identity operators
"""


# ============================================================
# 1. if STATEMENT
# ============================================================

"""
Syntax:

if condition:
    statement

The statement executes only when the condition is True.
"""

age = 21

if age >= 18:

    print("You are eligible to vote.")


# ============================================================
# 2. if-else STATEMENT
# ============================================================

age = 16

if age >= 18:

    print("You are eligible to vote.")

else:

    print("You are not eligible to vote.")


# ============================================================
# 3. if-elif-else
# ============================================================

"""
Used when there are multiple conditions.

Python checks conditions from top to bottom.

As soon as one condition becomes True,
its block executes and the remaining conditions
are skipped.
"""

marks = 85

if marks >= 90:

    print("A Grade")

elif marks >= 80:

    print("B Grade")

elif marks >= 70:

    print("C Grade")

elif marks >= 60:

    print("D Grade")

else:

    print("F Grade")


# ============================================================
# 4. IMPORTANT: ORDER OF CONDITIONS
# ============================================================

"""
Wrong:

if marks >= 50:
    print("E")

elif marks >= 90:
    print("A")


For marks = 95:

marks >= 50 is already True.

Therefore Python will print E.

Correct approach:

Check the highest condition first.
"""

marks = 95

if marks >= 90:

    print("A")

elif marks >= 80:

    print("B")

elif marks >= 70:

    print("C")

elif marks >= 60:

    print("D")

else:

    print("F")


# ============================================================
# 5. NESTED if
# ============================================================

"""
An if statement inside another if statement
is called a nested if.
"""

age = 65

if age >= 18:

    print("Eligible to vote.")

    if age >= 60:

        print("Senior citizen.")

    else:

        print("Not a senior citizen.")


# ============================================================
# 6. NESTED if-else
# ============================================================

age = 25
has_license = True

if age >= 18:

    if has_license:

        print("You can drive.")

    else:

        print("You need a driving license.")

else:

    print("You are underage.")


# ============================================================
# 7. COMPARISON OPERATORS
# ============================================================

"""
Comparison operators return True or False.

==    Equal to
!=    Not equal to
>     Greater than
<     Less than
>=    Greater than or equal to
<=    Less than or equal to
"""

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# ============================================================
# 8. == VS =
# ============================================================

"""
VERY IMPORTANT INTERVIEW QUESTION

=   -> Assignment operator

==  -> Comparison operator


Example:

x = 10

Means:
Assign 10 to x.


x == 10

Means:
Check whether x is equal to 10.
"""

x = 10

if x == 10:

    print("x is 10")


# ============================================================
# 9. LOGICAL AND
# ============================================================

"""
and returns True only when BOTH conditions are True.
"""

age = 25
has_id = True

if age >= 18 and has_id:

    print("Entry allowed.")


# Truth table:

"""
True  and True   -> True
True  and False  -> False
False and True   -> False
False and False  -> False
"""


# ============================================================
# 10. LOGICAL OR
# ============================================================

"""
or returns True when AT LEAST ONE condition is True.
"""

day = "Saturday"

if day == "Saturday" or day == "Sunday":

    print("Weekend")


# Truth table:

"""
True  or True   -> True
True  or False  -> True
False or True   -> True
False or False  -> False
"""


# ============================================================
# 11. LOGICAL NOT
# ============================================================

"""
not reverses the Boolean value.
"""

is_raining = False

if not is_raining:

    print("You can go outside.")


"""
not True  -> False
not False -> True
"""


# ============================================================
# 12. COMBINING AND / OR / NOT
# ============================================================

age = 25
has_ticket = True
is_vip = False

if (age >= 18 and has_ticket) or is_vip:

    print("Entry allowed.")


# ============================================================
# 13. MEMBERSHIP OPERATORS
# ============================================================

"""
in
not in

Used to check whether an element exists
inside an iterable.
"""

numbers = [10, 20, 30, 40]

if 20 in numbers:

    print("20 exists in the list.")


if 50 not in numbers:

    print("50 does not exist in the list.")


# String example

name = "Harshad"

if "H" in name:

    print("H exists in the name.")


# ============================================================
# 14. IDENTITY OPERATORS
# ============================================================

"""
is
is not

These check whether two variables refer to
the SAME OBJECT in memory.

Do NOT use 'is' to normally compare values.

Use == for value comparison.
"""

a = [1, 2, 3]

b = a

c = [1, 2, 3]

print(a == b)   # True
print(a == c)   # True

print(a is b)   # True
print(a is c)   # False


# ============================================================
# 15. == VS is
# ============================================================

"""
==

Checks whether values are equal.


is

Checks whether both references point to
the same object.
"""

x = [10, 20]
y = [10, 20]

print(x == y)   # True
print(x is y)   # False


# ============================================================
# 16. CHAINED COMPARISON
# ============================================================

"""
Python allows chained comparisons.

Instead of:

age >= 18 and age <= 60

we can write:

18 <= age <= 60
"""

age = 30

if 18 <= age <= 60:

    print("Age is between 18 and 60.")


# ============================================================
# 17. MULTIPLE CONDITIONS
# ============================================================

marks = 75

if marks >= 40 and marks <= 100:

    print("Valid passing marks.")


# ============================================================
# 18. CHECK POSITIVE / NEGATIVE / ZERO
# ============================================================

num = -10

if num > 0:

    print("Positive")

elif num < 0:

    print("Negative")

else:

    print("Zero")


# ============================================================
# 19. CHECK EVEN / ODD
# ============================================================

num = 25

if num % 2 == 0:

    print("Even")

else:

    print("Odd")


# ============================================================
# 20. CHECK DIVISIBILITY
# ============================================================

num = 30

if num % 5 == 0:

    print("Divisible by 5.")

else:

    print("Not divisible by 5.")


# ============================================================
# 21. DIVISIBLE BY BOTH
# ============================================================

num = 30

if num % 3 == 0 and num % 5 == 0:

    print("Divisible by both 3 and 5.")

else:

    print("Not divisible by both.")


# ============================================================
# 22. LARGEST OF TWO NUMBERS
# ============================================================

a = 10
b = 20

if a > b:

    print("a is larger.")

elif b > a:

    print("b is larger.")

else:

    print("Both are equal.")


# ============================================================
# 23. LARGEST OF THREE NUMBERS
# ============================================================

a = 10
b = 50
c = 30

if a >= b and a >= c:

    print("a is largest.")

elif b >= a and b >= c:

    print("b is largest.")

else:

    print("c is largest.")


# ============================================================
# 24. LEAP YEAR
# ============================================================

"""
A year is a leap year when:

1. It is divisible by 400

OR

2. It is divisible by 4 but NOT divisible by 100
"""

year = 2024

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):

    print("Leap year")

else:

    print("Not a leap year")


# ============================================================
# 25. VOTING ELIGIBILITY
# ============================================================

age = 21

if age >= 18:

    print("Eligible to vote.")

else:

    print("Not eligible to vote.")


# ============================================================
# 26. GRADE CALCULATOR
# ============================================================

marks = 82

if marks >= 90:

    grade = "A"

elif marks >= 80:

    grade = "B"

elif marks >= 70:

    grade = "C"

elif marks >= 60:

    grade = "D"

elif marks >= 50:

    grade = "E"

else:

    grade = "F"


print("Grade:", grade)


# ============================================================
# 27. CHECK VALID MARKS
# ============================================================

marks = 85

if 0 <= marks <= 100:

    print("Valid marks.")

else:

    print("Invalid marks.")


# ============================================================
# 28. SHORTHAND if
# ============================================================

"""
If there is only one statement:

if condition:
    statement

can be written as:

statement if condition
"""

age = 20

if age >= 18:
    print("Adult")


# ============================================================
# 29. CONDITIONAL EXPRESSION / TERNARY OPERATOR
# ============================================================

"""
Syntax:

value_if_true if condition else value_if_false
"""

num = 10

result = "Even" if num % 2 == 0 else "Odd"

print(result)


# Another example:

age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)


# ============================================================
# 30. TERNARY WITH FUNCTION
# ============================================================

def check_even_odd(num):

    return "Even" if num % 2 == 0 else "Odd"


print(check_even_odd(10))


# ============================================================
# 31. TRUTHY AND FALSY VALUES
# ============================================================

"""
Python doesn't always require:

if x == True:

Python can directly evaluate x.

Falsy values include:

False
None
0
0.0
""
[]
()
{}
set()

Most other values are Truthy.
"""

name = ""

if name:

    print("Name exists.")

else:

    print("Name is empty.")


numbers = []

if numbers:

    print("List is not empty.")

else:

    print("List is empty.")


# ============================================================
# 32. CHECK EMPTY LIST
# ============================================================

numbers = []

if not numbers:

    print("List is empty.")


# ============================================================
# 33. CHECK NONE
# ============================================================

value = None

if value is None:

    print("Value is None.")


"""
IMPORTANT:

Use:

is None

instead of:

== None
"""


# ============================================================
# 34. CONDITIONAL STATEMENT WITH LIST
# ============================================================

numbers = [10, 20, 30]

target = 20

if target in numbers:

    print("Target found.")

else:

    print("Target not found.")


# ============================================================
# 35. CONDITIONAL STATEMENT WITH STRING
# ============================================================

text = "Python programming"

if "Python" in text:

    print("Python exists.")


# ============================================================
# 36. CONDITIONAL STATEMENT WITH DICTIONARY
# ============================================================

student = {
    "name": "Harshad",
    "age": 21
}

if "name" in student:

    print("Name key exists.")


# ============================================================
# 37. NESTED CONDITIONS - INTERVIEW STYLE
# ============================================================

username = "admin"
password = "1234"

if username == "admin":

    if password == "1234":

        print("Login successful.")

    else:

        print("Wrong password.")

else:

    print("Wrong username.")


# ============================================================
# 38. LOGIN USING AND
# ============================================================

username = "admin"
password = "1234"

if username == "admin" and password == "1234":

    print("Login successful.")

else:

    print("Invalid credentials.")


# ============================================================
# 39. CONDITIONAL STATEMENTS + LOOP
# ============================================================

"""
This combination is VERY important for DSA.

Loop:
    visits elements

Condition:
    decides what to do with each element.
"""

numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:

    if num % 2 == 0:

        print(num, "is even.")


# ============================================================
# 40. FIND MAXIMUM USING CONDITION
# ============================================================

numbers = [10, 50, 20, 80, 30]

maximum = numbers[0]

for num in numbers:

    if num > maximum:

        maximum = num


print("Maximum:", maximum)


# ============================================================
# 41. COUNT POSITIVE NUMBERS
# ============================================================

numbers = [-5, 10, -2, 20, 30, -8]

count = 0

for num in numbers:

    if num > 0:

        count += 1


print("Positive numbers:", count)


# ============================================================
# 42. FILTER EVEN NUMBERS
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = []

for num in numbers:

    if num % 2 == 0:

        even_numbers.append(num)


print(even_numbers)


# ============================================================
# 43. SEARCH WITH BREAK
# ============================================================

numbers = [10, 20, 30, 40, 50]

target = 30

for i in range(len(numbers)):

    if numbers[i] == target:

        print("Found at index:", i)

        break


# ============================================================
# 44. SEARCH WITH FOR-ELSE
# ============================================================

numbers = [10, 20, 30, 40, 50]

target = 100

for num in numbers:

    if num == target:

        print("Found")

        break

else:

    print("Not found")


# ============================================================
# 45. CONDITIONAL STATEMENT IN MATRIX
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(matrix)):

    for j in range(len(matrix[i])):

        if i == j:

            print(matrix[i][j], end=" ")

        else:

            print("-", end=" ")

    print()


# ============================================================
# 46. IMPORTANT DSA CONDITION:
#     i == j
# ============================================================

"""
For a square matrix:

i == j

represents the MAIN DIAGONAL.

Example:

* . .
. * .
. . *
"""


# ============================================================
# 47. IMPORTANT DSA CONDITION:
#     i + j == n - 1
# ============================================================

"""
For a square matrix:

i + j == n - 1

represents the ANTI-DIAGONAL.

Example:

. . *
. * .
* . .
"""


# ============================================================
# 48. CONDITIONAL OPERATOR PRECEDENCE
# ============================================================

"""
Important order:

1. ()
2. not
3. and
4. or

Example:

a or b and c

is interpreted as:

a or (b and c)

Use parentheses when the logic is complicated.
"""

a = True
b = False
c = True

result = a or (b and c)

print(result)


# ============================================================
# 49. SHORT-CIRCUIT EVALUATION
# ============================================================

"""
Python uses short-circuit evaluation.

AND:

If the first condition is False,
Python may not evaluate the second condition.

OR:

If the first condition is True,
Python may not evaluate the second condition.
"""

age = 15

if age >= 18 and age < 60:

    print("Adult")


# ============================================================
# 50. IMPORTANT INTERVIEW QUESTIONS
# ============================================================

"""
Q1. What is a conditional statement?

A:
A statement used to execute different code
depending on whether a condition is True or False.


Q2. What are the conditional statements in Python?

A:

if
if-else
if-elif-else
nested if
conditional expression


Q3. What is elif?

A:
elif means "else if".

It allows us to check multiple conditions.


Q4. Is else mandatory?

A:
No.

Example:

if age >= 18:
    print("Adult")


Q5. Can we have multiple elif?

A:
Yes.


Q6. Can we have multiple if statements?

A:
Yes.

But multiple independent if statements are different
from an if-elif-else chain.


Q7. Difference between if and elif?

if:
    Each separate if can be checked.

elif:
    Only the first matching condition in the chain executes.


Q8. Difference between = and ==?

=   -> assignment
==  -> comparison


Q9. Difference between == and is?

==  -> compares values
is  -> compares object identity


Q10. What are logical operators?

and
or
not


Q11. What are membership operators?

in
not in


Q12. What are identity operators?

is
is not


Q13. What is a ternary operator in Python?

Conditional expression:

value1 if condition else value2


Q14. What are falsy values?

False
None
0
0.0
""
[]
()
{}
set()


Q15. What is short-circuit evaluation?

Python may stop evaluating a logical expression
as soon as its final result is known.


Q16. What is nested if?

An if statement inside another if statement.
"""


# ============================================================
# 51. QUICK REVISION
# ============================================================

"""
if:

if condition:
    ...


if-else:

if condition:
    ...
else:
    ...


if-elif-else:

if condition:
    ...
elif condition:
    ...
else:
    ...


Nested:

if condition:
    if condition:
        ...


Logical:

and
or
not


Comparison:

==
!=
>
<
>=
<=


Membership:

in
not in


Identity:

is
is not


Ternary:

x if condition else y


Chained comparison:

18 <= age <= 60


DSA:

if arr[i] == target:
    ...


Matrix:

if i == j:
    ...


Anti-diagonal:

if i + j == n - 1:
    ...
"""


# ============================================================
#                         END
# ============================================================

arr = [1, 2, 3]
condition = True
arr = [12, 45, 14]
n = 10

# 1
if condition:
    pass

# 2
if condition:
    pass
else:
    pass

# 3
if condition:
    pass
elif condition:
    pass
else:
    pass

# 4
if a > b and b > c:
    pass

# 5
if x in arr:
    pass

# 6
result = "Yes" if condition else "No"

# 7
for x in arr:
    if condition:
        pass

# 8
for i in range(len(arr)):
    if arr[i] == target:
        pass

# 9
for i in range(n):
    for j in range(n):
        if i == j:
            pass

