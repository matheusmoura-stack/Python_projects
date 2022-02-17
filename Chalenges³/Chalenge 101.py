def voto(ano=0):
    from datetime import date
    year = date.today().year
    idade = year - ano
    if idade >= 65:
        return f'com {idade} anos, o voto é \033[1;34mOPCIONAL'
    elif idade >= 18:
        return f"Com {idade} anos, o voto é \033[1;31mOBRIGATÓRIO\033[m"
    else:
        return f'Com {idade} anos, \033[1;33mNÃO VOTA\033[m'


print('~'*35)
an = int(input('Em que ano você nasceu? '))
print(voto(an))

