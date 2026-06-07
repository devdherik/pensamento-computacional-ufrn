print("Informe os gastos no dia:")
valor = float(input())
maior = valor

if valor == 0:
    print("Você não teve gastos hoje!")
else:
    while valor != 0:
        valor = float(input())
        if valor > maior:
            maior = valor
    print("O seu maior gasto hoje foi R$ {:.2f}".format(maior))