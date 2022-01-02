from datetime import date
perfil = dict()
perfil['nome'] = str(input('Nome: ')).capitalize()
perfil['nascimento'] = int(input(f'Ano de nascimento de {perfil["nome"]}: '))
year = date.today().year
idade = year - perfil['nascimento']
perfil.copy()
del(perfil['nascimento'])
perfil['idade'] = idade
perfil['Ctps'] = int(input(f'Carteira de trabalho de {perfil["nome"]} (0 não tem): '))
if perfil['Ctps'] != 0:
    perfil['contratação'] = int(input(f'Ano de contratação: '))
    anoi = year - perfil['contratação']
    if anoi >= 35:
        perfil['aposentadoria'] = 'aposentado'
    else:
        resultado = 35 - anoi
        perfil['aposentadoria'] = resultado + idade
    perfil['salário'] = float(input(f'Salário: '))
    print('-=' * 30)
for k, v in perfil.items():
    print(f'    - {k} tem valor: {v}')
