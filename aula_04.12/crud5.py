import os
import time
from dataclasses import dataclass

os.system('cls') 

lista_clientes = []

@dataclass
class Produto:
    Nome: str
    quantidade: str
    lote: str
    validade: str

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str
    telefone: str
    produto: Produtoimp
    def mostrar_dados(self):
        print(f'\nNome: {self.nome}')
        print(f'E-mail: {self.email}')
        print(f'Telefone: {self.telefone}')
    
def lista_esta_vazia(lista_clientes):
    if not lista_clientes:
        print('\nNão há clientes cadastrados.')
        return True
    return False

def adicionar_aluno(lista_clientes):
    print('\n--------- Adicionar novo Cliente ---------')
   
    nome = input('Nome: ')
    email = input('Data de Nascimento: ')
    telefone = input('Telefone: ')
   
    
    print('--- Dados do Produto ---')
    Nome = input('nome: ')
    quantidade = input('quantidade: ')
    lote = input('lote: ')
    validade = input('validade: ')

   
    novo_endereco = Produto(Nome, quantidade, lote, validade)
    
    novo_aluno = Cliente(nome, email, telefone, novo_endereco)
    
    lista_clientes.append(novo_aluno)
    print(f'\nCliente {nome} adicionado com sucesso!')


def encontrar_por_ra(lista_clientes, nome_buscar):
    for cliente in lista_clientes:
        if cliente.telefone.lower() == nome_buscar.lower():
            return cliente
    return None

def mostrar_todos_alunos(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return

    print('\n---- Lista de Clientes ----')
    for cliente in lista_clientes:
        cliente.mostrar_dados()


def atualizar_aluno(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return

    mostrar_todos_alunos(lista_clientes)

    print('\n----- Atualizar dados do Cliente -----')
    nome_buscar = input('Digite o Telefone do cliente: ')
    cliente = encontrar_por_ra(lista_clientes, nome_buscar)

    if cliente:
        print('\nCliente encontrado. Deixe em branco para manter o valor atual.\n')

       
        print(f'Nome atual: {cliente.nome}')
        novo_nome = input('Novo nome: ')
        
        print(f'Nascimento atual: {cliente.email}')
        novo_email = input('Nova data de email: ')
        
        print(f'nome atual: {cliente.Produto.Nome}')
        novo_logradouro = input('Novo Nome: ')

        print(f'quantidade atual: {cliente.Produto.quantidade}')
        novo_numero = input('Novo número: ')
        
        print(f'lote atual: {cliente.Produto.lote}')
        nova_cidade = input('Nova lote: ')
        
        print(f'validade atual: {cliente.Produto.validade}')
        novo_estado = input('Novo validade: ')

        if novo_nome: cliente.nome = novo_nome
        if novo_email: cliente.email = novo_email
        if novo_curso: cliente.telefone = novo_telefone
        
        if novo_logradouro: cliente.Produto.Nome = novo_logradouro
        if novo_numero: cliente.Produto.quantidade = novo_numero
        if nova_cidade: cliente.Produto.lote = nova_cidade
        if novo_estado: cliente.Produto.validade = novo_estado

        print('\nDados atualizados com sucesso!')

    else:
        print(f'\nR.A {nome_buscar} não encontrado.')

# Excluir cliente
def excluir_aluno(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return

    mostrar_todos_alunos(lista_clientes)

    nome_buscar = input('\nDigite o Telefone do cliente que deseja excluir: ')
    cliente = encontrar_por_ra(lista_clientes, nome_buscar)

    if cliente:
        lista_clientes.remove(cliente)
        print(f'\nCliente {cliente.nome} excluído com sucesso!')
    else:
        print('\nCliente não encontrado.')

while True:
    print("""
---- Gerenciador de Clientes ----
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
        os.system('cls')
        continue

    match opcao:
        case 1:
            adicionar_aluno(lista_clientes)
        case 2:
            mostrar_todos_alunos(lista_clientes)
        case 3:
            atualizar_aluno(lista_clientes)
        case 4:
            excluir_aluno(lista_clientes)
        case 0:
            print('\nSaindo do programa...')
            break
        case _:
            print('\nOpção inválida!')

    if opcao != 0:
        time.sleep(2)
        os.system('cls')