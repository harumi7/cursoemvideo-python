frase = str(input('Frase: '))

palindromo = frase

for i in range(1, len(frase)):
    for j in range(-1, len(frase), -1):
        if i != j:
            print('Não é palíndromo.')
            break
        else:
            pass
