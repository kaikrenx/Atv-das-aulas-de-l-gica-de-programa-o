import streamlit as st
import time 




st.title("Atividade")

st.header("Laço de repetição - For")
nota = 0


for i in range(4):
   
    soma = st.number_input(f"Digite a {i}ª nota para saber a nota (são quatro)", step=1, min_value=0)
    
    nota = nota + soma
    

    media = nota / 4

if st.button("Verificar a média"):
    media = nota / 4
    st.info(f"aqui a sua média: {media}")


