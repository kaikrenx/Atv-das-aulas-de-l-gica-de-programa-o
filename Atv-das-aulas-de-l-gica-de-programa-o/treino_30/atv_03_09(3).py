import os
os.system("cls")

mes = float(input("Digite o número ( 1 a 12) para saber o mês correspondente: "))


match mes:
    case 1:
        print(f"O mês correspondente a 1 é janeiro")
    case 2:
        print(f"O mês correspondente a 2 é fevereiro")
    case 3:
        print("O mês correspondente a 3 é março")
    case 4:
        print("O mês correspondente a 4 é abril")
    case 5:
        print("O mês correspondente a 5 é maio")
    case 6:
        print("O mês correspondente a 6 é junho")
    case 7:
        print("O mês correspondente a 7 é julho")
    case 8:
        print("O mês correspondente a 8 é agosto")
    case 9:
        print("O mês correspondente a 9 é setembro")
    case 10:
        print("O mês correspondente a 10 é outubro")
    case 11:
        print("O mês correspondente a 11 é novembro")
    case 12:
        print("O mês correspondente a 12 é dezembro")
    case _:
        print("Número inválido. Digite um número entre 1 e 12.")
    