p = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão da P.A.: '))
cont = 1
termo = p
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}-> '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSE')
    mais = int(input('Você quer que mostre mais quantos termos? '))
print('FIM')

