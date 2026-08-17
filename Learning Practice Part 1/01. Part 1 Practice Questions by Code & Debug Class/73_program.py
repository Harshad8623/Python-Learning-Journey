# Given a 4x4 matrix, print only the border elements and replace the inner elements with an asterisk (*).

matrix = [
    [1, 2, 3, 6],
    [4, 5, 6, 2],
    [7, 8, 9, 1],
    [5, 8, 6, 3]
]

for i in range(4):
    for j in range(4):
        if (i == 1):
            if (j == 1) or (j == 2):
                matrix[i][j] = "*"
        elif (i == 2):
            if (j == 1) or (j == 2):
                matrix[i][j] = "*"

for row in matrix:
    print(*row)

# solution gives the correct output for this specific 4×4 matrix.
# code is hardcoded specifically for a 4×4 matrix


# "What if I give you a 5×5 or 10×10 matrix?"

matrix = [
    [1, 2, 3, 6],
    [4, 5, 6, 2],
    [7, 8, 9, 1],
    [5, 8, 6, 3]
]

n = len(matrix)

for i in range(n):
    for j in range(n):
        if i != 0 and i != n - 1 and j != 0 and j != n - 1:
            matrix[i][j] = "*"

for row in matrix:
    print(*row)