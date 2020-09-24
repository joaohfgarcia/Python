print ('--Calcular Situação do Aluno---')
nota1 = float (input('Digite a Nota 1: '))
nota2 = float (input('Digite a Nota 2: '))
media = (nota1 + nota2)/2
print ('A média do aluno é:', media)
if media < 4:
    print (f'Aluno Reprovado com média {media}')
elif media >= 7:
    print (f'Aluno Aprovado com média {media}')
else:
     print (f'Prova Final com média {media}')