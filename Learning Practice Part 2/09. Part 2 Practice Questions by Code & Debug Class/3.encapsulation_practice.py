class Bank:
    
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance

    def update_balance(self, amount):
        if amount > 0:
            self.__balance += amount
            return self.__balance
        else:
            return "Enter Amount Greater Than 0"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return self.__balance
        else:
            return "Enter Amounr Greater than 0"

Cust1 = Bank("Harshad", 1000)
print(Cust1.name)
# print(Cust1.__balance)
# we can not access this private variable we have to use method for this
print(Cust1.get_balance())
print(Cust1.update_balance(500))
print(Cust1.withdraw(200))


# ============================================================
# TASK 1: EMPLOYEE — @property GETTER ONLY
# ============================================================

"""
TASK:
- Create an Employee class.
- name should be public.
- salary should be stored as __salary.
- Add a @property getter for salary.
- Do not create a setter.
"""

class EmployeeGetterOnly:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary


emp1 = EmployeeGetterOnly("Harshad", 80000)

print("TASK 1: EMPLOYEE WITH GETTER ONLY")
print("Name:", emp1.name)
print("Salary:", emp1.salary)

# There is no setter for salary in this task.
# Therefore, emp1.salary = 100000 raises AttributeError.


# ============================================================
# TASK 2: EMPLOYEE — @property GETTER AND SETTER
# ============================================================

"""
TASK:
1. Add @salary.setter.
2. Allow salary updates only if salary is greater than zero.
3. If salary is zero or negative, raise a ValueError.
4. Update salary to 100000.
5. Print the updated salary.
"""

class EmployeeWithSetter:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary <= 0:
            raise ValueError("Please enter a value greater than 0")
        else:
            self.__salary = new_salary


emp2 = EmployeeWithSetter("Harshad", 80000)

print("\\nTASK 2: EMPLOYEE WITH GETTER AND SETTER")
print("Initial salary:", emp2.salary)

emp2.salary = 100000
print("Updated salary:", emp2.salary)

# Uncomment to test validation:
# emp2.salary = -5000
# ValueError will be raised.