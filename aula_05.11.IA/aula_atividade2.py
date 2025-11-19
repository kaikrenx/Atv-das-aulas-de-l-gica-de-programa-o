import os
import streamlit as st
from crewai import Agent, Task, Crew, Process, LLM    

# TABELA DE PRODUTOS (HAVAIANAS) PARA TESTES

products = [
    {'barcode': '7891234567001', 'name': 'Top preto 33/34', 'price': 30.50, 'stock_qty': 24, 'last_sold': '2025-09-27'},
    {'barcode': '7891234567002', 'name': 'Top preto 35/36', 'price': 32.50, 'stock_qty': 37, 'last_sold': '2025-09-20'},
    {'barcode': '7891234567003', 'name': 'Top branco 33/34', 'price': 33.00, 'stock_qty': 21, 'last_sold': None},
    {'barcode': '7891234567004', 'name': 'Top branco 35/36', 'price': 38.50, 'stock_qty': 10, 'last_sold': '2025-09-25'},
    {'barcode': '7891234567005', 'name': 'Top marinho 33/34', 'price': 31.00, 'stock_qty': 34, 'last_sold': '2025-09-25'},
    {'barcode': '7891234567006', 'name': 'Top marinho 35/36', 'price': 37.00, 'stock_qty': 38, 'last_sold': '2025-09-27'},
    {'barcode': '7891234567007', 'name': 'Top azul 33/34', 'price': 37.50, 'stock_qty': 6, 'last_sold': '2025-09-07'},
    {'barcode': '7891234567008', 'name': 'Top azul 35/36', 'price': 30.50, 'stock_qty': 13, 'last_sold': '2025-09-17'},
    {'barcode': '7891234567009', 'name': 'Top rubi 33/34', 'price': 39.50, 'stock_qty': 11, 'last_sold': '2025-09-27'},
    {'barcode': '7891234567010', 'name': 'Top rubi 35/36', 'price': 36.00, 'stock_qty': 21, 'last_sold': '2025-09-19'}]


sales = [

    # =======================
    # DIA 1 — 2025-10-01 (quarta)
    # até ~R$ 1100 total
    # =======================
    {'date': '2025-10-01', 'barcode': '7891234567008', 'name': 'Top azul 35/36', 'qty': 2, 'unit_price': 33.50, 'total': 67.00},
    {'date': '2025-10-01', 'barcode': '7891234567012', 'name': 'Top Logomania preto 35/36', 'qty': 1, 'unit_price': 41.50, 'total': 41.50},
    {'date': '2025-10-01', 'barcode': '7891234567022', 'name': 'Slim preto 35/36', 'qty': 1, 'unit_price': 52.00, 'total': 52.00},
    {'date': '2025-10-01', 'barcode': '7891234567009', 'name': 'Top rubi 33/34', 'qty': 3, 'unit_price': 39.50, 'total': 118.50},
    {'date': '2025-10-01', 'barcode': '7891234567032', 'name': 'Brasil Logo preto 35/36', 'qty': 2, 'unit_price': 55.00, 'total': 110.00},
    {'date': '2025-10-01', 'barcode': '7891234567017', 'name': 'Top Logomania azul 33/34', 'qty': 2, 'unit_price': 44.50, 'total': 89.00},
    {'date': '2025-10-01', 'barcode': '7891234567028', 'name': 'Slim azul 35/36', 'qty': 1, 'unit_price': 61.00, 'total': 61.00},
    {'date': '2025-10-01', 'barcode': '7891234567001', 'name': 'Top preto 33/34', 'qty': 4, 'unit_price': 30.50, 'total': 122.00},
    {'date': '2025-10-01', 'barcode': '7891234567023', 'name': 'Slim branco 33/34', 'qty': 1, 'unit_price': 54.50, 'total': 54.50},
    {'date': '2025-10-01', 'barcode': '7891234567035', 'name': 'Brasil Logo marinho 33/34', 'qty': 2, 'unit_price': 51.50, 'total': 103.00},

    # =======================
    # DIA 2 — 2025-10-02 (quinta)
    # =======================
    {'date': '2025-10-02', 'barcode': '7891234567004', 'name': 'Top branco 35/36', 'qty': 2, 'unit_price': 38.50, 'total': 77.00},
    {'date': '2025-10-02', 'barcode': '7891234567016', 'name': 'Top Logomania marinho 35/36', 'qty': 1, 'unit_price': 49.50, 'total': 49.50},
    {'date': '2025-10-02', 'barcode': '7891234567021', 'name': 'Slim preto 33/34', 'qty': 1, 'unit_price': 45.00, 'total': 45.00},
    {'date': '2025-10-02', 'barcode': '7891234567013', 'name': 'Top Logomania branco 33/34', 'qty': 3, 'unit_price': 44.00, 'total': 132.00},
    {'date': '2025-10-02', 'barcode': '7891234567031', 'name': 'Brasil Logo preto 33/34', 'qty': 1, 'unit_price': 52.50, 'total': 52.50},
    {'date': '2025-10-02', 'barcode': '7891234567027', 'name': 'Slim azul 33/34', 'qty': 2, 'unit_price': 42.50, 'total': 85.00},
    {'date': '2025-10-02', 'barcode': '7891234567005', 'name': 'Top marinho 33/34', 'qty': 4, 'unit_price': 31.00, 'total': 124.00},
    {'date': '2025-10-02', 'barcode': '7891234567029', 'name': 'Slim rubi 33/34', 'qty': 1, 'unit_price': 58.00, 'total': 58.00},
    {'date': '2025-10-02', 'barcode': '7891234567034', 'name': 'Brasil Logo branco 35/36', 'qty': 2, 'unit_price': 57.50, 'total': 115.00},
    {'date': '2025-10-02', 'barcode': '7891234567018', 'name': 'Top Logomania azul 35/36', 'qty': 1, 'unit_price': 41.00, 'total': 41.00},

    # =======================
    # DIA 3 — 2025-10-03 (sexta)
    # =======================
    {'date': '2025-10-03', 'barcode': '7891234567007', 'name': 'Top azul 33/34', 'qty': 2, 'unit_price': 37.50, 'total': 75.00},
    {'date': '2025-10-03', 'barcode': '7891234567026', 'name': 'Slim marinho 35/36', 'qty': 1, 'unit_price': 67.50, 'total': 67.50},
    {'date': '2025-10-03', 'barcode': '7891234567002', 'name': 'Top preto 35/36', 'qty': 3, 'unit_price': 32.50, 'total': 97.50},
    {'date': '2025-10-03', 'barcode': '7891234567036', 'name': 'Brasil Logo marinho 35/36', 'qty': 1, 'unit_price': 48.50, 'total': 48.50},
    {'date': '2025-10-03', 'barcode': '7891234567024', 'name': 'Slim branco 35/36', 'qty': 1, 'unit_price': 59.00, 'total': 59.00},
    {'date': '2025-10-03', 'barcode': '7891234567019', 'name': 'Top Logomania rubi 33/34', 'qty': 2, 'unit_price': 47.50, 'total': 95.00},
    {'date': '2025-10-03', 'barcode': '7891234567006', 'name': 'Top marinho 35/36', 'qty': 2, 'unit_price': 37.00, 'total': 74.00},
    {'date': '2025-10-03', 'barcode': '7891234567030', 'name': 'Slim rubi 35/36', 'qty': 1, 'unit_price': 64.50, 'total': 64.50},
    {'date': '2025-10-03', 'barcode': '7891234567011', 'name': 'Top Logomania preto 33/34', 'qty': 1, 'unit_price': 46.50, 'total': 46.50},
    {'date': '2025-10-03', 'barcode': '7891234567003', 'name': 'Top branco 33/34', 'qty': 3, 'unit_price': 33.00, 'total': 99.00},

    # =======================
    # DIA 4 — 2025-10-04 (sábado — vendas maiores)
    # =======================
    {'date': '2025-10-04', 'barcode': '7891234567008', 'name': 'Top azul 35/36', 'qty': 4, 'unit_price': 33.50, 'total': 134.00},
    {'date': '2025-10-04', 'barcode': '7891234567026', 'name': 'Slim marinho 35/36', 'qty': 2, 'unit_price': 67.50, 'total': 135.00},
    {'date': '2025-10-04', 'barcode': '7891234567035', 'name': 'Brasil Logo marinho 33/34', 'qty': 3, 'unit_price': 51.50, 'total': 154.50},
    {'date': '2025-10-04', 'barcode': '7891234567023', 'name': 'Slim branco 33/34', 'qty': 2, 'unit_price': 54.50, 'total': 109.00},
    {'date': '2025-10-04', 'barcode': '7891234567015', 'name': 'Top Logomania marinho 33/34', 'qty': 4, 'unit_price': 40.00, 'total': 160.00},
    {'date': '2025-10-04', 'barcode': '7891234567001', 'name': 'Top preto 33/34', 'qty': 5, 'unit_price': 30.50, 'total': 152.50},
    {'date': '2025-10-04', 'barcode': '7891234567032', 'name': 'Brasil Logo preto 35/36', 'qty': 2, 'unit_price': 55.00, 'total': 110.00},
    {'date': '2025-10-04', 'barcode': '7891234567029', 'name': 'Slim rubi 33/34', 'qty': 2, 'unit_price': 58.00, 'total': 116.00},
    {'date': '2025-10-04', 'barcode': '7891234567012', 'name': 'Top Logomania preto 35/36', 'qty': 3, 'unit_price': 41.50, 'total': 124.50},
    {'date': '2025-10-04', 'barcode': '7891234567028', 'name': 'Slim azul 35/36', 'qty': 1, 'unit_price': 61.00, 'total': 61.00}]


# AGENTES DE AUXILIO DE PREVISÃO DE VENDA
st.header("Agentes de previsão")
st.write("Informe os produtos que mais estão vendendo.")

tema = st.text_input("Sobre o que deseja saber? ", placeholder="Exemplo: Qual produto investir mais?")
objetivo = st.text_input("Objetivo:", placeholder="Exemplo: Ver qual produto tem maior potencial de venda") 

executar = st.button("Gerar Material de Previsão")
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
        role="Verificar Previsão",
        goal=(
            "Verificar os {products} e  {sales} para responder o {tema}, Não invente nada que não esteja nos dados fornecidos, "
            "alinhado com o objetivo {objetivo}. "
            "Deve ser direto ao ponto, focado nas melhores possibilidades de futuras vendas e ajuste de estoque."
        ),
        backstory="Especialista em análise de vendas, estoque e previsão de demanda, utilizando dados históricos para orientar decisões de negócios.",
        llm=llm, verbose=False
    )

    # Agente 2: criador de previsões de venda
    agente_exemplos = Agent(
        role="Criador de previsões de venda e melhor ajuste de estoque",
        goal=(
            "Gerar 5 vias para o {tema}, cada uma com pontos fortes, "
            "probabilidade estimada de eficiencia e mudanças recomendadas."
        ),
        backstory="Criador de combinações mudanças de estoque seguras e lucrativas, baseado em dados reais de vendas.",
        llm=llm, verbose=False
    )

       # Tarefa 1 — visão geral
    t_resumo = Task(
        description=(
            "RESUMO: Explique o panorama geral das vendas usando {products} e {sales}, "
            "incluindo quais produtos mais vendem, padrões de dias mais fortes e pontos importantes para {objetivo}. "
            "Texto curto e objetivo, sem inventar nada fora dos dados."
        ),
        agent=agente_verificador,
        expected_output="Resumo em markdown, com análise direta e clara."
    )

    # Tarefa 2 — estratégias de venda
    t_exemplos = Task(
        description=(
            "Crie 5 estratégias de venda para o tema {tema}, usando somente os dados de {products} e {sales}, "
            "cada uma com título em negrito, cenário descrito, justificativa baseada nas vendas, "
            "ajuste de estoque recomendado e probabilidade aproximada de funcionar bem."
        ),
        agent=agente_exemplos,
        expected_output="Lista de 5 estratégias, bem organizadas e em markdown."
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
        "objetivo": objetivo or "não informado",
        "products": products,
        "sales": sales
    })

    # Resultados
    resumo_out = getattr(t_resumo, "output", "") or ""
    exemplos_out = getattr(t_exemplos, "output", "") or ""

    # Abas
    aba_resumo, aba_exemplos = st.tabs(
        ["Resumo", "Estratégias"]
    )

    with aba_resumo:
        st.markdown("### Visão geral das vendas")
        st.markdown(resumo_out)

    with aba_exemplos:
        st.markdown("### Estratégias sugeridas")
        st.markdown(exemplos_out)

