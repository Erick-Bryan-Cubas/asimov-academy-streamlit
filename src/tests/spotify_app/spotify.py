"""_summary_
"""
import os
import time
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Spotify Data Analysis",
    layout="wide"
)

st.title('Análise de Dados Spotify')

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
file_path = os.path.join(base_dir, 'src', 'data', 'raw', 'spotify.csv')

#st.write(f"Caminho absoluto do arquivo: {file_path}")

if os.path.exists(file_path):

    @st.cache_data
    def load_data():
        """_summary_
        Método para carregar os dados do arquivo csv
        """
        df = pd.read_csv(file_path)
        time.sleep(3)
        # Para operações pesadas
        return df
    df_spotify = load_data()
    # Persistindo os dados na sessão do browser
    st.session_state['df_spotify'] = df_spotify
    df_spotify.set_index("Track", inplace=True)
    #st.write(df_spotify)

    # Controlador de seleção dos artista
    artists = df_spotify['Artist'].value_counts().index
    artist = st.sidebar.selectbox("Artista", artists)

    # Controlador de seleção dos albuns
    albums = df_spotify[df_spotify['Artist'] == artist]['Album'].value_counts().index
    album = st.sidebar.selectbox('Album', albums)
    df_filtered_album = df_spotify[df_spotify['Album'] == album]

    # Controlador de exibição dos dados
    #display = st.checkbox("Mostrar dados em gráfico")
    #if display:
    #    st.bar_chart(df_filtered_album['Stream'])
    #else:
    #    st.write(df_filtered_album)

    col1, col2 = st.columns([0.7, 0.3])
    col1.bar_chart(df_filtered_album['Stream'])
    col1.line_chart(df_filtered_album['Danceability'])

    st.write(artist)

else:
    st.error(f"Arquivo não encontrado: {file_path}")
