# Programa para calcular o IMC
# Multiplique a sua altura em metros por ela mesma. Por exemplo, se você medir 1,60 m, o cálculo será: 1,6 x 1,6 = 2,56. 
# Divida o seu peso em quilogramas pelo resultado da multiplicação. 

# Entrada (default: teclado; mas pode ser trocado para: mouse, arquivo)
altura = float(input("Digite altura: "))
peso = float(input("Digite peso: ") )

# Processamento
imc = peso / ( altura * altura )

# Saida (default: tela; mas pode ser trocado para: arquivo, impressora)
print("imc:", imc)