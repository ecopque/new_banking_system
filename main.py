# FILE: /main.py

saldo_conta = 0
limite_saque = 500
qtde_limite = 3

while True:
    try:
        opcao = int(input('Choose one of the options:\n'
                                '[1] - Cash out\n'
                                '[2] - Deposit\n'
                                '[3] - View extract\n'
                                '[4] - Exit\n'
                                '[5] - Info): '))

        if opcao == 1:
            valor_saque = float(input('Informe o valor de saque: '))

            if valor_saque > limite_saque:
                print('Não é possível sacar valores acima de R$500,00.')
            
            elif qtde_limite == 0:
                print('Você atingiu o limite diário de saque.')

            elif valor_saque > saldo_conta:
                print(f'Você não tem saldo em conta. Atual: R${saldo_conta:.2f}')
            
            else:
                qtde_limite -= 1
                saldo_conta -= valor_saque
                print(f'Saque: R${valor_saque:.2f}. Saldo: R${saldo_conta:.2f}')

    except ValueError:
        print(f'Erro!')