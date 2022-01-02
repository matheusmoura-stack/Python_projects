'''valores = [int(input('Digite o 1º valor: ')), int(input('Digite o 2º valor: ')), int(input('Digite o 3º valor: ')),
           int(input('Digite o 4º valor: ')), int(input('Digite o 5º valor: '))]
v = sorted(valores)
v1 = v[4:]
v2 = v[:1]
print(f'Valores digitados em ordem crescente: {v}')
print(f'O maior valor foi o: {max(valores)}')
print(f'O menor valor foi o: {min(valores)}')
for c in range(0, 1):
    for y, f in enumerate(valores):
        print(f'Na posição {y + 1} encontrei o valor {v1}')'''''

valores = []
mai = 0
men = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = valores[c]
    else:
        if valores[c] > mai:#  |
            mai = valores[c]#  | \
        if valores[c] < men:#  | / é uma opção viável de mostrar o maior e o meno número
            men = valores[c]#  |
print('=-' * 30)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor foi o: {mai} nas posições: ', end='') # \
for i, v in enumerate(valores):                    #  |
    if v == mai:                                   #  |
        print(f'{i}...', end='')                   #  |
print()                                            #  |
print(f'O menor valor foi o: {men} nas posições: ', end='') # / outra opção de mostrar o maior e o menor número
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}...', end='')
print()
