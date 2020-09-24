print ('Testar valores maiores que 10')

cont = 0
n1 = int (input('Digite o 1º numero: '))
n2 = int (input('Digite o 2º numero: '))
n3 = int (input('Digite o 3º numero: '))
n4 = int (input('Digite o 4º numero: '))
n5 = int (input('Digite o 5º numero: '))

if n1 > 10:
    cont += 1
if n2 > 10:
    cont += 1
if n3 > 10:
    cont += 1
if n4 > 10:
    cont += 1
if n5 > 10:
    cont += 1

print ('O total de numeros maior que 10 é', cont)


