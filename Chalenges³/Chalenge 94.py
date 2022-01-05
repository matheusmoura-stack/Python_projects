media = soma = 0
pessoas2 = list()
pessoas = dict()
mulheres = list()
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: ')).title()
    while True:
        pessoas['sexo'] = str(input(f"Sexo de {pessoas['nome']} (F/M): ")).upper()
        if pessoas['sexo'] in 'MF':
            break
    pessoas['idade'] = int(input(f'Idade de {pessoas["nome"]}: '))
    soma += pessoas['idade']
    pessoas2.append(pessoas.copy())
    resposta = str(input('Quer continuar? [S/N]: ')).upper()
    print('-'*50)
    if resposta in 'Nn':
        break
print()
print(f'Foram cadastradas: {len(pessoas2)} pessoas.')
print('=-'*20)
media = soma / len(pessoas2)
print(f'A média de idade das pessoas é: {media:.1f}')
print('=-'*20)
print(f'lista de todas as mulheres:' )
for v in mulheres:
    print(f'{v}')
print('=-'*20)
print('pessoas acima da média de idade: ')
for p in pessoas2:
    if p['idade'] >= media:
        print('  ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print()


