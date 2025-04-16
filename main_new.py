# FILE: /main.py

from abc import ABC, abstractmethod #1:
from datetime import date

# Abstract Classes and Subclasses (Polymorphism):
class A001_TransactionCLS(ABC):
    def __init__(self, value: float): #2:
        self.A001_value = value #2:

    @abstractmethod #3:
    def A001_registerMTD(self, account): #3:
        pass

class A002_DepositCLS(A001_TransactionCLS):
    def A001_registerMTD(self, account): #4:
        if self.A001_value <= 0: #4:
            print('Enter only positive values.')
            return False
       
        else: #5:
            account.C001_balance += self.A001_value #5:
            account.C001_history.B001_add_transactionMTD(f'Deposit: R${self.A001_value:.2f}.') #5:
            return True

class A003_WithdrawCLS(A001_TransactionCLS):
    def A001_registerMTD(self, account): #6:
        if self.A001_value <= 0: #6:
            print('Enter only positive values.') #6:
            return False #6:
        
        elif self.A001_value > account.C001_balance: #7:
            print(f'You do not have enough balance. Current: R${account.C001_balance:.2f}.') #7:
            return False #7:
        
        else: #8:
            account.C001_balance -= self.A001_value #8:
            account.C001_history.B001_add_transactionMTD(f'Withdrawal: R${self.A001_value:.2f}.') #8:
            return True #8:


# Support Classes:
class B001_HistoryCLS: #9:
    def __init__(self): #9:
        self.B001_transactions = list() #9:

    def B001_add_transactionMTD(self, description: str): #10:
        self.B001_transactions.append(description) #10:


# Account and Subclass (Inheritance):
class C001_AccountCLS:
    def __init__(self, client, number, agency='0001', limit=500): #11:
        self.C001_client = client #11:
        self.C001_number = number #11:
        self.C001_agency = agency #11:
        self.C001_limit = limit #11:

        self.C001_balance = 0 #11:
        self.C001_history = B001_HistoryCLS() #11:

    def C001_depositMTD(self, value): #12:
        C001_transaction = A002_DepositCLS(value) #12:
        return C001_transaction.A001_registerMTD(self) #12:

    def C001_withdrawMTD(self, value): #13:
        C001_transaction = A003_WithdrawCLS(value) #13:
        return C001_transaction.A001_registerMTD(self) #13:

class C002_CurrentAccountCLS(C001_AccountCLS): #14:
    def __init__(self, client, number, agency='0001', limit=500, limit_withdrawals=3): #15:
        super().__init__(client, number, agency, limit) #15:
        self.C002_limit_withdrawals = limit_withdrawals #15:
        
        self.C002_number_withdrawals = 0 #15:

    def C002_withdrawMTD(self, value):
        if self.C002_number_withdrawals >= self.C002_limit_withdrawals: #16:
            print('You have reached your daily withdrawal limit.')
            return False

        if value > self.C001_limit: #17:
            print(f'It is not possible to withdraw amounts above {self.C001_limit}.')
            return False
        
        C002_success = super().C001_withdrawMTD(value) #18:
        if C002_success: #18:
            self.C002_number_withdrawals += 1 #18:
        
        return C002_success


# Client Class:
class D001_ClientCLS: #19:
    def __init__(self, name, birth, cpf, address): #19:
        self.D001_name = name
        self.D001_birth = birth
        self.D001_cpf = cpf
        self.D001_address = address

        self.D001_accounts = list()

    def D001_add_accountMTD(self, account): #20:
        self.D001_accounts.append(account) #20:
    

# Global Lists & Original Functions:
users_VARg = list() #21:
accounts_VARg = list() #21:

def create_user(name, birth, cpf: str, address: str): #22:
    cpf_exists = False
    
    for i1 in users_VARg: #22:
        if i1.D001_cpf == cpf:
            cpf_exists = True
            print('CPF already registered.')
            return
        
    if not cpf_exists: #22:
        new_user = D001_ClientCLS(name, birth, cpf, address)
        users_VARg.append(new_user)
        print(f'User {name} created successfully.')

def create_current_account(cpf): #23:
    user_found = None #24:

    for i2 in users_VARg:
        if i2.D001_cpf == cpf:
            user_found = i2
            print(f'User found: {user_found.D001_name}')
            break

    if not user_found:
        print('User not found.')
        return
    
    account_number = (len(accounts_VARg) + 1) #25:

    # [user_found = client] and [account_number = number] of CurrentAccount().
    new_account = C002_CurrentAccountCLS(user_found, account_number) #26: 
    user_found.D001_add_accountMTD(new_account)
    accounts_VARg.append(new_account)


def withdraw(*, balance, withdrawal, statement, limit, number_withdrawals, limit_withdrawals): #27: #33:
    if not accounts_VARg: #28: #TODO: Obstructed flow. Check.
        print('No accounts available to withdraw from.')
        return balance, statement #28:

    # We simulate withdrawing from the most recently created account.
    account = accounts_VARg[-1] #29:

    account.C001_limit = limit
    account.C002_limit_withdrawals = limit_withdrawals
    account.C002_number_withdrawals = number_withdrawals

    success = account.C002_withdrawMTD(withdrawal) #30: #boolean

    new_balance = account.balance #31:

    if success:
        statement.append(f'Withdrawal: R${withdrawal:.2f}.') #32:
        print(f'Cash out: R${withdrawal:.2f}. Balance: {new_balance:.2f}.')

    return new_balance, statement


def deposit(balance, amount, statement, /): #TODO
    if not accounts_VARg:
        print('No accounts available to deposit into.')
        return balance, statement

    account = accounts_VARg[-1]
    success = account.C001_depositMTD(amount)
    new_balance = account.C001_balance

    if success:
        statement.append(f'Deposit of R${amount:.2f}.')
        print(f'Deposit of R${amount:.2f}. Balance: {new_balance:.2f}.')

    return new_balance, statement

def bank_statement(balance, /, *, statement ): #34: #35:
    if not accounts_VARg:
        print('No accounts available.')
        return

    account = accounts_VARg[-1]
    print('EXTRACT: ')
    print('DEPOSIT: ')
    if account.C001_history.B001_transactions: #36:
        for i3 in account.C001_history.B001_transactions: #36:
            if i3.startswith('Deposit'): #36:
                print(i3)
    else:
        print('No deposit made.')

    print('WITHDRAWALS: ')
    if account.C001_history.B001_transactions: #37:
        for i4 in account.C001_history.B001_transactions: #37:
            if i4.startswith('Withdrawal'): #37:
                print(i4)
    else:
        print('No withdrawals made.')

    print(f'Balance: {account.C001_balance:.2f}.')

def list_accounts():
    if not accounts_VARg:
        print('No accounts registered yet.')
        return

    for i5 in accounts_VARg:
        print(
            f'Agency: {i5.C001_agency}',
            f'Number of account: {i5.C001_number}',
            f'User: {i5.C001_client.name}'
        )

# Menu:
def menu():
    balance = 0
    statement = list()
    withdrawal_limit = 500
    withdrawal_limit_day = 3
    number_withdrawals = 0
    
    while True:
        try:
            options = int(input('Choose one of the options:\n'
                                    '[1] - Cash out\n'
                                    '[2] - Deposit\n'
                                    '[3] - View extract\n'
                                    '[4] - Create user\n'
                                    '[5] - Create current account\n'
                                    '[6] - List accounts\n'
                                    '[7] - Exit\n'
                                    '[8] - Info: ')
            )

            if options == 1:
                if accounts_VARg:
                    cashout_amount = float(input('Enter the cash out amount: '))
                    old_withdrawals = number_withdrawals

                    balance, statement = withdraw(
                                        balance = balance, 
                                        withdrawal = cashout_amount, 
                                        statement = statement, 
                                        limit = withdrawal_limit, 
                                        number_withdrawals = number_withdrawals, 
                                        limit_withdrawals = withdrawal_limit_day
                    )

                    if (
                        cashout_amount > 0 
                        and cashout_amount <= balance 
                        and number_withdrawals < withdrawal_limit_day
                    ):
                        number_withdrawals += 1

                else:
                    print('No accounts available. Create one before making a withdrawal.')

            elif options == 2:
                deposit_amount = float(input('Enter the deposit amount: '))
                balance, statement = deposit(balance, deposit_amount, statement)

            elif options == 3:
                bank_statement(balance, statement=statement)

            elif options == 4:
                name = str(input('Enter your name: '))
                birth = str(input('Enter your birth date (DD/MM/YYY): '))
                cpf = str(input('Enter your CPF (numbers only): '))
                address = str(input('Enter you address (logradouro, nro - bairro - city/state: )'))

                create_user(name, birth, cpf, address)

            elif options == 5:
                cpf = str(input('Enter your CPF (numbers only): '))
                create_current_account(cpf)

            elif options == 6:
                list_accounts()
            
            elif options == 7:
                print('Thank you for using our system. Goodbye!')
                break

            elif options == 8:
                print('### DEVELOPER DATA ###')
                print('Developed by: Edson Copque\n'
                    'Site: https://linktr.ee/edsoncopque\n'
                    'GitHub: https://github.com/ecopque\n'
                    'Repo: https://github.com/ecopque/new_banking_system\n'
                    'Signal Messenger: ecop.01\n')

            else:
                print('Please enter a valid number.')

        except ValueError:
            print(f'Please enter a valid input.')

if __name__ == '__main__':
    menu()

    '''
    . Developer: Edson Copque
    . Website: https://linktr.ee/edsoncopque
    . GitHub: https://github.com/ecopque
    . Signal Messenger: ecop.01
    '''