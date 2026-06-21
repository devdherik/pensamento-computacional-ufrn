"""
feito pelo claude. acho esses problemas visuais meio idiotas e useless
"""

def main():
    n = int(input("Digite o valor de n: "))

    if verifica_positivo(n):
        loucura(n)
    else:
        print("Valor invalido!")

    return


def verifica_positivo(x):
    # retorna True se x for positivo e diferente de zero, False caso contrário
    if x > 0:
        return True
    else:
        return False


def loucura(x):
    # percorre cada linha, de 1 até x
    for i in range(1, x + 1):
        linha_texto = ""
        # monta a linha repetindo o número i, i vezes
        for j in range(i):
            linha_texto = linha_texto + str(i) + " "
        print(linha_texto)


main()