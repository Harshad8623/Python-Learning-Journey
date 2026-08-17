# Take input a 3x3 matrix, print its upper triangle. Replace all elements in the lower triangle (below the main diagonal) with an asterisk (*).

matrix = []
a = []
for i in range(3):
    for j in range(3):
        a.append(input(f"Enter Number for {i+1}, {j+1} position : "))
    matrix.append(a)
    a = []


for l in range(3):
    for m in range(3):
        if l <= m :
            matrix[l][m] = '*'
    print(matrix[l])


# if you want :
# ['1', '2', '3']
# ['*', '3', '1']
# ['*', '*', '5']
# Then : if l > m



# if you want :
# ['*', '2', '3']
# ['*', '*', '1']
# ['*', '*', '*']
# Then : if l >= m


# if you want :
# ['1', '*', '*']
# ['2', '1', '*']
# ['5', '4', '5']
# Then : if l < m


# if you want :
# ['*', '*', '*']
# ['6', '*', '*']
# ['3', '2', '*']
# Then : if l <= m