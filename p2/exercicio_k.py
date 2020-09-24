#Verifica Aprovação

def verifica(valor):
    if valor == 10.0:
        return ("Aprovado com Distinção")
    elif valor >= 7.0:
        return ("Aprovado")
    else:
        return ("Reprovado")


def main ():

    nota1 = float (input("Digite a nota 1: "))
    nota2 = float (input("Digite a nota 2: "))

    media = (nota1 + nota2)/2
    
    print (f"Com a média {media} o aluno está {verifica(media)}")


main()