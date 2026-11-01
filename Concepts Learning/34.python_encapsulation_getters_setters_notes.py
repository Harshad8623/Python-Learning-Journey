"""

Topics:
1. Encapsulation
2. Public, protected, and private-style attributes
3. Name mangling
4. Bank account example
5. Traditional getters and setters
6. @property getter and setter
7. Interview questions and practice tasks



Important:
Python's double underscore does not provide absolute security.
It triggers name mangling, which discourages accidental access.
"""


# ============================================================
# 1. ENCAPSULATION
# ============================================================

"""
Encapsulation is one of the four main pillars of OOP.

It means combining data (attributes) and methods that work on
that data inside a class, while controlling how the data is
accessed or modified.

It is commonly described as data hiding and controlled access.

Example: A bank account stores a balance. A user should deposit,
withdraw, or check the balance through methods instead of changing
the balance directly to any value.
"""


# ============================================================
# 2. PUBLIC ATTRIBUTES
# ============================================================

"""
Public attributes:
- Accessible inside and outside the class.
- Default in Python.
- No special underscore is needed.
"""

class PublicStudent:
    def __init__(self, name, age):
        self.name = name  # Public
        self.age = age    # Public


student = PublicStudent("Aniruddh", 21)

print("1. PUBLIC ATTRIBUTES")
print(student.name)
print(student.age)

student.age = 100  # Direct update is allowed
print("Updated age:", student.age)


# ============================================================
# 3. PROTECTED ATTRIBUTES
# ============================================================

"""
Protected-style attributes start with one underscore:
    self._balance

This is a convention telling other developers that the
attribute is intended for internal use.

Python still allows direct access from outside the class.
A single underscore does NOT technically block access.
"""

class ProtectedAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance


account = ProtectedAccount("Aniruddh", 1000)

print("\\n2. PROTECTED ATTRIBUTES")
print(account.owner)
print(account._balance)  # Works, but direct access is discouraged.


# ============================================================
# 4. PRIVATE-STYLE ATTRIBUTES AND NAME MANGLING
# ============================================================

"""
Private-style attributes start with two underscores:
    self.__balance

Python applies name mangling. In a class named Bank, __balance
is internally renamed to _Bank__balance.

So account.__balance normally raises AttributeError.
However, account._Bank__balance can still access the value.

Therefore, double underscore is not strict security.
"""

class PrivateStudent:
    def __init__(self, name):
        self.__name = name


private_student = PrivateStudent("Aniruddh")

print("\\n3. PRIVATE-STYLE ATTRIBUTE")
try:
    print(private_student.__name)
except AttributeError:
    print("Direct access to __name is not available.")

print("Mangled name:", private_student._PrivateStudent__name)


# ============================================================
# 5. BANK ACCOUNT WITH A PRIVATE BALANCE
# ============================================================

"""
The balance is stored in __balance.
The user interacts with it through methods such as deposit()
and get_balance(). The deposit method validates the amount.
"""

class Bank:
    def __init__(self, name: str, balance: int):
        self.name = name
        self.__balance = balance

    def deposit(self, amount: int):
        if amount <= 0:
            print("Invalid amount. Deposit must be positive.")
        else:
            self.__balance += amount
            print("Deposit successful.")

    def get_balance(self):
        return self.__balance


b1 = Bank("Aniruddh", 1000)

print("\\n4. BANK ACCOUNT")
print("Account holder:", b1.name)
print("Initial balance:", b1.get_balance())

b1.deposit(500)
print("Balance after deposit:", b1.get_balance())

b1.deposit(-1000)
print("Balance after invalid deposit:", b1.get_balance())


# ============================================================
# 6. TRADITIONAL GETTERS AND SETTERS
# ============================================================

"""
Getter:
A method that reads/returns an attribute's value.

Setter:
A method that updates an attribute, often after validation.

Traditional naming:
    get_name()
    set_name(new_name)

A getter does not always need a setter. Some values may be
readable but should not be changeable through the public interface.
"""

class StudentTraditional:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if new_name != "":
            self.__name = new_name
        else:
            print("Name cannot be blank.")


s1 = StudentTraditional("Aniruddh")

print("\\n5. TRADITIONAL GETTER AND SETTER")
print("Current name:", s1.get_name())

s1.set_name("XYZ")
print("Updated name:", s1.get_name())

s1.set_name("")
print("After invalid update:", s1.get_name())


# ============================================================
# 7. GETTER WITHOUT A SETTER
# ============================================================

class StudentRollNumber:
    def __init__(self, roll_no):
        self.__roll_no = roll_no

    def get_roll_no(self):
        return self.__roll_no


s2 = StudentRollNumber(101)

print("\\n6. GETTER WITHOUT SETTER")
print("Roll number:", s2.get_roll_no())
# There is intentionally no set_roll_no() method.


# ============================================================
# 8. @property DECORATOR — GETTER
# ============================================================

"""
@property allows a method to be accessed like an attribute.

Without @property:
    student.get_name()

With @property:
    student.name

The method still runs internally, but parentheses are not used.
"""

class StudentProperty:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


s3 = StudentProperty("Aniruddh")

print("\\n7. PROPERTY GETTER")
print(s3.name)


# ============================================================
# 9. @property WITH A SETTER
# ============================================================

"""
For a property named name, create its setter using:
    @name.setter

Then assignment such as student.name = "XYZ" calls the setter
behind the scenes. The setter can validate the new value.
"""

class StudentWithProperty:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name != "":
            self.__name = new_name
        else:
            print("Name cannot be blank.")


s4 = StudentWithProperty("Aniruddh")

print("\\n8. PROPERTY WITH SETTER")
print("Current name:", s4.name)

s4.name = "XYZ"
print("Updated name:", s4.name)

s4.name = ""
print("After invalid update:", s4.name)


# ============================================================
# 10. TRADITIONAL VS PROPERTY APPROACH
# ============================================================

"""
Traditional:
    student.get_name()
    student.set_name("XYZ")

@property:
    student.name
    student.name = "XYZ"

Both approaches allow controlled access and validation.
@property provides a clean, attribute-like interface.
"""

print("\\n9. QUICK COMPARISON")
print("Traditional getter: object.get_name()")
print("Traditional setter: object.set_name('XYZ')")
print("Property getter:    object.name")
print("Property setter:    object.name = 'XYZ'")


# ============================================================
# 11. QUICK DIFFERENCE: PUBLIC / PROTECTED / PRIVATE-STYLE
# ============================================================

"""
PUBLIC:
    self.name
    Directly accessible from outside the class.

PROTECTED-STYLE:
    self._name
    Accessible, but the underscore convention says to avoid
    direct external use. Often useful for internal/subclass use.

PRIVATE-STYLE:
    self.__name
    Name mangling is applied. Direct access with __name normally
    fails, but the mangled name can still be accessed.

Python's conventions are not a security boundary. Use validation
and a well-designed public interface to control normal access.
"""


# ============================================================
# 12. INTERVIEW QUESTIONS
# ============================================================

"""
Q1. What is encapsulation?
A: Combining data and methods inside a class and controlling
   how the data is accessed or modified.

Q2. What are the benefits of encapsulation?
A: It helps control updates, validate data, reduce accidental
   modification, and improve maintainability.

Q3. Difference between public, protected, and private-style?
A: Public has no leading underscore; protected-style uses one
   leading underscore; private-style uses two leading underscores.

Q4. Does Python support truly private variables?
A: Python does not enforce strict private access. Double-leading
   underscores trigger name mangling, not absolute privacy.

Q5. What is name mangling?
A: A name like __balance in class Bank is internally changed to
   _Bank__balance to avoid accidental name clashes.

Q6. What is a getter?
A: A method/property used to read an attribute's value.

Q7. What is a setter?
A: A method/property used to update an attribute, often after
   validation.

Q8. What is @property?
A: A decorator that lets a method be accessed like an attribute.

Q9. Is a setter compulsory with a getter?
A: No. A value can be readable without allowing updates through
   the public interface.

Q10. Does @property make an attribute truly private?
A: No. It provides a controlled interface; it does not create
   strict security.
"""


# ============================================================
# 13. PRACTICE TASKS
# ============================================================

"""
TASK 1:
Create an Employee class.
- name should be public.
- salary should be stored as __salary.
- Add a @property getter for salary.
- Initially, do not create a setter.

TASK 2:
Add @salary.setter.
- Accept only salary values greater than zero.
- Reject zero and negative values.

TASK 3:
Create a Bank class.
- Store account holder name.
- Store balance as __balance.
- Add deposit(), withdraw(), and get_balance().
- Reject zero/negative deposits.
- Reject withdrawals greater than the available balance.

TASK 4:
Explain in your own words:
- What is encapsulation?
- Difference between _value and __value?
- What is name mangling?
- Difference between traditional getters/setters and @property?

Try solving these tasks yourself.
"""


# ============================================================