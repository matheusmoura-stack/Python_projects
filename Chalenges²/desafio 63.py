n = int(input('Quantos termos você quer mostrar na sequência de fibonacci?? '))
termo = 0
termo2 = 1
print('-_'*25)
print('{}-> {}-> '.format(termo, termo2), end='')
cont = 3
while cont <= n:
    termo3 = termo + termo2
    print('{}-> '.format(termo3), end='')
    termo = termo2
    termo2 = termo3
    cont += 1
print('Fim')
print('-_'*25)

