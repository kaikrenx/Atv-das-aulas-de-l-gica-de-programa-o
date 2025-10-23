import os
from dataclasses import dataclass
os.system("cls")



@dataclass 

class Pessoa: 
    nome: str
    idade: int
    peso: float
    altura: float


pessoa1 = Pessoa(nome="Julia" ,idade=12 ,peso=67.2 , altura=1.72 )



print("===Exibindo dados da Pessoa===") 
print("")
print(f"\nNome: {pessoa1.nome} \n Idade: {pessoa1.idade} anos\n Peso: {pessoa1.peso} KG\n  Altura: {pessoa1.altura} m")