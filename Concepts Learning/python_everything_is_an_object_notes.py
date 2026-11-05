# PYTHON OBJECT MODEL: EVERYTHING IS AN OBJECT
# =============================================
#
# Beginner-friendly notes, runnable examples, and interview Q&A.
#
# CORE IDEA
# ---------
# Python follows an object model. Values and runtime entities such as integers,
# strings, lists, functions, classes, and modules are objects.
#
# An object has:
# 1. Identity: identifies a particular object during its lifetime.
# 2. Type: tells us what kind of object it is and what operations it supports.
# 3. Value/state: the data represented by the object.
#
# A variable is a NAME that refers to an object. It is not the object itself.
#
# Run: python python_everything_is_an_object_notes.py

print("=" * 60)
print("1. VARIABLES REFER TO OBJECTS")

age = 21
name = "Python"
marks = [80, 90, 95]
print(age, type(age))
print(name, type(name))
print(marks, type(marks))

# Two names can refer to the same object.
first = [1, 2, 3]
second = first
print(first is second)      # True
second.append(4)
print(first)                # [1, 2, 3, 4]


print("\n2. FUNCTIONS ARE OBJECTS")

def area(length, width):
    return length * width

print(type(area))           # <class 'function'>
print(callable(area))       # True
calculate_area = area
print(calculate_area(5, 4)) # 20

def run_function(function):
    return function(3, 2)

print(run_function(area))   # 6


print("\n3. CLASSES ARE ALSO OBJECTS")

class Student:
    def __init__(self, student_name):
        self.student_name = student_name

student1 = Student("Aarav")
print(type(Student))        # <class 'type'>
print(type(student1))       # <class '__main__.Student'>
print(student1.student_name)

# Student is a class object. student1 is an instance of Student.
# The class itself is an object; its type is usually 'type'.


print("\n4. BUILT-IN FUNCTIONS AND TYPES ARE OBJECTS")

print(type(print))          # Usually <class 'builtin_function_or_method'>
print(type(len))            # Usually <class 'builtin_function_or_method'>
print(type(int))            # <class 'type'>
print(type(list))            # <class 'type'>
print(type(type))            # <class 'type'>
print(callable(print))      # True
print(callable(int))        # True


print("\n5. MODULES ARE OBJECTS")

import math
print(type(math))           # <class 'module'>
print(math.sqrt(25))        # 5.0


print("\n6. WHAT EXACTLY DOES type() DO?")

number = 100
word = "Hello"
number_type = type(number)
word_type = type(word)

print(number_type)              # <class 'int'>
print(word_type)                # <class 'str'>
print(number_type is int)       # True
print(word_type is str)         # True

# IMPORTANT:
# - type is itself a built-in class and metaclass.
# - type(10) returns the class object int.
# - int is a class object, and classes are objects too.
# - type(10) does not return a new integer instance.

print(type(type))               # <class 'type'>
print(type(10) is int)          # True
print(type("hi") is str)        # True


print("\n7. type() VERSUS isinstance()")

class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()
print(type(dog) is Dog)         # True
print(type(dog) is Animal)      # False: exact type is Dog
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True: Dog inherits from Animal

# Use isinstance() for inheritance-aware checks.
# Use type() when you specifically need the exact type.


print("\n8. EXAMPLES: MANY KINDS OF OBJECTS")

examples = [
    42, 3.14, True, "Python", [1, 2], (1, 2),
    {"name": "Aarav"}, {1, 2, 3}, None,
    area, Student, student1, math
]
for item in examples:
    print(repr(item), "->", type(item))


print("\n9. IMPORTANT CLARIFICATIONS")

# 1. A function object is created when the def statement executes.
#    Calling it runs the function; it does not create another function object.
#
# 2. Calling a class, for example Student("Aarav"), normally creates an
#    instance of that class.
#
# 3. print is an existing built-in function object. Calling print() executes
#    it; it does not create a new print function object.
#
# 4. Assigning a variable binds a name to an object. It does not always create
#    a new object. Multiple names can refer to the same object.
#
# 5. Objects can be mutable (like lists) or immutable (like integers/strings).
#
# 6. "Everything is an object" is a useful summary of Python's object model.
#    Variable names and syntax keywords are not themselves ordinary objects.


print("\n10. INTERVIEW QUESTIONS AND ANSWERS")

qa = [
    ("Q1. Is everything an object in Python?",
     "Almost all values and important runtime entities are objects. Examples "
     "include integers, strings, lists, functions, classes and modules. "
     "Objects have identity, type and value/state."),
    ("Q2. What is an object in Python?",
     "An object is a runtime entity with an identity, a type and a value. "
     "For example, 10 is an integer object and 'Python' is a string object."),
    ("Q3. Are variables objects in Python?",
     "A variable name is a name bound to an object. In x = 10, x refers to "
     "the integer object 10. The name x is not the integer object."),
    ("Q4. Are functions objects?",
     "Yes. A function created with def is a function object. It can be assigned "
     "to another variable, passed as an argument, and returned from a function."),
    ("Q5. Are classes objects?",
     "Yes. A class is also an object. A normal user-defined class usually has "
     "'type' as its type. An instance created from it has that class as its type."),
    ("Q6. Is print() an object?",
     "print is a built-in function object. Calling print() executes that "
     "existing function; it does not create a new print function each time."),
    ("Q7. What does type() return?",
     "type(object) returns the exact type/class of the object. For example, "
     "type(10) returns int, which is the int class object."),
    ("Q8. Is type itself an object? Is it a class?",
     "Yes. The name type refers to a built-in class and metaclass. It is also "
     "an object. type(type) returns type. Calling type(10) returns int, the "
     "class object for integers."),
    ("Q9. Does type(10) return an object or a class?",
     "It returns a class object: int. Classes are objects too, so the returned "
     "class is itself an object."),
    ("Q10. Difference between type() and isinstance()?",
     "type(obj) identifies the exact type. isinstance(obj, Class) checks "
     "whether obj is an instance of that class or one of its subclasses. "
     "Prefer isinstance() for inheritance-aware checks."),
    ("Q11. Why does isinstance(True, int) return True?",
     "bool is a subclass of int in Python. The exact type of True is bool, "
     "but a bool object is also an instance of int."),
    ("Q12. Difference between a class and an object?",
     "A class is a type used to create instances. An object is a runtime "
     "instance or value. In Python, the class itself is also an object.")
]

for question, answer in qa:
    print("\n" + question)
    print("Answer:", answer)


print("\n11. QUICK REVISION")
print("type(10)       ->", type(10))
print('type("Hello")  ->', type("Hello"))
print("type([])       ->", type([]))
print("type(area)     ->", type(area))
print("type(Student)  ->", type(Student))
print("type(student1) ->", type(student1))
print("type(type)     ->", type(type))

# GOLDEN INTERVIEW ANSWER:
# "Python follows an object model. Values such as numbers, strings,
# collections, functions, classes and modules are objects. Each object
# has an identity, a type and a value. Variable names refer to objects."
#
# MOST IMPORTANT:
# - type(obj) returns the exact class object of obj.
# - type itself is also a class object (a metaclass).
# - isinstance(obj, SomeClass) also checks inheritance relationships.
