def main():
    '''
    listaNum = []
    quant = int(input("Quantos numeros vc deseja digitar: "))
    for i in range (0, quant):
        listaNum.append(int(input(f"Digite o {i+1} º número: ")))
    print(listaNum)
    '''
    num = 0
    somaImpar = 0
    somaPar = 0

    while num!=1000:
        if (num % 2 == 0):
            somaPar = somaPar + num
        else:
            somaImpar = somaImpar + num
        num += 1
    
    print("A soma dos numeros pares foi :", somaPar)
    print("A soma dos numeros ímpares foi :", somaImpar)                

main()