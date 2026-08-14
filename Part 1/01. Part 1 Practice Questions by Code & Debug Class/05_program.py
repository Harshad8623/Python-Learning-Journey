# take a number as input print the result of that number raised to the power of 3 and also print what //7 and %7 of that number is.
num = int(input("Enter a number: "))
print("The number raised to the power of 3 is:", num ** 3)
# To avoid division by zero, we check if num is not zero before performing floor division and modulus
if num != 0:
    print("The floor division of", num, "by 7 is:", num // 7)
    print("The modulus of", num, "by 7 is:", num % 7)
else:
    print("Answer is Zero because the number is 0.")