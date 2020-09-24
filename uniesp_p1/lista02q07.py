print ('Diferença entre os numeros')

n1 = int (input('Digite o 1º numero: '))
n2 = int (input('Digite o 2º numero: '))

if n1 > n2:
    result = n1 - n2
    print ('A diferença entre os numeros é', result)
elif n1 < n2:
    result = n2 - n1
    print ('A diferença entre os numeros é', result)
else:
    print ('A diferença entre os numeros é', 0)