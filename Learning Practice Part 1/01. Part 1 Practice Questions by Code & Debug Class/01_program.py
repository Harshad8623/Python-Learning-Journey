# Take two numbers as input from the user and perform basic arithmetic operations on them.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Addition
print("Sum of", a, "and", b, "is:", a + b)

# Subtraction
print("Difference of", a, "and", b, "is:", a - b)

# Multiplication
print("Product of", a, "and", b, "is:", a * b)

# Division, Modulus, and Floor Division
# To avoid division by zero, check if b is not zero
if b != 0:
    print("Quotient of", a, "and", b, "is:", a / b)
    print("Modulus of", a, "and", b, "is:", a % b)
    print("Floor Division of", a, "and", b, "is:", a // b)
else:
    print("Quotient of", a, "and", b, "is: Not Defined")
    print("Modulus of", a, "and", b, "is: Not Defined")
    print("Floor Division of", a, "and", b, "is: Not Defined")

# Exponentiation
print("Exponentiation of", a, "to the power of", b, "is:", a ** b)

# Average
print("Average of", a, "and", b, "is:", (a + b) / 2)