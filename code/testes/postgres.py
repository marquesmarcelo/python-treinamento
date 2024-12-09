import psycopg
import pandas as pd
import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

db_host = os.environ.get("DB_HOST")
db_name = os.environ.get("DB_NAME")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_port = os.environ.get("DB_PORT")

# Conectar ao banco de dados PostgreSQL
conn = psycopg.connect(
    host=db_host,
    dbname=db_name,
    user=db_user,
    password=db_password,
    port=db_port
)

# Executar a consulta e carregar os resultados em um DataFrame
with conn.cursor() as cur:
    cur.execute("SELECT id, nome FROM cliente;")
    # Fetchall para obter todos os resultados
    data = cur.fetchall()
    # Obter os nomes das colunas da consulta
    colunas = [desc[0] for desc in cur.description]

# Fechar a conexão
conn.close()

# Criar o DataFrame a partir dos resultados
df = pd.DataFrame(data, columns=colunas)

# Exibir o DataFrame
print(df)
