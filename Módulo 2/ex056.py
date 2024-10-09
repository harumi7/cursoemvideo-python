soma_idades = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''
mulheres_menos_que_vinte = 0
for i in range(4):
    print(f'Pessoa {i + 1}')
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo: ')
    print()

    soma_idades += idade

    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    elif idade_homem_mais_velho == idade:
        nome_homem_mais_velho += ' e ' + nome
    elif sexo == 'F' and idade < 20:
        mulheres_menos_que_vinte += 1
print()
print(f'A média das idades é: {soma_idades / 4:.2f}')
print(f'O homem mais velho é {nome_homem_mais_velho}.')
print(f'{mulheres_menos_que_vinte} mulheres possuem menos de 20 anos.')
