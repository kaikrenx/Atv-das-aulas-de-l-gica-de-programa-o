import os
from dataclasses import dataclass
os.system("cls")



@dataclass

class Paciente:
    nome: str
    idade: int
    peso: float
    altura: float
    cpf: float
    def exibir_dados(self):
        print(f"Nome: {self.nome}\n\n Idade: {self.idade}\n\n Peso: {self.peso}KG\n\n Altura: {self.altura}\n\n CPF: {self.cpf}")

lista_pacientes = []
QUANTIDADE_DE_PACIENTES = 2

for i in range(QUANTIDADE_DE_PACIENTES):
    paciente = Paciente(
        nome= input("Digite seu nome: "),
        idade= int(input("Digite sua idade: ")),
        peso= float(input("Digite seu peso ( Ex: 67.2): ")),
        altura= float(input("Digite sua altura( Ex: 56.2): ")),
        cpf= float(input("Digite seu cpf: "))
    )
    lista_pacientes.append(paciente)
    print()

nome_do_arquivo = "dados_paciente.csv"
with open(nome_do_arquivo, "a") as arquivo_pacientes:
    for paciente in lista_pacientes:
        arquivo_pacientes.write(f"{paciente.nome}, {paciente.idade}, {paciente.peso}, {paciente.altura}, {paciente.cpf}\n")
        print()
        print("Dados salvos com sucesso.")

# print("\nExibindo lista de pacientes: \n")

# for paciente in lista_pacientes:
#     paciente.exibir_dados()

print("\Exibindo todos os pacientes: ")
try:
    # "r" - Read - leitura
    with open(nome_do_arquivo, "r") as arquivo:
        lista_todos_pacientes = arquivo.readlines()
        for paciente in lista_todos_pacientes: 
            print(f"- {paciente.strip{}}")
        # linhas = arquivo.readlines()
        # for linha in linhas:
        #     print(f"- {linhas.strip()}")
except FileNotFoundError:
    print("Erro, arquivo não encontrado")