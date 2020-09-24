# Verifica se é palíndromo

def palindromo(n):
    tamanho = len(n)
    centro = int(tamanho/2)
    if tamanho % 2 == 0:
        for i in range (0, centro):
            if n[i] == n[tamanho-1]:
                resposta = "é Palindromo"
            else:
                resposta = "não é Palindromo"
            tamanho -= 1
  
    else:
        for i in range (0,centro+1):
            if n[i] == n [tamanho-1]:
                resposta = "é palindromo"
            else:
                resposta = "não é palindromo"
            tamanho -=1
         
    return(resposta)


def main():
    num = str(input("Digite um número: "))
    print (f"O número {palindromo(num)}")


main()