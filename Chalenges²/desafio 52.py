n = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end="")
print('\033[mO NÚMERO {} FOI DIVISÍVEL {} VEZES'.format(n, tot))
if tot == 2:
    print('E POR ISSO ELE É PRIMO!')
else:
    print('E POR ISSO ELE NÃO É PRIMO!')
