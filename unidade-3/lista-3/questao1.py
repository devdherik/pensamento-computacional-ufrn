N = int(input("Qual o N? "))
lista = []

print("Digite os valores: ")
for i in range(N):
    valor = int(input())
    lista.append(valor)

op = int(input("Qual a op? "))
a = int(input("Qual o A? "))
b = int(input("Qual o B? "))

num_a = lista[a-1]
num_b = lista[b-1]

if op == 0:
    soma = num_a + num_b
    print("{} + {} = {}".format(num_a, num_b, soma))
elif op == 1:
    multi = num_a * num_b
    print("{} * {} = {}".format(num_a, num_b, multi))
else: 
    print("Operação inválida. Tente novamente.")

    