import os
os.system("cls")

#  Função de cada calculo
def somar(primeiro_numero, segundo_numero):
    soma = primeiro_numero + segundo_numero
    return soma
def subtrair(primeiro_numero, segundo_numero):
    subtracao = primeiro_numero - segundo_numero
    return subtracao
def dividir(primeiro_numero, segundo_numero):
    divisao = primeiro_numero / segundo_numero 
    return divisao

def multiplicar(primeiro_numero, segundo_numero):
    multiplicacao = primeiro_numero * segundo_numero
    return multiplicacao
# Entrada de numero
primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite um número: "))
opcao = int(input("""Digite qual operação deseja realizar:
1 - soma
2 - subtração
3 - divisao
4 - multiplicação

"""))

soma = somar(primeiro_numero, segundo_numero)
subtracao = subtrair(primeiro_numero, segundo_numero)
divisao = dividir(primeiro_numero, segundo_numero)
multicacao = multiplicar(primeiro_numero, segundo_numero)
match opcao:
    case 1: 
        os.system("cls")
        print(f"O resultado da soma é: {soma}")
    case 2:
        os.system("cls")
        print(f"O resultado da subtração é: {subtracao}")
    case 3:
        os.system("cls")
        print(f"O resultado da operação é: {divisao}")
    case 4: 
        os.system("cls")
        print(f"O resultado da multiplicação é: {multicacao}")




