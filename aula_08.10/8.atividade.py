import os 
os.system("cls")


def nota_final(primeira_nota, segunda_nota):
    return (primeira_nota + segunda_nota) / 2 

primeira_nota = float(input("Digite uma nota: "))
segunda_nota = float(input("Digite uma nota: "))

media = nota_final(primeira_nota, segunda_nota)



if media>= 7:
    print(f"Você foi aprovado, aqui sua média: {media}")
else:
    print(F"Você foi Reprovado: {media}")
