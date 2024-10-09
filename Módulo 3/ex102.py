def fatorial(numero: int):
    if numero == 0 or numero == 1:
        return 1

    fat = 1
    for i in range(numero, 1, -1):
        fat *= i
    return fat


num = 5
resultado = fatorial(num)
print(f"Fatorial de {num}: {resultado}")
