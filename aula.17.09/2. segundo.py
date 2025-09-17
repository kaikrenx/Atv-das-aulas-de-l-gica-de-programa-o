import streamlit as st

st.title("Laço de repetição")


st.write("Escreva um algoritmo que solicite duas notas para um aluno" \
"caso seja menor que 0 ou maior que 10, mpstre a pergunta novamente" \
"Calcule e mostre a média aritimética do aluno")


nota1 = st.number_input("Digite a primeira nota: ", min_value=0, max_value=10)
nota2 = st.number_input("Digite a segunda nota: ", min_value=0, max_value=10)


media = (nota1 + nota2) / 2

if st.button("Calcular média"):
    st.info(f"Média: {media: .2f}")