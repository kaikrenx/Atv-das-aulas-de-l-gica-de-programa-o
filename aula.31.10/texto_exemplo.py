import os
os.system("cls")

# texto que desejo salvar

texto = input("Digite o texto: ")

# DEFINIR O NOME DO ARQUIVO PARA SALVAR.
nome_arquivo = "exemplo.txt"

# Comandos para salvar.
with open(nome_arquivo, "a") as meu_arquivo:
    meu_arquivo.write(f"{texto}\n")

    print("Salvo com sucesso")