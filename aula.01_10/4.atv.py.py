import os
os.system("cls")


lista_notas = []

for i in range(4):
    nota = float(input(f"Digite sua {i+1}ª: "))
    lista_notas.append(nota)

soma = sum(lista_notas)

media = soma / 4

# Mostrar as notas

if media >= 7:
    print(f"Você foi aprovado")

elif media >=5 and media < 7:
    print("Você está em recuperação")

else:
    print("Você foi reprovado")

for i in range(4):
    print(f"Sua nota: {lista_notas[i]}")     

print(f"Sua média é: {media: .2f}")

