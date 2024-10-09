from time import sleep


def linha():
    print("_" * 30)


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    linha()
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    sleep(0.5)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f"{cont}", end=" ")
            sleep(0.4)
            cont += passo
        print("FIM!")

    else:
        cont = inicio
        while cont >= fim:
            print(f"{cont}", end=" ")
            sleep(0.4)
            cont -= passo
        print("FIM!")


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
linha()
print("Personalize a contagem:")
inicio_usuario = int(input("Início: "))
fim_usuario = int(input("Fim: "))
passo_usuario = int(input("Passo: "))
contador(inicio_usuario, fim_usuario, passo_usuario)
