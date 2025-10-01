import os
os.system("cls")


# Criando um vetor (lista).
lista_notas = []

# Inserindo notas
for i in range(3):
    nota = int(input(f"Digite a {i+1}ª nota: "))
    lista_notas.append(nota)
   # soma += nota
soma = sum(lista_notas)

media = soma / 3

# Mostrar as notas

print(f"A media das notas é: {media}")


print("FIM")