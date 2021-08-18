ano = int(input('Digite um ano: '))
if ano % 100 !=0 and ano %4 ==0 or ano % 400 ==0:
    print('O ano {} informado é bissexto'.format(ano))
else:
    print('O ano {} informado não é bissexto.'.format(ano))

