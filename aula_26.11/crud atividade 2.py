import os
os.system("cls")


# Lista inicial
lista_clientes = []


# CREATE - Adicionar / Inserir
print("CREATE - Adicionar / Inserir")
nome = input("Digite o nome que deseja inserir: ")
lista_clientes.append(nome)
print(f"O nome: {nome} foi inserido com sucesso!")


# READ - Ler / Mostrar
print("\nREAD - Ler / Mostrar")
print(lista_clientes)


# UPDATE - Atualizar / Alterar
print("\nUPDATE - Atualizar / Alterar")
nome_para_atualizar = input("Digite o novo nome: ")

if nome_para_atualizar in lista_clientes:
    novo_nome = input("Digite o novo nome que deseja inserir: ")
    indice = lista_clientes.index(nome_para_atualizar)
    lista_clientes[indice] = novo_nome
    print(f"O nome {nome_para_atualizar} foi atualizado para {novo_nome}")
else:
    print(f"O nome {nome_para_atualizar} não foi encontrado.")

print(lista_clientes)

# DElETE

print("\nDelete - Excluir / Remover")
nome_para_excluir = input("Digite o nome que deseja excluir: ")
if nome_para_excluir in lista_clientes:
    lista_clientes.remove(nome_para_excluir)
    print(f"{nome_para_excluir} foi excluída com sucesso!")

else:
    print(f"O nome {nome_para_excluir} não foi encontrado.")

print(lista_clientes)