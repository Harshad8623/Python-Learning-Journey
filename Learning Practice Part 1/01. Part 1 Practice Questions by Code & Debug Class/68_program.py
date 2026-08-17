# Create a 3x3 matrix (a nested list) and then use nested loops to calculate and print the sum of all its elements

matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

total = 0
for i in range(len(matrix)):
    for j in matrix[i]:
        total += j
print(total)



# AI Suggestion :

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
total = 0
for row in matrix:
    for num in row:
        total += num
print(total)