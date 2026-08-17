# Take a numbers as input print largest of the three numbers.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# method 1
print("The largest number is:", max(num1, num2, num3))
# method 2
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print("The largest number is:", largest)

# method 3
print("The largest number is:", num1 if (num1 >= num2 and num1 >= num3) else (num2 if (num2 >= num1 and num2 >= num3) else num3))