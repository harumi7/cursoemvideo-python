from random import randint
from time import sleep

numeros = []


def sorteia(lista_numeros):
    print("Sorteando 5 números aleatórios...", end=" ")
    for _ in range(5):
        numero_sorteado = randint(0, 10)
        sleep(0.4)
        print(numero_sorteado, end=" ")
        lista_numeros.append(numero_sorteado)
    print()


def soma_par(lista_numeros):
    soma_pares = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            soma_pares += numero
    return soma_pares


sorteia(numeros)
print(f"Lista sorteada: {numeros}")
print(f"A soma dos números pares é {soma_par(numeros)}.")
