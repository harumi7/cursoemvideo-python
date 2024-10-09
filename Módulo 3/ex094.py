pessoa = dict()
lista_pessoas = list()

while True:
    pessoa['nome'] = str(input("Nome: "))
    while True:
        pessoa['genero'] = str(input("Gênero [M/F]: "))
        if pessoa['genero'] in "MmFf":
            break
    while True:
        pessoa['idade'] = int(input("Idade: "))
        if 0 < pessoa['idade'] <= 120:
            break
    lista_pessoas.append(pessoa.copy())
    pessoa.clear()
    continuar = str(input("Deseja continuar? [S/N] "))
    if continuar in 'Nn':
        break

print("_" * 70)

print(f"- Há {len(lista_pessoas)} pessoas no grupo.")

soma_idades = 0
for dicionario_pessoa in lista_pessoas:
    soma_idades += dicionario_pessoa['idade']
media_idades = soma_idades / len(lista_pessoas)
print(f"- A média de idade do grupo é {media_idades:.2f} anos.")

lista_mulheres = list()
for pessoa in lista_pessoas:
    if pessoa['genero'] == "F":
        lista_mulheres.append(pessoa['nome'])
print(f"- As mulheres do grupo são {lista_mulheres}")

lista_pessoas_idade_acima_media = list()
for pessoa in lista_pessoas:
    if pessoa['idade'] > media_idades:
        lista_pessoas_idade_acima_media.append(pessoa)
if lista_pessoas_idade_acima_media:
    print("- As pessoas com idade acima da média do grupo são: ")
    for dicionario in lista_pessoas_idade_acima_media:
        for chave, valor in dicionario.items():
            print(f"{chave} = {valor}", end='; ')
        print()
else:
    print("Não há pessoas com idade acima da média do grupo.")

print("<<< ENCERRADO >>>")
