import streamlit as st
import time

st.title("LAÇO DE LOGIN")

usuario1 = "pac@gmail.com"
senha1 = "123"


usuario = st.text_input("Digite seu email: ")
senha = st.text_input("Digite sua senha: ", type="password")


if st.button("Logar"):

    if usuario == usuario1 and senha == senha1:
        st.success("Bem-vindo rosca alada")

    else: 
        st.error("Email ou senha incorretos")