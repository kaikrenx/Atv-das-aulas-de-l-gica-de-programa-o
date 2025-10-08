import os 
os.system("cls")


# Escreva um programa que solicite ao usuário o ano de
#nascimento e, utilizando uma função, retorne com a idade do
# usuário.


def calculo(ano_nc, ano):
    if ano < ano_nc:
        print("INVÁLIDO REINICIE O PROGRAMA")
    else: 
        return ano - ano_nc

ano_nc = int(input("Digite o ano de seu nascimento: "))
ano = int(input("Digite o ano atual: "))

idade = calculo(ano_nc, ano)

print(f"Sua idade é: {idade}")