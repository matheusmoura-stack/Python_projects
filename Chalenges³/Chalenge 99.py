from time import sleep


def maior(*num):
    cont = maior2 = 0
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', flush=True, end=' ')
        sleep(0.3)
        if cont == 0:
            maior2 = valor
        else:
            if valor > maior2:
                maior2 = valor
        cont += 1
    print()
    print(f'Foram digitados um total de {len(num)} números.')
    # print(f'o maior valor digitado foi {max(num)}.')
    # ou a opção de cima
    print(f'O maior valor digitado foi {maior2}.')
    print('~' * 45)


# programa principal
maior(4, 6, 8, 1, 7, 10)
maior(4, 3, 7, 2)
maior(0)
maior(2, 1)
