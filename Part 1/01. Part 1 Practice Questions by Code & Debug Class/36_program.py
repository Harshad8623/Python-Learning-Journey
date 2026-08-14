# Write a function that print all the factors of a number entered by user
def factors():
    num = abs(int(input("Enter a Number : ")))
    for i in range(1, num+1):
        if num % i == 0:
            print(i)
factors()