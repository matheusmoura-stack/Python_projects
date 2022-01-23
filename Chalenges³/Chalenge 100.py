from random import randint
from time import sleep
print(f'Sorteando 5 valores na lista: ', end='')


def sorteia(lista):
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)


def SomaPar():
    soma = 0
    for i, v in enumerate(numeros):
        if v % 2 == 0:
            soma += v
    print(f'\nA soma entre os números pares da lista: {numeros} é : {soma}')


numeros = list()
sorteia(numeros)
SomaPar()
