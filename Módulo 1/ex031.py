while True:
    try:
        distancia = float(input('Digite a distância da viagem: '))
    except:
        print('Digite apenas números.')
        continue

    if 0 <= distancia <= 200:
        passagem = distancia * 0.50
        print(f'Preço da passagem: {passagem:.2f}')
    elif distancia > 200:
        passagem = distancia * 0.45
        print(f'Preço da passagem: {passagem:.2f}')
    else:
        print('Verifique se a distância digitada está correta.')
        