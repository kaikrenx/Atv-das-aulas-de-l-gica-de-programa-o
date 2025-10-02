import os
os.system("cls")

# criando um vetor

lista_numeros = []

QUANTIDADE_NUMEROS = 5

print(F"Solicitando {QUANTIDADE_NUMEROS} numeros")
#solicitando 3 notas
for i in range(QUANTIDADE_NUMEROS):
    numero = float(input("Digite um numero: "))
    #Inserindo uma nota na vetor de notas.
    lista_numeros.append(numero)


# Verificando maior e menor numero

menor = min(lista_numeros)
maior = max(lista_numeros)




print("\nMostrando todas as numero.")
for i in range(QUANTIDADE_NUMEROS):
    # O valor da variável i começa com zero.
    # O valor de i no vetor faz mostrar o índice no vetor

    print(f" {i+1}ª numero: {lista_numeros[i]}")

print(f"\nMenor numero: {menor}")
print(f"\nMaior numero: {maior}")
