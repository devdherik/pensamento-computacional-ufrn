"""
feito pelo claude e entendido por mim :D
"""


def main():
    valor = int(input("Digite um valor: "))
    print(f"Inverso: {inverso(valor)}")
    return


def inverso(n):
    texto = str(n)              # transforma o número em string, pra poder acessar cada caractere
    texto_invertido = ""        # string vazia que vai guardar o resultado invertido

    # percorre os índices da string de trás pra frente
    for i in range(len(texto) - 1, -1, -1):
        texto_invertido = texto_invertido + texto[i]

    return texto_invertido


main()