"""
PART 3 — Pattern Printing (26-35)

KEY IDEA:
Outer loop -> rows.
Inner loop -> columns/items/spaces.
"""


def right_triangle(n):
    for i in range(1, n + 1):
        print("* " * i)


def pyramid(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "* " * i
        print(spaces + stars)


def diamond(n):
    # n = number of rows in upper half
    for i in range(1, n + 1):
        print(" " * (n-i) + "* " * i)
    for i in range(n-1, 0, -1):
        print(" " * (n-i) + "* " * i)


def number_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def inverted_triangle(n):
    for i in range(n, 0, -1):
        print("* " * i)


def inverted_pyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n-i) + "* " * i)


def floyd_triangle(n):
    value = 1
    for i in range(1, n + 1):
        for _ in range(i):
            print(value, end=" ")
            value += 1
        print()


def alphabet_triangle(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(65 + j), end=" ")
        print()


def hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def butterfly(n):
    # Upper half
    for i in range(1, n + 1):
        left = "* " * i
        middle = "  " * (2 * (n-i))
        right = "* " * i
        print(left + middle + right)
    # Lower half
    for i in range(n, 0, -1):
        left = "* " * i
        middle = "  " * (2 * (n-i))
        right = "* " * i
        print(left + middle + right)


# INTERVIEW PATTERN METHOD:
# For each pattern, write row formulas before coding.
#
# Example pyramid:
# row i -> spaces = n-i, stars = i
#
# This same reasoning becomes useful later for nested loops,
# matrices, backtracking and 2-D array problems.


if __name__ == "__main__":
    n = 5
    print("Right Triangle"); right_triangle(n)
    print("\nPyramid"); pyramid(n)
    print("\nDiamond"); diamond(n)
    print("\nNumber Triangle"); number_triangle(n)
    print("\nInverted Triangle"); inverted_triangle(n)
    print("\nInverted Pyramid"); inverted_pyramid(n)
    print("\nFloyd"); floyd_triangle(n)
    print("\nAlphabet"); alphabet_triangle(n)
    print("\nHollow Square"); hollow_square(n)
    print("\nButterfly"); butterfly(n)
