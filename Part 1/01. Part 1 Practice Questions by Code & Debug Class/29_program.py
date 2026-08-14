# Remaining

# Space pattern
'''
          6
        5 6
      4 5 6
    3 4 5 6
  2 3 4 5 6
1 2 3 4 5 6

'''
for i in range(1, 7):
    for j in range(7-i, 7):
        print((6-i)*' ', end='')
        print(j, end=' ')
    print()

for i in range(1, 7):          # controls rows
    print((i - 1) * ' ', end='') # spaces before each row

    for j in range(7 - i, 7):  # controls numbers
        print(j, end=' ')

    print()                    # move to next line