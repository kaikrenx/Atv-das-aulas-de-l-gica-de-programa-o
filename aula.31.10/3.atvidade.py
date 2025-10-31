import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Aluno:
    nome: str
    idade: int
    email: str
    telefone: float

QUANTIDADE_ALUNOS = 2
lista_alunos = []

print("Solicitando dados do aluno.")
for i in range(QUANTIDADE_ALUNOS):
    os.system("cls")
    aluno = Aluno(
        nome=input("Digite seu nome: "),
        idade=input("Digite sua idade: "),
        email=input("Digite seu e-mail: "),
        telefone=(input("Digite seu telefone: ")))

    lista_alunos.append(aluno)

print()
print("Salvando dados.")
arquivo = "dados_alunos.txt"

with open(arquivo, "a") as arquivo_alunos:
    for aluno in lista_alunos:
        arquivo_alunos.write(f"\n ===Dados do Aluno ===\n Nome: {aluno.nome}\nIdade: {aluno.idade}\nE-mail: {aluno.email}\nTelefone: {aluno.telefone}\n")
        print("Salvo com sucesso!")
