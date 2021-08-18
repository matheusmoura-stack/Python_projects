from math import radians, sin, cos, tan
an = float(input('Digite um ângulo: '))
sen = sin(radians(an))
co = cos(radians(an))
tg = tan(radians(an))

print(' O seno de {}º vale {:.2f} \n O cosseno vale {:.2f} \n E a tangente vale {:.2f}'.format(an, sen, co, tg))
