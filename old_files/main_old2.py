# FILE: /main_old2.py

users = list()
def create_user(name, birth, cpf: str, address: str): #1:
    cpf_exists = False
    for i1 in users:
        if i1['cpf'] == cpf:
            cpf_exists = True
            print('CPF already registered.')
            return
    
    if not cpf_exists:
        new_user = {
            'name': name,
            'birth': birth,
            'cpf': cpf,
            'address': address
        }

        users.append(new_user)
        print(f'User {name} created successfully.')
        # return new_user

accounts = list()
def create_current_account(cpf):
    user_found = None
    for i2 in users:
        if i2['cpf'] == cpf:
            user_found = i2
            print(f'User found: {user_found}')
            break
    
    if not user_found:
        print('User not found.')
        return

    account_number = (len(accounts) + 1)
    account_new = {
        'agency': '0001',
        'account_number': account_number,
        'user': user_found
    }

    accounts.append(account_new)
    print('Account created successfully.')

# Keyword only:
def withdraw(*, balance, withdrawal, statement, limit, number_withdrawals, limit_withdrawals):
    if withdrawal > limit:
        print(f'It is not possible to withdraw ammounts above {limit}')
    elif number_withdrawals >= limit_withdrawals:
        print('You have reached your daily withdrawal limit.')
    elif withdrawal > balance:
        print(f'You do not have enough balance. Current: R${balance:.2f}.')
    elif withdrawal > 0:
        balance -= withdrawal
        statement.append(f'Withdrawal: R${withdrawal:.2f}.')
        number_withdrawals += 1
        print(f'Cash out: R${withdrawal:.2f}. Balance: {balance:.2f}.')
    else:
        print('Enter only positive values.')
    return balance, statement

# Positional only:
def deposit(balance, amount, statement, /):
    if amount > 0:
        balance += amount
        statement.append(f'Deposit of R${amount:.2f}.')
        print(f'Deposit of R${amount:.2f}. Balance: {balance:.2f}.')
    else:
        print('Enter only positive values.')
    return balance, statement

# Positional only and keyword only:
def bank_statement(balance, /, *, statement ):
    print('EXTRACT: ')
    print('DEPOSIT: ')
    if statement:
        for i3 in statement:
            if i3.startswith('Deposit'):
                print(i3)
    else:
        print('No deposit made.')

    print('WITHDRAWALS: ')
    if statement:
        for i4 in statement:
            if i4.startswith('Withdrawal'):
                print(i4)
    
    else:
        print('No withdrawals made.')

    print(f'Balance: {balance:.2f}.')

def list_accounts():
    for i5 in accounts:
        print(f'Agency: {i5["agency"]}', 
              f'Number of account: {i5["account_number"]}',
              f'User: {i5["user"]["name"]}'
        )

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
                cashout_amount = float(input('Enter the cash out amount: '))
                balance, statement = withdraw(
                                     balance = balance, 
                                     withdrawal = cashout_amount, 
                                     statement = statement, 
                                     limit = withdrawal_limit, 
                                     number_withdrawals = number_withdrawals, 
                                     limit_withdrawals = withdrawal_limit_day
                )
                if cashout_amount > 0 and cashout_amount <= balance and number_withdrawals < withdrawal_limit_day:
                    number_withdrawals += 1

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