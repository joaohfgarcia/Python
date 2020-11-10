
""" Crie um programa no qual o usuário digitará 5 nomes num vetor (OBRIGATÓRIO TER SEU NOME INCLUÍDO NO VETOR). Em seguida:
a) Mostre os valores na tela. 
b) Adicione seu sobrenome na posição do seu nome no array.
c) Imprima o resultado na tela. """


def main():

    i = 0

    listNomes = []

    while i < 5:
        print('::: Digite 5 nomes sendo um deles o seu :::')
        listNomes.append(input(f'Digite o {i+1}º nome: ').upper())
        i +=1

    print(listNomes)    

    nome = input('Qual o seu nome? ').upper()
    
    sobreNome = input(f'Digite seu sobrenome: ').upper()

    posicao = listNomes.index(nome)

    listNomes.pop(posicao)

    listNomes.insert(posicao, sobreNome)

    print(listNomes)

    
main()