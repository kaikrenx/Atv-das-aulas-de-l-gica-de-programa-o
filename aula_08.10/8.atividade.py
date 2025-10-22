import os 
os.system("cls")


def nota_final(primeira_nota, segunda_nota):
    os.system("cls")
    return (primeira_nota + segunda_nota) / 2 


while True: 

    primeira_nota = float(input("Digite uma nota: "))
    segunda_nota = float(input("Digite uma nota: "))

    if primeira_nota and segunda_nota >= 0 and primeira_nota and segunda_nota  <= 10:
        media = nota_final(primeira_nota, segunda_nota)
        break
    else: 
        print("")
        print("Tente novamente (apenas notas de 0 a 10)")
        print("")



if media>= 7:
    print(f"Você foi aprovado, aqui sua média: {media}")
else:
    print(F"Você foi Reprovado: {media}")
