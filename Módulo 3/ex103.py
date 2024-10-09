def ficha(nome="<desconhecido>", gols=0):
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")


print("_" * 50)
print("Ficha do jogador".center(46))
print("=" * 50)
nome_jogador = str(input("Nome do jogador: "))
gols_jogador = str(input("Número de gols: "))

if gols_jogador.isnumeric():
    gols_jogador = int(gols_jogador)
else:
    gols_jogador = 0
if nome_jogador.strip() == "":
    ficha(gols=gols_jogador)
else:
    ficha(nome_jogador, gols_jogador)
print("_" * 50)
