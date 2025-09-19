import os
os.system("cls")


qntd_nota = 0
nota_final = 0


while True:

    notas = int(input("Digite as notas: "))



    if notas < 0:
        break
    
    qntd_nota += 1
    nota_final += notas



media = nota_final / qntd_nota
print(f"Sua média é de: {media: .2f}")
        
