#6 comandos 
# inicio

# definicao - criar variavel
# atribuicao - colocar conteudo na variavel
nome = "marcelo"

# receber - ligar o standart in (teclado) e colocar o valor em uma variavel
#nome = input("Digite o nome: ")
# mostrar - mostrar algo no standart out (monitor)
print(nome)
# fim

#2 estruturas
## condicional
if (nome == "marcelo"):
    print(nome)
    print (nome + "bem vindo")
    print (nome + "teste")
else:
    print("não é marcelo")
    print(nome +" seja bem vindo novo usuário")

area = 15000.0
gadsup3 = 0

if (area >=10000.0 and area <=20000.0):
    print("enviar para Secretaria da SPU")
else:
    if (area >= 1000.0):
        print("enviar para GADESUP3")
        gadsup3 = gadsup3 + 1
    else:
        gadsup1 = 0
        if (area < 1000.0):
            print("enviar para GADESUP1")
            gadsup1 = gadsup1 + 1

gadsup1 = 0

if (area >=10000.0 and area <=20000.0):
    print("enviar para Secretaria da SPU")
elif  (area >= 1000.0):
    print("enviar para GADESUP3")
    gadsup3 = gadsup3 + 1
elif (area < 1000.0):
    print("enviar para GADESUP1")
    gadsup1 = gadsup1 + 1

## Repeticao

for i in range(1,11):
    print ("palavra")

i = 11
while (i <=10):
    print ("nova palavra")
    i = i + 1
    
i = 11

# entrada - processamento - saida