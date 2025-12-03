import os 
import time
from dataclasses import dataclass
os.system('cls || clear ') #Limpar terminal


lista_clientes=[]

@dataclass
class Cliente:
    # Atributos da classe.
    # Atributos são variaveis que pertecem a classe.
    nome: str
    email: str
    telefone: str

    # Método para mostrar as informações dos clientes.
    # Método é o nome dado a uma função que pertence a classe.
    
    def mostrar_dados(self):
        print(f'Nome: {self.nome} \nE-mail: {self.email} \nTelefone: {self.telefone}')


# Função para verificar se a lista esta vazia.
def lista_esta_vazia(lista_clientes):
    if not lista_clientes:
        print('\nNão há clientes cadastrados')
        return True
    return False 

# Função para adicionar um novo cliente na lista.

def adicionar_cliente(lista_clientes):
    print('\n ------ Adicionar novo cliente -----')
    nome=input('Digite seu nome:')
    email=input('Digite seu E-mail:')
    telefone=input('Digite seu Telefone:')

    novo_cliente= Cliente(nome=nome, email=email, telefone=telefone)
    lista_clientes.append(novo_cliente)
    print(f'\n Cliente{nome} adicionado com sucesso!')

# Função para encontrar um cliente na lista.
def encontrar_cliente_por_email(lista_clientes, email_buscar):
    email_buscar_lower=email_buscar.lower()
    for cliente in lista_clientes:
        if cliente.email.lower()== email_buscar_lower:
            return cliente
    return None # None significa retornar vazio, sem conteudo.
    
# Função para mostrar todos os clientes.
def mostrar_todos_clientes(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
   
    print('\n---- Lsita de Clientes ----')
    for cliente in lista_clientes:
        cliente.mostrar_dados()

# Função para atualizar clientes.

def atualizar_clientes(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
    
    # Mostrar a lista para ajudar o usuário.
    mostrar_todos_clientes(lista_clientes)
    print('----- Atualizar dados do cliente ----')
    email_buscar=input('\nDigite o E-mail do cliente: ')
    cliente_para_atualizar= encontrar_cliente_por_email(lista_clientes, email_buscar)


    if cliente_para_atualizar:
        print('\nPessoa encontrada.')
        print('\nDigite os novos dados ou deixe em branco para manter o valor atual.')
       
       
        
        print('E-mail atual: {cliente_para_atualizar.email}')
        novo_email=input(f'Novo email:')
        print('Nome atual: {cliente_para_atualizar.nome}')
        novo_nome=input(f'Novo nome: ')
        print('Telefone atual: {cliente_para_atualizar.telefone}')
        novo_telefone=input(f'Novo telefone:')

        if novo_nome:
            cliente_para_atualizar.nome= novo_nome
        if novo_email:
            cliente_para_atualizar.email=novo_email
        if novo_telefone:
            cliente_para_atualizar.telefone=novo_telefone

            print(f'\n Dados do Cliente {email_buscar} atualizado com sucesso!')
        else:
            print(f'\n Cliente com nome: {email_buscar} não encontrado.')

# Função para excluir um cliente.
def excluir_cliente(lista_cliente):
    if lista_esta_vazia(lista_clientes):
        return
    
    mostrar_todos_clientes(lista_cliente)
    email_buscar=input ('\nDigite o E-mail do cliente que deseja excluir: ')
    cliente_para_remover= encontrar_cliente_por_email(lista_clientes, email_buscar)

    if cliente_para_remover:
        lista_clientes.remove(cliente_para_remover)
        print(f'\nCliente {cliente_para_remover.email} excluido com sucesso!')
    else:
        print(f'\nCliente com o nome {email_buscar} não encontrado.')

# Mostrando menu.
while True:
    print("""

---- Gerenciador de Clientes ----
1- Adicionar
2- Mostrar todos
3- Atualizar
4- Excluir
0 - Sair



""")
    try:

        opcao=int(input('Digite uma das opções acima: '))
    except ValueError:
        print('\nEntrada invalida. Digite um número...')
        time.sleep(2)
        os.system('cls || clear ')
        continue

    match opcao:
            case 1:
                adicionar_cliente(lista_clientes)
            case 2:
                mostrar_todos_clientes(lista_clientes)
            case 3:
                atualizar_clientes(lista_clientes)
            case 4:
                excluir_cliente(lista_clientes)
            case 0:
                print('\nSaindo programa...')
                break
            case _:
                print('\nOpção inválida \nTente novamente.')


    if opcao !=1 and opcao !=0:
        time.sleep(3)
    elif opcao == 1:
        time.sleep(1)

        if opcao !=0:
            os.system('cls || clear')