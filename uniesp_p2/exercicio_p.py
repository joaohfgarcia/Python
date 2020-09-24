# Calcula do Fatorial de um Numero


def fatorialFor(n):
    fat = 1
    for i in range(1, n+1):
        fat *= i
    return (fat)

def fatorialWhile(n):
    fat = 1
    i = 1
    while i <=n:
        fat *= i
        i += 1
    return (fat)

def main():
    num = int(input("Digite o numero para calcular o fatorial:" ))   
    if (num > 0) :
        print (f"O Fatorial de {num} com função For é {fatorialFor(num)}")
        print (f"O Fatorial de {num} com função While é {fatorialWhile(num)}")
    elif (num == 0):
        print ("O Fatorial de 0 é 1")
    else:
        print ("Não existe fatorial de número negativo")


main()


