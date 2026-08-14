# Take two numbers as input print the greater of the two if they are equal print "Both numbers are equal".
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print(a, "is greater than", b)
elif b > a:
    print(b, "is greater than", a)
else:
    print("Both numbers are equal.")