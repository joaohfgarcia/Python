
def produto(n1, n2):
    produto = n1**2 * n2/2
    return (produto)

def triplo (n1, n2):
    triplo = n1*3 + n2
    return (triplo)

def cubo(n):
    cubo = n**3
    return(cubo)

def main ():

    numA = int(input("Digite o primeiro numero: "))
    numB = int(input("Digite o segundo numero: "))
    numC = float(input("Digite o terceiro numero: "))

    print (f"O produto do dobro de {numA} e com metade de {numC} é: {produto(numA, numC)}")
    
    print (f"A soma do triplo de {numA} com {numC} é: {triplo(numA, numC)}")

    print (f"o cubo de {numC} é: {cubo(numC)}")



main()