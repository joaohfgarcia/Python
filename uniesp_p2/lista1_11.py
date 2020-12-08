def bissexto(ano):

    if (ano%4==0 and ano%100!=0 or ano%400==0):
        return("Ano Bissexto,")
    else:
        return("Não é um ano Bissexto")


def validarData(ano, mes, dia):
    import datetime
    try:
        datetime.datetime(ano, mes, dia)
        return True
    except ValueError:
        return False

def main():

    mesExtenso = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]    
    data = input("Digite a data: ")
    dd, mm, aa = data.split("/")
    dia = int(dd)
    mes = int(mm)
    ano = int(aa)
    
    if validarData(ano, mes, dia):
        print("Data válida")
        print (f"{dia} de {mesExtenso[mes-1]} de {ano}")
        print(bissexto(ano))
    else:
        print("Data inválida")
    

main()