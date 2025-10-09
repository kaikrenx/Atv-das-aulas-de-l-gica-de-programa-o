import os
os.system("cls")

def  CAL_IMC(peso, altura):
    
    return peso / (altura * altura)

print("=== Programa pra saber o (IMC)===")
print("")

peso = float(input("Digite seu peso em Kg(ex: 67.2): "))
altura = float(input("Digite sua altura em metros(Ex: 1.70): "))

IMC = CAL_IMC(peso, altura)

if IMC < 18.5:
    print(f"Seu IMC é de: {IMC: .2f} Você está abaixo do peso")
elif 18.5 <= IMC <= 24.9:
    print(f"Seu IMC é de: {IMC: .2f} é um peso normal")
elif 25 <= IMC <= 29.9:
    print(f"Seu IMC é de: {IMC: .2f} Você está com sobrepeso")
else:
    print(f"Seu IMC é de: {IMC: .2f} Você está com obesidade")




