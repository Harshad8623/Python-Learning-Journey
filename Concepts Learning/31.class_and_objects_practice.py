# Step 1

class Student:
    # Attributes
    roll_no = 0
    name = ''
    gender = ''
    age = 0

# Objects / Instances
xyz = Student()
pqr = Student()
print(xyz)          # it prints .....
print(Student)      # it prints .....
print(Student.name)
print(Student.age)
xyz.name = 'Harshad'
xyz.age = 21
print(Student.name)
print(Student.age)
print(xyz.name)
print(xyz.age)
print(pqr.name)
print(pqr.age)



# Step 2


class Student:
    # Attributes
    roll_no = 0
    name = ''
    gender = ''
    age = 0

    def display_details(self):
        print(self)


# Objects / Instances
xyz = Student()
pqr = Student()
print(xyz)
print(xyz.display_details())



# Step 3

class Student:
    roll_no = 0
    name = ''
    gender = ''
    age = 0

    def display_details(self):
        print(self.name)
        print(self.roll_no)
        print(self.gender)
        print(self.age)



xyz = Student()
pqr = Student()
xyz.name = "harshad"
xyz.age = 21
xyz.gender = "Male"
xyz.roll_no = 45
print(xyz.display_details())
print("--------------------")
print(pqr.display_details())



# Step 4

class Student:

    def set_details(self, name, age, gender, roll_no):
        self.name = name
        self.age = age
        self.gender = gender
        self.roll_no = roll_no

    def display_details(self):
        print(self.name)
        print(self.roll_no)
        print(self.gender)
        print(self.age)



xyz = Student()
pqr = Student()
xyz.set_details("harshad", 21, "male", 45)
print(xyz.display_details())





# Step 5

class Student:

    def set_details(self, name, age, gender, roll_no):
        self.name = name
        self.age = age
        self.gender = gender
        self.roll_no = roll_no

    def display_details(self):
        print(self.name)
        print(self.roll_no)
        print(self.gender)
        print(self.age)



xyz = Student()
pqr = Student()
# xyz.set_details("harshad", 21, "male", 45)
# print(xyz.display_details())

# This produces Attribute error



# Step 6

class Student:

    def __init__(self, name, age, gender, roll_no):
        self.name = name
        self.age = age
        self.gender = gender
        self.roll_no = roll_no


    def display_details(self):
        print(self.name)
        print(self.roll_no)
        print(self.gender)
        print(self.age)



xyz = Student("harshad", 21, "male", 45)

print(xyz.display_details())


# PYTHON OOP — UPDATED ADVANCED NOTES
# Based on your six-step Student class practice.
#
# Topics: class, object, attributes, methods, self, __init__, AttributeError,
# instance variables, class variables, attribute shadowing, type annotations,
# local variables, return values, interview questions and practice tasks.
#
# Run this file to execute the examples. Each section is independent.


# ============================================================
# STEP 1 — CLASS AND OBJECT
# ============================================================
# A class is a blueprint. An object (instance) is created from a class.

class Student:
    # Class attributes: defined directly inside the class.
    roll_no = 0
    name = ""
    gender = ""
    age = 0


xyz = Student()
pqr = Student()

print("\nSTEP 1 — CLASS AND OBJECT")
print("xyz object:", xyz)       # Usually shows class name and object address
print("Student class:", Student)
print("Student.name:", Student.name)
print("Student.age:", Student.age)

# Assignment through an object creates instance attributes.
xyz.name = "Harshad"
xyz.age = 21

print("Student.name:", Student.name)  # "" — class attribute unchanged
print("Student.age:", Student.age)    # 0 — class attribute unchanged
print("xyz.name:", xyz.name)          # Harshad
print("xyz.age:", xyz.age)             # 21
print("pqr.name:", pqr.name)           # "" — found on the class
print("pqr.age:", pqr.age)             # 0 — found on the class


# IMPORTANT: ATTRIBUTE LOOKUP AND SHADOWING
# When Python evaluates xyz.name, it first checks xyz.
# If name is not on xyz, Python looks on the Student class.
# xyz.name = "Harshad" creates an instance attribute; it does not
# change Student.name. The instance attribute shadows the class attribute.


# ============================================================
# STEP 2 — self AND INSTANCE METHODS
# ============================================================
# A function defined inside a class is called a method.
# self refers to the current object calling the instance method.
#
# xyz.display_details() is conceptually equivalent to:
# Student.display_details(xyz)
#
# Python passes the object as self automatically. Do not pass self manually.

class Student:
    def display_details(self):
        print("Current object inside method:", self)


xyz = Student()
print("\nSTEP 2 — SELF")
print("Object outside method:", xyz)
xyz.display_details()


# IMPORTANT: print(xyz.display_details()) prints None after the method output
# if the method has no return statement. A function with no explicit return
# returns None. Prefer xyz.display_details() when the method prints itself.


# ============================================================
# STEP 3 — ACCESSING ATTRIBUTES USING self
# ============================================================

class Student:
    roll_no = 0
    name = ""
    gender = ""
    age = 0

    def display_details(self):
        print("Name:", self.name)
        print("Roll number:", self.roll_no)
        print("Gender:", self.gender)
        print("Age:", self.age)


xyz = Student()
pqr = Student()

xyz.name = "Harshad"
xyz.age = 21
xyz.gender = "Male"
xyz.roll_no = 45

print("\nSTEP 3 — DISPLAY DETAILS")
xyz.display_details()
print("--------------------")
pqr.display_details()  # pqr reads the class attribute values


# ============================================================
# STEP 4 — SETTING DETAILS USING A METHOD
# ============================================================

class Student:
    def set_details(self, name: str, age: int,
                    gender: str, roll_no: int) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.roll_no = roll_no

    def display_details(self) -> None:
        print("Name:", self.name)
        print("Roll number:", self.roll_no)
        print("Gender:", self.gender)
        print("Age:", self.age)


xyz = Student()
xyz.set_details("Harshad", 21, "Male", 45)
print("\nSTEP 4 — SET_DETAILS")
xyz.display_details()


# ============================================================
# STEP 5 — UNDERSTANDING AttributeError
# ============================================================
# If the class has no name attribute and we never assign xyz.name,
# then xyz.name raises AttributeError.
#
# Example (intentionally commented):
#
# class Student:
#     def display_details(self):
#         print(self.name)
#
# xyz = Student()
# xyz.display_details()
#
# Error:
# AttributeError: 'Student' object has no attribute 'name'
#
# This happens because name was never initialized or assigned.


# ============================================================
# STEP 6 — __init__() INITIALIZER
# ============================================================
# __init__() is called automatically when an object is initialized.
# It is commonly called the constructor in beginner explanations.
# More precisely: __new__ creates the object; __init__ initializes it.
#
# __init__ normally returns None. Do not return another value from it.

class Student:
    def __init__(self, name: str, age: int,
                 gender: str, roll_no: int) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.roll_no = roll_no

    def display_details(self) -> None:
        print("Name:", self.name)
        print("Roll number:", self.roll_no)
        print("Gender:", self.gender)
        print("Age:", self.age)


xyz = Student("Harshad", 21, "Male", 45)
print("\nSTEP 6 — __init__")
xyz.display_details()

# Required values are passed when creating the object.
# Python calls __init__ automatically; normally do not call it directly.


# ============================================================
# STEP 7 — MULTIPLE OBJECTS HAVE THEIR OWN INSTANCE DATA
# ============================================================

class Student:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def display_details(self) -> None:
        print(f"Name: {self.name}, Age: {self.age}")


xyz = Student("Harshad", 21)
pqr = Student("Aniruddh", 20)

print("\nSTEP 7 — MULTIPLE OBJECTS")
xyz.display_details()
pqr.display_details()

xyz.name = "Harshad Dhuppe"
print("After changing xyz:")
xyz.display_details()
pqr.display_details()  # pqr remains unchanged


# ============================================================
# STEP 8 — CLASS VARIABLES VS INSTANCE VARIABLES
# ============================================================
# Instance variable: belongs to one object; commonly created using self.
# Class variable: defined in the class body; shared at class level.

class Student:
    school = "ABC School"  # Class variable

    def __init__(self, name: str, age: int) -> None:
        self.name = name  # Instance variable
        self.age = age    # Instance variable


xyz = Student("Harshad", 21)
pqr = Student("Aniruddh", 20)

print("\nSTEP 8 — CLASS VS INSTANCE VARIABLES")
print("xyz.name:", xyz.name)
print("pqr.name:", pqr.name)
print("Student.school:", Student.school)
print("xyz.school:", xyz.school)
print("pqr.school:", pqr.school)


# ============================================================
# STEP 9 — ASSIGNING THROUGH AN OBJECT VS THROUGH THE CLASS
# ============================================================
# xyz.school = "XYZ" creates/updates an instance attribute on xyz.
# Student.school = "XYZ" updates the shared class variable.

class Student:
    school = "ABC School"


xyz = Student()
pqr = Student()

print("\nSTEP 9 — ATTRIBUTE SHADOWING")
xyz.school = "XYZ School"

print("xyz.school:", xyz.school)          # XYZ School
print("pqr.school:", pqr.school)          # ABC School
print("Student.school:", Student.school)  # ABC School

Student.school = "New Common School"

print("After changing Student.school:")
print("xyz.school:", xyz.school)          # XYZ School: instance value shadows it
print("pqr.school:", pqr.school)          # New Common School
print("Student.school:", Student.school)


# ============================================================
# STEP 10 — COMPLETE STUDENT CLASS: TOTAL, AVERAGE AND GRADE
# ============================================================

class Student:
    school = "ABC School"  # Class variable

    def __init__(self, name: str, age: int,
                 roll_no: int, marks: list[int]) -> None:
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self) -> None:
        print("\n--- Student Details ---")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll number:", self.roll_no)
        print("Marks:", self.marks)
        print("School:", self.school)

    def total_marks(self) -> int:
        return sum(self.marks)

    def average_marks(self) -> float:
        if len(self.marks) == 0:
            return 0.0
        return self.total_marks() / len(self.marks)

    def display_grade(self) -> None:
        # Calling another method of the same object using self.
        average = self.average_marks()

        if average >= 90:
            grade = "A"
        elif average >= 50:
            grade = "B"
        else:
            grade = "C"

        print("Grade:", grade)


student1 = Student("Harshad", 21, 45, [78, 54, 19, 63])

print("\nSTEP 10 — COMPLETE STUDENT CLASS")
student1.display_details()
print("Total marks:", student1.total_marks())
print("Average marks:", student1.average_marks())
student1.display_grade()

# Calculation: 78 + 54 + 19 + 63 = 214
# Average: 214 / 4 = 53.5


# ============================================================
# STEP 11 — LOCAL VARIABLE VS INSTANCE ATTRIBUTE
# ============================================================
# In average_marks(), the variable average is local to that method.
# self.marks is an instance attribute stored on the object.
#
# Use a local variable for a temporary calculation.
# Use self.variable_name when the value should be stored on the object.


# ============================================================
# QUICK REVISION
# ============================================================
# CLASS: blueprint/template used to create objects.
# OBJECT / INSTANCE: an actual object created from a class.
# ATTRIBUTE: data associated with an object or class.
# METHOD: a function defined inside a class.
# self: current object in an instance method.
# __init__(): initializer automatically called during object initialization.
# INSTANCE VARIABLE: object-specific data, commonly written as self.name.
# CLASS VARIABLE: variable defined in the class body.
# LOCAL VARIABLE: temporary variable inside a function or method.
# AttributeError: accessing an attribute that cannot be found.
# TYPE ANNOTATION: hint about expected type, e.g. name: str or -> int.
# Python does not enforce ordinary type annotations at runtime by default.


# ============================================================
# COMMON MISTAKES
# ============================================================
# 1. print(xyz.display_details()) may print None after method output.
#    Better: xyz.display_details()
#
# 2. An instance method needs self as its first parameter.
#
# 3. Student.school = "XYZ" and xyz.school = "XYZ" are not equivalent.
#
# 4. An object does not automatically have every attribute.
#    Initialize required attributes in __init__().
#
# 5. Create objects using Student(...). Python calls __init__() for you.


# ============================================================
# INTERVIEW QUESTIONS
# ============================================================
# 1. What is OOP?
# 2. Difference between a class and an object?
# 3. What is an instance?
# 4. What are attributes?
# 5. What is a method?
# 6. What is self?
# 7. Does Python pass self automatically?
# 8. What is __init__()?
# 9. Is __init__() called automatically?
# 10. What happens if an object does not have an attribute?
# 11. What is AttributeError?
# 12. What is an instance variable?
# 13. What is a class variable?
# 14. Difference between class and instance variables?
# 15. What happens when you assign xyz.school = "XYZ"?
# 16. How do you update a shared class variable?
# 17. What is a local variable?
# 18. What does -> None mean?
# 19. Why can print(method_call()) display None?
# 20. How can one method call another method of the same object?


# ============================================================
# PRACTICE TASKS
# ============================================================
# TASK 1: Create a Car class with brand, model and year. Create two objects.
# TASK 2: Create an Employee class with name, employee_id and salary.
# TASK 3: Add a display_details() method to Employee.
# TASK 4: Create a Student class with a list of marks; calculate total/average.
# TASK 5: Add a class variable school and create two Student objects.
# TASK 6: Change one student's name. Does the other student's name change?
# TASK 7: Assign s1.school to a new value. Print s1.school, s2.school,
#         and Student.school. Explain the output.
# TASK 8: Change Student.school through the class name.
# TASK 9: Access an uninitialized attribute and observe AttributeError.
# TASK 10: Write display_grade() that calls self.average_marks().
