import os
os.system("cls")

soma_notas = 0
QUANTIDADE_NOTAS = 3

for i in range(QUANTIDADE_NOTAS):
    notas= float(input(f"Digite a {i+1}ª nota: ")) 
    soma_notas += notas
def calculo(soma_notas):
    return soma_notas / QUANTIDADE_NOTAS

media = calculo(soma_notas)

print(f"A sua média é: {media}")

