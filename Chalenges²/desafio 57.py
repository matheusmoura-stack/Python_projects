s = str(input('Digite seu sexo [F/M]: ')).upper().strip()
while s not in 'MmFf':
    s = str(input('Digite um valor válido: ')).upper().strip()
print('sexo {} validado com sucesso!'.format(s))

