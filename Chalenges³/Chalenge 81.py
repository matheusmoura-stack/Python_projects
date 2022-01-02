cont = 0
valores = list()
while True:
    valores.append(int(input('Digite um valor inteiro: ')))
    usuario = ' '
    cont += 1
    while usuario not in 'SN':
        usuario = str(input('Quer continuar? [S/N]: ')).upper()
    if usuario == 'N':
        break
print('=-'*30)
print(f'lista: {valores}')
print(f'Foram digitados {cont} números')
print(f'A lista em ordem decrescente: {sorted(valores, reverse=True)}')
if 5 in valores:
    print('O valor "5" está na lista!')
else:
    print('O valor "5" não faz parte da lista')