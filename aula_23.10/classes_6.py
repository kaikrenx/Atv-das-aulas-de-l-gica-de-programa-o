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
            print(f"Aqui o nome do sr(a): {self.nome}")
            print(f"O email para contato: {self.email}")

    def dados_emaiL_marketing(self):
            os.system("cls")
            print(f"Aqui o nome do sr(a): {self.nome}")
            print(f"O email para contato: {self.email}")
    def mostrar_somente_nome(self):
            os.system("cls")
            print(f"O nome do cliente escolhido: {self.nome}")
    
pessoa1 = Pessoa(nome=input("Digite seu nome: "),
                        email=str(input("Digite seu email:")),
                        logradouro=str(input("Digite seu endereço: ")))
print("")
pessoa2 = Pessoa(nome=input("Digite seu nome: "),
                        email=str(input("Digite seu email: ")),
                        logradouro=str(input("Digite seu endereço: ")))

pessoa_op = str(input(f"""Digite de quem você quer ver os dados: "

1 - pessoa_1
                      
2 - pessoa_2

R: 
                      
"""))


if pessoa_op == "1":
    os.system("cls")
    opcao = str(input("""
=== Digite o que deseja ver === 

1 - Dados de entrega

2 - Dados de marketing     

3 - Ver somente o nome do cliente

R: 
    """))

    if opcao == "1":
        os.system("cls")
        print("=== dados abaixo para entrega ===")
        pessoa1.dados_entrega()
    elif opcao == "2":
        os.system("cls")
        print("=== dados abaixo para entrega ===")
        pessoa1.dados_emaiL_marketing()
    elif opcao == "3": 
        pessoa1.mostrar_somente_nome()
    else:
        os.system("cls")
        print("Pessoa inexistente, tente novamente")
elif pessoa_op == "2":
    os.system("cls")
    opcao = str(input("""
=== Digite o que deseja ver === 

1 - Dados de entrega

2 - Dados de marketing     
                      
3- Ver somente o nome do cliente

R:                
    """))

    if opcao == "1":
        print("=== dados abaixo para entrega ===")
        pessoa2.dados_entrega()
    elif opcao == "2":
        print("=== dados abaixo para entrega ===")
        pessoa2.dados_emaiL_marketing()
    elif opcao == "3": 
        pessoa2.mostrar_somente_nome()
    else:
        print("Pessoa inexistente, tente novamente")
else: 

    print("Error")
               

