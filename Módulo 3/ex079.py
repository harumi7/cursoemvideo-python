lista = []
print('Para sair, digite 0.')
while True:
    num = int(input(f'Digite um número: '))
    if num == 0:
        print('Saindo...')
        break
    elif num in lista:
        print('Número já digitado anteriormente.')
    else:
        lista.append(num)
if lista:
    lista.sort()  # <- sort não cria lista nova, só ordena a que já existe
    print(lista)
else:
    print('<!> Não foram adicionados números no sistema.')
