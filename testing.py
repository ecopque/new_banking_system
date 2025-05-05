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

class A003_WithdrawCLS(A001_TransactionCLS):
    def A001_registerMTD(self, account):
        if self.value <= 0:
            print('Enter a positive value. ')
            return False
        
        elif self.value > C001_balance:
            print(f'You do not have enought balance: {self.account.C001_balance}.')
            return False
        
        else:
            account.C001_balance -= self.A001_value
            account.C001_history.B001_add_transactionMTD(f'Withdra: {self.A001_value}.')
            return True

class B001_History():
    def __init__(self):
        self.B001_transaction = list()

    def B001_add_transactionMTD(self, description: str):
        self.B001_transaction.append(description)
        print('Registered transaction.')