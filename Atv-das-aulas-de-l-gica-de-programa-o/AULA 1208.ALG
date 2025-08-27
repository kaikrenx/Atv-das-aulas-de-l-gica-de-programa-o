Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 19/12/2024
Var
// Seção de Declarações das variáveis 

   nome: caractere
   idade: inteiro
   altura: real
   peso: real
   Faculdade: caractere
   Curso: caractere
   semestre: real
   resposta: caractere
   IMC: real
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   escreva("digite seu nome: ")
   leia (nome)
   escreva("digite sua idade: ")
   leia (idade)
   escreva("altura: ")
   leia(altura)
   escreva("peso: ")
   leia (peso)
   escreva("faculdade: ")
   leia(faculdade)
   escreva("curso: ")
   leia(curso)
   escreva("semestre, ex: 2025.2/ diga: ")
   leia(semestre)


   escreval //pula uma linha.
   escreval("= exibindo dados = ")
   escreval("Nome: ", nome)
   escreval("Idade: ", idade)
   escreval("Altura: ", altura)
   escreval("Peso: ", peso)
   escreval ("Faculdade: ", faculdade)
   escreval("curso: ", curso)
   escreval("semestre: ",semestre)
    //pula uma linha
    escreval
   escreva("Quer calcular seu IMC? (sim ou não): ")
   leia(resposta)

   se resposta = "não" entao
      escreval("Obrigado Aluno!")
   senao
      imc <- peso / (altura * altura)
      escreval("IMC: ", imc:4:2)

      fimse

Fimalgoritmo