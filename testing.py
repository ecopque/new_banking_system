# FILE: /testing.py

users = list()
def create_users(name, birth, cpf: str, address: str):
    for i1 in users:
        if i1['cpf'] == cpf:
            print('CPF already exists.')
            break
        
        else:
            new_user = {
                'name': name,
                'birth': birth,
                'cpf': cpf,
                'address': address
            }

            users.append(new_user)
            print(f'User {name} created successfully.')