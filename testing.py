# FILE: /testing.py

from abc import ABC, abstractclassmethod

class A001_TransactionCLS(ABC):
    def __init__(self, value: float):
        self.A001_value = value

    @abstractclassmethod
    def A001_registerMTD(self, account):
        pass

class A002_DepositCLS(A001_TransactionCLS):
    def A001_registerMTD(self, account):
        if self.A001_value <= 0:
            print('Enter a positive value.')
            return False

        else:
            account.C001_balance += self.A001_value
            account.C001_history.B001_add_transactionMTD(f'Deposit: {self.A001_value: .2f}.')
            return True