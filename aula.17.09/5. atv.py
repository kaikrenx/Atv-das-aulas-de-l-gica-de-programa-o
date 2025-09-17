import os 
os.system("cls")

usuario = "pac@gmail.com"
senha = "123"
tentativas = 1
max_tentativas = 3


while tentativas <= max_tentativas: 
    login = input("Digite seu email: ")
    Senha = input("Digite sua senha: ")
    

    if login == usuario and Senha == senha:
        print("Login efetuado com sucesso")
        break
    
    else:
        tentativas += 1

        print("Senha incorreta, tente novamente")
        if tentativas > max_tentativas:
            print("Você ultrapassou o limite de tentativas")
            break



