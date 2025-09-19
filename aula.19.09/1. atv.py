import os
os.system("cls")


valor_total = 0 

while True:

    print("""
Código \t prato \t\t\t valor
    1 \t picanha \t\t R$ 25,00
    2 \t lasanha \t\t R$ 20,00
    3 \t strogonoff \t\t R$ 18,00
    4 \t bife acebolado \t R$ 15,00
    5 \t pão com ovo \t\t R$ 5,00
    
""")

    codigo = str(input("Digite o código do prato desejado (se quiser parar digite 6): "))
    
    if codigo == "6": 
        print(f"\nValor total do pedido: R$ {valor_total:.2f}")
        print("Obrigado por fazer seu pedido!")
        break

    if codigo == "1":
        valor_total += 25.00
        print(f"Você escolheu picanha, o valor total ta sendo: R${valor_total:.2f}")


    elif codigo == "2":
        valor_total += 20.00 
        print(f"Você escolheu lasanha, o valor total ta sendo: R${valor_total:.2f}")


    elif codigo == "3":
        valor_total += 18.00  
        print(f"Você escolheu Strogonoff, o valor total ta sendo: R${valor_total:.2f}")

    elif codigo == "4":
        valor_total += 15.00  
        print(f"Você escolheu Bife Acebolado, o valor total ta sendo: R${valor_total:.2f}")

    elif codigo == "5":
        valor_total += 5.00  
        print(f"Você escolheu Pão com Ovo, o valor total ta sendo: R${valor_total:.2f}")

#pular uma linha

