import random

jogos = list()
dado = list()

print("Mega Sena - Palpites".upper())

jogos_gerados = int(input("Quantos jogos deseja gerar? "))
for _ in range(jogos_gerados):
    for i in range(0, 6):
        numero = random.randint(0, 60)
        dado.append(numero)
    jogos.append(dado[:])
    dado.clear()

for jogo in jogos:
    print(f"{jogo}")
    