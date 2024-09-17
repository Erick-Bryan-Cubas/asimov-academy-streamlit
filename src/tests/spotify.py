"""_summary_
"""
import os
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Spotify Data Analysis",
    layout="wide"
)

st.title('Análise de Dados Spotify')
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
file_path = os.path.join(base_dir, 'src', 'data', 'raw', 'spotify.csv')

#st.write(f"Caminho absoluto do arquivo: {file_path}")

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    df.set_index("Track", inplace=True)
    #st.write(df)

    # Controlador de seleção dos artista
    artists = df['Artist'].value_counts().index
    artist = st.sidebar.selectbox("Artista", artists)

    # Controlador de seleção dos albuns
    albums = df[df['Artist'] == artist]['Album'].value_counts().index
    album = st.sidebar.selectbox('Album', albums)

    # Botão de filtro
    if st.sidebar.button("Filtrar"):
        df_filtered = df[df['Artist'] == artist]
        df_filtered_album = df_filtered[df_filtered['Album'] == album]

        col1, col2 = st.columns([0.7, 0.3])
        col1.bar_chart(df_filtered_album['Stream'])
        col1.line_chart(df_filtered_album['Danceability'])

        st.write(artist)
    else:
        st.write("⚠️ Clique no botão para filtrar")

else:
    st.error(f"Arquivo não encontrado: {file_path}")
