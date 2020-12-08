def maquinadoTempo(ano):
    # testa se ano é maior que 1918
    if ano < 1918:
        if (ano%4==0):  
            return("Ano: " + str(ano) + " é bissexto - Dia do programador: 12.09." + str(ano))
        else:
            return("Ano: " + str(ano) + " não é bissexto - Dia do programador: 13.09." + str(ano))

    # testa se ano é menor que 1918
    elif ano >1918:
        if (ano%4==0):  
            return("Ano: " + str(ano) + " é bissexto - Dia do programador: 12.09." + str(ano))
        else:
            return("Ano: " + str(ano) + " não é bissexto - Dia do programador: 13.09." + str(ano))

    # ano igual a 1918
    else:
        return("Ano: " + str(ano) + " transição do calendário - Dia do programador: 26.09." + str(ano))


def main():
    aa = int(input("Digite o ano : "))

    #Teste condicional do input do ano 
    while aa < 1700 or aa > 2700:
        print("Ano inválido")
        aa = int(input("Digite o ano novamente: "))

    print(maquinadoTempo(aa))

main()