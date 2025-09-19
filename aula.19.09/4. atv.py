import os
os.system("cls")

qntd = 0

while True:

    qntd = 0
    numeros = int(input("Digite um número: "))
    qntd_par = 0
    qntd_impar = 0

    if qntd > 3: 

        norma = str(input("Digite S para continuar e N para parar (S/N): "))

        if numeros % 2 == 0:  
            qntd_par += 1
            pares = pares + 1
        else: 
            impares = impares + 1
            qntd_impar =+ 1

        media_par = pares / qntd_par
        media_impar = impares / qntd_impar


        media_geral = numeros / qntd


        if norma == "N":
            break

print(f"Sua quantidade de numeros pares: ")




