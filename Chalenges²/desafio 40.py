nota = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
m = (nota+nota2)/2
if m < 5.0:
    print('Sua média, {:.1f}, está abaixo de 5,0.'.format(m), end='')
    print(' Sendo assim, Você está \033[1;30mREPROVADO\033m!!!')
elif 5.0 < m < 6.9:
    print('Sua média {:.1f} está entre 5,0 e 6,9.'.format(m), end='')
    print(' Você está de \033[1;31mRECUPERAÇÃO\033[m!!')
elif m > 7:
    print('Sua média {:.1f} é maior que 7,0.'.format(m), end='')
    print(' Você está \033[1;34mAPROVADO\033[m')
else:
    print('Sua média é igual a {:.1f}.'.format(m), end='')
    print(' Você está \033[1;34mAPROVADO\033[m')