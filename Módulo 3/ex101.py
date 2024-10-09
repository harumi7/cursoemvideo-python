from datetime import date


def voto(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento

    if idade < 16:
        return "Com {0} anos: {1}".format(idade, "Voto negado".upper())
    elif idade < 18:
        return "Com {0} anos: {1}".format(idade, "Voto opcional".upper())
    elif idade < 70:
        return "Com {0} anos: {1}".format(idade, "Voto obrigatório".upper())
    else:
        return "Com {0} anos: {1}".format(idade, "Voto opcional".upper())


print("=== Você está apto para votar? ===")
ano_nascimento_eleitor = int(input("Ano de nascimento: "))
print(voto(ano_nascimento_eleitor))
