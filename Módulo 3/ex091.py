from operator import itemgetter
from time import sleep
from random import randint

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

print("Valores sorteados:")
for chave, valor in jogo.items():
    print(f"O {chave} tirou {valor} no dado.")
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("=-" * 20)
print("==== Ranking dos jogadores ====".upper())
for chave, valor in enumerate(ranking):
    print(f"    {chave + 1} lugar: {valor[0]} com {valor[1]}.")
    sleep(1)