# Take two numbers as input from the user and perform basic arithmetic operations on them.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum of", a, "and", b, "is:", a + b)
print("Difference of", a, "and", b, "is:", a - b)
print("Product of", a, "and", b, "is:", a * b)
# To avoid division by zero, we check if b is not zero before performing division and modulus
if b != 0:
    print("Quotient of", a, "and", b, "is:", a / b)
    print("Modulus of", a, "and", b, "is:", a % b)
print("Floor Division of", a, "and", b, "is:", a // b)
print("Exponentiation of", a, "to the power of", b, "is:", a ** b)
print("Average of", a, "and", b, "is:", (a + b) / 2)