'''
6
6 5
6 5 4
6 5 4 3
6 5 4 3 2
6 5 4 3 2 1
6 5 4 3 2
6 5 4 3
6 5 4
6 5
6
'''

for i in range(1, 7):
    for j in range(6, 6-i, -1):
        print(j, end =' ')
    print()
for i in range(5, 0, -1):
    for j in range(6, 6-i, -1):
        print(j, end =' ')
    print()
print("\n")


# Another Approach
for i in range(6, 0, -1):
    for j in range(6, i-1, -1):
        print(j, end = ' ')
    print()
for i in range(2, 6):
    for j in range(6, i-1, -1):
        print(j, end = ' ')
    print()