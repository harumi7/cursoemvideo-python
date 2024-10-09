salario = float(input('Digite o seu salário: R$'))
if salario > 1250:
    aumento = salario + (salario * (10/100))
else:
    aumento = salario + (salario * (15/100))
print(f'Com o aumento, seu salário foi para: R${aumento:.2f}')
