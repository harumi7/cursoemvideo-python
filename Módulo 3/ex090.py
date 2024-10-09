aluno = dict()

aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input(f"Média de {aluno['nome']}: "))

if aluno['media'] > 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

for chave, valor in aluno.items():
    print(f"- {chave} é igual a {valor}")
