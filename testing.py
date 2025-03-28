# FILE: /testing.py

# OK: 1. O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

users = list()
def create_user(name, birth, cpf: str, address: str):
    cpf_exists = False
    for i1 in users:
        if i1['cpf'] == cpf:
            print('User already exists.')
            cpf_exists = True
            break
        
    if not cpf_exists:
        new_user = {
            'name': name,
            'birth': birth,
            'cpf': cpf,
            'address': address
        }
    
    users.append(new_user)
    print(f'User {name} created.')
    return

# def create_current_account():
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