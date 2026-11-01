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