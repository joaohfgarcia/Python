#Positivo ou Negativo

def main ():

    valor = float (input("\nDigite um número: "))
    if valor > 0 :
        print (f"O valor {valor} é positivo")
    elif valor < 0 :
        print (f"O valor {valor} é negativo")
    else:
        print (f"O valor {valor} não é positivo nem negativo")


main()