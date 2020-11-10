#Crie um array que o conteúdo seja nomes das cores. Em seguida remova apenas a cor "vermelho”, se houver.


def main():

    listCores = []

    print('\n::: Digite o nome de 5 cores, sendo uma delas vermelho :::')

    for i in range (0,5):
        listCores.append(input(f'Digite a {i+1}ª cor: ').upper())
        
    print(listCores)    
    
    qtde = listCores.count('VERMELHO')

    if qtde != 0:
        for i in range (0,qtde):
            listCores.remove('VERMELHO')

        print('\nNova lista sem o vermelho:')       
        print(listCores)
    else:
        print('\nNão existe a cor vermelho na lista!')

    
main()