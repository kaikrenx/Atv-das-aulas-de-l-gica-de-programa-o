import os
os.system("cls")

aluno = str(input("Digite o nome do aluno: "))

Nota_1= float(input(f"Digite a primeira nota: "))
Nota_2= float(input(f"Digite a segunda nota: "))
A, B, C, D, E = "A", "B", "C", "D", "E"



media =  (Nota_1 + Nota_2) / 2 # calcular media

if media >= 9: 
    conceito = A
elif media >= 7.5 and media < 9:
    conceito = B
elif media >= 6 and media < 7.5:
    conceito = C
elif media >= 4 and media < 6:
    conceito = D
else:
    conceito = E

if conceito in [A, B, C]:  # ou if conceito in ("A", "B", "C")

    print(f" {aluno} Você foi aprovado, a seguir o desempenho, media: {media} e {conceito}")

else: 
    print(f" {aluno} Você foi reprovado, a seguir seu desempenho, média: {media} e {conceito}")