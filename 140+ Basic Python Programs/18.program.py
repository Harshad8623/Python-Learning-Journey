# Write a python program to print fibonacci series

a = 0
b = 1
n = int(input("Enter a Number (How many terms) : "))
i = 1
while i <= n:
    print(a, end = ' ')
    a, b = b, a + b
    i += 1