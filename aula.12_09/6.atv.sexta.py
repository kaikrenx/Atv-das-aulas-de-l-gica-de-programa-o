import streamlit as st

st.title("Laço de repetição - While")

nota = st.number_input("Digite uma nota: ", step=1)


if st.button("verificar"):
    if nota < 0 or nota > 10:
        st.error("A nota deve ser entre 0 a 10")
    else:
        st.info(f"Nota: {nota}")