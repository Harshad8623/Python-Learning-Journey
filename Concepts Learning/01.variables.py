# ============================================================
#                       PYTHON VARIABLES
# ============================================================

"""
A variable is a name/reference used to store or refer to
a value/object in Python.

Example:

name = "John"

Here:

name  -> variable name
"John" -> value
=     -> assignment operator
"""


# ============================================================
# 1. CREATING VARIABLES
# ============================================================

name = "John"
is_student = True
age = 20

print(name)
print(is_student)
print(age)


# ============================================================
# 2. VARIABLES WITH DIFFERENT DATA TYPES
# ============================================================

name = "Harshad"          # str
age = 21                  # int
percentage = 85.5        # float
is_student = True         # bool

print(name)
print(age)
print(percentage)
print(is_student)


# ============================================================
# 3. CHECKING VARIABLE TYPE
# ============================================================

print(type(name))
print(type(age))
print(type(percentage))
print(type(is_student))


# ============================================================
# 4. MULTIPLE VARIABLES
# ============================================================

a = 10
b = 20
c = 30

print(a)
print(b)
print(c)


# ============================================================
# 5. MULTIPLE ASSIGNMENT
# ============================================================

a, b, c = 10, 20, 30

print(a)
print(b)
print(c)


"""
This:

a, b, c = 10, 20, 30

is equivalent to:

a = 10
b = 20
c = 30
"""


# ============================================================
# 6. SAME VALUE TO MULTIPLE VARIABLES
# ============================================================

a = b = c = 100

print(a)
print(b)
print(c)


# ============================================================
# 7. VARIABLE VALUE CAN BE CHANGED
# ============================================================

age = 20

print(age)

age = 21

print(age)


"""
Python variables can be reassigned.
"""


# ============================================================
# 8. DIFFERENT TYPES CAN BE ASSIGNED TO THE SAME VARIABLE
# ============================================================

value = 100

print(value)
print(type(value))


value = "Hello"

print(value)
print(type(value))


value = [1, 2, 3]

print(value)
print(type(value))


"""
This is called DYNAMIC TYPING.

The variable 'value' can refer to objects
of different types during program execution.
"""


# ============================================================
# 9. VARIABLE NAMING RULES
# ============================================================

"""
Rules for naming variables:

1. Name can contain letters.
2. Name can contain numbers.
3. Name can contain underscore (_).
4. Name cannot start with a number.
5. Name cannot contain spaces.
6. Python is case-sensitive.
7. Keywords cannot be used as variable names.
"""


# Valid:

name = "Harshad"

age2 = 21

student_name = "Rahul"

_marks = 90


# Invalid examples:

# 2name = "Harshad"       # Cannot start with number
# student name = "Rahul" # Spaces are not allowed
# student-name = "Rahul" # - is treated as minus
# class = 10              # class is a Python keyword


# ============================================================
# 10. VARIABLE NAMES ARE CASE-SENSITIVE
# ============================================================

name = "Harshad"

Name = "Rahul"

NAME = "Sanjay"

print(name)
print(Name)
print(NAME)


"""
These are three different variables:

name
Name
NAME
"""


# ============================================================
# 11. GOOD VARIABLE NAMING
# ============================================================

"""
Use meaningful variable names.

Bad:

x = 21
y = 85.5

Better:

age = 21
percentage = 85.5
"""


age = 21
percentage = 85.5

print(age)
print(percentage)


# ============================================================
# 12. SNAKE_CASE
# ============================================================

"""
Python convention:

Use snake_case for variable names.

Examples:
"""

student_name = "Harshad"

student_age = 21

total_marks = 450

average_marks = 90.0


# ============================================================
# 13. VARIABLES CAN STORE EXPRESSIONS
# ============================================================

a = 10
b = 20

sum_value = a + b

product = a * b

difference = b - a

print(sum_value)
print(product)
print(difference)


# ============================================================
# 14. VARIABLE SWAPPING
# ============================================================

a = 10
b = 20

print("Before:", a, b)

a, b = b, a

print("After:", a, b)


"""
Python allows swapping without a temporary variable.

This is very useful and commonly asked in interviews.
"""


# ============================================================
# 15. TRADITIONAL SWAPPING
# ============================================================

a = 10
b = 20

temp = a

a = b

b = temp

print(a)
print(b)


# ============================================================
# 16. VARIABLE WITH LIST
# ============================================================

marks = [85, 90, 78, 95]

print(marks)


# ============================================================
# 17. VARIABLE WITH TUPLE
# ============================================================

subjects = ("Math", "Science", "English")

print(subjects)


# ============================================================
# 18. VARIABLE WITH SET
# ============================================================

numbers = {1, 2, 3, 4}

print(numbers)


# ============================================================
# 19. VARIABLE WITH DICTIONARY
# ============================================================

student = {
    "name": "Harshad",
    "age": 21
}

print(student)


# ============================================================
# 20. VARIABLE WITH NONE
# ============================================================

result = None

print(result)

print(type(result))

# Output:
# None
# <class 'NoneType'>


"""
None is used when a variable currently has no value.
"""


# ============================================================
# 21. CONSTANTS IN PYTHON
# ============================================================

"""
Python does not have a strict constant keyword.

By convention, constants are written in UPPERCASE.

Example:
"""

PI = 3.14159

MAX_SIZE = 100

COLLEGE_NAME = "CSMSS"

print(PI)
print(MAX_SIZE)
print(COLLEGE_NAME)


"""
IMPORTANT:

Python does NOT prevent you from changing these values.

UPPERCASE is simply a convention meaning:

"Do not change this value."
"""


# ============================================================
# 22. DELETING A VARIABLE
# ============================================================

x = 100

print(x)

del x

# Now x no longer exists.

# print(x)   # NameError


# ============================================================
# 23. CHECK WHETHER A VARIABLE EXISTS
# ============================================================

"""
You generally don't need to do this in beginner code,
but understanding NameError is important.

If you use a variable before defining it:

print(student_name)

you get:

NameError
"""


# ============================================================
# 24. VARIABLE REFERENCES / OBJECTS
# ============================================================

a = 10

b = a

print(a)
print(b)


"""
Now both variables refer to the value 10.

Conceptually:

a ──┐
    ├──> 10
b ──┘
"""


# ============================================================
# 25. IDENTITY OF AN OBJECT
# ============================================================

a = 10

print(id(a))


"""
id() returns the identity of an object.

You don't need to memorize the actual number because
it can vary between executions.
"""


# ============================================================
# 26. VARIABLES AND MUTABLE OBJECTS
# ============================================================

a = [1, 2, 3]

b = a

b.append(4)

print(a)
print(b)


"""
Output:

[1, 2, 3, 4]
[1, 2, 3, 4]

Why?

Because a and b refer to the SAME list object.

This concept becomes very important when learning:

- Lists
- Functions
- References
- Shallow copy
- Deep copy
"""


# ============================================================
# 27. COPY OF A LIST
# ============================================================

a = [1, 2, 3]

b = a.copy()

b.append(4)

print(a)

print(b)


"""
Output:

[1, 2, 3]
[1, 2, 3, 4]

Now they are separate list objects.
"""


# ============================================================
# 28. VARIABLE WITH USER INPUT
# ============================================================

"""
input() always returns a string.
"""

name = input("Enter your name: ")

print("Hello", name)


# ============================================================
# 29. INPUT + TYPE CONVERSION
# ============================================================

age = int(input("Enter your age: "))

print(age)

print(type(age))


# ============================================================
# 30. VARIABLES IN DSA
# ============================================================

"""
Variables are everywhere in DSA.

Example:

arr = [10, 20, 30, 40, 50]

target = 30

count = 0

max_value = arr[0]

left = 0

right = len(arr) - 1


Common variable names in DSA:

i
j
k
left
right
start
end
mid
count
sum
target
max_value
min_value
result
"""


# ============================================================
# 31. DSA EXAMPLE
# ============================================================

arr = [10, 20, 30, 40, 50]

target = 30

found = False

for number in arr:

    if number == target:

        found = True

        break


print("Found:", found)


# ============================================================
# 32. VARIABLE NAMING IN DSA
# ============================================================

"""
For small loops:

for i in range(5):
    print(i)

i is perfectly normal.

For meaningful values:

target = 50
max_value = 100
student_count = 50

Use descriptive names.
"""


# ============================================================
# 33. INTERVIEW QUESTIONS
# ============================================================

"""
Q1. What is a variable?

A variable is a name/reference that refers to an object/value.


Q2. Is Python statically typed or dynamically typed?

Python is dynamically typed.


Q3. Can the same variable hold different types?

Yes.

Example:

x = 10
x = "Hello"


Q4. Is Python case-sensitive?

Yes.

name, Name and NAME are different identifiers.


Q5. Can a variable name start with a number?

No.


Q6. Can a variable name contain underscore?

Yes.

Example:

student_name


Q7. Can a variable name contain spaces?

No.


Q8. What is snake_case?

A naming convention where words are separated by
underscores.

Example:

student_name
total_marks
average_percentage


Q9. How do you swap two variables in Python?

a, b = b, a


Q10. What does input() return?

input() always returns a string.


Q11. What is None?

None represents the absence of a value.


Q12. What is id()?

id() returns the identity of an object during its lifetime.


Q13. What happens here?

a = [1, 2, 3]
b = a
b.append(4)

Both a and b refer to the same list,
so both show [1, 2, 3, 4].


Q14. What is the difference between:

b = a

and:

b = a.copy()

b = a:
Both refer to the same object.

b = a.copy():
Creates a separate shallow copy.
"""


# ============================================================
# 34. QUICK REVISION
# ============================================================

"""
VARIABLE:

name = "Harshad"


MULTIPLE ASSIGNMENT:

a, b, c = 10, 20, 30


SAME VALUE:

a = b = c = 10


DYNAMIC TYPING:

x = 10
x = "Hello"


SWAP:

a, b = b, a


CONSTANT CONVENTION:

MAX_SIZE = 100


DELETE:

del x


CHECK TYPE:

type(x)


CHECK INSTANCE:

isinstance(x, int)


OBJECT ID:

id(x)


NONE:

result = None


LIST REFERENCE:

b = a


LIST COPY:

b = a.copy()
"""


# ============================================================
#                         END
# ============================================================