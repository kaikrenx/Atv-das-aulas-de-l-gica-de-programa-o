import os
import time

os.system("cls")

# Função sem parâmetros e sem retorno
def limpa_tela():
    os.system("cls")
    time.sleep(3) # Espera 3 segundos.

# Função com parâmetros e com retorno
def somar(n1, n2):
    calcular = n1 + n2 
    return calcular

# Função com parâmetros e sem retorno.
def mostrar_resultado (soma):
    print(f"Resultado: {soma}")
    

# Código princpal
limpa_tela() # Chamando a função
print("Exemplo de uso de uma função sem parâmetros.")
primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite um número: "))


# Função com parâmetros e com retorno.
soma = somar(primeiro_numero, segundo_numero)

# Função com parâmetros e sem retorno
mostrar_resultado(soma) # Mostrar resultado chamando função