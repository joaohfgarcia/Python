
def trianguloRetangulo(v1, v2, hip):
    if hip**2 == v1**2 + v2**2:
        return ("É um Triângulo Retângulo")
    else:
        return ("Não é um Triângulo Retângulo")


    
def main():

    hipotenusa = 0
    lado2 = 0
    lado1 = 0

    for i in range (0,3):
        valor = int (input("Digite o valor lado:" ))
        
        if valor >= hipotenusa : 
            lado2 = lado1
            lado1 = hipotenusa
            hipotenusa = valor
        else:
            lado2 = valor
    print("\nDe acordo com o teorema de Pitágoras se h² = c1² + c2² o triângulo é retângulo")
    print(f"Seu triângulo tem catetos com valores {lado1} e {lado2} e hipotenusa {hipotenusa}")
    print(trianguloRetangulo(lado1, lado2, hipotenusa)) 


main()

