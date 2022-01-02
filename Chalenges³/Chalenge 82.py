cont = 0
valores = list()
pares = list()
impares = list()
while True:
    valores.append(int(input('Digite um número inteiro: ')))
    usuario = ' '
    cont += 1
    while usuario not in 'SN':
        usuario = str(input('Quer continuar? [S/N]: ')).upper()
    if usuario == 'N':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista completa é: {valores}')
print(f'Os valores pares são: {pares}')
print(f'Os valores ímpares são: {impares}')


