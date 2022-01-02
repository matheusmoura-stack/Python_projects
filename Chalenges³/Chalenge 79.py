valores = list()
while True:
    u = int(input('Digite um valor inteiro: '))
    usuario = ' '
    if u not in valores:
        valores.append(u)
    else:
        print('esse valor já foi digitado, tente novamente')
    while usuario not in 'SN':
        usuario = str(input('Quer continuar? [S/N]: ')).upper()
    if usuario == 'N':
        break
print(sorted(valores))
