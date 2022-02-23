def leiaint(a):
    ok = False
    valor = 0
    while True:
        n = str(input(a))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido!\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}')