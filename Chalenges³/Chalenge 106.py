from time import sleep


def lin3(txt):
    print('\033[30;41m~' * len(txt))
    print(f' {txt}')
    print('~' * len(txt))


def lin2(txt):
    print('\033[30;46m')


def lin(txt):
    print('\033[30;42m=-' * len(txt))
    print(f' {txt}')
    print('=-' * len(txt))


def man(a):
    while True:
        sleep(0.5)
        lin3(f'ACESSANDO O MANUAL DO COMANDO {f}'.upper())
        sleep(0.5)
        lin2('')
        help(f)
        break


f = ' '
while True:
    lin(f'SISTEMA DE AJUDA PyHELP')
    f = input('\033[mDigite a biblioteca ou função > ')
    if f.upper() == 'FIM':
        lin3('ATÉ LOGO!')
        break
    else:
        man(f)
