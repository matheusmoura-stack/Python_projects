dados = []
galera = []
cont = mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    cont += 1
    dados.append(float(input('Peso: ')))
    if len(galera) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    galera.append(dados[:])
    dados.clear()
    resposta = str(input('Quer continuar? [S/N]: ')).upper()
    if resposta in 'Nn':
        break
print('=-'*30)
print(f'Os dados foram: {galera}')
print('=-'*30)
print(f'Foram cadastradas {cont} pessoas.')
print(f'O maior peso foi de {mai}Kg, de: ', end='')
for p in galera:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg, de: ', end='')
for p in galera:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')