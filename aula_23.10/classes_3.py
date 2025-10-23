import os
from dataclasses import dataclass
os.system("cls")



@dataclass 

class Pessoa: 
    nome: str
    idade: int
    peso: float
    altura: float

print("Solicitando os dados da pessoa")
pessoa1 = Pessoa(nome=input("Digite seu nome: "),
                idade=int(input("Digite sua idade: ")),
                peso=float(input("Digite seu peso: ")), 
                altura=float(input("Digite sua altura: ")))



print("===Exibindo dados da Pessoa===") 
print("")
print(f"\nNome: {pessoa1.nome} \n Idade: {pessoa1.idade} anos\n Peso: {pessoa1.peso} KG\n  Altura: {pessoa1.altura} m")