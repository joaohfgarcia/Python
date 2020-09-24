print('--SOMA DE POSITIVOS E QUANTIDADE DE NEGATIVOS--\n')

valores = [-3, 9, 12, -34, -2, 20, 10]
i = 0
somap = 0
quantn = 0

print('Valores =', valores)

for i in range(7):
    if valores[i] >= 0:
        somap = somap + valores[i]
    else:
        quantn += 1
print('A soma dos valores positivos é: ', somap)
print('A quantidade de valores negativos é: ', quantn)
