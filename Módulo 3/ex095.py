time = []
partidas = []
jogador = dict()

while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome: "))
    while True:
        try:
            partidas_jogadas = int(input("Partidas jogadas: "))
            break
        except ValueError:
            print("[!] Digite um valor válido.")
    partidas.clear()
    for partida in range(partidas_jogadas):
        while True:
            try:
                partidas.append(int(input(f"Número de gols na partida {partida + 1}: ")))
                break
            except ValueError:
                print("[!] Digite um valor válido.")
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resposta = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resposta in "SN":
            break
        print("ERRO! Responda apenas com S ou N.")
    if resposta == "N":
        break

print("=" * 50)

print("COD ", end="")
for indice in jogador.keys():
    print(f"{indice:<15}".upper(), end="")
print()
print("_" * 50)
for chave, valor in enumerate(time):
    print(f"{chave:>3} ", end="")
    for dado in valor.values():
        print(f"{str(dado):<15}", end="")
    print()

print("=" * 50)

while True:
    try:
        busca = int(input("Mostrar dados de qual jogador? (999 para parar) "))
        if busca == 999:
            break
        elif busca >= len(time):
            print(f"ERRO! Não existe jogador com código {busca}!")
        else:
            print(f"--- Levantamento do jogador {time[busca]['nome']} ---".upper())
            for indice, gols in enumerate(time[busca]['gols']):
                print(f"    No jogo {indice + 1} fez {gols} gols.")
        print("_" * 50)
    except ValueError:
        print("[!] Digite um valor válido.")
print("<< VOLTE SEMPRE >>")
