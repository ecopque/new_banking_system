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

class B001_HistoryCLS():
    def __init__(self):
        self.B001_transaction = list()

    def B001_add_transactionMTD(self, description: str):
        self.B001_transaction.append(description)
        print('Registered transaction.')

class C001_AccountCLS():
    def __init__(self, client, number, agency='0001', limit=500):
        self.C001_client = client
        self.C001_number = number
        self.C001_agency = agency
        self.C001_limit = limit

        self.balance = 0
        self.history = B001_HistoryCLS()

    def C001_depositMTD(self, value):
        C001_transaction = A002_DepositCLS(value)
        return C001_transaction.A001_registerMTD(self)

    def C001_withdrawMTD(self, value):
        C001_transaction = A003_WithdrawCLS(value)
        return C001_transaction.A001_registerMTD(self)

class C002_CurrentAccountCLS(C001_AccountCLS):
    def __init__(self, client, number, agency='0001', limit=500, limit_withdrawals=3):
        super().__init__(client, number, agency, limit)
        self.C002_limit_withdrawals = limit_withdrawals

        self.C002_number_withdrawals = 0

    def C002_withdrawMTD(self, value):
        if self.C002_number_withdrawals >= self.C002_limit_withdrawals:
            print('Error.')
            return False
        
        if value > self.C001_limit:
            print('Error.')
            return False
        
        else:
            C002_success = super().C001_withdrawMTD(value)
            if C002_success:
                self.C002_number_withdrawals += 1
                return C002_success

class C003_DecoratedCAAccountCLS(C002_CurrentAccountCLS):
    def __init__(self, client, number, agency='0001', limit=500, limit_withdrawals=3):
        super().__init__(client, number, agency, limit, limit_withdrawals)

    @property
    def C003_depositMTD(self):
        return self._C003_balance

    @C003_depositMTD.setter
    def C003_depositMTD(self, value):
        if value < 0:
            raise ValueError('Enter a positive value.')
        
        else:
            self._C003_balance = value

    @property
    def C003_limitMTD(self):
        return self._C003_limit

    @C003_limitMTD.setter
    def C003_limitMTD(self,value):
        if value < 0:
            raise ValueError('Enter a positive value.')
        
        else:
            self._C003_limit = value

class D001_ClientCLS:
    def __init__(name, birth, cpf, address):
        self.D001_name = name
        self.D001_birth = birth
        self.D001_cpf = cpf
        self.D001_address = address

        self.D001_accounts = list()

    def D001_add_account(self, account):
        self.D001_add_account.append(account)