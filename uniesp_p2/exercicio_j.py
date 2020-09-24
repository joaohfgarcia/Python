#Positivo ou Negativo

def main ():

    genero = str (input("\nDigite o gênero: M para masculino ou F para feminino: "))
    if genero in "Mm":
        print (f"O gênero é masculino")
    elif genero in "Ff" :
        print (f"O gênero é feminino")
    else:
        print (f"Gênero inválido")


main()