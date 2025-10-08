import os
import time

os.system("cls")

# Criando uma função

def saudacao():
    print("Boa tarde")
    time.sleep(3) # Espera 3 segundos.
    os.system("cls")
    return

# Código princpal
saudacao() # Função a função
print("Exemplo de uso de uma função sem parâmetros.")