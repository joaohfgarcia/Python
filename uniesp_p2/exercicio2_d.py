#Elabore um programa que cria um array de nomes de países e outro array com nomes de cidades. Cada uma das criações devem ser feitas com métodos diferentes.


def main():

    i = 0
    j = 0

    cidades = []
    paises = []
    
    while i <3:
        cidades.append(input(f'Digite o nome de cidade {i+1}: '))
        i +=1

    print(cidades)

    while j <3:
        paises.insert(j, (input(f'Digite o nome do país {j+1}: ')))
        j +=1
    
    print(paises)

main()