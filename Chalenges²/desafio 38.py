n = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
if n > n2:
    print('O valor {} é o \033[4;34mMAIOR\033[m número!'.format(n))
elif n2 > n:
    print('O valor {} é o \033[4;34mMAIOR\033[m número!'.format(n2))
else:
    print('Não existe valor maior, os dois números são \033[1;31mIGUAIS\033[m!!')