from time import sleep

def maior(*numeros):
    cont = maior = 0
    print("=" * 30)
    print("Analisando os valores informados...")
    for valor in numeros:
        print(f"{valor}", end=" ")
        sleep(0.4)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"Foram informados {len(numeros)} valores ao todo.")
    print(f"O maior valor informado foi {maior}.")


# Programa principal
maior(8, 6, 7, 5, 3, 0, 9)
maior(7, 1, 9, 2)
