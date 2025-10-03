import os
os.system("cls")

def valor(numero):

    if numero < 0:
        print(f"{numero} é negativo")
    else: 
        print(f"{numero} é positivo")


numero = int(input("Digite o número: "))


valor(numero)