""" Crie um programa no qual o usuário digitará 5 nomes. Todos os cinco nomes serão salvos no vetor chamado "registros”. Em seguida:
a) Mostre o que o usuário digitou na tela;
b) O programa pedirá outro nome, que será adicionado no fim do vetor "registros”;
c) O programa pedirá outro nome, que será adicionado na 2ª posição do vetor "registros”;
d) Imprima o resultado na tela. """


def main():

    i = 0
    
    registros = []

    while i <5:
        registros.append(input(f'Digite {i+1}º nome: '))
        i +=1

    print(registros)

    registros.append(input(f'Digite um nome extra: '))

    novo2 = input(f'Digite um novo nome para a 2ª posição: ')

    registros.pop(1)

    registros.insert(1, novo2)

    print(registros)

    
main()