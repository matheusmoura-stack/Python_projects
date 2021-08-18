from random import randint
from time import sleep
cont = 0
print('')
print('*-'*20)
print('      VAMOS JOGAR PAR OU ÍMPAR!!')
print('*-'*20)
print('')
while True:
    cont += 1
    maquina = randint(0, 11)
    jogador = int(input('Digite um valor: '))
    pi = str(input('Par ou ímpar? (P/I) ').upper())
    print('Processando...')
    sleep(1)
    resultado = jogador + maquina
    print('=-'*20)
    if resultado % 2 == 0:
        if pi in 'Pp':
            print(f'A soma entre {maquina} (o que eu escolhi) e {jogador} (o que você escolheu) ', end='')
            print(f'Deu {resultado} coincidindo com a sua escolha (par)')
            print(f'Você ganhou com \033[31m{cont}\033[m tentativas')
            print('\033[35mFIM DO JOGO\033[m')
            break
        else:
            print(f'Você perdeu, pois eu escolhi {maquina} e você {jogador}. ', end='')
            print(f'A soma entre eles ({resultado}) é par e você escolheu ímpar. Tente novamente!!')
    else:
        if pi in 'Ii':
            print(f'A soma entre {maquina} (o que eu escolhi) e {jogador} (o que você escolheu) ', end='')
            print(f'Deu {resultado} coincidindo com a sua escolha (ímpar)')
            print(f'Você ganhou com \033[31m{cont}\033[m tentativas')
            print('\033[35mFIM DO JOGO\033[m')
            break
        else:
            print(f'Você perdeu, pois eu escolhi {maquina} e você {jogador}. ', end='')
            print(f'A soma entre eles ({resultado}) é ímpar e você escolheu par. Tente novamente!!')
    print('=-' * 20)
