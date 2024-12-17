# Entrada
## Aguardar o usuário digitar algo na console(função receber).
### Depois criar a variável nome do tipo string (função definir) e, por fim,
### atribuir o valor informado pelo usuário na variável nome (função atribuir)
nome = input("Digite seu nome: ")

# Visto que tudo que vem do teclado é string, a função int() foi utilizada para converter o que for digitado em inteiro
idade = int(input("Digite sua idade: "))

# mostrar o tipo da variável que foi criado automaticamente pelo python
print(type(idade))

# mostrar o restulado final usando a função f
print(f"{nome}, você tem {idade} anos!")
