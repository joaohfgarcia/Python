def main():

    ano = int (input("Digite o ano: "))
    
    if (ano%4==0 and ano%100!=0 or ano%400==0):
        teste = True
        print("Ano Bissexto,", teste)
    else:
        teste = False
        print("Não é um ano Bissexto,", teste)

main()