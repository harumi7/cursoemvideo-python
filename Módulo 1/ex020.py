# PRIMEIRA FORMA
from random import sample

lista = []

for i in range(4):
    nome = input(f"Digite o nome do {i + 1}° aluno: ")
    lista += nome,
ordem = ", ".join(sample(lista, len(lista)))

print(f"A ordem de apresentação do trabalho é: {ordem}")

'''
# SEGUNDA FORMA
from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1, n2, n3, n4]
shuffle(lista)

print(f'A ordem de apresentação será: {lista}')
'''
