valores = list()
pares = list()
impares = list()
for c in range(0, 7):
    valores.append(int(input(f'Digite o {c + 1}º valor: ')))
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-='*35)
print(f'Os valores digitados em ordem crescente foram: {sorted(valores)}')
print(f'Os valres pares digitados são: {sorted(pares)}')
print(f'Os valores ímpares digitados são: {sorted(impares)}')