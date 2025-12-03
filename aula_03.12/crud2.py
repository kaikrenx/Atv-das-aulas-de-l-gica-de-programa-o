import os
import time
from dataclasses import dataclass

os.system('cls || clear')  # Limpar terminal

lista_funcionarios = []


@dataclass
class Funcionario:
    nome: str
    nascimento: str
    cpf: str
    funcao: str

    def mostrar_dados(self):
        print(f'\nNome: {self.nome}')
        print(f'Data de Nascimento: {self.nascimento}')
        print(f'CPF: {self.cpf}')
        print(f'Função: {self.funcao}')


# Verificar se a lista está vazia
def lista_esta_vazia(lista_funcionarios):
    if not lista_funcionarios:
        print('\nNão há funcionários cadastrados.')
        return True
    return False


# Adicionar funcionário
def adicionar_funcionarios(lista_funcionarios):
    print('\n------ Adicionar novo funcionário -----')
    nome = input('Nome: ')
    nascimento = input('Data de Nascimento: ')
    cpf = input('CPF: ')
    funcao = input('Cargo: ')

    novo_funcionario = Funcionario(nome, nascimento, cpf, funcao)
    lista_funcionarios.append(novo_funcionario)

    print(f'\nFuncionário {nome} adicionado com sucesso!')


# Encontrar funcionário por CPF
def encontrar_por_cpf(lista_funcionarios, cpf_buscar):
    for funcionario in lista_funcionarios:
        if funcionario.cpf.lower() == cpf_buscar.lower():
            return funcionario
    return None


# Mostrar todos os funcionários
def mostrar_todos_funcionarios(lista_funcionarios):
    if lista_esta_vazia(lista_funcionarios):
        return

    print('\n---- Lista de Funcionários ----')
    for funcionario in lista_funcionarios:
        funcionario.mostrar_dados()


# Atualizar funcionário
def atualizar_funcionarios(lista_funcionarios):
    if lista_esta_vazia(lista_funcionarios):
        return

    mostrar_todos_funcionarios(lista_funcionarios)

    print('\n----- Atualizar dados do funcionário -----')
    cpf_buscar = input('Digite o CPF do funcionário: ')
    funcionario = encontrar_por_cpf(lista_funcionarios, cpf_buscar)

    if funcionario:
        print('\nFuncionário encontrado. Deixe em branco para manter o valor atual.\n')

        print(f'CPF atual: {funcionario.cpf}')
        novo_cpf = input('Novo CPF: ')

        print(f'Nome atual: {funcionario.nome}')
        novo_nome = input('Novo nome: ')

        print(f'Nascimento atual: {funcionario.nascimento}')
        novo_nascimento = input('Nova data de nascimento: ')

        print(f'Função atual: {funcionario.funcao}')
        nova_funcao = input('Nova função: ')

        if novo_cpf:
            funcionario.cpf = novo_cpf
        if novo_nome:
            funcionario.nome = novo_nome
        if novo_nascimento:
            funcionario.nascimento = novo_nascimento
        if nova_funcao:
            funcionario.funcao = nova_funcao

        print('\nDados atualizados com sucesso!')

    else:
        print(f'\nCPF {cpf_buscar} não encontrado.')


# Excluir funcionário
def excluir_funcionario(lista_funcionarios):
    if lista_esta_vazia(lista_funcionarios):
        return

    mostrar_todos_funcionarios(lista_funcionarios)

    cpf_buscar = input('\nDigite o CPF do funcionário que deseja excluir: ')
    funcionario = encontrar_por_cpf(lista_funcionarios, cpf_buscar)

    if funcionario:
        lista_funcionarios.remove(funcionario)
        print(f'\nFuncionário {funcionario.nome} excluído com sucesso!')
    else:
        print('\nFuncionário não encontrado.')


# MENU PRINCIPAL
while True:
    print("""
---- Gerenciador de Funcionários ----
1 - Adicionar
2 - Mostrar todos
3 - Atualizar
4 - Excluir
0 - Sair
""")

    try:
        opcao = int(input('Digite uma opção: '))
    except ValueError:
        print('\nEntrada inválida. Digite um número.')
        time.sleep(2)
        os.system('cls || clear')
        continue

    match opcao:
        case 1:
            adicionar_funcionarios(lista_funcionarios)
        case 2:
            mostrar_todos_funcionarios(lista_funcionarios)
        case 3:
            atualizar_funcionarios(lista_funcionarios)
        case 4:
            excluir_funcionario(lista_funcionarios)
        case 0:
            print('\nSaindo do programa...')
            break
        case _:
            print('\nOpção inválida!')

    if opcao != 0:
        time.sleep(2)
        os.system('cls || clear')