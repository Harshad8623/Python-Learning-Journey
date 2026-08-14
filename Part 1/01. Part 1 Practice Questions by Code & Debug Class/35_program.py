# Write a function that ask a number from user and prints  if that number is even or odd
def even_odd():
    num = int(input("Enter a Number : "))
    if num % 2 == 0:
        return "Even"
    return "Odd"

print(even_odd())