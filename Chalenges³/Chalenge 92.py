
perfil = dict()
perfil['nome'] = str(input('Nome: '))
perfil['nascimento'] = int(input(f'Ano de nascimento de {perfil["nome"]}: '))
perfil['Carteira'] = int(input(f'Carteira de trabalho de {perfil["nome"]} (0 não tem): '))
if perfil['Carteira'] != 0:
    perfil['ano'] = int(input(f'Ano de contratação: '))
    perfil['salário'] = float(input(f'Salário: '))
    for k, v in perfil.items():
        print(f'{k} tem valor {v}')
else:
    for k, v in perfil.items():
        print(f'{k} tem valor {v}')