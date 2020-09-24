print('--Separando Valores Pares--')

import random
valores = []
i = 0

print('Imprindo Lista Completa')

for i in range(0,100):
    valores.append(random.randrange(1, 101))
print(valores)

i = 0
print('\n')
print('Imprindo Índices Pares')

for i in range (0, 100, 2):
    print (valores[i], end=" ")
