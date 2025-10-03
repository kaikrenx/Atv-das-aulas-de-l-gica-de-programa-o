import os
os.system("cls")


QUANTIDADE_NUMEROS = 5
lista_numeros = []
soma = 0

for i in range(QUANTIDADE_NUMEROS):
    numeros = float(input("Digite um numero: "))
    
    if numeros <= 0:
        numeros = 0
    lista_numeros.append(numeros)
    

for i, numeros in enumerate(lista_numeros,start=1):
    print(f"{i} Numero: {numeros}")
