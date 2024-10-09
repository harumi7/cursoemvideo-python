nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print(f'Média: {media}, REPROVADO.')
elif 5 <= media < 7:
    print(f'Média: {media}, RECUPERAÇÃO.')
else:
    print(f'Média: {media}, APROVADO.')
