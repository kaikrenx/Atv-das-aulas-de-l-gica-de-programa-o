import os
os.system("cls")



def contador(numero):

    if numero % 2 == 0:
        print(f"Seu numero é {numero} e ele é par")
    else:
        print(f"Seu numero é {numero} e ele é impar")

numero = float(input("Digite o numero: "))

contador(numero)