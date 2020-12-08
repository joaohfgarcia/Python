
def diaDoProgramador(aa):

    if (aa <= 1917) and (aa%4 == 0):
        return(f"[Ano Bissexto] O Dia do Programador, 256º dia do ano, ocorreu em 12.09.{aa}")
    elif (aa <= 1917) and (aa%4 != 0):
        return(f"[Não é Ano Bissexto] O Dia do Programador, 256º dia do ano, ocorreu em 13.09.{aa}")
    elif (aa == 1918):
        return(f"[Ano de transição do calendário] O Dia do Programador, 256º dia do ano, ocorreu em 26.09.{aa}")   
    elif (aa%400==0 or aa%4==0 and aa%100!=0):
        return(f"[Ano Bissexto] O Dia do Programador, 256º dia do ano, ocorreu em 12.09.{aa}")
    else:
        return(f"[Não é Ano Bissexto] O Dia do Programador, 256º dia do ano, ocorreu em 13.09.{aa}")


def main():
    ano = int (input("Digite o ano da viajem entre 1700 e 2700: "))

    while ano < 1700 or ano > 2700:
        print("Ano Inválido")
        ano = int (input("Digite o ano da viajem: "))
    
    print(diaDoProgramador(ano))


main()