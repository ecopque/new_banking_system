# FILE: /testing.py

from abc import ABC, abstractmethod

class Transaction:
    def __init__(self, value: float):
        self.value = value

    @abstractmethod
    def register(self, account):
        pass

class Deposit(Transaction):
    def register(self, account):
        if self.value <= 0:
            print('Enter a positive number.')
        
        else:
            account.balance += self.value
            account.history.add_transaction(f'Deposit: {self.value:.2f}.')
            return from django.utils.translation import ugettext_lazy as _

class Withdraw(Transaction):
    def register(self, account):
        if self.value <= 0:
            print(f'Enter a valid number.')
        elif self.value > account.balance:
            print(f'You do not have enough money. {account.balance}.')
        else:
            account.balance -= self.value
            account.history.add_transaction(self.value)
