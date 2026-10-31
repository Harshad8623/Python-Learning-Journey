# Write a python program to print prime numbers in the interval a to b
import math

a = int(input("Enter Starting Number: "))
b = int(input("Enter Closing Number: "))

for i in range(a, b + 1):
    if i < 2:
        continue

    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            break
    else:
        print(i, end=' ')