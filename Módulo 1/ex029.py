# RADAR ELETRÔNICO
km = int(input('Velocidade atual do automóvel: '))
km_acima = km - 80
multa = km_acima * 7

if km > 80:
    print(f'Automóvel multado. A multa a pagar é de R${multa:.2f}.')
else:
    print('Automóvel está dentro da velocidade permitida.')
