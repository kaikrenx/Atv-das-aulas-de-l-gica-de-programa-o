import os
os.system("cls")


qntd_fam = 0
salario_familia = 0
maior_salario = 0
menor_salario = 999999999
total_sal = 0

while True: 
        
    codigo = int(input("""
        CÓDIGO | Descrição
            1     | Adicionar Família
            2     | sair e exibir resultados 
           
              
            
"""))
    


    match codigo:
        
        case 1: 
            qntd_fam += 1

            salario_familia = int(input("Digite o sálario total da família: "))
            qntd_filhos = int(input("Digite a quantidade de filhos na familia: "))

            total_sal += salario_familia

            os.system("cls")

            if salario_familia < menor_salario:

                menor_salario = salario_familia

            if salario_familia > maior_salario:

                maior_salario = salario_familia
        case 2:
            
            media_sal = total_sal / qntd_fam
            media_fil = qntd_filhos / qntd_fam
            


            print(f"{qntd_fam: .2f} familias responderam a pesquisa")
            print(f"R$ {media_sal: .2f} - média salarial por família")
            print(f"{media_fil: .2f} média de filhos por família")
            print(f"O menor salario familiar é de: {menor_salario}")
            print(f"O maior salario familiar: {maior_salario}")


        



