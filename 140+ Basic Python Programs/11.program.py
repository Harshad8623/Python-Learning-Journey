# Program to Check if a number is Positive, Negative or Zero

while True:
    try:
        num = int(input("Enter a number (or type anything else to exit): "))

        if num == 0:
            print("Number is Zero")
        elif num > 0:
            print("Number is Positive")
        else:
            print("Number is Negative")

    except ValueError:
        print("Thank You! Visit Again!")
        break