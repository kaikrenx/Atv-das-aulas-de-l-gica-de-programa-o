import os
os.system("cls")

lista_numeros = []
QUANTIDADE_NUMEROS = 5
qntd_negativo = 0
soma = 0


for i in range(QUANTIDADE_NUMEROS):
    numero = float(input("Digite 5 numeros, negativos e positivos: "))
    lista_numeros.append(numero)


    if numero < 0:
        qntd_negativo += 1
    else:
        soma += numero





print(f"\nSoma dos positivos: {soma}")


print(f"A quantidade de numeros negativos: {qntd_negativo}")


    


  



