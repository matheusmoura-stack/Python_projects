'''n = int(input('Digite um número para ver sua tabuada: '))
for n1 in range(1, 11):
    for c in range(1):
        result = n * n1
        print('{} x {} = {} '.format(n, n1, result))'''

'''OU...'''

num = int(input('Digite um valor para ver sua tabuada: '))
print('=-' * 6)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
print('=-' * 6)


