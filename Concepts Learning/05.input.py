# ============================================================
#                     INPUT IN PYTHON
# ============================================================

"""
input() is used to take input from the user.

Syntax:

input()

or

input("message")

IMPORTANT:

input() ALWAYS returns a STRING.

Even if the user enters:

10

Python receives:

"10"

If you need a number, you must convert it.
"""


# ============================================================
# 1. BASIC INPUT
# ============================================================

name = input("Enter Your Name: ")

print("Hello, " + name + "!")


# ============================================================
# 2. input() ALWAYS RETURNS STRING
# ============================================================

age = input("Enter your age: ")

print(age)
print(type(age))


"""
If you enter:

21

Output:

21
<class 'str'>
"""


# ============================================================
# 3. STRING INPUT
# ============================================================

name = input("Enter your name: ")

print("Name:", name)

print(type(name))


# ============================================================
# 4. INTEGER INPUT
# ============================================================

"""
Convert string to integer using int().
"""

age = int(input("Enter your age: "))

print("Age:", age)

print(type(age))


# ============================================================
# 5. FLOAT INPUT
# ============================================================

salary = float(input("Enter your salary: "))

print("Salary:", salary)

print(type(salary))


# ============================================================
# 6. BOOLEAN INPUT - IMPORTANT
# ============================================================

"""
DO NOT do this:

is_student = bool(input("Are you a student? "))

Because:

bool("False") -> True

Any non-empty string is True.

Instead, check the input explicitly.
"""

answer = input("Are you a student? ")

if answer.lower() == "yes":

    is_student = True

else:

    is_student = False


print(is_student)


# ============================================================
# 7. TWO INTEGER INPUTS
# ============================================================

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)


# ============================================================
# 8. THREE INTEGER INPUTS
# ============================================================

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Sum:", a + b + c)


# ============================================================
# 9. MULTIPLE INPUTS USING split()
# ============================================================

"""
Suppose input is:

10 20 30

input() gives:

"10 20 30"

split() separates it into:

["10", "20", "30"]
"""

a, *b, c = (10, 20,30,40,50) # tuple
print(a, b, c)  # 10, [20, 30, 40], 50

a, *b, c = [10, 20,30,40,50] # list
print(a, b, c)  # 10, [20, 30, 40], 50


values = input("Enter numbers: ").split()

print(values)


"""
Important:

split() returns strings.
"""


# ============================================================
# 10. MULTIPLE INTEGER INPUTS
# ============================================================

"""
Convert each value to int using map().
"""

numbers = list(map(int, input("Enter numbers: ").split()))

print(numbers)


"""
If input is:

10 20 30 40

numbers becomes:

[10, 20, 30, 40]
"""


# ============================================================
# 11. TWO INTEGER INPUTS - VERY IMPORTANT DSA PATTERN
# ============================================================

a, b = map(int, input("Enter two numbers: ").split())

print(a)
print(b)

print("Sum:", a + b)


"""
This is VERY common in coding platforms.

Input:

10 20

Code:

a, b = map(int, input().split())
"""


# ============================================================
# 12. THREE INTEGER INPUTS
# ============================================================

a, b, c = map(int, input().split())

print(a, b, c)


# ============================================================
# 13. LIST INPUT
# ============================================================

"""
Very common in DSA.

Input:

1 2 3 4 5

Code:

"""

numbers = list(map(int, input().split()))

print(numbers)


# ============================================================
# 14. STRING LIST INPUT
# ============================================================

"""
Input:

Apple Mango Banana Orange
"""

fruits = input().split()

print(fruits)


# Output:

# ['Apple', 'Mango', 'Banana', 'Orange']


# ============================================================
# 15. split() WITH CUSTOM SEPARATOR
# ============================================================

"""
By default:

split()

splits on whitespace.

You can also specify a separator.
"""

data = "10,20,30,40"

numbers = data.split(",")

print(numbers)


# Output:

# ['10', '20', '30', '40']


# ============================================================
# 16. map()
# ============================================================

"""
map(function, iterable)

map() applies a function to every item.

Example:

map(int, ["10", "20", "30"])

becomes an iterator containing:

10
20
30
"""

numbers = list(map(int, ["10", "20", "30"]))

print(numbers)


# ============================================================
# 17. map() + split() + list()
# ============================================================

numbers = list(map(int, input("Enter numbers: ").split()))

print(numbers)


"""
This line is EXTREMELY IMPORTANT for DSA.

Memorize the pattern:

list(map(int, input().split()))
"""


# ============================================================
# 18. INPUT AND LOOP
# ============================================================

n = int(input("Enter n: "))

for i in range(n):

    print(i)


"""
If input:

5

Output:

0
1
2
3
4
"""


# ============================================================
# 19. INPUT + LIST + LOOP
# ============================================================

numbers = list(map(int, input("Enter numbers: ").split()))

for num in numbers:

    print(num)


# ============================================================
# 20. FIND SUM FROM INPUT LIST
# ============================================================

numbers = list(map(int, input("Enter numbers: ").split()))

total = 0

for num in numbers:

    total += num

print("Sum:", total)


# ============================================================
# 21. FIND MAXIMUM FROM INPUT LIST
# ============================================================

numbers = list(map(int, input("Enter numbers: ").split()))

maximum = numbers[0]

for num in numbers:

    if num > maximum:

        maximum = num

print("Maximum:", maximum)


# ============================================================
# 22. FIND EVEN NUMBERS FROM INPUT
# ============================================================

numbers = list(map(int, input("Enter numbers: ").split()))

for num in numbers:

    if num % 2 == 0:

        print(num)


# ============================================================
# 23. INPUT WITH strip()
# ============================================================

"""
strip() removes leading and trailing whitespace.
"""

name = input("Enter your name: ").strip()

print("Hello", name)


"""
Example:

Input:

   Harshad

After strip():

Harshad
"""


# ============================================================
# 24. LOWERCASE INPUT
# ============================================================

answer = input("Enter yes/no: ").strip().lower()

if answer == "yes":

    print("You selected yes.")

else:

    print("You selected no.")


# ============================================================
# 25. UPPERCASE INPUT
# ============================================================

city = input("Enter city: ").strip().upper()

print(city)


# ============================================================
# 26. INPUT VALIDATION
# ============================================================

"""
Sometimes users enter invalid input.

Example:

int("abc")

causes:

ValueError
"""

try:

    age = int(input("Enter your age: "))

    print("Age:", age)

except ValueError:

    print("Please enter a valid integer.")


# ============================================================
# 27. MULTIPLE INPUT WITH VALIDATION
# ============================================================

try:

    a, b = map(int, input("Enter two numbers: ").split())

    print("Sum:", a + b)

except ValueError:

    print("Please enter exactly two integers.")


# ============================================================
# 28. INPUT FROM A SINGLE LINE
# ============================================================

"""
Suppose the input is:

10 20 30

We can process everything from one line.
"""

numbers = list(map(int, input().split()))

print(numbers)


# ============================================================
# 29. INPUT FORMAT COMMON IN CODING PLATFORMS
# ============================================================

"""
Example input:

5
10 20 30 40 50

First line = number of elements
Second line = elements
"""

n = int(input())

numbers = list(map(int, input().split()))

print("N =", n)
print("Numbers =", numbers)


# ============================================================
# 30. INPUT WITH N ELEMENTS
# ============================================================

n = int(input())

numbers = list(map(int, input().split()))

"""
Usually we expect:

len(numbers) == n
"""

print("Number of elements:", len(numbers))


# ============================================================
# 31. INPUT MATRIX
# ============================================================

"""
Example input:

3
1 2 3
4 5 6
7 8 9
"""

n = int(input())

matrix = []

for i in range(n):

    row = list(map(int, input().split()))

    matrix.append(row)


print(matrix)


# ============================================================
# 32. MATRIX INPUT WITH ROWS AND COLUMNS
# ============================================================

"""
Example:

3 3

1 2 3
4 5 6
7 8 9
"""

rows, cols = map(int, input().split())

matrix = []

for i in range(rows):

    row = list(map(int, input().split()))

    matrix.append(row)


print(matrix)


# ============================================================
# 33. FAST INPUT USING sys.stdin
# ============================================================

"""
For normal beginner programs:

input()

is enough.

For competitive programming / large input,
sys.stdin.readline() can be useful.
"""

import sys

name = sys.stdin.readline().strip()

print(name)


# ============================================================
# 34. sys.stdin.readline()
# ============================================================

"""
readline() reads one line.

It usually includes the newline character.

Therefore:

.strip()

is commonly used.
"""

name = sys.stdin.readline().strip()

print("Hello", name)


# ============================================================
# 35. FAST INTEGER INPUT
# ============================================================

import sys

n = int(sys.stdin.readline())

print(n)


# ============================================================
# 36. FAST LIST INPUT
# ============================================================

import sys

numbers = list(map(int, sys.stdin.readline().split()))

print(numbers)


# ============================================================
# 37. input() VS sys.stdin.readline()
# ============================================================

"""
input():

- Easy to use
- Beginner friendly
- Good for most coding problems
- Automatically removes the newline


sys.stdin.readline():

- Reads directly from standard input
- Useful for large input
- Often used in competitive programming
- Usually requires .strip() when you don't want newline


For now:

Use input().

Learn sys.stdin.readline() when you start
competitive programming.
"""


# ============================================================
# 38. IMPORTANT DSA INPUT PATTERN
# ============================================================

"""
You should memorize these patterns.
"""


# Pattern 1: Single integer

n = int(input())


# Pattern 2: Two integers

a, b = map(int, input().split())


# Pattern 3: Multiple integers

numbers = list(map(int, input().split()))


# Pattern 4: String list

words = input().split()


# Pattern 5: Matrix row

row = list(map(int, input().split()))


# ============================================================
# 39. INPUT + FUNCTION
# ============================================================

def add(a, b):

    return a + b


a, b = map(int, input("Enter two numbers: ").split())

result = add(a, b)

print("Sum:", result)


# ============================================================
# 40. INPUT + CONDITIONAL
# ============================================================

age = int(input("Enter age: "))

if age >= 18:

    print("Adult")

else:

    print("Minor")


# ============================================================
# 41. INPUT + LOOP + CONDITION
# ============================================================

numbers = list(map(int, input("Enter numbers: ").split()))

for num in numbers:

    if num % 2 == 0:

        print(num, "is even.")

    else:

        print(num, "is odd.")


# ============================================================
# 42. INPUT + SEARCH
# ============================================================

numbers = list(map(int, input("Enter numbers: ").split()))

target = int(input("Enter target: "))

found = False

for num in numbers:

    if num == target:

        found = True

        break


if found:

    print("Target found.")

else:

    print("Target not found.")


# ============================================================
# 43. INPUT + TWO POINTER
# ============================================================

numbers = list(map(int, input("Enter sorted numbers: ").split()))

left = 0
right = len(numbers) - 1

while left < right:

    print(numbers[left], numbers[right])

    left += 1
    right -= 1


# ============================================================
# 44. INPUT + FREQUENCY COUNT
# ============================================================

numbers = list(map(int, input("Enter numbers: ").split()))

target = int(input("Enter target: "))

count = 0

for num in numbers:

    if num == target:

        count += 1


print("Frequency:", count)


# ============================================================
# 45. IMPORTANT INTERVIEW QUESTIONS
# ============================================================

"""
Q1. What does input() return?

Answer:

A string.


Q2. How do you take integer input?

int(input())


Q3. How do you take float input?

float(input())


Q4. How do you take multiple integers in one line?

a, b = map(int, input().split())


Q5. How do you take a list of integers?

numbers = list(map(int, input().split()))


Q6. What does split() do?

It splits a string into a list based on a separator.


Q7. What does map() do?

It applies a function to every item of an iterable
and returns a map iterator.


Q8. Why do we use list() with map()?

To convert the map iterator into a list.


Q9. What is the difference between:

input().split()

and:

list(map(int, input().split()))

First:

["10", "20", "30"]

Second:

[10, 20, 30]


Q10. What happens if we do:

int("abc")?

ValueError.


Q11. Why use strip()?

To remove leading and trailing whitespace.


Q12. What is sys.stdin.readline()?

It reads a line from standard input and is commonly
used when handling large input efficiently.


Q13. How do you take matrix input?

Use a loop and read each row.


Q14. Is input() suitable for DSA?

Yes, absolutely for normal coding problems.
For very large input, sys.stdin.readline() can be useful.
"""


# ============================================================
# 46. QUICK REVISION
# ============================================================

"""
SINGLE STRING:

name = input()


INTEGER:

n = int(input())


FLOAT:

x = float(input())


TWO INTEGERS:

a, b = map(int, input().split())


LIST OF INTEGERS:

arr = list(map(int, input().split()))


LIST OF STRINGS:

arr = input().split()


REMOVE EXTRA SPACES:

name = input().strip()


LOWERCASE:

name = input().lower()


FAST INPUT:

import sys

n = int(sys.stdin.readline())


FAST LIST INPUT:

arr = list(map(int, sys.stdin.readline().split()))
"""


# ============================================================
#                         END
# ============================================================