#Calcula o quadrado de cada elemento do intervalo

def main():
    inicio = int (input("Digite o valor inicial da sequência: "))
    fim = int (input("Digite o valor final da sequência: "))
    
    for i in range(inicio, fim+1):
        print (i**2, end=" ")


def main2():
    inicio = int (input("Digite o valor inicial da sequência: "))
    fim = int (input("Digite o valor final da sequência: "))
    
    while inicio <= fim:
        print (inicio**2, end=" ")
        inicio += 1


#main()

main2()
