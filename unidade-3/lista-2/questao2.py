N = int(input())
while N != 0:
    for linha in range(1, N+1):
        for coluna in range(1, N+1):
            valor = abs(linha - coluna) + 1
            print(valor, end=" ")
        print()
    print()
    N = int(input()) 