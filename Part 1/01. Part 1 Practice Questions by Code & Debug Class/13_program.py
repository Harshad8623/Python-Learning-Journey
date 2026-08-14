# Take a number as an input and check if it is even or odd in one line using ternary operator.
num = int(input("Enter a number: "))
print(f"{num} is an even number." if num % 2 == 0 else f"{num} is an odd number.")