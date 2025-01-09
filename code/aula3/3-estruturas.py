# lista
notas = [5, 10, 3, 5, 7, 9 ,10, 8, 3, 5]

acumulador = 0
contador = 0
for i in range(0, len(notas)):
    acumulador = acumulador + notas[i]
    contador = contador + 1
    print(f"notas[{i}] = {notas[i]}")
    
#processamento
media = acumulador / contador

#saida
print (f"Média = {media}")

# nova versão mais eficiente
# Vetor
notas = [5, 10, 3, 5, 7, 9, 10, 8, 3, 5]

# Cálculo e saída da média
print(f"Média = {sum(notas) / len(notas)}")

