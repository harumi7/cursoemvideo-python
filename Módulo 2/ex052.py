num = int(input('Digite um número: '))
# numero primo: maior que 1, divisível por 1 e por si mesmo
for i in range(1, 1001):
    if num % i == 0 and i != 1 and i != num:
        print('Não é número primo.')
        break
else:
    print('É número primo.')
