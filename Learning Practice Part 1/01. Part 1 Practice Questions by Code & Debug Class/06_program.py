# Take 2 numbers as input without using * calculate and print the result of their multiplication. (Hint: Use + operator)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = 0

for i in range(abs(num2)):
    result += abs(num1)

if (num1 < 0 and num2 >= 0) or (num1 >= 0 and num2 < 0):
    result = -result

print("The result of multiplication is:", result)