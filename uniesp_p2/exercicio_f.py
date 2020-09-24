#Calcula Tinta
area = float(input("\nQual a área a ser pintada em m2?"))
litros = area/3
latas = int(litros/18)
valor = float(latas * 80)
if litros % 18 != 0:
    latas = int(latas + 1) 
    valor = float(latas * 80)
print (f"Você precisa adquirir {latas} latas de tinta")
print (f"O valor a ser pago é de R$ {valor}")
