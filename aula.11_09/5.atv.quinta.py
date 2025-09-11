import streamlit as st 
import time

n1= st.number_input("Digite um Número", step=1, key=1)
n2= st.number_input("Digite um Número", step=1, key=2)
n3= st.number_input("Digite um Número", step=1, key=3)
n4= st.number_input("Digite um Número", step=1, key=4)
n5= st.number_input("Digite um Número", step=1, key=5)
 
soma = n1 + n2 + n3 + n4 + n5

if st.button("Calcule"):
    soma = n1 + n2 + n3 + n4 + n5
    st.success(f"a soma de todos os números é de: {soma}")






    import streamlit as st
import time

st.title("Atividade")

st.header("Laço de repetição - For")

st.write("Escrever um programa de computador que solicite do usuário 5 " \
"números inteiros e, ao final, apresente a soma de todos os números lidos.")

soma = 0

for i in range(1,6):
    numero = st.number_input(f"Digite o {i}º número: ", step=1, min_value=0)
    soma = soma + numero
    time.sleep(1)    
   
if st.button("Iniciar"):
    st.success(f"A soma do números é: {soma}")
else:
    st.info("Informe um número")