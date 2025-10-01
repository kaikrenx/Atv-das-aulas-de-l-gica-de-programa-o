import os
os.system("cls")


lista_numero = []

for i in range(5):
    numero = float(input(f"Digite o {i+1}º numero"))
    lista_numero.append(numero)


numero_maior = max(lista_numero)
numero_menor = min(lista_numero)

print(f"O maior numero escolhido é {numero_maior}")
print(f"O menor numero escolhido é {numero_menor}")