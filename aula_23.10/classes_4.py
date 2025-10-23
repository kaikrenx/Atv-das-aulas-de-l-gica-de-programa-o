import os
from dataclasses import dataclass
os.system("cls")



@dataclass 

class Pessoa: 
    nome: str
    email: str
    telefone: float
    endereço: str

    def mostrar_dados(self):
        print("===Exibindo dados da Pessoa===") 
        print("")
        print(f"\nNome: {self.nome} \n Email: {self.email} \n telefone: {self.telefone} \n  endereço: {self.endereço} ")





print("Solicitando os dados da pessoa")
pessoa1 = Pessoa(nome=input("Digite seu nome: "),
                email=str(input("Digite seu email: ")),
                telefone=str(input("Digite seu telefone: ")), 
                endereço=str(input("Digite seu endereço: ")))



pessoa1.mostrar_dados()