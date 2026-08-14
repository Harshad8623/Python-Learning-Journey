# Program to print numbers between 1 and 100 that are divisible by both 2 and 7
i = 1
while i <= 100:
    if i % 2 == 0 and i % 7 == 0:
        print(i)
    i += 1