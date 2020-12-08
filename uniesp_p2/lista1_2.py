
def soma(a,b):
    soma = a+b
    return(soma)

def subtracao (a,b):
    subtracao = a-b
    return (subtracao)

def produto(a,b):
    produto = a*b
    return (produto)


def main ():

    numA = float(input("Digite o primeiro numero: "))

    numB = float(input("Digite o segundo numero: "))

    print (f"A soma de {numA} e {numB} é: {soma(numA, numB)}")

    print (f"A diferença de {numA} e {numB} é: {subtracao(numA, numB)}")

    print (f"O produto de {numA} e {numB} é: {produto(numA, numB)}")

main()