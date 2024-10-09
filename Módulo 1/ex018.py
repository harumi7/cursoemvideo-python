import math

'''
as funções sin, cos e tan dá o resultado em radianos, portanto é necessário,
primeiramente, converter o ângulo inserido em radiano.
'''
angle = int(input('Enter any angle: '))
angle_rad = math.radians(angle)
print(f'About the {angle}° angle: \n'
      f'sin = {math.sin(angle_rad):.2f} \n'
      f'cos = {math.cos(angle_rad):.2f} \n'
      f'tan = {math.tan(angle_rad):.2f}')
