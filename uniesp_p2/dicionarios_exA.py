def main():
    agenda = {}

    agenda ['joao'] = ['01/01/1988', 'Rua Sao José', 2, 'Centro', 'Cabedelo']
    agenda ['claudia'] = ['01/01/1999', 'Rua Eptácio', 123, 'Centro', 'Baayeux']
    agenda ['marcos'] = ['01/01/2000', 'Rua um', 100, 'Centro', 'Joao Pessoa']
    agenda ['pedro'] = ['01/01/1980', 'Rua dois', 207, 'Centro', 'Guarabira']
    agenda ['julia'] = ['01/01/2005', 'Rua tres', 565, 'Centro', 'Santa Rita']

    for i in agenda.items():
        print(i)

main()