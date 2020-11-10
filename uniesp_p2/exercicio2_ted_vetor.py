'''Crie uma agenda eletrônica que contenha dois vetores: um array com o nome dos seus amigos e outro com as suas respectivas datas de aniversário.
Tente inserir e remover as informações da agenda de maneira dinâmica (apagando pelo nome ou posição, inserindo n usuários por vez caso queira, etc...)'''

def main():

    listNomes = []
    listDatas = []

    print('\n::: CADASTRO DE ANIVERSÁRIOS :::')

    for i in range (0,5):
        print(f'{i+1}º registro ')
        listNomes.append(input('Nome: ').upper())
        listDatas.append(input('Data de Aniversário: '))
    
    print('\n::: ANIVERSÁRIOS CADASTRADOS :::')

    for i in range (0,5):
        print (f'{listNomes[i]} - {listDatas[i]}') 

    excluir = input('\nDigite o nome que deseja remover: ').upper()
    posicao = listNomes.index(excluir)

    listNomes.pop(posicao)
    listDatas.pop(posicao)

    print('\n::: ANIVERSÁRIOS ATUALIZADOS :::')

    for i in range (0,len(listNomes)):
        print (f'{listNomes[i]} - {listDatas[i]}') 



main()