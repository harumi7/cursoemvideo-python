while True:
    nome = input('Digite o seu nome completo (digite 0 para sair): ')
    if nome == '0':
        print('Você escolheu sair.')
        break
    elif nome:
        nome = nome.split()
        if len(nome) == 1:
            print('Opa! Digite o seu nome completo.')
        else:
            print(f'Primeiro nome: {nome[0].strip().title()}\n'
                  f'Último nome: {nome[-1].strip().title()}')
            continue
    elif not nome:
        print('Preencha o campo de resposta.')
