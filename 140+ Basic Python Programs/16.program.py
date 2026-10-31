# Write a program to find factorial of given number

num = int(input("Enter a Number : "))
fact = 1
if num < 0:
    print("The factorial of a negative number is undefined")
elif num == 0 or num == 1:
    print(f"factorial of {num} is 1")
else:
    for i in range(1, num+1):
        fact *= i
    print(f"factorial of {num} is {fact}")
