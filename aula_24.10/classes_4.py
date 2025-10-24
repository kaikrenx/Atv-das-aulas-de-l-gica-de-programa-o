import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Endereco:
    logradouro: str
    numero: int
    cidade: str

@dataclass
class Cliente:
    nome: str
    email: str
    endereco: Endereco

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Logradouro: {self.endereco.logradouro}")
        print(f"Número: {self.endereco.numero}")
        print(f"Cidade: {self.endereco.cidade}")

cliente1 = Cliente(nome=input("Digite seu nome: "),
                   email=input("Digite seu e-mail: "),
                   endereco=Endereco(
                       logradouro=input("Dgitie seu logradouro: "),
                       numero=int(input("Digite o número: ")),
                       cidade=input("Digite sua cidade: ")))

print("\nMostrar dados do cliente.")
cliente1.mostrar_dados()