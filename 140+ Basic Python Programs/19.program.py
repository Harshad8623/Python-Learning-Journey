# Write a python program to check the number is armstrong number or not

num = int(input("Enter a Number : "))
ln = len(str(abs(num)))
if num < 0:
    print("Negative numbers are not Armstrong numbers")
else:
    total = 0
    n = num
    while n > 0:
        dg = n % 10
        total += dg ** ln
        n //= 10
    if total == num:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")