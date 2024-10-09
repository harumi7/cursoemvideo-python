distancia_metro = float(input('Digite uma distância em metro: '))

dm = distancia_metro * 10
cm = distancia_metro * 100
mm = distancia_metro * 1000
dam = distancia_metro / 10
hm = distancia_metro / 100
km = distancia_metro / 1000

print(f'A medida de {distancia_metro} corresponde a {cm}cm e {km}km.')

print(f'A medida de \033[1;33m{distancia_metro}\033[m corresponde a:')
print(f'\033[0;32m{dm}dm\n'
      f'{cm}cm\n'
      f'{mm}mm\n'
      f'{dam}dam\n'
      f'{hm}hm\n'
      f'{km}km\n\033[m')
