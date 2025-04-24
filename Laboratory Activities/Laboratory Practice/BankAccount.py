
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self._balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def display_account_type(self):
        pass

class CurrentAccount(BankAccount):
    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance - amount >= -5000:
            self._balance -= amount
        else:
            print("Overdraft limit exceeded!")

    def display_account_type(self):
        return "Current Account"

class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient balance! No overdraft allowed.")

    def display_account_type(self):
        return "Savings Account"

def print_account_details(account):
    print(f"Account Number: {account.account_number}")
    print(f"Balance: {account.balance}")
    print(f"Type: {account.display_account_type()}")
    print("-" * 30)

s1 = SavingsAccount("SA123", 1000)
s2 = SavingsAccount("SA124", 2000)
c1 = CurrentAccount("CA123", 500)
c2 = CurrentAccount("CA124", 100)


s1.deposit(200)
s1.withdraw(500)
s2.withdraw(2500)  

c1.withdraw(1000)
c2.withdraw(5200)  
c2.withdraw(1000)  

print_account_details(s1)
print_account_details(s2)
print_account_details(c1)
print_account_details(c2)
    
    
    
    
    
    