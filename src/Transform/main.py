#Importando bibliotecas
import pandas as pd
import os
import sqlite3
import datetime

# Definir caminho para arquivo JSONL
df = pd.read_json('..\data\data.jsonl', lines=True)
print(df)