import os
os.system("cls")

Nota_1= int(input(f"Digite a primeira nota: "))
Nota_2= int(input(f"Digite a segunda nota: "))

media =  (Nota_1 + Nota_2) / 2 # calcular media

soma = Nota_1 + Nota_2

produto = Nota_1 * Nota_2

Maior = max(Nota_1, Nota_2)
Menor = min(Nota_1, Nota_2)


if Nota_1 == Nota_2: 
    print("São iguais")
else: 
    print("Não são iguais")



# if primeiro_numero > segundo_numero:
#        maior = primeiro_numero:
#        menor = segundo_numero:
# else:
#        maior = segundo_numero
#        menor = primeiro_numero

print(f"Média: {media}")
#pular uma linha
print(f"Soma: {soma}")
#pular uma linha
print(f"Produto: {produto}")
#pular uma linha
print(f"Maior: {Maior}")
#pular uma linha
print(f"Menor: {Menor}")
#pular uma linha 
