# FILE: /main.py

# UML ARCHITECTURE AND CLASS HIERARCHY

from abc import ABC, abstractmethod #1:
from datetime import date

# Abstract Classes and Subclasses (Polymorphism):
class Transaction(ABC):
    def __init__(self, value: float): #2:
        self.value = value #2:

    @abstractmethod #3:
    def register(self, account): #3:
        pass

class Deposit(Transaction):
    def register(self, account): #4:
        if self.value <= 0: #4:
            print('Enter only positive values.')
            return False
       
        else: #5:
            account.balance += self.value #5:
            account.history.add_transaction(f'Deposit: R${self.value:.2f}.') #5:
            return True

class Withdraw(Transaction):
    def register(self, account): #6:
        if self.value <= 0: #6:
            print('Enter only positive values.') #6:
            return False #6:
        
        elif self.value > account.balance: #7:
            print(f'You do not have enough balance. Current: R${account.balance:.2f}.') #7:
            return False #7:
        
        else: #8:
            account.balance -= self.value #8:
            account.history.add_transaction(f'Withdrawal: R${self.value:.2f}.') #8:
            return True #8:


# Support Classes:
class History: #9:
    def __init__(self): #9:
        self.transactions = list() #9:

    def add_transaction(self, description: str): #10:
        self.transactions.append(description) #10:


# Account and Subclass (Inheritance):
class Account:
    def __init__(self, client, number, agency='0001', limit=500): #11:
        self.client = client #11:
        self.number = number #11:
        self.agency = agency #11:
        self.limit = limit #11:

        self.balance = 0 #11:
        self.history = History() #11:

    def deposit(self, value): #12:
        transaction = Deposit(value) #12:
        return transaction.register(self) #12:

    def withdraw(self, value): #13:
        transaction = Withdraw(value) #13:
        return transaction.register(self) #13:

class CurrentAccount(Account): #14:
    def __init__(self, client, number, agency='0001', limit=500, limit_withdrawals=3): #15:
        super().__init__(client, number, agency, limit) #15:
        self.limit_withdrawals = limit_withdrawals #15:
        
        self.number_withdrawals = 0 #15:

    def withdraw(self, value):
        if self.number_withdrawals >= self.limit_withdrawals: #16:
            print('You have reached your daily withdrawal limit.')
            return False

        if value > self.limit: #17:
            print(f'It is not possible to withdraw amounts above {self.limit}.')
            return False
        
        success = super().withdraw(value) #18:
        if success: #18:
            self.number_withdrawals += 1 #18:
        
        return success


# Client Class:
class Client: #19:
    def __init__(self, name, birth, cpf, address): #19:
        self.name = name
        self.birth = birth
        self.cpf = cpf
        self.address = address

        self.accounts = list()

    def add_account(self, account): #20:
        self.accounts.append(account) #20:
    

# Global Lists & Original Functions:
users = list() #21:
accounts = list() #21:

def create_user(name, birth, cpf: str, address: str): #22:
    cpf_exists = False
    
    for i1 in users: #22:
        if i1.cpf == cpf:
            cpf_exists = True
            print('CPF already registered.')
            return
        
    if not cpf_exists: #22:
        new_user = Client(name, birth, cpf, address)
        users.append(new_user)
        print(f'User {name} created successfully.')

def create_current_account(cpf): #23:
    user_found = None

    for i2 in users: #23:
        if i2.cpf == cpf:
            user_found = i2
            print(f'User found: {user_found.name}')
            break

    if not user_found: #23:
        print('User not found.')
        return
    
    account_number = (len(accounts) + 1)
    new_account = CurrentAccount(user_found, account_number)
    user_found.add_account(new_account)
    accounts.append(new_account)
#TODO
def withdraw(*, balance, withdrawal, statement, limit, number_withdrawals, limit_withdrawals):
    if not accounts:
        print('No accounts available to withdraw from.')
        return balance, statement

    # We simulate withdrawing from the most recently created account
    account = accounts[-1]

    # Force the account's internal limit to match arguments (for demonstration).
    # This aligns with the old procedural limit checks, but is not strictly required.
    account.limit = limit
    account.limit_withdrawals = limit_withdrawals
    account.number_withdrawals = number_withdrawals

    success = account.withdraw(withdrawal)
    # Return updated balance from the account
    new_balance = account.balance

    # If success, append to statement
    if success:
        statement.append(f'Withdrawal: R${withdrawal:.2f}.')
        print(f'Cash out: R${withdrawal:.2f}. Balance: {new_balance:.2f}.')

    return new_balance, statement

def deposit(balance, amount, statement, /):
    if not accounts:
        print('No accounts available to deposit into.')
        return balance, statement

    account = accounts[-1]
    success = account.deposit(amount)
    new_balance = account.balance

    if success:
        statement.append(f'Deposit of R${amount:.2f}.')
        print(f'Deposit of R${amount:.2f}. Balance: {new_balance:.2f}.')

    return new_balance, statement

def bank_statement(balance, /, *, statement ):
    if not accounts:
        print('No accounts available.')
        return

    account = accounts[-1]
    print('EXTRACT: ')
    print('DEPOSIT: ')
    if account.history.transactions:
        for i3 in account.history.transactions:
            if i3.startswith('Deposit'):
                print(i3)
    else:
        print('No deposit made.')

    print('WITHDRAWALS: ')
    if account.history.transactions:
        for i4 in account.history.transactions:
            if i4.startswith('Withdrawal'):
                print(i4)
    else:
        print('No withdrawals made.')

    print(f'Balance: {account.balance:.2f}.')

def list_accounts():
    if not accounts:
        print('No accounts registered yet.')
        return

    for i5 in accounts:
        print(
            f'Agency: {i5.agency}',
            f'Number of account: {i5.number}',
            f'User: {i5.client.name}'
        )

# ==============================
# 6) MENU (UNCHANGED FLOW)
# ==============================
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
                                    '[8] - Info): ')
            )

            if options == 1:
                if accounts:
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