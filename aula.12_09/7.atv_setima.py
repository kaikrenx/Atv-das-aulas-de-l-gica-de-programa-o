import streamlit as st
import time


st.title("Atividade")


st.header("Laço de repetição - For")
nota = 0


for i in range(2):
    
    soma = st.number_input(f"Digite a {i+1}ª nota para saber a nota", step=1, min_value=0, max_value=10)
    
    nota = nota + soma
    

    media = nota / 2
    

if st.button("Verificar a média"):

    if media >= 7:
        st.success(f"Você foi aprovado, aqui a sua média: {media: .2f}")
    elif media >= 4 and media < 7:
        st.warning(f"Você está de recuperação, aqui sua média: {media: .2f}")
    else:
        st.error(f"Você foi reprovado, aqui sua média: {media: .2f}")