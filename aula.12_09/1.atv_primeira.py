import streamlit as st 
import time

st.title("Atividade")

st.header("Laço de repetição - For")

pares = 0
impares = 0


for i in range(1,6):
    numero = st.number_input(f"Digite o {i}º número: ", step=1, min_value=0)
    if numero % 2 == 0:
        pares = pares + 1
    else: 
        impares = impares + 1

if st.button("Verificar"):
        st.success(f"Quantidade de pares: {pares}")
        st.info(f"Quantidade de ímpares: {impares}")
