# Take input a 3x3 matrix, print only the main diagonal elements and replace everything else with an asterisk (*).

matrix = []
a = []
for i in range(3):
    for j in range(3):
        a.append(input(f"Enter element for position {i+1} , {j+1} : "))
    matrix.append(a)
    a = []

for l in range(3):
    for m in range(3):
        if l != m:
            matrix[l][m] = '*'
    print(matrix[l])


# Given a 3x3 matrix, print only the main diagonal elements and replace everything else with an asterisk (*).
# Input:
# 1 2 3
# 4 5 6
# 7 8 9
# Expected Output:
# 1 * *
# * 5 *
# * * 9

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(3):
    for j in range(3):
        if i != j:
            matrix[i][j] = '*'

for row in matrix:
    print(*row)