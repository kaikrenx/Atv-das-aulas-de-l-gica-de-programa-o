import os 
os.system("cls")

usuario = "pac@gmail.com"
senha = "123"


while True: 
    login = input("Digite seu email: ")
    Senha = input("Digite sua senha: ")
    

    if login == usuario and Senha == senha:
        print("Login efetuado com sucesso")
        break
    else: 
        print("Login ou senha incorreta! tente novamente. ")