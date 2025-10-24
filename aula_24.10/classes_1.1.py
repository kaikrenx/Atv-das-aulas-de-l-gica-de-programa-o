from dataclasses import dataclass
import os
os.system("cls")

# Criando uma classe.

# Cliente é uma pessoa?
# CPF? Endereço? Nome? Título de eleitor? E-mail? Telefone?
# Seu sistema precisa de algumas informações.
# Uma venda.
# Endereço, nome, telefone. (Mini-mundo)

@dataclass
class Cliente:
    nome: str
    endereco: str
    telefone: str

    # Função apenas desta classe.
    def mostrar_dados_cliente(self):
        print(f"\nNome: {self.nome}")
        print(f"Endereço: {self.endereco}")
        print(f"Telefone: {self.telefone}\n")


# Criando dois clientes com as características
# definidas na classe.

# Vetor.
lista_de_clientes = []

for i in range(3):
    dados_cliente = Cliente(nome=input("Digite seu nome: "),
                   endereco=input("Digite seu endereço: "),
                   telefone=input("Digite seu telefone: "))
    lista_de_clientes.append(dados_cliente)
    os.system("cls")

# Mostrando os dados do cliente.
for cliente in lista_de_clientes:
    # Posição: 0, 1, 2
    cliente.mostrar_dados_cliente()