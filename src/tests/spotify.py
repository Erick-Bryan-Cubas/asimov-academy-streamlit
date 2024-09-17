"""_summary_
"""
import os
import streamlit as st
import pandas as pd

st.title('Análise de Dados Spotify')
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
file_path = os.path.join(base_dir, 'src', 'data', 'raw', 'spotify.csv')

#st.write(f"Caminho absoluto do arquivo: {file_path}")

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    df.set_index("Artist", inplace=True)
    #st.write(df)
    st.line_chart(df[df['Stream'] > 1000000000]['Stream'])
else:
    st.error(f"Arquivo não encontrado: {file_path}")
