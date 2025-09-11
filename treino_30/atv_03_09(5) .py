import os
os.system("cls")

genero = str(input(""" 
-------Digite seu gênero para saber seu peso ideal: --------- 
M = Masculino
F = Feminino                  
                   
"""))
print ("")

altura = float(input("Digite sua altura para saber seu peso ideal: "))


if genero == "M" or "m":

    peso_ideal= (72.7 * altura) - 58 # type: ignore
    print("")
    print(f"Seu peso ideal sendo Homem é: {peso_ideal: .2f}")

elif genero == "F" or "f": 

    peso_ideal= (62.1 * altura) - 44.7
    print ("")
    print(f"Seu peso ideal sendo Mulher é: {peso_ideal: .2f}")

