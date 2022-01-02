from random import randint
from time import sleep
print('=-'*20)
n = 'JOGA NA MEGA SENA'
print(f'{n:^40}')
print('=-'*20)
n = (int(input('Quantos jogos você quer que eu sorteie? ')))
lista = list()
jogos = list()
tot = 1
while tot <= n:
    cont = 0
    while True:
        pc = randint(1, 60)
        if pc not in lista:
            lista.append(pc)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print()
print('=-' * 3, f'SORTEANDO {n} JOGOS' , '=-' * 3 )
sleep(1)
for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i+1}: {l}')


