valor_compra = float(input("Qual o valor da compra: "))
forma_pagamento = input("Como gostaria de pagar: à vista (V) ou à prazo (P)? ").upper()

if forma_pagamento == "V":
    valor_compra = valor_compra * 0.95
    print("Valor à pagar: {:.2f}".format(valor_compra))
elif forma_pagamento == "P":
    valor_compra = valor_compra * 1.08
    valor_parcela = valor_compra / 3

    print("Valor à pagar: {:.2f}".format(valor_compra))
    print("Parcela 1: {:.2f}".format(valor_parcela))
    print("Parcela 2: {:.2f}".format(valor_parcela))
    print("Parcela 3: {:.2f}".format(valor_parcela))
else:
    print("Opção inválida. Tente novmente.")