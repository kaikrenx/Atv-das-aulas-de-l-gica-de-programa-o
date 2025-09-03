import os
os.system("cls")

produto = "notebook"
preco = 3000

print("Opções de pagamento: débito ou crédito")
forma_pg = input("Digite uma forma de pagamento: ")

if forma_pg == "debito":
    preco_final = preco * 0.9
    print(f"O valor total do {produto} com 10% de desconto é: R$ {preco_final:.2f}")



elif forma_pg == "credito":
    vezes = int(input("Digite em quantas vezes deseja parcelar (1 a 6): "))
    
    match vezes:
        case 1:
            print(f"1x de R$ {preco:.2f} ")
        case 2:
            parcela = preco / 2
            print(f"2x de R$ {parcela:.2f}")
        case 3:
            parcela = preco / 3
            print(f"3x de R$ {parcela:.2f}")
        case 4:
            parcela = preco / 4
            print(f"4x de R$ {parcela:.2f}")
        case 5:
            parcela = preco / 5
            print(f"5x de R$ {parcela:.2f}")
        case 6:
            parcela = preco / 6
            print(f"6x de R$ {parcela:.2f}")
        case _:
            print("Fim")