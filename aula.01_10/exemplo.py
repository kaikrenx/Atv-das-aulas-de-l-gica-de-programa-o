import os
os.system("cls")


# Criando um vetor (lista).

lista_notas = []
QUANTIDADE_DE_NOTAS = 3

# Inserindo notas
for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    lista_notas.append(nota)
    soma = sum(lista_notas)
    média = soma / QUANTIDADE_DE_NOTAS

print(f'Notas informadas {lista_notas}')
print(f'Média = {média:.2f}')
