import os
os.system("cls")

qtd_nota = 0

while True:

    nota_final = 0
    

    notas = float(input(f"Digite sua nota: "))
    print("")

    qtd_nota += 1

    nota_final = nota_final + notas



    if qtd_nota > 1:
        continuar = str(input("Caso já tenha escrevido todas as notas digite N, caso vá adicionar alguma digite S   (S/N): ")).upper()

        if continuar == "N":
            break

        

        media = nota_final / qtd_nota

        print("")
        print(f"Você teve {qtd_nota} notas e sua média final foi de: {media: .2f}")
        


    

