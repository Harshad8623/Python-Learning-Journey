n = int(input("Enter a Number : "))
fact = 1
for  i in range(1, n+1):
    fact *= i
print(fact)


# Using while loop
n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial =", fact)



# using Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))



# Using Python's built-in math.factorial()
import math
print(math.factorial(5))


# Using a function + for loop, This is a nice approach because the logic is reusable.
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
print(factorial(5))