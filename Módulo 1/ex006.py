numero = int(input('Digite um número: '))

print('O dobro de {} é {}.'.format(numero, (numero*2)))
print('O triplo de {} é {}.'.format(numero, (numero*3)))
print('A raiz quadrada de {} é {:.2f}.'. format(numero, (numero**(1/2))))

# Além de (numero**(1/2)), é possível substituir por pow(numero, (1/2))
