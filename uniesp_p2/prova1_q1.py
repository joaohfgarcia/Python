def numVelasAniversario(qtde, alturas):
    soma = 0
    maior = str(max(alturas, key=int))

    for i in range (0,qtde):
        if alturas[i] == maior:
            soma += 1
       
    return ("Número de velas com altura máxima = "+str(soma))


def main():
    
    n = int(input("Digite a quantidade de velas: "))
    while n < 1 or n > 10**5:
        print("Quantidade digitada inválida")
        n = int(input("Digite a quantidade de velas: "))

    velasAltura = input(f"Digite a altura das {n} velas separadas por espaços: ").split()
    for i in range (0,n):
        if (int(velasAltura[i]) < 1) or (int(velasAltura[i]) > 10**7): 
            print(f"Altura da vela {i+1} inválida")
            velasAltura[i] = input("Digite a nova altura: ")
            
    print(numVelasAniversario(n, velasAltura))


main()