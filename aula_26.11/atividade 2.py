import os
from dataclasses import dataclass 
os.system("cls")

QNT_FUNCIONARIO = 1
QNT_CLIENTE = 1


@dataclass 
class Funcionario:
    nome: str
    data_admissao: str
    matricula: str
    endereco_funcionario: str
    def exibir_dados_funcionario(self):
        print(f"""
=====Exibindo dados====\n
              
Nome: {self.nome}      
data de admissão: {self.data_admissao}
matrícula: {self.matricula}
Endereço: {self.endereco_funcionario}     
              
              
""")

@dataclass
class Cliente:
    nome: str
    data_nasc: str
    endereco: str
    def exibir_dados_cliente(self): 
        print(f"""
==== Exibindo dados do cliente ===
              
Nome: {self.nome}
data de nascimento: {self.data_nasc}
Endereço: {self.endereco}


""")

lista_funcionario = []
lista_cliente = []

for i in range(QNT_FUNCIONARIO):
    funcionario=Funcionario(nome=(input(f"digite o nome do {i+1}º funcionário: ")),
                data_admissao=(input(f"Digite a data de admissão do {i+1}º funcionário: ")),
                matricula=(input(f"Digite a matrícula do {i+1}º funcionário: ")),
                endereco_funcionario=(input(f"Digite o endereço do {i+1}º funcionário: ")))
    lista_funcionario.append(funcionario)
    print("Funcionário Salvo!!!")
    os.system("cls")

for i in range(QNT_CLIENTE):
    cliente= Cliente(nome=(input(f"Digite o nome do {i+1}º cliente: ")),
    data_nasc=(input(f"Digite a data de nascimento do {i+1}º cliente: ")), 
    endereco=(input(f"Digite o endereço do {i+1}º cliente: ")))
    lista_cliente.append(cliente)  
    print()


arqv_funcionario = "Funcionários.csv"

with open(arqv_funcionario, "a", encoding="uft-8") as arquivos_funcionarios:
    for funcionario in lista_funcionario: 
        arquivos_funcionarios.write(f"""

=====Exibindo dados====
              
Nome: {funcionario.nome}      
data de admissão: {funcionario.data_admissao}
matrícula: {funcionario.matricula}
Endereço: {funcionario.endereco_funcionario}    



""")
        



arqv_cliente = "Clientes.csv"

with open(arqv_cliente, "a", encoding="uft-8") as arquivo_clientes:
    for cliente in lista_cliente:
    
        arquivo_clientes.write(f"""
==== Exibindo dados do cliente ===
              
Nome: {cliente.nome}
data de nascimento: {cliente.data_nasc}
Endereço: {cliente.endereco}

""")
print("Salvo com sucesso!")


try: 
    with open(arquivos_funcionarios, "r", encoding="uft-8"):
        lista_funcionario = arquivos_funcionarios.readlines()
        for funcionario in lista_funcionario:
            funcionario.exibir_dados()
            print()
            print()
    with open(arquivo_clientes, "r", encoding="uft-8"):
        lista_funcionario = arquivo_clientes.readlines()
        cliente.exibir_dados.clientes
    


except FileNotFoundError:
    print("Erro, arquivo não encontrado")