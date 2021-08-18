from time import sleep
n = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
soma = n + n2
multiplicação = n * n2
opção = 0
while opção != 5:
    opção = int(input('Escolha entre: \n[ 1 ] Somar \n[ 2 ] Multiplicar \n[ 3 ] Maior \n[ 4 ] Novos números \n[ 5 ] Sair do programa \n'))
    if opção == 1:
        print('A soma entre {} e {}, é igual a: {} '.format(n, n2, soma))
        sleep(1)
        print('\033[31m-=\033[m'*19)
    elif opção == 2:
        print('A multiplicação entre {} e {}, é igual a: {} '.format(n, n2, multiplicação))
        sleep(1)
        print('\033[31m-=\033[m'*19)
    elif opção == 3:
        if n > n2:
            print('O maior número entre {} e {}, é o {}'.format(n, n2, n))
            sleep(1)
            print('\033[31m-=\033[m'*19)
        else:
            print('O maior número entre {} e {}, é o {}'.format(n, n2, n2))
            sleep(1)
            print('\033[31m-=\033[m'*19)
    elif opção == 4:
        n = int(input('Digite o primeiro novo número: '))
        n2 = int(input('Digite o segundo novo número: '))
        sleep(1)
        print('\033[31m-=\033[m'*19)
    elif opção == 5:
        print('Obrigado por jogar!')
    else:
        print('Digite um valor válido, por favor.')
print('Até mais!')