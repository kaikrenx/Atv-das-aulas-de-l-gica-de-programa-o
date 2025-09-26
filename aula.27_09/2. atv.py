import os
os.system("cls")

qntd_f = 0
qntd = 0
total_salario = 0
menor_idade = 999999999999
maior_idade = 0




while True: 
        
    codigo = int(input("""
        CÓDIGO | Descrição
            1     | Adicionar pessoa
            2     | Exibir resultados
            3     | Sair
              
            
"""))

   

    match codigo:
        
        case 1: 
            qntd += 1
            idade = float(input("Digite sua idade: "))
            sexo = str(input("Digite seu sexo (M/F): ")).upper()
            salario = float(input("Digite seu salário: "))
            
            os.system("cls")
            
            if sexo == "F" and salario >= 5000:
                qntd_f += 1
            
            total_salario += salario

            if idade < menor_idade:
                menor_idade = idade
            if idade > maior_idade:
                maior_idade = idade


        case 2:
            os.system("cls")
            
            print(f"Idade: ")


            if qntd > 0:
                media_sal = total_salario / qntd
                print(f"A média do salário é: R$ {media_sal:.2f}")
                print(f"Quantidade de mulheres com salário > R$5000: {qntd_f}")
                print(f"Menor idade cadastrada: {menor_idade}")
                print(f"Maior idade cadastrada: {maior_idade}")

        
        case 3:
            os.system("cls")
            print ("Encerrando...")
            break