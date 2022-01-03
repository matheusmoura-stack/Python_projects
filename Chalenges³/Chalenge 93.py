jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na {c+1}º partida? ')))
jogador['gols'] = partidas[:]
jogador['total de gols'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo "{k}" tem o valor {v}.')
print('-='*30)
print(f'O jogador: {jogador["nome"]} jogou {tot} partidas.')
for c in range(0, tot):
    print(f'  => Na partida {c+1}, fez {partidas[c]} gol(s). ')
print(f'Foi um total de {jogador["total de gols"]} gol(s).')
