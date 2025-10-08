import os 
os.system("cls")


print("Programa para saber sua altura em metros e convertê-lá em centímetros ou pés")
print("")

def centimetros(altura):    
    return altura * 100

def pes(altura):
    return altura * 3.281

altura = float(input("Digite sua altura em metros (ex: 1.74): "))

opcao = int(input(""" 
 ====== Escolha a opção ======
                  
1 - Centimetros
2 - Pés

"""))

altura_cm = centimetros(altura)
altura_pes = pes(altura)

if opcao == 1: 
    os.system("cls")
    print(f"Sua altura em centimetros é: {altura_cm} cm")
else: 
    os.system("cls")
    print(f"Sua altura em pés é de aproximadamente: {altura_pes: .3f} pés")




