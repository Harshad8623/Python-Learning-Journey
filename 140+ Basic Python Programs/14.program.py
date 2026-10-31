# Write a python program to check prime number
import math

num = int(input("Enter a Number: "))
if num < 2:
    print("Not Prime Number")
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print("Not Prime Number")
            break
    else:
        print("Prime Number")