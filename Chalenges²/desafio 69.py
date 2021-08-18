c = 1
homens = cont = mulheres = 0
print('\033[31mCADASTRO DE PESSOAS\033[m')
print('')
while True:
    print('='*30)
    i = int(input(f'Digite a idade da {c}º pessoa: '))
    s = ' '
    while s not in 'MF':
        s = str(input(f'Digite o sexo da {c}º pessoa [F/M]: ')).upper()
    c += 1
    if i >= 18:
        cont += 1
    if s in 'Mm':
        homens += 1
    if s in 'Ff' and i < 20:
        mulheres += 1
    print('='*30)
    usuario = ' '
    while usuario not in 'SN':
        usuario = str(input('Quer continuar? [S/N]: ')).upper()
    if usuario == 'N':
        break
print('')
print(f'{cont} pessoa(s) têm mais de 18 anos;')
print(f'No total, Foi(ram) cadastrado(s) {homens} homem(s);')
print(f'{mulheres} mulhere(s) pussuí(em) menos de 20 anos.')
