valores = list()
for c in range(0, 5):
    n = int(input('Digite um Valor: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem, são: {valores}')
