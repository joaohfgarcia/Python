print ('::Calculando o valor da prestação::')
valor = float(input('Digite o valor original da prestação: '))
taxa = float(input('Digite o valor da taxa de juros (%): '))
tempo = float(input('Digite o tempo de atraso(meses): '))
prestacao = valor + (valor * (taxa/100)*tempo)
print ('O valor da prestação atualizado é: ', prestacao)