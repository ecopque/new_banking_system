# FILE: /testing.py

#OK: 1. O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

# users = list()
# def create_user(name, birth, cpf: str, address: str):
#     cpf_exists = False
#     for i1 in users:
#         if i1['cpf'] == cpf:
#             print('User already exists.')
#             cpf_exists = True
#             break
        
#     if not cpf_exists:
#         new_user = {
#             'name': name,
#             'birth': birth,
#             'cpf': cpf,
#             'address': address
#         }
    
#     users.append(new_user)
#     print(f'User {name} created.')
#     return

class Animal:
    def __init__(self, patas_animal):
        self.patas = patas_animal  # Atributo da classe Animal

class Mamifero(Animal):
    def __init__(self, patas_mamifero):
        super().__init__(patas_mamifero)  # Chama o construtor da classe Animal

class Cachorro(Mamifero):
    def __init__(self, patas_cachorro, raca):
        super().__init__(patas_cachorro)  # Chama o construtor da classe Mamifero
        self.raca = raca  # Atributo específico da classe Cachorro

# Exemplo de uso
meu_cachorro = Cachorro(patas_cachorro=4, raca="Labrador")
print(f"Patas: {meu_cachorro.patas}, Raça: {meu_cachorro.raca}")