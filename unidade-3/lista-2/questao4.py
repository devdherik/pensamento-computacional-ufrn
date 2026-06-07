# feito compeletamente por ia

T = int(input())

for _ in range(T):
    dados = input().split()
    PA = int(dados[0])   # população da cidade A (menor)
    PB = int(dados[1])   # população da cidade B (maior)
    G1 = float(dados[2]) # taxa de crescimento de A
    G2 = float(dados[3]) # taxa de crescimento de B

    anos = 0

    # simula ano por ano enquanto A não ultrapassar B
    while PA <= PB:
        PA = int(PA + PA * G1 / 100)  # aplica crescimento em A
        PB = int(PB + PB * G2 / 100)  # aplica crescimento em B
        anos += 1
        if anos > 100:  # para imediatamente após 100 anos
            break

    if anos > 100:
        print("Mais de 1 seculo.")
    else:
        print(str(anos) + " anos.")