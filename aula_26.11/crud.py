# Lista inicial
lista_clientes = []


# CREATE - Adicionar / Inserir
print("CREATE - Adicionar / Inserir")
nome = "Marta"
lista_cliente.append(nome)
print(f"O nome: {nome} foi inserido com sucesso!")


# READ - Ler / Mostrar
print("\nREAD - Ler / Mostrar")
print(lista_cliente)


# UPDATE - Atualizar / Alterar
print("\nUPDATE - Atualizar / Alterar")
nome_para_atualizar = "Marta"

if nome_para_atualizar in lista_clientes:
    novo_nome = "Marta Silva"
    indice = lista_cliente.index(nome_para_atualizar)
    lista_cliente[indice] = novo_nome
    print(f"O nome {nome_para_atualizar} foi atualizado para {novo_nome}")
else:
    print(f"O nome {nome_para_atualizar} não foi encontrado.")

print(lista_clientes)

# DEFETE

print("\nDelete - Excluir / Remover")
nome_para_excluir = "Maria"
if nome_para_excluir in lista_clientes:
    lista_clientes.remove(nome_para_excluir)
    print(f"{nome_para_excluir} foi excluída com sucesso!")

else:
    print(f"O nome {nome_para_excluir} não foi encontrado.")

print(lista_clientes)