valores = [[], []]
valor = 0
for c in range(0, 7):
    valor = (int(input(f'Digite o {c + 1}º valor: ')))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
print('-='*35)
print(f'Os valores digitados em ordem crescente foram: {sorted(valores)}')
print(f'Os valres pares digitados são: {sorted(valores[0])}')
print(f'Os valores ímpares digitados são: {sorted(valores[1])}')