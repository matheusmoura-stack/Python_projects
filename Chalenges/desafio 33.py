n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
menor = n2
if n1<n2 and n1<n3:
    menor = n1
if n3<n2 and n3<n1:
    menor = n3
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('o maior número é o {}'.format(maior))
print('O menor número é o {}'.format(menor))