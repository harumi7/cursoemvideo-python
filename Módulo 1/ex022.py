# DESAFIO 022
contador = 0
nome_completo = input('Digite seu nome completo: ')
print(f'Nome completo em letras maiúsculas: {nome_completo.strip().upper()}')
print(f'Nome completo em letras minúsculas: {nome_completo.strip().lower()}')
print(f'O nome completo possui: {len(nome_completo.strip()) - nome_completo.count(" ")} caracteres')
print(f'O primeiro nome, "{nome_completo.split()[0].title()}", possui: {len(nome_completo.split()[0])} caracteres')
