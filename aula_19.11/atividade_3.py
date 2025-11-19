import os
from dataclasses import dataclass
os.system("cls")



@dataclass

class Paciente:
    nome: str
    rg: float
    data_nascimento: float
    cpf: float
    def exibir_dados(self):
        print(f"Nome: {self.nome}\n\n rg: {self.rg}\n\n Data de nascimento: {self.data_nascimento}\n\n CPF: {self.cpf}")

lista_pacientes = []
QUANTIDADE_DE_PACIENTES = 5

for i in range(QUANTIDADE_DE_PACIENTES):
    paciente = Paciente(
        nome= input("Digite seu nome: "),
        rg= int(input("Digite seu RG: ")),
        data_nascimento= float(input("Digite sua data de nascimento: ")),
        cpf= float(input("Digite seu cpf: "))
    )
    lista_pacientes.append(paciente)
    print()

nome_do_arquivo = "dados_paciente.csv"
with open(nome_do_arquivo, "a", encoding="uft-8") as arquivo_pacientes:
    for paciente in lista_pacientes:
        arquivo_pacientes.write(f"{paciente.nome}, {paciente.rg}, {paciente.data_nascimento}, {paciente.cpf}\n")
        print()
        print("Dados salvos com sucesso.")

# print("\nExibindo lista de pacientes: \n")

# for paciente in lista_pacientes:
#     paciente.exibir_dados()

print("\Exibindo todos os pacientes: ")
lista = []
try:
    # "r" - Read - leitura
    with open(nome_do_arquivo, "r", encoding="uft-8") as arquivo:
        lista_todos_pacientes = arquivo.readlines()
        for paciente in lista_todos_pacientes: 
            nome, rg, data_nascimento, cpf = paciente.strip().split(",")
            dados_paciente = Paciente(nome=nome, rg=int(rg), data_nascimento=float(data_nascimento), cpf=float(cpf))
            lista.append(dados_paciente)
    for paciente in lista:
        paciente.exibir_dados()
except FileNotFoundError:

    print("Erro, arquivo não encontrado")