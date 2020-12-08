

def main():
    
    entrada = input("Digite o CPF: ").replace("."," ").replace("-"," ")
    numCpf = entrada.split()

    print (numCpf)


main()