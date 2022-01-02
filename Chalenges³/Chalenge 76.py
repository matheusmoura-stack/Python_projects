listagem = ('Agulha', 0.25, 'Pão', 5, 'Almofada', 32, 'Sapato', 367.90, 'Alexa', 259.90, 'Lápis', 2.50)
print('---'*15)
print("             LISTAGEM DE PREÇOS")
print('---'*15)
for n in range(0, len(listagem)):
    if n % 2 == 0:
        print(f'{listagem[n]:.<36}', end='')
    else:
        print(f'R${listagem[n]:>7.2f}')
print('---'*15)
