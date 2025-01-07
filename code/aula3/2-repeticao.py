# A média de 10 notas informadas pelo usuário

acumulador = 0
contador = 0

for i in range(1, 11):
    # entrada
    numero = int(input(f"Digite o valor{i}:"))
    acumulador = acumulador + numero
    contador = contador + 1
    
#processamento
media = acumulador / contador

#saida
print (f"Média = {media}")
    
