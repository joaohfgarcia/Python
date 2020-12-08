def numVelasAniversario(num, lista):

    velaMaior = max(lista)
    quantidadeVelas = lista.count(velaMaior)
    #retorna para a função principal o resultado da quantidade de velas
    return("Número de velas com a altura máxima = {}".format(quantidadeVelas))


def main():

    n = int(input("Digite a quantidade de velas: "))

    #Teste condicional do input n
    while n < 1 or n > 10**5:
        print("Quantidade de velas inválida")
        n = int(input("Digite a quantidade de velas: "))
    
    velasAlturas = str(input("Digite a altura das velas: ")).split()

    #Teste condicional do input velasAlturas
    for i in range(0,n):
        while int(velasAlturas[i]) < 1 or int(velasAlturas[i]) > 10**7:
            print("Altura da {}ª vela Inválida ".format(i+1))  
            velasAlturas[i] = input("Digite uma nova altura: ")

    #impressão e chamada da função com passagem dos inputs  
    print(numVelasAniversario(n, velasAlturas))


main()

