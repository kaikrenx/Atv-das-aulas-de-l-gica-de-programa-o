import os
os.system("cls")



def valor_final(preco_produto):
    if preco_produto < 100: 
        return preco_produto * 1.10
    else: 
        return preco_produto * 1.20


print("""
Se o preço for a partir de 100 reais sofrerá inflação de 20% 
Se o preço for abaixo de 100 reais sofrerá inflação de 10%
      
""")

preco_produto = float(input("Diga o preço do seu produto: "))

total = valor_final(preco_produto)


os.system("cls")
print(f"O valor total do seu produto com sua respectiva inflação: {total}")