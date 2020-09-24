# Calculo Salário

def irpf (valor_bruto):
    return (valor_bruto * 0.11)
    
def inss (valor_bruto):
    return (valor_bruto * 0.08)
    
def sindicato (valor_bruto):
    return (valor_bruto * 0.05)
    
def main ():
    horas_trab = int(input("Digite o numero horas trabalhadas: "))
    valor_hora = float(input("Digite o valor pago por hora trabalhada: "))
    salario_bruto = horas_trab * valor_hora
    desc1 = irpf (salario_bruto)
    desc2 = inss (salario_bruto)
    desc3 = sindicato(salario_bruto)
    desconto = desc1 + desc2 + desc3
    salario_liquido = salario_bruto - desconto
    print(f"\nValor do Salário Bruto: {salario_bruto}")
    print (f"Valor de IRPF: {desc1}")
    print (f"Valor de INSS: {desc2}")
    print (f"Valor Sindicato: {desc3}")
    print (f"Total Descontado: {desconto}")
    print (f"Valor do Salário Líquido: {salario_liquido}\n")

main()