import os
import time
from dataclasses import dataclass

os.system('cls')

lista_clientes = []
lista_produtos = []


@dataclass
class Produto:
    nome: str
    quantidade: str
    lote: str
    validade: str

    def mostrar_dados(self):
        print("\n--- Produto --- ")
        print(f"Nome: {self.nome}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Lote: {self.lote}")
        print(f"Validade: {self.validade}")

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str
    endereco: str

    def mostrar_dados(self):
        print("\n--- Cliente --- ")
        print(f'Nome: {self.nome}')
        print(f'E-mail: {self.email}')
        print(f'Telefone: {self.telefone}')
        print(f"Endereço: {self.endereco}")



def lista_esta_vazia(lista, tipo_item):
    if not lista:
        print(f'\nNão há {tipo_item} cadastrados.')
        return True
    return False

def encontrar_cliente_por_nome(lista_clientes, nome_buscar):
    for cliente in lista_clientes:
        if cliente.nome.lower() == nome_buscar.lower():
            return cliente
    return None

def encontrar_produto_por_nome(lista_produtos, nome_buscar):
    for produto in lista_produtos:
        if produto.nome.lower() == nome_buscar.lower():
            return produto
    return None

def adicionar_clientes(lista_clientes):
    print('\n------ Adicionar novo Cliente -----')
    nome = input('Nome: ')
    email = input('E-mail: ')
    telefone = input('Telefone: ')
    endereco = input('Endereço: ')

    novo_cliente = Cliente(nome, email, telefone, endereco)
    lista_clientes.append(novo_cliente)

    print(f'\nCliente {nome} adicionado com sucesso!')

def mostrar_todos_clientes(lista_clientes):
    if lista_esta_vazia(lista_clientes, "Clientes"):
        return
    print('\n---- Lista de Clientes ----')
    for cliente in lista_clientes:
        cliente.mostrar_dados()

def atualizar_cliente(lista_clientes):
    if lista_esta_vazia(lista_clientes, "Clientes"):
        return

    mostrar_todos_clientes(lista_clientes)

    print('\n----- Atualizar dados do Cliente -----')
    # Busca pelo nome,  função encontra usa o nome
    nome_buscar = input('Digite o NOME do cliente para editar: ')
    cliente = encontrar_cliente_por_nome(lista_clientes, nome_buscar)

    if cliente:
        print('\nCliente encontrado. Deixe em branco para manter o valor atual.\n')

        print(f'Nome atual: {cliente.nome}')
        novo_nome = input('Novo nome: ')
        
        print(f'Email atual: {cliente.email}')
        novo_email = input('Novo Email: ')

        print(f'Telefone atual: {cliente.telefone}')
        novo_telefone = input('Novo Telefone: ')

        print(f'Endereço atual: {cliente.endereco}')
        novo_endereco = input('Novo Endereço: ')

        if novo_nome: cliente.nome = novo_nome
        if novo_email: cliente.email = novo_email
        if novo_telefone: cliente.telefone = novo_telefone
        if novo_endereco: cliente.endereco = novo_endereco

        print('\nDados atualizados com sucesso!')
    else:
        print(f'\nCliente "{nome_buscar}" não encontrado.')

def excluir_cliente(lista_clientes):
    if lista_esta_vazia(lista_clientes, "Clientes"):
        return

    mostrar_todos_clientes(lista_clientes)

    nome_buscar = input('\nDigite o NOME do cliente que deseja excluir: ')
    cliente = encontrar_cliente_por_nome(lista_clientes, nome_buscar)

    if cliente:
        lista_clientes.remove(cliente)
        print(f'\nCliente {cliente.nome} excluído com sucesso!')
    else:
        print('\nCliente não encontrado.')

# --- FUNÇÕES PRODUTOS ---

def adicionar_produtos(lista_produtos):
    print('\n------ Adicionar novo Produto -----')
    nome = input('Nome: ')
    quantidade = input('Quantidade: ')
    lote = input('Lote: ')
    validade = input('Validade: ')

    novo_produto = Produto(nome, quantidade, lote, validade)
    lista_produtos.append(novo_produto)

    print(f'\nProduto {nome} adicionado com sucesso!')

def mostrar_todos_produtos(lista_produtos):
    if lista_esta_vazia(lista_produtos, "Produtos"):
        return
    print('\n---- Lista de Produtos ----')
    for produto in lista_produtos:
        produto.mostrar_dados()

def atualizar_produto(lista_produtos):
    if lista_esta_vazia(lista_produtos, "Produtos"):
        return
    
    mostrar_todos_produtos(lista_produtos)
    
    print('\n----- Atualizar dados do Produto -----')
    nome_buscar = input('Digite o NOME do produto para editar: ')
    produto = encontrar_produto_por_nome(lista_produtos, nome_buscar)

    if produto:
        print('\nProduto encontrado. Deixe em branco para manter o valor atual.\n')

        print(f'Nome atual: {produto.nome}')
        novo_nome = input('Novo nome: ')

        print(f'Quantidade atual: {produto.quantidade}')
        nova_qtde = input('Nova Quantidade: ')

        print(f'Lote atual: {produto.lote}')
        novo_lote = input('Novo Lote: ')

        print(f'Validade atual: {produto.validade}')
        nova_validade = input('Nova Validade: ')

        if novo_nome: produto.nome = novo_nome
        if nova_qtde: produto.quantidade = nova_qtde
        if novo_lote: produto.lote = novo_lote
        if nova_validade: produto.validade = nova_validade

        print('\nProduto atualizado com sucesso!')
    else:
        print(f'\nProduto "{nome_buscar}" não encontrado.')

def excluir_produto(lista_produtos):
    if lista_esta_vazia(lista_produtos, "Produtos"):
        return

    mostrar_todos_produtos(lista_produtos)

    nome_buscar = input('\nDigite o NOME do produto que deseja excluir: ')
    produto = encontrar_produto_por_nome(lista_produtos, nome_buscar)

    if produto:
        lista_produtos.remove(produto)
        print(f'\nProduto {produto.nome} excluído com sucesso!')
    else:
        print('\nProduto não encontrado.')

# --- MENU PRINCIPAL ---
while True:
    print("""
---- SISTEMA DE GERENCIAMENTO ----

    CLIENTES:           PRODUTOS:
    1 - Adicionar       5 - Adicionar
    2 - Mostrar Todos   6 - Mostrar Todos
    3 - Atualizar       7 - Atualizar
    4 - Excluir         8 - Excluir
    
    0 - SAIR
""")

    try:
        opcao = int(input('Digite uma opção: '))
    except ValueError:
        print('\nEntrada inválida. Digite um número.')
        time.sleep(1)
        os.system('cls')
        continue

    match opcao:
        # Clientes
        case 1:
            adicionar_clientes(lista_clientes)
        case 2:
            mostrar_todos_clientes(lista_clientes)
        case 3:
            atualizar_cliente(lista_clientes)
        case 4:
            excluir_cliente(lista_clientes)
        
        # Produtos
        case 5:
            adicionar_produtos(lista_produtos)
        case 6:
            mostrar_todos_produtos(lista_produtos)
        case 7:
            atualizar_produto(lista_produtos)
        case 8:
            excluir_produto(lista_produtos)

        # Sair
        case 0:
            print('\nSaindo do programa...')
            break
        case _:
            print('\nOpção inválida!')

    if opcao != 0:
        input('\nPressione ENTER para continuar...')
        os.system('cls')