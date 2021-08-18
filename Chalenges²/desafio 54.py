from datetime import date
totmaior = 0
totmenor = 0
i = date.today().year
for ano in range(1, 8):
    id = int(input('Ano de nascença da {}º pessoa: '.format(ano)))
    idade = i-id
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('{} pessoas são maiores de 18 anos, e {} são de menores'.format(totmaior, totmenor))










