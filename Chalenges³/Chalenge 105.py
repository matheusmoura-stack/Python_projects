def notas(*num,  sit=False):
    """
    --> Função que analisa as notas e situações de vários alunos.
    :param num: uma ou mais notas do(s) aluno(s) (aceita várias).
    :param sit: Valor opcional indicando se deve ou não adicionar a situação do aluno.
    :return: Retorna o dicionário com as informações da turma.
    """
    n = dict()
    n['total de notas'] = len(num)
    n['maior'] = max(num)
    n['menor'] = min(num)
    n['media'] = sum(num) / len(num)
    if sit:
        if n['media'] >= 7:
            n['situação'] = 'BOA!'
        elif n['media'] < 5:
            n['situação'] = 'RUIM!'
        else:
            n['situação'] = 'RAZOÁVEL'
    return n


resp = notas(3, 1, 10, 2, sit=True)
print(resp)