# Primeira forma
'''
from math import pow, sqrt

cateto_op = float(input('Digite o comprimento do cateto oposto: '))
cateto_adj = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = (pow(cateto_op, 2) + pow(cateto_adj, 2))
hipotenusa_result = sqrt(hipotenusa)

print(f'A comprimento da hipotenusa do triângulo é: {hipotenusa_result:.2f}')
'''

# Segunda forma
'''
cateto_op = float(input('Digite o comprimento do cateto oposto: '))
cateto_adj = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = (cateto_op ** 2 + cateto_adj ** 2) ** 1/2

print(f'A comprimento da hipotenusa do triângulo é: {hipotenusa:.2f}')
'''

# Terceira forma
from math import hypot
cateto_op = float(input('Digite o comprimento do cateto oposto: '))
cateto_adj = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = hypot(cateto_op, cateto_adj)

print(f'A comprimento da hipotenusa do triângulo é: {hipotenusa:.2f}')
