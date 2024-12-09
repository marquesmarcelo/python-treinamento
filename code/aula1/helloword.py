import pandas as pd
from sqlalchemy import create_engine

# Configurando a conexão
engine = create_engine("postgresql+psycopg2://user:password@localhost/dbname")

# Leitura de uma tabela
df = pd.read_sql("SELECT * FROM tabela", engine)

# Exportar um DataFrame para o banco de dados
df.to_sql("tabela_nova", engine, if_exists="replace", index=False)