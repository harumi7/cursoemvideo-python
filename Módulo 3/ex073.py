futebol = ('Botafogo', 'Palmeiras', 'São Paulo', 'Atlético-MG', 'Grêmio', 'Cruzeiro',
           'Flamengo', 'Fluminense', 'Fortaleza', 'Bragantino', 'Athletico-PR', 'Santos',
           'Internacional', 'Corinthians', 'Cuiabá', 'Bahia', 'Goiás', 'Vasco da Gama',
           'América-MG', 'Coritiba')
print('LISTA DE TIMES DO BRASILEIRÃO')
for i, j in enumerate(futebol, start=1):
    print(f'{i}. {j}')
print()
# a) 5 primeiros colocados
print(f'a) 5 primeiros colocados:\n'
      f'{futebol[0:6]}\n')

# b) últimos 4 colocados
print(f'b) últimos 4 colocados:\n'
      f'{futebol[-4:]}\n')

# c) times em ordem alfabética
print(f'c) times em ordem alfabética:\n'
      f'{sorted(futebol)}\n')

# d) posição do time Bahia
print(f'd) O time Bahia está na posição {futebol.index("Bahia")}.')
