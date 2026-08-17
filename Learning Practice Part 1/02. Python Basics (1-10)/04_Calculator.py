# Calculator using eval function
exp = input("Enter your expression: ")
result = eval(exp)
print("Result: ", result)


# CLI Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
choice = input("Enter choice (1/2/3/4/5): ")
if choice == '1':
    print(num1, "+", num2, "=", num1 + num2)
elif choice == '2':
    print(num1, "-", num2, "=", num1 - num2)
elif choice == '3':
    print(num1, "*", num2, "=", num1 * num2)
elif choice == '4':
    if num2 != 0:
        print(num1, "/", num2, "=", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
elif choice == '5':
    print(num1, "%", num2, "=", num1 % num2)
else:
    print("Invalid input")
