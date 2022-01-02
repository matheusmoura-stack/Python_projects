ficha = list()
cont = 0
while True:
    nome = str(input('Nome: '))
    cont += 1
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input('Quer continuar? [S/N]: ')).upper()
    if resposta in 'Nn':
        break
print('=-'*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for n, i in enumerate(ficha):
    print(f'{n:<4}{i[0]:<10}{i[2]:>8.1f}')
print('-'*26)
while True:
    resposta2 = int(input('Quer mostrar as notas de qual aluno? (999 interrompe): '))
    print('-' * 36)
    if resposta2 <= len(ficha) - 1:
        print(f'Notas de {ficha[resposta2] [0]} são: {ficha[resposta2][1]}')
    if resposta2 == 999:
        print('Finalizando...')
        break