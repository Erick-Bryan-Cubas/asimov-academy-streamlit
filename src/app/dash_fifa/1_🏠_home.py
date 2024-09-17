import os
import webbrowser
import streamlit as st
import pandas as pd
from datetime import datetime


base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
file_path = os.path.join(base_dir, 'data', 'raw', 'CLEAN_FIFA23_official_data.csv')

if "data" not in st.session_state:
    df_data = pd.read_csv(file_path, index_col=0)
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    df_data = df_data[df_data['Value(£)'] > 0]
    df_data = df_data.sort_values(by='Overall', ascending=False)
    st.session_state["data"] = df_data

st.markdown("# FIFA World Cup 2023 ⚽")
st.sidebar.markdown("Desenvolvido por [Erick Bryan Cubas](https://www.linkedin.com/in/the-bryan/)")

btn = st.button("Acesse os dados no Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown(
    """
## Conjunto de Dados de Jogadores de Futebol (2017-2023)

Este conjunto de dados oferece uma visão abrangente sobre jogadores de futebol profissionais, com informações detalhadas que abrangem:

- **Dados Demográficos**: Informações pessoais dos jogadores.
- **Características Físicas**: Atributos físicos e de desempenho.
- **Estatísticas de Jogo**: Métricas detalhadas de desempenho em campo.
- **Detalhes do Contrato**: Informações sobre os contratos dos jogadores.
- **Afiliações de Clubes**: Dados sobre os clubes com os quais os jogadores estiveram associados.

Com **mais de 17.000 registros**, este recurso é valioso para analistas de futebol, pesquisadores e entusiastas que desejam explorar diversos aspectos do mundo do futebol. Ele permite o estudo de:

- Atributos dos jogadores
- Métricas de desempenho
- Avaliação de mercado
- Análise de clubes
- Posicionamento dos jogadores
- Desenvolvimento dos jogadores ao longo do tempo

"""
)
