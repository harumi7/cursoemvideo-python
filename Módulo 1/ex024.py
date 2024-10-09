cidade = input('Digite o nome de uma cidade: ').strip()
if cidade.split()[0].lower().title() == 'Santo':
    print('O nome da cidade começa com a palavra "Santo"!')
else:
    print('O nome da cidade não começa com a palavra "Santo"...')
