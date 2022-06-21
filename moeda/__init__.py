def aumentar (n, por):
    p = n * (por / 100)
    aumento = p + n
    return aumento


def metade (a):
    resultado = a / 2
    return resultado


def dobro (a):
    resultado = a * 2
    return resultado


def reduzir (a , b):
    p = a * (b / 100)
    redução = a - p
    return redução


def moeda (a = 0, moeda = 'R$'):
    return f'{moeda}{a:>.2f}'.replace('.', ',')
