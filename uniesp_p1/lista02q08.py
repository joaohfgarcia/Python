print ('Cálculos considerando 20 de referencia')

n1 = int (input('Digite o 1º numero: '))
n2 = int (input('Digite o 2º numero: '))

soma = n1 + n2

if soma > 20:
    result = soma + 8
    print ('A soma dos números + 8 =', result)
elif soma < 20:
    result = soma -5
    print('A soma dos números - 5 é =', result)
else:
    print('A soma dos números é =', 20)