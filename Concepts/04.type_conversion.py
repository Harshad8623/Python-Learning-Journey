# ============================================================
#                    TYPE CONVERSION IN PYTHON
# ============================================================

"""
Type conversion means converting a value from one data type
to another data type.

There are two main types:

1. Implicit Type Conversion
2. Explicit Type Conversion
"""


# ============================================================
# 1. BASIC DATA
# ============================================================

x = 10
age = 21
percentage = 97.85

num1 = "100"
num2 = "200.5"

print(type(x))
print(type(percentage))
print(type(num1))


# ============================================================
# 2. INTEGER -> FLOAT
# ============================================================

"""
int -> float

Example:

10 -> 10.0
"""

print("Integer to Float:", float(x))

print(type(float(x)))


# ============================================================
# 3. INTEGER -> STRING
# ============================================================

"""
int -> str

Example:

10 -> "10"
"""

print("Integer to String:", str(x))

print(type(str(x)))


# ============================================================
# 4. FLOAT -> INTEGER
# ============================================================

"""
float -> int

The decimal portion is truncated.

It does NOT round the number.

97.85 -> 97
"""

print("Float to Integer:", int(percentage))

print(int(97.85))
print(int(97.99))
print(int(-97.85))


# ============================================================
# 5. STRING -> INTEGER
# ============================================================

"""
A numeric string can be converted into an integer.

"100" -> 100
"""

print("String to Integer:", int(num1))

print(type(int(num1)))


# ============================================================
# 6. STRING -> FLOAT
# ============================================================

"""
A numeric string can be converted into a float.

"200.5" -> 200.5
"""

print("String to Float:", float(num2))

print(type(float(num2)))


# ============================================================
# 7. STRING -> INTEGER USING int()
# ============================================================

num = "500"

result = int(num)

print(result)

print(type(result))


# ============================================================
# 8. STRING FLOAT -> INTEGER
# ============================================================

"""
This is NOT valid:

int("200.5")

Because "200.5" is not a valid integer string.

Instead:

"200.5"
   ↓
float()
   ↓
200.5
   ↓
int()
   ↓
200
"""

num = "200.5"

result = int(float(num))

print(result)


# This would cause ValueError:

# print(int("200.5"))


# ============================================================
# 9. STRING -> BOOLEAN
# ============================================================

"""
IMPORTANT INTERVIEW CONCEPT:

Any NON-EMPTY string is True.

An EMPTY string is False.
"""

print(bool("Hello"))       # True
print(bool("Harshad"))     # True
print(bool("100"))         # True
print(bool("False"))       # True
print(bool("0"))           # True

print(bool(""))            # False


"""
Very important:

bool("False") -> True

Why?

Because "False" is a non-empty string.

Python does NOT interpret the text "False"
as the Boolean value False.
"""


# ============================================================
# 10. INTEGER -> BOOLEAN
# ============================================================

"""
0 -> False

Any non-zero integer -> True
"""

print(bool(0))       # False
print(bool(1))       # True
print(bool(10))      # True
print(bool(-10))     # True


# ============================================================
# 11. FLOAT -> BOOLEAN
# ============================================================

print(bool(0.0))     # False
print(bool(1.5))     # True
print(bool(-2.5))    # True


# ============================================================
# 12. BOOLEAN -> INTEGER
# ============================================================

"""
In Python:

True  behaves like 1
False behaves like 0
"""

print(int(True))     # 1
print(int(False))    # 0


# ============================================================
# 13. BOOLEAN -> FLOAT
# ============================================================

print(float(True))   # 1.0
print(float(False))  # 0.0


# ============================================================
# 14. BOOLEAN -> STRING
# ============================================================

print(str(True))     # "True"
print(str(False))    # "False"


# ============================================================
# 15. STRING -> BOOLEAN - COMMON TRAP
# ============================================================

value = "False"

print(bool(value))

# Output:
# True


"""
If you actually want to convert the text
"True"/"False" into Boolean:

"""

value = "False"

if value.lower() == "true":

    result = True

else:

    result = False


print(result)


# ============================================================
# 16. INTEGER -> INTEGER
# ============================================================

x = 10

print(int(x))


# ============================================================
# 17. FLOAT -> FLOAT
# ============================================================

x = 10.5

print(float(x))


# ============================================================
# 18. STRING -> STRING
# ============================================================

name = "Harshad"

print(str(name))


# ============================================================
# 19. IMPLICIT TYPE CONVERSION
# ============================================================

"""
Implicit conversion happens automatically.

Python converts a value to a compatible type
without us explicitly calling a conversion function.

Example:

int + float

The integer is converted to float.
"""

x = 10
percentage = 97.85

result = x + percentage

print(result)

print(type(result))


"""
10 + 97.85

10 is treated as:

10.0

Then:

10.0 + 97.85
= 107.85
"""


# ============================================================
# 20. INTEGER + FLOAT
# ============================================================

x = 10
y = 2.5

result = x + y

print(result)
print(type(result))


# ============================================================
# 21. INTEGER + BOOLEAN
# ============================================================

"""
Because:

True = 1
False = 0
"""

print(10 + True)      # 11
print(10 + False)     # 10


# ============================================================
# 22. EXPLICIT TYPE CONVERSION
# ============================================================

"""
Explicit conversion means WE tell Python
to convert the type.

Common functions:

int()
float()
str()
bool()
list()
tuple()
set()
dict()
"""

percentage = 97.85

print(int(percentage))


# ============================================================
# 23. STRING -> LIST
# ============================================================

"""
list() converts an iterable into a list.

A string is iterable character by character.
"""

name = "Harshad"

result = list(name)

print(result)


# Output:

# ['H', 'a', 'r', 's', 'h', 'a', 'd']


# ============================================================
# 24. STRING -> TUPLE
# ============================================================

name = "Python"

result = tuple(name)

print(result)


# ============================================================
# 25. STRING -> SET
# ============================================================

"""
A set removes duplicate values.
"""

name = "banana"

result = set(name)

print(result)


# ============================================================
# 26. LIST -> TUPLE
# ============================================================

numbers = [1, 2, 3, 4]

result = tuple(numbers)

print(result)


# ============================================================
# 27. TUPLE -> LIST
# ============================================================

numbers = (1, 2, 3, 4)

result = list(numbers)

print(result)


# ============================================================
# 28. LIST -> SET
# ============================================================

numbers = [1, 2, 2, 3, 3, 4]

result = set(numbers)

print(result)


"""
Output:

{1, 2, 3, 4}

Duplicates are removed.
"""


# ============================================================
# 29. SET -> LIST
# ============================================================

numbers = {1, 2, 3, 4}

result = list(numbers)

print(result)


# ============================================================
# 30. TUPLE -> SET
# ============================================================

numbers = (1, 2, 2, 3)

result = set(numbers)

print(result)


# ============================================================
# 31. DICTIONARY -> LIST
# ============================================================

student = {
    "name": "Harshad",
    "age": 21
}

result = list(student)

print(result)


"""
Converting a dictionary to a list gives its KEYS.
"""


# ============================================================
# 32. DICTIONARY KEYS / VALUES
# ============================================================

student = {
    "name": "Harshad",
    "age": 21
}

print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))


# ============================================================
# 33. CONVERTING USER INPUT
# ============================================================

"""
Remember:

input() always returns a string.

Therefore:

n = int(input())

is very common.
"""

age = int(input("Enter age: "))

print(age)
print(type(age))


# ============================================================
# 34. DSA INPUT CONVERSION
# ============================================================

"""
VERY IMPORTANT:

Input:

10 20 30 40 50

We want:

[10, 20, 30, 40, 50]
"""

numbers = list(map(int, input("Enter numbers: ").split()))

print(numbers)


"""
Breakdown:

input()
    ↓
"10 20 30 40 50"

split()
    ↓
["10", "20", "30", "40", "50"]

map(int, ...)
    ↓
10, 20, 30, 40, 50

list(...)
    ↓
[10, 20, 30, 40, 50]
"""


# ============================================================
# 35. TWO INTEGER INPUTS
# ============================================================

a, b = map(int, input("Enter two numbers: ").split())

print(a)
print(b)


# ============================================================
# 36. FLOAT LIST INPUT
# ============================================================

numbers = list(map(float, input("Enter numbers: ").split()))

print(numbers)


# ============================================================
# 37. TYPE CONVERSION ERROR
# ============================================================

"""
Invalid conversions produce errors.

Examples:

int("abc")
float("hello")
int("10.5")

These cause ValueError.
"""

# Uncomment to test:

# print(int("abc"))
# print(float("hello"))
# print(int("10.5"))


# ============================================================
# 38. HANDLING CONVERSION ERRORS
# ============================================================

try:

    number = int(input("Enter an integer: "))

    print("Number:", number)

except ValueError:

    print("Invalid integer.")


# ============================================================
# 39. CONVERTING DECIMAL STRING
# ============================================================

value = "98.75"

number = float(value)

print(number)


# ============================================================
# 40. FLOAT -> INT DOES NOT ROUND
# ============================================================

print(int(10.9))     # 10
print(int(10.1))     # 10

"""
If you want rounding:

round()
"""

print(round(10.9))   # 11
print(round(10.1))   # 10


# ============================================================
# 41. int() TRUNCATES TOWARD ZERO
# ============================================================

print(int(5.9))      # 5
print(int(-5.9))     # -5


"""
This is different from floor division:

-5 // 2 = -3
"""


# ============================================================
# 42. TYPE CHECKING
# ============================================================

"""
type() tells us the exact type of an object.
"""

x = 10

print(type(x))


# ============================================================
# 43. isinstance()
# ============================================================

"""
isinstance() checks whether an object
belongs to a particular type.

It is often more useful than type() ==.
"""

x = 10

print(isinstance(x, int))

print(isinstance(x, float))

print(isinstance(x, (int, float)))


# ============================================================
# 44. TYPE CONVERSION IN EXPRESSIONS
# ============================================================

x = "10"
y = "20"

"""
This:

x + y

performs string concatenation.
"""

print(x + y)

# Output:
# 1020


"""
Convert them first:

"""

print(int(x) + int(y))

# Output:
# 30


# ============================================================
# 45. COMMON INTERVIEW TRAP
# ============================================================

x = "10"
y = "20"

print(x + y)

"""
Output:

1020

NOT:

30

Because both are strings.
"""


# ============================================================
# 46. ANOTHER COMMON TRAP
# ============================================================

x = 10
y = 20

print(str(x) + str(y))

# Output:
# 1020


# ============================================================
# 47. TYPE CONVERSION + CONDITIONAL
# ============================================================

age = int(input("Enter age: "))

if age >= 18:

    print("Adult")

else:

    print("Minor")


# ============================================================
# 48. TYPE CONVERSION + LOOP
# ============================================================

numbers = list(map(int, input("Enter numbers: ").split()))

for num in numbers:

    print(num)


# ============================================================
# 49. TYPE CONVERSION + DSA
# ============================================================

numbers = list(map(int, input("Enter numbers: ").split()))

total = 0

for num in numbers:

    total += num

print("Sum:", total)


# ============================================================
# 50. TYPE CONVERSION + SEARCH
# ============================================================

numbers = list(map(int, input("Enter numbers: ").split()))

target = int(input("Enter target: "))

for num in numbers:

    if num == target:

        print("Found")

        break


# ============================================================
# 51. IMPORTANT INTERVIEW QUESTIONS
# ============================================================

"""
Q1. What is type conversion?

Changing a value from one data type to another.


Q2. What are the two types of type conversion?

1. Implicit
2. Explicit


Q3. What is implicit conversion?

Python automatically converts one type into another
when appropriate.

Example:

10 + 2.5

The integer is promoted to float.


Q4. What is explicit conversion?

The programmer manually converts a value.

Examples:

int()
float()
str()
bool()


Q5. What does int(10.9) return?

10


Q6. What does int(-10.9) return?

-10

int() truncates toward zero.


Q7. What does bool(0) return?

False


Q8. What does bool(1) return?

True


Q9. What does bool("") return?

False


Q10. What does bool("False") return?

True

Because the string is not empty.


Q11. What does input() return?

Always a string.


Q12. How do you take an integer input?

int(input())


Q13. How do you take an integer list?

list(map(int, input().split()))


Q14. What happens when you do:

int("abc")?

ValueError


Q15. Difference between int() and round()?

int() truncates toward zero.

round() rounds according to Python's rounding rules.


Q16. What does isinstance() do?

Checks whether an object is an instance of
a specified type or types.
"""


# ============================================================
# 52. QUICK REVISION
# ============================================================

"""
BASIC CONVERSION:

int(x)
float(x)
str(x)
bool(x)


COLLECTION CONVERSION:

list(x)
tuple(x)
set(x)


TYPE CHECKING:

type(x)

isinstance(x, int)


COMMON INPUT:

n = int(input())


MULTIPLE INPUT:

a, b = map(int, input().split())


LIST INPUT:

arr = list(map(int, input().split()))


FLOAT LIST:

arr = list(map(float, input().split()))


IMPORTANT:

input() -> always str


IMPORTANT BOOL:

bool(0)       -> False
bool(1)       -> True
bool("")      -> False
bool("False") -> True


IMPORTANT FLOAT:

int(10.9)  -> 10
int(-10.9) -> -10


IMPORTANT:

int("10")    -> 10
float("10.5") -> 10.5

int("10.5")  -> ValueError
"""


# ============================================================
#                         END
# ============================================================