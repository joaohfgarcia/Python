#Compra Mais Barato

def main ():

    preco1 = float (input("Qual o primeiro valor?: "))
    preco2 = float (input("Qual o segundo valor?: "))
    preco3 = float (input("Qual o terceiro valor?: "))

    if preco1 <= preco2 and preco1 <= preco3:
        print (f"O produto 1 é o mais barato e custa R$ {preco1}")
    elif preco2 <= preco1 and preco2 <= preco3:
        print (f"O produto 2 é o mais barato e custa R$ {preco2}")
    else:
        print (f"O produto 3 é o mais barato e custa R$ {preco3}")


def main2():
    valorMinimo = 1000000
    produtoBarato = 0
    for p in range(0,3):
        valorProduto = float (input("Digite o valor do produto: "))
        
        if (valorProduto <= valorMinimo):
            valorMinimo = valorProduto
            produtoBarato = p + 1
    print (f"O produto {produtoBarato} é o mais barato e custa R$ {valorMinimo}")

main2()