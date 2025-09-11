import os
os.system("cls")

macas= float(input("digite a quantidade de maçãs desejadas, sabendo que R$ 1,30 cada se menos de uma duzia e R$ 1,00 se for ao menos R$ 12,00: "))
preco_macas= float

if macas <= 11:
    preco_macas = macas * 1.30

else: 
   preco_macas = macas * 1.00 


print(f"O total da sua compra foi de R$", {preco_macas})

