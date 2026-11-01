# ============================================================
# 1. ENCAPSULATION - PROTECTING AND CONTROLLING ACCESS TO DATA
# ============================================================

class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # private-style attribute

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount

    @property
    def balance(self):
        return self.__balance


account = BankAccount(10000)
account.deposit(2000)
account.withdraw(3000)
print("Encapsulation - balance:", account.balance)  # 9000

# Python naming conventions:
# name    -> public
# _name   -> protected-style convention; not enforced by Python
# __name  -> name mangling; not absolute security
#
# @property provides getter-style access.
# A @balance.setter can be added if controlled assignment is needed.


# ============================================================
# 2. INHERITANCE - REUSING CODE
# ============================================================

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle is starting")


class Car(Vehicle):
    def __init__(self, brand, fuel_type):
        super().__init__(brand)  # initialize parent part
        self.fuel_type = fuel_type

    def drive(self):
        print(f"{self.brand} car is driving")


car = Car("Toyota", "Petrol")
print("Inheritance - brand:", car.brand)
car.start()
car.drive()

# Main types:
# 1. Single:       Vehicle -> Car
# 2. Multilevel:   Animal -> Mammal -> Dog
# 3. Multiple:     Flyer + Swimmer -> Duck
# 4. Hierarchical: Animal -> Dog, Cat, Cow

# Method overriding: child supplies its own implementation.
class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("Dog barks")


Dog().speak()

# super() accesses the next implementation in the Method Resolution Order.
class BetterDog(Animal):
    def speak(self):
        super().speak()
        print("Dog also barks")


BetterDog().speak()
print("MRO:", BetterDog.mro())


# ============================================================
# 3. POLYMORPHISM - SAME INTERFACE, DIFFERENT BEHAVIOUR
# ============================================================

class DogSpeaker:
    def speak(self):
        print("Dog barks")


class CatSpeaker:
    def speak(self):
        print("Cat meows")


class CowSpeaker:
    def speak(self):
        print("Cow moos")


def make_speak(animal):
    # This function works with any object that provides speak().
    animal.speak()


print("Polymorphism:")
for animal in [DogSpeaker(), CatSpeaker(), CowSpeaker()]:
    make_speak(animal)

# This is an example of duck typing:
# Python cares that the object supports speak(), not necessarily
# which class it belongs to.

# Operator overloading is another form of polymorphic behaviour.
class Distance:
    def __init__(self, kilometres):
        self.kilometres = kilometres

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return Distance(self.kilometres + other.kilometres)

    def __str__(self):
        return f"{self.kilometres} km"


distance1 = Distance(10)
distance2 = Distance(5)
print("Operator overloading:", distance1 + distance2)

# Python does not provide traditional compile-time method overloading
# based on different parameter lists like Java/C++.
# Defaults, *args and other techniques can provide similar flexibility.


# ============================================================
# 4. ABSTRACTION - HIDING IMPLEMENTATION DETAILS
# ============================================================

from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid Rs. {amount} using credit card")


class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid Rs. {amount} using UPI")


payments = [CreditCardPayment(), UPIPayment()]
print("Abstraction:")
for payment in payments:
    payment.pay(500)

# Payment() cannot be instantiated because pay() is abstract.
# A concrete child class must implement every inherited abstract method.


# ============================================================
# DIFFERENCES BETWEEN THE FOUR PILLARS
# ============================================================

"""
Encapsulation:
- Focus: controlling access to data.
- Example: balance is changed through deposit/withdraw methods.

Inheritance:
- Focus: code reuse and class relationships.
- Example: Car inherits common features from Vehicle.

Polymorphism:
- Focus: same interface, different implementations/behaviour.
- Example: Dog, Cat and Cow each implement speak().

Abstraction:
- Focus: exposing essential operations and hiding implementation details.
- Example: Payment defines pay(); UPI and card payments implement it.
"""


# ============================================================
# INTERVIEW QUESTIONS WITH SHORT ANSWERS
# ============================================================

"""
BASIC OOP QUESTIONS
-------------------

1. What is OOP?
Object-Oriented Programming is a programming approach that organizes
code around objects, which combine data (attributes) and behaviour
(methods).

2. What are the four pillars of OOP?
Encapsulation, Inheritance, Polymorphism and Abstraction.

3. What is a class?
A class is a blueprint used to create objects.

4. What is an object?
An object is an instance of a class. It has state (attributes) and
behaviour (methods).

ENCAPSULATION
-------------

5. What is encapsulation?
It combines data and methods in a class and controls access to data.

6. Why is encapsulation useful?
It supports validation, controlled updates, and maintainable code.

7. What do public, protected and private mean in Python?
Public has no leading underscore. _name is a protected-style convention.
__name triggers name mangling; it is not strict security.

8. Does Python support private variables?
Python does not enforce strict private access. Double underscores
trigger name mangling.

9. What is @property?
It allows a method to be accessed like an attribute and can provide
controlled getter/setter behaviour.

INHERITANCE
-----------

10. What is inheritance?
A child class reuses attributes and methods from a parent class.

11. What are the benefits of inheritance?
Code reuse, less duplication, and support for overriding and extension.

12. What is method overriding?
A child class provides its own implementation of an inherited method.

13. What is super()?
It provides access to the next implementation in the method resolution
order, commonly used to call parent-class methods or initializers.

14. What is MRO?
Method Resolution Order is the order Python follows when searching
for methods and attributes in an inheritance hierarchy.

15. What are the types of inheritance?
Single, multilevel, multiple and hierarchical. Hybrid structures can
combine these patterns.

POLYMORPHISM
------------

16. What is polymorphism?
The same interface or operation can produce different behaviour
depending on the object.

17. What is duck typing?
Python allows an operation when an object supports the required
behaviour, without requiring a particular class relationship.

18. What is operator overloading?
Defining how operators work with custom objects using special methods
such as __add__ and __eq__.

19. Does Python support method overloading?
Not traditional compile-time overloading based on parameter signatures.
Defaults, *args and dispatch techniques can provide similar behaviour.

20. What is the difference between overriding and overloading?
Overriding replaces an inherited method implementation in a child class.
Overloading uses the same method name for different parameter patterns.

ABSTRACTION
-----------

21. What is abstraction?
It hides implementation details and exposes essential functionality.

22. What is an abstract class?
A base class that can declare abstract methods and cannot be instantiated
while abstract methods remain unimplemented.

23. What is an abstract method?
A method declared using @abstractmethod that concrete child classes
must implement.

24. What is ABC?
ABC stands for Abstract Base Class. Python's abc module supports
abstract base classes and abstract methods.

25. What happens if a child class does not implement an abstract method?
It remains abstract and cannot be instantiated.

SCENARIO-BASED QUESTIONS
------------------------

26. How would you protect a bank account balance?
Keep the balance as a private-style attribute and provide validated
deposit and withdrawal methods.

27. How would you design different payment methods?
Define a common Payment interface or abstract base class with pay().
Implement it in UPI, card and wallet payment classes.

28. How would you avoid repeating common vehicle functionality?
Put shared attributes and methods in a Vehicle parent class and let
Car and Bike inherit them, when the relationship is appropriate.

29. How can one function work with different object types?
Use polymorphism or duck typing. For example, call speak() on any
object that provides that method.

30. When should you avoid inheritance?
Avoid it when the classes do not have a genuine is-a relationship or
when composition would make the design simpler and less tightly coupled.
"""


# ============================================================
# ROLE-BASED PREPARATION NOTES
# ============================================================

"""
SOFTWARE ENGINEER / SDE / BACKEND DEVELOPER
-------------------------------------------
Be ready to:
- Explain all four pillars with code.
- Write and debug classes, constructors and instance methods.
- Explain overriding, super(), MRO and multiple inheritance.
- Implement __str__, __eq__ and __add__.
- Use ABC and @abstractmethod.
- Design small systems such as bank accounts, payments, employees,
  notifications and vehicles.
- Explain when composition is better than inheritance.

DATA ANALYST
------------
OOP may be tested in Python interviews, but role preparation should
also prioritize Python data handling, SQL, joins, aggregation,
statistics, Excel/Power BI and communicating insights.
Understand classes, objects, encapsulation and basic inheritance;
be able to read and explain simple OOP code.

COMPANY PREPARATION
-------------------
For TCS, Infosys, Deloitte, Visa, Mastercard and other employers,
interview rounds and questions vary by role, campus, team and year.
Do not assume these are verified questions from a particular company.
Use this file as a role-relevant OOP preparation set, and practise
explaining each answer aloud with a small example.
"""

# END OF NOTES