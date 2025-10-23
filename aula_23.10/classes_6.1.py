import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Pessoa:
    nome: str
    email: str
    logradouro: str

    def dados_entrega(self):
        os.system("cls")
        print("=== Dados abaixo para entrega ===")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")

    def dados_marketing(self):
        os.system("cls")
        print("=== Dados abaixo para marketing ===")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")

    def mostrar_nome(self):
        os.system("cls")
        print(f"O nome do cliente escolhido: {self.nome}")


# === Cadastro de várias pessoas com for ===
pessoas = []
qtd_pessoas = 2  # número de pessoas para cadastrar

for i in range(qtd_pessoas):
    print(f"\n=== Cadastro da Pessoa {i + 1} ===")
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    logradouro = input("Digite seu endereço: ")
    pessoa = Pessoa(nome, email, logradouro)
    pessoas.append(pessoa)

# === Escolher pessoa ===
os.system("cls")
print("=== Pessoas cadastradas ===")
for i in range(qtd_pessoas):
    print(f"{i + 1} - {pessoas[i].nome}")

pessoa_op = input("\nDigite o número da pessoa que deseja ver os dados: ")

if pessoa_op == "1" or pessoa_op == "2":
    indice = int(pessoa_op) - 1
    pessoa_escolhida = pessoas[indice]

    opcao = input("""
=== Digite o que deseja ver === 
1 - Dados de entrega
2 - Dados de marketing
3 - Ver somente o nome do cliente
R: """)

    if opcao == "1":
        pessoa_escolhida.dados_entrega()
    elif opcao == "2":
        pessoa_escolhida.dados_marketing()
    elif opcao == "3":
        pessoa_escolhida.mostrar_nome()
    else:
        os.system("cls")
        print("Opção inválida, tente novamente.")
else:
    os.system("cls")
    print("Pessoa inexistente, tente novamente.")
