import os
os.system("cls")

print("""
Código \t prato \t\t\t valor
    1 \t picanha \t\t R$ 25,00
    2 \t lasanha \t\t R$ 20,00
    3 \t strogonoff \t\t R$ 18,00
    4 \t bife acebolado \t R$ 15,00
    5 \t pão com ovo \t\t R$ 5,00
    
""")

codigo = int(input("Digite o código do prato desejado: "))


#pular uma linha

print("")
match codigo:
    case 1:
        print("Seu prato é picanha e o valor é R$ 25,00")
    case 2:
        print("Seu prato é lasanha e o valor é R$ 20,00")
    case 3: 
        print("Seu prato é strogonoff e o valor é R$ 18,00")
    case 4:
        print("Seu prato é bife acebolado e o valor é R$ 15,00")
    case 5:
        print("Seu prato é pão com ovo e o valor é R$ 5,00")
