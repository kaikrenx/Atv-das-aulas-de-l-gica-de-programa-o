import os
os.system("cls")


# Lista inicial
lista_funcionario = []


# CREATE - Adicionar / Inserir
print("CREATE - Adicionar / Inserir")
nome = input("Digite o nome que deseja inserir: ")
lista_funcionario.append(nome)



# READ - Ler / Mostrar
print("\nREAD - Ler / Mostrar")
print(lista_funcionario)


# UPDATE - Atualizar / Alterar
print("\nUPDATE - Atualizar / Alterar")
nome_para_atualizar = input("Digite o novo nome: ")

if nome_para_atualizar in lista_funcionario:
    novo_nome = input("Digite o novo nome que deseja inserir: ")
    indice = lista_funcionario.index(nome_para_atualizar)
    lista_funcionario[indice] = novo_nome
    print(f"O nome {nome_para_atualizar} foi atualizado para {novo_nome}")
else:
    print(f"O nome {nome_para_atualizar} não foi encontrado.")

print(lista_funcionario)

# DEFETE

print("\nDelete - Excluir / Remover")
nome_para_excluir = input("Digite o nome que deseja excluir: ")
if nome_para_excluir in lista_funcionario:
    lista_funcionario.remove(nome_para_excluir)
    print(f"{nome_para_excluir} foi excluída com sucesso!")

else:
    print(f"O nome {nome_para_excluir} não foi encontrado.")

print(lista_funcionario)