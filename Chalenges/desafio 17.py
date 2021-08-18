'''co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjascente: '))
hp = (co**2 + ca**2)**(1/2)
print('O valor da hipotenusa é: {:.2f} '.format(hp))'''


import math
co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjascente: '))
hip = math.hypot(co, ca)
print('A hipotenusa vale {}'.format(hip))