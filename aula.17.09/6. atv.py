import streamlit as st
import time

st.title("LAÇO DE LOGIN")

usuario1 = "pac@gmail.com"
senha1 = "123"

st.session_state.setdefault("desabilitar", False)
st.session_state.setdefault("tentativas", 0)



usuario = st.text_input("Digite seu email: ", disabled=st.session_state.desabilitar)
senha = st.text_input("Digite sua senha: ", type="password", disabled=st.session_state.desabilitar)


if st.button("Logar"):

    if usuario == usuario1 and senha == senha1:
        st.success("Bem-vindo rosca alada")

    else: 
        st.session_state.tentativas += 1
        if st.session_state.tentativas <= 3: 
            st.error(f"Email ou senha incorretos, tentativas: {st.session_state.tentativas}")

        else:
            st.session_state.desabilitar = True
            st.error("Número de tentativas inválidas.")