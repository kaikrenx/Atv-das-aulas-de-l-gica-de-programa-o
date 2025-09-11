import streamlit as st

st.title("Tabuada")

numero = st.number_input("Digite um Número", step=1)

if st.button("Calcular"):
    for i in range(1, 11, 1):
        st.success(f"{numero} X {i} = {numero * i}")
        