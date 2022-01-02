from random import randint
sortiado = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), \
           randint(0, 10),
print('Os números sorteados foram:')
for n in sortiado:
    print(f'{n}', end=' ')
print(f'\nO maior número foi o {max(sortiado)}')
print(f'O menor número foi o {min(sortiado)}')