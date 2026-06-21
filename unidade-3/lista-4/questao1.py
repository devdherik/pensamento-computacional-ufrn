
"""
codigo desenvolvido com AUXILIO do claude. os comentarios foram feitos totalmente por ele, mas quem escreveu todo o resto fui eu. aceita bb
"""


def main():
    # lê quantos números o usuário vai digitar
    n = int(input("Qual o valor de N? "))

    # lista vazia que vai guardar todos os números digitados
    conjunto_n = []
    for i in range(n):
        valor = int(input())          # lê um número e converte pra inteiro
        conjunto_n.append(valor)      # adiciona esse número na lista

    print("A classificação é: ")

    # percorre cada número da lista, usando o índice i (0, 1, 2...)
    for i in range(n):
        # chama a função lista_divisores() passando o número atual
        # guarda o resultado (a lista de divisores) na variável "divisores"
        divisores = lista_divisores(conjunto_n[i])

        # um número primo só tem 2 divisores: o 1 e ele mesmo
        # por isso, se a lista de divisores tem exatamente 2 itens, é primo
        if len(divisores) == 2:
            print(f"{conjunto_n[i]} é primo")
        else:
            # se não é primo, imprime o número e a lista de divisores
            # que já estava calculada na variável "divisores"
            print(f"{conjunto_n[i]} não é primo, os divisores são: {divisores}")

    return


def lista_divisores(x):
    # essa função recebe um número x e devolve a lista de todos os divisores dele

    divisores = []  # lista vazia que vai guardar os divisores encontrados

    # testa todos os números de 1 até x (incluindo o próprio x)
    for i in range(1, x + 1):
        # se x dividido por i tem resto 0, então i é divisor de x
        if x % i == 0:
            divisores.append(i)

    # devolve a lista pronta pra quem chamou a função
    return divisores


# chama a função main() pra começar a execução do programa
main()