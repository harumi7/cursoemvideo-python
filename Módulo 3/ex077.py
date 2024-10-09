tupla = ('gato', 'batata', 'caderno', 'mobilia', 'bruxa', 'anel', 'borboleta', 'historia',
         'pipoca', 'bode', 'macaco', 'quarto', 'janela', 'ouro', 'dezoito', 'ilha')

vogal = ('a', 'e', 'i', 'o', 'u')

vogais = ''
for i in tupla:
    print(f'\nNa palavra {i} temos: ', end='')
    for j in i:
        if j in vogal:
            print(j, end=' ')
