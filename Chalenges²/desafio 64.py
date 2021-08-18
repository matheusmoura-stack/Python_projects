n = 0
cont = 0
total = 0
print('\033[31mPara parar, digite "999"\033[m')
print('\033[32m¨`¨\033[m'*20)
while n != 999:
    n = int(input('Digite um número inteiro: '))
    if n != 999:
        cont += 1
        total = total + n
print('\033[32m¨`¨\033[m'*20)
print('Foram digitados {} números'.format(cont))
print('\033[32m¨`¨\033[m'*20)
print('Asoma dos {} números digitados, é: {} '.format(cont, total))
print('\033[32m¨`¨\033[m'*20)
print('\033[33mFIM!\033[m')