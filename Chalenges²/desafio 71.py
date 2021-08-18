print('='*35)
print('{:^35}'.format('BANCO MOURINHA'))
print('='*35)
print('')
v = int(input('Qual o valor a ser sacado? R$'))
tot = v
cem = 100
cont = 0
while True:
    if tot >= cem:
        tot -= cem
        cont += 1
    else:
        if cont > 0:
            print(f'São {cont} cédulas de {cem}')
        if cem == 100:
            cem = 50
        elif cem == 50:
            cem = 20
        elif cem == 20:
            cem = 10
        elif cem == 10:
            cem = 1
        cont = 0
        if tot == 0:
            break
print('='*35)
print('Obrigado por fazer parte do banco MOURINHA, VOLTE SEMPRE!!')


