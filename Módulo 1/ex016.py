'''
from math import trunc

num = float(input('Digite um número: '))
print(f'O número {num} tem a parte inteira {trunc(num)}.')
'''

# Sem import math
num = float(input('Digite um número: '))
print(f'O número {num} tem a parte inteira {int(num)}.')
