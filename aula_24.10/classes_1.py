import os
from dataclasses import dataclass

os.system("cls")

# Criando uma classe.
@dataclass
class Cliente:
    nome: str
    endereco: str


# Criando dois clientes com as características
# definidas na classe.
cliente1 = Cliente(nome="Marta", endereco="Rua A.")
cliente2 = Cliente(nome="João", endereco="Rua C.")

print("\n") # Deixando uma linha vazia.
print("Mostrando apenas os nomes dos clientes.")
print(f"Nome: {cliente1.nome}")
print(f"Nome: {cliente2.nome}")

print("\n") # Deixando uma linha vazia.
print("Mostrando apenas os endereços dos clientes.")
print(f"Endereço: {cliente1.endereco}")
print(f"Endereço: {cliente2.endereco}")

print("\n") # Deixando uma linha vazia.
print("Mostrando todos os dados dos clientes.")
print(f"Nome: {cliente1.nome}")
print(f"Endereço: {cliente1.endereco}\n")
print(f"Nome: {cliente2.nome}")
print(f"Endereço: {cliente2.endereco}\n")