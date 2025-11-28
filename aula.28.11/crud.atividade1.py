import os
import time
from dataclasses import dataclass
os.system("cls || clear")

lista_clientes = []

@dataclass

class Cliente:

    # Atributos da classe.
    # Atributos são variáveis que pertecem à classe.
    nome: str
    email: str
    telefone:str

    # Métoto para mostrar as informações dos clientes.
    # Método é o nome dado a uma função que pertecence à classe
    def mostrar_dados(self):
        print(f"Nome: {self.nome}  \nEmail: {self.email} \nTelefone: {self.telefone}")


# Função para verificar se a lista está vazia.

def lista_esta_vazia(lista_clientes):
    if not lista_clientes:
       print("\nnão há clientes cadastrados.")
       return True
    
    return False

def adicionar_cliente(lista_clientes):
    print("\n--- Adicionar novo Cliente ---")
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    telefone = input("Digite seu telefone: ")

    novo_cliente = Cliente(nome=nome, email=email,telefone=telefone)
    lista_clientes.append(novo_cliente)
    print(f"\n Cliente {email} adicionado com sucesso")

    # Função para encontrar um cliente na lista. 

def encontrar_cliente_por_email(lista_clientes, email_buscar):
    email_buscar_Lower = email_buscar.lower()
    for cliente in lista_clientes:
        if cliente.email.lower() == email_buscar_Lower:
            return cliente
    return None # None sigifica retornar vzoo sem conteúdo.

def mostrar_todos_clientes(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
    
    print("\n--- Lista de clientes ---")

    for cliente in lista_clientes:
        print(f"{cliente.mostrar_dados()}")


def atualizar_clientes(lista_clientes):
    if lista_esta_vazia(lista_clientes):
            return
        

    # Mostrar a lista de cliente para ajudar o usuario.

    mostrar_todos_clientes(lista_clientes)
    print("--- Atualizar dados do cliente --- ")
    email_buscar = input("\n Digite o email do cliente: ")
    cliente_para_atualizar = encontrar_cliente_por_email(lista_clientes, email_buscar)

    if cliente_para_atualizar:
        print("\n Pessoa encontrada.")
        print("\nDigite os novos dados ou deixe em branco para manter o valor atual.")


        print(f"\nNome atual: {cliente_para_atualizar.nome}")
        novo_nome = input("Novo nome: ")

        print(f"\nE-mail atual: {cliente_para_atualizar.email}")
        novo_email = input("Novo e-mail: ")

        print(f"\nTelefone atual: {cliente_para_atualizar.telefone}")
        novo_telefone = input("Novo telefone: ")

        if novo_nome:
            cliente_para_atualizar.nome = novo_nome
        if novo_email:
            cliente_para_atualizar.email = novo_email

        if novo_telefone:
            cliente_para_atualizar.telefone = novo_telefone

        print(f"\nDados do cliente: {email_buscar} atualizados com sucesso!")
    else:
        print(f"\nCliente com e-mail: {email_buscar} não encontrado")

# função para excluir um cliente.
def excluir_cliente(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
    
    mostrar_todos_clientes(lista_clientes)

    email_buscar = input("\nDigite o nome do cliente que deseja excluir: ")

    cliente_para_remover = encontrar_cliente_por_email(lista_clientes, email_buscar)

    if cliente_para_remover:
        lista_clientes.remove(cliente_para_remover)
        print(f"\n Cliente com o E-mail {email_buscar} encontrado!")
    else:
        print(f"\nCliente com o E-mail {email_buscar} não encontrado.")

# Mostrando menu.
while True:
        print("""
---- Gerenciador de Clientes ---
1 - Adicionar
2 - Mostrar todos
3 - Atualizar
4 - excluir
0 - sair
          
          
          
""")
    
    
        try: 
            opcao = int(input("Digite uma das opções acima: "))
        except ValueError:
            print("\nEntrada inválida. Digite um número...")

            time.sleep(2)
            os.system("cls || clear")
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
                print("\nSaindo do programa...")
            case _:
                print('\nOpção inválida. \nTente novamente.')

        # Pausa antes de mudar o menu.
        if opcao !=  1 and opcao != 0:
            print("carregando...")
            time.sleep(4)
        elif opcao == 1:
            time.sleep(1)

        if opcao != 0:
            os.system("cls || clear")