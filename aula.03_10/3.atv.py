import os
os.system
# Função com passagem de parâmetros
# Criando uma função.

def saudacao(nome, idade):
    print(f"Olá, {nome}! Bem-vindo(a)!")
    print(f"Sua idade é {idade}anos.")



print("Solicitando dados") 
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
#chamando função

saudacao(nome, idade)
