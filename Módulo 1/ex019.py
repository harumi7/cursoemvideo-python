# PRIMEIRA FORMA
from random import choice
alunos = []

for i in range(4):
    nome = input(f'Insira o nome do {i + 1}° aluno: ')
    alunos += nome,
alunos_comma = ', '.join(alunos)

# Variável alunos é uma lista
'''
Quando coloca join, a lista vira string e as
vírgulas e aspas somem, necessitando o ','.join(alunos)
para separar os nomes na hora do print().
A criação da variável alunos_comma em vez da reutilização
da váriável alunos se deve ao fato que na parte do choice(alunos),
o programa escolhe apenas uma letra da lista, e não a palavra inteira.
'''

print(f'Entre os alunos {alunos_comma}, o escolhido para apagar o quadro foi: {choice(alunos)}')

# SEGUNDA FORMA
'''
from random import choice

nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')

nomes = [nome1, nome2, nome3, nome4]

print(f'O aluno escolhido foi {choice(nomes)}.')
'''
