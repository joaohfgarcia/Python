def main():
    enderecos = {}

    enderecos ['58001'] = ['Rua Sao José', 2, 'Centro', 'Cabedelo']
    enderecos ['58002'] = ['Rua Eptácio', 123, 'Centro', 'Baayeux']
    enderecos ['58003'] = ['Rua um', 100, 'Centro', 'Joao Pessoa']
    enderecos ['58004'] = ['Rua dois', 207, 'Centro', 'Guarabira']
    enderecos ['58005'] = ['Rua tres', 565, 'Centro', 'Santa Rita']

    print('\nCEPs REGISTRADOS:')
    for k in enderecos.keys():
        print(k)

main()