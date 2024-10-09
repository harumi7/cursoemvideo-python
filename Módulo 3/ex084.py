pessoas = []
dado = []
maior_peso = None
menor_peso = None

while True:
    dado.append(str(input("Nome: ")))
    dado.append(float(input("Peso: ")))
    pessoas.append(dado[:])
    dado.clear()
    continuar = str(input("Deseja continuar? [S/N] "))
    if continuar in 'Nn':
        break

for pessoa in pessoas:
    if maior_peso is None or menor_peso is None:
        maior_peso = menor_peso = pessoa[1]
    elif pessoa[1] > maior_peso:
        maior_peso = pessoa[1]
    elif pessoa[1] < menor_peso:
        menor_peso = pessoa[1]

print(f"Ao todo, você cadastrou {len(pessoas)} pessoas.")
print(f"O maior peso é de {maior_peso}Kg.")
print(f"O menor peso é de {menor_peso}Kg.")
