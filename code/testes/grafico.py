import pandas as pd
import matplotlib.pyplot as plt

# Criando um DataFrame fictício
data = {
    "Categoria": ["A", "B", "C", "D", "E"],
    "Valores": [10, 15, 8, 22, 19]
}
df = pd.DataFrame(data)

# Criando o gráfico de barras
plt.bar(df["Categoria"], df["Valores"])

# Adicionando título e rótulos
plt.title("Gráfico de Barras com Pandas e Matplotlib")
plt.xlabel("Categorias")
plt.ylabel("Valores")

# Exibir o gráfico
plt.show()
