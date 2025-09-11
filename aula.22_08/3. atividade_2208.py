import os
os.system("cls")

Nota_1= float(input(f"Digite a primeira nota: "))
Nota_2= float(input(f"Digite a segunda nota: "))

media =  (Nota_1 + Nota_2) / 2 # calcular mediag 

soma = Nota_1 + Nota_2

produto = Nota_1 * Nota_2

Maior = max(Nota_1, Nota_2)
Menor = min(Nota_1, Nota_2)

print(f"Média: {media}")
#pular uma linha
print(f"Soma: {soma}")
#pular uma linha
print(f"Produto: {produto}")
#pular uma linha
print(f"Maior: {Maior}")
#pular uma linha
print(f"Menor: {Menor}")
 
