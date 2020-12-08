def main():

    busca = 0
    enderecos = {}

    enderecos ['58001'] = ['RUA UM', 100]
    enderecos ['58002'] = ['RUA DOIS', 200]
    enderecos ['58003'] = ['RUA TRES', 300]
    enderecos ['58004'] = ['RUA QUATRO', 400]
    enderecos ['58005'] = ['RUA CINCO', 500]

    filtro = int(input('Busca: CEP (Digite 1) Endereço (Digite 2): '))

    if filtro == 1:
        busca = input('Digite o CEP  ser pesquisado: ')
        if busca in enderecos.keys():
            print (enderecos[busca])

    elif filtro == 2:
        busca = input('Digite o ENDEREÇO  ser pesquisado: ').upper()
        for k, v in enderecos.items():
            if v[0] == busca:
                encontrado = True
        if encontrado == True:
            print ('Endereço cadastrado')
        else:
            print ('Endereço não cadastrado')


    else:
        print('Opção Inválida')

main()