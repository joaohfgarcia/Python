def main():

    matriz = [[1,2,3,4],[5,6,7, 8]]
    
    for i in range (2):
        matriz[i].append(int(input(f'insira o valor extra na linha {i+1}: ')))

    print (matriz)

   
main()
