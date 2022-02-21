def fatorial(a, show=False):
    """
    -> fatorial de um número determinado com funções!
    :param a: valor a ser calculado.
    :param show: (opcional) mostrar o processo de cálculo.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    print(f'Calculando o fatorial de {a}! = ', end='')
    for c in range(a, 0, -1):
        if show:
            print(f'{a}', end='')
            print(' x ' if a > 1 else ' = ', end='')
        a -= 1
        f *= c
    return f


help(fatorial)
print(fatorial(10, show=True))
