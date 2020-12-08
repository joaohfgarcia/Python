
tabuleiro = [ [0 for i in range(3)] for j in range(3)]

def imprimeTabuleiro():

    for i in range (3):
        for j in range (3):
            if tabuleiro[i][j] == 0:
                print(" _ ", end=' ') 
            else:
                print(f' {tabuleiro[i][j]} ', end=' ')
        print()


def main():

    
    fim = 1
    imprimeTabuleiro()

    while fim <= 9 :
        
        jogar = True
        print ('\nJogador 1')
        while jogar == True:
            l = int(input('Digite a linha [1 à 3]: '))-1
            c = int(input('Digite a coluna [1 à 3]: '))-1
            if  tabuleiro[l][c] == 0:
                tabuleiro[l][c] = "X"
                jogar = False
            else:
                print ("Posição Indisponível. Jogue Novamente!\n")
        fim +=1
        imprimeTabuleiro()

        if fim > 9:
            print('\nGAME OVER!\n')
            break
        

        jogar = True
        print ('\nJogador2')
        while jogar == True:
            l = int(input('Digite a linha [1 à 3]: '))-1
            c = int(input('Digite a coluna [1 à 3]: '))-1
            if  tabuleiro[l][c] == 0:
                tabuleiro[l][c] = "O"
                jogar = False
            else:
                print ("Posição Indisponível. Jogue Novamente!\n")
        fim +=1
        imprimeTabuleiro()
        
   

main()
