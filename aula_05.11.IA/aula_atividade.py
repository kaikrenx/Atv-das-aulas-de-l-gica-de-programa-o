import os
import streamlit as st
from crewai import Agent, Task, Crew, Process, LLM    

# AGENTES PARA APOSTA 
st.header("Agentes de aposta")
st.write("Informe o campeonato que deseja ver as probabilidades.")

tema = st.text_input("Campeonato: ", placeholder="Exemplo: Brasileirão Série A")
objetivo = st.text_input("Objetivo:", placeholder="Exemplo: Ver melhores múltiplas") 

executar = st.button("Gerar Material de Aposta")
api_key = ""

if executar:
    # Características do LLM
    llm = LLM(
        model="groq/llama-3.3-70b-versatile",
        api_key=api_key,
        temperature=0.1
    )

    # Agente 1: verificador
    agente_verificador = Agent(
        role="Verificar probabilidades",
        goal=(
            "Verificar PROBABILIDADES de resultado do campeonato {tema}, "
            "alinhado com o objetivo {objetivo}. "
            "Deve ser direto ao ponto, focado nas melhores possibilidades de aposta."
        ),
        backstory="Especialista em análise de dados esportivos e apostas.",
        llm=llm, verbose=False
    )

    # Agente 2: criador de múltiplas
    agente_exemplos = Agent(
        role="Criador de múltiplas",
        goal=(
            "Gerar 5 múltiplas de aposta do {tema}, cada uma com pontos fortes, "
            "probabilidade estimada e valor recomendado."
        ),
        backstory="Criador de combinações de apostas seguras e lucrativas.",
        llm=llm, verbose=False
    )

    # Tarefa 1 — visão geral
    t_resumo = Task(
        description=(
            "RESUMO: Explique o panorama geral do campeonato {tema}, "
            "incluindo momento dos times, tendências e aspectos importantes para {objetivo}. "
            "Texto curto e objetivo."
        ),
        agent=agente_verificador,
        expected_output="Resumo em markdown, com análise direta e clara."
    )

    # Tarefa 2 — múltiplas
    t_exemplos = Task(
        description=(
            "Crie 5 múltiplas de aposta para o campeonato {tema}, "
            "cada uma com título em negrito, cenário, justificativa e valor recomendado e pelo menos 70% chance de acerto."
        ),
        agent=agente_exemplos,
        expected_output="Lista de 5 múltiplas, bem organizadas e em markdown."
    )

    # Criando equipe
    agents = [agente_verificador, agente_exemplos]
    Tasks = [t_resumo, t_exemplos]

    crew = Crew(
        agents=agents,
        tasks=Tasks,
        llm=llm,
        process=Process.sequential
    )

    crew.kickoff(inputs={
        "tema": tema,
        "objetivo": objetivo or "não informado"
    })

    # Resultados
    resumo_out = getattr(t_resumo, "output", "") or ""
    exemplos_out = getattr(t_exemplos, "output", "") or ""

    # Abas
    aba_resumo, aba_exemplos = st.tabs(
        ["Resumo", "Múltiplas"]
    )

    with aba_resumo:
        st.markdown("### Visão geral do campeonato")
        st.markdown(resumo_out)

    with aba_exemplos:
        st.markdown("### Múltiplas sugeridas")
        st.markdown(exemplos_out)
