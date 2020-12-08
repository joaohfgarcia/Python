def main():

    lista = []
    
    print ('CADASTRO DE USUÁRIOS')

    for i in range (1,4):
        print(f'\nCadastro {i}')
        usuario = {
            'nome':input("Nome: ").upper(),
            'endereco':input("Endereço: "),
            'cpf':input("CPF: "),
        }
        lista.append(usuario)

    print ('\nLISTA DE USUÁRIOS CADASTRADOS') 

    for i in range (0,3):
        print(f'\nUsuário {i+1}')
        print (f"Nome: {lista[i]['nome']}")
        print (f"Endereço: {lista[i]['endereco']}")
        print (f"CPF: {lista[i]['cpf']}")
   

main()