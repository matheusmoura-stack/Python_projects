from datetime import date
year = date.today().year
print('\033[31mA CNN (Confraternização Nacional de Natação), necessita de alguns documentos para fechar o cadastro, ', end='')
print('dentre elas, o ano de nascimento do candidato.\033[m')
nas = int(input('Insira seu ano de nascimento para determinar sua categoria de acordo com sua idade: '))
i = year - nas
if 0 < i <= 9:
    print('A idade "{}" inserida, entra na nossa categoria \033[32;4mMIRIN\033[m'.format(i))
elif 9 < i <= 14:
    print('A idade "{}" inserida, corresponde a categoria \033[34;4mINFANTIL\033[m'.format(i))
elif 14 < i <= 19:
    print('A idade inserida, "{}", corresponde a categoria \033[36;4mJUNIOR\033[m'.format(i))
elif i == 20:
    print('A idade correspondida a "{}", se refere à categoria \033[35;4mSÊNIOR\033[m'.format(i))
else:
    print('A idade "{}", inserida, corresponde à categoria \033[33;4mMASTER\033[m'.format(i))
