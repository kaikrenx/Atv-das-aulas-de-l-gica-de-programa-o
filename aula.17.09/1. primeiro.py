import os
os.system("cls")



QUANTIDADE_NOTAS = 2
soma = 0



for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input("Digite uma nota:"))
        if nota < 0 or nota >10:
            print("A nota inválida.")
        else:
            soma += nota
            break
media = soma / QUANTIDADE_NOTAS
print(f"Média: {media}")