import os
import time
from dataclasses import dataclass
os.system("cls")


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
    print(f"\n Cliente {nome} adicionado com sucesso")

    # Função para encontrar um cliente na lista. 

def encontrar_cliente_por_nome(lista_clientes, nome_buscar):
    nome_buscar_Lower = nome_buscar.lower()
    for cliente in lista_clientes:
        if cliente.nome.lower() == nome_buscar_Lower:
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
        print("--- Atualizaar dados do cliente --- ")
        nome_buscar = input("\n Digite o nome do cliente: ")
        cliente_para_atualizar = encontrar_cliente_por_nome(lista_clientes, nome_buscar)

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

            print(f"\nDados do cliente: {nome_buscar} atualizados com sucesso!")
        else:
            print(f"\nCliente com nome: {nome_buscar} não encontrado")


