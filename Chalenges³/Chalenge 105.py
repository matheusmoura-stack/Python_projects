def notas(*num,  sit=False):
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