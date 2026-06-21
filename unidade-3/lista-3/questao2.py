njogadores = int(input("Quantidade de jogadores? "))
print("Digite os dados para cada jogador:")

lista_jogadores = []

for i in range(njogadores):
    infos = input()
    lista_jogadores.append(infos)

total_s = 0
total_b = 0
total_a = 0
total_s1 = 0 
total_b1 = 0
total_a1 = 0 

#aqui o 'len()' retorna o tamanho da lista, tipo: se a lista tiver 3 elementos, o range vai ser 3
for i in range(len(lista_jogadores)):
    #aqui, dados se torna uma lista para cada jogador.
    #renan 10 20 12 1 10 9
    #0 -> nome, 1 -> total de saques(total_s), 2 -> total de bloqueios(total_b), 3 -> total de ataques(total_a)
    #4 -> saques bem sucedidos(total_s1), 5 -> bloqueios bem sucedidos(total_b1), 6 -> ataques bem sucedidos(total_a1)
    dados = lista_jogadores[i].split(" ")
    total_s += int(dados[1])
    total_b += int(dados[2])
    total_a += int(dados[3])
    total_s1 += int(dados[4])
    total_b1 += int(dados[5])
    total_a1 += int(dados[6])

print("As estatísticas do jogo são as seguintes:")
print(f"Pontos de Saque: {total_s1/total_s*100:.2f} %")
print(f"Pontos de Bloqueio: {total_b1/total_b*100:.2f} %")
print(f"Pontos de Ataque: {total_a1/total_a*100:.2f} %")