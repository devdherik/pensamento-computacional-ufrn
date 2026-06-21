"""
ESSA FOI FEITA TOTALMENTE PELA IA, SO FIZ ENTENDER (ESTAVA SEM SACO)
"""

n = int(input("Quantos alunos? "))
print("Digite os nomes dos alunos:")

alunos = []
for i in range(n):
    nome = input()
    alunos.append(nome)

# pega as posições das cadeiras pares (cadeira 2, 4, 6... = índices 1, 3, 5...)
indices_pares = list(range(1, n, 2))

# pega os nomes que estão nessas posições
nomes_pares = []
for idx in indices_pares:
    nomes_pares.append(alunos[idx])

# inverte a ordem desses nomes
nomes_pares.reverse()

# recoloca cada nome invertido na mesma posição original
for i in range(len(indices_pares)):
    alunos[indices_pares[i]] = nomes_pares[i]

print("Nova lista:")
for nome in alunos:
    print(nome)