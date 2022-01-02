palavras = 'tomate', 'canada', 'python', 'udem', 'estudar', 'programacao', 'goiaba'
for n in palavras:
    print(f'\nNa palavra \033[1;31m{n.upper()}\033[m temos: ', end='')
    for letras in n:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')

