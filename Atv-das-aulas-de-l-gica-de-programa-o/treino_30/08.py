import os
os.system("clear")

#Solicitar ao usuário uma forma de pagamento
opcoes_pg = [ "debito", "credito"]
produtos = ["notebook"]
precos = 3000


print(F"Opções de pagamento: {opcoes_pg}")

forma_pg = str(input("Digite uma forma de pagamento:  "))






match forma_pg:
    case "debito": 
        precos_final = (precos * 0.10)
        print(F"O valor total do {produtos} é de: {precos_final}")
    case "credito":
        vezes = float(input("Digite quantas vezes deseja: (1x, 2x, 3x, 4x, 5x, 6x)"))
         # pula uma linha
        precos_final = (precos / vezes) 
         # pula uma linha
        case
