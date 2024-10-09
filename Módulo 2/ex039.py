from datetime import date

while True:
    data_nascimento = input('Digite a data de nascimento (dd/mm/aaaa): ')
    if len(data_nascimento) == 10:
        break
    else:
        print('Valor inválido, tente novamente.')
        continue

genero = input('Gênero (F/M): ')
if genero == 'F':
    print('Não é necessário realizar o alistamento militar.')
elif genero == 'M':
    # verificar já fez aniversário esse ano
    if int(data_nascimento[3:5]) < date.today().month:
        idade = date.today().year - int(data_nascimento[6:])
    else:
        idade = date.today().year - int(data_nascimento[6:]) - 1

    # verificar idade
    if idade == 18:
        print(f'Você tem {idade} anos.\n'
              'Está na hora de realizar o alistamento militar.')
    elif idade > 18:
        tempo = idade - 18
        print(f'Você tem {idade} anos.\n'
              'Já passou da hora de realizar o alistamento militar.\n'
              f'Já se passaram: {tempo} ano(s)')
    else:
        tempo = 18 - idade
        print(f'Você tem {idade} anos.\n'
              'Ainda não é hora de realizar o alistamento militar.\n'
              f'Ainda faltam: {tempo} ano(s)')
