#Uma escola deseja controlar as notas dos alunos em diferentes disciplinas para calcular a média geral e identificar o desempenho de cada estudante. Sabendo-se que cada aluno pode estar matriculado em até 5 disciplinas, e que cada disciplina pode ter até 4 notas (provas ou trabalhos), crie um algoritmo que:

#Solicite o nome de cada aluno e o número de disciplinas em que ele está matriculado.
#Para cada disciplina, peça as notas das avaliações e calcule a média da disciplina.
#Após calcular as médias de todas as disciplinas de um aluno, exiba o nome do aluno, a média geral (média das médias das disciplinas) e sua situação, seguindo os critérios:
#Média geral maior ou igual a 7: "Aprovado".
#Média geral entre 5 e 6.9: "Recuperação".
#Média geral abaixo de 5: "Reprovado".
#O algoritmo deve permitir que o professor controle até 10 alunos. Utilize estruturas de repetição para resolver o problema.

qtde_alunos = 3

while (qtde_alunos <= 10):
    qtde_alunos = qtde_alunos + 1
    nome = input ("digite o nome do aluno: ")
    qtde_disciplinas = 0
    media_disciplinas = 0
    while (qtde_disciplinas <= 5):
        qtde_disciplinas = qtde_disciplinas + 1
        disciplina = input ("digite a disciplina: ")
        n1 = float(input ("Digite a nota 1: "))
        n2 = float(input ("Digite a nota 2: "))
        n3 = float(input ("Digite a nota 3: "))
        n4 = float(input ("Digite a nota 4: "))

        # processamento
        media = (n1 + n2 + n3 + n4)/4
        media_disciplinas = media_disciplinas + media
        
        if( media >=7):
            situacao = "Aprovado"
        else:
            if (media > 5 and media < 6.9):
                situacao= "Recuperação"
            else:
                situacao = "Reprovado"

        #saida
        print (disciplina)
        print (media)
        print (situacao)
        
        opcao = input ("Processar mais uma disciplina? ")
        if (opcao == "não"):
            break
    print (f"Média Geral das disciplinas: {media_disciplinas / qtde_disciplinas }")
    
    opcao = input ("Processar mais um aluno? ")
    if (opcao == "não"):
        print("Adeus!")
        break