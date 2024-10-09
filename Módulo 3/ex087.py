soma_pares = 0
soma_terceira_coluna = 0
maior_valor_segunda_linha = 0

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        valor = int(input(f"[{linha}][{coluna}]: "))
        matriz[linha][coluna] = valor
        if valor % 2 == 0:
            soma_pares += valor
        if coluna == 2:
            soma_terceira_coluna += valor

print("=-" * 10)
for linha in range(0, 3):
    for coluna in range(0, 3):
        valor = matriz[linha][coluna]
        print(f"[{valor}]", end=' ')
        if linha == 2:
            if valor > maior_valor_segunda_linha:
                maior_valor_segunda_linha = valor
    print()
print("=-" * 10)

print(f"A soma de todos os valores pares é {soma_pares}.")
print(f"A soma dos valores da terceira coluna é {soma_terceira_coluna}.")
print(f"O maior valor da segunda linha é {maior_valor_segunda_linha}.")