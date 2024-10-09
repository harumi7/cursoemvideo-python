partidas = list()
jogador = dict()
jogador['nome'] = str(input("Nome: "))
partidas_jogadas = int(input("Partidas jogadas: "))
for partida in range(partidas_jogadas):
    partidas.append(int(input(f"Número de gols na partida {partida + 1}: ")))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print("_" * 60)
print(jogador)
print("_" * 60)

for chave, valor in jogador.items():
    print(f"O campo {chave} tem o valor {valor}.")
print("_" * 60)

print(f"O jogador {jogador['nome']} jogou {jogador['total']} partidas.")
for indice, valor in enumerate(jogador['gols']):
    print(f"=> Na partida {indice}, fez {valor} gols.")
print(f"Foi um total de {jogador['total']} gols.")
