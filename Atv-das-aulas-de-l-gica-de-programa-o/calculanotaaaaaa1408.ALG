Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/08/2025
Var
// Seção de Declarações das variáveis 
   NOME: CARACTERE
   IDADE: CARACTERE
   Nota_matematica: REAL
   Nota_Portugues: REAL
   Nota_ciencias: Real
   soma: real
   media: real
   minima: real
   pendente: real
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

   escreva("Nome do Aluno: ")
   leia(NOME)
    //pular uma linha
   escreva("Idade do aluno: ")
   leia(IDADE)
     //pular uma linha
   escreva("Escreva sua nota de matématica: ")
   leia(Nota_matematica)
     //pular uma linha
   escreva("Escreva sua nota de português: ")
   leia(Nota_portugues)
   escreva("Escreva sua nota de ciencias: ")
   leia(Nota_ciencias)
        //pular uma linha
   soma <- Nota_matematica + Nota_portugues + Nota_ciencias
   media <- soma / 3
   minima <- 7
   pendente <- minima - media
   //pula uma linha
   se media >= minima entao
    escreval ("Aluno passou!!! confira: ")
    senao
    escreval("Aluno perdeu :( confira: ")
    escreval("O aluno precisa de: ", pendente," para alcançar a média")

fimse

    //pular uma linha

   escreval ("-------------------------------------------")
   escreval("Média aritmetica do aluno: ", media)





Fimalgoritmo