s = c = n = 0
while True:
    n = int(input('Digite um valor (digite 999 para parar): '))
    if n != 999:
        s += n
        c += 1
    elif n == 999:
            break
print(f'Os {c} valores digitados têm sua sumatória igual a: {s} ')

