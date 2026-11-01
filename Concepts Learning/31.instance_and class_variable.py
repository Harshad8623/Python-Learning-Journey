# ============================================================
# 1. INSTANCE VARIABLES
# ============================================================

"""
Instance variables belong to a particular object.
Each object can have its own separate values.
They are commonly created using self inside __init__().
"""

class Student:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable


student1 = Student("Harshad", 21)
student2 = Student("Rahul", 22)

print("1. INSTANCE VARIABLES")
print(student1.name)  # Harshad
print(student2.name)  # Rahul
print(student1.age)   # 21
print(student2.age)   # 22


# ============================================================
# 2. CLASS VARIABLES
# ============================================================

"""
Class variables belong to the class itself.
They are shared by all objects of that class by default.
They are declared directly inside the class, outside methods.
"""

class CollegeStudent:
    college = "CSMSS College"  # Class variable

    def __init__(self, name):
        self.name = name       # Instance variable


student1 = CollegeStudent("Harshad")
student2 = CollegeStudent("Rahul")

print("\n2. CLASS VARIABLES")
print(student1.college)        # CSMSS College
print(student2.college)        # CSMSS College
print(CollegeStudent.college)  # CSMSS College


# ============================================================
# 3. CHANGING A CLASS VARIABLE
# ============================================================

"""
Change the class variable using the class name.
Objects without their own instance variable of the same name
will see the updated class value.
"""

class College:
    name = "CSMSS College"


s1 = College()
s2 = College()

College.name = "COEP"

print("\n3. CHANGING A CLASS VARIABLE")
print(s1.name)       # COEP
print(s2.name)       # COEP
print(College.name)  # COEP


# ============================================================
# 4. INSTANCE VARIABLE SHADOWING A CLASS VARIABLE
# ============================================================

"""
Assigning object.variable_name creates an instance variable
for that object. It takes priority for that object's lookup.
The class variable remains unchanged.

This is called attribute shadowing.
"""

class StudentCollege:
    college = "CSMSS College"


s1 = StudentCollege()
s2 = StudentCollege()

s1.college = "IIT Bombay"

print("\n4. INSTANCE VARIABLE SHADOWING")
print(s1.college)             # IIT Bombay
print(s2.college)             # CSMSS College
print(StudentCollege.college) # CSMSS College


# ============================================================
# 5. STATIC VARIABLES IN PYTHON
# ============================================================

"""
In Python, 'static variable' commonly refers to a class variable.
Python has no separate 'static' keyword for declaring class
variables, unlike Java or C++.
"""

class Employee:
    company = "Google"  # Class variable (sometimes called static variable)

    def __init__(self, name):
        self.name = name  # Instance variable


emp1 = Employee("Amit")
emp2 = Employee("Rahul")

print("\n5. STATIC / CLASS VARIABLE")
print(emp1.company)  # Google
print(emp2.company)  # Google


# ============================================================
# 6. DIFFERENCE BETWEEN INSTANCE AND CLASS VARIABLES
# ============================================================

"""
INSTANCE VARIABLE:
- Belongs to an individual object.
- Each object can store a different value.
- Commonly declared using self.variable_name.
- Example: self.name, self.age.

CLASS VARIABLE:
- Belongs to the class.
- Shared by objects unless an object has its own attribute
  with the same name.
- Declared directly inside the class, outside methods.
- Example: college, company.
"""

print("\n6. QUICK COMPARISON")
print("Instance variable: separate data for each object.")
print("Class variable: shared class-level data by default.")


# ============================================================
# 7. REAL-WORLD STUDENT EXAMPLE
# ============================================================

"""
college and total_students are class variables.
name and roll_no are instance variables.
total_students increases whenever a StudentRecord is created.
"""

class StudentRecord:
    college = "CSMSS College"
    total_students = 0

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        StudentRecord.total_students += 1

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("College:", StudentRecord.college)


record1 = StudentRecord("Harshad", 101)
record2 = StudentRecord("Rahul", 102)

print("\n7. REAL-WORLD STUDENT EXAMPLE")
record1.display()
print()
record2.display()
print("Total Students:", StudentRecord.total_students)  # 2


# ============================================================
# 8. PRACTICE QUESTION
# ============================================================

"""
Predict the output:

class Demo:
    value = "Class Value"

obj1 = Demo()
obj2 = Demo()

obj1.value = "Object 1 Value"

print(obj1.value)
print(obj2.value)
print(Demo.value)

Expected output:
Object 1 Value
Class Value
Class Value

Reason:
obj1.value creates an instance variable only for obj1.
obj2 and Demo still access the class variable.
"""


# ============================================================
# 9. IMPORTANT INTERVIEW POINTS
# ============================================================

"""
1. Instance variables belong to objects.
2. Class variables belong to the class.
3. Class variables are shared by objects by default.
4. Use ClassName.variable_name to update a class variable
   for the whole class.
5. Assigning obj.variable_name creates or updates an instance
   variable; it does not update the class variable.
6. Python has no separate 'static' keyword for class variables.
7. An instance attribute can shadow a class attribute.
"""


# ===========================================================