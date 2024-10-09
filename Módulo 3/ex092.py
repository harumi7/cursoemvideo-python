import datetime

pessoa = dict()

pessoa["nome"] = str(input("Nome: "))

ano_nascimento = int(input("Ano de nascimento: "))
idade = datetime.date.today().year - ano_nascimento
pessoa["idade"] = idade

pessoa["ctps"] = int(input("CTPS (0 não tem): "))
if pessoa["ctps"] != 0:
    pessoa["ano_contratacao"] = int(input("Ano de contratação: "))
    pessoa["salario"] = float(input("Salário: "))

    anos_contribuidos = datetime.date.today().year - pessoa["ano_contratacao"]
    anos_faltantes_aposentar = 35 - anos_contribuidos
    pessoa["idade_aposentar"] = pessoa["idade"] + anos_faltantes_aposentar

print("_" * 20)
for chave, valor in pessoa.items():
    print(f"{chave.capitalize()}: {valor}")
print("_" * 20)
