def main():

    turma = []
 
    cont = 0

    for i in range (3):
        print (f'\nCadastro do Aluno {i+1}')
        aluno = []
        aluno.append(input('Nome..............: '))
        aluno.append(int(input('Matrícula.........: ')))
        aluno.append(input('Data de Nascimento: '))

        turma.append(aluno)

    for i in range (0, 3):
        print (turma[i])
                

main()
