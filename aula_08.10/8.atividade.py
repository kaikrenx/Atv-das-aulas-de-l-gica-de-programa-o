import os 
os.system("cls")


def nota_final(primeira_nota, segunda_nota):
    return primeira_nota + segunda_nota / 2 
media = nota_final(primeira_nota, segunda_nota)


primeira_nota = float(input("Digite uma nota: "))
segunda_nota = float(input("Digite uma nota: "))
