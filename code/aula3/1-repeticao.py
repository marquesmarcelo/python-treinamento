# Crie um algoritmo para imprimir a tabuada de um numero informado pelo usuário

# entrada
#numero = int(input("Digite um numero: "))
numero = 4

# processamento
vezes1 = numero * 1
vezes2 = numero * 2
vezes3 = numero * 3
vezes4 = numero * 4
vezes5 = numero * 5
vezes6 = numero * 6
vezes7 = numero * 7
vezes8 = numero * 8
vezes9 = numero * 9
vezes10 = numero * 10


# saida
print (numero, "x", "1 = ", vezes1)
print (numero, "x", "2 = ", vezes2)
print (numero, "x", "3 = ", vezes3)
print (numero, "x", "4 = ", vezes4)
print (numero, "x", "5 = ", vezes5)
print (numero, "x", "6 = ", vezes6)
print (numero, "x", "7 = ", vezes7)
print (numero, "x", "8 = ", vezes8)
print (numero, "x", "9 = ", vezes9)
print (numero, "x", "10 = ", vezes10)

print("-------")


numero = 5
acumulador = 0 # somar o valor anterior com um novo valor atual
contador = 0 # contar a quantidade de vezes que a estrura repetiu

for i in range(1, 11):
    contador = contador + 1
    acumulador = acumulador + numero
    resultado = numero * i
    print (f"{numero} x {i} = {vezes1}")
    
print (f"acumulador = {acumulador} e contador = {contador}")
    

