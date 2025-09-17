import os
os.system 


nota = 0
    for i in range(3):
    
    soma = float(input(f"Digite a {i+1}ª nota para saber a nota (são quatro)", step=1))
    
    if soma < 0 and soma > 10:
        
    
        nota = nota + soma
    

        media = nota / 3
    


    if media >= 7:
        print(f"Você foi aprovado, aqui a sua média: {media: .2f}")
    elif media >= 4 and media < 7:
        print(f"Você está de recuperação, aqui sua média: {media: .2f}")
    else:
        print(f"Você foi reprovado, aqui sua média: {media: .2f}")
