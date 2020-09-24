def validaNome(nome):
    tamanho = len(nome)
    if tamanho > 3:
        return ("Nome: "+nome)
    else:
        return ("Nome: Inválido")
      
def validaIdade(idade):
    if 0 < idade < 150:
        return ("Idade: "+ str(idade)+"anos")
    else:
        return ("Idade: Inválida")

def validaSalario(salario):
    if salario > 0:
        return ("Salário: R$ "+ f"{salario:.2f}")
    else:
        return ("Salário: Inválido")

def validaSexo(sexo):
    if sexo in "fF" or sexo in "mM":
        return ("Sexo: "+sexo)
    else:
        return ("Sexo: Inválido")

def validaEstadoCivil(ecivil):
    if ecivil in "sS" or ecivil in "cC" or ecivil in "vV" or ecivil in "dD":
        return ("Estado Civil: "+ecivil)
    else:
        return ("Estado Civil: Inválido")  


def main():

    print("\nPreencha abaixo os seus dados")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    salario = float(input("Salário: "))
    sexo = input("Sexo Feminino [F] ou Masculino [M]: ")
    estadocivil = input("Estado Civil, Solteiro[S], Casado[C], Viúvo[V], Divorciado[D]: ")
    salvar = input("Salvar [S] ou [N]: ")

    if salvar in "sS":

        print("\nDADOS CADASTRADOS")
        print(validaNome(nome))
        print(validaIdade(idade))
        print(validaSalario(salario))
        print(validaSexo(sexo))
        print(validaEstadoCivil(estadocivil))
        print("\nPROGRAMA ENCERRADO!")
          
    else:
        print("\nPROGRAMA ENCERRADO!")

main()