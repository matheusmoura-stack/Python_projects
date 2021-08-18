frase = input('Digite uma frase: ').strip().upper()
p = frase.split()
j = ''.join(p)
i = j[::-1]
if i == j:
    print('{} é igual ao inverso de {}, ou seja, É UM PALÍNDROMO!'.format(i, j))
else:
    print('Não é um palíndromo, pois o inverso de {} é {} e eles não são iguais.'.format(j, i))


