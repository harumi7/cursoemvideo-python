valor_produto = float(input('Digite o valor do produto: '))
pagamento = int(input('Formas de pagamento: \n'
                      '1: à vista com dinheiro/cheque (10% de desconto)\n'
                      '2: à vista no cartão (5% de desconto) \n'
                      '3: 2x no cartão\n'
                      '4: 3x ou mais no cartão (20% de juros)\n'
                      'Digite a forma de pagamento desejada: '))
print()
if pagamento == 1:
    valor_com_desconto = valor_produto - (valor_produto * 10/100)
    print(f'O valor do produto com desconto de 10% é de: R${valor_com_desconto:.2f}')
elif pagamento == 2:
    valor_com_desconto = valor_produto - (valor_produto * 5/100)
    print(f'O valor do produto com desconto de 5% é de: R${valor_com_desconto:.2f}')
elif pagamento == 3:
    print(f'Valor do produto a pagar: {valor_produto}')
elif pagamento == 4:
    valor_com_desconto = valor_produto + (valor_produto * 20/100)
    print(f'O valor do produto com juros de 20% é de: R${valor_com_desconto:.2f}')
