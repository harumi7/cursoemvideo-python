from datetime import date

maior = 0
menor = 0
for i in range(7):
    data_nasc = input(f'Digite a data de nascimento da {i + 1}° pessoa (dd/mm/aaaa): ')
    if date.today().year - int(data_nasc[6:10]) > 18:
        maior += 1
    elif date.today().year - int(data_nasc[6:10]) < 18:
        menor += 1
    else:
        if int(data_nasc[3:5]) > date.today().month:
            menor += 1
        elif int(data_nasc[3:5]) < date.today().month:
            maior += 1
        else:
            if int(data_nasc[0:2]) > date.today().day:
                menor += 1
            else:
                maior += 1

print(f'{maior} pessoas já são de maior.\n'
      f'{menor} pessoas ainda não atingiram a maioridade.')
