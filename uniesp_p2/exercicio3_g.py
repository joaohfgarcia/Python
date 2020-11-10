def main():

    matriz = []
    matrizT = [ [0 for i in range(3)] for j in range(2)]
  
    for i in range (2):
        print (f'Linha {i+1}')
        valores = []
        for j in range (3):
            valores.append(int(input(f'Digite o {j+1}° valor: ')))
        matriz.append(valores)

    print('\nMatriz Original')

    for i in range (0,2):
        print (matriz[i])


    print('\nMatriz Transposta')
  
      
    for i in range (3):
        for j in range (2):
            matrizT[i][j] = matriz [j][i]

  
    for i in range (0,3):
        print (matrizT[i])



main()
