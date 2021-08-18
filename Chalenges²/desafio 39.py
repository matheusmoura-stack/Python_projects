from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
a = date.today().year
idade = a-ano
if idade < 18:
    saldo = 18 - idade
    print('Você deve se alistar quando completar 18, ainda faltam {} anos'.format(saldo))
    ano1 = saldo + a
    print('Você terá de se alistar em {}'.format(ano1))
elif idade == 18:
    print('Este é o ano de se alistar')
else:
    saldo = idade - 18
    print('Já se passou o seu tempo de alistamento. Passaram-se {} anos'.format(saldo))
    ano1 = a - saldo
    print('Você deveria ter se alistado em {}'.format(ano1))
