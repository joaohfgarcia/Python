print ('--DIGITE 10 NÚMEROS INTEIROS--')

lista = []
i = 1

for i in range(10):
    num = int(input('Digite o número: '))
    lista.append(num)
    
while i >= 0:
    print(lista[i], end=" ")
    i -= 1