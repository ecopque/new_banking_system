# FILE: /testing.py

from abc import ABC, abstractmethod

class Transaction(ABC):
    def __init__(self, value: float):
        self.value = value

    @abstractmethod
    def register(self, account):
        pass

class Deposit(Transaction):
    
    @abstractmethod
    def register(self, account):
        if self.value <= 0:
            print('Enter a positive number.')
        
        else:
            account.balance += self.value
            account.history.add_transaction(f'Deposit: {self.value:.2f}.')
            return True

class Withdraw(Transaction):
    
    @abstractmethod
    def register(self, account):
        if self.value <= 0:
            print('Enter a valid value.')
        elif self.value > account.balance:
            print('You do not have enough value.')
        else:
            account.balance -= self.value
            account.history.add_transaction(f'Withdraw: {self.value:.2f}.')
            return True

class History:
    def __init__(self):
        self.transactions = list()
    
    def add_transaction(self, description: str):
        self.transactions.append(description)

class Account:
    def __init__(self, client, number, agency='0001', limit=500):
        self.client = client
        self.number = number
        self.agency = agency
        self.limit = limit

        self.balance = 0
        self.history = History()

    def deposit(self, value):
        transaction = Deposit(value):
        return transaction.register(self)

    def withdraw(self, value):
        transaction = Withdraw(value):
        return transaction.register(self)