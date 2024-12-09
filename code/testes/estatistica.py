import pandas as pd
import numpy as np

# Criando um DataFrame fictício
data = {
    "Categoria": ["A", "B", "C", "D", "E"],
    "Valores": [10, 15, 8, 22, 19]
}
df = pd.DataFrame(data)

# Funções Estatísticas Usando Pandas
media = df["Valores"].mean()  # Média
mediana = df["Valores"].median()  # Mediana
variancia = df["Valores"].var()  # Variância
desvio_padrao = df["Valores"].std()  # Desvio padrão
soma = df["Valores"].sum()  # Soma

# Funções Estatísticas Usando NumPy
minimo = np.min(df["Valores"])  # Valor mínimo
maximo = np.max(df["Valores"])  # Valor máximo
percentil_75 = np.percentile(df["Valores"], 75)  # Percentil 75

# Exibindo os resultados
print("Estatísticas Básicas:")
print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Variância: {variancia}")
print(f"Desvio Padrão: {desvio_padrao}")
print(f"Soma: {soma}")
print(f"Mínimo: {minimo}")
print(f"Máximo: {maximo}")
print(f"Percentil 75: {percentil_75}")