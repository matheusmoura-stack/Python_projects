p = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão da P.A.: '))
cont = 1
termo = p
while cont <= 10:
    print('{}-> '.format(termo), end='')
    termo += r
    cont += 1
print('FIM!')
