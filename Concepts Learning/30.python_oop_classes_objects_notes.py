"""
PYTHON OOP NOTES — CLASSES, OBJECTS, __init__, AND VARIABLES

=============================================================
1. WHAT IS OOP?
=============================================================

OOP stands for Object-Oriented Programming.

OOP is a way of thinking about and organizing code as a collection of
cooperating objects.

It helps us group related data and the functions that work on that data.

Why do we need OOP?
-------------------
Suppose we need to store details of 10 students.

Without OOP, we may create separate variables such as:
    student1_name, student1_marks
    student2_name, student2_marks
    student3_name, student3_marks

If we later need to store gender, age, address, etc., managing all these
separate variables becomes difficult.

We may also write separate functions for updating marks, calculating
averages, displaying details, and deleting students. This can lead to
repeated code and difficult maintenance.

OOP helps us group:
    1. Data  -> attributes / variables
    2. Work  -> methods / functions inside a class

Important:
OOP is a programming approach, not a Python keyword or a single syntax.

=============================================================
2. CLASS AND OBJECT
=============================================================

CLASS
-----
A class is a blueprint or template used to create objects.

Example:
A general Car blueprint may describe common features such as:
- Mirrors
- Wheels
- Windshield
- Headlights

The blueprint is the class. It is not one specific car.

OBJECT
------
An object is an actual instance created from a class.

For example:
- A red Hyundai car
- A blue Toyota car
- A black BMW car

All can be created using the same Car class, but each object can have
its own data.

Student example:
A Student class can describe these details:
- Roll number
- Name
- Gender
- Age

We can create many Student objects from one Student class.

SYNTAX:
    class Student:
        pass

    student1 = Student()
    student2 = Student()

Here:
- Student is the class.
- student1 and student2 are objects (also called instances).
- Student() creates a new object.

Naming convention:
Use PascalCase for class names:
    Student
    BankAccount
    OnlineCourse

Python may still run names such as student or bank_account as class names,
but PascalCase is the usual convention for classes.

=============================================================
3. ATTRIBUTES
=============================================================

Attributes are variables/data associated with an object or class.

Example:
    class Student:
        roll_no = 0
        name = ""
        gender = ""
        age = 0

    student1 = Student()

Access an attribute using dot notation:
    print(student1.roll_no)
    print(student1.name)
    print(student1.gender)
    print(student1.age)

Change an attribute using dot notation:
    student1.roll_no = 1
    student1.name = "Aniruddh"
    student1.gender = "Male"
    student1.age = 20

Each separately created object can have its own attribute values.

Note:
The transcript first demonstrates attributes declared directly in the
class. Later it demonstrates instance attributes created with self.

=============================================================
4. METHODS
=============================================================

A function defined inside a class is called a method.

Methods describe the actions an object can perform.

Example:
    class Student:
        def display_details(self):
            print("Student details")

    student1 = Student()
    student1.display_details()

Difference:
- Function: defined independently.
- Method: defined inside a class and normally called through an object.

Methods help us keep related data and operations together.

=============================================================
5. THE self PARAMETER
=============================================================

self refers to the current object that is calling the instance method.

Example:
    class Student:
        def display(self):
            print(self)

    student1 = Student()
    print(student1)
    student1.display()

The object that calls display() is automatically passed as self.

Therefore:
    student1.display()

works like:
    Student.display(student1)

You normally do not pass self manually when calling an instance method.

Use self to access or update the current object's attributes:
    self.name
    self.age
    self.roll_no

Example:
    class Student:
        def display_details(self):
            print(self.name)
            print(self.age)

=============================================================
6. SETTING OBJECT DETAILS USING A METHOD
=============================================================

One approach is to create a method that receives details and stores them
in the object.

Example:
    class Student:
        def set_details( self, roll_no: int, name: str, gender: str, age: int) -> None:
            self.roll_no = roll_no
            self.name = name
            self.gender = gender
            self.age = age

        def display_details(self) -> None:
            print(self.roll_no, self.name, self.gender, self.age)

    student1 = Student()
    student1.set_details(1, "Aniruddh", "Male", 20)
    student1.display_details()

The self parameter identifies which object's details should be updated.

Type annotations in this example:
- roll_no: int means an integer is expected.
- name: str means a string is expected.
- gender: str means a string is expected.
- age: int means an integer is expected.
- -> None means the method is not expected to return a value.

Type annotations are hints. Python does not enforce them automatically
at runtime by default.

=============================================================
7. WHY DO WE NEED __init__?
=============================================================

Problem with manual initialization:
If we create an object but forget to call set_details(), the object may
not have attributes such as name or roll_no.

If a method tries to access a missing attribute, Python can raise:
    AttributeError

Example:
    class Student:
        def display(self):
            print(self.name)

    student1 = Student()
    student1.display()

This raises AttributeError because name was never created for student1.

Solution: use __init__.

=============================================================
8. THE __init__() METHOD
=============================================================

__init__ is a special method that Python calls automatically when a new
object is initialized.

It is commonly called the constructor in beginner-level explanations.
More precisely, __init__ is the initializer; __new__ is responsible for
creating the object.

Syntax:
    class Student:
        def __init__(self):
            self.name = ""
            self.age = 0

    student1 = Student()

When Student() is called, Python automatically calls __init__ for the
new object. You do not call __init__ yourself in normal usage.

Passing values during object creation:
    class Student:
        def __init__(
            self,
            roll_no: int,
            name: str,
            gender: str,
            age: int
        ) -> None:
            self.roll_no = roll_no
            self.name = name
            self.gender = gender
            self.age = age

    student1 = Student(1, "Aniruddh", "Male", 20)

Now the object's attributes are initialized at the time the object is
created. There is no separate set_details() call required.

Important points:
- The method name must be exactly __init__ (two underscores on each side).
- self refers to the newly initialized object.
- __init__ normally returns None; do not return another value from it.
- Parameters after self receive the values supplied when creating the object.

=============================================================
9. COMPLETE STUDENT CLASS — TOTAL, AVERAGE, AND GRADE
=============================================================

The transcript builds a Student class with:
- name: string
- age: integer
- marks: list of integers

Methods:
- total_marks() calculates the sum of marks.
- average_marks() calculates the average.
- display_grade() displays a grade based on the average.

Example:
    class Student:
        def __init__(
            self,
            name: str,
            age: int,
            marks: list[int]
        ) -> None:
            self.name = name
            self.age = age
            self.marks = marks

        def total_marks(self) -> int:
            return sum(self.marks)

        def average_marks(self) -> float:
            return self.total_marks() / len(self.marks)

        def display_grade(self) -> None:
            average = self.average_marks()

            if average >= 90:
                print("Grade A")
            elif average >= 50:
                print("Grade B")
            else:
                print("Grade C")


    student1 = Student("Aniruddh", 20, [78, 54, 19, 63])

    print("Total:", student1.total_marks())
    print("Average:", student1.average_marks())
    student1.display_grade()

Expected calculation:
    Total = 78 + 54 + 19 + 63 = 214
    Average = 214 / 4 = 53.5
    Grade = B

The transcript's spoken average sounds like 53.4, but the arithmetic
for the listed marks gives 53.5.

The grade conditions shown in the transcript are:
- Average >= 90       -> Grade A
- Average from 50 to 89 -> Grade B
- Otherwise           -> Grade C

=============================================================
10. LOCAL VARIABLE VS INSTANCE ATTRIBUTE
=============================================================

A local variable is created inside a method and is normally available
only within that method.

Example:
    def average_marks(self) -> float:
        average = sum(self.marks) / len(self.marks)
        return average

Here, average is a local variable.

An instance attribute is stored on the object using self.

Example:
    self.name = name
    self.age = age

Difference:
- average: local to the method call.
- self.name: belongs to the object and can be accessed by its methods.

If you want a value to be stored as part of the object, use self:
    self.average = ...

If you only need a temporary value inside one method, a local variable
is usually enough:
    average = ...

=============================================================
11. CALLING ONE METHOD FROM ANOTHER METHOD
=============================================================

When one instance method calls another instance method of the same
object, use self.method_name().

Example:
    class Student:
        def __init__(self, marks: list[int]) -> None:
            self.marks = marks

        def total_marks(self) -> int:
            return sum(self.marks)

        def average_marks(self) -> float:
            return self.total_marks() / len(self.marks)

        def display_grade(self) -> None:
            average = self.average_marks()

            if average >= 90:
                print("Grade A")
            elif average >= 50:
                print("Grade B")
            else:
                print("Grade C")

Why self.average_marks()?
Because it calls average_marks() for the same object that called
display_grade().

Outside the class, call a method through the object:
    student1.average_marks()

Inside another instance method, use:
    self.average_marks()

=============================================================
12. INSTANCE VARIABLES
=============================================================

An instance variable belongs to a particular object.

It is commonly created using self inside __init__.

Example:
    class Student:
        def __init__(self, name: str) -> None:
            self.name = name

    student1 = Student("Aniruddh")
    student2 = Student("Priya")

    print(student1.name)  # Aniruddh
    print(student2.name)  # Priya

Here:
- student1.name belongs to student1.
- student2.name belongs to student2.

Each object has its own instance value. Changing one object's name
does not automatically change the other object's name.

Use instance variables for data that can be different for every object:
- Student name
- Student roll number
- Student marks
- Employee salary
- Employee ID

=============================================================
13. CLASS VARIABLES
=============================================================

A class variable is defined directly inside the class, outside methods.

It is shared as a common class-level value and can be accessed through
the class name or through an instance (when no instance attribute with
the same name shadows it).

Example:
    class Student:
        school = "SG Jain Modern School"  # Class variable

        def __init__(self, name: str) -> None:
            self.name = name              # Instance variable

    student1 = Student("Aniruddh")
    student2 = Student("Priya")

    print(student1.school)
    print(student2.school)
    print(Student.school)

All three accesses find the class variable's value.

Changing the class variable:
    Student.school = "XYZ School"

Now objects that do not have their own school attribute will read
"XYZ School" from the class.

Use class variables for values common to all objects:
- School name shared by students
- Company name shared by employees
- A common organization address
- A shared configuration value

=============================================================
14. INSTANCE VARIABLE VS CLASS VARIABLE
=============================================================

INSTANCE VARIABLE:
- Belongs to an individual object.
- Usually created with self inside __init__ or another method.
- Each object can have a different value.
- Changing one object's instance variable does not change other objects.

CLASS VARIABLE:
- Defined in the class body, outside instance methods.
- Shared at the class level.
- Useful for values common to all objects.
- Normally update it through the class name.

Example:
    class Student:
        school = "SG Jain Modern School"

        def __init__(self, name: str) -> None:
            self.name = name

    s1 = Student("Aniruddh")
    s2 = Student("Priya")

    s1.name = "Aniruddh D"
    print(s1.name)       # Aniruddh D
    print(s2.name)       # Priya

    Student.school = "XYZ School"
    print(s1.school)     # XYZ School
    print(s2.school)     # XYZ School

=============================================================
15. IMPORTANT: s1.school = ... IS NOT THE SAME AS
    Student.school = ...
=============================================================

This is an important detail from the transcript.

When you write:
    s1.school = "ABC School"

Python creates or updates an instance attribute named school on s1.
It does not change the class variable Student.school.

Example:
    class Student:
        school = "SG Jain Modern School"

    s1 = Student()
    s2 = Student()

    s1.school = "XYZ School"

    print(s1.school)       # XYZ School
    print(s2.school)       # SG Jain Modern School
    print(Student.school)  # SG Jain Modern School

Why?
When reading s1.school, Python first checks s1 for an instance
attribute named school. It finds one, so that value is used.
For s2.school, no instance attribute exists, so Python finds the
class variable Student.school.

To change the shared class variable, use:
    Student.school = "XYZ School"

To access the class variable, you can use:
    Student.school
    s1.school
    s2.school

But accessing through an object does not mean assignment through that
object changes the class variable.

=============================================================
16. QUICK REVISION
=============================================================

OOP:
    A way to organize programs around objects.

Class:
    A blueprint for creating objects.

Object / Instance:
    An actual object created from a class.

Attribute:
    Data or a variable associated with an object or class.

Method:
    A function defined inside a class.

self:
    Refers to the current object in an instance method.

__init__:
    Special initializer called automatically when an object is initialized.

Instance variable:
    A variable belonging to one particular object, commonly self.name.

Class variable:
    A variable defined in the class body and shared at class level.

Local variable:
    A temporary variable created inside a function or method.

Type annotation:
    A hint describing the expected type, e.g. name: str or -> int.

=============================================================
17. INTERVIEW QUESTIONS — SHORT ANSWERS
=============================================================

Q1. What is OOP?
A. OOP is a programming approach that organizes code around objects
   containing data and methods.

Q2. What is a class?
A. A class is a blueprint or template used to create objects.

Q3. What is an object?
A. An object is an instance of a class.

Q4. What is a method?
A. A method is a function defined inside a class.

Q5. What is self in Python?
A. self refers to the current object calling an instance method.

Q6. What is __init__?
A. __init__ is a special initializer that Python calls automatically
   when an object is initialized.

Q7. What happens if an attribute is not created?
A. Accessing a missing attribute can raise AttributeError.

Q8. What is an instance variable?
A. A variable associated with a particular object. Different objects
   can have different values.

Q9. What is a class variable?
A. A variable defined in the class body and shared at class level.

Q10. How do you change a class variable?
A. Assign through the class name, for example Student.school = "XYZ".

Q11. What is the difference between a local variable and an instance
    variable?
A. A local variable is used within a method, while an instance variable
   is stored on an object using self.

Q12. How do you call one method from another method in the same object?
A. Use self.method_name().

=============================================================
18. PRACTICE TASKS
=============================================================

1. Create a Car class with brand, model, and year attributes.
2. Create three Car objects with different details.
3. Create an Employee class using __init__ with name, employee_id,
   and salary.
4. Add a method to display employee details.
5. Create a Student class with name, age, and a list of marks.
6. Add methods to calculate total marks, average marks, and grade.
7. Add a class variable school and create two Student objects.
8. Change one student's name and check whether the other student's
   name changes.
9. Change Student.school and check the value through both objects.
10. Assign s1.school to a new value and compare s1.school, s2.school,
    and Student.school.

END OF NOTES
============
"""
