import os
os.system("cls")



qntd = 0
pares = 0
impares = 0
qntd_par = 0
qntd_impar = 0

while True:
    numeros = int(input("Digite um número: "))
    
    if numeros > 0: 
        qntd += 1
        if numeros % 2 == 0:  
            qntd_par += 1
            pares = pares + 1
        else: 
            qntd_impar += 1
            impares = impares + 1
    if numeros == 0:
        break


    
media_par = pares / qntd_par 
media_geral = (pares + impares) / qntd

print(f"Sua quantidade de numeros pares: {qntd_par: .2f}")
print(f"a média dos numeros é: {media_geral: .2f}")
print(f"a média dos pares: {media_par: .2f}")


