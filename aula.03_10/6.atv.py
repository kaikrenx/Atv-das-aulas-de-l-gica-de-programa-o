import os
os.system("cls")

QUANTIDADE_NUMERO = 10

def calculo(numero):
    
    for i in range(QUANTIDADE_NUMERO):
        resultado = numero * i 
        
        print(f"{numero} X {i} = {resultado}")

numero = int(input("Digite um número inteiro pra ter a tabúada: "))

calculo(numero)



