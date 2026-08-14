# ============================================================
#              PYTHON PATTERN PROGRAMS
# ============================================================

"""
IMPORTANT PATTERN CONCEPT

Most patterns use:

for i in range(rows):
    for j in range(columns):
        print(...)

Think:

i -> ROW
j -> COLUMN


Before coding any pattern, ask:

1. How many rows?
2. How many columns?
3. What should I print?
4. Does the output depend on i?
5. Does the output depend on j?
6. Does the output depend on i + j?
7. Does the output depend on i - j?
8. Do I need spaces?
9. Do I need increasing/decreasing loops?
"""


# ============================================================
# 1. SAME NUMBERS IN EVERY ROW
# ============================================================

"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

for i in range(1, 6):

    for j in range(1, 6):
        print(j, end=" ")

    print()

print()


# LOGIC:
# Output depends on j.


# ============================================================
# 2. SAME NUMBER IN EVERY COLUMN
# ============================================================

"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
"""

for i in range(1, 6):

    for j in range(1, 6):
        print(i, end=" ")

    print()

print()


# LOGIC:
# Output depends on i.


# ============================================================
# 3. DECREASING ROW NUMBERS
# ============================================================

"""
5 5 5 5 5
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1
"""

for i in range(5, 0, -1):

    for j in range(1, 6):
        print(i, end=" ")

    print()

print()


# ============================================================
# 4. INCREASING STAR SQUARE
# ============================================================

"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""

for i in range(5):

    for j in range(5):
        print("*", end=" ")

    print()

print()


# ============================================================
# 5. INCREASING RIGHT TRIANGLE
# ============================================================

"""
*
* *
* * *
* * * *
* * * * *
"""

for i in range(1, 6):

    for j in range(i):
        print("*", end=" ")

    print()

print()


# LOGIC:
# Number of columns = i


# ============================================================
# 6. NUMBER RIGHT TRIANGLE
# ============================================================

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

for i in range(1, 6):

    for j in range(1, i + 1):
        print(j, end=" ")

    print()

print()


# ============================================================
# 7. SAME NUMBER TRIANGLE
# ============================================================

"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""

for i in range(1, 6):

    for j in range(i):
        print(i, end=" ")

    print()

print()


# ============================================================
# 8. INVERTED STAR TRIANGLE
# ============================================================

"""
* * * * *
* * * *
* * *
* *
*
"""

for i in range(5, 0, -1):

    for j in range(i):
        print("*", end=" ")

    print()

print()


# ============================================================
# 9. INVERTED NUMBER TRIANGLE
# ============================================================

"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

for i in range(5, 0, -1):

    for j in range(1, i + 1):
        print(j, end=" ")

    print()

print()


# ============================================================
# 10. INVERTED SAME NUMBER TRIANGLE
# ============================================================

"""
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
"""

for i in range(5, 0, -1):

    for j in range(i):
        print(i, end=" ")

    print()

print()


# ============================================================
# 11. CONTINUOUS NUMBER TRIANGLE
# ============================================================

"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""

num = 1

for i in range(1, 6):

    for j in range(i):

        print(num, end=" ")
        num += 1

    print()

print()


# ============================================================
# 12. REVERSE CONTINUOUS NUMBERS
# ============================================================

"""
1 2 3 4 5
6 7 8 9
10 11 12
13 14
15
"""

num = 1

for i in range(5, 0, -1):

    for j in range(i):

        print(num, end=" ")
        num += 1

    print()

print()


# ============================================================
# 13. ALPHABET PATTERN
# ============================================================

"""
A
A B
A B C
A B C D
A B C D E
"""

for i in range(1, 6):

    for j in range(i):

        print(chr(65 + j), end=" ")

    print()

print()


# ============================================================
# 14. SAME ALPHABET ROW
# ============================================================

"""
A
B B
C C C
D D D D
E E E E E
"""

for i in range(5):

    for j in range(i + 1):

        print(chr(65 + i), end=" ")

    print()

print()


# ============================================================
# 15. REVERSE ALPHABET PATTERN
# ============================================================

"""
E E E E E
D D D D
C C C
B B
A
"""

for i in range(4, -1, -1):

    for j in range(i + 1):

        print(chr(65 + i), end=" ")

    print()

print()


# ============================================================
# 16. RIGHT-ALIGNED STAR TRIANGLE
# ============================================================

"""
        *
      * *
    * * *
  * * * *
* * * * *
"""

for i in range(1, 6):

    # Spaces
    for j in range(5 - i):
        print(" ", end="  ")

    # Stars
    for j in range(i):
        print("*", end=" ")

    print()

print()


# ============================================================
# 17. RIGHT-ALIGNED NUMBER TRIANGLE
# ============================================================

"""
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
"""

for i in range(1, 6):

    for j in range(5 - i):
        print(" ", end="  ")

    for j in range(1, i + 1):
        print(j, end=" ")

    print()

print()


# ============================================================
# 18. PYRAMID
# ============================================================

"""
        *
       ***
      *****
     *******
    *********
"""

for i in range(1, 6):

    # Spaces
    for j in range(5 - i):
        print(" ", end="")

    # Stars
    for j in range(2 * i - 1):
        print("*", end="")

    print()

print()


# IMPORTANT FORMULA:
#
# Spaces = n - i
# Stars  = 2*i - 1


# ============================================================
# 19. NUMBER PYRAMID
# ============================================================

"""
    1
   123
  12345
 1234567
123456789
"""

for i in range(1, 6):

    for j in range(5 - i):
        print(" ", end="")

    for j in range(1, 2 * i):
        print(j, end="")

    print()

print()


# ============================================================
# 20. INVERTED PYRAMID
# ============================================================

"""
*********
 *******
  *****
   ***
    *
"""

for i in range(5, 0, -1):

    for j in range(5 - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()

print()


# ============================================================
# 21. DIAMOND
# ============================================================

"""
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""

# Upper half

for i in range(1, 6):

    for j in range(5 - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()


# Lower half

for i in range(4, 0, -1):

    for j in range(5 - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()

print()


# ============================================================
# 22. HOLLOW SQUARE
# ============================================================

"""
* * * * *
*       *
*       *
*       *
* * * * *
"""

n = 5

for i in range(n):

    for j in range(n):

        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()

print()


# ============================================================
# 23. HOLLOW TRIANGLE
# ============================================================

"""
*
* *
*   *
*     *
* * * * *
"""

n = 5

for i in range(1, n + 1):

    for j in range(1, i + 1):

        if j == 1 or j == i or i == n:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()

print()


# ============================================================
# 24. MAIN DIAGONAL
# ============================================================

"""
* . . . .
. * . . .
. . * . .
. . . * .
. . . . *
"""

n = 5

for i in range(n):

    for j in range(n):

        if i == j:
            print("*", end=" ")

        else:
            print(".", end=" ")

    print()

print()


# LOGIC:
# Main diagonal -> i == j


# ============================================================
# 25. ANTI-DIAGONAL
# ============================================================

"""
. . . . *
. . . * .
. . * . .
. * . . .
* . . . .
"""

n = 5

for i in range(n):

    for j in range(n):

        if i + j == n - 1:
            print("*", end=" ")

        else:
            print(".", end=" ")

    print()

print()


# LOGIC:
# Anti-diagonal -> i + j == n - 1


# ============================================================
# 26. X PATTERN
# ============================================================

"""
* . . . *
. * . * .
. . * . .
. * . * .
* . . . *
"""

n = 5

for i in range(n):

    for j in range(n):

        if i == j or i + j == n - 1:
            print("*", end=" ")

        else:
            print(".", end=" ")

    print()

print()


# ============================================================
# 27. PLUS (+) PATTERN
# ============================================================

"""
. . * . .
. . * . .
* * * * *
. . * . .
. . * . .
"""

n = 5

for i in range(n):

    for j in range(n):

        if i == n // 2 or j == n // 2:
            print("*", end=" ")

        else:
            print(".", end=" ")

    print()

print()


# ============================================================
# 28. BINARY PATTERN
# ============================================================

"""
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
"""

for i in range(1, 6):

    for j in range(i):

        print((i + j) % 2, end=" ")

    print()

print()


# ============================================================
# 29. ALTERNATING 1 AND 0
# ============================================================

"""
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
"""

n = 5

for i in range(n):

    for j in range(n):

        print((i + j) % 2, end=" ")

    print()

print()


# ============================================================
# 30. NUMBER INCREASING BY ROW
# ============================================================

"""
1
2 3
3 4 5
4 5 6 7
5 6 7 8 9
"""

for i in range(1, 6):

    for j in range(i):

        print(i + j, end=" ")

    print()

print()


# ============================================================
# 31. DECREASING NUMBER PATTERN
# ============================================================

"""
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""

for i in range(5, 0, -1):

    for j in range(i, 0, -1):

        print(j, end=" ")

    print()

print()


# ============================================================
# 32. STARTING FROM ROW NUMBER
# ============================================================

"""
1 2 3 4 5
2 3 4 5
3 4 5
4 5
5
"""

for i in range(1, 6):

    for j in range(i, 6):

        print(j, end=" ")

    print()

print()


# ============================================================
# 33. REVERSE STARTING NUMBER
# ============================================================

"""
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""

for i in range(5, 0, -1):

    for j in range(i, 0, -1):

        print(j, end=" ")

    print()

print()


# ============================================================
# 34. FLOYD'S TRIANGLE
# ============================================================

"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""

num = 1

for i in range(1, 6):

    for j in range(i):

        print(num, end=" ")

        num += 1

    print()

print()


# ============================================================
# 35. 0-1 TRIANGLE
# ============================================================

"""
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
"""

for i in range(1, 6):

    for j in range(i):

        if (i + j) % 2 == 0:
            print(1, end=" ")

        else:
            print(0, end=" ")

    print()

print()


# ============================================================
# 36. SQUARE WITH ROW + COLUMN SUM
# ============================================================

"""
0 1 2 3 4
1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8
"""

n = 5

for i in range(n):

    for j in range(n):

        print(i + j, end=" ")

    print()

print()


# ============================================================
# 37. MULTIPLICATION TABLE PATTERN
# ============================================================

"""
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20 25
"""

n = 5

for i in range(1, n + 1):

    for j in range(1, n + 1):

        print(i * j, end=" ")

    print()

print()


# ============================================================
# 38. BORDER + DIAGONAL PATTERN
# ============================================================

"""
* * * * *
* * . * *
* . * . *
* * . * *
* * * * *
"""

n = 5

for i in range(n):

    for j in range(n):

        if (
            i == 0
            or i == n - 1
            or j == 0
            or j == n - 1
            or i == j
            or i + j == n - 1
        ):
            print("*", end=" ")

        else:
            print(".", end=" ")

    print()

print()


# ============================================================
# 39. CONCENTRIC SQUARE / NUMBER MATRIX
# ============================================================

"""
For n = 3:

3 3 3 3 3
3 2 2 2 3
3 2 1 2 3
3 2 2 2 3
3 3 3 3 3
"""

n = 3

size = 2 * n - 1

for i in range(size):

    for j in range(size):

        top = i
        left = j
        right = size - 1 - j
        bottom = size - 1 - i

        value = n - min(top, left, right, bottom)

        print(value, end=" ")

    print()

print()


# ============================================================
# 40. CHARACTER GRID
# ============================================================

"""
A B C D E
A B C D E
A B C D E
A B C D E
A B C D E
"""

n = 5

for i in range(n):

    for j in range(n):

        print(chr(65 + j), end=" ")

    print()

print()


# ============================================================
# 41. REVERSE CHARACTER GRID
# ============================================================

"""
E D C B A
E D C B A
E D C B A
E D C B A
E D C B A
"""

n = 5

for i in range(n):

    for j in range(n - 1, -1, -1):

        print(chr(65 + j), end=" ")

    print()

print()


# ============================================================
# 42. BUTTERFLY PATTERN
# ============================================================

"""
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
"""

n = 5

# Upper half

for i in range(1, n + 1):

    # Left stars
    for j in range(i):
        print("*", end="")

    # Spaces
    for j in range(2 * (n - i)):
        print(" ", end="")

    # Right stars
    for j in range(i):
        print("*", end="")

    print()


# Lower half

for i in range(n - 1, 0, -1):

    # Left stars
    for j in range(i):
        print("*", end="")

    # Spaces
    for j in range(2 * (n - i)):
        print(" ", end="")

    # Right stars
    for j in range(i):
        print("*", end="")

    print()

print()


# ============================================================
# 43. HOLLOW PYRAMID
# ============================================================

"""
    *
   * *
  *   *
 *     *
*********
"""

n = 5

for i in range(1, n + 1):

    # Spaces
    for j in range(n - i):
        print(" ", end="")

    # Pyramid positions
    for j in range(2 * i - 1):

        if j == 0 or j == 2 * i - 2 or i == n:
            print("*", end="")

        else:
            print(" ", end="")

    print()

print()


# ============================================================
# 44. HOLLOW INVERTED PYRAMID
# ============================================================

"""
*********
 *     *
  *   *
   * *
    *
"""

n = 5

for i in range(n, 0, -1):

    # Spaces
    for j in range(n - i):
        print(" ", end="")

    # Stars
    for j in range(2 * i - 1):

        if j == 0 or j == 2 * i - 2 or i == n:
            print("*", end="")

        else:
            print(" ", end="")

    print()

print()


# ============================================================
# 45. NUMBER PALINDROME PYRAMID
# ============================================================

"""
    1
   121
  12321
 1234321
123454321
"""

n = 5

for i in range(1, n + 1):

    # Spaces
    for j in range(n - i):
        print(" ", end="")

    # Increasing
    for j in range(1, i + 1):
        print(j, end="")

    # Decreasing
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()

print()


# ============================================================
# 46. PALINDROME NUMBER TRIANGLE
# ============================================================

"""
1
121
12321
1234321
123454321
"""

for i in range(1, 6):

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()

print()


# ============================================================
# 47. PATTERN USING i + j
# ============================================================

"""
0 1 2 3 4
1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8
"""

n = 5

for i in range(n):

    for j in range(n):

        print(i + j, end=" ")

    print()

print()


# ============================================================
# 48. PATTERN USING i - j
# ============================================================

"""
0 -1 -2 -3 -4
1 0 -1 -2 -3
2 1 0 -1 -2
3 2 1 0 -1
4 3 2 1 0
"""

n = 5

for i in range(n):

    for j in range(n):

        print(i - j, end=" ")

    print()

print()


# ============================================================
# 49. PATTERN USING max(i, j)
# ============================================================

"""
0 1 2 3 4
1 1 2 3 4
2 2 2 3 4
3 3 3 3 4
4 4 4 4 4
"""

n = 5

for i in range(n):

    for j in range(n):

        print(max(i, j), end=" ")

    print()

print()


# ============================================================
# 50. PATTERN USING min(i, j)
# ============================================================

"""
0 0 0 0 0
0 1 1 1 1
0 1 2 2 2
0 1 2 3 3
0 1 2 3 4
"""

n = 5

for i in range(n):

    for j in range(n):

        print(min(i, j), end=" ")

    print()

print()


# ============================================================
#              PATTERN THINKING FOR DSA
# ============================================================

"""
The most important part is NOT memorizing 50 patterns.

Learn these relationships:

--------------------------------------------------------------
1. i
--------------------------------------------------------------

Output depends on row.

Example:

1 1 1
2 2 2
3 3 3


--------------------------------------------------------------
2. j
--------------------------------------------------------------

Output depends on column.

Example:

1 2 3
1 2 3
1 2 3


--------------------------------------------------------------
3. i + j
--------------------------------------------------------------

Useful for:

- Alternating patterns
- Diagonals
- Matrix problems


--------------------------------------------------------------
4. i - j
--------------------------------------------------------------

Useful for:

- Diagonal relationships
- Matrix transformations


--------------------------------------------------------------
5. i == j
--------------------------------------------------------------

Main diagonal.


--------------------------------------------------------------
6. i + j == n - 1
--------------------------------------------------------------

Anti-diagonal.


--------------------------------------------------------------
7. i == j OR i + j == n - 1
--------------------------------------------------------------

X pattern.


--------------------------------------------------------------
8. i == n // 2 OR j == n // 2
--------------------------------------------------------------

Plus pattern.


--------------------------------------------------------------
9. 2 * i - 1
--------------------------------------------------------------

Number of elements in pyramid row.


--------------------------------------------------------------
10. n - i
--------------------------------------------------------------

Common space calculation.


--------------------------------------------------------------
11. min(i, j)
--------------------------------------------------------------

Useful for matrix / concentric patterns.


--------------------------------------------------------------
12. max(i, j)
--------------------------------------------------------------

Useful for matrix / boundary patterns.
"""


# ============================================================
#                  PATTERN SOLVING METHOD
# ============================================================

"""
When you receive a pattern question in a coding round:

STEP 1:
Count the rows.

STEP 2:
Look at each row separately.

STEP 3:
Count how many elements/spaces are in each row.

STEP 4:
Find the relationship between row and column.

STEP 5:
Decide what to print.

STEP 6:
Write nested loops.

STEP 7:
Add conditions if the pattern is hollow/diagonal/etc.


Example:

*
**
***
****

Observe:

Row 1 -> 1 star
Row 2 -> 2 stars
Row 3 -> 3 stars
Row 4 -> 4 stars

Therefore:

for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()
"""


# ============================================================
#                MOST IMPORTANT PATTERN RULE
# ============================================================

"""
Don't memorize:

for i in range(...)
for j in range(...)

Instead ask:

WHAT CHANGES?

Example:

1 2 3 4
1 2 3 4
1 2 3 4

Column changes -> print j


Example:

1 1 1 1
2 2 2 2
3 3 3 3

Row changes -> print i


Example:

*
**
***
****

Number of columns depends on row -> j < i


Example:

****
***
**
*

Number of columns decreases -> reverse range


Example:

    *
   ***
  *****

Need:

spaces + stars


Example:

* . . .
. * . .
. . * .

Need:

i == j
"""


# ============================================================
#                         END
# ============================================================

print("\n======================================")
print("       PATTERN PRACTICE COMPLETED")
print("======================================")