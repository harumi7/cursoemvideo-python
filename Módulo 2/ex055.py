maior = 0
menor = 1000000
for i in range(5):
    peso = float(input(f'Digite o {i + 1}° peso: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print(f'O maior peso é {maior:.2f}kg.\n'
      f'O menor peso é {menor:.2f}kg.')
