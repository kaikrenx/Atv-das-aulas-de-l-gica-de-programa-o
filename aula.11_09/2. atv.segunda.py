import streamlit as st
import time


st.title("NÚMEROS ÍMPARES ENTRE 1 E 20")
st.header("contagem")

if st.button("CALCULAR"):
    for i in range(1,21, 2):
        st.info(i)
        time.sleep(1)