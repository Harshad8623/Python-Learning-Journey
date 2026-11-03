"""
TYPES OF METHODS IN PYTHON
==========================

Python classes commonly use three types of methods:

1. Instance Method
2. Class Method
3. Static Method

This file explains each type with simple examples and outputs.
"""


# ============================================================
# 1. INSTANCE METHOD
# ============================================================
# - An instance method works with a particular object.
# - It takes 'self' as its first parameter.
# - 'self' refers to the current object.
# - It can access and modify instance variables and class variables.
# - No decorator is required.


class Student:
    college = "CSMSS College of Engineering"  # Class variable

    def __init__(self, name: str, age: int) -> None:
        self.name = name                    # Instance variable
        self.age = age                      # Instance variable

    def display_details(self) -> None:
        """Instance method: accesses instance variables using self."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def update_age(self, new_age: int) -> None:
        """Instance method: modifies an instance variable."""
        self.age = new_age

    def display_college(self) -> None:
        """An instance method can also access a class variable."""
        print(f"College: {self.college}")


print("\n========== 1. INSTANCE METHOD ==========")

student1 = Student("Harshad", 21)
student1.display_details()
student1.update_age(22)
print("After updating age:")
student1.display_details()
student1.display_college()


# ============================================================
# 2. CLASS METHOD
# ============================================================
# - A class method works with the class rather than a particular object.
# - It takes 'cls' as its first parameter.
# - 'cls' refers to the current class.
# - It is defined using the @classmethod decorator.
# - It can access and modify class variables.
# - It does not receive the instance automatically.


class Employee:
    company = "OpenAI"

    def __init__(self, name: str) -> None:
        self.name = name

    @classmethod
    def change_company(cls, new_company: str) -> None:
        """Class method: changes a class-level variable."""
        cls.company = new_company

    @classmethod
    def display_company(cls) -> None:
        """Class method: displays the class-level variable."""
        print(f"Company: {cls.company}")


print("\n========== 2. CLASS METHOD ==========")

Employee.display_company()
Employee.change_company("Microsoft")
Employee.display_company()

# A class method can also be called using an object.
employee1 = Employee("Aniruddh")
employee1.display_company()


# ============================================================
# 3. STATIC METHOD
# ============================================================
# - A static method does not receive 'self' or 'cls' automatically.
# - It is defined using the @staticmethod decorator.
# - It does not directly access instance or class variables.
# - It is useful for a utility/helper function related to the class.
# - It can be called using either the class name or an object.


class Calculator:

    @staticmethod
    def add(a: int, b: int) -> int:
        """Static method: adds two numbers."""
        return a + b

    @staticmethod
    def is_even(number: int) -> bool:
        """Static method: checks whether a number is even."""
        return number % 2 == 0


print("\n========== 3. STATIC METHOD ==========")

print("Addition:", Calculator.add(10, 20))
print("Is 8 even?", Calculator.is_even(8))

# A static method can also be called using an object.
calculator1 = Calculator()
print("Addition using object:", calculator1.add(5, 7))


# ============================================================
# IMPORTANT: A METHOD WITHOUT self IS NOT AUTOMATICALLY STATIC
# ============================================================
# If a method is defined without self and without @staticmethod,
# calling it through an object usually causes a TypeError because
# Python automatically passes the object as the first argument.


class Demo:

    def show_message():
        print("This is a regular function stored in the class.")

    @staticmethod
    def show_static_message():
        print("This is a static method.")


print("\n========== METHOD WITHOUT self ==========")

# Calling the first function through the class works:
Demo.show_message()

# Calling the first function through an object causes TypeError:
# demo1 = Demo()
# demo1.show_message()  # TypeError: takes 0 positional arguments but 1 was given

# The static method works through both the class and an object:
Demo.show_static_message()
demo1 = Demo()
demo1.show_static_message()


# ============================================================
# QUICK COMPARISON
# ============================================================
#
# Instance Method:
#     def method(self):
#         ...
#
# Class Method:
#     @classmethod
#     def method(cls):
#         ...
#
# Static Method:
#     @staticmethod
#     def method():
#         ...
#
# Remember:
# self -> current object
# cls  -> current class
# static method -> receives neither automatically
#
# Note:
# A static method can still access class or object data if those
# values are explicitly passed to it, or if it refers to the class
# by name. It simply does not receive self or cls automatically.
