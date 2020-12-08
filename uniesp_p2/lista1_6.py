
def calculaNotas(valor):
    notas100 = int(valor/100)
    valor = valor - 100*notas100
    notas50 = int(valor/50)
    valor = valor - 50*notas50
    notas20 = int(valor/20)
    valor = valor - 20*notas20
    notas10 = int(valor/10)
    valor = valor - 10*notas10
    notas5 = int(valor/5)

    print ("Notas de R$ 100: ", notas100)
    print ("Notas de R$  50: ", notas50)
    print ("Notas de R$  20: ", notas20)
    print ("Notas de R$  10: ", notas10)
    print ("Notas de R$   5: ", notas5)


def main():

    saque = float(input ("Digite o valor do saque (Mín: R$10,00 Máx: R$600,00):"))

    while saque < 10 or saque > 600:
        print ("Valor inválido")
        saque = float(input ("Digite o valor do saque (Mín: R$10,00 Máx: R$600,00):"))
           
    calculaNotas(saque)
       

main()