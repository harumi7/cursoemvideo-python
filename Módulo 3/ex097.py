def escreva(texto):
    tamanho = len(texto) + 4
    print("~" * tamanho)
    print(f"{texto.center(tamanho)} ")
    print("~" * tamanho)


texto_usuario = str(input("Digite: "))
escreva(texto_usuario)
