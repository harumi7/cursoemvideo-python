def leiaInt(mensagem):
    while True:
        numero = str(input(mensagem))
        if numero.isnumeric():
            return numero
        else:
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[m")


# Programa principal
numero_usuario = leiaInt("Digite um número: ")
print()
print(f"Você digitou o número {numero_usuario}.")
