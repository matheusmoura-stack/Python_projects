p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da P.A.: '))
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print('{}-> '.format(p), end='')
        p += r
        cont += 1
    print('Pause')
    mais = int(input('Você quer que mostre mais quantos termos? '))
print('Fim')
