print('Verificar se 1º Numero é Maior que Soma dos demais')
n1 = int (input ('Digite o 1º numero: '))
n2 = int (input ('Digite o 2º numero: '))
n3 = int (input ('Digite o 3º numero: '))
soma = n2 + n3
if n1 > soma:
    print ('1º numero é maior que a soma dos demais')
elif n1 < soma:
    print ('1º numero é menor que a soma dos demais')
else:
    print ('1º numero é igual a soma dos demais')