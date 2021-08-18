n = c = 0
tot = 10
while c < 10:
    n = int(input('Quer ver a tabuada de qual valor? '))
    c += 1
    if n > 0:
        print('\033[35m.\033[m' * 20)
        for cu in range(1, 11):
            r = n * cu
            print(f'{n} X {cu} = {r}')
        print('\033[35m.\033[m' * 20)
    elif n < 0:
        print('Programa "\033[31mTABUADA\033[m" foi encerrado. Volte sempre!!', end='')
        break
