 #📌 Resumo pra imaginar:

#input() = o programa te pergunta.

#float() = transforma sua resposta em número.

#def ... = cria uma caixinha que faz contas.

#return = a caixinha devolve o resultado.

#print() = mostra o resultado na tela.


import os
os.system("cls")






a = float(input("Diga um primeiro_numero: "))
b = float(input("Diga um segundo_numero: "))

def soma(a, b): 
    return a + b # devolve o resultado

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):  
    return a * b

def divisao(a, b):
    return a / b

print(f"O resultado da soma é {soma(a, b)}")
print(f"O resultado da subtracao é {subtracao(a,b)}")
print(f"O resultado da multiplicacao é {multiplicacao(a,b)}")
print(f"O resultado da divisao é {divisao(a,b)}")