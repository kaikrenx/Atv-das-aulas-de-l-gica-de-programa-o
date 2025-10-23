import os 
from dataclasses import dataclass 
os.system("cls")



@dataclass
class Pessoa:
    nome: str
    idade: int
    cpf: str

@dataclass
class Pet:
    nome: str
    idade: int
    peso: float
x   
# Exemplo de uso da classe 
pessoa1 = Pessoa(nome="Alice",idade= 30,cpf= "234.452.222-22")
pet1 = Pet(nome="Totó",idade= 4, peso=2.100)

print("Exibindo dados da Pessoa")

print(f"Nome: {pessoa1.nome},\n idade: {pessoa1.idade}\n CPF: {pessoa1.cpf}\n")
print(f"Nome: {pet1.nome}, \nidade: {pet1.idade}\n Peso: {pet1.peso}")