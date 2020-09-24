#calcula tempo de espera

def main():
    tempoAcumulado = 0
    numClientes = int (input("Quantidade de Clientes: "))
    for i in range(0, numClientes):
        tempoEspera = int(input("Digite quanto tempo você aguardou para ser atendido: "))
        tempoAcumulado += tempoEspera
    tempoMedio = tempoAcumulado / numClientes
    print (f"O tempo médio de espera atual é de: {tempoMedio} minutos")
    

def main2():
    i = 1
    tempoAcumulado = 0
    numClientes = int (input("Quantidade de Clientes: "))
    while i <= numClientes:
        tempoEspera = int(input("Digite quanto tempo você aguardou para ser atendido: ")) 
        tempoAcumulado += tempoEspera
        i += 1
    tempoMedio = tempoAcumulado / numClientes
    print (f"O tempo médio de espera atual é de: {tempoMedio} minutos")


# main()

main2()