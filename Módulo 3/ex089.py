ficha = []

while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    continuar = str(input("Deseja continuar? [S/N] "))
    if continuar in 'Nn':
        break

print("=-" * 30)
print(f'{"No.":<4}{"Nome".upper():<10}{"Média".upper():>8}')
print("_" * 25)

for index, value in enumerate(ficha):
    print(f"{index:<4}{value[0]:<10}{value[2]:>8.1f}")

while True:
    print("-" * 35)
    opcao = int(input("Mostrar notas de qual aluno? [999 interrompe] "))
    if opcao == 999:
        print("Finalizando...".upper())
        break
    if opcao <= len(ficha) - 1:
        print(f"Notas de {ficha[opcao][0]} são {ficha[opcao][1]}")

print("<<< Volte sempre >>>".upper())
