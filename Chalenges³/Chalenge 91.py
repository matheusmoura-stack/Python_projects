from random import randint
from time import sleep
from operator import itemgetter
print('JOGO DO DADO')
print()
print('REGRAS:\n'
      'QUEM TIRAR O MAIOR NÚMERO GANHA!!')
print()
print('1')
sleep(1)
print('2')
sleep(1)
print('3')
sleep(1)
print('VAI!')
jogadores = dict()
jogadores['jogador1'] = randint(1, 6)
jogadores['jogador2'] = randint(1, 6)
jogadores['jogador3'] = randint(1, 6)
jogadores['jogador4'] = randint(1, 6)
ranking = list()
for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
print('-='*25)
print('   == RANKING DOS JOGADORES == ')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-='*25)
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)

