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
        return C001_transaction.A001_registerMTD(self) #13: #(1.6.3.1)

class C002_CurrentAccountCLS(C001_AccountCLS): #14:
    def __init__(self, client, number, agency='0001', limit=500, limit_withdrawals=3): #15:
        super().__init__(client, number, agency, limit) #15:
        self.C002_limit_withdrawals = limit_withdrawals #15:
        
        self.C002_number_withdrawals = 0 #15:

    def C002_withdrawMTD(self, value):
        if self.C002_number_withdrawals >= self.C002_limit_withdrawals: #16:
            print('You have reached your daily withdrawal limit.')
            return False

        if value > self.C001_limit: #17: #(1.6.1)
            print(f'It is not possible to withdraw amounts above {self.C001_limit}.')
            return False
        
        C002_success = super().C001_withdrawMTD(value) #18: #(1.6.2)
        if C002_success: #18:
            self.C002_number_withdrawals += 1 #18:
        
        return C002_success

class C003_DecoratedCAAccountCLS(C002_CurrentAccountCLS): #38:
    def __init__(self, client, number, agency='0001', limit=500, limit_withdrawals=3):
        super().__init__(client, number, agency, limit, limit_withdrawals)

    @property #39: #40:
    def C003_balanceMTD(self): #39:
        return self._C003_balance #39:
    
    @C003_balanceMTD.setter #41:
    def C003_balanceMTD(self, value): #41:
        if value < 0: #42:
            raise ValueError('Balance cannot be negative.') #42:
        self._C003_balance = value

    @property
    def C003_limitMTD(self):
        return self._C003_limit

    @C003_limitMTD.setter
    def C003_limitMTD(self, value):
        if value < 0:
            raise ValueError('Limit cannot be negative.')
        self._C003_limit = value


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
users_VARG = list() #21:
accounts_VARG = list() #21:

def E001_create_userFCT(name, birth, cpf: str, address: str): #22:
    E001_cpf_exists = False
    
    for it1 in users_VARG: #22:
        if it1.D001_cpf == cpf:
            E001_cpf_exists = True
            print('CPF already registered.')
            return
        
    if not E001_cpf_exists: #22:
        E001_new_userVARL = D001_ClientCLS(name, birth, cpf, address)
        users_VARG.append(E001_new_userVARL)
        print(f'User {name} created successfully.')

def F001_create_current_accountFCT(cpf): #23:
    F001_user_found = None #24:

    for it2 in users_VARG:
        if it2.D001_cpf == cpf:
            F001_user_found = it2
            print(f'User found: {F001_user_found.D001_name}')
            break

    if not F001_user_found:
        print('User not found.')
        return
    
    F001_account_number = (len(accounts_VARG) + 1) #25:

    # [user_found = client] and [account_number = number] of CurrentAccount().
    F001_new_account = C002_CurrentAccountCLS(F001_user_found, F001_account_number) #26: 
    F001_user_found.D001_add_accountMTD(F001_new_account)
    accounts_VARG.append(F001_new_account)

def F002_create_decorated_caFCT(cpf): #43:
    F002_user_found = None

    for it6 in users_VARG:
        if it6.D001_cpf == cpf:
            F002_user_found = it6
            print(f'User found: {it6.D001_name}.')
            break

    if not F002_user_found:
        print('User not found.')
        return
    
    F002_account_number = (len(accounts_VARG) + 1)

    F002_new_account = C003_DecoratedCAAccountCLS(F002_user_found, F002_account_number)
    F002_user_found.D001_add_accountMTD(F002_new_account)
    accounts_VARG.append(F002_new_account)
    
    print(f'Decorated account #{F002_account_number} created for {F002_user_found.D001_name}.')


def G001_withdrawFCT(*, balance, withdrawal, statement, limit, number_withdrawals, limit_withdrawals): #27: #33:
    if not accounts_VARG: #28: #(1.2)
        print('No accounts available to withdraw from.')
        return balance, statement #28:

    # We simulate withdrawing from the most recently created account.
    G001_account = accounts_VARG[-1] #29:

    G001_account.C001_limit = limit #(1.3)
    G001_account.C002_limit_withdrawals = limit_withdrawals #(1.4)
    G001_account.C002_number_withdrawals = number_withdrawals #(1.5)

    G001_success = G001_account.C002_withdrawMTD(withdrawal) #30: #(1.6) #boolean

    G001_new_balance = G001_account.C001_balance #31:

    if G001_success:
        statement.append(f'Withdrawal: R${withdrawal:.2f}.') #32:
        print(f'Cash out: R${withdrawal:.2f}. Balance: {G001_new_balance:.2f}.')

    return G001_new_balance, statement


def H001_depositFCT(balance, amount, statement, /):
    if not accounts_VARG: #TODO: Obstructed flow. Check.
        print('No accounts available to deposit into.')
        return balance, statement

    H001_account = accounts_VARG[-1]
    H001_success = H001_account.C001_depositMTD(amount)
    H001_new_balance = H001_account.C001_balance

    if H001_success:
        statement.append(f'Deposit of R${amount:.2f}.')
        print(f'Deposit of R${amount:.2f}. Balance: {H001_new_balance:.2f}.')

    return H001_new_balance, statement

def I001_bank_statementFCT(balance, /, *, statement ): #34: #35:
    if not accounts_VARG: #TODO Obstructed flow? Check.
        print('No accounts available.')
        return

    I001_account = accounts_VARG[-1]
    print('EXTRACT: ')
    print('DEPOSIT: ')
    if I001_account.C001_history.B001_transactions: #36:
        for it3 in I001_account.C001_history.B001_transactions: #36:
            if it3.startswith('Deposit'): #36:
                print(it3)
    else:
        print('No deposit made.')

    print('WITHDRAWALS: ')
    if I001_account.C001_history.B001_transactions: #37:
        for it4 in I001_account.C001_history.B001_transactions: #37:
            if it4.startswith('Withdrawal'): #37:
                print(it4)
    else:
        print('No withdrawals made.')

    print(f'Balance: {I001_account.C001_balance:.2f}.')

def J001_list_accountsFCT():
    if not accounts_VARG:
        print('No accounts registered yet.')
        return

    for it5 in accounts_VARG:
        print(
            f'Agency: {it5.C001_agency}',
            f'Number of account: {it5.C001_number}',
            f'User: {it5.C001_client.D001_name}'
        )

# Menu:
def K001_menuFCT():
    K001_balance = 0
    K001_statement = list()
    K001_value_limit = 500
    K001_number_withdrawals = 0
    K001_limit_withdrawals = 3
    
    while True:
        try:
            K001_options = int(input('Choose one of the options:\n'
                                    '[1] - Cash out\n'
                                    '[2] - Deposit\n'
                                    '[3] - View extract\n'
                                    '[4] - Create user\n'
                                    '[5] - Create current account\n'
                                    '[6] - List accounts\n'
                                    '[7] - Exit\n'
                                    '[8] - Info\n'
                                    '[9] - Create DECORATED current account: ')
            )

            if K001_options == 1:
                if accounts_VARG:
                    K001_cashout_amount = float(input('Enter the cash out amount: '))
                    K001_old_withdrawals = K001_number_withdrawals

                    K001_balance, K001_statement = G001_withdrawFCT( # (1.1)
                                        balance = K001_balance, 
                                        withdrawal = K001_cashout_amount, 
                                        statement = K001_statement, 
                                        limit = K001_value_limit, 
                                        number_withdrawals = K001_number_withdrawals, 
                                        limit_withdrawals = K001_limit_withdrawals
                    )

                    if (
                        K001_cashout_amount > 0 
                        and K001_cashout_amount <= K001_balance 
                        and K001_number_withdrawals < K001_limit_withdrawals
                    ):
                        K001_number_withdrawals += 1

                else:
                    print('No accounts available. Create one before making a withdrawal.')

            elif K001_options == 2:
                K001_deposit_amount = float(input('Enter the deposit amount: '))
                K001_balance, K001_statement = H001_depositFCT(K001_balance, K001_deposit_amount, K001_statement)

            elif K001_options == 3:
                I001_bank_statementFCT(K001_balance, statement=K001_statement)

            elif K001_options == 4:
                K001_name = str(input('Enter your name: '))
                K001_birth = str(input('Enter your birth date (DD/MM/YYY): '))
                K001_cpf = str(input('Enter your CPF (numbers only): '))
                K001_address = str(input('Enter you address (logradouro, nro - bairro - city/state: )'))

                E001_create_userFCT(K001_name, K001_birth, K001_cpf, K001_address)

            elif K001_options == 5:
                K001_cpf = str(input('Enter your CPF (numbers only): '))
                F001_create_current_accountFCT(K001_cpf)

            elif K001_options == 6:
                J001_list_accountsFCT()
            
            elif K001_options == 7:
                print('Thank you for using our system. Goodbye!')
                break

            elif K001_options == 8:
                print('### DEVELOPER DATA ###')
                print('Developed by: Edson Copque\n'
                    'Hub: https://linktr.ee/edsoncopque\n'
                    'GitHub: https://github.com/ecopque\n'
                    'Repository: https://github.com/ecopque/new_banking_system\n'
                    'Signal Messenger: ecop.01\n')
            
            elif K001_options == 9:
                K001_cpf = input('Enter your CPF (numbers only): ')
                F002_create_decorated_caFCT(K001_cpf)

            else:
                print('Please enter a valid number.')

        except ValueError:
            print(f'Please enter a valid input.')

if __name__ == '__main__':
    K001_menuFCT()