# FILE: /main.py

# Estrutura de dados:
usuarios = []
contas = []

# Funções para operações bancárias:
# A função de saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    ...




updated_balance = 0
limit_cashout = 500
limit_qtde = 3

cashouts = []
deposits = []

while True:
    try:
        options = int(input('Choose one of the options:\n'
                                '[1] - Cash out\n'
                                '[2] - Deposit\n'
                                '[3] - View extract\n'
                                '[4] - Exit\n'
                                '[5] - Info): '))

        if options == 1:
            cashout_amount = float(input('Enter the cash out amount: '))

            if cashout_amount > 0:

                if cashout_amount > limit_cashout:
                    print('It is not possible to withdraw amounts above R$500.00.')
                elif limit_qtde == 0:
                    print('You have reached your daily withdrawal limit.')
                elif cashout_amount > updated_balance:
                    print(f'You do not have enough balance. Current: R${updated_balance:.2f}.')
                else:
                    limit_qtde -= 1
                    updated_balance -= cashout_amount
                    cashouts.append(cashout_amount)
                    print(f'Cash out: R${cashout_amount:.2f}. Balance: R${updated_balance:.2f}.')
            else:
                print('Enter only positive values.')

        elif options == 2:
            deposit_amount = float(input('Enter the deposit amount: '))

            if deposit_amount > 0:
                deposits.append(deposit_amount)
                updated_balance += deposit_amount
                print(f'Deposit: R${deposit_amount:.2f}. Updated balance: R${updated_balance:.2f}.')
            else:
                print('Enter only positive values.')

        elif options == 3:
            print('\n*** EXTRACT: ***')
            
            print('Deposits:')
            if deposits:
                for i1 in deposits:
                    print(f'R${i1:.2f}')
            else:
                print('No deposit made.')
            
            print('Saques:')
            if cashouts:
                for i2 in cashouts:
                    print(f'R${i2:.2f}')
            else:
                print('No deposit made.')
            
            print(f'Balance: R${updated_balance:.2f}')

        elif options == 5:
            print('### DEVELOPER DATA ###')
            print('Developed by: Edson Copque\n'
                  'Site: https://linktr.ee/edsoncopque\n'
                  'GitHub: https://github.com/ecopque\n'
                  'Repo: https://github.com/ecopque/new_banking_system\n'
                  'Signal Messenger: ecop.01\n')

        elif options == 4:
            print('Thank you for being our customer. Leaving...')
            break
        
        else:
            print('Please enter a valid number.')

    except ValueError:
        print(f'Please enter a valid input.')


'''
. Developer: Edson Copque
. Website: https://linktr.ee/edsoncopque
. GitHub: https://github.com/ecopque
. Signal Messenger: ecop.01
'''