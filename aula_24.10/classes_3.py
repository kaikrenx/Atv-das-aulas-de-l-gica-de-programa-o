import os
from dataclasses import dataclass


@dataclass
class Endereco:
    logradouro: str
    numero: int

@dataclass
class Cliente:
    nome: str
    endereco: Endereco


cliente1 = Cliente(nome="Laura",
                   endereco=Endereco(logradouro="Rua A", numero=23))


print("Mostrar dados do cliente.")
print(f"Nome: {cliente1.nome}")
print(f"Endereço: {cliente1.endereco.logradouro}")
print(f"Número: {cliente1.endereco.numero}")