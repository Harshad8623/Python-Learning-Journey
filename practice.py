'''
Create a Bank class with these requirements:
1. Store account holder name as a public variable.
2. Store balance as a private variable __balance.
3. Create a @property getter for balance.
4. Create a deposit method.
5. Create a withdraw method.
6. Reject deposits of zero or negative amounts.
7. Reject withdrawals of zero or negative amounts.
8. Reject withdrawals greater than the available balance.
'''

class Bank:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Amount credited successfully. Balance: {self.__balance}"
        else:
            return "Enter amount greater than 0"

    def withdraw(self, amount):
        if amount <= 0:
            return "Enter valid amount above 0"
        elif amount > self.__balance:
            return "Insufficient balance"

        self.__balance -= amount
        return f"Amount debited successfully. Balance: {self.__balance}"


cust1 = Bank("Harshad", 10000)

print("Initial Balance:", cust1.balance)
print(cust1.deposit(5000))
print(cust1.withdraw(3000))
print(cust1.withdraw(20000))
