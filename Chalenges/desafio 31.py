dist = float(input('A distância da viagem é de: '))
if dist <= 200:
    print('O valor da viagem ficou {}R$'.format((dist * 0.5)))
else:
    print('O valor da viagem ficou {}R$'.format(dist * 0.45))
