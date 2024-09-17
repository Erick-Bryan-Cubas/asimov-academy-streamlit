import streamlit as st

st.set_page_config(
    page_title='Teams',
    page_icon=':soccer:',
    layout='wide'
)

df_data = st.session_state["data"]

clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox("Selecione um clube", clubes)

# Filtrando os dados do clube selecionado e definindo o índice como o nome do jogador
df_filtered = df_data[(df_data['Club'] == club)].set_index('Name')

st.image(df_filtered.iloc[0]['Club Logo'])
st.markdown(f'## {club}')


columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']

st.dataframe(df_filtered[columns],
             column_config={
                 # Valor de mercado do jogador
                "Overall": st.column_config.ProgressColumn(
                     "Overall", format="%d", min_value=0, max_value=100
                 ),
                 # Valor de remuneração semanal mínimo e máximo para o jogador
                "Wage(£)": st.column_config.ProgressColumn(
                        "Weekly Wage", format="£%d", min_value=0,
                        max_value=df_filtered['Wage(£)'].max()
                    ),
                # Coluna de imagem do jogador
                "Photo": st.column_config.ImageColumn("Photo"),
                # Coluna de imagem da bandeira do país do jogador
                "Flag": st.column_config.ImageColumn("Flag"),
             })
