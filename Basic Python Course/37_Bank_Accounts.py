"""
It's time to open up a bank account! 🏦

Create a file called bank_accounts.py.

Let's define a BankAccount class. Then, let's use the __init__() method to set the following attributes:

first_name (string)
last_name (string)
account_id (integer)
account_type (string)
pin (integer)
balance (float)
Next, let's create three methods:

.deposit(): Add money into the account and return the new balance.
.withdraw(): Take money out by subtracting from balance and returning the withdrawn amount.
.display_balance(): Print the current value of balance.
Lastly, initialize a new object from the BankAccount class and use these methods to do the following:

Deposit $96 into the account.
Withdraw $25 from the account.
Print the current account balance.
"""


class BankAccount:

    # Constructor
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self, money):
        self.balance = self.balance + money
        print(f"You Deposit {money:.2f}")

    def withdraw(self, money):
        if money > self.balance:
            print("Insufficeint Funds")
            return
        self.balance = self.balance - money
        print(f"You Withdraw {money:.2f}")

    def current_balance(self):
        print(f"Your current balance is {self.balance:.2f}")


print("Account 1")
ali = BankAccount("Ali", "Khan", 1001, "Savings", 1234, 500000.0)
ali.deposit(25000)
ali.withdraw(1000000000)
ali.current_balance()
print()

print("Account 2")
ahmed = BankAccount("Ahmed", "Raza", 1002, "Current", 5678, 1200000.0)
ahmed.deposit(50000)
ahmed.withdraw(5000)
ahmed.current_balance()


print("Account 3")
sara = BankAccount("Sara", "Noor", 1003, "Savings", 2468, 980000.5)
sara.deposit(10000)
sara.withdraw(2500)
sara.current_balance()
print()

print("Account 4")
zain = BankAccount("Zain", "Ali", 1004, "Student", 1357, 300000.0)
zain.deposit(15000)
zain.withdraw(1200)
zain.current_balance()
print()
