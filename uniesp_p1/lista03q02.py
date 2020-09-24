print('--- MÉDIA ALUNO ---')

n1 = float(input('Digite a primeira nota: '))
while n1<0 or n1>10:
    n1 = float(input('Nota invalida, digite uma nota entre 0 e 10: '))

if n1>=0 and n1<=10:
    print('Nota computada')

n2 = float(input('Digite agora segunda nota: '))

while n2<0 or n2>10:
    n2 = float(input('Nota invalida, digite uma nota entre 0 e 10: '))

if n2>=0 and n2<=10:
    print('Nota computada')

media = (n1 + n2)/2

if media<4:
    print('O aluno está REPROVADO com media {}'.format(media))
elif media <7:
    print('O aluno está APTO A FINAL com media {}'.format(media))
else:
    #print('O aluno está APROVADO com media {}'.format(media))
    print(f'O aluno está APROVADO com media {media}')