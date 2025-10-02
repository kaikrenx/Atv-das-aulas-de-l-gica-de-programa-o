import os
os.system("cls")

# criando um vetor

vetor_de_notas = []

print("Solicitando 3 notas")
#solicitando 3 notas
for i in range(3):
    nota = float(input("Digite uma nota: "))
    #Inserindo uma nota na vetor de notas.
    vetor_de_notas.append(nota)


print("\nMostrando todas as notas.")
for i in range(3):
    # O valor da variável i começa com zero.
    # O valor de i no vetor faz mostrar o índice no vetor

    print(f"Nota {i+1}ª: {vetor_de_notas[i]}")
