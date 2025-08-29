import os
os.system("cls")


nota = 12

# Se nota menor que zero ou maior que 10.
# OR -> Fora do intervalo definido

if nota < 0 or nota > 10:
    print("Nota inválida.")
else:
    print(f"Nota: {nota} ")

#se nota maior ou igual a zero e
#nota menor igual ou igual a 10.
# AND -> Dentro de um intervalo definido


# if nota >= 0 and nota <= 10:
#   print(f"Nota: {nota})
#else: 
#    print("Nota inválida.")



