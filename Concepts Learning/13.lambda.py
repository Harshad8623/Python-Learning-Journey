# ============================================================
# 1. WHAT IS A LAMBDA FUNCTION?
# ============================================================

"""
Lambda is a small anonymous function.

Syntax:

lambda arguments: expression

Example:

lambda x: x * x

A lambda can contain only ONE expression.
The result of that expression is automatically returned.
"""


# ============================================================
# 2. NORMAL FUNCTION VS LAMBDA
# ============================================================

# Normal function
def square(n):
    return n * n


print(square(5))


# Same functionality using lambda
square = lambda n: n * n

print(square(5))


# ============================================================
# 3. LAMBDA WITH MULTIPLE ARGUMENTS
# ============================================================

# Normal function
def add(a, b):
    return a + b


print(add(10, 20))


# Lambda function
add = lambda a, b: a + b

print(add(10, 20))


# Another example
multiply = lambda a, b: a * b

print(multiply(5, 4))


# ============================================================
# 4. LAMBDA WITH THREE ARGUMENTS
# ============================================================

calculate = lambda a, b, c: a + b + c

print(calculate(10, 20, 30))


# ============================================================
# 5. LAMBDA WITH CONDITIONAL EXPRESSION
# ============================================================

# Normal function
def is_adult(age):

    if age >= 18:
        return True
    else:
        return False


print(is_adult(50))


# Lambda version

is_adult = lambda age: age >= 18

print(is_adult(50))


# IMPORTANT:
#
# We don't need:
#
# lambda age: True if age >= 18 else False
#
# because:
#
# age >= 18
#
# already returns True or False.


# ============================================================
# 6. LAMBDA WITH IF-ELSE
# ============================================================

# Lambda can use a conditional expression.

check_number = lambda n: "Positive" if n > 0 else "Non-positive"

print(check_number(10))
print(check_number(-5))


# Multiple conditions

find_max = lambda a, b: a if a > b else b

print(find_max(10, 20))


# ============================================================
# 7. LAMBDA WITH STRING
# ============================================================

get_length = lambda text: len(text)

print(get_length("Harshad"))


# Convert to uppercase
upper = lambda text: text.upper()

print(upper("harshad"))


# ============================================================
# 8. LAMBDA WITH LIST
# ============================================================

numbers = [1, 2, 3, 4, 5]

# Lambda function
square = lambda x: x * x

for number in numbers:
    print(square(number))


# ============================================================
# 9. map() FUNCTION
# ============================================================

"""
map() applies a function to EVERY element of an iterable.

Syntax:

map(function, iterable)

map() returns a map object,
so we commonly convert it to a list.
"""


numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print(squares)

# Output:
# [1, 4, 9, 16, 25]


# ============================================================
# 10. map() WITHOUT LAMBDA
# ============================================================

def square_number(x):
    return x * x


numbers = [1, 2, 3, 4, 5]

squares = list(map(square_number, numbers))

print(squares)


# ============================================================
# 11. map() WITH TWO LISTS
# ============================================================

numbers1 = [1, 2, 3, 4]
numbers2 = [10, 20, 30, 40]

result = list(
    map(lambda x, y: x + y, numbers1, numbers2)
)

print(result)

# Output:
# [11, 22, 33, 44]


# ============================================================
# 12. filter() FUNCTION
# ============================================================

"""
filter() selects elements based on a condition.

Syntax:

filter(function, iterable)

The function should return True or False.
Only elements for which the function returns True
are kept.
"""


numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print(even_numbers)

# Output:
# [2, 4, 6]


# ============================================================
# 13. FILTER ODD NUMBERS
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

odd_numbers = list(
    filter(lambda x: x % 2 != 0, numbers)
)

print(odd_numbers)

# Output:
# [1, 3, 5]


# ============================================================
# 14. FILTER NUMBERS GREATER THAN 10
# ============================================================

numbers = [5, 12, 3, 20, 15, 7]

result = list(
    filter(lambda x: x > 10, numbers)
)

print(result)

# Output:
# [12, 20, 15]


# ============================================================
# 15. map() VS filter()
# ============================================================

"""
map()
------------------------------------------------
Used to TRANSFORM every element.

Example:

[1, 2, 3]

map(lambda x: x * 2)

Result:
[2, 4, 6]


filter()
------------------------------------------------
Used to SELECT elements based on a condition.

Example:

[1, 2, 3, 4]

filter(lambda x: x % 2 == 0)

Result:
[2, 4]


Remember:

map()    -> Transform
filter() -> Select
"""


# ============================================================
# 16. sorted() WITH LAMBDA
# ============================================================

"""
One of the MOST IMPORTANT uses of lambda
for Python interviews.

sorted() can accept a key function.

Syntax:

sorted(iterable, key=function)
"""


numbers = [5, 2, 8, 1, 9]

result = sorted(
    numbers,
    key=lambda x: x
)

print(result)


# ============================================================
# 17. SORT LIST OF TUPLES USING LAMBDA
# ============================================================

students = [
    ("Harshad", 85),
    ("Rahul", 92),
    ("Sanjay", 78)
]

# Sort according to marks
result = sorted(
    students,
    key=lambda student: student[1]
)

print(result)


# Output:
# [
#     ('Sanjay', 78),
#     ('Harshad', 85),
#     ('Rahul', 92)
# ]


# ============================================================
# 18. SORT IN DESCENDING ORDER
# ============================================================

students = [
    ("Harshad", 85),
    ("Rahul", 92),
    ("Sanjay", 78)
]

result = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print(result)


# ============================================================
# 19. SORT BY NAME
# ============================================================

students = [
    ("Harshad", 85),
    ("Rahul", 92),
    ("Sanjay", 78)
]

result = sorted(
    students,
    key=lambda student: student[0]
)

print(result)


# ============================================================
# 20. sort() WITH LAMBDA
# ============================================================

students = [
    ("Harshad", 85),
    ("Rahul", 92),
    ("Sanjay", 78)
]

# sort() changes the original list

students.sort(
    key=lambda student: student[1]
)

print(students)


# ============================================================
# 21. LAMBDA WITH DICTIONARY
# ============================================================

students = {
    "Harshad": 85,
    "Rahul": 92,
    "Sanjay": 78
}

# items() produces:
#
# ('Harshad', 85)
# ('Rahul', 92)
# ('Sanjay', 78)


result = sorted(
    students.items(),
    key=lambda x: x[1]
)

print(result)


# ============================================================
# 22. DICTIONARY SORTING - DESCENDING
# ============================================================

students = {
    "Harshad": 85,
    "Rahul": 92,
    "Sanjay": 78
}

result = sorted(
    students.items(),
    key=lambda x: x[1],
    reverse=True
)

print(result)


# ============================================================
# 23. LAMBDA WITH TUPLES
# ============================================================

data = [
    (3, "C"),
    (1, "A"),
    (2, "B")
]

# Sort according to first element

result = sorted(
    data,
    key=lambda x: x[0]
)

print(result)


# Sort according to second element

result = sorted(
    data,
    key=lambda x: x[1]
)

print(result)


# ============================================================
# 24. reduce() FUNCTION
# ============================================================

"""
reduce() is available in the functools module.

reduce() repeatedly applies a function
and reduces all elements into ONE final value.

Example:

[1, 2, 3, 4]

1 + 2 = 3
3 + 3 = 6
6 + 4 = 10

Final result = 10
"""


from functools import reduce


numbers = [1, 2, 3, 4, 5]

result = reduce(
    lambda x, y: x + y,
    numbers
)

print(result)

# Output:
# 15


# ============================================================
# 25. reduce() FOR MULTIPLICATION
# ============================================================

numbers = [1, 2, 3, 4, 5]

result = reduce(
    lambda x, y: x * y,
    numbers
)

print(result)

# Output:
# 120


# ============================================================
# 26. reduce() TO FIND MAXIMUM
# ============================================================

numbers = [10, 25, 5, 40, 15]

maximum = reduce(
    lambda x, y: x if x > y else y,
    numbers
)

print(maximum)

# Output:
# 40


# ============================================================
# 27. map + filter TOGETHER
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

# Step 1:
# Filter even numbers

even = filter(
    lambda x: x % 2 == 0,
    numbers
)

# Step 2:
# Square the even numbers

squares = map(
    lambda x: x * x,
    even
)

result = list(squares)

print(result)

# Output:
# [4, 16, 36]


# ============================================================
# 28. map + filter IN ONE LINE
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

result = list(
    map(
        lambda x: x * x,
        filter(lambda x: x % 2 == 0, numbers)
    )
)

print(result)

# Output:
# [4, 16, 36]


# ============================================================
# 29. LAMBDA VS NORMAL FUNCTION
# ============================================================

"""
NORMAL FUNCTION:

def square(x):
    return x * x


LAMBDA:

square = lambda x: x * x


Use a NORMAL FUNCTION when:

- Logic is complex
- Multiple statements are required
- Function will be reused
- Function needs documentation
- Code needs to be very readable


Use LAMBDA when:

- Logic is very small
- Only one expression is needed
- Function is used temporarily
- Passing a function to map(), filter(), sorted(), etc.
"""


# ============================================================
# 30. LAMBDA LIMITATION
# ============================================================

"""
Lambda is designed for a SINGLE expression.

Example:

lambda x: x * x

This is valid.


A normal function can contain multiple statements:

def example(x):

    if x > 10:
        return x * 2

    return x
"""


# ============================================================
# 31. IMPORTANT INTERVIEW QUESTIONS
# ============================================================

"""
Q1. What is lambda?

Answer:
Lambda is an anonymous function used to create
small one-expression functions.


Q2. What is the syntax?

lambda arguments: expression


Q3. Can lambda have multiple arguments?

Yes.

Example:

lambda a, b: a + b


Q4. Can lambda contain multiple statements?

No. Lambda is restricted to a single expression.


Q5. Does lambda automatically return the result?

Yes.


Q6. What is map()?

map() applies a function to every element.


Q7. What is filter()?

filter() selects elements based on a condition.


Q8. What is reduce()?

reduce() repeatedly applies a function and
reduces an iterable to one final result.


Q9. What is a common use of lambda?

sorted(
    data,
    key=lambda x: x[1]
)


Q10. map() vs filter()?

map()    -> Transform elements
filter() -> Select elements
reduce() -> Reduce to one value
"""


# ============================================================
# 32. QUICK REVISION
# ============================================================

"""
LAMBDA
------------------------------------------------

Basic:
lambda x: x * x


Multiple arguments:
lambda a, b: a + b


Condition:
lambda x: "Even" if x % 2 == 0 else "Odd"


map():
map(lambda x: x * 2, numbers)


filter():
filter(lambda x: x % 2 == 0, numbers)


sorted():
sorted(data, key=lambda x: x[1])


reduce():
reduce(lambda x, y: x + y, numbers)


IMPORTANT MEMORY TRICK:

map()    -> MODIFY / TRANSFORM
filter() -> FILTER / SELECT
reduce() -> REDUCE / ONE RESULT
"""


# ============================================================
#                         END
# ============================================================