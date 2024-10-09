lista = []
lista_pares = []
lista_impares = []
while True:
        x = int(input('Digite um número: '))
        lista.append(x)
        if x % 2 == 0:
            lista_pares.append(x)
        else:
            lista_impares.append(x)

        ask = str(input('Quer continuar? [S/N] '))
        if ask in 'Nn':
            break

print(f'A lista completa é {lista}.')
print(f'A lista de pares é {lista_pares}.')
print(f'A lista de ímpares é {lista_impares}.')

