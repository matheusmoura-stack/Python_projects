jogador1 = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na {c+1}º partida? ')))
    jogador['gols'] = partidas[:]
    jogador['total de gols'] = sum(partidas)
    jogador1.append(jogador.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N]: ')).upper()
        print('=-'*30)
        if resposta in 'SN':
            break
    if resposta == 'N':
        break
print()
print(f'{"No.":<4}{"NOME":<10}{"GOLS":>9}{"TOTAL":>13}')
print('_'*37)
for k, v in enumerate(jogador1):
    print(f'{k+1:<4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('_'*37)
while True:
    resposta2 = int(input('Quer mostrar os dados de qual jogador? (999 interrompe): '))
    if resposta2 == 999:
        break
    if resposta2 >= len(jogador1):
        print('Erro... não existe jogador com esse código')
    else:
        print(F'-- LEVANTANDO DADOS DO JOGADOR {jogador1[resposta2]["nome"]}:')
        for i, g in enumerate(jogador1[resposta2]['gols']):
            print(f'    No jogo {i} fez {g} gols.')
    print('-'*40)
print('VOLTE SEMPRE!')