#Um comerciante calcula o valor final de uma venda utilizando as seguintes regras para calcular o lucro:
#Valor < R$ 10,00 => lucro de 70%
#R$10,00 <= valor < R$ 30,00 =>lucro de 50%
#R$30,00 <= valor < R$ 50,00 =>lucro de 40%
#valor >= R$50,00 => lucro de 30%
#Criar o algoritmo que possa entrar com nome do produto e o valor da compra. Imprimir o nome do produto e o valor da venda (já adicionado o lucro do vendedor).

# entrada
nome = "arroz"
valor = 10.4

# processamento
lucro = 0

if (valor >=50):
    lucro = valor * 0.3
else:
    if (valor >= 30 and valor <50):
        lucro = valor * 0.4
    else:
        if (valor >=10 and valor < 30):
            lucro = valor * 0.5
        else:
            lucro = lucro * 0.7

valor_venda = valor + lucro
#saida
print (nome)
print (valor_venda)