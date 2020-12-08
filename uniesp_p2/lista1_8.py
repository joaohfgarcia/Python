def main():
    palavra = input("Digite a palavra: ")
    tam = len(palavra)
    for i in range (0,tam):
        print (palavra.upper()[i])

main()