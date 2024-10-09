from random import randint
from time import sleep


def linhas(quantidade):
    print('=' * quantidade)


while True:
    linhas(55)
    print('JOGO DA ADIVINHAÇÃO')
    print('Pense em um número entre 0 e 5. Vou tentar adivinhar!')
    sleep(0.5)
    linhas(55)
    print('PROCESSANDO UM NÚMERO...')
    sleep(1)
    numero_computador = randint(0, 5)
    numero_usuario = int(input('Em que número eu pensei? (digite 101 para sair): '))
    if numero_computador == numero_usuario:
        print(f'Você acertou! O número que pensei foi {numero_computador}!')
        sleep(5)
    elif 0 <= numero_usuario <= 5:
        print(f'Você errou, que pena! O número que pensei foi {numero_computador}!')
        sleep(5)
    elif numero_usuario == 101:
        break
    else:
        print('O número que você digitou não está entre 0 e 5...')
        sleep(3)
