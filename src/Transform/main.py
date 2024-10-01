#Importando bibliotecas
import pandas as pd
import os
import sqlite3
from datetime import datetime

# Definir caminho para arquivo JSONL
df = pd.read_json('../data/data.jsonl', lines=True)

# Adicionar coluna _source com um valor fixo
df['_source'] =  "https://lista.mercadolivre.com.br/data-science"

# Setar pandas para mostrar todas as colunas
pd.options.display.max_columns = None

# Adicionar a coluna _data_coleta com a data e hora atuais
df['_data_extract'] = datetime.now()

# Tratar valores nulos para colunas numéricas e de texto
df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
df['old_price_centavos'] = df['old_price_centavos'].fillna(0).astype(float)
df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
df['new_price_centavos'] = df['old_price_centavos'].fillna(0).astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)

# Remover os parênteses das colunas 'reviews_amount'
df['reviews_amount'] = df['reviews_amount'].str.replace('[\(\)]','', regex=True)
df['reviews_amount'] = df['reviews_amount'].fillna(0).astype(int)

# Tratar preços como floats e calcular valores totais
df['old_price'] = df['old_price_reais'] + (df['old_price_centavos']/100)
df['new_price'] = df['new_price_reais'] +  (df['new_price_centavos']/100)

# Remover as colunas que não serão utilizadas no dashboard
df.drop(columns=['old_price_reais', 'old_price_centavos', 'new_price_reais', 'new_price_centavos'], axis=1)

# Conectar ao banco de dados SQLite3
conn = sqlite3.connect('../data/quotes.db')

# Salvar o Dataframe no banco de dados SQLite3
df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)

# Fechar a conexão com o banco de dados
conn.close()

print(df.head())
