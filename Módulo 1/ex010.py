dinheiro = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = dinheiro / 4.93
yen = dinheiro / 0.037
euro = dinheiro / 5.37

dolar_resp = ['Dólar', 'dólar', 'Dolar', 'dolar']
yen_resp = ['Yen', 'yen', 'iene', 'Iene']
euro_resp = ['Euro', 'euro']
converter = input('Deseja converter para? (dólar, yen, euro): ')
if converter in dolar_resp:
    print(f'Com R${dinheiro} você pode comprar \033[0;32mUS${dolar:.2f}\033[m.')
elif converter in yen_resp:
    print(f'Com R${dinheiro} você pode comprar \033[0;32m¥{yen:.2f}\033[m.')
elif converter in euro_resp:
    print(f'Com R${dinheiro} você pode comprar \033[0;32m€{euro:.2f}\033[m.')
else:
    print(f'Resposta inválida, tente novamente.')
