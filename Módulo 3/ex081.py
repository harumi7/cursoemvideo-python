lista = []
while True:
    x = int(input('Digite um valor: '))
    lista.append(x)
    ask = input('Quer continuar? [S/N] ')
    if ask in 'Nn':
        break

print('-=' * 30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)  # .sort() não retorna uma nova lista, apenas altera a que já existe
print(f'Os valores em ordem decrescente são {lista}.')
if 5 in lista:
    print('O valor 5 foi encontrado na lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
