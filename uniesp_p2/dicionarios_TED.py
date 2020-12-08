lista = []

def cadDevedor():   
    devedor = {
        'nome':input("Nome: ").upper(),
        'endereco':input("Endereco: "),
        'fone':input("Fone: "),
        'divida':float(input("Dívida: ")),
    }
    lista.append(devedor)
    print('Cadastro efetuado com sucesso!')


def atualizaDivida():
    nomeDevedor = input('Digite o nome do devedor: ').upper() 
    for i in range (0,len(lista)):
        if lista[i]['nome'] == nomeDevedor:
            lista[i]['divida'] = (float(input('Digite o novo valor da dívida: ')))
        break

    print('Dívida atualizada com sucesso!')


def removeDevedor():
    nomeDevedor = input('Digite o nome do devedor a ser removido: ').upper() 
    for i in range (0,len(lista)):
        if lista[i]['nome'] == nomeDevedor:
            lista.pop(i)
        break
    
    print('Cadastro removido com sucesso!')


def buscaDevedor():
    nomeDevedor = input('Digite o nome do devedor: ').upper()
    for i in range (0,len(lista)):
        if lista[i]['nome'] == nomeDevedor:
            print (f"Nome: {lista[i]['nome']}")
            print (f"Endereço: {lista[i]['endereco']}")
            print (f"Fone: {lista[i]['fone']}")
            print (f"Dívida: {lista[i]['divida']}")
        break


def listarDevedores():
    print ('\nLISTA DE DEVEDORES CADASTRADOS') 
    for i in range (0,len(lista)):
        print(f'\nCadastro {i+1}')
        print (f"Nome: {lista[i]['nome']}")
        print (f"Endereço: {lista[i]['endereco']}")
        print (f"Fone: {lista[i]['fone']}")
        print (f"Dívida: {lista[i]['divida']}")

def menu():
    print ('\nSISTEMA DE CONTROLE DE INADIMPLÊNCIA')
    print ('[1] CADASTRAR DEVEDOR')
    print ('[2] ATUALIZAR DÍVIDA')
    print ('[3] REMOVER DEVEDOR')
    print ('[4] BUSCAR DEVEDOR')
    print ('[5] LISTAR DEVEDORES')
    print ('[0] ENCERRAR PROGRAMA')

    
def main():
    
    menu()
    opcao = input('\nDigite a opção desejada: ')

    while True:
        if opcao == '1':
            cadDevedor()

        elif opcao == '2':
            atualizaDivida()
        
        elif opcao == '3':
            removeDevedor()
        
        elif opcao == '4':
            buscaDevedor()

        elif opcao == '5':
            listarDevedores()
        
        elif opcao == '0':
            break

        else:
            print('Opção Inválida')
        
        menu()
        opcao = input('\nDigite a opção desejada: ')
        

  

main()