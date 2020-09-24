print('Definir Turma do Aluno')
idade = int (input('Digite a Idade do Aluno em anos: '))
if idade < 5:
    print('Idade insuficiente para matrícula')
elif idade >= 5 and idade <= 7:
    print('Aluno Infantil A')
elif idade >= 8 and idade <= 10:
    print('Aluno Infantil B')
elif idade >= 11 and idade <= 13:
    print('Aluno Juvenil A')
elif idade >= 14 and idade <= 17:
    print('Aluno Juvenil B')
else:
    print ('Aluno Sênior')

