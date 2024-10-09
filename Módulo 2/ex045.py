from random import choice

lista = ['Pedra', 'Papel', 'Tesoura']

print('\033[1;33m=================\033[m\n'
      '\033[1;33mJOGO DO JANKENPON\033[m\n'
      '\033[1;33m=================\033[m')
while True:
    selecao_usuario = str(input('-> Pedra, papel ou tesoura?: ').strip().title())
    selecao_computador = choice(lista)
    print('\033[0;33mJANKENPON!\033[m')

    if selecao_computador == selecao_usuario:
        print(f'USUÁRIO: {selecao_usuario}\n'
              f'COMPUTADOR: {selecao_computador}')
        print('\033[0;37mAiko dessho!\033[m')
        print()
        continue
    elif selecao_usuario == 'Tesoura' and selecao_computador == 'Papel':
        print(f'USUÁRIO: {selecao_usuario}\n'
              f'COMPUTADOR: {selecao_computador}\n'
              '\033[0;32m**Usuário ganhou!**\033[m')
    elif selecao_usuario == 'Papel' and selecao_computador == 'Pedra':
        print(f'USUÁRIO: {selecao_usuario}\n'
              f'COMPUTADOR: {selecao_computador}\n'
              '\033[0;32m**Usuário ganhou!**\033[m')
    elif selecao_usuario == 'Pedra' and selecao_computador == 'Tesoura':
        print(f'USUÁRIO: {selecao_usuario}\n'
              f'COMPUTADOR: {selecao_computador}\n'
              '\033[0;32m**Usuário ganhou!**\033[m')
    elif selecao_usuario == 0:
        print('Saindo do programa...')
    else:
        print(f'USUÁRIO: {selecao_usuario}\n'
              f'COMPUTADOR: {selecao_computador}\n'
              '\033[0:31mEu, um mero computador, ganhei!\033[m')
    print()
