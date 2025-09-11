import streamlit as st

import streamlit as st
import time 


st.title("Laço de repetição - FOR ")
st.header ("Contagem de 100 a 120.")


if st.button("Iniciar"):
    for i in range (100,122, 2):
        st.sucess(i)
        time.sleep(1)
    st.header("FIM")