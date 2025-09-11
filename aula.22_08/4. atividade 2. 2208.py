import os
os.system("cls")


Nota_1 = float(input("Digite a primeira nota: "))
Nota_2 = float(input("Digite a segunda nota: "))
Nota_3 = float(input("Digite a terceira nota: "))

media = (Nota_1 + Nota_2 + Nota_3) / 3

if media >= 7: 
    print(f"Sua média foi: {media: .2f} está aprovado!")
else:
    print(f"Sua média foi: {media: .2f} está reprovado")