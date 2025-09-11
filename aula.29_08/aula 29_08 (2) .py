
import os
os.system("cls")

login = str(input("Digite o seu email: "))
senha = str(input("Digite sua senha: "))


if login == "polar@gmail.com" and senha == "polar123":
    print("Bem-vindo!")
else: 
    print("Login ou senha inválidos: ")


