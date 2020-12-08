def main():

    busca = 0
    produtos = {}

    produtos ['20201'] = ['arroz', 5.00]
    produtos ['20202'] = ['feijao', 8.00]
    produtos ['20203'] = ['farinha', 3.00]
    produtos ['20204'] = ['tomate', 6.50]
    produtos ['20205'] = ['cebola', 7.50]
    produtos ['20206'] = ['batata', 3.50]

    print(produtos)

    for j in range (1,3):
        busca = input(f'Digite o codigo de barras do {j}º produto a ser removido: ')
        if busca in produtos.keys():
            produtos[busca] = ['',0]
            produtos.pop(busca)

    print(produtos)
    print()

    for j in range (3,5):
        busca = input(f'Digite o nome do {j}º produto  ser removido: ').lower()
        for k, v in produtos.items():
            if v[0] == busca:
                encontrado = True
                busca = k
        produtos[busca] = ['',0]
        produtos.pop(busca)
    print(produtos)

main()