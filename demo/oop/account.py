class Account:
    # Constructor
    def __init__(self, acno, ahname, balance = 0):
        # Object Attributes
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    # Methods
    def getbalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def __str__(self):
        return f"{self.acno},{self.ahname},{self.balance}"

    def __eq__(self, other):
        return self.acno == other.acno


    # Create an object of Account
a1 = Account(1, "Gary", 10000)
print(a1)
a1.withdraw(2000)
a1.deposit(5000)
print(a1.getbalance())
#print(a1.balance)  # not to be done


a2 = Account(2, 'Ben')
print(a2.getbalance())

