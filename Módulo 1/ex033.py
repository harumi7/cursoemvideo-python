"""
numeros = []
for i in range(3):
    num = int(input(f'Digite o {i + 1}° número: '))
    numeros.append(num)

print(f'O menor número digitado foi: {min(numeros)}')
print(f'O maior número digitado foi: {max(numeros)}')
"""

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num2 and num3 < num1:
    menor = num3

maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print(f'O maior número é {maior}.\n'
      f'O menor número é {menor}')
