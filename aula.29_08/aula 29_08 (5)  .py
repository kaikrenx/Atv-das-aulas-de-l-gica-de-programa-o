
import os
os.system

n1 = float(input("Digite um numero: "))
n2 = float(input("Digite o segundo numero: "))



operacao= str(input("Digite a operação desejada +, /, -, *: "))


soma = (n1 + n2)
subtracao = (n1 - n2)
divisao = (n1 / n2)
multiplicacao = (n1 * n2)


match operacao:
    case "+":
        print(f"O resultado da soma: {soma}")
    case "-":
        print(f"O resutado da subtração: {subtracao}")
    case "/":
        print(f"O resultado da sua divisão: {divisao}")
    case "*":
        print(f"O resultado da sua multiplicação: {multiplicacao}")


