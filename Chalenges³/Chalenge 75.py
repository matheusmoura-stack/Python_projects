n = int(input('Digite o 1º número: ')), int(input('Digite o 2º número: ')), \
    int(input('Digite o 3º número: ')), int(input('Digite o 4º número: '))
print(f'Os valores digitados foram: ')
for c in n:
    print(f'{c}', end=' ')
print('')
print('=-'*20)
print(f'O número 9 apareceu {n.count(9)} vezes')
print('=-'*20)
if 3 in n:
    print(f'O primeiro número 3 está na posição {n.index(3)+1}')
else:
    print('O número 3 não foi digitado em nenhuma posição')
print('=-'*20)
print(f'os números pares digitados foram: ')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')

