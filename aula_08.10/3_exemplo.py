import os
import time

os.system("cls")

# Função sem parâmetros e sem retorno
def limpa_tela():
    os.system("cls")
    time.sleep(3) # Espera 3 segundos.

# Função com parâmetros e com retorno
def calcular_media(n1, n2):
    media = (n1 + n2)/ 2
    return media

# Função com parâmetros e sem retorno.
def mostrar_resultado (media):
    print(f"Resultado: {media}")

    if media>= 7:
        print(f"Aprovado")
    else:
        print(F"Reprovado")
    

# Código princpal
limpa_tela() # Chamando a função
print("Exemplo de uso de uma função sem parâmetros.")
primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite um número: "))


# Função com parâmetros e com retorno.
media = calcular_media(primeiro_numero, segundo_numero)

# Função com parâmetros e sem retorno
mostrar_resultado(media) # Mostrar resultado chamando função