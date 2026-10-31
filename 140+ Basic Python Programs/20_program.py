# Write a Python program to find Armstrong numbers in an interval

a = int(input("Enter Lower limit: "))
b = int(input("Enter Upper limit: "))

for i in range(a, b + 1):
    if i < 0:
        continue

    ln = len(str(i))
    total = 0
    n = i

    while n > 0:
        dg = n % 10
        total += dg ** ln
        n //= 10

    if total == i:
        print(i)
