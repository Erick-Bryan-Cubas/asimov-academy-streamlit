import streamlit as st

st.set_page_config(
    page_title='Players',
    page_icon=':soccer:',
    layout='wide'
)

df_data = st.session_state["data"]

# Controladores de seleção de clube e jogador
# clubes = df_data['Club'].nunique()
clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox("Selecione um clube", clubes)

df_players = df_data[(df_data['Club'] == club)]
players = df_players['Name'].value_counts().index
player = st.sidebar.selectbox("Selecione um jogador", players)

player_stats = df_data[df_data['Name'] == player].iloc[0]

# Exibindo a foto do jogador e o nome
st.image(player_stats['Photo'])
st.title(player_stats['Name'])

# Exibindo o clube e a posição do jogador
st.markdown(f"**Clube**: {player_stats['Club']}")
st.markdown(f"**Posição**: {player_stats['Position']}")

# Exibindo a nacionalidade do jogador
col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade**: {player_stats['Age']}")
col2.markdown(f"**Altura**: {player_stats['Height(cm.)']} cm")
col3.markdown(f"**Peso**: {round((player_stats['Weight(lbs.)'] * 0.453), 2)} kg")
st.divider()

# Exibindo o overall do jogador
st.subheader(f"Overall: {player_stats['Overall']}")
# Barra de progresso para exibir o overall do jogador
st.progress(int(player_stats['Overall']))

# Exibindo as estatísticas do jogador
col1, col2, col3, col4 = st.columns(4)
col1.metric(label='Valor de mercado', value=f"${player_stats['Value(£)']:,}")
col2.metric(label='Remuneracao Semanal', value=f"${player_stats['Wage(£)']:,}")
col3.metric(label='Cláusula de Rescisão', value=f"${player_stats['Release Clause(£)']:,}")