print('----------LOJA DE ELETRÔNICOS----------')
print('')
tot = mais = barato = cont = 0
n = ' '
while True:
    print('=' * 30)
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: R$'))
    tot += preco
    cont += 1
    print('='*30)
    r = ' '
    if preco > 1000:
        mais += 1
    if cont == 1:
        barato = preco
        n = nome
    else:
        if preco < barato:
            barato = preco
            n = nome
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]: ')).upper()
    if r == 'N':
        break
print(f'O total, em reais, de sua compra foi: R${tot:.2f}')
print(f'{mais} produtos passaram de R$1.000,00')
print(f'O produto mais barato foi o {n}, custando R${barato}')
