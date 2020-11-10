#Crie um programa que o usuário digite uma sequência de valores (de tamanho dinâmico) numa única variável, chamada registro. Em seguida, mostre os valores armazenados.

def registrosAppend():

    registro = []
    tam = int(input("Quantos elementos serão registrados? "))

    for i in range(0, tam):
        registro.append(input("Elemento "+str(i+1)+" :"))
    
    print (registro)


def registrosSplit():
    
    registro = input("\nDigite os elementos separados por espaço: ").split()
    print (registro)


def main():
       
    registrosAppend()
    registrosSplit()

main()