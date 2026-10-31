# Space pattern
'''
          6
        5 6
      4 5 6
    3 4 5 6
  2 3 4 5 6
1 2 3 4 5 6

'''

for i in range(6, 0, -1):
    for k in range(1, i):
        print(' ', end = ' ')
    for j in range(i, 7):
        print(j ,end = ' ')
    print()


"""
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
"""

for i in range(1, 6):
    for j in range(1, 6 - i):
        print(' ', end = ' ')
    for k in range(1, i + 1):
        print(k, end = ' ')
    print()


"""
        5
      5 4
    5 4 3
  5 4 3 2
5 4 3 2 1
"""

for i in range(5, 0, -1):
    for j in range(1, i):
        print(' ', end = ' ')
    for k in range(5, i-1, -1):
        print(k, end = ' ')
    print()
print('\n')
"""
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
  1 2 3 4 5 6 7
    1 2 3 4 5
      1 2 3
        1
"""

for i in range(1, 6):
    for j in range(1, 6-i):
        print(' ', end = ' ')
    for k in range(1, (i * 2)):
        print(k, end = ' ')
    print()
for i in range(4, 0, -1):
    for j in range(1, 6-i):
        print(' ', end = ' ')
    for k in range(1, (i * 2)):
        print(k, end = ' ')
    print()