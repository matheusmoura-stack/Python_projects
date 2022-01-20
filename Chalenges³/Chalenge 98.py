from time import sleep


def contador(i, f, p):
    print('~' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    cont = i
    if i < f:
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
    else:
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
    print()
    if p == 0:
        p = 1
    if p < 0:
        p *= -1


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
print('~'*30)
ini = int(input('Início:  '))
fim = int(input('Fim:     '))
pas = int(input('Passo:   '))
contador(ini, fim, pas)
