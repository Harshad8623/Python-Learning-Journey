# Given a 3x3 matrix as input, print its lower triangle. Replace all elements in the upper triangle (above the main diagonal) with an asterisk (*).

matrix = []

for i in range(3):
    row = []

    for j in range(3):
        row.append(int(input(f"Enter {i+1},{j+1} Number : ")))

    matrix.append(row)

print(matrix)

for i in range(3):
    for j in range(3):
        if j > i:
            matrix[i][j] = "*"

for row in matrix:
    print(row)