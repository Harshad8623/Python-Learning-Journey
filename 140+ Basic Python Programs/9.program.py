# Write a python program to solve Quadratic Equation
import math

a = float(input("Enter the coefficient of a : "))
b = float(input("Enter the coefficient of b : "))
c = float(input("Enter the coefficient of c : "))

discriment = (b ** 2) - (4 * a * c)

if discriment > 0:
    root1 = (-b + math.sqrt(discriment)) / 2 * a
    root2 = (-b - math.sqrt(discriment)) / 2 * a
    print("roots are :",root1, root2)
elif discriment == 0:
    root = -b / (2 * a)
    print(root)
else :
    real_part = -b / (2*a)
    imag_part = math.sqrt(abs(discriment)) / 2 * a
    print(f"root 1 is : {real_part} + {imag_part}i")
    print(f"root 2 is : {real_part} - {imag_part}i")