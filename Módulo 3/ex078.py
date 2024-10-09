lista_numeros = []
maior_numero = 0
menor_numero = 0
for i in range(5):
    valor = int(input(f'Digite o {i + 1}° valor: '))
    lista_numeros.append(valor)
    if i == 0:
        maior_numero = menor_numero = valor
    else:
        if valor > maior_numero:
            maior_numero = valor
        elif valor < menor_numero:
            menor_numero = valor

print("_" * 50)
print(f'Os números digitados foram: {lista_numeros}')
print(f'O maior valor da lista é {maior_numero} na(s) posição(ões)', end=' ')  # alternativa: max(lista)
for indice, valor in enumerate(lista_numeros):
    if valor == maior_numero:
        print(f"{indice}...", end=' ')
print()
print(f'O menor valor da lista é {menor_numero} na(s) posição(ões)', end=' ')  # alternativa: min(lista)
for indice, valor in enumerate(lista_numeros):
    if valor == menor_numero:
        print(f"{indice}...", end=' ')
