primeiro_valor = int(input("Digite um valor: "))
segundo_valor = int(input("Digite outro valor: "))
soma = primeiro_valor + segundo_valor

print(
    f"A soma entre \033[0;33m{primeiro_valor}\033[m e \033[0;33m{segundo_valor}\033[m é igual a \033[1;32m{soma}\033[m!"
)
