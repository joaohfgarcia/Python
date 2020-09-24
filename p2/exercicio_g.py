# Calculos Diversos

def solucao1 (n1, n2):
    return (n1 * 2 * n2/2)
    
def solucao2 (n1, n3):
    return (n1 * 3 + n3)
    
def solucao3 (n3):
    return (n3 ** 3)
    
def main ():
    num1 = int(input("Digite o primeiro numero inteiro: "))
    num2 = int(input("Digite o segundo numero inteiro: "))
    num3 = float(input("Digite um numero Real: "))
    resultado1 = solucao1 (num1, num2)
    resultado2 = solucao2 (num1, num3)
    resultado3 = solucao3 (num3)
    print (f"A operação 1 teve como resultado {resultado1}")
    print (f"A operação 2 teve como resultado {resultado2}")
    print (f"A operação 3 teve como resultado {resultado3}")

main()