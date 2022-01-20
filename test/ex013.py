jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    resposta = str(input('Quer continuar? [S/N]: ')).upper()
    print('=-'*30)
    partidas.append(jogador.copy())
    if resposta in 'Nn':
        break
print(partidas)