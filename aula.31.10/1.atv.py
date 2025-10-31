import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Endereco:
    logradouro: str
    numero: str

@dataclass
class Pessoa:
    nome: str
    idade: int
    endereco: Endereco
    def mostrar_dados(self):
        print(f"aqui o nome: {self.nome}")
        print(f"Aqui seu endereço: {self.endereco}")
    

dados_pessoa = Pessoa(nome= input(f"Digite seu nome: "), idade = int(input("Digite sua idade"),
                                                                      endereco=Endereco(
                       logradouro=input("Dgitie seu logradouro: "),
                       numero=int(input("Digite o número: ")))))
