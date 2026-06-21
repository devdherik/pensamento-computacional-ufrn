"""
vamos lar pra essa questao 2, começando agora
feito por mim com ajuda do claude
"""


def main():
    n1 = int(input("Digite número 1: "))
    n2 = int(input("Digite número 2: "))
    n3 = int(input("Digite número 3: "))
    n4 = int(input("Digite número 4: "))


    soma_par = 0
    if funcao_par(n1) == 0:
        soma_par += n1
    if funcao_par(n2) == 0:
        soma_par += n2
    if funcao_par(n3) == 0:
        soma_par += n3
    if funcao_par(n4) == 0:
        soma_par += n4

    print(f"Soma dos números pares: {soma_par}")

    return


def funcao_par(num):
    if num % 2 == 0:
        return(0)
    else:
        return(1)

main()