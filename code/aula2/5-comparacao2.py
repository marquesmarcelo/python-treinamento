# Informar se a pessoa esta aprovada ou não na disciplina.
# O aluno é avaliado por duas notas, sendo que a primeira vale 60% da média e a segunda vale 40% da média
# o aluno esta aprovado quando sua média for maior que 6
# se o aluno tiver média menor que 6 ele poderá fazer uma prova de recuperação. Se nessa prova tiver nota superior a 6 ele será aprovado.

# objetivo media parcial
# entrada
n1 = 6
n2 = 6

# processamento
media = (n1 + n2)/2

# saida
# informar se aprovado
print(media)
if (media >= 6):
    print("Aprovado")
else:
    print("Reprovado")

    # objetivo prova de recuperação
    # entrada


    # processamento
    if (media < 6):
        recuperacao = 4
        if (recuperacao > 6):
            print("aprovado")
        else:
            print("reprovado")
    # saida
