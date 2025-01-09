#1.	Um endocrinologista deseja controlar a saúde de seus pacientes e, para isso, se utiliza do Índice de Massa Corporal (IMC). Sabendo-se que o IMC é calculado através da seguinte fórmula: IMC = peso / (altura * altura) Onde:
#●	peso é dado em Kg
#●	altura é dada em metros
#Criar um algoritmo que apresente o nome do paciente e sua faixa de risco, baseando-se na seguinte regras:
#IMC abaixo de 20 => abaixo do peso
#IMC a partir de 20 até 25 => normal
#IMC acima de 25 até 30 => excesso de peso
#IMC acima de 30 até 35 => obesidade
#IMC acima de 35 => obesidade mórbida

#entrada
nome = "marcelo"
peso = 65
altura =1.65

faixa = ""

#processamento
IMC = peso / (altura * altura)

if (IMC >= 35):
    faixa = "obesidade mórbida"
else:
    if (IMC >= 30 and IMC < 35):
        faixa = "obesidade"
    else:
        if (IMC >= 25 and IMC < 30):
            faixa = "excesso de peso"
        else:
            if (IMC >= 20 and IMC < 25):
                faixa = "normal"
            else:
                if (IMC < 20):
                    faixa = "abaixo do peso"
                
# Determinação da faixa
if IMC >= 35:
    faixa = "obesidade mórbida"
elif IMC >= 30:
    faixa = "obesidade"
elif IMC >= 25:
    faixa = "excesso de peso"
elif IMC >= 20:
    faixa = "normal"
else:
    faixa = "abaixo do peso"


#saida
print(nome)
print (faixa)
print (IMC)