import os
from dataclasses import dataclass
os.system("cls")



@dataclass
class Pessoa:
    nome: str
    cpf: str
    telefone: str

    def dados(self):
        os.system("cls")
        print("=== Dados abaixo ===")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")

    def dados_marketing(self):
      
        print("=== Dados abaixo para marketing ===")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")

   
lista_pessoas = []
pessoas = 3

for i in range(pessoas):
    dados_pessoa = Pessoa(nome=input("Digite seu nome: "),
                   cpf=input("Digite seu cpf: "),
                   telefone=input("Digite seu telefone: "))
    os.system("cls")
    lista_pessoas.append(dados_pessoa)



for Pessoa in lista_pessoas:
    Pessoa.dados_marketing()



   