num = int(input('Digite um número para a tabuada: '))

print(f'\nTABUADA DO {num}')
for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')
