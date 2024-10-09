"""
while True:
    num = int(input('Digite um número (digite 0 para sair): '))
    numero = str(num)
    if num == 0:
        print('Você escolheu sair.')
        break
    elif 0 <= num <= 9999:
        print(f'Unidade: {numero[-1]}')
        try:
            print(f'Dezena: {numero[-2]}')
        except IndexError:
            pass
        try:
            print(f'Centena: {numero[-3]}')
        except IndexError:
            pass
        try:
            print(f'Milhar: {numero[-4]}')
        except IndexError:
            pass
    else:
        print('Digite um número entre 0 e 9999.')
        continue
"""

while True:
    num = int(input('Digite um número (digite 0 para sair): '))
    if num == 0:
        print('Você escolheu sair.')
        break
    elif 0 <= num <= 9999:
        u = num // 1 % 10
        d = num // 10 % 10
        c = num // 100 % 10
        m = num // 1000 % 10
        print(f'Unidade: {u}')
        print(f'Dezena: {d}')
        print(f'Centena: {c}')
        print(f'Milhar: {m}')
    else:
        print('Digite um número entre 0 e 9999.')
        continue