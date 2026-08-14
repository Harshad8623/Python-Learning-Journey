# ============================================================
#          NESTED LISTS AND MATRICES IN PYTHON
#       BASICS + LOGIC BUILDING + DSA QUESTIONS
# ============================================================

"""
NESTED LIST
===========

A nested list is a list containing another list.

Example:

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

Think of it as:

        column
        0  1  2
      +---------
    0 | 1  2  3
    1 | 4  5  6
    2 | 7  8  9

The first index represents ROW.
The second index represents COLUMN.

matrix[row][column]

This concept is extremely important for DSA.
"""


# ============================================================
# 1. CREATING A NESTED LIST
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)


# ============================================================
# 2. ACCESSING COMPLETE ROW
# ============================================================

print(matrix[0])
print(matrix[1])
print(matrix[2])


# ============================================================
# 3. ACCESSING INDIVIDUAL ELEMENT
# ============================================================

print(matrix[0][0])
print(matrix[0][1])
print(matrix[0][2])

print(matrix[1][0])
print(matrix[1][1])
print(matrix[1][2])

print(matrix[2][0])
print(matrix[2][1])
print(matrix[2][2])


"""
matrix[1][2]

First [1] -> row 1
Second [2] -> column 2

        0  1  2
    0   1  2  3
    1   4  5  6
    2   7  8  9

matrix[1][2] = 6
"""


# ============================================================
# 4. MODIFYING AN ELEMENT
# ============================================================

matrix[1][1] = 50

print(matrix)


# ============================================================
# 5. MODIFYING COMPLETE ROW
# ============================================================

matrix[0] = [10, 20, 30]

print(matrix)


# ============================================================
# 6. LENGTH OF MATRIX
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(len(matrix))

"""
len(matrix)

gives number of rows.

Output:

3
"""


# ============================================================
# 7. NUMBER OF COLUMNS
# ============================================================

print(len(matrix[0]))

"""
len(matrix[0])

gives number of columns in the first row.

Output:

3
"""


# ============================================================
# 8. ROWS AND COLUMNS
# ============================================================

rows = len(matrix)
columns = len(matrix[0])

print("Rows:", rows)
print("Columns:", columns)


# ============================================================
# 9. NESTED LOOP
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:

    for value in row:
        print(value)

"""
Output:

1
2
3
4
5
6
7
8
9
"""


# ============================================================
# 10. PRINT MATRIX PROPERLY
# ============================================================

for row in matrix:
    print(*row)


"""
Output:

1 2 3
4 5 6
7 8 9
"""


# ============================================================
# 11. ACCESS USING INDEX
# ============================================================

for i in range(len(matrix)):

    for j in range(len(matrix[i])):

        print(matrix[i][j], end=" ")

    print()


"""
i -> row
j -> column

matrix[i][j]
"""


# ============================================================
# 12. PRINT ROW INDEX + COLUMN INDEX
# ============================================================

for i in range(len(matrix)):

    for j in range(len(matrix[i])):

        print(
            "row =", i,
            "column =", j,
            "value =", matrix[i][j]
        )


# ============================================================
# 13. SUM OF ALL ELEMENTS
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

print("Sum:", total)


# ============================================================
# 14. SUM USING sum()
# ============================================================

total = 0

for row in matrix:
    total += sum(row)

print("Sum:", total)


# ============================================================
# 15. FIND MAXIMUM ELEMENT
# ============================================================

maximum = matrix[0][0]

for row in matrix:

    for value in row:

        if value > maximum:
            maximum = value

print("Maximum:", maximum)


# ============================================================
# 16. FIND MINIMUM ELEMENT
# ============================================================

minimum = matrix[0][0]

for row in matrix:

    for value in row:

        if value < minimum:
            minimum = value

print("Minimum:", minimum)


# ============================================================
# 17. COUNT EVEN NUMBERS
# ============================================================

count = 0

for row in matrix:

    for value in row:

        if value % 2 == 0:
            count += 1

print("Even numbers:", count)


# ============================================================
# 18. COUNT ODD NUMBERS
# ============================================================

count = 0

for row in matrix:

    for value in row:

        if value % 2 != 0:
            count += 1

print("Odd numbers:", count)


# ============================================================
# 19. SEARCH ELEMENT IN MATRIX
# ============================================================

target = 5
found = False

for row in matrix:

    for value in row:

        if value == target:
            found = True
            break

    if found:
        break

print("Found:", found)


# ============================================================
# 20. SEARCH WITH POSITION
# ============================================================

target = 8

for i in range(len(matrix)):

    for j in range(len(matrix[i])):

        if matrix[i][j] == target:

            print("Found at:", i, j)


# ============================================================
# 21. COUNT OCCURRENCES
# ============================================================

matrix = [
    [1, 2, 3],
    [2, 5, 2],
    [7, 2, 9]
]

target = 2
count = 0

for row in matrix:

    for value in row:

        if value == target:
            count += 1

print("Occurrences:", count)


# ============================================================
# 22. SUM OF EACH ROW
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:

    print(sum(row))


"""
Output:

6
15
24
"""


# ============================================================
# 23. SUM OF EACH COLUMN
# ============================================================

rows = len(matrix)
columns = len(matrix[0])

for j in range(columns):

    total = 0

    for i in range(rows):

        total += matrix[i][j]

    print("Column", j, "sum:", total)


# ============================================================
# 24. FIND ROW WITH MAXIMUM SUM
# ============================================================

maximum_sum = float("-inf")
max_row = -1

for i in range(len(matrix)):

    row_sum = sum(matrix[i])

    if row_sum > maximum_sum:

        maximum_sum = row_sum
        max_row = i

print("Maximum row:", max_row)
print("Maximum sum:", maximum_sum)


# ============================================================
# 25. PRINT MAIN DIAGONAL
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(matrix)):

    print(matrix[i][i])


"""
Main diagonal:

1
5
9

Positions:

(0,0)
(1,1)
(2,2)
"""


# ============================================================
# 26. MAIN DIAGONAL SUM
# ============================================================

total = 0

for i in range(len(matrix)):

    total += matrix[i][i]

print("Main diagonal sum:", total)


# ============================================================
# 27. SECONDARY DIAGONAL
# ============================================================

n = len(matrix)

for i in range(n):

    print(matrix[i][n - 1 - i])


"""
Secondary diagonal:

3
5
7

Positions:

(0,2)
(1,1)
(2,0)
"""


# ============================================================
# 28. SECONDARY DIAGONAL SUM
# ============================================================

total = 0
n = len(matrix)

for i in range(n):

    total += matrix[i][n - 1 - i]

print("Secondary diagonal sum:", total)


# ============================================================
# 29. BOTH DIAGONAL SUM
# ============================================================

n = len(matrix)

main_sum = 0
secondary_sum = 0

for i in range(n):

    main_sum += matrix[i][i]
    secondary_sum += matrix[i][n - 1 - i]

print(main_sum)
print(secondary_sum)


# ============================================================
# 30. TRANSPOSE OF MATRIX
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

rows = len(matrix)
columns = len(matrix[0])

transpose = []

for j in range(columns):

    new_row = []

    for i in range(rows):

        new_row.append(matrix[i][j])

    transpose.append(new_row)

print(transpose)


"""
Original:

1 2 3
4 5 6

Transpose:

1 4
2 5
3 6
"""


# ============================================================
# 31. TRANSPOSE USING ZIP
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = list(zip(*matrix))

print(transpose)


"""
zip(*matrix) is a very important Python trick.

It produces tuples.

If you want lists:

transpose = [list(row) for row in zip(*matrix)]
"""


# ============================================================
# 32. REVERSE EACH ROW
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:

    row.reverse()

print(matrix)


# ============================================================
# 33. REVERSE MATRIX ROW ORDER
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix.reverse()

print(matrix)


# ============================================================
# 34. MATRIX ROTATION 90 DEGREE CLOCKWISE
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated = [list(row) for row in zip(*matrix[::-1])]

print(rotated)


"""
Original:

1 2 3
4 5 6
7 8 9

After 90 degree clockwise:

7 4 1
8 5 2
9 6 3
"""


# ============================================================
# 35. ROTATE 90 DEGREE CLOCKWISE WITHOUT EXTRA MATRIX
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matrix)

# Step 1: Transpose
for i in range(n):

    for j in range(i + 1, n):

        matrix[i][j], matrix[j][i] = \
            matrix[j][i], matrix[i][j]

# Step 2: Reverse every row
for row in matrix:

    row.reverse()

print(matrix)


"""
This is a very important interview problem.

Pattern:

    Transpose
        +
    Reverse each row

= 90 degree clockwise rotation.
"""


# ============================================================
# 36. ROTATE 90 DEGREE ANTI-CLOCKWISE
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matrix)

# Transpose
for i in range(n):

    for j in range(i + 1, n):

        matrix[i][j], matrix[j][i] = \
            matrix[j][i], matrix[i][j]

# Reverse order of rows
matrix.reverse()

print(matrix)


# ============================================================
# 37. FLATTEN NESTED LIST
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flat = []

for row in matrix:

    for value in row:
        flat.append(value)

print(flat)


"""
Output:

[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""


# ============================================================
# 38. FLATTEN USING LIST COMPREHENSION
# ============================================================

flat = [
    value
    for row in matrix
    for value in row
]

print(flat)


# ============================================================
# 39. CREATE MATRIX USING LOOP
# ============================================================

rows = 3
columns = 4

matrix = []

for i in range(rows):

    row = []

    for j in range(columns):

        row.append(0)

    matrix.append(row)

print(matrix)


# ============================================================
# 40. MATRIX USING LIST COMPREHENSION
# ============================================================

rows = 3
columns = 4

matrix = [
    [0 for j in range(columns)]
    for i in range(rows)
]

print(matrix)


# ============================================================
# 41. IMPORTANT: DON'T DO THIS
# ============================================================

"""
WRONG:

matrix = [[0] * 3] * 3

This creates references to the SAME inner list.

If you change:

matrix[0][0] = 99

other rows may also change.
"""


# ============================================================
# 42. CORRECT WAY
# ============================================================

matrix = [[0] * 3 for _ in range(3)]

matrix[0][0] = 99

print(matrix)


"""
Each row is a separate list.
"""


# ============================================================
# 43. IDENTITY CHECK
# ============================================================

wrong = [[0] * 3] * 3

print(wrong[0] is wrong[1])

correct = [[0] * 3 for _ in range(3)]

print(correct[0] is correct[1])


"""
Wrong:

True

Correct:

False
"""


# ============================================================
# 44. MATRIX ADDITION
# ============================================================

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

result = []

for i in range(len(A)):

    row = []

    for j in range(len(A[0])):

        row.append(A[i][j] + B[i][j])

    result.append(row)

print(result)


"""
A + B:

1 2       5 6
3 4   +   7 8

=

6  8
10 12
"""


# ============================================================
# 45. MATRIX SUBTRACTION
# ============================================================

result = []

for i in range(len(A)):

    row = []

    for j in range(len(A[0])):

        row.append(A[i][j] - B[i][j])

    result.append(row)

print(result)


# ============================================================
# 46. MATRIX MULTIPLICATION
# ============================================================

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

result = [
    [0, 0],
    [0, 0]
]

for i in range(len(A)):

    for j in range(len(B[0])):

        for k in range(len(B)):

            result[i][j] += A[i][k] * B[k][j]

print(result)


"""
IMPORTANT MATRIX MULTIPLICATION PATTERN:

for i -> rows of A
for j -> columns of B
for k -> common dimension

result[i][j] += A[i][k] * B[k][j]

This is important for understanding matrix
multiplication and also appears in DSA.
"""


# ============================================================
# 47. SEARCH IN SORTED MATRIX
# ============================================================

matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17]
]

target = 9

rows = len(matrix)
columns = len(matrix[0])

row = 0
column = columns - 1

found = False

while row < rows and column >= 0:

    if matrix[row][column] == target:

        found = True
        break

    elif matrix[row][column] > target:

        column -= 1

    else:

        row += 1

print("Found:", found)


"""
This is called the staircase search technique.

Start from TOP-RIGHT.

If current > target:
    move LEFT

If current < target:
    move DOWN
"""


# ============================================================
# 48. SPIRAL TRAVERSAL
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

top = 0
bottom = len(matrix) - 1
left = 0
right = len(matrix[0]) - 1

result = []

while top <= bottom and left <= right:

    # Left -> Right
    for j in range(left, right + 1):
        result.append(matrix[top][j])

    top += 1

    # Top -> Bottom
    for i in range(top, bottom + 1):
        result.append(matrix[i][right])

    right -= 1

    # Right -> Left
    if top <= bottom:

        for j in range(right, left - 1, -1):
            result.append(matrix[bottom][j])

        bottom -= 1

    # Bottom -> Top
    if left <= right:

        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])

        left += 1

print(result)


"""
Output:

[1, 2, 3, 6, 9, 8, 7, 4, 5]

Spiral traversal is a VERY important
matrix interview problem.
"""


# ============================================================
# 49. BOUNDARY TRAVERSAL
# ============================================================

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

rows = len(matrix)
columns = len(matrix[0])

result = []

# Top row
for j in range(columns):
    result.append(matrix[0][j])

# Right column
for i in range(1, rows):
    result.append(matrix[i][columns - 1])

# Bottom row
for j in range(columns - 2, -1, -1):
    result.append(matrix[rows - 1][j])

# Left column
for i in range(rows - 2, 0, -1):
    result.append(matrix[i][0])

print(result)


# ============================================================
# 50. DIAGONAL TRAVERSAL
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(matrix)):

    for j in range(len(matrix[0])):

        if i == j:

            print(matrix[i][j])


# ============================================================
# 51. CHECK SYMMETRIC MATRIX
# ============================================================

matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

symmetric = True

for i in range(len(matrix)):

    for j in range(len(matrix)):

        if matrix[i][j] != matrix[j][i]:

            symmetric = False
            break

    if not symmetric:
        break

print("Symmetric:", symmetric)


"""
A matrix is symmetric when:

matrix[i][j] == matrix[j][i]
"""


# ============================================================
# 52. CHECK IDENTITY MATRIX
# ============================================================

matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

identity = True

for i in range(len(matrix)):

    for j in range(len(matrix)):

        if i == j:

            if matrix[i][j] != 1:
                identity = False

        else:

            if matrix[i][j] != 0:
                identity = False

print("Identity matrix:", identity)


# ============================================================
# 53. TRANSPOSE WITHOUT ZIP
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

rows = len(matrix)
columns = len(matrix[0])

transpose = []

for j in range(columns):

    row = []

    for i in range(rows):

        row.append(matrix[i][j])

    transpose.append(row)

print(transpose)


"""
This version is more important for DSA
because you understand the actual logic.
"""


# ============================================================
# 54. MATRIX INPUT FROM USER
# ============================================================

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):

    row = []

    for j in range(columns):

        value = int(input(
            f"Enter element [{i}][{j}]: "
        ))

        row.append(value)

    matrix.append(row)

print(matrix)


# ============================================================
# 55. MATRIX INPUT - ROW BY ROW
# ============================================================

rows = int(input("Rows: "))
columns = int(input("Columns: "))

matrix = []

for i in range(rows):

    row = list(
        map(
            int,
            input("Enter row: ").split()
        )
    )

    matrix.append(row)

print(matrix)


"""
Example input:

3 3

1 2 3
4 5 6
7 8 9
"""


# ============================================================
# 56. MATRIX PRINTING
# ============================================================

for row in matrix:

    print(*row)


# ============================================================
# 57. TRANSPOSE USING LIST COMPREHENSION
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = [
    [matrix[i][j] for i in range(len(matrix))]
    for j in range(len(matrix[0]))
]

print(transpose)


# ============================================================
# 58. FLATTEN USING SUM
# ============================================================

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

flat = sum(matrix, [])

print(flat)


"""
This works, but for large lists it is not the preferred
performance approach.

Prefer:

    [x for row in matrix for x in row]
"""


# ============================================================
# 59. FIND SECOND LARGEST ELEMENT
# ============================================================

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

values = []

for row in matrix:

    for value in row:

        values.append(value)

values = list(set(values))

values.sort()

print("Second largest:", values[-2])


# ============================================================
# 60. FIND SECOND LARGEST WITHOUT SORTING
# ============================================================

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

largest = float("-inf")
second = float("-inf")

for row in matrix:

    for value in row:

        if value > largest:

            second = largest
            largest = value

        elif value > second and value != largest:

            second = value

print("Largest:", largest)
print("Second largest:", second)


# ============================================================
# 61. SUM OF MAIN + SECONDARY DIAGONAL
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matrix)

total = 0

for i in range(n):

    total += matrix[i][i]

    if i != n - 1 - i:
        total += matrix[i][n - 1 - i]

print(total)


"""
The condition:

if i != n - 1 - i

prevents counting the center twice
when n is odd.
"""


# ============================================================
# 62. ZERO MATRIX ROW AND COLUMN
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

rows = len(matrix)
columns = len(matrix[0])

zero_rows = set()
zero_columns = set()

for i in range(rows):

    for j in range(columns):

        if matrix[i][j] == 0:

            zero_rows.add(i)
            zero_columns.add(j)

for i in range(rows):

    for j in range(columns):

        if i in zero_rows or j in zero_columns:

            matrix[i][j] = 0

print(matrix)


"""
Important DSA problem:

If an element is zero,
make its complete row and column zero.
"""


# ============================================================
# 63. MAXIMUM ELEMENT IN EACH ROW
# ============================================================

matrix = [
    [1, 9, 3],
    [7, 2, 8],
    [4, 6, 5]
]

for row in matrix:

    print(max(row))


# ============================================================
# 64. MINIMUM ELEMENT IN EACH ROW
# ============================================================

for row in matrix:

    print(min(row))


# ============================================================
# 65. MATRIX SIZE
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

rows = len(matrix)
columns = len(matrix[0])

print("Rows:", rows)
print("Columns:", columns)


"""
Important:

Number of elements:

    rows * columns

Here:

    2 * 3 = 6
"""


# ============================================================
# 66. RECTANGULAR MATRIX
# ============================================================

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

print("Rows:", len(matrix))
print("Columns:", len(matrix[0]))


"""
2 x 4 matrix.

Not every matrix is square.
"""


# ============================================================
# 67. SQUARE MATRIX
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

if len(matrix) == len(matrix[0]):

    print("Square matrix")


# ============================================================
# 68. FIND ROW WITH MAXIMUM NUMBER OF 1s
# ============================================================

matrix = [
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1]
]

max_count = 0
answer_row = -1

for i in range(len(matrix)):

    count = matrix[i].count(1)

    if count > max_count:

        max_count = count
        answer_row = i

print("Row:", answer_row)
print("Number of 1s:", max_count)


# ============================================================
# 69. MATRIX DSA COMPLEXITY
# ============================================================

"""
For an m x n matrix:

Traversing all elements:

    O(m * n)


Searching every element:

    O(m * n)


Finding sum:

    O(m * n)


Transpose:

    O(m * n)


Matrix addition:

    O(m * n)


Matrix multiplication:

    O(n^3)

for two n x n matrices using the basic algorithm.


Space:

A matrix itself:

    O(m * n)


Extra space depends on the problem.
"""


# ============================================================
# 70. IMPORTANT MATRIX PATTERNS
# ============================================================

"""
You should recognize these patterns:

1. ROW TRAVERSAL

    for i in range(rows):
        for j in range(columns):
            matrix[i][j]


2. COLUMN TRAVERSAL

    for j in range(columns):
        for i in range(rows):
            matrix[i][j]


3. MAIN DIAGONAL

    matrix[i][i]


4. SECONDARY DIAGONAL

    matrix[i][n - 1 - i]


5. TRANSPOSE

    matrix[i][j] <-> matrix[j][i]


6. TWO POINTER / BOUNDARY

    top
    bottom
    left
    right


7. SPIRAL

    top -> right -> bottom -> left


8. SEARCH SORTED MATRIX

    Start top-right.


9. FREQUENCY

    Dictionary / Counter / Array


10. IN-PLACE MODIFICATION

    Modify original matrix without creating
    another matrix when possible.
"""


# ============================================================
# 71. INTERVIEW QUESTIONS
# ============================================================

"""
BEGINNER
========

1. What is a nested list?

2. How do you access an element from a nested list?

3. What does matrix[i][j] mean?

4. How do you find number of rows?

5. How do you find number of columns?

6. How do you traverse a matrix?

7. How do you find sum of all elements?

8. How do you find maximum element?

9. How do you search for an element?

10. How do you count even numbers?


INTERMEDIATE
============

11. Find sum of every row.

12. Find sum of every column.

13. Find row with maximum sum.

14. Find main diagonal sum.

15. Find secondary diagonal sum.

16. Find transpose.

17. Rotate matrix by 90 degrees.

18. Check if matrix is symmetric.

19. Check whether matrix is identity matrix.

20. Search an element in a sorted matrix.

21. Spiral traversal.

22. Boundary traversal.

23. Set matrix rows and columns to zero.

24. Find second largest element.

25. Matrix addition.

26. Matrix multiplication.


ADVANCED
========

27. Rotate matrix in-place.

28. Search in a row-wise and column-wise sorted matrix.

29. Spiral Matrix.

30. Set Matrix Zeroes.

31. Number of Islands.

32. Flood Fill.

33. Word Search.

34. Game of Life.

35. Diagonal traversal.

36. Maximum sum submatrix.

37. Prefix sum matrix.

38. 2D sliding window.
"""


# ============================================================
# 72. IMPORTANT CODING QUESTIONS TO PRACTICE
# ============================================================

"""
Solve these WITHOUT LOOKING AT THE SOLUTION:

LEVEL 1
-------

Q1. Print every element of a matrix.

Q2. Print matrix row by row.

Q3. Print matrix column by column.

Q4. Find sum of all elements.

Q5. Find maximum element.

Q6. Find minimum element.

Q7. Count even and odd elements.

Q8. Search an element and return its position.

Q9. Find sum of every row.

Q10. Find sum of every column.


LEVEL 2
-------

Q11. Find maximum row sum.

Q12. Find minimum row sum.

Q13. Find main diagonal sum.

Q14. Find secondary diagonal sum.

Q15. Transpose a matrix.

Q16. Check whether matrix is symmetric.

Q17. Check identity matrix.

Q18. Reverse every row.

Q19. Rotate matrix 90° clockwise.

Q20. Rotate matrix 90° anti-clockwise.


LEVEL 3
-------

Q21. Spiral traversal.

Q22. Boundary traversal.

Q23. Search in sorted matrix.

Q24. Set Matrix Zeroes.

Q25. Matrix multiplication.

Q26. Find second largest element.

Q27. Find row containing maximum number of 1s.

Q28. Flatten a matrix.

Q29. Find duplicate values.

Q30. Find frequency of each value.


LEVEL 4 - DSA
-------------

Q31. Number of Islands.

Q32. Flood Fill.

Q33. Word Search.

Q34. Game of Life.

Q35. Maximum area of island.

Q36. Rotten Oranges.

Q37. Surrounded Regions.

Q38. Shortest path in a binary matrix.
"""


# ============================================================
# 73. MOST IMPORTANT MATRIX TEMPLATE
# ============================================================

"""
MEMORIZE THIS:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
columns = len(matrix[0])

for i in range(rows):

    for j in range(columns):

        print(matrix[i][j])


Remember:

    i -> ROW
    j -> COLUMN

    matrix[i][j]
"""


# ============================================================
# 74. FINAL DSA CHEAT SHEET
# ============================================================

"""
NESTED LIST:

    matrix = [
        [1, 2],
        [3, 4]
    ]


ACCESS:

    matrix[i][j]


ROWS:

    len(matrix)


COLUMNS:

    len(matrix[0])


TRAVERSAL:

    for i in range(rows):
        for j in range(columns):
            matrix[i][j]


PRINT:

    for row in matrix:
        print(*row)


MAIN DIAGONAL:

    matrix[i][i]


SECONDARY DIAGONAL:

    matrix[i][n - 1 - i]


TRANSPOSE:

    zip(*matrix)


ROTATE CLOCKWISE:

    transpose + reverse rows


SPIRAL:

    top
    bottom
    left
    right


SEARCH SORTED MATRIX:

    start top-right


MATRIX SIZE:

    rows * columns


COMMON COMPLEXITY:

    Full traversal -> O(rows * columns)


MOST IMPORTANT WARNING:

    [[0] * n] * n

is dangerous because all rows refer to
the same inner list.

Use:

    [[0] * n for _ in range(n)]
"""


print()
print("=" * 60)
print("       NESTED LIST + MATRIX LEARNING COMPLETE")
print("=" * 60)