# Forma Errada

valor1 = 0.1
valor2 = 0.2
resultado = valor1 + valor2
print(resultado)  # Saída: 0.30000000000000004

# Forma certa
from decimal import Decimal

valor1 = Decimal("0.1")
valor2 = Decimal("0.2")
resultado = valor1 + valor2
print(resultado)  # Saída: 0.3
