# Programa para calcular o IMC
# Multiplique a sua altura em metros por ela mesma. Por exemplo, se você medir 1,60 m, o cálculo será: 1,6 x 1,6 = 2,56. 
# Divida o seu peso em quilogramas pelo resultado da multiplicação. 

# area de entrada
altura = float(input("Digite altura: "))
peso = float(input("Digite peso: ") )

# processamento
imc = peso / ( altura * altura )

# saida (tela, arquvo, impressora, banco de dados)
print("imc:", imc)