import pandas as pd
import os

# Diretório do script
diretorio_script = os.path.dirname(os.path.abspath(__file__))

# Caminho relativo (dois níveis acima)
caminho_arquivo = os.path.join(diretorio_script, r"..\..\assets\cliente.xlsx")

# Lendo a planilha
df = pd.read_excel(caminho_arquivo)

# Exibindo as primeiras linhas do DataFrame
print(df.head())
