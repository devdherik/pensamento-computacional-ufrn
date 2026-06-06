temp = input("Digite a temperatura e a escala em que ela se encontra (ex: 30 C, 86 F, 300 K): ").upper()
valor, escala = temp.split(" ")
valor = float(valor)


if escala == "C":
    print("Temperatura em Celsius: {:.2f} °C".format(valor))
    print("Temperatura em Fahrenheit: {:.2f} °F".format((valor * 9/5) + 32))
    print("Temperatura em Kelvin: {:.2f} K".format(valor + 273.15))
elif escala == "F":
    print("Temperatura em Celsius: {:.2f} °C".format((valor - 32) * 5/9))
    print("Temperatura em Fahrenheit: {:.2f} °F".format(valor))
    print("Temperatura em Kelvin: {:.2f} K".format((valor + 459.67) * 5/9))
elif escala == "K":
    print("Temperatura em Celsius: {:.2f} °C".format(valor - 273.15))
    print("Temperatura em Fahrenheit: {:.2f} °F".format(valor * 9/5 - 459.67))
    print("Temperatura em Kelvin: {:.2f} K".format(valor))
else:
    print("Escala inválida. Tente Novamente.")