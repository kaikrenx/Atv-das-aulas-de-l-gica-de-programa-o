Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 14/08/2025
Var
// Seção de Declarações das variáveis 

   numeros: real
   sucessor, a: real
   antecessor, b: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...


  escreval("Digite Um Número: ")
  leia(numeros)

  sucessor <- numeros + 1
  antecessor <- numeros - 1
  
  //pula uma linha
  escreval("Antecessor: ", antecessor)
  //pula uma linha
  escreval("Numero escolhido: ", numeros)
  //pula uma linha
  escreval("Sucessor: ", sucessor)
    //pula uma linha
  escreval("Agora ao quadrado, digite um numero: ")
  leia(numeros)
    //pula uma linha
  sucessor <- numeros * numeros
  antecessor <- numeros * 1
  
    //pula uma linha
    
    escreval("Sucessor ao quadrado: ", sucessor)
    escreval("Antecessor do ao quadrado: ", antecessor)


Fimalgoritmo