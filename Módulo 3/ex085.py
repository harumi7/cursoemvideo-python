pares = list()
impares = list()

for i in range(0, 7):
    valor = int(input(f"Digite o {i + 1}° valor: "))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
