import os
import time
from dataclasses import dataclass

os.system('cls') 

lista_alunos = []

@dataclass
class Endereço:
    logradouro: str
    numero: str
    cidade: str
    estado: str

@dataclass
class Aluno:
    nome: str
    nascimento: str
    r_a: str
    curso: str
    endereco: Endereço  

    def mostrar_dados(self):
        print(f'\nNome: {self.nome}')
        print(f'Data de Nascimento: {self.nascimento}')
        print(f'R.A: {self.r_a}')
        print(f'Curso: {self.curso}')
        print('--- Endereço ---')
        print(f'Logradouro: {self.endereco.logradouro}, Nº {self.endereco.numero}')
        print(f'Cidade: {self.endereco.cidade} - {self.endereco.estado}')

def lista_esta_vazia(lista_alunos):
    if not lista_alunos:
        print('\nNão há alunos cadastrados.')
        return True
    return False

def adicionar_aluno(lista_alunos):
    print('\n--------- Adicionar novo Aluno ---------')
   
    nome = input('Nome: ')
    nascimento = input('Data de Nascimento: ')
    r_a = input('R.A: ')
    curso = input('Curso: ')
    
    print('--- Dados do Endereço ---')
    logradouro = input('Logradouro: ')
    numero = input('Número: ')
    cidade = input('Cidade: ')
    estado = input('Estado: ')

   
    novo_endereco = Endereço(logradouro, numero, cidade, estado)
    
    novo_aluno = Aluno(nome, nascimento, r_a, curso, novo_endereco)
    
    lista_alunos.append(novo_aluno)
    print(f'\nAluno {nome} adicionado com sucesso!')


def encontrar_por_ra(lista_alunos, ra_buscar):
    for aluno in lista_alunos:
        if aluno.r_a.lower() == ra_buscar.lower():
            return aluno
    return None

def mostrar_todos_alunos(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return

    print('\n---- Lista de Alunos ----')
    for aluno in lista_alunos:
        aluno.mostrar_dados()


def atualizar_aluno(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return

    mostrar_todos_alunos(lista_alunos)

    print('\n----- Atualizar dados do Aluno -----')
    ra_buscar = input('Digite o R.A do aluno: ')
    aluno = encontrar_por_ra(lista_alunos, ra_buscar)

    if aluno:
        print('\nAluno encontrado. Deixe em branco para manter o valor atual.\n')

       
        print(f'Nome atual: {aluno.nome}')
        novo_nome = input('Novo nome: ')
        
        print(f'Nascimento atual: {aluno.nascimento}')
        novo_nascimento = input('Nova data de nascimento: ')
        
        print(f'Curso atual: {aluno.curso}')
        novo_curso = input('Novo curso: ')

     
        print(f'Logradouro atual: {aluno.endereco.logradouro}')
        novo_logradouro = input('Novo logradouro: ')

        print(f'Número atual: {aluno.endereco.numero}')
        novo_numero = input('Novo número: ')
        
        print(f'Cidade atual: {aluno.endereco.cidade}')
        nova_cidade = input('Nova cidade: ')
        
        print(f'Estado atual: {aluno.endereco.estado}')
        novo_estado = input('Novo estado: ')

        if novo_nome: aluno.nome = novo_nome
        if novo_nascimento: aluno.nascimento = novo_nascimento
        if novo_curso: aluno.curso = novo_curso
        
        if novo_logradouro: aluno.endereco.logradouro = novo_logradouro
        if novo_numero: aluno.endereco.numero = novo_numero
        if nova_cidade: aluno.endereco.cidade = nova_cidade
        if novo_estado: aluno.endereco.estado = novo_estado

        print('\nDados atualizados com sucesso!')

    else:
        print(f'\nR.A {ra_buscar} não encontrado.')

# Excluir aluno
def excluir_aluno(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return

    mostrar_todos_alunos(lista_alunos)

    ra_buscar = input('\nDigite o R.A do aluno que deseja excluir: ')
    aluno = encontrar_por_ra(lista_alunos, ra_buscar)

    if aluno:
        lista_alunos.remove(aluno)
        print(f'\nAluno {aluno.nome} excluído com sucesso!')
    else:
        print('\nAluno não encontrado.')

while True:
    print("""
---- Gerenciador de Alunos ----
1 - Adicionar
2 - Mostrar todos
3 - Atualizar
4 - Excluir
0 - Sair
""")

    try:
        opcao = int(input('Digite uma opção: '))
    except ValueError:
        print('\nEntrada inválida. Digite um número.')
        time.sleep(2)
        os.system('cls')
        continue

    match opcao:
        case 1:
            adicionar_aluno(lista_alunos)
        case 2:
            mostrar_todos_alunos(lista_alunos)
        case 3:
            atualizar_aluno(lista_alunos)
        case 4:
            excluir_aluno(lista_alunos)
        case 0:
            print('\nSaindo do programa...')
            break
        case _:
            print('\nOpção inválida!')

    if opcao != 0:
        time.sleep(2)
        os.system('cls')