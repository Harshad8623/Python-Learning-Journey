# Given a 3x3 matrix, print only the anti-diagonal (top-right to bottom-left) elements and replace everything else with an asterisk (*).

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(3):
    for j in range(3):
        if i+j != 2:
            matrix[i][j] = "*"

for rows in matrix:
    print(*rows)