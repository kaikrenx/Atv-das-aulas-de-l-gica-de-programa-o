import os
from dataclasses import dataclass


@dataclass
class Pessoa:

    nome: str
    idade: float
    peso: float
    altura: float

    def mostrar_dados(self):
        print(f"== Dados da {i+1}° Pessoa ==")
        print(f"Nome da pessoa: {self.nome}")
        print(f"Idade da pessoa: {self.idade} anos")
        print(f"Peso da pessoa: {self.peso} kg")
        print(f"Altura da pessoa: {self.altura} metros")


lista_pessoas = []
pessoas = 3

for i in range(pessoas):
    dados_pessoa = Pessoa(input(f"Digite o nome da {i+1}º pessoa: "),
                          idade=(input(f"Digite a idade da {i+1}° pessoa: ")),
                          peso=(input(f"Digite o peso da {i+1}° pessoa: ")),
                          altura=(input(f"Digite a altura da {i+1}° Pessoa: ")))
    os.system("cls")
    lista_pessoas.append(dados_pessoa)

for dados_pessoas in lista_pessoas:
    Pessoa.mostrar_dados()
