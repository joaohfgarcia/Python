def main():

    matriz = []
 
    cont = 0

    for i in range (4):
        print (f'Linha {i+1}')
        valores = []
        for j in range (4):
            valores.append(int(input(f'Digite o {j+1}° valor: ')))
        matriz.append(valores)

    for i in range (0, 4):
        for j in range (0, 4):
            if (matriz[i][j] > 10):
                cont += 1

    print (matriz)

    print(f'A matriz possui {cont} valores maiores que 10')


main()
