digitar = str(input('Digite algo: ').strip().upper())
digitar = digitar.replace('Á', 'A')
digitar = digitar.replace('À', 'A')

print(f'Na palavra/frase digitada, há {digitar.count("A")} caracteres de A.')
print(f'A primeira ocorrência do caractere A se encontra na posição: {digitar.find("A") + 1}')
print(f'A última ocorrência do caractere A se encontra na posição: {digitar.rfind("A") + 1}')