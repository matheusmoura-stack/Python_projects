from random import randint
from time import sleep
print('\033[1;31m-=\033[m' * 25)
print('\033[1;34m             VAMOS JOGAR UM JOGO!!\033[m')
print('\033[1;31m=-\033[m' * 25)
print('')
print('ELE SE CHAMA \033[1;32mJOKEMPÔ\033[m')
print('')
print('COMO JOGAR:\n'
      '- ESCOLHA ENTRE: \n PEDRA -   [ 0 ] \n PAPEL -   [ 1 ] \n TESOURA - [ 2 ]\n'
      '- O COMPUTADOR ESCOLHERÁ ALEATORIAMENTE TAMBÉM!')
print('')
print('\033[1;36mREGRAS\033[m: ')
print('- PEDRA GANHA DE TESOURA MAS PERDE PARA O PAPEL;')
print('- TESOURA PERDE PARA PAPEL.')
print('')
jogador = int(input('Faça sua escolha: '))
computador = randint(0, 2)
opcoes = ('pedra', 'papel', 'tesoura')
print('')
print('CARREGANDO RESULTADOS...')
print('')
sleep(1)
print('\033[1;35mJO\033[m')
sleep(1)
print('\033[1;35mKEM\033[m')
sleep(1)
print('\033[1;35mPÔ\033[m')
print('')
print('O jogador escolheu: \033[1;33m{}\033[m'.format(opcoes[jogador]))
print('O computador escolheu \033[1;33m{}\033[m'. format(opcoes[computador]))
print('')
sleep(3)
if computador == 0:
    if jogador == 0:
        print('EMPATAMOS! ESCOLHEMOS AS MESMAS OPÇÕES.')
        print('VAMOS! TENTE NOVAMENTE!')
    elif jogador == 1:
        print('DROGA, VOCÊ ME VENCEU! \nVAMOS JOGAR NOVAMENTE!')
    elif jogador == 2:
        print('EU VENCI!! HAHAHAHA, TENTE NOVAMENTE!')
    else:
        print('ESCOLHA INVÁLIDA, TENTE NOVAMENTE!')
elif computador == 1:
    if jogador == 0:
        print('EU VENCI!! HAHAHAHA, TENTE NOVAMENTE!')
    elif jogador == 1:
        print('EMPATAMOS! ESCOLHEMOS AS MESMAS OPÇÕES.')
        print('VAMOS! TENTE NOVAMENTE!!')
    elif jogador == 2:
        print('DROGA, VOCÊ ME VENCEU! \nVAMOS JOGAR NOVAMENTE!')
    else:
        print('ESCOLHA INVÁLIDA, TENTE NOVAMENTE!')
elif computador == 2:
    if jogador == 0:
        print('DROGA, VOCÊ ME VENCEU! \nVAMOS JOGAR NOVAMENTE!')
    elif jogador == 1:
        print('EU VENCI!! HAHAHAHA, TENTE NOVAMENTE!')
    elif jogador == 2:
        print('EMPATAMOS! ESCOLHEMOS AS MESMAS OPÇÕES.')
        print('VAMOS! TENTE NOVAMENTE!!')
    else:
        print('ESCOLHA INVÁLIDA, TENTE NOVAMENTE!')
else:
    print('JOGADA INVÁLIDA, TENTE NOVAMENTE!!')



