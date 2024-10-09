retas = []
for i in range(3):
    comprimento = float(input('\033[0;37mDigite o comprimento da reta: '))
    retas.append(comprimento)

if retas[0] < retas[1] + retas[2] and retas[1] < retas[0] + retas[2] and retas[2] < retas[0] + retas[1]:
    print('Os segmentos informados podem formar triângulo!')
else:
    print('Os segmentos informados não podem formar triângulo.')
