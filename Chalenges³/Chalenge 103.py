def ficha(n='<desconhecido>', g=0):
    print(f'O jogador {n}, fez {g} gol(s)')


print('~' * 30)
nome = str(input('Nome do jogador: ')).capitalize()
gols = str(input(f'Número de gols de {nome}: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)
