p = float(input('Preço das compras: '))
d = p * 0.1
d2 = p * 0.05
ju = p * 0.2
ju2 = p + ju
di = p - d
ca = p - d2
print('\nOPÇÕES DE PAGAMENTO:\n \n - Dinheiro/cheque\033[1;31m (10% de desconto)\033[m - OPÇÃO [1]')
print(' - Cartão à vista \033[1;31m(5% de desconto)\033[m - OPÇÃO [2]\n - 2x no cartão', end='')
print(' \033[1;31m(preço normal)\033[m - OPÇÃO [3]')
print(' - 3x ou mais no cartão \033[1;31m(juros de 20%)\033[m - OPÇÃO [4]\n')
r = int(input('Escolha a opção de pagamento: '))
if r == 1:
    print('O valor do objeto (R${}) passou a custar R${} com os 10% '.format(p, di), end='')
    print('de desconto pagando à vista no dinheiro/cheque.')
elif r == 2:
    print('O valor do objeto (R${}) passou a custar R${} com os 5% '.format(p, ca), end='')
    print('de desconto pagando à vista no cartão.')
elif r == 3:
    print('O valor a pagar continua o mesmo do produto(R${}) utilizando até 2x no cartão.'.format(p))
elif r == 4:
    n = int(input('Quantas parcelas? '))
    parcela = ju2 / n
    print('Pagando em {}x, o valor mensal será de R${:.2f} '.format(n, parcela))
    print('E o valor R${} passará a custar RS${:.2f}'.format(p, ju2))

