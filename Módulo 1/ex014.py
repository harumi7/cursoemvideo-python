celsius = float(input('Informe a temperatura em °C: '))

kelvin = celsius + 273.15
fahrenheit = ((celsius * 9) / 5) + 32

print(f'A temperatura de {celsius}°C corresponde a:\n'
      f'{kelvin}°K\n'
      f'{fahrenheit}°F')
