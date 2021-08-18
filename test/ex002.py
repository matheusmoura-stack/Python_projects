algo = input('Digite algo: ')
print('O tipo primitivo de {}, é: '.format(algo), type(algo))
print('{} É um número?: '.format(algo), algo.isnumeric())
print('{} É uma alfabético?: '.format(algo), algo.isalpha())
print('{} É alfanumérico?: '.format(algo), algo.isalnum())
print('{} Está maiúsculo?: '.format(algo), algo.isupper())
print('{} Está minúsculo?: '.format(algo), algo.islower())
print('{} Está capitalizada?: '.format(algo), algo.istitle())
print('{} Só tem espaços?: '.format(algo), algo.isspace())






















