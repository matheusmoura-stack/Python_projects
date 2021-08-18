from random import randint
from time import sleep
n3 = randint(0, 10)
cont = 0
print('\033[31m=-=\033[m' * 19)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('\033[31m=-=\033[m' * 19)
acertou = False
while not acertou:
    cont += 1
    num = int(input('Em que número eu pensei? '))
    if num == n3:
        acertou = True
    else:
        print('Você errou, tente novamente!')
print('Você acertou com {} tentativas. Boa!'.format(cont))




