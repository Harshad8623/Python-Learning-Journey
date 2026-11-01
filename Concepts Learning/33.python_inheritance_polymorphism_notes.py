"""
PYTHON OOP — INHERITANCE AND POLYMORPHISM

Topics covered in this chapter:
1. Inheritance: parent class and child class
2. Basic / single inheritance
3. Reusing parent attributes and methods
4. Method overriding
5. super() with methods
6. super() with __init__()
7. Types of inheritance:
   - Single
   - Multilevel
   - Multiple
   - Hierarchical
8. Diamond problem and Method Resolution Order (MRO)
9. Polymorphism
10. Method overriding as runtime polymorphism
"""


# ============================================================
# 1. WHAT IS INHERITANCE?
# ============================================================

"""
Inheritance is an OOP concept in which a child class can reuse
attributes and methods of a parent class.

Parent class:
- Also called base class or superclass.

Child class:
- Also called derived class or subclass.

Why use inheritance?
- Code reusability.
- Avoid writing the same common code again and again.
- Represent an "is-a" relationship.

Example:
A Dog is an Animal.
A Car is a Vehicle.

Syntax:
    class ChildClass(ParentClass):
        pass
"""


# ============================================================
# 2. BASIC / SINGLE INHERITANCE
# ============================================================

"""
A child class inherits from one parent class.

Vehicle is the parent class.
Car is the child class.
Car can use the brand attribute and start() method from Vehicle.
Car also has its own drive() method.
"""

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle is starting.")


class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} car is driving.")


print("2. BASIC / SINGLE INHERITANCE")
v1 = Vehicle("Maruti")
v1.start()
# v1.drive()  # This would raise AttributeError: Vehicle has no drive().

car1 = Car("Maruti")
car1.start()  # Inherited from Vehicle
car1.drive()  # Defined inside Car
print("Car brand:", car1.brand)  # Inherited attribute


# ============================================================
# 3. INHERITING __init__(), ATTRIBUTES, AND METHODS
# ============================================================

"""
If the child class does not define its own __init__(), Python
uses the parent's __init__() when creating a child object.

The Dog class below does not define __init__().
Therefore, Animal's __init__() receives the name and age.
Dog can access the parent's attributes and methods.
"""

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} is speaking.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")


print("\\n3. INHERITED CONSTRUCTOR, ATTRIBUTES, AND METHODS")
dog1 = Dog("ABC", 6)

print("Name:", dog1.name)
print("Age:", dog1.age)
dog1.speak()
dog1.sleep()
dog1.bark()


# ============================================================
# 4. METHOD OVERRIDING
# ============================================================

"""
Method overriding happens when a child class defines a method
with the same name as a method in its parent class.

When that method is called using a child object, Python uses
the child's version.

Parent Animal has speak().
Child Dog also has speak().
Dog's speak() overrides Animal's speak().
"""

class AnimalForOverride:
    def speak(self):
        print("Animal is speaking.")


class DogForOverride(AnimalForOverride):
    def speak(self):
        print("Dog is barking.")


print("\\n4. METHOD OVERRIDING")
animal = AnimalForOverride()
dog = DogForOverride()

animal.speak()  # Animal's version
dog.speak()     # Dog's overridden version


# ============================================================
# 5. USING super() WITH A PARENT METHOD
# ============================================================

"""
super() lets a child class call a method from its parent class
(or the next class in the method resolution order).

If the child overrides speak() but also wants the parent's
speak() to run, it can use:
    super().speak()

Do not use self.speak() for this purpose inside the overriding
speak() method. That would call the child's method again.
"""

class AnimalWithSuper:
    def speak(self):
        print("Animal is speaking.")


class DogWithSuper(AnimalWithSuper):
    def speak(self):
        super().speak()
        print("Dog is barking.")


print("\\n5. super() WITH A PARENT METHOD")
dog2 = DogWithSuper()
dog2.speak()


# ============================================================
# 6. super() WITH __init__()
# ============================================================

"""
When a child class defines its own __init__(), it overrides the
parent's initializer.

If the child still needs the parent's initialization, call:
    super().__init__(parent_arguments)

Example:
Vehicle stores the common brand.
Car stores its specific fuel type.
The Car constructor initializes both sets of attributes.
"""

class VehicleWithBrand:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print(f"Brand: {self.brand}")


class CarWithFuel(VehicleWithBrand):
    def __init__(self, brand, fuel):
        super().__init__(brand)  # Calls parent __init__()
        self.fuel = fuel         # Child-specific attribute

    def display_car(self):
        print(f"You have a {self.brand} car with {self.fuel} fuel.")


print("\\n6. super() WITH __init__()")
car2 = CarWithFuel("Maruti", "Petrol")
car2.display()
car2.display_car()


# ============================================================
# 7. TYPES OF INHERITANCE
# ============================================================

"""
A. SINGLE INHERITANCE
One child class inherits from one parent class.

    Parent
      |
    Child


B. MULTILEVEL INHERITANCE
A class inherits from a class that itself inherits from another.

    Animal
      |
    Mammal
      |
     Dog


C. MULTIPLE INHERITANCE
One child class inherits from more than one parent class.

    Flyer    Swimmer
       \\      /
         Duck


D. HIERARCHICAL INHERITANCE
Multiple child classes inherit from the same parent class.

          Animal
         /  |   \\
       Dog Cat  Cow
"""


# ============================================================
# 8. MULTILEVEL INHERITANCE
# ============================================================

"""
Dog inherits Mammal.
Mammal inherits Animal.

So Dog can access:
- Its own bark() method.
- Mammal's feed_young() method.
- Animal's breathe() method.
"""

class AnimalLevel1:
    def breathe(self):
        print("Animal is breathing.")


class MammalLevel2(AnimalLevel1):
    def feed_young(self):
        print("Mammal feeds its young.")


class DogLevel3(MammalLevel2):
    def bark(self):
        print("Dog is barking.")


print("\\n8. MULTILEVEL INHERITANCE")
dog3 = DogLevel3()
dog3.breathe()     # From AnimalLevel1
dog3.feed_young()  # From MammalLevel2
dog3.bark()        # From DogLevel3


# ============================================================
# 9. MULTIPLE INHERITANCE
# ============================================================

"""
One child class inherits from multiple parent classes.

Flyer has fly().
Swimmer has swim().
Duck inherits from both and has quack().
"""

class Flyer:
    def fly(self):
        print("Can fly.")


class Swimmer:
    def swim(self):
        print("Can swim.")


class Duck(Flyer, Swimmer):
    def quack(self):
        print("Duck says quack.")


print("\\n9. MULTIPLE INHERITANCE")
duck = Duck()
duck.fly()
duck.swim()
duck.quack()


# ============================================================
# 10. HIERARCHICAL INHERITANCE
# ============================================================

"""
Multiple child classes inherit from one parent class.

Dog, Cat, and Cow all inherit the common breathe() method
from AnimalBase. Each child has its own specific method.
"""

class AnimalBase:
    def breathe(self):
        print("Animal is breathing.")


class DogChild(AnimalBase):
    def bark(self):
        print("Dog is barking.")


class CatChild(AnimalBase):
    def meow(self):
        print("Cat is meowing.")


class CowChild(AnimalBase):
    def moo(self):
        print("Cow is mooing.")


print("\\n10. HIERARCHICAL INHERITANCE")
dog_child = DogChild()
cat_child = CatChild()
cow_child = CowChild()

dog_child.breathe()
dog_child.bark()

cat_child.breathe()
cat_child.meow()

cow_child.breathe()
cow_child.moo()


# ============================================================
# 11. DIAMOND PROBLEM AND MRO
# ============================================================

"""
The diamond inheritance shape:

        A
       / \\
      B   C
       \\ /
        D

D inherits from B and C.
Both B and C inherit from A.

If more than one parent provides a method with the same name,
which implementation should Python use?

Python uses Method Resolution Order (MRO) to decide the lookup
order. You can inspect it using:
    ClassName.mro()
or:
    ClassName.__mro__

In the example below:
- D inherits from B first, then C.
- B and C inherit from A.
- D does not define hello().
- B defines hello(), so D().hello() uses B's method.
"""

class A:
    def hello(self):
        print("Hello from A")


class B(A):
    def hello(self):
        print("Hello from B")


class C(A):
    def hello(self):
        print("Hello from C")


class D(B, C):
    pass


print("\\n11. DIAMOND PROBLEM AND MRO")
d = D()
d.hello()

print("MRO of D:")
for cls in D.mro():
    print(cls.__name__)

"""
For this class hierarchy, the MRO is:
D -> B -> C -> A -> object

Python checks D first, then B, then C, then A, then object.
Because B has hello(), B's method is selected.
"""


# ============================================================
# 12. WHAT IS POLYMORPHISM?
# ============================================================

"""
Polymorphism:
- Poly means many.
- Morph means forms.
- Polymorphism means one interface/name can have different forms
  of behaviour.

Example:
Different animals can all have a speak() method, but each animal
speaks differently.

Dog.speak() -> Woof
Cat.speak() -> Meow
Cow.speak() -> Moo

The same method name is used, but the behaviour differs.
Method overriding is one common way to achieve polymorphism.
"""


# ============================================================
# 13. POLYMORPHISM USING METHOD OVERRIDING
# ============================================================

class AnimalSound:
    def speak(self):
        print("Animal makes a sound.")


class DogSound(AnimalSound):
    def speak(self):
        print("Woof!")


class CatSound(AnimalSound):
    def speak(self):
        print("Meow!")


class CowSound(AnimalSound):
    def speak(self):
        print("Moo!")


print("\\n13. POLYMORPHISM")
animals = [DogSound(), CatSound(), CowSound()]

for animal in animals:
    animal.speak()


# ============================================================
# 14. POLYMORPHISM WITH SHAPES AND AREA
# ============================================================

"""
Shape provides a general area() method.
Rectangle overrides area() using width * height.
Circle overrides area() using pi * radius ** 2.

The loop calls area() on each object.
The correct version runs according to the object's actual class.
"""

class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


print("\\n14. POLYMORPHISM WITH SHAPES")
shapes = [
    Rectangle(3, 4),
    Circle(5),
    Rectangle(6, 2)
]

for shape in shapes:
    print("Area:", shape.area())

"""
Expected areas:
Rectangle(3, 4) -> 12
Circle(5)       -> 78.5
Rectangle(6, 2) -> 12

One method name, area(), gives different results depending
on the object's class.
"""


# ============================================================
# 15. METHOD OVERLOADING NOTE FROM THE LESSON
# ============================================================

"""
The lesson distinguishes method overriding from method overloading.

METHOD OVERRIDING:
A child class defines a method with the same name as a parent
class method, replacing the inherited behaviour for that child.

METHOD OVERLOADING:
In languages such as Java and C++, method overloading commonly
means defining multiple methods with the same name but different
parameter lists.

Python does not support that same traditional compile-time
method-overloading mechanism by defining multiple same-name
methods in one class. A later definition replaces an earlier one.

Python code can often achieve similar flexible behaviour with
default arguments, *args, or other techniques.
"""


# ============================================================
# 16. IMPORTANT INTERVIEW QUESTIONS AND ANSWERS
# ============================================================

"""
Q1. What is inheritance?
A: Inheritance allows a child class to reuse attributes and methods
   from a parent class.

Q2. What are parent and child classes?
A: The parent class is the class whose features are inherited.
   The child class is the class that inherits those features.

Q3. Why do we use inheritance?
A: To reuse common code, reduce repetition, and model an "is-a"
   relationship.

Q4. How do we inherit a class in Python?
A: Put the parent class name in parentheses:
       class Car(Vehicle):
           pass

Q5. Can a child class access parent attributes and methods?
A: Yes, subject to normal attribute and method lookup and access
   conventions.

Q6. What is method overriding?
A: It happens when a child class defines a method with the same
   name as a method in its parent class.

Q7. What is super()?
A: super() provides access to the next class in the MRO. It is
   commonly used to call parent-class methods and initializers.

Q8. Why use super().__init__()?
A: To run the next class's initializer so the inherited part of
   the object is initialized as well.

Q9. What is single inheritance?
A: One child class inherits from one parent class.

Q10. What is multilevel inheritance?
A: A class inherits from a child/intermediate class, forming a
    chain such as Animal -> Mammal -> Dog.

Q11. What is multiple inheritance?
A: One child class inherits from more than one parent class.

Q12. What is hierarchical inheritance?
A: Multiple child classes inherit from the same parent class.

Q13. What is the diamond problem?
A: It is a method lookup ambiguity that can occur when a class
    inherits through multiple paths from a common ancestor.

Q14. What is MRO?
A: Method Resolution Order is the order Python follows when looking
    for a method or attribute in an inheritance hierarchy.

Q15. How can we check a class's MRO?
A: Use ClassName.mro() or ClassName.__mro__.

Q16. What is polymorphism?
A: Polymorphism means one interface or method name can show
    different behaviours for different object types.

Q17. How does method overriding support polymorphism?
A: Different child classes can provide their own implementations
    of the same method, and the appropriate implementation runs
    for each object.

Q18. Does Python support traditional method overloading like Java?
A: Python does not use the same traditional compile-time
    overloading mechanism. Similar flexible behaviour can be
    written using default arguments or *args.
"""


# ============================================================
# 17. QUICK REVISION
# ============================================================

"""
INHERITANCE:
- Reuse parent class features in a child class.
- Syntax: class Child(Parent):

METHOD OVERRIDING:
- Child defines a method with the same name as the parent's method.
- The child's implementation is selected for the child object.

super():
- Calls the next implementation in the MRO.
- Often used with parent methods and __init__().

TYPES:
- Single: one parent -> one child.
- Multilevel: inheritance chain.
- Multiple: one child -> multiple parents.
- Hierarchical: one parent -> multiple children.

MRO:
- Defines the method lookup order.
- Inspect with ClassName.mro().

POLYMORPHISM:
- Same method/interface, different behaviours.
- Method overriding is one common example.
"""


# ============================================================
