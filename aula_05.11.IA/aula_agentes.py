import os
import streamlit as st
from crewai import Agent, Task, Crew, Process, LLM    

# AGENTES PARA ESTUDO.
st.header("Agentes para Estudo")
st.write("informe O tema e gere material para estudar:.")

tema = st.text_input("Tema para estudo:", placeholder="Exemplo: Algoritmos")
objetivo = st.text_input("Objetivo:", placeholder="Exemplo: Entender conceitos") 

executar = st.button("Gerar Material de Estudo")
api_key = ""

if executar:
    # Características do LLM
    llm = LLM(
        model = "groq/llama-3.3-70b-versatile",
        api_key=api_key,
        temperature=0.3
        # Temperature: define o nivel de criatividade.
        # <= 0.3 mais deterministico.
        # entre 0.4 e 0.7 equilibrado para explicação
        # maior que 0.7 mais criativo e menos previsivel.
    )

    # Agentes
    agente_resumo = Agent(
        role="Redator de resumo didático",
        goal=(
            "Escrever RESUMO claro e didático sobre o {tema} alinhado com o {objetivo}. "
            "A linguagem deve ser didática, direta com contexto prático e sem jargões. "
        ),
        backstory="Você transforma temas técnicos/acadêmicos em explicações curtas e precisas",
        llm=llm, verbose=False
    )

    agente_exemplos = Agent(
        role="criador de exemplos contextualizados",
        goal=(
            "Gerar 5 EXEMPLOS curtos sobre {tema}, cada um com contexto realista."
            "Cada exemplo com título (em negrito), cenário, dados(se houver), aplicação e resultado"
        ),
        backstory="Você mostra o conceito em ação com exemplos breves e concretos.",
        llm=llm, verbose=False
    )

    agente_exercicios = Agent(
        role="Criador de exercícios práticos",
        goal=(
            "Criar 4 EXERCÍCIOS SIMPLES sobre {tema}."
            "Variar o formato(Múltipla escolha, verdadeiro/falso, completar, resolução curta)."
        ),
        backstory="Você cria atividades rápidas que fixam os conceitos essenciais",
        llm=llm, verbose=False
    )

    agente_gabarito = Agent(
        role="Revisor e gabaritador",
        goal=(
            "Ler os EXERCÍCIOS sobre {tema} e produzir o GABARITO oficial. "
            "Com respostas corretas e justificativa breve (1-3 frases) por item."
        ),
        backstory="Você confere consistênia e explica rapidamente o porquê da resposta.",
        llm=llm, verbose=False
    )

    # Tarefas
    t_resumo = Task(
        description=(
            "RESUMO: escreva em português do brasil um resumo didático sobre {tema} e objetivo {objetivo}. "
            "Inclua:  definição (3-4 frases), por que importa (2-3), onde se aplica (2,3) e conceitos chave (lista com 4-6 itens)."
        ),
        agent=agente_resumo,
        expected_output="Resumo em markedown com título, paragráfos curtos e 4-6 marcadores (bullets)."
    )

    t_exemplos = Task(
        description="EXEMPLOS: produza 4 exemplos contextualizados e curtos sobre {tema}."
        "Padrão (até 5 linhas cada): Título, cenário, dados/entrada, como aplicar (1-2 frases), resulta (1-2 frases).",
        agent=agente_exemplos,
        expected_output="5 exemplos em markdown com títulos em negrito e estrutura clara."
    )

    t_exercicios = Task(
        description=(
            "EXERCÍCIOS: crie 4 exercícios simples sobre {tema} em PT-BR."
            "Várie formatos e não inclua respostas."
            "Entregue lista numerada (1-4) em Markdown"
        ),
        agent=agente_exercicios,
        expected_output="Lista numerada (1-4) com exercícios simples, sem respostas."
    )

    t_gabarito = Task(
        description=(
            "GABARITO: Com base nos EXERCÍCIOS fornecido no contexto, produza o gabarito oficial."
            "Para cada item, dê: \n"
            "- Resposta: (letra, valor, solução)\n"
            "- comentário: justificativa breve e direta (1-2 frases)< citando o conceito-chave \n"
            "Formato: lista numeradoa (1 a 3) em Markdown."
        ),
        agent=agente_gabarito,
        expected_output="Lista numerada (1-3) com respostas e comentários.",
        context=[t_exercicios]
    )

    # Definindo equipe.
    agents = [agente_resumo, agente_exemplos, agente_exercicios, agente_gabarito]
    Tasks = [t_resumo, t_exemplos, t_exercicios, t_gabarito]
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

    # Exibindo resultados.
    resumo_out = getattr(t_resumo, "output", None) or getattr(t_resumo, "result", "") or ""
    exemplos_out = getattr(t_exemplos, "output", None) or getattr(t_exemplos, "result", "") or ""
    exercicios_out = getattr(t_exercicios, "output", None) or getattr(t_exercicios, "result", "") or ""
    gabarito_out = getattr(t_gabarito, "output", None) or getattr(t_gabarito, "result", "") or ""

    # Abas para mostrar os resultados.
    aba_resumo, aba_exemplos, aba_exercicios, aba_gabarito = st.tabs(
        ["Resumo", "Exemplos", "Exercícios", "Gabarito"]
    )

    with aba_resumo:
        st.markdown("### Resumo Didático")
        st.markdown(resumo_out)
    with aba_exemplos:
        st.markdown("### Exemplos Contextualizados")
        st.markdown(exemplos_out)
    with aba_exercicios:
        st.markdown("### Exercícios Práticos")
        st.markdown(exercicios_out)
    with aba_gabarito:
        st.markdown("### Gabarito Oficial")
        st.markdown(gabarito_out)

# Fim do código.
