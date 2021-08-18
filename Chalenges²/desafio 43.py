p = float(input('Digite seu peso: '))
h = float(input('Digite sua altura: '))
imc = p / h ** 2
if imc <= 18.5:
    print('O seu status, a partir do seu imc ({:.1f}), é \033[1;34mABAIXO DO PESO\033[m, '.format(imc), end='')
    print('ou seja, está abaixo de 18,5.')
elif imc <= 25:
    print('O status de acordo com o seu imc ({:.1f}), é \033[1;32mPESO IDEAL\033[m!'.format(imc), end='')
    print(' Pois está entre 18,5 e 25.')
elif imc <= 30:
    print('O status de acordo com o seu imc ({:.1f}), é \033[1;33mSOBREPESO\033[m'.format(imc), end='')
    print(' por ser entre 25 e 30.')
elif imc <= 40:
    print('O status de acordo com o seu imc ({:.1f}), é \033[1;31mOBESIDADE\033[m'.format(imc), end='')
    print(' por ser entre 30 e 40.')
else:
    print('O status de acordo com o seu imc ({:.1f}), é \033[30mOBESIDADE MÓRBIDA\033[m'.format(imc), end='')
    print(' pois o seu imc ultrapassa 40.')
