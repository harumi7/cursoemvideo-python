peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'IMC: {imc:.2f}\n'
          'Abaixo do peso.')
elif 18.5 >= imc <= 25:
    print(f'IMC: {imc:.2f}\n'
          'Peso ideal.')
elif 25 >= imc <= 30:
    print(f'IMC: {imc:.2f}\n'
          'Sobrepeso.')
elif 30 >= imc <= 40:
    print(f'IMC: {imc:.2f}\n'
          'Obesidade.')
elif imc > 40:
    print(f'IMC: {imc:.2f}\n'
          'Obesidade mórbida.')
