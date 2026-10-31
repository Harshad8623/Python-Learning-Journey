# ============================================================
#                        PYTHON LOOPS
# ============================================================

"""
Loops are used to execute a block of code repeatedly.

Python mainly has two types of loops:

1. while loop
2. for loop


Important loop concepts:

- while
- for
- range()
- break
- continue
- pass
- nested loops
- enumerate()
- zip()
- loop else
- iterating over strings
- iterating over lists
- iterating over tuples
- iterating over sets
- iterating over dictionaries
"""


# ============================================================
# 1. WHILE LOOP
# ============================================================

"""
Syntax:

while condition:
    # code

The loop continues as long as the condition is True.
"""

a = 1

while a <= 5:

    print(a)

    a += 1


# Output:
# 1
# 2
# 3
# 4
# 5


# ============================================================
# 2. WHILE LOOP WITH DECREMENT
# ============================================================

a = 10

while a > 0:

    print(a)

    a -= 1


# ============================================================
# 3. INFINITE WHILE LOOP
# ============================================================

"""
while True:

    # code

This creates an infinite loop.

We generally use break to stop it.
"""

# Example:

# while True:
#     print("Hello")


# ============================================================
# 4. WHILE TRUE + BREAK
# ============================================================

while True:

    user_input = input("Enter 'exit' to stop: ")

    if user_input.lower() == "exit":
        break

    print("You entered:", user_input)


# ============================================================
# 5. FOR LOOP
# ============================================================

"""
A for loop is used to iterate over an iterable.

Examples of iterables:

- list
- tuple
- string
- set
- dictionary
- range()
"""

for i in range(5):

    print(i)


# Output:
# 0
# 1
# 2
# 3
# 4


# ============================================================
# 6. LOOP THROUGH STRING
# ============================================================

name = "Harshad"

for char in name:

    print(char)


# ============================================================
# 7. LOOP THROUGH LIST
# ============================================================

numbers = [10, 20, 30, 40, 50]

for num in numbers:

    print(num)


# ============================================================
# 8. LOOP THROUGH TUPLE
# ============================================================

numbers = (10, 20, 30, 40)

for num in numbers:

    print(num)


# ============================================================
# 9. LOOP THROUGH SET
# ============================================================

numbers = {10, 20, 30, 40}

for num in numbers:

    print(num)


"""
NOTE:

Sets are unordered collections.

Therefore, don't rely on the order in which
elements are printed.
"""


# ============================================================
# 10. LOOP THROUGH DICTIONARY
# ============================================================

student = {
    "name": "Harshad",
    "age": 21,
    "city": "Latur"
}


# By default, looping through a dictionary
# gives the keys.

for key in student:

    print(key)


# ============================================================
# 11. DICTIONARY VALUES
# ============================================================

for value in student.values():

    print(value)


# ============================================================
# 12. DICTIONARY KEY + VALUE
# ============================================================

for key, value in student.items():

    print(key, ":", value)


# ============================================================
# 13. range()
# ============================================================

"""
range() generates a sequence of numbers.

Syntax:

range(stop)

range(start, stop)

range(start, stop, step)
"""


# ------------------------------------------------------------
# range(stop)
# ------------------------------------------------------------

for i in range(5):

    print(i)


# 0 1 2 3 4


# ------------------------------------------------------------
# range(start, stop)
# ------------------------------------------------------------

for i in range(1, 6):

    print(i)


# 1 2 3 4 5


# ------------------------------------------------------------
# range(start, stop, step)
# ------------------------------------------------------------

for i in range(1, 11, 2):

    print(i)


# 1 3 5 7 9


# ============================================================
# 14. REVERSE range()
# ============================================================

for i in range(10, 0, -1):

    print(i)


# 10 9 8 7 6 5 4 3 2 1


# ============================================================
# 15. EVEN NUMBERS USING range()
# ============================================================

for i in range(2, 11, 2):
    print(i)


# 2 4 6 8 10


# ============================================================
# 16. ODD NUMBERS USING range()
# ============================================================

for i in range(1, 11, 2):

    print(i)


# 1 3 5 7 9


# ============================================================
# 17. BREAK
# ============================================================

"""
break immediately terminates the loop.
"""

for i in range(1, 11):

    if i == 5:
        break

    print(i)


# Output:
# 1
# 2
# 3
# 4


# ============================================================
# 18. CONTINUE
# ============================================================

"""
continue skips the current iteration
and moves to the next iteration.
"""

for i in range(1, 11):

    if i == 5:
        continue

    print(i)


# Output:
# 1 2 3 4 6 7 8 9 10


# ============================================================
# 19. PASS
# ============================================================

"""
pass does nothing.

It is mainly used as a placeholder.
"""

for i in range(5):

    pass


# Example:

def future_function():

    pass


# ============================================================
# 20. BREAK VS CONTINUE VS PASS
# ============================================================

"""
break
-----
Stops the entire loop.


continue
--------
Skips the current iteration.


pass
----
Does nothing.
"""


# ============================================================
# 21. NESTED LOOPS
# ============================================================

"""
A loop inside another loop is called
a nested loop.
"""

for i in range(3):

    for j in range(3):

        print(i, j)


# ============================================================
# 22. NESTED LOOP - STAR PATTERN
# ============================================================

for i in range(5):

    for j in range(5):

        print("*", end=" ")

    print()


# ============================================================
# 23. NESTED LOOP - TRIANGLE
# ============================================================

for i in range(1, 6):

    for j in range(i):

        print("*", end=" ")

    print()


# ============================================================
# 24. LOOP WITH INDEX
# ============================================================

numbers = [10, 20, 30, 40, 50]

for i in range(len(numbers)):

    print(i, numbers[i])


# Output:
# 0 10
# 1 20
# 2 30
# 3 40
# 4 50


# ============================================================
# 25. enumerate()
# ============================================================

"""
enumerate() gives:

index + value

This is usually cleaner than:

for i in range(len(numbers)):
"""


numbers = [10, 20, 30, 40, 50]

for index, value in enumerate(numbers):

    print(index, value)


# ============================================================
# 26. enumerate() WITH START
# ============================================================

numbers = ["A", "B", "C"]

for index, value in enumerate(numbers, start=1):

    print(index, value)


# Output:
# 1 A
# 2 B
# 3 C


# ============================================================
# 27. zip()
# ============================================================

"""
zip() allows us to iterate through
multiple iterables simultaneously.
"""

names = ["Harshad", "Rahul", "Sanjay"]

marks = [85, 90, 78]

for name, mark in zip(names, marks):

    print(name, mark)


# ============================================================
# 28. zip() WITH THREE LISTS
# ============================================================

names = ["Harshad", "Rahul", "Sanjay"]

marks = [85, 90, 78]

cities = ["Latur", "Pune", "Nanded"]


for name, mark, city in zip(names, marks, cities):

    print(name, mark, city)


# ============================================================
# 29. LOOP ELSE
# ============================================================

"""
Python allows else with loops.

The else block executes when the loop
finishes normally.

If the loop is terminated by break,
the else block does NOT execute.
"""


for i in range(5):

    print(i)

else:

    print("Loop completed normally")


# ============================================================
# 30. LOOP ELSE WITH BREAK
# ============================================================

for i in range(5):

    if i == 3:

        break

    print(i)

else:

    print("Loop completed")


"""
Output:

0
1
2

The else block doesn't execute because
break stopped the loop.
"""


# ============================================================
# 31. SEARCH USING LOOP
# ============================================================

numbers = [10, 20, 30, 40, 50]

target = 30

found = False

for num in numbers:

    if num == target:

        found = True
        break


print(found)


# ============================================================
# 32. SEARCH USING for-else
# ============================================================

numbers = [10, 20, 30, 40, 50]

target = 30


for num in numbers:

    if num == target:

        print("Found")
        break

else:

    print("Not Found")


# ============================================================
# 33. COUNT EVEN NUMBERS
# ============================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

count = 0

for num in numbers:

    if num % 2 == 0:

        count += 1


print("Even count:", count)


# ============================================================
# 34. SUM OF LIST
# ============================================================

numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:

    total += num


print("Sum:", total)


# ============================================================
# 35. FIND MAXIMUM WITHOUT max()
# ============================================================

numbers = [10, 50, 20, 80, 30]

maximum = numbers[0]

for num in numbers:

    if num > maximum:

        maximum = num


print("Maximum:", maximum)


# ============================================================
# 36. FIND MINIMUM WITHOUT min()
# ============================================================

numbers = [10, 50, 20, 80, 30]

minimum = numbers[0]

for num in numbers:

    if num < minimum:

        minimum = num


print("Minimum:", minimum)


# ============================================================
# 37. REVERSE A LIST USING LOOP
# ============================================================

numbers = [1, 2, 3, 4, 5]

reverse = []

for i in range(len(numbers) - 1, -1, -1):

    reverse.append(numbers[i])


print(reverse)


# ============================================================
# 38. REVERSE STRING USING LOOP
# ============================================================

text = "Harshad"

reverse = ""

for char in text:

    reverse = char + reverse


print(reverse)


# ============================================================
# 39. COUNT VOWELS
# ============================================================

text = "programming"

count = 0

for char in text:

    if char.lower() in "aeiou":

        count += 1


print("Vowels:", count)


# ============================================================
# 40. COUNT CHARACTERS
# ============================================================

text = "hello"

count = 0

for char in text:

    count += 1


print(count)


# ============================================================
# 41. FIND FACTORS
# ============================================================

num = 12

for i in range(1, num + 1):

    if num % i == 0:

        print(i)


# ============================================================
# 42. PRIME NUMBER USING LOOP
# ============================================================

num = 17

is_prime = True

if num < 2:

    is_prime = False

else:

    for i in range(2, num):

        if num % i == 0:

            is_prime = False
            break


print(is_prime)


# ============================================================
# 43. OPTIMIZED PRIME CHECK
# ============================================================

num = 97

is_prime = True

if num < 2:

    is_prime = False

else:

    i = 2

    while i * i <= num:

        if num % i == 0:

            is_prime = False
            break

        i += 1


print(is_prime)


# ============================================================
# 44. MULTIPLICATION TABLE
# ============================================================

num = 5

for i in range(1, 11):

    print(num, "x", i, "=", num * i)


# ============================================================
# 45. FACTORIAL USING LOOP
# ============================================================

num = 5

factorial = 1

for i in range(1, num + 1):

    factorial *= i


print("Factorial:", factorial)


# ============================================================
# 46. FIBONACCI SERIES
# ============================================================

"""
0 1 1 2 3 5 8 13 ...
"""

n = 10

a = 0
b = 1

for i in range(n):

    print(a, end=" ")

    a, b = b, a + b

print()


# ============================================================
# 47. NESTED LOOP - MATRIX
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


for row in matrix:

    for value in row:

        print(value, end=" ")

    print()


# ============================================================
# 48. MATRIX USING INDEX
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


for i in range(len(matrix)):

    for j in range(len(matrix[i])):

        print(matrix[i][j], end=" ")

    print()


# ============================================================
# 49. MAIN DIAGONAL OF MATRIX
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


for i in range(len(matrix)):

    print(matrix[i][i])


# Output:
# 1
# 5
# 9


# ============================================================
# 50. SUM OF MATRIX
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total = 0

for row in matrix:

    for value in row:

        total += value


print("Matrix sum:", total)


# ============================================================
# 51. LOOP + LIST COMPREHENSION
# ============================================================

"""
Normal loop:

squares = []

for x in range(1, 6):

    squares.append(x * x)
"""


squares = [x * x for x in range(1, 6)]

print(squares)


# ============================================================
# 52. LIST COMPREHENSION WITH CONDITION
# ============================================================

even_numbers = [
    x
    for x in range(1, 11)
    if x % 2 == 0
]

print(even_numbers)


# ============================================================
# 53. BREAK IN NESTED LOOP
# ============================================================

"""
Important:

break only breaks the CURRENT loop.

It does not automatically break all
outer loops.
"""


for i in range(3):

    for j in range(3):

        if j == 1:

            break

        print(i, j)


# ============================================================
# 54. CONTINUE IN NESTED LOOP
# ============================================================

for i in range(3):

    for j in range(3):

        if j == 1:

            continue

        print(i, j)


# ============================================================
# 55. WHILE LOOP WITH USER INPUT
# ============================================================

"""
Useful pattern for menu-driven programs.
"""

# Uncomment to run:

# while True:
#
#     print("1. Add")
#     print("2. Exit")
#
#     choice = input("Enter choice: ")
#
#     if choice == "1":
#         print("Add selected")
#
#     elif choice == "2":
#         break
#
#     else:
#         print("Invalid choice")


# ============================================================
# 56. COMMON LOOP MISTAKE - INFINITE LOOP
# ============================================================

"""
Wrong:

a = 1

while a <= 10:

    print(a)

    # Forgot:
    # a += 1


Correct:

a = 1

while a <= 10:

    print(a)

    a += 1
"""


# ============================================================
# 57. COMMON LOOP MISTAKE - OFF BY ONE
# ============================================================

"""
Remember:

range(start, stop)

STOP is EXCLUDED.

range(1, 5)

produces:

1 2 3 4

NOT:

1 2 3 4 5
"""


# ============================================================
# 58. LOOP TIME COMPLEXITY
# ============================================================

"""
One loop:

for i in range(n):
    ...

Time Complexity:
O(n)


Two nested loops:

for i in range(n):
    for j in range(n):
        ...

Time Complexity:
O(n²)


Three nested loops:

for i in range(n):
    for j in range(n):
        for k in range(n):
            ...

Time Complexity:
O(n³)


Two separate loops:

for i in range(n):
    ...

for j in range(n):
    ...

Time:

O(n) + O(n)

= O(2n)

Drop constant:

O(n)


IMPORTANT:

Nested loops -> usually multiply

Separate loops -> usually add
"""


# ============================================================
# 59. LOOP + DSA EXAMPLE
# ============================================================

"""
Problem:

Find whether target exists in a list.

This is Linear Search.
"""

numbers = [10, 20, 30, 40, 50]

target = 40

for i in range(len(numbers)):

    if numbers[i] == target:

        print("Found at index:", i)
        break

else:

    print("Not found")


# Time Complexity:
# O(n)


# ============================================================
# 60. TWO POINTER BASIC LOOP IDEA
# ============================================================

"""
This is an important DSA pattern.

Start from both ends.
"""

numbers = [1, 2, 3, 4, 5]

left = 0
right = len(numbers) - 1

while left < right:

    print(
        "Left:",
        numbers[left],
        "Right:",
        numbers[right]
    )

    left += 1
    right -= 1


# ============================================================
# 61. TWO POINTER - CHECK PALINDROME
# ============================================================

text = "madam"

left = 0
right = len(text) - 1

is_palindrome = True

while left < right:

    if text[left] != text[right]:

        is_palindrome = False
        break

    left += 1
    right -= 1


print(is_palindrome)


# ============================================================
# 62. SLIDING WINDOW BASIC IDEA
# ============================================================

"""
Example:

Find sum of every window of size k.

This introduces an important DSA pattern.
"""

numbers = [1, 2, 3, 4, 5]

k = 3

window_sum = sum(numbers[:k])

print(window_sum)

for i in range(k, len(numbers)):

    window_sum += numbers[i]
    window_sum -= numbers[i - k]

    print(window_sum)



# ============================================================
# for loop (infinite times)
# ============================================================

import itertools

# Generates numbers 0, 1, 2, 3... infinitely
for i in itertools.count(start=0, step=1):
    print(i)
    
    # Example exit condition to prevent crashing your system
    if i >= 1000:
        break



# ============================================================
# 63. IMPORTANT LOOP PATTERNS FOR DSA
# ============================================================

"""
You should become comfortable with:

1. Forward loop

for i in range(n):


2. Reverse loop

for i in range(n - 1, -1, -1):


3. Loop through values

for value in numbers:


4. Loop through index

for i in range(len(numbers)):


5. Index + value

for i, value in enumerate(numbers):


6. Two arrays simultaneously

for a, b in zip(arr1, arr2):


7. Two pointers

left = 0
right = len(arr) - 1

while left < right:


8. Nested loops

for i in range(n):
    for j in range(n):


9. Search with break

for x in arr:

    if x == target:
        break


10. Search with for-else

for x in arr:

    if x == target:
        break

else:
    print("Not found")
"""


# ============================================================
# 64. INTERVIEW QUESTIONS
# ============================================================

"""
Q1. What are the types of loops in Python?

Answer:

1. for loop
2. while loop


Q2. Difference between for and while?

for:
    Generally used when iterating over
    a sequence or known range.

while:
    Used when repetition depends on
    a condition.


Q3. What does range() do?

It generates a sequence of numbers.


Q4. Is stop included in range()?

NO.

range(1, 5)

=> 1, 2, 3, 4


Q5. What does break do?

Terminates the current loop immediately.


Q6. What does continue do?

Skips the current iteration.


Q7. What does pass do?

Does nothing; it acts as a placeholder.


Q8. What is a nested loop?

A loop inside another loop.


Q9. What does enumerate() do?

Returns index and value while iterating.


Q10. What does zip() do?

Combines multiple iterables for simultaneous iteration.


Q11. Can a for loop have else?

YES.


Q12. When does loop else execute?

When the loop completes normally without break.


Q13. What is an infinite loop?

A loop whose condition never becomes False.


Q14. What is an off-by-one error?

A common error where a loop runs one time too
many or one time too few.


Q15. What is the time complexity of:

for i in range(n):
    ...

Answer:
O(n)


Q16. What is the complexity of:

for i in range(n):
    for j in range(n):
        ...

Answer:
O(n²)
"""


# ============================================================
# 65. QUICK REVISION
# ============================================================

"""
WHILE:

while condition:
    ...


FOR:

for item in iterable:
    ...


RANGE:

range(stop)
range(start, stop)
range(start, stop, step)


BREAK:

break


CONTINUE:

continue


PASS:

pass


ENUMERATE:

for index, value in enumerate(numbers):
    ...


ZIP:

for a, b in zip(list1, list2):
    ...


DICTIONARY:

for key, value in dictionary.items():
    ...


NESTED LOOP:

for i in range(n):
    for j in range(n):
        ...


REVERSE:

for i in range(n - 1, -1, -1):
    ...


TWO POINTER:

left = 0
right = len(arr) - 1

while left < right:
    ...


LOOP COMPLEXITY:

One loop        -> O(n)
Nested loops    -> O(n²)
Three loops     -> O(n³)
Separate loops  -> O(n)
"""


# ============================================================
#                         END
# ============================================================