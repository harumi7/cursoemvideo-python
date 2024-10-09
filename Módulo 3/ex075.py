lista = []

for i in range(5):
    num = int(input('Digite um número: '))
    lista.append(num)
tupla = tuple(lista)
print(f'TUPLA: {tupla}')

tupla_cont = tupla.count(9)
print(f'O número 9 aparece na tupla: {tupla_cont} vez(es)')

if 3 in tupla:
    tupla_index = tupla.index(3)
    print(f'O primeiro valor 3 foi digitado na posição: {tupla_index}')
else:
    print('O valor 3 não foi digitado em nenhuma posição!')

pares = []
for i in tupla:
    if i % 2 == 0:
        pares.append(i)
print(f'Os valores pares são: {pares}')

'''
lista = []
num = (int(input(f'Digite o primeiro número: ')),
       int(input(f'Digite o segundo número: ')),
       int(input(f'Digite o terceiro número: ')),
       int(input(f'Digite o quarto número: ')))
print(f'Você digitou os valores: {num}')

if 9 in num:
    print(f'O número 9 apareceu {num.count(9)} vez(es).')
else:
    print('O número 9 não foi digitado.')

if 3 in num:
    print(f'O número 3 se encontra na posição {num.index(3)}.')
else:
    print(f'O número 3 não foi digitado.')
'''