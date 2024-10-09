def ajuda(comando: str):
    print("_" * 40)
    # "\033[LETRA;COR;FUNDOmDigiteSeuTextoAqui\033[m"
    # 0=padrão; 30=preto; 107=branco
    print("\033[0;30;107mAcessando o manual do comando '" + comando + "'\033[m")
    print("_" * 40)

    # 0=padrão; 30=preto; 46=ciano
    print("\033[0;30;46m")
    help(comando)
    print("\033[m")  # Reseta para a cor padrão


# Programa principal
while True:
    print("--- SISTEMA DE AJUDA PYHELP ---")
    comando_usuario = str(input("Função ou biblioteca > "))
    if comando_usuario.upper() == "FIM":
        break
    ajuda(comando_usuario)
    print("=" * 40)
print("Você saiu do sistema de ajuda PyHelp.")
