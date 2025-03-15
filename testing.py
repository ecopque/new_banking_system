# FILE: /testing.py

users = list()
def create_users(name, birth, cpf: str, address: str):
    cpf_exists = False
    for i1 in users:
        if i1['cpf'] == cpf:
            cpf_exists = True
            print('CPF already exists.')
            break
    
    if not cpf_exists:
        new_users = {
            'name': name,
            'birth': birth,
            'cpf': cpf,
            'address': address
        }

        users.append(new_users)
        print(f'User {name} created.')
        