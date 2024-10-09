valor_casa = float(input('Valor da casa: '))
salario_comprador = float(input('Salário do comprador: '))
anos_para_pagar = int(input('Pagar em quantos anos?: '))

trinta_porcento = salario_comprador * (30/100)

valor_prestacao_mensal = valor_casa / (anos_para_pagar * 12)

if valor_prestacao_mensal <= trinta_porcento:
    print(f'Empréstimo pode ser concedido. \n'
          f'A prestação mensal será de \033[0;33mR${valor_prestacao_mensal:.2f}\033[m.')
else:
    print(f'Empréstimo negado.\n'
          f'Para pagar uma casa de R${valor_casa:.2f} em {anos_para_pagar} anos a prestação será de '
          f'\033[0;33mR${valor_prestacao_mensal:.2f}\033[m. \n'
          f'O valor da prestação mensal ultrapassa 30% do seu salário.')
