from datetime import date

data_nascimento = input('Digite a data de nascimento (dd/mm/aaaa): ')
if int(data_nascimento[3:5]) < date.today().month:
    idade = date.today().year - int(data_nascimento[6:])
else:
    idade = date.today().year - int(data_nascimento[6:]) - 1

if 0 < idade <= 9:
    print(f'Idade: {idade} anos\n'
          'Classificação: Mirim')
elif idade <= 14:
    print(f'Idade: {idade} anos\n'
          'Classificação: Mirim')
elif idade <= 19:
    print(f'Idade: {idade} anos\n'
          'Classificação: Júnior')
elif idade <= 20:
    print(f'Idade: {idade} anos\n'
          'Classificação: Sênior')
elif idade > 20:
    print(f'Idade: {idade} anos\n'
          'Classificação: Master')
    