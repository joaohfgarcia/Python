def main():
    
    frase = input("Digite a frase: ")
    cont = len(frase.split())
    print (f"A frase contem {cont} palavras")
    print (frase.replace (" ", "-"))

main()