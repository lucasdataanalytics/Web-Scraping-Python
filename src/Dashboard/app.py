import streamlit as st
import pandas as pd
import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('../data/quotes.db')

# Carregar os dados da tabela 'mercadolivre_items' em um DataFrame pandas
df = pd.read_sql_query("SELECT * FROM mercadolivre_items", conn)

# Fechar a conexão com o banco de dados
conn.close()

# Título da aplicação
st.title('Pesquisa de Mercado - Livros de Data Science no Mercado Livre')

# Melhorar o layout com colunas para KPIs
st.subheader('KPIs principais do sistema')
col1, col2, col3 = st.columns(3)

# KPI 1: Número total de itens
total_itens = df.shape[0]
col1.metric(label="Número Total de Itens", value=total_itens)

# KPI 2: Preço médio novo (em reais)
average_new_price = df['new_price'].mean()
col2.metric(label="Preço Médio Novo (R$)", value=f"{average_new_price:.2f}")

# KPI 3: Preço mais alto
highest_price = df['new_price'].max()
col3.metric(label="Preço Mais Alto (R$)", value=f"{highest_price:.2f}")

# Filtro de Preços
st.subheader('Filtrar por Intervalo de Preço')
min_price, max_price = st.slider('Selecione o intervalo de preço', 
                                   0, 
                                   int(df['new_price'].max()), 
                                   (0, int(df['new_price'].max())))

df_filtered = df[(df['new_price'] >= min_price) & (df['new_price'] <= max_price)]
st.dataframe(df_filtered)

# Seção para títulos mais encontrados até a 10ª página
st.subheader('Títulos mais encontrados até a 10ª página')
col1, col2 = st.columns([4, 2])

# Gráfico de barras dos títulos mais encontrados
top_10_pages_names = df['name'].value_counts().head(10)  # Top 10 títulos mais encontrados
col1.bar_chart(top_10_pages_names)

# Exibir a tabela dos títulos mais encontrados
col2.dataframe(top_10_pages_names)

# Adição de um histograma para a distribuição de preços
st.subheader('Distribuição de Preços')
st.bar_chart(df['new_price'].value_counts().sort_index())

# Tabela de Itens com mais avaliações
st.subheader('Itens com mais avaliações')
top_reviewed = df[['name', 'reviews_amount']].sort_values(by='reviews_amount', ascending=False).head(10)
st.dataframe(top_reviewed)