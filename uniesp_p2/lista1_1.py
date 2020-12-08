
def converte (f):
    c = 5* ((f-32)/9 )
    return(c)


def main ():

    tempF = float(input("Digite a temperatura em Fahrhenheit: "))
    
    print (f"A temperatura {tempF}°F em Celsius é {converte(tempF)}°C")

main()