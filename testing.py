# FILE: /testing.py

#OK: 1. O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

usuarios = list()

def criar_usuario(*, nome, nascimento, cpf: str, endereco: str):
    for i1 in usuarios:
        if i1['cpf'] == cpf:
            print('Erro: CPF já cadastrado.')
            return None

    usuario = {
        'nome': nome,
        'nascimento': nascimento,
        'cpf': cpf,
        'endereco': endereco
    }

    usuarios.append(usuario)
    print(f'Usuário {usuario['nome']} cadastrado com sucesso.')
    return usuario

#OK: 2. O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

contas = list()

def criar_conta(usuario):
    ...

    numero_conta = (len(contas) + 1)

    conta = {
        'agencia': '0001',
        'numero_conta': numero_conta,
        'usuario': usuario
    }

    contas.append(conta)
    print(f'Cadas registrada: {usuario['']}')
