a = float(input('Digite o comprimento da 1º reta: '))
b = float(input('Digite o comprimento da 2º reta: '))
c = float(input('Digite o comprimento da 3º reta: '))
if b+c > a > b//c:
    print('Com as medidas "{}m", "{}m" e "{}m" selecionadas, '.format(a, b, c), end='')
    print('podemos constituir um triângulo de acordo com a condição de existência.')
    print('')
    if a == b == c:
        print('Este é um triângulo \033[4;34mEQUILÁTERO\033[m!!, por possui todos os lados "{}", "{}" e "{}" iguais.'.format(a, b, c))
    elif a == b or b == c or c == a:
        print('As medidas "{}", "{}" e "{}" formam um triângulo \033[4;31mISÓCELES\033[m, '.format(a, b, c), end='')
        print('pois das 3 medidas, 2 delas são iguais!')
    else:
        print('todos os lados "{}", "{}" e "{}" possuem medidas diferentes uns dos outros, '.format(a, b, c), end='')
        print('portanto eles formam um triângulo \033[4;36mESCALENO\033[m!!')
else:
    print('Com essas medidas é impossível formar um triângulo!')
