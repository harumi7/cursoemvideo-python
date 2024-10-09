listagem = ('Pão', 5.90,
            'Arroz', 12.90,
            'Azeite', 40.00,
            'Feijão', 8.30,
            'Leite', 9.50,
            'Páprica', 3.50,
            'Alface', 4.80,
            'Carne de frango', 38.60)

print(f'{"=" * 40}\n'
      f'{"LISTAGEM DE PREÇOS":^40}\n'
      f'{"=" * 40}')
for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(f'{listagem[i]:.<30}', end='')
    else:
        print(f'R${listagem[i]:>7.2f}')
