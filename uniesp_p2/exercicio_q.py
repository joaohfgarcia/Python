# Gerador de Tabuada
'''
def tabuadaFor(n):
    for i in range (0, 11):
        print (f"{n} x {i} = {n*i}")


def tabuadaWhile(n):
    i = 0
    while i <= 10:
        print (f"{n} x {i} = {n*i}")
        i +=1


def main():
    num = int(input("Qual tabuada você deseja: "))
    print ("Tabuada com função For")
    tabuadaFor(num)
    print ("Tabuada com função While")
    tabuadaWhile(num)

main()
'''

def tabuadaFor(n):
    tabuada = []
    for i in range (0, 11):
        tabuada.append (f"{n} x {i} = {n*i}")
    return (tabuada)

def tabuadaWhile(n):
    i = 0
    tabuada = []
    while i <= 10:
        tabuada.append  (f"{n} x {i} = {n*i}")
        i +=1
    return (tabuada)


def main():
    num = int(input("Qual tabuada você deseja: "))
    print ("Tabuada com função For")
    print (tabuadaFor(num))
    print ("Tabuada com função While")
    print (tabuadaWhile(num))

main()



