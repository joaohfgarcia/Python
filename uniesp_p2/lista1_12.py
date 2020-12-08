def main():
    alunos = []
    notas = []
    media = []
    resultado = []
    
    for i in range(0,2):
        alunos.append(input(f"Digite o nome do aluno {i+1}: "))

        for j in range(0,3):
            notas.append(int(input(f"Digite a nota {j+1}: ")))
        media.append(float((notas[0]*2 + notas[1]*4 + notas[2]*3)/10))
        
        if (media[i] > 7):
            resultado.append("Aprovado")
        elif (media[i] > 4 and media[i] < 7):
            resultado.append("Recuperação")
        else:
            resultado.append("Reprovado")
    
    mediaGeral = sum(media)/len(media)

    for i in range (0,2):
        print (alunos[i])
        print (resultado[i])
    
    print("\nA média geral da turma foi: ", mediaGeral)

main()