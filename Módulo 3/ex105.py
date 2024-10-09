def notas(*notas_alunos, sit=False):
    """
    Função para analisar notas e situações de vários alunos.

    :param notas_alunos: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    dicionario_notas_alunos = {
        'quantidade_notas': len(notas_alunos),
        'maior_notas': max(notas_alunos),
        'menor_nota': min(notas_alunos),
        'media': sum(notas_alunos) / len(notas_alunos),
    }

    if sit:
        if dicionario_notas_alunos['media'] < 6:
            dicionario_notas_alunos['sit'] = "Ruim"
        elif dicionario_notas_alunos['media'] < 7:
            dicionario_notas_alunos['sit'] = "Razoável"
        else:
            dicionario_notas_alunos['sit'] = "Boa"
    return dicionario_notas_alunos


resposta = notas(7, 8.5, 9.1, 6, 5, sit=True)
print(resposta)
