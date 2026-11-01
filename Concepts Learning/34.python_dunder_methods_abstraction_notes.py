"""
PYTHON OOP NOTES

Dunder (Magic) Methods
Abstraction

"""


# ============================================================
# CHAPTER 10: DUNDER (MAGIC) METHODS
# ============================================================

# 1. What are Dunder Methods?
#
# Dunder means "double underscore".
# These special methods have names that begin and end with two underscores.
#
# Examples:
# __init__, __str__, __repr__, __eq__, __lt__, __add__, __len__
#
# Python calls many of these methods automatically when we use
# familiar operations such as print(object), object1 == object2,
# object1 + object2, and len(object).


# 2. __str__() - readable string representation
#
# When we print an object, Python calls its __str__() method.
# We can define this method to decide what a user sees.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point: ({self.x}, {self.y})"


p1 = Point(3, 4)
p2 = Point(6, 5)

print("STR EXAMPLE")
print(p1)  # Python internally calls p1.__str__()
print(p2)
print()


# Important:
# __str__() must return a string.
# It should give a clear, readable representation of the object.


# 3. __repr__() - developer-oriented representation
#
# __repr__() is intended to provide an unambiguous/developer-friendly
# representation of an object.
# repr(object) calls __repr__().
#
# If __str__() is not defined, print(object) can fall back to __repr__().
# If neither is defined, Python displays its default object representation.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} costs Rs. {self.price}"

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price!r})"


product = Product("Keyboard", 1200)

print("REPR EXAMPLE")
print(product)       # Calls __str__()
print(repr(product)) # Calls __repr__()
print()


# 4. __eq__() - equality comparison
#
# By default, two separate objects generally compare unequal with ==,
# even if their attributes contain the same values.
# We can define __eq__() to decide what equality means for our class.
#
# For a == b:
#   a is passed as self
#   b is passed as other

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount


a = Money(100)
b = Money(100)
c = Money(200)

print("EQ EXAMPLE")
print(a == b)  # True: same amount
print(a == c)  # False: different amounts
print()


# 5. __lt__() - less-than comparison
#
# __lt__ means "less than".
# For a < b, Python can call a.__lt__(b).

class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def __lt__(self, other):
        if not isinstance(other, Wallet):
            return NotImplemented
        return self.amount < other.amount


wallet1 = Wallet(80)
wallet2 = Wallet(100)

print("LT EXAMPLE")
print(wallet1 < wallet2)  # True
print(wallet2 < wallet1)  # False
print()


# Other comparison dunder methods:
#
# __eq__  -> ==
# __lt__  -> <
# __le__  -> <=
# __gt__  -> >
# __ge__  -> >=
#
# These methods should return a meaningful comparison result.
# Python does not automatically know which attribute should be compared.


# 6. __add__() - addition of objects
#
# For object1 + object2, Python can call object1.__add__(object2).
# We decide what adding two objects of our class should mean.

class Distance:
    def __init__(self, km):
        self.km = km

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented

        # Return a new Distance object, not just an integer.
        return Distance(self.km + other.km)

    def __str__(self):
        return f"{self.km} km"


d1 = Distance(10)
d2 = Distance(5)

total_distance = d1 + d2

print("ADD EXAMPLE")
print(total_distance)  # 15 km
print()


# Note:
# __add__ could return a number or a new object.
# Choose the return type that makes sense for your class.


# 7. __len__() - length of an object
#
# len(object) calls object.__len__().
# The method should return a non-negative integer.

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)


playlist = Playlist()
playlist.add_song("Song A")
playlist.add_song("Song B")
playlist.add_song("Song C")

print("LEN EXAMPLE")
print(playlist.songs)  # The songs
print(len(playlist))   # 3
print()


# More useful dunder methods to know:
#
# __getitem__(self, key) -> supports object[key]
# __call__(self, ...)    -> supports object(...)
# __mul__(self, other)   -> supports object * other
# __sub__(self, other)   -> supports object - other
#
# These were mentioned in the lecture as examples of other dunder
# methods. The main worked examples above are the methods explained
# in detail in the transcript.


# ============================================================
# CHAPTER 11: ABSTRACTION
# ============================================================

# 1. What is Abstraction?
#
# Abstraction means hiding the internal implementation details
# and exposing only the essential features or operations.
#
# Real-life example:
# When you use an ATM, you select withdraw and enter an amount.
# You do not need to know all the internal steps used by the bank
# to process the transaction.


# 2. Abstract classes and abstract methods
#
# Python provides the abc module.
# ABC means Abstract Base Class.
#
# An abstract class is a class that cannot be instantiated directly
# when it contains abstract methods that have not been implemented.
#
# An abstract method declares a method that concrete child classes
# are required to implement.

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Shape is abstract. This would raise TypeError:
#
# shape = Shape()
#
# A child class must implement all inherited abstract methods
# before its objects can be created.


# 3. Rectangle implements the abstract methods

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


rectangle = Rectangle(20, 10)

print("ABSTRACTION - RECTANGLE")
print("Area:", rectangle.area())             # 200
print("Perimeter:", rectangle.perimeter())   # 60
print()


# 4. Circle implements the same abstract methods

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


circle = Circle(5)

print("ABSTRACTION - CIRCLE")
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())
print()


# 5. Why use abstraction?
#
# - It defines a common structure for related classes.
# - It forces concrete child classes to implement required methods.
# - It helps make code more organized and consistent.
# - It allows us to work with different child objects through
#   a common interface.


# ============================================================
# IMPORTANT DIFFERENCE
# ============================================================

# Abstract method:
# A method declared in an abstract base class using @abstractmethod.
# A concrete child class must implement it before it can be instantiated.
#
# Normal method:
# A method with an implementation that child classes can inherit.
#
# Abstract class:
# A base class intended to define a common interface/structure.
# It cannot be instantiated while abstract methods remain unimplemented.


# ============================================================
# INTERVIEW QUESTIONS AND ANSWERS
# ============================================================

"""
Q1. What are dunder methods in Python?
Answer:
Dunder methods are special methods whose names begin and end with
double underscores. Python uses them to define how objects behave
with built-in operations. Examples include __init__, __str__, and __len__.

Q2. What is __str__()?
Answer:
__str__() returns a readable string representation of an object.
It is called when we use print(object) or str(object).

Q3. What is the difference between __str__() and __repr__()?
Answer:
__str__() is mainly for a readable, user-friendly representation.
__repr__() is mainly for a developer-friendly and preferably
unambiguous representation.

Q4. What is __eq__()?
Answer:
__eq__() defines how two objects are compared using ==.

Q5. What is __lt__()?
Answer:
__lt__() defines the behaviour of the less-than operator (<).

Q6. What is operator overloading?
Answer:
Operator overloading means defining how operators such as +, ==,
or < behave with objects of our own classes, using special methods
such as __add__, __eq__, and __lt__.

Q7. What is __add__()?
Answer:
__add__() defines what happens when we use the + operator between
objects of a class.

Q8. What is __len__()?
Answer:
__len__() defines the length of an object and is called by len(object).
It should return a non-negative integer.

Q9. What is abstraction?
Answer:
Abstraction means hiding internal implementation details and
showing only the essential features to the user.

Q10. What is an abstract class?
Answer:
An abstract class is a base class that can define abstract methods.
It cannot be instantiated while it still has unimplemented abstract
methods.

Q11. What is an abstract method?
Answer:
An abstract method is a method declared with @abstractmethod.
Concrete child classes must provide its implementation.

Q12. What is the ABC module?
Answer:
abc is a Python standard-library module used to create abstract
base classes and abstract methods. ABC stands for Abstract Base Class.

Q13. Can we create an object of an abstract class?
Answer:
Not if it still has abstract methods that have not been implemented.
Python raises TypeError when we try.

Q14. What happens if a child class does not implement all abstract
methods?
Answer:
The child class remains abstract, so we cannot create its object.

Q15. Why is abstraction useful?
Answer:
It provides a common structure, enforces required methods in child
classes, and helps keep code organized and consistent.
"""


# ============================================================
# QUICK REVISION
# ============================================================

"""
DUNDER METHODS
__str__()   -> readable string; print(object)
__repr__()  -> developer-oriented representation; repr(object)
__eq__()    -> equality; object1 == object2
__lt__()    -> less than; object1 < object2
__le__()    -> less than or equal to; object1 <= object2
__gt__()    -> greater than; object1 > object2
__ge__()    -> greater than or equal to; object1 >= object2
__add__()   -> addition; object1 + object2
__len__()   -> length; len(object)

ABSTRACTION
ABC              -> Abstract Base Class
@abstractmethod  -> declares an abstract method
Abstract class   -> defines a common structure/interface
Concrete child   -> implements all required abstract methods
"""

# END OF NOTES
