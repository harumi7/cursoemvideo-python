retas = []
for i in range(3):
    comprimento = float(input('\033[0;37mDigite o comprimento da reta: '))
    retas.append(comprimento)

if retas[0] < retas[1] + retas[2] and retas[1] < retas[0] + retas[2] and retas[2] < retas[0] + retas[1]:
    print('Os segmentos informados podem formar triângulo!')
    if retas[0] == retas[1] == retas[2]:
        print('Todos os lados são iguais. Triângulo equilátero.')
    elif retas[0] == retas[1] or retas[0] == retas[2] or retas[1] == retas[2]:
        print('Dois lados são iguais. Triângulo isósceles.')
    else:
        print('Todos os lados são diferentes. Triângulo escaleno.')
else:
    print('Os segmentos informados não podem formar triângulo.')
