n = int(input("Quantos nomes? "))

alunos = []
for i in range(n):
    nome = input()
    alunos.append(nome)

print("Você digitou:")
alunos.reverse()

for i in range(len(alunos)):
    print(alunos[i])