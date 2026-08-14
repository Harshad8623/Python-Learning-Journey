'''
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''

for i in range(1, 7):
    for j in range(1, 7-i+1):
        print(j, end=' ')
    print()
print("\n")

# Another solution

for i in range(6, 0, -1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()