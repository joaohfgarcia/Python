print('--LOCALIZAR MULTIPLOS DE 2--')
mult2 = []
cont = 1
cont_i = 0

for cont in range(3):
    num = int(input('Digite um número: '))
    mult2.append(num)
cont = 0
print ('\nOs números múltiplos de 2 são:')
for cont in range(len(mult2)):
    if mult2[cont] % 2 == 0:
        print(mult2[cont], end=" ")
    else:
        cont_i += 1
if cont_i == len(mult2):
    print('INEXISTENTES')