import os
import time 
from dataclasses import dataclass

os.system("cls")

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
        print(f"nome: {self.nome}")
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
        print(f'\nNome: {self.nome}')
        print(f'E-mail: {self.email}')
        print(f'Telefone: {self.telefone}')
        print(f"Endereço: {self.endereco}")

def lista_esta_vazia(lista_clientes):
    if not lista_clientes:
        print("\nNão Há clientes cadastrados")
        return True
    return False

def lista_esta_vazia(lista_produtos):
    if not lista_produtos:
        print("\nNão Há produtos cadastrados")
        return True
    return False


def adicionar_cliente(lista_clientes):
    print('\n--------- Adicionar novo cliente ---------')
    
    nome = input('Nome: ')
    email = input('E-mail: ')
    telefone = input("Telefone:")
    endereco = input("Endereço: ")

    novo_cliente = 

