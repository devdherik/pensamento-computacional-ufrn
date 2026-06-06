entrada = input("Digite seis numeros separados por espaços, sendo os dois primeiros as coordenadas de um canto superior esquerdo de um retângulo, os dois seguintes serão os as coordenadas do canto inferior direito. Por fim, os dois ultimos servirão como um ponto aleatório e verificarei se este mesmo ponto se encontra dentro do retângulo que você criou com os pares de coordenadas. ")
x1, y1, x2, y2, xp, yp = entrada.split(" ")
x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)
xp = int(xp)
yp = int(yp)

if xp >= x1 and xp <= x2 and yp >= y1 and yp <=y2:
    print("Dentro!")
else:
    print("Fora!")