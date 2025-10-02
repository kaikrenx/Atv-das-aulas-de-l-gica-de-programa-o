import os
os.system('cls')

preco_total = 0
lista_pratos = []
lista_precos = []
quantidade = 0
while True:
    print("""
===== MENU =====
Código       Prato            Valor
  1         Picanha         R$ 25,00
  2         Lasanha         R$ 20,00
  3         Strogonoff      R$ 18,00
  4         Bife acebolado  R$ 15,00
  5         Pão com ovo     R$ 5,00        
          """)
   
    opcao = int(input("Digite o código da opção desejada: "))

    match opcao:
        case 1:
            prato = "Picanha"
            preco = 25 
            lista_pratos.append(prato)
            lista_precos.append(preco)
            quantidade +=1 
        case 2:
            prato = "Lasanha"
            preco = 20
            lista_pratos.append(prato)
            lista_precos.append(preco)
            quantidade +=1 
        case 3:
            prato = "Strogonoff"
            preco = 18
            lista_pratos.append(prato)
            lista_precos.append(preco)
            quantidade +=1 
        case 4:
            prato = "Bife acebolado"
            preco = 15
            lista_pratos.append(prato)
            lista_precos.append(preco)
            quantidade +=1 
        case 5:
            prato = "Pão com ovo"
            preco = 5
            lista_pratos.append(prato)
            lista_precos.append(preco)
            quantidade +=1 
        case _:
            print("Opção inválida.")
            print("Tente novamente...")
            preco = 0

    preco_total = preco_total + preco


    mais_pedidos = input("Deseja fazer um novo pedido? \nUse S ou N para responder: ").upper()

    os.system("cls")

    if mais_pedidos == "N":
        break


# Mostrando resultado.
print("\n=== RESTAURANTE ===")

contador = 1

for i in range(quantidade):
    print(f"\nPrato: {lista_pratos[i]}, Preço: R${lista_precos[i]}")

print(f"Total a pagar: {preco_total}")
