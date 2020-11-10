def main():

    matriz = [[39,14,27],[21,83,92],[31,12,43]]

    for i in range (3):
        for j in range (3):
            temp = matriz[i][j] * 7
            matriz[i][j] = temp

    print (matriz)

   
main()
