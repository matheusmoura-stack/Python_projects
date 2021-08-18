soma = 0
maior = 0
media = 0
nome = ''
cont = 0
for c in range(1, 5):
    n = input('Digite o nome da {}º pessoa: '.format(c))
    i = float(input('Digite a idade de {}: '.format(n)))
    s = input('Digite o sexo de {} [M/F]: '.format(n))
    print('\033[1;31m-=\033[m'*18)
    soma += i
    media = soma / c
    if c == 1 and s in 'Mm':
        maior = i
        nome = n
    else:
        if i > maior and n > nome:
            maior = i
            nome = n
    if i < 20 and s in 'fF':
        cont += 1
print('A média de idade entre as 4 pessoas foi de {:.2f} anos'.format(media))
print('{} é o homem mais velho, possuindo {} anos.'.format(nome, maior))
print('{} mulheres tem menos de 20 anos'.format(cont))


