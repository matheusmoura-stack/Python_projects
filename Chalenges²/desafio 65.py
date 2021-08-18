sim = 'S'
soma = cont = maior = menor = 0
while sim == 'S':
    n = int(input('Digite um valor: '))
    cont += 1
    sim = str(input('Você quer continuar? [S/N] ')).upper().strip()
    soma += n
    media = soma / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('A média dos números digitados é igual a: {:.2f}'.format(media))
print('O maior número foi o {}'.format(maior))
print('O menor número foi o {}'.format(menor))
