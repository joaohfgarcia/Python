'''Crie um array referente aos anos de nascimento das 5 pessoas mais próximas a você. Em seguida:
- Ordene o array  na ordem crescente e mostre o resultado
- Ordene o array na ordem decrescente e mostre o resultado'''

def main():

    listAnos = []

    print('\n::: Digite o ano de nascimento de 5 pessoas :::')

    for i in range (0,5):
        listAnos.append(input(f'Digite a {i+1}ª ano: '))
        
    print(listAnos)    

    print('\nNova lista em ordem crescente:')
    listAnos.sort()
    print(listAnos)

    print('\nNova lista em ordem decrescente:')
    listAnos.reverse()
    print(listAnos)
    
main()