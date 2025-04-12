# FILE: /main.py

from abc import ABC, abstractmethod #1:
from datetime import date

# UML Architecture and Class Hierarchy

# Abstract Classes and Subclasses (Polymorphism)
class Transaction(ABC):
    def __init__(self, value: float): #2:
        self.value = value #2:

    @abstractmethod #3:
    def register(self, account): #3:
        pass

class Deposit(Transaction):
    def register(self, account):
        if self.value <= 0:
            print('Enter only positive values.')
            return False
       
        else:
            account.balance += self.value
            account.history.add_transaction(f'Deposit: R${self.value:.2f}.')
            return True

class Withdraw(Transaction):
    def register(self, account):
        if self.value <= 0:
            print('Enter only positive values.')
            return False
        
        elif self.value > account.balance:
            print(f'You do not have enough balance. Current: R${account.balance:.2f}.')
            return False
        
        else:
            account.balance -= self.value
            account.history.add_transaction(f'Withdrawal: R${self.value:.2f}.')
            return True

# ==============================
# 2) SUPPORT CLASSES
# ==============================
class History:
    def __init__(self):
        self.transactions = list()

    def add_transaction(self, description: str):
        self.transactions.append(description)

# ==============================
# 3) ACCOUNT AND SUBCLASS (INHERITANCE)
# ==============================
class Account:
    def __init__(self, client, number, agency='0001', limit=500):
        self.client = client
        self.number = number
        self.agency = agency
        self.limit = limit

        self.balance = 0
        self.history = History()

    def deposit(self, value):
        transaction = Deposit(value)
        return transaction.register(self)

    def withdraw(self, value):
        transaction = Withdraw(value)
        return transaction.register(self)

class CurrentAccount(Account):
    def __init__(self, client, number, agency='0001', limit=500, limit_withdrawals=3):
        super().__init__(client, number, agency, limit)
        self.limit_withdrawals = limit_withdrawals
        
        self.number_withdrawals = 0

    def withdraw(self, value):
        if self.number_withdrawals >= self.limit_withdrawals:
            print('You have reached your daily withdrawal limit.')
            return False

        if value > self.limit:
            print(f'It is not possible to withdraw amounts above {self.limit}.')
            return False
        
        success = super().withdraw(value)
        if success:
            self.number_withdrawals += 1
        
        return success

# ==============================
# 4) CLIENT CLASS
# ==============================
class Client:
    def __init__(self, name, birth, cpf, address):
        self.name = name
        self.birth = birth
        self.cpf = cpf
        self.address = address

        self.accounts = list()

    def add_account(self, account):
        self.accounts.append(account)
    
# ==============================
# 5) GLOBAL LISTS (USERS/ACCOUNTS) & ORIGINAL FUNCTIONS
# ==============================
users = list()
accounts = list()

def create_user(name, birth, cpf: str, address: str):
    cpf_exists = False
    
    for i1 in users:
        if i1.cpf == cpf:
            cpf_exists = True
            print('CPF already registered.')
            return
        
    if not cpf_exists:
        new_user = Client(name, birth, cpf, address)
        users.append(new_user)
        print(f'User {name} created successfully.')

def create_current_account(cpf):
    user_found = None

    for i2 in users:
        if i2.cpf == cpf:
            user_found = i2
            print(f'User found: {user_found.name}')
            break

    if not user_found:
        print('User not found.')
        return
    
    account_number = (len(accounts) + 1)
    new_account = CurrentAccount(user_found, account_number)
    user_found.add_account(new_account)
    accounts.append(new_account)

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