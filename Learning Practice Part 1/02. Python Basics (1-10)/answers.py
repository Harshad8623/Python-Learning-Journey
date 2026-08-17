"""
PART 1 — Python Basics (1-10)
"""

# 1. Hello World
print("Hello, World!")


# 2. Swap two numbers — using third variable
def swap_temp(a, b):
    temp = a
    a = b
    b = temp
    return a, b

# Swap without third variable — arithmetic
def swap_arithmetic(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

# Swap without third variable — XOR (integers only)
def swap_xor(a, b):
    a ^= b
    b ^= a
    a ^= b
    return a, b

# Pythonic / recommended
def swap_pythonic(a, b):
    return b, a


# 3. Calculator
def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return "Cannot divide by zero" if b == 0 else a / b
    elif op == "%":
        return "Cannot divide by zero" if b == 0 else a % b
    elif op == "**":
        return a ** b
    return "Invalid operator"

# Interview point: dictionary dispatch can replace a long if/elif chain.
def calculator_dispatch(a, b, op):
    operations = {
        "+": lambda: a + b,
        "-": lambda: a - b,
        "*": lambda: a * b,
        "/": lambda: a / b if b else "Cannot divide by zero",
        "%": lambda: a % b if b else "Cannot divide by zero",
        "**": lambda: a ** b,
    }
    return operations[op]() if op in operations else "Invalid operator"


# 4. Even or Odd
def even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

# Bitwise version: useful for understanding binary representation.
def even_odd_bitwise(n):
    return "Even" if (n & 1) == 0 else "Odd"


# 5. Positive / Negative / Zero
def number_sign(n):
    if n > 0:
        return "Positive"
    if n < 0:
        return "Negative"
    return "Zero"


# 6. Leap Year
def is_leap_year(year):
    # Divisible by 400 OR divisible by 4 but not 100.
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


# 7. Temperature Converter
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15


# 8. BMI Calculator
def bmi(weight_kg, height_m):
    if height_m <= 0:
        raise ValueError("Height must be positive")
    value = weight_kg / (height_m ** 2)
    if value < 18.5:
        category = "Underweight"
    elif value < 25:
        category = "Normal"
    elif value < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return round(value, 2), category


# 9. Area & Perimeter Calculator
def rectangle(length, width):
    return 2 * (length + width), length * width

def square(side):
    return 4 * side, side * side

def circle(radius):
    import math
    return 2 * math.pi * radius, math.pi * radius * radius

def triangle(a, b, c):
    perimeter = a + b + c
    s = perimeter / 2
    # Heron's formula
    area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
    return perimeter, area


# 10. Quick interview test
if __name__ == "__main__":
    print(swap_temp(10, 20))
    print(swap_arithmetic(10, 20))
    print(swap_xor(10, 20))
    print(swap_pythonic(10, 20))
    print(calculator(10, 3, "+"))
    print(even_odd(7))
    print(number_sign(-4))
    print(is_leap_year(2024))
    print(celsius_to_fahrenheit(25))
    print(bmi(70, 1.75))
    print(rectangle(5, 3))
