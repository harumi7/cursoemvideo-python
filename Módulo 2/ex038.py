num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O número {num1} é maior que o número {num2}.')
elif num2 > num1:
    print(f'O número {num2} é maior que o número {num2}.')
else:
    print('Os dois números informados são iguais.')
