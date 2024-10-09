aluguel = int(input('O carro foi alugado por quantos dias?: '))
km = float(input('Quantos km rodados?: '))

preco_total = (aluguel * 60) + (km * 0.15)

print(f'O total a pagar é de R${preco_total:.2f}.')
