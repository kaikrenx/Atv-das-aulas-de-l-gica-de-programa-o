import os
os.system("cls")

# criando um vetor

qntd_pares = 0
qntd_impares = 0


lista_numeros = []

QUANTIDADE_NUMEROS = 3

print(F"\033[32mSolicitando {QUANTIDADE_NUMEROS} numeros\033[0m]")
#solicitando 3 numeros
for i in range(QUANTIDADE_NUMEROS):
    numero = float(input("Digite um numero: "))
    #Inserindo uma nota na vetor de numeros.
    lista_numeros.append(numero)

    if numero % 2 == 0:
        qntd_pares += 1
    else:
        qntd_impares += 1

    # lista_numeros.append(numero)

for i in lista_numeros:
    print(f"\nNúmero: {i}")


print(f"\nQuantidade numeros pares: {qntd_pares: .2f}")
print(f"\nQuantidade de numeros ímpares: {qntd_impares: .2f}")





