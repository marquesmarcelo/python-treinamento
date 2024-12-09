import pandas as pd
import psycopg2

# Conexão com o PostgreSQL
connection = psycopg2.connect(
    host="localhost",
    database="sua_base",
    user="seu_usuario",
    password="sua_senha",
    port=5432
)

# Leitura de uma tabela para um DataFrame
query = "SELECT * FROM tabela"
df = pd.read_sql(query, connection)

# Fechar a conexão
connection.close()