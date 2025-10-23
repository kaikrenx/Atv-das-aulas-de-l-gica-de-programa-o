import os
from dataclasses import dataclass
os.system("cls")



@dataclass 

class Pessoa: 
    nome: str
    idade: int
    def mostrar_dados(self):
        print("===Exibindo dados da Pessoa===") 
        print("")
        print(f"\nNome: {self.nome}")
        print(f"Idade: {self.idade}")
              

print("Solicitando os dados da pessoa")

pessoa1 = Pessoa(nome=input("Digite seu nome: "),
                        idade=int(input("Digire sua idade:")))

pessoa2 = Pessoa(nome=input("Digite seu nome: "),
                        idade=int(input("Digire sua idade:")))


pessoa1.mostrar_dados()
pessoa2.mostrar_dados()